"""Finite checks for explicit three-observable fiber law.
The universal analytical assertions are proved separately.
"""
from fractions import Fraction
from math import sqrt
import random


def bounds(p,r):
    return abs((1+r)*p-r), r+(1-r)*p


def check():
    count=0
    # Exact rational interval geometry and sharp witness.
    for den in (1,2,3,5,7,11,13,17,19):
        for num in range(den+1):
            r=Fraction(num,den)
            pstar=2*r/(1+r)
            q=Fraction(0)
            Lp,Up=bounds(pstar,r)
            Lq,Uq=bounds(q,r)
            assert Lp <= Uq and Lq <= Up
            assert 2*(pstar-q)==4*r/(1+r)
            count+=3
            for grid in (3,7,13):
                P=[Fraction(k,grid) for k in range(grid+1)]
                for p in P:
                    for q in P:
                        if p < q:continue
                        lp,up=bounds(p,r)
                        lq,uq=bounds(q,r)
                        if max(lp,lq)<=min(up,uq):
                            assert 2*(p-q)<=4*r/(1+r)
                            count+=1
    # Complex state-level explicit witness for nonzero rational r.
    for den in (2,3,5,7,11,13,17):
        for num in range(1,den+1):
            r=num/den
            p=2*r/(1+r)
            top=[complex(sqrt(p)),0j]
            bottom=[0j,complex(sqrt(1-p))]
            x=top+bottom
            y=[0j,0j,1+0j,0j]
            def spin(z):
                z0,z1=z
                return (2*(z0.conjugate()*z1).real, 2*(z0.conjugate()*z1).imag, abs(z0)**2-abs(z1)**2)
            def obs(w,r):
                s=spin(w[:2]);t=spin(w[2:]);return [s[j]+r*t[j] for j in range(3)]
            ox=obs(x,r);oy=obs(y,r)
            assert max(abs(a-b) for a,b in zip(ox,oy))<1e-12
            assert abs((sum(abs(z)**2 for z in x[:2])-sum(abs(z)**2 for z in x[2:]))+1 -4*r/(1+r))<1e-12
            count+=2
    print('PASS', count, 'finite rational/witness assertions')

if __name__=='__main__':check()
