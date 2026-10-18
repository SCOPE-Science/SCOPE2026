"""Reproduce modular-hyperbola pair-sum histograms and Kloosterman moments.
Requires Python 3 standard library; finite checks corroborate, not replace, proof.
"""
from collections import Counter, defaultdict
from cmath import exp
from math import gcd, pi, isclose

CASES = [(3, 2), (3, 3), (3, 4), (5, 2), (5, 3), (7, 2), (11, 2)]

def count_fibers(p, k):
    n = p**k
    U = [u for u in range(n) if gcd(u, n) == 1]
    inv = {u: pow(u, -1, n) for u in U}
    r = Counter(((x + y) % n, (inv[x] + inv[y]) % n) for x in U for y in U)
    return n, U, r

def valuation(a, p, k):
    if a == 0:
        return k
    v = 0
    while a % p == 0:
        a //= p
        v += 1
    return v

def strata(p, k, s, n):
    a = valuation(s, p, k)
    if a == k:
        return {len([x for x in range(n) if gcd(x, n) == 1]): 1}
    if a:
        return {2*p**a: (p-1)*p**(k-a-1)//2}
    positive = {}
    zero_val = (p-3)*p**(k-1)//2
    if zero_val:
        positive[2] = zero_val
    for j in range(1, (k-1)//2 + 1):
        positive[2*p**j] = (p-1)*p**(k-2*j-1)//2
    positive[p**(k//2)] = 1
    return positive

def verify():
    rows = 0
    ordered = 0
    for p, k in CASES:
        n, U, rep = count_fibers(p, k)
        m = len(U)
        assert m == (p-1)*p**(k-1)
        assert sum(rep.values()) == m*m
        assert rep[(0, 0)] == m
        for s in range(n):
            actual = Counter(rep.get((s, z), 0) for z in range(n))
            positive = strata(p, k, s, n)
            expected = Counter(positive)
            expected[0] = n - sum(positive.values())
            assert actual == expected, (p, k, s, actual, expected)
            if s and valuation(s, p, k) < k:
                a = valuation(s, p, k)
                assert all((valuation(z,p,k) == a) for z in range(n) if rep.get((s,z), 0)), (p,k,s)
            rows += 1
        energy = sum(v*v for v in rep.values())
        expected_energy = 3*(p-1)*p**(2*k-2)*(k*(p-1)-1)
        assert energy == expected_energy, (p, k, energy, expected_energy)
        ordered += m*m
        if (p,k) in [(3,2),(5,2)]:
            roots = [exp(2j*pi*a/n) for a in range(n)]
            inverse = [pow(u,-1,n) for u in U]
            direct = 0.
            for a in range(n):
                for b in range(n):
                    z = sum(roots[(a*u+b*v)%n] for u,v in zip(U,inverse))
                    direct += abs(z)**4
            assert isclose(direct,n*n*energy,rel_tol=4e-12,abs_tol=1e-5), (p,k,direct,n*n*energy)
        print('CHECK', p, k, 'N', n, 'fibers', len(rep), 'energy',energy)
    print('VERIFY_OK fields=%d rows=%d ordered_pairs=%d direct_moments=2'%(len(CASES),rows,ordered))

if __name__ == '__main__':
    verify()
