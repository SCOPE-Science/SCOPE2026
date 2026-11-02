#!/usr/bin/env python3
"""Exact checks for maximum-spacing / quadratic-spacing moment theorem.
Run: python3 verify.py (Python standard library only).
Finite checks do not substitute for the analytic simplex-inclusion-exclusion proof.
"""
from fractions import Fraction as F
from math import comb, factorial, sqrt, pi, log

checks=0

def eq(a,b,msg):
    global checks
    assert a==b,(msg,a,b)
    checks+=1

# Univariate polynomial represented by ascending-power fractions.
def padd(a,b):
    c=[F(0)]*max(len(a),len(b))
    for i,z in enumerate(a):c[i]+=z
    for i,z in enumerate(b):c[i]+=z
    return c

def pmul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,ai in enumerate(a):
        for j,bj in enumerate(b):c[i+j]+=ai*bj
    return c

def ppow(a,k):
    v=[F(1)]
    for _ in range(k):v=pmul(v,a)
    return v

def integ_poly(p,a,b):
    return sum(z*(b**(i+1)-a**(i+1))/F(i+1) for i,z in enumerate(p))

# Integrate f(x,y) over a strip a<=x<=b, low(x)<=y<=high(x).
# f uses monomial dictionary {(i,j): coefficient}.
def strip(poly,a,b,low,high):
    acc=[F(0)]
    for (i,j),z in poly.items():
        q=pmul([F(0)]*i+[F(1)],padd(ppow(high,j+1),[-u for u in ppow(low,j+1)]))
        acc=padd(acc,[v*z/F(j+1) for v in q])
    return integ_poly(acc,a,b)

# For three spacings, marginal density of (X1,X2) on unit triangle is 2.
G={(2,0):F(2),(0,2):F(2),(1,1):F(2),(1,0):F(-2),(0,1):F(-2),(0,0):F(1)}
x={(1,0):F(1)}
xG={(i+1,j):z for (i,j),z in G.items()}
one={(0,0):F(1)}

def largest_region(poly):
    # X1>=X2 and X1>=1-X1-X2; multiply by 3 symmetric sectors.
    return 6*(strip(poly,F(1,3),F(1,2),[F(1),F(-2)],[F(0),F(1)])+
              strip(poly,F(1,2),F(1),[F(0)],[F(1),F(-1)]))

def truncated_m3(poly,t):
    if t==F(2,5):
        return 2*strip(poly,F(1,5),F(2,5),[F(3,5),F(-1)],[F(2,5)])
    if t==F(3,5):
        return 2*(strip(poly,F(0),F(2,5),[F(2,5),F(-1)],[F(3,5)])+
                  strip(poly,F(2,5),F(3,5),[F(0)],[F(1),F(-1)]))
    raise ValueError(t)

def harmonic(m,r=1):
    return sum((F(1,k**r) for k in range(1,m+1)),F(0))

def formula_cov(m):
    h=harmonic(m);h2=harmonic(m,2)
    return (h*h+h2-2*h)/F(m*(m+1)*(m+2))

def tail_mix(m,k,t):
    z=1-k*t
    if z<=0:return F(0),F(0)
    p=z**(m-1)
    conditional_g=k*t*t+F(2*k,m)*t*z+F(2,m+1)*z*z
    return p,p*conditional_g

def truncated_formula(m,t):
    probability=F(1)
    quadratic=F(2,m+1)
    for k in range(1,m+1):
        p,a=tail_mix(m,k,t)
        coeff=(-1)**k*comb(m,k)
        probability+=coeff*p
        quadratic+=coeff*a
    return probability,quadratic

# An independently integrated two-dimensional Dirichlet(1,1,1) density.
eq(largest_region(x),F(11,18),'m3 max mean direct')
eq(largest_region(xG),F(349,1080),'m3 max-quad moment direct')
eq(largest_region(xG)-largest_region(x)*F(1,2),F(19,1080),'m3 covariance direct')
for t in (F(2,5),F(3,5)):
    f,g=truncated_formula(3,t)
    eq(f,truncated_m3(one,t),f'm3 event integral at {t}')
    eq(g,truncated_m3(G,t),f'm3 mixed moment integral at {t}')

# m=2 direct one-dimensional calculus: max has density 2 on [1/2,1].
eq(formula_cov(2),F(1,48),'m2 independent covariance')
eq(formula_cov(3),F(19,1080),'m3 independent covariance')

for m in range(2,501):
    h=harmonic(m);h2=harmonic(m,2)
    # The inclusion-exclusion layer-cake integral is an independent finite sum.
    em=F(0); em2=F(0); emg=F(0)
    for k in range(1,m+1):
        c=(-1)**(k+1)*comb(m,k)
        em+=F(c,k*m)
        em2+=F(2*c,k*k*m*(m+1))
        emg+=F(2*c,m*(m+1)*(m+2))*(F(1,k*k)+F(m+1,k))
    eg=F(2,m+1)
    eq(em,h/m,f'EM m={m}')
    eq(em2,(h*h+h2)/F(m*(m+1)),f'EM2 m={m}')
    eq(emg-em*eg,formula_cov(m),f'Cov m={m}')
    assert formula_cov(m)>0
    checks+=1
    # Exact moment variance formulas from Dirichlet joint moments.
    v_g=F(4*(m-1),(m+1)**2*(m+2)*(m+3))
    v_m=(m*h2-h*h)/F(m*m*(m+1))
    assert v_g>0 and v_m>0
    checks+=1

# Boundary behavior of the exact truncated mixed moment at rational thresholds.
for m in range(2,30):
    for t in (F(0),F(1,m),F(1,m)+F(1,5*m),F(1,2),F(2,3),F(1)):
        p,a=truncated_formula(m,t)
        assert 0<=p<=1 and F(0)<=a<=F(2,m+1)
        if t<=F(1,m):eq(p,F(0),f'boundary CDF m={m}')
        if t==F(1):eq(a,F(2,m+1),f'upper moment m={m}')
        checks+=1

for m in (100,1000,10000):
    hm=log(m)+0.5772156649015329
    h2=float(harmonic(m,2))
    h=float(harmonic(m))
    b=h*h+h2-2*h
    corr=b*sqrt((m+1)*(m+3))/(2*sqrt((m+2)*(m-1)*(m*h2-h*h)))
    assert corr>0
    print('m',m,'corr',corr,'normalized',corr*sqrt(m)/(log(m)**2),'target',sqrt(6)/(2*pi))
    checks+=1
print('VERIFIED',checks,'assertions')
