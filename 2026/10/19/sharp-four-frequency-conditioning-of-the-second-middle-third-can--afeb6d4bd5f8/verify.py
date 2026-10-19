#!/usr/bin/env python3
"""Exact rational proof checker for the two-stage ternary Cantor Fourier conditioning theorem.
No third-party dependencies. Every inequality is checked in rational arithmetic.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import factorial, isqrt

def atan_interval(q, n=30):
    s=sum(((-1)**k)*Q(1, (2*k+1)*q**(2*k+1)) for k in range(n))
    e=Q(1, (2*n+1)*q**(2*n+1))
    return (s, s+e) if n%2==0 else (s-e, s)

def pi_interval():
    a=atan_interval(5); b=atan_interval(239)
    return (16*a[0]-4*b[1], 16*a[1]-4*b[0])

def cos_interval(k, pi_bounds, terms=45):
    # Calculate cos(k*pi) via a Taylor polynomial at the midpoint,
    # then bound Taylor and pi-argument error separately.
    p=(pi_bounds[0]+pi_bounds[1])/2
    x=k*p
    val=sum((-1)**j*x**(2*j)/factorial(2*j) for j in range(terms))
    e=abs(x)**(2*terms)/factorial(2*terms)+abs(k)*(pi_bounds[1]-pi_bounds[0])/2
    return val-e,val+e

S=10**12
P=pi_interval()
assert Q(314159265358979323846,10**20)<P[0]<P[1]<Q(314159265358979323847,10**20)
# Coefficients t_r are the rephased column-correlation values.
bounds={0:(S,S),3:(-S//2,-S//2)}
for r in (1,2,4):
    v1=cos_interval(Q(4*r,9),P)
    v2=cos_interval(Q(8*r,9),P)
    lo=(v1[0]+v2[0])/2; hi=(v1[1]+v2[1])/2
    floorlo=(lo.numerator*S)//lo.denominator
    ceilhi=-((-hi.numerator*S)//hi.denominator)
    # whole grid intervals enclose the exact trigonometric values
    assert Q(floorlo,S)<=lo<=hi<=Q(ceilhi,S)
    bounds[r]=(floorlo,ceilhi)
assert bounds[1]==(-383022221560,-383022221559),bounds
assert bounds[2]==(-86824088834,-86824088833),bounds
assert bounds[4]==(469846310392,469846310393),bounds

def dist(a,b):
    r=abs(a-b)%9
    return min(r,9-r)

def translate(F,t):
    return tuple(sorted((x+t)%9 for x in F))

def canon(F):
    return min(translate(F,t) for t in range(9))

reps=sorted({canon(F) for F in combinations(range(9),4)})
assert len(reps)==14
assert all(sum(canon(F)==R for F in combinations(range(9),4))==9 for R in reps)

# Pairs of rational test vectors, approximating least and greatest eigenvectors.
# These only *witness* a Rayleigh quotient bound; their provenance is immaterial.
W={
(0,1,2,3):((530,468,468,530),(546,-449,449,-546)),
(0,1,2,4):((109,708,479,508),(-532,597,-143,-582)),
(0,1,2,5):((560,546,-59,-621),(-178,-486,565,-642)),
(0,1,2,6):((59,-546,-560,621),(565,-486,-178,-642)),
(0,1,2,7):((479,708,109,508),(-143,597,-532,-582)),
(0,1,3,4):((-418,-570,-570,-418),(570,-418,-418,570)),
(0,1,3,5):((610,515,313,-514),(670,47,-525,523)),
(0,1,3,6):((-577,0,-577,-577),(-519,558,-118,637)),
(0,1,3,7):((-630,-630,-321,-321),(-321,-321,630,630)),
(0,1,4,5):((-611,-356,356,611),(-356,611,-611,356)),
(0,1,4,6):((461,-461,-536,536),(-536,536,-461,461)),
(0,1,4,7):((0,-577,-577,-577),(558,-519,637,-118)),
(0,1,5,7):((515,610,-514,313),(-47,-670,-523,525)),
(0,2,4,6):((607,-362,-362,607),(-581,404,-404,581)),
}
assert set(reps)==set(W)

def rayleigh_interval(F,v):
    # Integer numerator divided by S*|v|^2. For each cross term,
    # choose the interval endpoint that gives the rigorous bound.
    norm=sum(x*x for x in v)
    lo=hi=S*norm
    for i in range(4):
      for j in range(i+1,4):
        k=2*v[i]*v[j]
        l,u=bounds[dist(F[i],F[j])]
        lo+=min(k*l,k*u)
        hi+=max(k*l,k*u)
    return Q(lo,S*norm),Q(hi,S*norm)

R=(0,1,3,7)
# Prove every other translation class has squared spectral condition >57/10.
for F in reps:
    if F==R:continue
    vl,vu=W[F]
    lower=rayleigh_interval(F,vu)[0]  # lambda_max >= Rayleigh(u)
    upper=rayleigh_interval(F,vl)[1]  # lambda_min <= Rayleigh(v)
    assert lower>0,(F,lower)
    assert 10*lower > 57*upper,(F,lower,upper)
print('13 nonoptimal translation classes: EXACT RATIONAL RAYLEIGH SEPARATION >57/10: PASS')

# Interval arithmetic for the two 2-by-2 Gram blocks of the optimal class.
def interval_add(a,b):return a[0]+b[0],a[1]+b[1]
def interval_neg(a):return -a[1],-a[0]
def interval_sub(a,b):return interval_add(a,interval_neg(b))
def interval_mul(a,b):
    xx=[x*y for x in a for y in b]
    return min(xx),max(xx)
def interval_sqrt(a,scale=10**12):
    assert a[0]>0
    def floor_root(q):
      return isqrt(q.numerator*scale*scale//q.denominator)
    l=floor_root(a[0]); u=floor_root(a[1])+1
    assert Q(l*l,scale*scale)<=a[0] and Q(u*u,scale*scale)>a[1]
    return Q(l,scale),Q(u,scale)

def qinterval(r):return Q(bounds[r][0],S),Q(bounds[r][1],S)
a,b,c=qinterval(1),qinterval(2),qinterval(4)
half=(Q(1,2),Q(1,2))
two=(Q(2),Q(2))
def eigen_blocks(sign):
  trace=interval_add(two,interval_add(a,c) if sign==1 else interval_neg(interval_add(a,c)))
  diff=interval_sub(a,c)
  cross=interval_sub(b,half) if sign==1 else interval_add(b,half)
  discriminant=interval_add(interval_mul(diff,diff),interval_mul((2*cross[0],2*cross[1]),(2*cross[0],2*cross[1])))
  root=interval_sqrt(discriminant)
  lo=interval_mul(interval_sub(trace,root),(Q(1,2),Q(1,2)))
  hi=interval_mul(interval_add(trace,root),(Q(1,2),Q(1,2)))
  return lo,hi
pmin,pmax=eigen_blocks(1)
mmin,mmax=eigen_blocks(-1)
assert pmin[0]>Q(317,1000) and pmax[1]<Q(1770,1000)
assert pmin[1]<mmin[0] and mmax[1]<pmax[0]
assert pmin[0]>0 and Q(1770,1000)/Q(317,1000)<Q(57,10)
print('Unique optimal class and algebraic extremal block: EXACT RATIONAL CHECK PASS')
print('all optimal sets', [translate(R,t) for t in range(9)])
print('opt squared condition interval',pmax[0]/pmin[1],pmax[1]/pmin[0])
print('minimum condition interval',float(pmax[0]/pmin[1])**.5,float(pmax[1]/pmin[0])**.5)
print('no floating-point decisions were used in this checker')
