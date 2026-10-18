"""Standalone checks for the three-capacity escort benchmark. No network or external packages."""
from fractions import Fraction
from math import isclose, sqrt, log, exp

def limits(b):
    return max(0.0, b-1.0), b/2.0

def f(t,b,r):
    return (1-b+t)**r + (b-2*t)**r + t**r

def df(t,b,r):
    return r*((1-b+t)**(r-1) - 2*(b-2*t)**(r-1) + t**(r-1))

def optimum(b,q):
    assert 0 < b < 2 and q > 0 and q != 1
    r = 1/q
    left,right=limits(b)
    if r > 1: # strict convex minimum
        if df(left,b,r)>=0: return left
        if df(right,b,r)<=0: return right
        for _ in range(110):
            mid = (left+right)/2
            if df(mid,b,r)<0: left=mid
            else: right=mid
    else: # strict concave maximum (infinite endpoint slopes)
        for _ in range(110):
            mid=(left+right)/2
            if df(mid,b,r)>0:left=mid
            else:right=mid
    return (left+right)/2

# Exact q=1/2 complete phase diagram: finite algebra identities.
for k in range(1,200):
    b=Fraction(k,100)
    left=max(Fraction(0),b-1)
    right=b/2
    tstar=min(right,max(left,(3*b-1)/6))
    # expansion of sum square of the linear y coordinates
    derivative=Fraction(2)*(1-3*b+6*tstar)
    if tstar==left: assert derivative>=0
    elif tstar==right: assert derivative<=0
    else: assert derivative==0
    vertex= (1-b+tstar,b-2*tstar,tstar)
    assert all(z>=0 for z in vertex)
    assert sum(vertex)==1 and vertex[1]+2*vertex[2]==b
    bflt=float(b)
    assert abs(optimum(bflt,0.5)-float(tstar))<2e-14

for q in (0.1,0.25,0.4,0.5,0.8,0.95,1.01,1.5,2,5,30):
    r=1/q
    thresh=1/(1+2**(q/(1-q))) if q<1 else None
    for k in range(1,200):
        b=k/100
        t=optimum(b,q)
        lo,hi=limits(b)
        assert lo-1e-12<=t<=hi+1e-12
        assert abs((1-b+t)+(b-2*t)+t-1)<1e-10
        if q<1:
            if b<thresh-1e-9: assert abs(t)<1e-12, (q,b,t,thresh)
            if b>2-thresh+1e-9: assert abs(t-(b-1))<1e-12,(q,b,t,thresh)
            if thresh+1e-8<b<2-thresh-1e-8: assert t>max(lo,1e-13) and t<hi
        else:
            assert t>lo and t<hi

# q=1/2, b=1/4: p = (9/10,1/10,0), D = 8/5.
y=(Fraction(3,4),Fraction(1,4),Fraction(0))
p=tuple(u*u/sum(v*v for v in y) for u in y)
assert p==(Fraction(9,10),Fraction(1,10),Fraction(0))
assert 1/sum(v*v for v in y)==Fraction(8,5)
# q=1/2, b=1: y=(1/3,1/3,1/3) gives D=3.
y=(Fraction(1,3),)*3
assert 1/sum(u*u for u in y)==3
print('PASS: exact q=1/2 certificate across 199 rational budgets;')
print('       2,189 parameter trials for strict KKT phase classification;')
print('       exact representative species weights and potential Hill numbers.')

# Leading activation exponents at the low-capacity support transition.
for q in (0.25,0.50,0.75):
    s=(1-q)/q
    k=2**(1/s)
    b0=1/(1+k)
    u0=1-b0
    K=s*(u0**(s-1)+2*b0**(s-1))
    L=s*(u0**(s-1)+4*b0**(s-1))
    if s>1:
        C=K/L; a=1.
    elif s==1:
        C=K/(L+1); a=1.
    else:
        C=K**(1/s); a=1/s
    delta=1e-4
    y3=optimum(b0+delta,q)
    assert abs(y3/(C*delta**a)-1)<0.01,(q,y3,C,delta,a)
print('PASS: asymptotic activation coefficients checked in three regimes.')
