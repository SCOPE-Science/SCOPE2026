#!/usr/bin/env python3
"""Finite symbolic/numerical checks for the Gaussian grid-peak sampling-loss theorem."""
from fractions import Fraction
import math
import random
import sympy as s
import mpmath as mp

def symbolic():
    # h = mesh, M_2j = even spectral moments. Work with y=h^2.
    y,M2,M4,M6=s.symbols('y M2 M4 M6', positive=True)
    V=M2*y/2 - M4*y*y/24 + M6*y**3/720
    V2=4*M2*y/2 - 16*M4*y*y/24 + 64*M6*y**3/720
    eps=s.factor((4*V-V2)/(2*V))
    a=s.simplify(s.limit(eps/y,y,0))
    b=s.simplify(s.limit((eps/(a*y)-1)/y,y,0))
    # arccos(1-epsilon)=sqrt(2epsilon)*(1+epsilon/12+O(epsilon^2))
    relative=s.factor(b/2 + a/12)
    wanted=(M4*M4-M2*M6)/(12*M2*M4)
    assert s.simplify(relative-wanted)==0
    assert s.simplify(a-M4/(2*M2))==0
    print('SYMBOLIC: normalized O(h^2) coefficient =',relative)
    print('SYMBOLIC: equals - (M2*M6-M4^2)/(12*M2*M4): YES')


def probability(r,h):
    v=1-r(h)
    if v==0: return mp.mpf('0')
    gamma=(2*r(h)-1-r(2*h))/(2*v)
    return mp.acos(max(-1,min(1,gamma)))/(2*mp.pi)

def cases():
    mp.mp.dps=80
    models=[
        ('squared exponential',lambda h: mp.exp(-h*h/2),mp.mpf(1),mp.mpf(3),mp.mpf(15)),
        ('two harmonics', lambda h: (mp.cos(h)+mp.cos(2*h))/2,mp.mpf(5)/2,mp.mpf(17)/2,mp.mpf(65)/2),
        ('monochromatic', lambda h: mp.cos(h),mp.mpf(1),mp.mpf(1),mp.mpf(1)),
        ('monochromatic + constant', lambda h: mp.mpf('0.7')+mp.mpf('0.3')*mp.cos(2*h),mp.mpf('1.2'),mp.mpf('4.8'),mp.mpf('19.2')),
    ]
    assertions=0
    for name,r,m2,m4,m6 in models:
        J=mp.sqrt(m4/m2)/(2*mp.pi)
        loss=(m2*m6-m4*m4)/(12*m2*m4)
        print(name,'J=',mp.nstr(J,25),'spectral_loss=',mp.nstr(loss,25))
        for h in [mp.mpf('0.07'), mp.mpf('0.035'), mp.mpf('0.0175'), mp.mpf('0.00875')]:
            p=probability(r,h)
            est=(J-p/h)/(J*h*h)
            # second-order approximation has O(h^2) normalized error.
            if loss>0:
                assert abs(est-loss)<mp.mpf('0.02')
                assertions+=1
            else:
                assert abs(p/h-J)<mp.mpf('1e-65')
                assertions+=1
            assert p/h<=J+mp.mpf('1e-65')
            assertions+=1
            print(' ',mp.nstr(h,7),'p/h=',mp.nstr(p/h,18),'normalized loss=',mp.nstr(est,14))
    # Weighted Jensen/Chebyshev strictness below the highest spectral frequency.
    rng=random.Random(1729)
    trials=96
    for _ in range(trials):
        freqs=[mp.mpf(str(rng.uniform(.15,5))) for i in range(4)]
        weights=[mp.mpf(str(rng.uniform(.1,1))) for i in range(4)]
        weights=[w/sum(weights) for w in weights]
        m2=sum(w*f*f for w,f in zip(weights,freqs))
        m4=sum(w*f**4 for w,f in zip(weights,freqs))
        J=mp.sqrt(m4/m2)/(2*mp.pi)
        h=mp.pi/(max(freqs)*mp.mpf(str(rng.uniform(1,3))))
        r=lambda t: sum(w*mp.cos(f*t) for w,f in zip(weights,freqs))
        assert probability(r,h)/h < J
        assertions+=1
    print('BANDLIMITED strict-inequality cases passed:',trials)
    print('NUMERICAL assertions passed:',assertions)

if __name__=='__main__':symbolic();cases()
