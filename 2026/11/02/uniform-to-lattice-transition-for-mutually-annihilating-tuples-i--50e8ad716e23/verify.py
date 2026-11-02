#!/usr/bin/env python3
"""Direct finite checks of pairwise-zero tuple valuation formulas.
Only standard Python required. No external data or resources.
"""
from itertools import product
from fractions import Fraction
from math import prod


def valuation(x, p, m):
    if x == 0:
        return m
    ans = 0
    while ans < m and x % p == 0:
        ans += 1
        x //= p
    return ans


def truncated_multiply(a, b, p, m):
    aa = []
    bb = []
    for _ in range(m):
        aa.append(a % p)
        bb.append(b % p)
        a //= p
        b //= p
    return all(sum(aa[j]*bb[d-j] for j in range(d+1)) % p == 0 for d in range(m))


def ring_zero_tuple_count(p, m, r, typ):
    universe = range(p**m)
    count = 0
    for xs in product(universe, repeat=r):
        if all((xs[i]*xs[j]) % (p**m) == 0 if typ == 'integers' else
               truncated_multiply(xs[i],xs[j],p,m)
               for i in range(r) for j in range(i+1,r)):
            count += 1
    return count


def shell_zero_tuple_count(q, m, r):
    shells = [(q-1)*q**(m-v-1) for v in range(m)] + [1]
    return sum(prod(shells[v] for v in vs)
               for vs in product(range(m+1), repeat=r)
               if all(vs[i]+vs[j]>=m for i in range(r)
                      for j in range(i+1,r)))


def asymptotic_prefactor(q, r, eps):
    t = Fraction(1,q)
    u = 1-t
    a = t**(r-2)
    assert r>=3 and eps in (0,1)
    return (1 + r*u*a/(1-a)) if eps == 0 else (t**r + r*u*t**(r-1)/(1-a))


def main():
    exhaustive = 0
    for p, m, r in [(2,2,2),(2,3,2),(2,4,2),(3,2,2),
                    (2,2,3),(2,3,3),(2,4,3),(3,2,3),
                    (2,2,4),(2,3,4),(3,2,4)]:
        want = shell_zero_tuple_count(p,m,r)
        for typ in ('integers','polynomials'):
            got = ring_zero_tuple_count(p,m,r,typ)
            assert got == want, (p,m,r,typ,got,want)
            exhaustive += 1
    shell_checks = 0
    for q in (2,3,4,5):
        for m in range(1,9):
            for r in range(2,6):
                if (m+1)**r > 500000:
                    continue
                cnt = shell_zero_tuple_count(q,m,r)
                assert cnt > 0
                if r==2:
                    expected = (1+m*(1-Fraction(1,q)))*q**(2*m-m)
                    assert cnt == expected, (q,m,r,cnt,expected)
                else:
                    # Restricted sum must increase to its unrestricted limit.
                    h, eps = divmod(m,2)
                    p = Fraction(cnt,q**(m*r))
                    limit = asymptotic_prefactor(q,r,eps)/q**(r*h)
                    assert p <= limit
                    if m>=7 and r>=4:
                        assert float(p/limit)>0.98
                shell_checks += 1
    # For two factors, the one-coordinate conditional distribution is
    # exactly flat on all finite valuations, with one exceptional zero atom.
    for q in (2,3,4):
        for m in range(1,15):
            count=shell_zero_tuple_count(q,m,2)
            base=(q-1)*q**(m-1) # # of elements of valuation zero
            for v in range(m):
                # There are (q-1)q^{m-v-1} elements with q^v annihilators.
                assert ((q-1)*q**(m-v-1))*q**v == base
            assert count == m*base+q**m
    print('VERIFY_OK: exhaustive_ring_models=%d; shell_and_limit_checks=%d; pair_flatness=%d' %
          (exhaustive,shell_checks,42))

if __name__=='__main__':
    main()
