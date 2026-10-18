"""Independent exact checks for a three-season Beverton--Holt mean-order theorem."""
from fractions import Fraction as F
from itertools import combinations, permutations
import sympy as s


def orbit_formula(r):
    u,v,w = map(F,r)
    p=u*v*w
    if p <= 1:
        raise ValueError('positive periodic orbit requires product above one')
    return ((p-1)/(1+u+u*v), (p-1)/(1+v+v*w), (p-1)/(1+w+w*u))


def direct_affine_fixed_point(r):
    """Compute fixed orbit via independent exact fractional matrix composition."""
    mul, bias = F(1),F(0)
    for rate in map(F,r):
        mul,bias=mul/rate,(bias+1)/rate
    assert mul<1
    y=bias/(1-mul)
    out=[]
    for rate in map(F,r):
        out.append(1/y)
        y=(y+1)/rate
    assert y==1/out[0]
    return tuple(out)


def mean(r):
    return sum(orbit_formula(r),F(0))/3


def gap(a,b,c):
    p=a*b*c
    d=(1+a+a*b)*(1+b+a*b)*(1+a+a*c)*(1+c+a*c)*(1+b+b*c)*(1+c+b*c)
    return (b-a)*(c-a)*(c-b)*(p-1)**2*(p+a*b+a*c+a+b*c+b+c+2)/(3*d)


a,b,c=s.symbols('a b c', positive=True)
p=a*b*c
T=lambda u,v,w:sum([1/(1+u+u*v),1/(1+v+v*w),1/(1+w+w*u)])
D=(1+a+a*b)*(1+b+a*b)*(1+a+a*c)*(1+c+a*c)*(1+b+b*c)*(1+c+b*c)
assert s.simplify((p-1)*(T(a,b,c)-T(a,c,b))*D/3-(b-a)*(c-a)*(c-b)*(p-1)**2*(p+a*b+a*c+a+b*c+b+c+2)/3)==0

checks=0
for aa,bb,cc in combinations([F(1,10), F(1,3), F(1,2), F(1), F(3,2), F(2), F(4), F(8), F(16)],3):
    if aa*bb*cc<=1:
        continue
    mm=[]
    for r in permutations((aa,bb,cc)):
        assert orbit_formula(r)==direct_affine_fixed_point(r)
        mm.append(mean(r))
    assert len(set(mm))==2
    assert mean((aa,bb,cc))>mean((aa,cc,bb))
    assert mean((aa,bb,cc))-mean((aa,cc,bb))==gap(aa,bb,cc)
    checks+=1

example=(F(1,2),F(2),F(8))
print('EXAMPLE',tuple(str(x) for x in (mean(example),mean((example[0],example[2],example[1])),gap(*example))))
for t in (10,100,1000):
    rates=(F(1,t),F(t),F(t**3))
    ratio=mean(rates)/mean((rates[0],rates[2],rates[1]))
    print('AMPLIFICATION',t,float(ratio),float(ratio/t))
    assert ratio>F(t,3)
print('CHECKED_TRIPLES',checks)
print('VERIFY_OK')
