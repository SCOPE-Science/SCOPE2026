#!/usr/bin/env python3
"""Independent finite verification of five-column Paley conference-frame spectra."""
from itertools import combinations
from collections import Counter
from math import comb,sqrt
import numpy as np


def conference(p):
    assert p>=7 and p%4==3 and all(p%d for d in range(2,int(sqrt(p))+1))
    def chi(t):
        t%=p
        return 0 if t==0 else (1 if pow(t,(p-1)//2,p)==1 else -1)
    c=np.zeros((p+1,p+1),dtype=np.int64)
    for a in range(p):
        for b in range(p):
            c[a,b]=chi(b-a)
        c[a,p]=-1
        c[p,a]=1
    assert np.array_equal(c @ c,-p*np.eye(p+1,dtype=np.int64))
    return c


def pf4(c, inds):
    a,b,d,e=inds
    return int(c[a,b]*c[d,e]-c[a,d]*c[b,e]+c[a,e]*c[b,d])


def test_p(p):
    c=conference(p)
    actual=Counter()
    rep={}
    for five in combinations(range(p+1),5):
        r=sum(pf4(c,quad)**2==9 for quad in combinations(five,4))
        assert r in (0,2),(p,five,r)
        actual[r]+=1
        rep.setdefault(r,five)
    expected0=p*(p-1)*(p+1)*(p-3)*(p-7)//320
    expected2=p*(p-1)*(p+1)**2*(p-3)//192
    assert expected0+expected2==comb(p+1,5)
    assert actual==Counter({k:v for k,v in [(0,expected0),(2,expected2)] if v})
    for r,five in rep.items():
        s=c[np.ix_(five,five)]
        eig=np.linalg.eigvalsh(np.eye(5)+1j*s/np.sqrt(p))
        mu=[5+2*np.sqrt(5),5-2*np.sqrt(5)] if r==0 else [7,3]
        want=sorted([1]+[1+sign*np.sqrt(m/p) for m in mu for sign in (-1,1)])
        assert np.allclose(eig,want,rtol=0,atol=1.e-12),(p,r,eig,want)
        assert np.linalg.matrix_rank(np.eye(5)+1j*s/np.sqrt(p),tol=1.e-9)==(4 if p==7 else 5)
    print('p=',p,' five-subsets=',comb(p+1,5),'r0=',actual[0],'r2=',actual[2])


def test_universal():
    count=Counter()
    for bits in range(1024):
        s=np.zeros((5,5),dtype=np.int64)
        for i,(a,b) in enumerate(combinations(range(5),2)):
            s[a,b]=1 if bits>>i&1 else -1
            s[b,a]=-s[a,b]
        r=sum(pf4(s,t)**2==9 for t in combinations(range(5),4))
        assert r in (0,2)
        assert int(round(np.linalg.det(np.eye(5,dtype=np.int64)+s)))==16+8*r
        count[r]+=1
    print('1024 universal skew sign patterns:',dict(count))

if __name__=='__main__':
    test_universal()
    for p in (7,11,19,23,31):
        test_p(p)
    print('PASS: all exact subset counts, conference identities and spectral representatives')
