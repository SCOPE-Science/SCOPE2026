#!/usr/bin/env python3
"""Independent finite checks for the modulated circle Poisson covariance theorem.
Python 3 standard library only. These checks do not replace the infinite proof.
"""
from fractions import Fraction
import cmath
import math
import random

PI=math.pi

def kernel(r,k,e,x,y):
    p=(1-r*r)/(1-2*r*math.cos(x-y)+r*r)
    return p*(1+e*math.cos(k*(x+y)))

def quadratic(r,k,e,angles,weights):
    return sum((weights[i].conjugate()*weights[j]*kernel(r,k,e,angles[i],angles[j])
                for i in range(len(angles)) for j in range(len(angles))),0j)

def series_quadratic(r,k,e,angles,weights,nmax=120):
    F={n:sum((z*cmath.exp(-1j*n*x) for x,z in zip(angles,weights)),0j)
         for n in range(-nmax-k,nmax+k+1)}
    main=sum(r**abs(n)*abs(F[n])**2 for n in range(-nmax,nmax+1))
    interaction=sum(r**abs(n)*F[n+k].conjugate()*F[n-k]
                    for n in range(-nmax,nmax+1))
    return main+e*interaction.real

def threshold(r,k):
    return 2*r**k/(1+r**(2*k))

def polygon(r,k,e):
    sign=1 if e>=0 else -1
    alpha=PI/(2*k) if sign>0 else 0.0
    angles=[alpha+j*PI/k for j in range(2*k)]
    weights=[complex((-1)**j) for j in range(2*k)]
    return angles,weights

def exact_four():
    # r=1/2, k=2, e=8/17, alpha=pi/4: direct Gram is rational.
    actual=[]
    for i in range(4):
        row=[]
        for j in range(4):
            d=(i-j)%4
            if d==0: p=Fraction(3,1)
            elif d==2:p=Fraction(1,3)
            else:p=Fraction(3,5)
            factor=1-Fraction(8,17)*((-1)**(i+j))
            row.append(p*factor)
        actual.append(row)
    expected=[[Fraction(v,17) for v in row] for row in
              [[27,15,3,15],[15,27,15,3],[3,15,27,15],[15,3,15,27]]]
    assert actual==expected
    null=[1,-1,1,-1]
    assert all(sum(actual[i][j]*null[j] for j in range(4))==0 for i in range(4))
    # Eigenvalues are 0, 24/17 (twice), 60/17, by circulant DFT.
    return True

def main():
    assert exact_four()
    rng=random.Random(140025)
    comparisons=0
    for r in (0.2,0.5,0.75):
        for k in (1,2,3,4,5,6):
            edge=threshold(r,k)
            for e in (0.0,edge*0.9,-edge*0.9,edge,-edge):
                angles=[rng.uniform(0,2*PI) for _ in range(4)]
                weights=[complex(rng.uniform(-1,1),rng.uniform(-1,1)) for _ in range(4)]
                a=quadratic(r,k,e,angles,weights)
                b=series_quadratic(r,k,e,angles,weights)
                assert abs(a.imag)<2e-11
                assert abs(a.real-b)<5e-9,(r,k,e,a,b)
                assert a.real>=-2e-10,(r,k,e,a)
                comparisons+=1
            for side in (-1,1):
                e=side*edge
                angles,weights=polygon(r,k,e)
                # The exact polygon energy identity holds for both signs.
                predicted=(2*k)**2/(1-r**(2*k))*(2*r**k-abs(e)*(1+r**(2*k)))
                actual=quadratic(r,k,e,angles,weights)
                assert abs(actual.real-predicted)<5e-9,(r,k,e,actual,predicted)
                assert abs(actual.imag)<5e-9
                outside=quadratic(r,k,side*edge*1.01,angles,weights)
                assert outside.real<-1e-12,(r,k,e,outside)
                # Each row of the critical polygon Gram annihilates alternating weights.
                for x in angles:
                    val=sum(kernel(r,k,e,x,y)*w for y,w in zip(angles,weights))
                    assert abs(val)<5e-10,(r,k,e,x,val)
                comparisons+=3
    print('PASS: exact rational four-gon, Fourier vs spatial quadratic, '
          'signed polygon sharpness and nullity; checks=',comparisons)

if __name__=='__main__':main()
