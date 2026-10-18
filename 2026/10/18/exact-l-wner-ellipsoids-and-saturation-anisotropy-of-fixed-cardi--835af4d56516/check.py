"""Exact finite checks for the spectral enclosing-ellipsoid theorem.

Run: python3 check.py  (standard library only).
These tests check finite instances; they do not prove the general theorem.
"""
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations, permutations
from math import comb, factorial


def matchings(p, q, k):
    for rr in combinations(range(p), k):
        for cc in combinations(range(q), k):
            for order in permutations(cc):
                yield frozenset(i*q+j for i, j in zip(rr, order))


def covariance_spectrum(p, q, k):
    t = Q(k, p*q)
    u = Q(k*(k-1), p*q*(p-1)*(q-1))
    return (t-(q-1)*u, t-(p-1)*u, t+u)


def dimension(p, q, k):
    return (p-1)*(q-1) + ((p-1) if k<p else 0) + ((q-1) if k<q else 0)


def check(p, q, k):
    ms = list(matchings(p, q, k))
    N = len(ms)
    assert N == comb(p,k)*comb(q,k)*factorial(k)
    n = p*q
    hits = Counter()
    together = Counter()
    for S in ms:
        hits.update(S)
        for e in S:
            for f in S:
                together[(e,f)] += 1
    mu = Q(k,n)
    rho = Q(k*(k-1),p*q*(p-1)*(q-1))
    l10,l01,l11 = covariance_spectrum(p,q,k)
    assert l11>0 and l10>=0 and l01>=0
    for e in range(n):
        assert Q(hits[e],N) == mu
        for f in range(n):
            if e==f: expect = mu
            elif e//q==f//q or e%q==f%q: expect = Q(0)
            else: expect = rho
            assert Q(together[e,f],N)==expect,(p,q,k,e,f)
    s10=Q(k*(p-k),p*q)
    s01=Q(k*(q-k),p*q)
    s11=Q(k*((p-1)*(q-1)+k-1),p*q)
    assert s10+s01+s11==Q(k)-Q(k*k,p*q)
    value=sum((s/ell for s,ell in [(s10,l10),(s01,l01),(s11,l11)] if ell))
    assert value==dimension(p,q,k),(p,q,k,value)
    assert all((ell==0)==(s==0) for ell,s in [(l10,s10),(l01,s01),(l11,s11)])
    return N


def main():
    profiles=0
    examined=0
    for p in range(2,6):
        for q in range(p,7):
            for k in range(1,p+1):
                examined += check(p,q,k)
                profiles+=1
    print('PASS:', profiles, 'profiles;', examined, 'individual matchings; exact pair moments and spectral-contact identities')

if __name__=='__main__':
    main()
