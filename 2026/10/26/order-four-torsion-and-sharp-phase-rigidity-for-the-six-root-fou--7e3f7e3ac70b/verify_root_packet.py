#!/usr/bin/env python3
"""Exact Fourier collision and deficit checks for a six-character root packet."""
from collections import defaultdict
from fractions import Fraction
from itertools import product
import random

R=((1,0),(-1,0),(0,1),(0,-1),(1,-1),(-1,1))
PAIRS=((0,1),(2,3),(4,5))

def fibres(q):
    table=defaultdict(list)
    for i,j in product(range(6), repeat=2):
        r=(R[i][0]+R[j][0],R[i][1]+R[j][1])
        if q is not None: r=(r[0]%q,r[1]%q)
        table[r].append((i,j))
    return table

def inner(u,v): return (u.conjugate()*v).real

def fourth(c,q):
    return sum(abs(sum(c[i]*c[j] for i,j in ij))**2 for ij in fibres(q).values())

def prediction(c,q):
    S=sum(abs(z)**2 for z in c)
    z=[c[i]*c[j] for i,j in PAIRS]
    v=2*S*S-sum(abs(t)**4 for t in c)
    v+=8*sum(inner(z[i],z[j]) for i in range(3) for j in range(i+1,3))
    if q==4:
        v+=2*sum(inner(c[i]**2,c[j]**2) for i,j in PAIRS)
    return v

def deficit(c,q):
    X=[abs(c[i])**2+abs(c[j])**2 for i,j in PAIRS]
    D=[abs(c[i])**2-abs(c[j])**2 for i,j in PAIRS]
    z=[c[i]*c[j] for i,j in PAIRS]
    S=sum(X)
    F=lambda:sum(X[i]*X[j]/4-inner(z[i],z[j]) for i in range(3) for j in range(i+1,3))
    variance=sum(Xi*Xi for Xi in X)-S*S/3
    if q==4:
        return variance+sum(Di*Di for Di in D)+8*F()+2*sum(abs(c[i]*c[j])**2-inner(c[i]**2,c[j]**2) for i,j in PAIRS)
    return Fraction(3,2)*variance+Fraction(1,2)*sum(Di*Di for Di in D)+8*F()

def main():
    checks=0
    for q,counts in [(None,{1:6,2:12,6:1}),(4,{2:15,6:1}),(5,{1:6,2:12,6:1}),(7,{1:6,2:12,6:1})]:
        d=defaultdict(int)
        for pairlist in fibres(q).values():d[len(pairlist)]+=1
        assert dict(d)==counts,(q,d);checks+=1
    rng=random.Random(20261020)
    for _ in range(120):
        c=[complex(rng.randint(-5,5),rng.randint(-5,5)) for _ in range(6)]
        for q in [None,4,5,7]:
            a=fourth(c,q)
            b=prediction(c,q)
            assert abs(a-b)<1e-7,(q,c,a,b);checks+=1
            K=Fraction(8,3) if q==4 else Fraction(5,2)
            S=sum(abs(z)**2 for z in c)
            D=deficit(c,q)
            assert D>=-1e-8 and abs(K*S*S-a-D)<1e-7,(q,a,D);checks+=1
    for q,K in [(4,Fraction(8,3)),(5,Fraction(5,2)),(7,Fraction(5,2))]:
        c=[1+0j]*6
        assert fourth(c,q)==K*36;checks+=1
    # q=3 uniform sharp value and coset relation.
    assert fourth([1]*6,3)==Fraction(9,2)*36;checks+=1
    G={(a,b) for a,b in product(range(3),repeat=2)}
    missing=G-{(x%3,y%3) for x,y in R}
    assert missing=={(0,0),(1,1),(2,2)};checks+=1
    # Every 4th-root-valued maximizing phase on Z_4^2 is counted exactly.
    roots=(1,-1,1j,-1j)
    count=0
    for c in product(roots,repeat=6):
        s=sum(abs(z)**2 for z in c)
        if fourth(c,4)==Fraction(8,3)*s*s:
            count+=1
            ps=[c[i]*c[j] for i,j in PAIRS]
            assert ps[0]==ps[1]==ps[2] and all((c[i]/c[j]).imag==0 for i,j in PAIRS)
        checks+=1
    assert count==128;checks+=1
    # Distinct projective complex lines among the 128 fourth-root arrays.
    reps=set()
    for c in product(roots,repeat=6):
        if fourth(c,4)==Fraction(8,3)*36:
            reps.add(tuple(z/c[0] for z in c))
    assert len(reps)==32;checks+=1
    print('PASS',checks,'exact collision/deficit/phase assertions; 32 projective q=4 optimizers')
if __name__=='__main__':main()
