#!/usr/bin/env python3
"""Independent exact-arithmetic checks of skew-tent ordinal-transition identities.

Python 3 standard library only; execute: python3 verify_ordinal_skew.py
Finite tests corroborate, but do not replace, the universal proof.
"""
from fractions import Fraction as F
from itertools import product
from math import log, isclose

SYMBOLS = ('012', '021', '201', '102', '120')
A = ((1,1,1,0,0),(0,0,0,1,0),(0,0,0,1,1),(0,0,1,0,0),(1,1,0,0,0))


def data(c):
    s = 1+c*(1-c)
    a,b,u,v = c/(2-c), c/s, 1/(2-c), 1/s
    x = (F(0),a,b,u,v,F(1))
    pi=tuple(x[i+1]-x[i] for i in range(5))
    P=((c,c*(1-c)**2/s,(1-c)/s,F(0),F(0)),
       (F(0),F(0),F(0),F(1),F(0)),
       (F(0),F(0),F(0),(1-c)**2,c*(2-c)),
       (F(0),F(0),F(1),F(0),F(0)),
       (s/(2-c),(1-c)**2/(2-c),F(0),F(0),F(0)))
    return s,x,pi,P


def meet(intervals, lo, hi):
    out=[]
    for l,r in intervals:
        a,b=max(lo,l),min(hi,r)
        if a<b:out.append((a,b))
    return out


def preimage(intervals,c):
    out=[]
    for l,r in intervals:
        out += [(c*l,c*r), (1-(1-c)*r,1-(1-c)*l)]
    return out


def cylinder_mass(word,x,c):
    intervals=[(x[word[-1]],x[word[-1]+1])]
    for i in reversed(word[:-1]):
        intervals=meet(preimage(intervals,c),x[i],x[i+1])
    return sum((r-l for l,r in intervals),F(0))


def determinant(M):
    # Bareiss algorithm exact integer determinant (for evaluating characteristic polynomial).
    arr=[list(v) for v in M]
    n=len(arr)
    d=1; sign=1
    for k in range(n-1):
        if arr[k][k]==0:
            row=next((j for j in range(k+1,n) if arr[j][k]!=0),None)
            if row is None:return 0
            arr[k],arr[row]=arr[row],arr[k];sign=-sign
        p=arr[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                arr[i][j]=(arr[i][j]*p-arr[i][k]*arr[k][j])/d
        for i in range(k+1,n):arr[i][k]=0
        d=p
    return sign*arr[-1][-1]


def chk(c):
    s,x,pi,P=data(c)
    assert F(0)<x[1]<x[2]<c<x[3]<x[4]<F(1),x
    assert sum(pi)==1 and all(sum(row)==1 for row in P)
    assert all(sum(pi[i]*P[i][j] for i in range(5))==pi[j] for j in range(5))
    for i in range(5):
        for j in range(5):
            assert cylinder_mass((i,j),x,c)==pi[i]*P[i][j],(c,i,j)
            assert (P[i][j]>0)==bool(A[i][j])
            for k in range(5):
                actual=cylinder_mass((i,j,k),x,c)
                predicted=pi[i]*P[i][j]*P[j][k]
                assert actual==predicted,(c,i,j,k,actual,predicted)
    # Every allowed word of length <= 4 is realized, forbidden words have zero mass.
    for n in range(1,5):
        for word in product(range(5),repeat=n):
            allowed=all(A[i][j] for i,j in zip(word,word[1:]))
            mass=cylinder_mass(word,x,c)
            assert (mass>0)==allowed,(c,word,mass)
    for t in (F(-2),F(-1),F(0),F(1),F(2),F(3)):
        M=[[t*(i==j)-P[i][j] for j in range(5)] for i in range(5)]
        want=t*(t-1)*(t+1-c)*(t*t+c*(1-c))
        assert determinant(M)==want,(c,t,determinant(M),want)
    for t in (-2,-1,0,1,2,3):
        M=[[t*(i==j)-A[i][j] for j in range(5)] for i in range(5)]
        want=t*(t+1)*(t**3-2*t*t+t-1)
        assert determinant(M)==want,(t,determinant(M),want)
    h=-sum(float(pi[i]*p)*log(float(p)) for i in range(5) for p in P[i] if p)
    hb=-float(c)*log(float(c))-float(1-c)*log(float(1-c))
    assert isclose(h,hb/float(s),rel_tol=1e-13,abs_tol=1e-13),(c,h,hb/float(s))
    assert pi[2]*P[2][4]==c*(1-c)/s
    print('PASS c=',c,'atoms=',x,'h_ordinal=',round(h,12),'h_original=',round(hb,12))


def main():
    for c in (F(1,10),F(1,4),F(1,3),F(1,2),F(2,3),F(3,4),F(9,10)):
        chk(c)
    print('ALL CHECKS PASSED: rational cylinders, Markov triples, matrix spectra, path language, entropy.')

if __name__=='__main__':main()
