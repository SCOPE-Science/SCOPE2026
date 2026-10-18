#!/usr/bin/env python3
"""Exact integer check of an unbordered-conjugate histogram and two generators."""
import csv, sys
from math import isqrt
from fractions import Fraction

def mobius(k):
    d=2; parity=0
    while d*d<=k:
        if k%d==0:
            k//=d;parity+=1
            if k%d==0:return 0
        d+=1
    if k>1:parity+=1
    return -1 if parity&1 else 1

def primitive(n):
    return sum(mobius(d)*(1<<(n//d)) for d in range(1,n+1) if n%d==0)

def parse(path):
    out={}
    for line in open(path,encoding='utf8'):
        z=list(map(int,line.split()))
        if z:
            assert len(z)==z[0]+2
            out[z[0]]=z[1:]
    return out

def main():
    with open(sys.argv[1],encoding='utf8',newline='') as f:
        reader=csv.DictReader(f);assert reader.fieldnames==['n']+[f'h_{j}' for j in range(29)]
        rows={int(d['n']):[int(d[f'h_{j}']) for j in range(29)] for d in reader}
    assert len(rows)==28 and set(rows)==set(range(1,29))
    necklaces=parse(sys.argv[2]);direct=parse(sys.argv[3]);assert len(necklaces)==28 and len(direct)==25
    u=[0]*29;u[1]=2
    for n in range(2,29):
        if n%2:u[n]=2*u[n-1]
        else:u[n]=2*u[n-1]-u[n//2]
    for n in range(1,29):
        h=rows[n];assert all(z==0 for z in h[n+1:]); h=h[:n+1]
        assert h==necklaces[n]
        if n<=25:assert h==direct[n]
        assert sum(h)==1<<n
        assert sum(j*z for j,z in enumerate(h))==n*u[n]
        assert h[0]==(1<<n)-primitive(n)
        assert h[1]==0 if n>=2 else True
    h=rows[28];mean=Fraction(sum(j*v for j,v in enumerate(h)),1<<28)
    var=Fraction(sum(j*j*v for j,v in enumerate(h)),1<<28)-mean**2
    assert mean==Fraction(62901909,8388608)
    assert var==Fraction(131772345343303,70368744177664)
    assert h[13]==5040 and all(h[j]==0 for j in range(14,29))
    print('PASS: 28 complete orbit rows, 25 independent all-word rows, 28 moment/nonprimitive/total checks, exact variance')

if __name__=='__main__':main()
