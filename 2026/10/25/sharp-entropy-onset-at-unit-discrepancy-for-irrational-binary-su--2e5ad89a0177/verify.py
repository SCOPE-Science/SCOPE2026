#!/usr/bin/env python3
"""Finite checks for binary irrational-discrepancy corridors; not a proof."""
import math

def check(alpha, B, theta, eps, radius=260):
    def fract(v): return v-math.floor(v)
    base={i:math.floor((i+1)*alpha+theta)-math.floor(i*alpha+theta)
          for i in range(-radius-110,radius+111)}
    eligible=[i for i in range(-radius-100,radius+100)
              if 1-alpha-eps < fract(i*alpha+theta) < 1-alpha]
    assert all(base[i:i+1] if False else (base[i],base[i+1])==(0,1) for i in eligible)
    assert all(eligible[k+1]-eligible[k]>=2 for k in range(len(eligible)-1))
    for phase in range(4):
        word=base.copy()
        for j,i in enumerate(eligible):
            if (j+phase)%4 in (0,1):
                word[i],word[i+1]=1,0
        bound=0.0
        for a in range(-radius,radius+1,13):
            s=0
            for n in range(1,90):
                s+=word[a+n-1]
                bound=max(bound,abs(s-alpha*n))
        assert bound < B, (alpha,B,bound)
    count=sum(-radius<=i<=radius-2 for i in eligible)
    assert abs(count/(2*radius)-eps)<0.012, (count,eps)
    return len(eligible)

if __name__=='__main__':
    for alpha in ((math.sqrt(5)-1)/2, math.sqrt(2)-1):
        for B in (1.05,1.20,1.45):
            eps=0.5*min(B-1,alpha,1-alpha)
            check(alpha,B,0.271,eps)
    print('PASS: six slope/corridor cases, four independent exchange choices each')
