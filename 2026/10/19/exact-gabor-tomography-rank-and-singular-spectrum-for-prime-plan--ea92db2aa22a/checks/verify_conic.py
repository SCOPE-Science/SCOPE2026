"""Finite prime-plane conic indicator Gabor ambiguity: exact support and numerical spectra.

This is a stand-alone arithmetic checker for representative primes; the mathematical
proof for all primes is in RESULT.md.
"""
import cmath
from collections import Counter
from math import pi


def quadratic_character(a,p):
    a %= p
    return 0 if a == 0 else (1 if pow(a,(p-1)//2,p)==1 else -1)


def check(p,d):
    d %= p
    eps=quadratic_character(d,p)
    m=p-eps
    C={(x,y) for x in range(p) for y in range(p) if (x*x-d*y*y)%p==1}
    assert len(C)==m
    norm=lambda x,y:(x*x-d*y*y)%p
    zeta=cmath.exp(2j*pi/p)
    nshift=Counter()
    spectral=Counter()
    norm_spectral=Counter()
    nonempty=set()
    for a in range(p):
      for b in range(p):
        h=(a,b)
        S=[(x,y) for x,y in C if ((x-a)%p,(y-b)%p) in C]
        nshift[len(S)]+=1
        if S: nonempty.add(h)
        for u in range(p):
          for v in range(p):
            counts=[0]*p
            for x,y in S: counts[(u*x+v*y)%p]+=1
            is_zero=len(set(counts))==1
            assert is_zero == (not S), (p,d,h,(u,v),S,counts)
            if S:
              amp=sum(zeta**((u*x+v*y)%p) for x,y in S)
              if h==(0,0):
                if (u,v)==(0,0): target=m
                else:
                  zz=(u*u - pow(d,-1,p)*v*v)%p
                  target=eps*sum(zeta**((-t-zz*pow(4*t,-1,p))%p) for t in range(1,p))
                assert abs(amp-target)<2e-10,(p,d,h,(u,v),amp,target)
              elif len(S)==1:
                assert abs(abs(amp)-1)<2e-10
              elif len(S)==2:
                x,y=S
                j=((u*(x[0]-y[0])+v*(x[1]-y[1]))%p)
                assert abs(abs(amp)-abs(2*cmath.cos(pi*j/p)))<2e-10
              else:
                raise AssertionError((p,d,h,S))
              spectral[len(S)]+=1
              norm_spectral[(norm(a,b),len(S))]+=1
    expected={0:p*p-1-m*m//2,1:m,2:m*(m-2)//2,m:1}
    assert nshift==Counter(expected),(p,d,nshift,expected)
    assert len(nonempty)==1+m*m//2
    rank=p*p*len(nonempty)
    assert sum(spectral.values())==rank
    print(f'p={p} d={d} chi(d)={eps:+d} conic={m} shift_counts={dict(nshift)} rank={rank} nullity={p**4-rank}')


def main():
    for p in (5,7,11,13,17):
      for eps in (+1,-1):
        d=next(d for d in range(1,p) if quadratic_character(d,p)==eps)
        check(p,d)
    print('PASS: ten conics; exact support, intersections, ranks, Kloosterman and cosine magnitudes')

if __name__=='__main__':main()
