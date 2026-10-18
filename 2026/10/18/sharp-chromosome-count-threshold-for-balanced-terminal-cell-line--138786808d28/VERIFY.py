"""Reproducible finite checks of balanced complementary-daughter genealogy identities.
Run: python VERIFY.py. Python standard library only.
"""
from fractions import Fraction
from math import comb, sqrt
from itertools import product

def joint(m,j):
    n=2*m
    t=n-j-1
    return Fraction(sum(comb(j,r)*comb(t,m-r-1)*comb(t,m-r)
                        for r in range(j+1) if 0 <= m-r-1 <= t and 0 <= m-r <= t),2**(j+2*t))

def subtree(k,m):
    # Enumerate all fair assignment bits at nodes and coordinates for tiny cases.
    n=2*m
    node_count=(1<<n)-1
    total=Fraction(0)
    second=Fraction(0)
    for bits in product((0,1), repeat=k*node_count):
        states=[((0,0),)*k]
        idx=0
        for depth in range(n):
            new=[]
            for state in states:
                dec=bits[idx:idx+k]
                idx+=k
                a=[];b=[]
                for (lo,hi),coin in zip(state,dec):
                    a.append((lo+coin,hi+1-coin))
                    b.append((lo+1-coin,hi+coin))
                new.append(tuple(a));new.append(tuple(b))
            states=new
        z=sum(all(x==m and y==m for x,y in state) for state in states)
        total+=z;second+=z*z
    d=2**(k*node_count)
    return total/d,second/d

checks=0
for m in range(1,35):
    n=2*m
    p=Fraction(comb(n,m),2**n)
    for j in range(n):
        q=joint(m,j)
        assert 0<=q<=p
        if j==n-1: assert q==0
        else:
            t=n-j-1
            maxbin=Fraction(comb(t,t//2),2**t)
            assert q<=p*maxbin
            assert float(q/p**2)<=sqrt(n/t)+1e-12
        checks+=1
for m,k in ((1,1),(1,2),(2,1)):
    n=2*m
    p=Fraction(comb(n,m),2**n)
    e,e2=subtree(k,m)
    rhs_e=2**n*p**k
    rhs_e2=rhs_e+sum(Fraction(2**(2*n-j-1))*(joint(m,j)**k) for j in range(n))
    assert e==rhs_e,(m,k,e,rhs_e)
    assert e2==rhs_e2,(m,k,e2,rhs_e2)
    checks+=2
print('PASS',checks,'exact identities and finite bound checks; asymptotic theorem proved analytically.')
