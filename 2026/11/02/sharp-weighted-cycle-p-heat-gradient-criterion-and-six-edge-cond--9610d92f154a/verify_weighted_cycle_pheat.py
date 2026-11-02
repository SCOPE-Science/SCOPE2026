"""Independent finite checks of the weighted-cycle nonlinear heat formula.

Run: python3 verify_weighted_cycle_pheat.py
Uses Python's standard library only. Exhaustive finite grids do not replace proof.
"""
from fractions import Fraction as Q
from itertools import product
from math import isclose
from random import Random


def flux(x, p):
    return abs(x)**(p-1) if x >= 0 else -abs(x)**(p-1)


def H(n, p, a, b):
    if n == 3:
        if p == 3:
            return -(a*b)/(a+b)
        if p <= 2:
            return -min(a, b)
        r = 1 / (p-2)
        return -(a**(-r) + b**(-r))**(-1/r)
    if n == 4:
        return abs(a-b)
    if n == 5:
        if p >= 2:
            return max(a,b)
        r = 1/(2-p)
        return (a**r+b**r)**(1/r)
    return a+b


def derivatives(e, c, m, p):
    n = len(e)
    return [c[(i+1)%n]/m[(i+1)%n]*flux(e[(i+1)%n],p)
            +c[(i-1)%n]/m[i]*flux(e[(i-1)%n],p)
            -c[i]*(1/m[i]+1/m[(i+1)%n])*flux(e[i],p)
            for i in range(n)]


def rates(c, m, p):
    n=len(c)
    return [H(n,p,c[(i-1)%n]/m[i],c[(i+1)%n]/m[(i+1)%n])
            -c[i]*(1/m[i]+1/m[(i+1)%n]) for i in range(n)]


def witness(n, i, p, a, b):
    e=[0]*n
    e[i]=1
    left,right=(i-1)%n,(i+1)%n
    if n==3:
        h=(1 if a<b else 0) if p<=2 else (b/(a+b) if p==3 else a**(-1/(p-2))/(a**(-1/(p-2))+b**(-1/(p-2))))
        e[left],e[right]=-h,-(1-h)
    elif n==4:
        e[left],e[right]=(1,-1) if a>=b else (-1,1)
        e[(i+2)%n]=-1
    elif n==5:
        h=(1 if a>=b else 0) if p>=2 else a**(1/(2-p))/(a**(1/(2-p))+b**(1/(2-p)))
        e[left],e[right]=h,1-h
        for j in range(n):
            if j not in (i,left,right):
                e[j]=-1
    else:
        e[left]=e[right]=1
        for j in range(n):
            if j not in (i,left,right):
                e[j]=-Q(3,n-3)
    assert abs(sum(e))<1e-10 and max(abs(z) for z in e)==1
    return e


RNG=Random(24017)
tests=0
for n in range(3,13):
    for p in (1.23,1.5,2,2.7,3,4.2):
        for trial in range(8):
            c=[.5+3*RNG.random() for _ in range(n)]
            m=[.6+3*RNG.random() for _ in range(n)]
            k=rates(c,m,p)
            for i in range(n):
                a=c[(i-1)%n]/m[i]; b=c[(i+1)%n]/m[(i+1)%n]
                e=witness(n,i,p,a,b)
                assert isclose(derivatives(e,c,m,p)[i],k[i],rel_tol=1e-10,abs_tol=1e-10)
                tests+=1
            for _ in range(30):
                e=[RNG.uniform(-1,1) for _ in range(n)]
                avg=sum(e)/n
                e=[z-avg for z in e]
                peak=max(abs(z) for z in e)
                e=[z/peak for z in e]
                der=derivatives(e,c,m,p)
                active=[i for i in range(n) if abs(e[i])>=1-1e-12]
                assert max((1 if e[i]>0 else -1)*der[i] for i in active)<=max(k)+1e-9
print('NUMERIC_SHARP_WITNESSES_AND_DINI_BOUNDS_OK',tests)

# Exact p=3 rational witnesses and exact signed-gradient upper bounds.
exact=0
for n in range(3,12):
    for trial in range(10):
        c=[Q(RNG.randrange(2,23),RNG.randrange(2,13)) for _ in range(n)]
        m=[Q(RNG.randrange(2,23),RNG.randrange(2,13)) for _ in range(n)]
        k=rates(c,m,3)
        assert all(isinstance(z,Q) for z in k)
        for i in range(n):
            a=c[(i-1)%n]/m[i]; b=c[(i+1)%n]/m[(i+1)%n]
            e=[Q(z) for z in witness(n,i,3,a,b)]
            assert sum(e)==0 and max(abs(z) for z in e)==1
            assert derivatives(e,c,m,3)[i]==k[i]
            exact+=1
        for j in range(n):
            e=[Q(0)]*n
            e[j]=Q(1); e[(j+1)%n]=Q(-1)
            assert max(abs(z) for z in e)==1
            der=derivatives(e,c,m,3)
            assert max((1 if e[i]>0 else -1)*der[i] for i in range(n) if abs(e[i])==1)<=max(k)
print('EXACT_RATIONAL_CUBIC_WITNESSES_OK',exact)

# Exhaustive integer-edge slope grids: rational cubic flux and cycle closure.
grids=0
for n in range(3,9):
    c=[Q(1)+Q((3*i)%5,4) for i in range(n)]
    m=[Q(1)+Q((5*i)%7,3) for i in range(n)]
    k=max(rates(c,m,3))
    for pre in product((-1,0,1),repeat=n-1):
        e=list(map(Q,pre));e.append(-sum(e))
        if max(abs(z) for z in e)!=1:
            continue
        der=derivatives(e,c,m,3)
        assert max((1 if e[i]>0 else -1)*der[i] for i in range(n) if abs(e[i])==1)<=k
        grids+=1
print('EXACT_RATIONAL_GRID_UPPER_BOUNDS_OK',grids)

# A nonconstant pentagon shows a genuinely nonlinear phase boundary.
c=[1,1,1,1,1.5];m=[1]*5
lo,hi=1.01,1.99
for _ in range(70):
    md=(lo+hi)/2
    if max(rates(c,m,md))>0:
        lo=md
    else:
        hi=md
assert 1.336485729 < (lo+hi)/2 < 1.336485732
assert max(rates(c,m,1.2))>0 and max(rates(c,m,1.5))<0
print('PENTAGON_EXPONENT_PHASE_TRANSITION_OK',f'{(lo+hi)/2:.12f}')

# An arbitrary nonconstant conductance cycle of length at least six must expand initially.
for n in range(6,16):
    for trial in range(40):
        c=[.5+2*RNG.random() for _ in range(n)]
        m=[.5+2*RNG.random() for _ in range(n)]
        for p in (1.2,2,3.5):
            k=rates(c,m,p)
            assert abs(sum(k))<1e-10
            assert max(k)>1e-10
            assert max(abs(z) for z in rates([1]*n,m,p))<1e-10
print('SIX_VERTEX_CONDUCTANCE_RIGIDITY_CHECKS_OK')
print('ALL_WEIGHTED_CYCLE_P_HEAT_CHECKS_OK')
