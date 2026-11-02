#!/usr/bin/env python3
"""Exact exhaustive certificate for six fertility regimes in a two-stage projection."""
from __future__ import annotations
import csv
import itertools
from fractions import Fraction as F
from pathlib import Path

A = (1,2,4,6,5,3)
B = (1,2,4,5,6,3)
C = (1,5,3,4,2,6)

def canonical(seq):
    t=tuple(seq)
    return min([tuple(t[i:]+t[:i]) for i in range(6)] +
               [tuple(t[::-1][i:]+t[::-1][:i]) for i in range(6)])

def stats(seq):
    a,b,c,d,e,f=seq
    B=(a*c+a*d+a*e+b*d+b*e+b*f+c*e+c*f+d*f)
    H=(a*c+a*e+c*e+b*d+b*f+d*f)
    C=a*c*e+b*d*f
    return B,H,C

def matmul(X,Y):
    return tuple(tuple(sum(X[i][k]*Y[k][j] for k in range(2))
        for j in range(2)) for i in range(2))

def trace_product(seq,alpha,delta,s,p):
    X=((F(1),F(0)),(F(0),F(1)))
    for digit in seq:
        M=((F(0),alpha+delta*digit),(s,p))
        X=matmul(M,X)
    return X[0][0]+X[1][1]

def trace_polynomial(seq,alpha,delta,s,p):
    b,h,c=stats(seq)
    return (p**6+s*p**4*(6*alpha+21*delta)
         +s**2*p**2*(9*alpha**2+63*alpha*delta+delta**2*b)
         +s**3*(2*alpha**3+21*alpha**2*delta
                 +alpha*delta**2*h+delta**3*c))

def main():
    root=Path(__file__).resolve().parent
    perms=list(itertools.permutations(range(1,7)))
    assert len(perms)==720
    orbits={}
    for seq in perms:
        key=canonical(seq)
        orbits.setdefault(key,[]).append(seq)
    assert len(orbits)==60
    assert all(len(v)==12 for v in orbits.values())

    # Entire 720-case enumeration; 60 dihedral classes are listed in the CSV.
    actual=sorted((key,*stats(key),len(members)) for key,members in orbits.items())
    with (root/'orbit_certificate.csv').open(newline='',encoding='utf-8') as h:
        rows=list(csv.DictReader(h))
    assert len(rows)==60
    expected=sorted((tuple(map(int, r['word'].split('-'))),
        int(r['B']),int(r['H']),int(r['C']),int(r['orbit_size'])) for r in rows)
    assert actual==expected

    vminB=min(stats(z)[0] for z in perms)
    vmaxB=max(stats(z)[0] for z in perms)
    vminH=min(stats(z)[1] for z in perms)
    vmaxH=max(stats(z)[1] for z in perms)
    vminC=min(stats(z)[2] for z in perms)
    vmaxC=max(stats(z)[2] for z in perms)
    assert (vminB,vmaxB,vminH,vmaxH,vminC,vmaxC)==(93,117,65,85,54,126)

    assert stats(A)==(93,65,56)
    assert stats(B)==(94,65,54)
    assert stats(C)==(117,85,126)
    # Unique extremal orbits and sharp distinction from other calendars.
    assert {canonical(z) for z in perms if stats(z)[0]==93}=={canonical(A)}
    assert {canonical(z) for z in perms if stats(z)[0]==94 and stats(z)[2]==54}=={canonical(B)}
    assert {canonical(z) for z in perms if stats(z)[0]==117}=={canonical(C)}
    assert all(stats(z)[0]>=94 for z in perms if canonical(z)!=canonical(A))
    assert all(stats(z)[1]>=65 and stats(z)[2]>=54 for z in perms)
    assert all(stats(z)[0]<=117 and stats(z)[1]<=85 and stats(z)[2]<=126 for z in perms)

    for alpha,delta,s,p in ((F(1),F(1),F(1,16),F(1,2)),
                            (F(1),F(1),F(1,8),F(1,2)),
                            (F(1),F(1),F(1,4),F(1,2)),
                            (F(2,3),F(5,7),F(3,10),F(2,5))):
        assert all(trace_product(seq,alpha,delta,s,p)==
                   trace_polynomial(seq,alpha,delta,s,p) for seq in perms)
        weights={canonical(seq):trace_product(seq,alpha,delta,s,p) for seq in perms}
        chi=s*delta/p**2
        winners={z for z,v in weights.items() if v==min(weights.values())}
        assert winners==({canonical(A)} if chi<F(1,2) else
                         {canonical(B)} if chi>F(1,2) else
                         {canonical(A),canonical(B)})
        assert {z for z,v in weights.items() if v==max(weights.values())}=={canonical(C)}
        assert (trace_product(A,alpha,delta,s,p)-trace_product(B,alpha,delta,s,p)
                ==s*s*p*p*delta*delta*(-1+2*chi))
    # Small-period order rankings involve only one order-sensitive coefficient.
    from functools import reduce
    for n in range(2,6):
        trial=list(itertools.permutations(range(1,n+1)))
        def tr(z,s,p):
            X=((F(1),F(0)),(F(0),F(1)))
            for f in z:X=matmul(((F(0),F(f)),(s,p)),X)
            return X[0][0]+X[1][1]
        left={z:tr(z,F(1,8),F(1,2)) for z in trial}
        right={z:tr(z,F(1,4),F(1,2)) for z in trial}
        for u in trial:
            for v in trial:
                assert (left[u]>left[v])-(left[u]<left[v]) == (right[u]>right[v])-(right[u]<right[v])
    print('PASS: 720 schedules; 60 full dihedral orbits; full 60-row certificate;')
    print('exact trace expansion; all extremal classes; both sides and equality of sharp threshold;')
    print('order-ranking invariant at periods 2 through 5 in exact test instances.')

if __name__=='__main__':main()
