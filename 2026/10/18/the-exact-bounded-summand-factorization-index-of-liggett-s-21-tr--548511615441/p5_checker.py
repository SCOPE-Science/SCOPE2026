"""Exact rational certificate for a sum-of-bounded-variables factorization index.
Only Python's standard library is required. Execute: python p5_checker.py
"""
from fractions import Fraction as F
from math import comb
from functools import lru_cache

# Integer generating polynomial for Y = floor(3X/5), X ~ Bin(21, 1/2).
coeff = tuple(sum(comb(21, j) for j in range(22) if 3*j//5 == t)
              for t in range(13))
assert coeff == (22,1540,5985,74613,319770,293930,705432,497420,
                 116280,74613,7315,210,22)
assert sum(coeff) == 2**21

# Complex centers rationalized to 9 digits. Four real roots then four upper-half roots.
centers = (
    ("-9.237621391", "0"),
    ("-1.376162279", "0"),
    ("-0.258889384", "0"),
    ("-0.015007664", "0"),
    ("0.010417789", "0.144062467"),
    ("0.059525176", "0.675632118"),
    ("0.229170259", "2.541421787"),
    ("0.371999864", "17.995777456"),
)
rad = F(1, 10**5)

# Exact rational complex numbers as (real, imaginary) tuples.
def cadd(a,b): return (a[0]+b[0],a[1]+b[1])
def cmul(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def cnorm1(a):return abs(a[0])+abs(a[1])
def cpow(a,n):
    s=(F(1),F(0))
    for _ in range(n):s=cmul(s,a)
    return s

def eval_deriv_at(c):
    # Taylor coefficients P(c+t), computed via exact binomial expansion.
    powc=[cpow(c,i) for i in range(13)]
    out=[]
    for k in range(13):
        s=(F(0),F(0))
        for i in range(k,13):
            s=cadd(s,(powc[i-k][0]*comb(i,k)*coeff[i],
                      powc[i-k][1]*comb(i,k)*coeff[i]))
        out.append(s)
    return out

for re,im in centers:
    c=(F(re),F(im))
    t=eval_deriv_at(c)
    left=cnorm1(t[0])+sum(cnorm1(t[i])*rad**i for i in range(2,13))
    right=max(abs(t[1][0]),abs(t[1][1]))*rad
    assert left < right, ('Root disk fails Rouche test', re, im)
# Disjoint disks: center separations (in a max-coordinate lower bound) > 2 radius.
allcenters=[(F(a), F(b)) for a,b in centers]
allcenters += [(F(a),-F(b)) for a,b in centers[4:]]
for i in range(len(allcenters)):
    for j in range(i):
        assert max(abs(allcenters[i][0]-allcenters[j][0]),
                   abs(allcenters[i][1]-allcenters[j][1])) > 2*rad

# Interval arithmetic over exact rationals, with rounding entirely excluded.
def I(a,b=None):
    return (F(a),F(a if b is None else b))
def plus(a,b):return (a[0]+b[0],a[1]+b[1])
def neg(a):return (-a[1],-a[0])
def times(a,b):
    p=[x*y for x in a for y in b]
    return (min(p), max(p))
def poly_times(a,b):
    out=[I(0) for _ in range(len(a)+len(b)-1)]
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]=plus(out[i+j],times(x,y))
    return tuple(out)

# Eight real irreducible factors: four linears and four conjugate-pair quadratics.
factors=[]
for a,b in centers[:4]:
    v=I(F(a)-rad,F(a)+rad)
    factors.append((neg(v),I(1)))
for a,b in centers[4:]:
    u=I(F(a)-rad,F(a)+rad)
    v=I(F(b)-rad,F(b)+rad)
    # all upper-half center imag > radius; direct square is legitimate here.
    s=plus(times(u,u),times(v,v))
    factors.append((s, times(I(-2),u), I(1)))

@lru_cache(None)
def group(mask):
    res=(I(1),)
    for j in range(8):
        if mask>>j&1:res=poly_times(res,factors[j])
    return res

def degree(mask):return sum((1 if j<4 else 2) for j in range(8) if mask>>j&1)

# An explicit three-factor decomposition of degrees 2, 5, 5.
cover=(0b00001001,0b00110100,0b11000010)
assert sum(cover) == 255 and (cover[0]|cover[1]|cover[2])==255
assert tuple(degree(mask) for mask in cover)==(2,5,5)
for mask in cover:
    poly=group(mask)
    assert all(lo>0 for lo,hi in poly), ('Positive factor not certified',mask)

# A rigorous NO-cover certificate for maximum degree four. Any genuine
# nonnegative factor must be among the optimistic candidates whose interval
# upper bounds are all nonnegative. Thus allowing ambiguous factors only
# strengthens the impossibility conclusion.
possible=[mask for mask in range(1,256) if degree(mask)<=4 and
          all(hi>=0 for lo,hi in group(mask))]
reachable={0}
for _ in range(12):
    extra={s|g for s in reachable for g in possible if not(s&g)}
    reachable |= extra
assert 255 not in reachable, 'Degree-four decomposition not excluded'
print('PASS: integer coefficients, 12 individually isolated simple roots,')
print('three strictly positive factors of degrees 2+5+5;')
print('no nonnegative-factor partition at maximum degree 4.')
print('Optimistic degree<=4 factors:',len(possible))
