"""Exact finite-field certificate for the characteristic-23 Humbert Hasse arrangement.

Run using Python 3.9+ (standard library only): python humbert23_verifier.py
"""
from collections import Counter
from itertools import combinations, product
from math import comb

P = 23
D = 5  # nonsquare modulo 23
Q = P * P
ZERO = (0, 0)
ONE = (1, 0)


def add(x, y):
    return ((x[0] + y[0]) % P, (x[1] + y[1]) % P)


def neg(x):
    return ((-x[0]) % P, (-x[1]) % P)


def sub(x, y):
    return add(x, neg(y))


def mul(x, y):
    return ((x[0] * y[0] + D * x[1] * y[1]) % P,
            (x[0] * y[1] + x[1] * y[0]) % P)


def power(x, n):
    ans = ONE
    while n:
        if n & 1:
            ans = mul(ans, x)
        x = mul(x, x)
        n >>= 1
    return ans


def inverse(x):
    assert x != ZERO
    return power(x, Q - 2)


def divide(x, y):
    return mul(x, inverse(y))


HASSE = [comb(11, j) ** 2 % P for j in range(12)]


def H(x):
    ans = ZERO
    for coeff in reversed(HASSE):
        ans = add(mul(ans, x), (coeff, 0))
    return ans


def cr(u, v):
    assert u not in (ZERO, ONE) and v not in (ZERO, ONE, u)
    return (u, v, divide(v, u),
            divide(sub(v, ONE), sub(u, ONE)),
            divide(mul(u, sub(v, ONE)), mul(v, sub(u, ONE))))


def s(u, v):
    return sum(H(x) == ZERO for x in cr(u, v))


def check_polynomial_factorization():
    # H(X) = (X^2-X+1) product_{r in R_1}(X-r), exactly in F_23[X].
    r1 = (2, 3, 8, 11, 12, 13, 16, 21, 22)
    c = [1, -1, 1]
    for root in r1:
        b = [0] * (len(c) + 1)
        for i, a in enumerate(c):
            b[i] -= root * a
            b[i + 1] += a
        c = [x % P for x in b]
    assert c == HASSE
    assert pow(D, (P - 1) // 2, P) == P - 1
    assert pow(P - 3, (P - 1) // 2, P) == P - 1  # discriminant -3
    return r1


def algebraic_root_incidence():
    R = tuple((a, b) for a in range(P) for b in range(P) if H((a, b)) == ZERO)
    assert len(R) == 11 and all(z not in (ZERO, ONE) for z in R)
    assert sum(b == 0 for a, b in R) == 9
    results = []
    for even in (False, True):
        roots = tuple(z for z in R if even or z[1] == 0)
        pairs = Counter(s(u, v) for u in roots for v in roots if u != v)
        assert sum(pairs.values()) == len(roots) * (len(roots) - 1)
        assert set(pairs) == {2, 3, 4}, pairs
        expected = {2: 56 if even else 18, 3: 18, 4: 36}
        assert dict(pairs) == expected, (even, pairs)
        # S_5 symmetry: each of ten pairs of Hasse divisors has
        # the same root-pair distribution. Divide by C(s,2).
        N = {ss: 10 * pairs[ss] // comb(ss, 2) for ss in pairs}
        assert all(10 * pairs[ss] % comb(ss, 2) == 0 for ss in pairs)
        q = Q if even else P
        N[1] = 5 * len(roots) * (q - 3) - sum(ss * n for ss, n in N.items())
        N[0] = (q - 2) * (q - 3) - sum(N.values())
        expected_N = ({0: 249132, 1: 27390, 2: 560, 3: 60, 4: 60} if even
                      else {0: 0, 1: 120, 2: 180, 3: 60, 4: 60})
        assert N == expected_N, (even, N)
        print('ROOT_PAIR_DISTRIBUTION', q, dict(sorted(pairs.items())))
        print('MARKED_PARAMETER_STRATA', q, dict(sorted(N.items())))
        results.append(N)
    assert results[0][4] == results[1][4] == 60
    assert results[0][3] == results[1][3] == 60
    return R, results


def all_parameter_direct_count(qroots, elements):
    # Independent enumeration of each rational parameter pair, not moment counts.
    out = Counter()
    for u in elements:
        if u in (ZERO, ONE):
            continue
        for v in elements:
            if v in (ZERO, ONE, u):
                continue
            out[s(u, v)] += 1
    return out


def verify_tangent_distinctness():
    # Numerators and denominators of the five cross ratios and their gradients.
    # At each singular arrangement point, simple Hasse roots mean the tangent
    # to a component is the kernel of d(lambda_i).
    roots = [z for z in range(P) if H((z, 0)) == ZERO]
    # lambda = u, v, v/u, (v-1)/(u-1), u(v-1)/(v(u-1))
    def inv(z):
        return pow(z % P, P - 2, P)
    # Differentiation of lambda_5: lambda_5=u(v-1)/(v(u-1)).
    def gg(u, v):
        lam = u * (v - 1) * inv(v) * inv(u - 1) % P
        # logarithmic formula allowed only if u,v,v-1,u-1 nonzero, ensured.
        a = lam * (inv(u) - inv(u - 1)) % P
        b = lam * (inv(v - 1) - inv(v)) % P
        return [(1, 0), (0, 1),
                (-v * inv(u)**2 % P, inv(u)),
                (-(v - 1) * inv(u - 1)**2 % P, inv(u - 1)),
                (a, b)]
    for u, v in product(roots, repeat=2):
        if u == v:continue
        inds = [i for i, x in enumerate(cr((u, 0), (v, 0))) if H(x) == ZERO]
        if len(inds) >= 3:
            g = gg(u, v)
            for i, j in combinations(inds, 2):
                a, b = g[i]
                c, d = g[j]
                assert (a * d - b * c) % P != 0, (u, v, i, j)
    print('HIGHER_INCIDENCE_TANGENTS_PAIRWISE_DISTINCT=PASS')


def verify_rank_one_single_branch_orbit():
    # PGL_2-normalize each relabeling of five branch points to infinity,0,1,u,v.
    from itertools import permutations
    inf = (1, 0)
    def det(x, y):
        return (x[0] * y[1] - x[1] * y[0]) % P
    def normal(a, b, c, z):
        n = det(z, b) * det(c, a) % P
        d = det(z, a) * det(c, b) % P
        assert d != 0
        return n * pow(d, P - 2, P) % P
    def orbit_image(u, v, perm):
        branches = (inf, (0, 1), (1, 1), (u, 1), (v, 1))
        a, b, c = (branches[perm[j]] for j in range(3))
        return (normal(a, b, c, branches[perm[3]]),
                normal(a, b, c, branches[perm[4]]))
    orbit = {orbit_image(6, 12, pi) for pi in permutations(range(5))}
    fourfold = {(u, v) for u in range(2, P) for v in range(2, P)
                if u != v and s((u, 0), (v, 0)) == 4}
    assert orbit == fourfold and len(orbit) == 60
    print('S5_SINGLE_BRANCH_EQUIVALENCE_ORBIT_FOURFOLD=60')


def main():
    r1 = check_polynomial_factorization()
    print('HASSE_FACTOR_RATIONAL_ROOTS', r1, 'IRREDUCIBLE_QUADRATIC=X^2-X+1')
    R, expected = algebraic_root_incidence()
    for even in (False, True):
        elts = [(a, b) for a in range(P) for b in (range(P) if even else (0,))]
        direct = all_parameter_direct_count(R, elts)
        assert {k:direct.get(k,0) for k in range(5)} == expected[int(even)], (even, direct)
        print('DIRECT_PARAMETER_CHECK', Q if even else P, dict(sorted(direct.items())))
    verify_tangent_distinctness()
    verify_rank_one_single_branch_orbit()
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
