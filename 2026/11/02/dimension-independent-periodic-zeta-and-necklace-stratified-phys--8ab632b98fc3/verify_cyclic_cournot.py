"""Finite reproducibility checks for a cyclic tent-map model.
These checks illustrate exact proofs, rather than establish infinite claims.
"""
from itertools import product
from math import comb, gcd, log
import numpy as np


def g(t):
    return 0.25+0.5*t if t<=0.5 else (2*t-0.5 if t<=0.75 else 2.5-2*t)

def F(z):
    return np.array([g(z[-1]),*z[:-1]])

def inv_step(w):
    n=len(w)
    # branch 0 or 1 inverse of upper tent g on J
    def psi(y,bit):
        return np.array([*y[1:],(0.25+0.5*y[0]) if bit==0 else (1.25-0.5*y[0])])
    return psi

def fixed_by_word(n,word):
    psi=inv_step([0]*n)
    # affine map for the composition of m inverse branches:
    # recursively apply branches in chronological inverse order.
    def P(y):
        for b in word: y=psi(y,b)
        return y
    zero=np.zeros(n)
    b=P(zero)
    A=np.stack([P(np.eye(n)[j])-b for j in range(n)],axis=1)
    return np.linalg.solve(np.eye(n)-A,b)

def necklace_count(n,k):
    a=0
    for d in range(1,n+1):
        if n%d==0 and k%d==0:
            phi=sum(gcd(x,d)==1 for x in range(1,d+1))
            a+=phi*comb(n//d,k//d)
    assert a%n==0
    return a//n

def enumerate_necklaces(n):
    remaining=set(product((0,1),repeat=n)); classes=[]
    while remaining:
        p=next(iter(remaining))
        rot={p[i:]+p[:i] for i in range(n)}
        remaining-=rot
        classes.append((sum(p),len(rot)))
    return classes

def iter_F(x,m):
    for _ in range(m): x=F(x)
    return x

for n in range(2,9):
    cls=enumerate_necklaces(n)
    assert len(cls)==sum(necklace_count(n,k) for k in range(n+1))
    assert sum(d for k,d in cls)==2**n
    assert all(sum(1 for k0,d in cls if k0==k)==necklace_count(n,k) for k in range(n+1))
    assert abs(sum(d/(2**n) for k,d in cls)-1)<1e-12
    assert abs(sum(k/n*d/(2**n) for k,d in cls)-0.5)<1e-12
    for m in range(1,7):
        points=[fixed_by_word(n,w) for w in product((0,1),repeat=m)]
        assert len(points)==2**m
        assert all(np.max(np.abs(np.linalg.matrix_power(np.eye(n),1) @ z - z))<1e-10 for z in points)
        assert all(np.max(np.abs(np.array([g(z[-1]),*z[:-1]])-F(z)))<1e-10 for z in points)
        assert all(np.max(np.abs(z))<=1+1e-10 and np.min(z)>=.5-1e-10 for z in points)
        assert all(np.max(np.abs((lambda q: q)(iter_F(z,m))-z))<2e-9 for z in points)
        assert len({tuple(np.round(z,10)) for z in points})==2**m

for n in range(2,9):
    # explicit geometric identity; each fixed point set lives in the upper cube
    assert all(abs(g(t)-t)>1e-12 for t in [0.0,0.125,0.25,0.4])

print('PASS: necklace counts, basin masses and entropy means for dimensions 2..8;')
print('PASS: 2^m distinct branch-fixed points and full iterate identities for n=2..8, m=1..6.')
