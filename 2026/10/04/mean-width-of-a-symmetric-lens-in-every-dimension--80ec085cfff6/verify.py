#!/usr/bin/env python3
import math


def support_formula(t, c):
    q = math.sqrt(max(0.0, 1.0-t*t))
    if t <= c:
        return math.sqrt(1.0-c*c)*q
    return 1.0-c*t


def support_direct(t, c):
    q = math.sqrt(max(0.0, 1.0-t*t))
    lo, hi = c, 1.0
    # Golden-section maximization of t*(y-c)+q*sqrt(1-y^2).
    gr = (math.sqrt(5.0)-1.0)/2.0
    x1 = hi-gr*(hi-lo)
    x2 = lo+gr*(hi-lo)
    def f(y):
        return t*(y-c)+q*math.sqrt(max(0.0, 1.0-y*y))
    f1, f2 = f(x1), f(x2)
    for _ in range(120):
        if f1 < f2:
            lo, x1, f1 = x1, x2, f2
            x2 = lo+gr*(hi-lo); f2 = f(x2)
        else:
            hi, x2, f2 = x2, x1, f1
            x1 = hi-gr*(hi-lo); f1 = f(x1)
    return max(f1, f2, f(c), f(1.0))


def simpson(f, a, b, N=200000):
    if N % 2: N += 1
    h = (b-a)/N
    s = f(a)+f(b)
    for i in range(1,N):
        s += (4 if i%2 else 2)*f(a+i*h)
    return s*h/3.0


def Cn(n):
    return 2.0*math.gamma(n/2.0)/(math.sqrt(math.pi)*math.gamma((n-1)/2.0))


def mean_integral(n,c):
    C = Cn(n)
    def f(t):
        return 2.0*support_formula(t,c)*C*((1.0-t*t)**((n-3)/2.0) if t < 1.0 else (0.0 if n>3 else (1.0 if n==3 else 0.0)))
    # avoid the integrable endpoint singularity for n=2 by theta substitution
    def g(theta):
        t=math.sin(theta)
        # density*dt simplifies to C*cos(theta)^(n-2)
        return 2.0*support_formula(t,c)*C*(math.cos(theta)**(n-2))
    return simpson(g,0.0,math.pi/2,40000)


def finch3(c):
    phi=math.acos(c)
    return 2.0-2.0*c+(math.pi/2.0-phi)*math.sqrt(1.0-c*c)

for c in (0.05,0.2,0.5,0.8,0.95):
    for t in (0.0,c/2.0,c,min(1.0,(1+c)/2.0),0.999999):
        a=support_formula(t,c); b=support_direct(t,c)
        assert abs(a-b) < 2e-10, (c,t,a,b)

for c in (0.1,0.3,0.5,0.8):
    a=mean_integral(3,c); b=finch3(c)
    assert abs(a-b) < 2e-8, (c,a,b)

for n in (2,3,4,7,12):
    vals=[mean_integral(n,c) for c in (0.0,0.1,0.25,0.5,0.75,0.9,0.98)]
    assert abs(vals[0]-2.0) < 2e-8, (n,vals[0])
    assert all(vals[i]>vals[i+1] for i in range(len(vals)-1)), (n,vals)

print('VERIFY_OK')
