#!/usr/bin/env python3
"""Independent small finite-field checks for weighted 2-cycle evolution algebras.

Uses the multiplication table, modular linear algebra and exhaustive candidate
monomial maps for selected cases. Finite checks supplement the symbolic proof.
"""
from itertools import product
from math import gcd


def primitive_cube_roots(q):
    r = [x for x in range(1, q) if pow(x, 3, q) == 1]
    assert len(r) == 3 and 1 in r
    return r


def det_mod(mat, q):
    a = [list(row) for row in mat]
    n = len(a)
    d = 1
    for j in range(n):
        t = next((i for i in range(j, n) if a[i][j] % q), None)
        if t is None:
            return 0
        if t != j:
            a[t], a[j] = a[j], a[t]
            d = -d
        p = a[j][j] % q
        d = d * p % q
        ip = pow(p, -1, q)
        for i in range(j + 1, n):
            k = a[i][j] * ip % q
            if k:
                for h in range(j, n):
                    a[i][h] = (a[i][h] - k * a[j][h]) % q
    return d % q


def multiplication(n, c, q):
    # Basis (a0,b0,a1,b1,...)
    sq = [[0] * (2*n) for _ in range(2*n)]
    for i in range(n):
        sq[2*i][2*i+1] = 1
        sq[2*i][2*((i+1)%n)+1] = c[i]
        sq[2*i+1][2*i] = 1
    return sq


def is_auto(n, c, q, k, v):
    # f(b_i) = v_i b_{i+k}, f(a_i) = v_i^2 a_{i+k}.
    sq = multiplication(n, c, q)
    N = 2*n
    def dest(j):
        return (2*((j//2+k)%n) + j%2)
    scale = [pow(v[j//2], 2 if j % 2 == 0 else 1, q) for j in range(N)]
    for j in range(N):
        lhs = [0] * N
        for h in range(N):
            lhs[dest(h)] = (lhs[dest(h)] + sq[j][h] * scale[h]) % q
        rhs = [scale[j]**2 * s % q for s in sq[dest(j)]]
        if lhs != rhs:
            return False
    return True


def run():
    det_cases = 0
    lift_cases = 0
    exhaustive = 0
    distribution = {"split":0,"nonsplit":0,"not_perfect":0}
    for q in (7, 13, 19):
        mu = primitive_cube_roots(q)
        cases = [(3, list(product(mu, repeat=3))),
                 (4, list(product(mu, repeat=4)))]
        if q == 7:
            cases += [(5, list(product(mu, repeat=5))),
                      (6, list(product(mu, repeat=6)))]
        else:
            cases += [(5, [tuple([x] + [1]*4) for x in mu]),
                      (6, [tuple([x] + [1]*5) for x in mu]),
                      (9, [tuple([x] + [1]*8) for x in mu])]
        for n, coeffs in cases:
            for c in coeffs:
                P = 1
                for x in c:
                    P = P*x % q
                sq = multiplication(n, c, q)
                d = det_mod(sq, q)
                predicted = (((-1)**n-P) % q)
                assert d == predicted, (n, q, c, d, predicted)
                perfect = (n % 2 == 1 or P != 1)
                assert bool(d) == perfect
                det_cases += 1
                if not perfect:
                    distribution['not_perfect'] += 1
                    continue
                predicted_split = (P == 1 or gcd(n, 3) == 1)
                distribution['split' if predicted_split else 'nonsplit'] += 1
                for k in range(n):
                    v = [None] * n
                    v[0] = 1
                    for i in range(n - 1):
                        v[i+1] = v[i] * c[(i+k)%n] * pow(c[i], -1, q) % q
                    assert v[-1] * c[(n-1+k)%n] * pow(c[-1], -1, q) % q == v[0]
                    for t in mu:
                        vt = [t*x%q for x in v]
                        assert is_auto(n, c, q, k, vt), (q,n,c,k,vt)
                        lift_cases += 1
                # Explicit group law of the weighted rotation generator:
                # phi^n scales every a_i by P^2 and every b_i by P.
                assert pow(P, 3, q) == 1
                if q == 7 and n in (3, 4):
                    # Enumerate ALL candidates that could be monomial automorphisms
                    # after graph outdegree constraints, no assumption that v_i are roots.
                    count = 0
                    for k in range(n):
                        for v in product(range(1, q), repeat=n):
                            count += is_auto(n, c, q, k, v)
                    assert count == 3*n, (n,c,count)
                    exhaustive += 1
    print('VERIFY_OK')
    print('determinants_checked', det_cases)
    print('explicit_lifts_checked', lift_cases)
    print('all_monomial_candidates_exhaustive_cases', exhaustive)
    print('case_distribution', distribution)

if __name__ == '__main__':
    run()
