#!/usr/bin/env python3
"""Independent small-field orbit checks and exact Burnside coefficient tests.

Uses only Python's standard library.  This is finite verification of a separately
proved all-parameter classification, not an infinite proof.
"""
from itertools import product, combinations_with_replacement
from math import comb


def euler_phi(n):
    return sum(1 for i in range(1, n + 1) if gcd(i, n) == 1)


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def factor(length, mult, T):
    out = [0] * (T + 1)
    for j in range(T // length + 1):
        out[j * length] = comb(mult + j - 1, j)
    return out


def multiply(a, b):
    T = len(a) - 1
    return [sum(a[k] * b[i-k] for k in range(i+1)) for i in range(T+1)]


def rational_coefficients(N, T):
    """Closed rotation/reflection formula, N=q-1."""
    total = [0] * (T + 1)
    for d in range(1, N + 1):
        if N % d:
            continue
        p = multiply(factor(1, 3, T), factor(d, N // d, T))
        for i in range(T + 1):
            total[i] += euler_phi(d) * p[i]
    if N % 2:
        refl = multiply(factor(1, 2, T), factor(2, (N + 1) // 2, T))
        for i in range(T + 1):
            total[i] += N * refl[i]
    else:
        fixed_two = multiply(factor(1, 3, T), factor(2, N // 2, T))
        fixed_zero = multiply(factor(1, 1, T), factor(2, N // 2 + 1, T))
        for i in range(T + 1):
            total[i] += N // 2 * (fixed_two[i] + fixed_zero[i])
    assert all(x % (2*N) == 0 for x in total)
    return [x // (2*N) for x in total]


def projective_orbits(N, T):
    """Independent orbit construction on multisets (C_N plus 0, axes)."""
    alphabet = list(range(N + 3))
    def act(x, a, flip):
        if x == N: return N
        if x == N + 1: return N + 2 if flip else N + 1
        if x == N + 2: return N + 1 if flip else N + 2
        return (a + (-x if flip else x)) % N
    ans = []
    for t in range(T + 1):
        reps = set()
        for c in combinations_with_replacement(alphabet, t):
            reps.add(min(tuple(sorted(act(x, a, flip) for x in c))
                         for a in range(N) for flip in (False, True)))
        ans.append(len(reps))
    return ans


def mul(a, b, q):
    if q != 4:
        return a * b % q
    # GF(4) = F_2[z]/(z^2+z+1), represented by two-bit polynomials.
    res = 0
    for i in range(2):
        for j in range(2):
            if (a >> i) & 1 and (b >> j) & 1:
                res ^= (1 << (i+j))
    if res & 4:
        res ^= 7
    return res


def sub(a, b, q):
    return a ^ b if q == 4 else (a - b) % q


def rank_2xt(v, q):
    cols = [(v[2*i], v[2*i+1]) for i in range(len(v)//2)]
    if all(a == b == 0 for a, b in cols): return 0
    for a,b in cols:
        for c,d in cols:
            if sub(mul(a,d,q),mul(b,c,q),q) != 0:
                return 2
    return 1


def direct_matrix_orbits(q, t):
    """Orbit BFS under actual elementary row/column monomial generators."""
    primitive = {2:1, 3:2, 4:2, 5:2}[q]
    def nbrs(v):
        w = list(v)
        for i in range(t):w[2*i],w[2*i+1] = w[2*i+1],w[2*i]
        yield tuple(w)
        w = list(v)
        for i in range(t):w[2*i] = mul(primitive,w[2*i],q)
        yield tuple(w)
        for i in range(t):
            w=list(v)
            w[2*i]=mul(w[2*i], primitive,q)
            w[2*i+1]=mul(w[2*i+1],primitive,q)
            yield tuple(w)
        for i in range(t-1):
            w=list(v)
            w[2*i:2*i+2],w[2*i+2:2*i+4] = w[2*i+2:2*i+4],w[2*i:2*i+2]
            yield tuple(w)
    unseen = set(product(range(q), repeat=2*t))
    byrank = [0, 0, 0]
    while unseen:
        seed=unseen.pop()
        byrank[rank_2xt(seed,q)] += 1
        todo = [seed]
        while todo:
            v=todo.pop()
            for w in nbrs(v):
                if w in unseen:
                    unseen.remove(w)
                    todo.append(w)
    return byrank


def run():
    checks=0
    for q, T in [(2,5),(3,5),(4,5),(5,5),(7,4),(8,4),(9,4)]:
        x=rational_coefficients(q-1,T)
        y=projective_orbits(q-1,T)
        assert x == y,(q,x,y)
        print('PROJECTIVE',q,'t=0..'+str(T),x)
        checks+=1
    for q,t in [(2,2),(2,3),(2,4),(3,2),(3,3),(4,2),(4,3),(5,2)]:
        counts=direct_matrix_orbits(q,t)
        expected=[1,2*t,rational_coefficients(q-1,t)[t]-(2*t+1)]
        assert counts==expected,(q,t,counts,expected)
        print('MATRIX',q,t,counts)
        checks+=1
    for q in [2,3,4,5,7,8,9,11]:
        N=q-1
        assert rational_coefficients(N,2)[2] == 7 + N//2
        checks+=1
    print('INCIDENCE_LOEWY_ORBITS_OK', checks,'independent parameter checks')

if __name__=='__main__':
    run()
