#!/usr/bin/env python3
"""Reproduce first-Hermite infinite-strip scalar calculations (supplementary)."""
import math

ROOT_PI=math.sqrt(math.pi)
COUNT=0

def check(condition, message):
    global COUNT
    COUNT += 1
    if not condition:
        raise AssertionError(message)

def close(x,y,tol=5e-11):
    return abs(x-y) <= tol * max(1.0,abs(x),abs(y))

def w(t):
    return 2.0*t*t*math.exp(-t*t)/ROOT_PI

def J(t):
    return 0.5*math.erf(t)-t*math.exp(-t*t)/ROOT_PI

def F(a,t):
    return J(t+a)-J(t-a)

def bisect(f,lo,hi,n=100):
    flo,fhi=f(lo),f(hi)
    assert flo*fhi < 0
    for _ in range(n):
        mid=(lo+hi)/2
        if f(mid)*flo > 0:
            lo,flo=mid,f(mid)
        else:
            hi=mid
    return (lo+hi)/2

def b(a):
    return bisect(lambda t:a/math.tanh(a*t)-t,a,a+5)

def u(a):
    assert a>1.0
    return bisect(lambda t:a*math.tanh(a*t)-t,1e-6,a)

def difference(a):
    return F(a,0)-F(a,b(a))

a_star=bisect(difference,1.0,2.0)
check(close(a_star,1.0776636283762369,1e-12),'critical width')
check(close(b(a_star),1.238236621768071,1e-12),'critical outer peak')
check(close(F(a_star,0),0.4918172428288642,1e-12),'critical norm')
check(close(J(50),.5),'primitive positive endpoint')
check(close(J(-50),-.5),'primitive negative endpoint')
for t in [i/41 for i in range(-400,401)]:
    eps=1e-5
    deriv=(J(t+eps)-J(t-eps))/(2*eps)
    check(close(deriv,w(t),2e-9),f'primitive derivative at {t}')
for a in [.2,.5,.9,1,1.02,1.05,a_star,1.1,1.3,2.0,3.0]:
    outer=b(a)
    check(outer>a,'outer critical point lies beyond edge')
    check(close(outer,a/math.tanh(a*outer),1e-12),'outer equation')
    check(close(w(outer+a),w(outer-a),1e-11),'outer density balance')
    check(close(F(a,-outer),F(a,outer),1e-12),'reflection symmetry')
    check(close(F(a,0),2*J(a),1e-12),'central mass')
    central=F(a,0)
    extreme=F(a,outer)
    maximum=max(central,extreme)
    for i in range(1001):
        t=-max(outer+4,5)+2*max(outer+4,5)*i/1000
        check(F(a,t)<=maximum+4e-13,'global maximum condition')
        check(F(a,t)>=-4e-13,'positivity')
    if a>1:
        inner=u(a)
        check(0<inner<a,'inner critical point')
        check(close(inner,a*math.tanh(a*inner),1e-12),'inner equation')
        check(F(a,inner)<min(central,extreme) if a<2.5 else F(a,inner)<=min(central,extreme)+1e-12,'inner valley below peaks (rounded at large width)')
        for i in range(1,201):
            t=inner*i/201
            check(w(t+a)<w(t-a),'decreasing from center to inner valley')
        for i in range(1,201):
            t=inner+(outer-inner)*i/201
            check(w(t+a)>w(t-a),'increasing from valley to outer peak')
    else:
        check(extreme>central,'outer global peak through central local threshold')
    for i in range(1,201):
        t=outer+3*i/200
        check(w(t+a)<w(t-a),'decaying tail')
for i in range(101):
    a=1+0.01*i
    check(difference(a+.0001)>difference(a),'strict central-minus-outer growth')
check(difference(1)<0,'first threshold below global switch')
check(difference(1.1)>0,'global switch below 1.1')
for a in [.6,1.05,1.1,1.7]:
    outer=b(a)
    critical=[0,outer]
    if a>1:
        critical=[0,u(a),outer]
    values=sorted(set([F(a,t) for t in critical]))
    # A grid on both sides of each interior critical level checks branch count.
    for j in range(len(values)-1):
        level=(values[j]+values[j+1])/2
        branch_count=0
        bound=outer+5
        grid=[bound*i/1000 for i in range(1001)]
        for i in range(1000):
            y0=F(a,grid[i])-level
            y1=F(a,grid[i+1])-level
            if y0*y1<0:
                branch_count+=1
        if a<=1:
            expected=1 if level<F(a,0) else 2
        else:
            valley=F(a,u(a)); center=F(a,0); outerheight=F(a,outer)
            expected=(1 if level<center and level>valley else 0)+(1 if level<outerheight and level>valley else 0)+(1 if level<outerheight else 0)
        check(branch_count==expected,f'spectral inverse branches {a}, {level}: {branch_count} vs {expected}')
print(f'{COUNT} supplementary checks passed; a_star={a_star:.16f}; b_star={b(a_star):.16f}; M_star={F(a_star,0):.16f}')
