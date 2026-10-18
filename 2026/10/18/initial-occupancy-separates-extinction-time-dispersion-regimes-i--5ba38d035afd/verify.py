#!/usr/bin/env python3
"""Exact rational cross-checks of a three-patch birth--death absorption model."""
from fractions import Fraction as Q

def solve(A,b):
    n=len(b); X=[[Q(z) for z in row]+[Q(b[i])] for i,row in enumerate(A)]
    for j in range(n):
        r=next(k for k in range(j,n) if X[k][j]); X[j],X[r]=X[r],X[j]
        p=X[j][j]; X[j]=[z/p for z in X[j]]
        for k in range(n):
            if k!=j:
                t=X[k][j]; X[k]=[a-t*v for a,v in zip(X[k],X[j])]
    return [X[i][-1] for i in range(n)]

def formulas(x):
    d1=2*x*x+3*x+3; d2=4*x*x+8*x+9; d3=4*x*x+8*x+11
    return [d1/3,d2/6,d3/6],[
      (4*x**4+16*x**3+37*x*x+27*x+9)/d1**2,
      (16*x**4+64*x**3+152*x*x+128*x+45)/d2**2,
      (16*x**4+64*x**3+152*x*x+128*x+49)/d3**2]

def run():
    tested=0
    for x in [Q(0),Q(1,13),Q(1,2),Q(1),Q(11,10),Q(2),Q(3),Q(4),Q(10),Q(50),Q(100)]:
        A=[[1+2*x,-2*x,0],[-2,2+2*x,-2*x],[0,-3,3]]
        mean=solve(A,[1,1,1]); second=solve(A,[2*u for u in mean]); f=[(v-u*u)/(u*u) for u,v in zip(mean,second)]
        other,otherf=formulas(x)
        assert mean==other,(x,mean,other)
        assert f==otherf,(x,f,otherf)
        assert f[0]-1==x*(4*x*x+16*x+9)/(2*x*x+3*x+3)**2
        assert f[1]-1==4*(4*x*x-4*x-9)/(4*x*x+8*x+9)**2
        assert f[2]-1==-24*(2*x+3)/(4*x*x+8*x+11)**2
        tested+=3
    print('PASS: 33 exact mean/CV-pair comparisons, with 33 exact dispersion identities')
if __name__=='__main__': run()
