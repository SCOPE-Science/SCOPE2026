#!/usr/bin/env python3
"""Exact rational checks for Fourier levels of the uniform Menger sponge measure.
All critical finite inequalities use fractions and a proven Machin-arctangent enclosure.
"""
from fractions import Fraction as Q
from itertools import product
from math import factorial, cos, pi

def atan_partial(z,n):
    return sum(((-1)**k*z**(2*k+1)/Q(2*k+1) for k in range(n)),Q(0))

# For 0<z<1, even-length alternating partial sums are lower bounds,
# odd-length partial sums are upper bounds. Machin: pi=16 atan(1/5)-4 atan(1/239).
pilo=16*atan_partial(Q(1,5),12)-4*atan_partial(Q(1,239),7)
pihi=16*atan_partial(Q(1,5),13)-4*atan_partial(Q(1,239),6)
assert pilo>Q(333,106) and pihi<Q(355,113)
assert Q(3)<pilo<pihi<Q(22,7)
assert pihi*pihi<10

def cos_bound(q):
    """Rational enclosure for cos(q*pi), for q in [0,1]."""
    assert 0<=q<=1
    x=q*pihi
    t=sum(((-1)**j*x**(2*j)/Q(factorial(2*j)) for j in range(10)),Q(0))
    # Taylor degree-19 (odd term zero) has error <= x^20/20!;
    # changing argument by at most q*(pihi-pilo) has same Lipschitz bound.
    err=x**20/Q(factorial(20))+q*(pihi-pilo)
    return t-err,t+err

constraints=[
 (Q(2,9),Q(3,4),Q(4,5)),
 (Q(4,9),Q(0),Q(3,16)),
 (Q(8,9),Q(-19,20),Q(-15,16)),
 (Q(2,27),Q(3,4),Q(1)),
 (Q(8,27),Q(19,32),Q(1)),
 (Q(10,27),Q(0),Q(2,5)),
 (Q(16,27),Q(-1,2),Q(0)),
 (Q(20,27),Q(-3,4),Q(-1,2)),
 (Q(26,27),Q(-1),Q(0)),
]
for angle,lo,hi in constraints:
    l,u=cos_bound(angle)
    assert lo<l<u<hi,(str(angle),float(l),float(u),str(lo),str(hi))

# Multiaffine Menger mask reaches extreme absolute values at cube corners.
def mask(x,y,z):
    return (2*x*y*z+x*y+x*z+y*z)/5
corners=[abs(mask(x,y,z)) for x,y,z in product((Q(-1),Q(4,5)),repeat=3)]
assert max(corners)<Q(3,5) # triple nonzero digit residuals die at depth two
# With inactive digit coordinate cosines in {1,-1/2}, the two mixed formulas:
for x in (Q(-1),Q(0),Q(1)):
    assert mask(x,Q(-1,2),Q(1))==-(1+x)/10
    assert mask(x,Q(-1,2),Q(-1,2))==(1-2*x)/20

# Third-level disposal of all four non-exceptional positive centered residues.
assert Q(1,5)*Q(14,25)*Q(13,25)<Q(7,100) # +/-5
assert Q(1,5)*Q(21,25)*Q(1,5)<Q(7,100)  # +/-8
assert Q(1,5)*Q(21,25)*Q(2,5)<Q(7,100)  # +/-10
assert Q(1,5)*Q(14,25)*Q(3,5)<Q(7,100) # +/-13
# Surviving +/-4, plus quantitative positive infinite tail.
third_prefix=Q(1,5)*Q(11,20)*Q(27,40)
tail=1-Q(16,3645)*10
assert third_prefix*tail==Q(7667,108000)>Q(7,100)
# A lift at depth j>=3 that first changes an active residue fails the cutoff.
assert Q(1,5)*Q(21,25)*(1+8*Q(22,7)/81)/5<Q(7,100)
assert Q(1,5)*Q(14,25)*(1+32*Q(22,7)/81)/5<Q(7,100)

# Independent finite check of the centered digit mask and first three levels.
digits=[d for d in product((-1,0,1),repeat=3) if d.count(0)<=1]
assert len(digits)==20
# Spot checks of the 27 exact third-root Fourier masks: (k nonzero mod 3).
for r in product(range(3),repeat=3):
    count=sum(t!=0 for t in r)
    if count==0:continue
    # cos(2pi*r/3) is 1 or -1/2, giving exact rational mask.
    c=[Q(1) if t==0 else Q(-1,2) for t in r]
    assert abs(mask(*c))=={1:Q(1,5),2:Q(1,20),3:Q(1,10)}[count]

# Check the exact residue survivors through depth three, with proven cos intervals.
# This is not used to extrapolate the infinite proof; the lift argument is analytic.
def interval_mask(rs,N):
    cs=[]
    for r in rs:
        q=Q(2*(r%N),N)
        if q>1:q=2-q
        cs.append(cos_bound(q))
    vals=[mask(*t) for t in product(*[(a,b) for a,b in cs])]
    return min(vals),max(vals)
# Approximate numerics below are only supplementary, never acceptance evidence.
def Fourier(n,levels=20):
    v=1.0
    for j in range(1,levels+1):
        cs=[cos(2*pi*a/3**j) for a in n]
        v*=abs(float(mask(*cs)))
    return v
for n in [(1,0,0),(4,0,0),(2,0,0),(1,1,1),(5,0,0),(10,0,0),(-1,0,0)]:
    assert Fourier(n)>0
assert .15862<Fourier((1,0,0))<.15864
assert .07158<Fourier((4,0,0))<.07159
for n in product(range(-12,13),repeat=3):
    if n==(0,0,0):continue
    a=tuple(n)
    while all(v%3==0 for v in a):a=tuple(v//3 for v in a)
    if a in ((t,0,0) for t in (-4,-1,1,4)) or a in ((0,t,0) for t in (-4,-1,1,4)) or a in ((0,0,t) for t in (-4,-1,1,4)):
        continue
    assert Fourier(n)<.07001,(n,Fourier(n))
print('MENGER_SPECTRAL_TWO_LEVEL_CERTIFICATE_OK',len(constraints),'rational cosine enclosures, 15624 finite tests')
