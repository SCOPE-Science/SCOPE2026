"""Numerical cross-checks for the stationary variance critical scaling.

Uses only Python's standard library. Numerical checks are not a proof of the
asymptotic statements in RESULT.md.
"""
import math

checks = 0

def check(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)

def close(a, b, rel=1e-8, abs_tol=1e-12):
    return abs(a-b) <= max(abs_tol, rel * max(abs(a), abs(b)))

def B(p):
    return 1/6 - 1/p + 2/p**2 - 2/(p * math.expm1(p))

def Bprime(p):
    # Derivative of 1/6 -1/p+2/p^2-2/(p(expm1(p))).
    e = math.exp(-p)
    q = 1-e
    return (1/p**2 - 4/p**3 + 2*e/(p**2*q) + 2*e/(p*q**2))

def coeff(p, beta):
    return p / (p - 1 + math.exp(-p) + beta)

def density_y(y, p, beta):
    # Normalized position y=x/L centered at 0, |y|<=1/2.
    c = coeff(p, beta)
    # avoid overflow for p near 50: direct cosh and sinh remain finite
    w = p*math.cosh(p*y)/(2*math.sinh(p/2))
    return (1-c)*w + c

def V(p,beta):
    delta=1-beta
    return 1/12 + (math.exp(-p)-delta)*B(p)/(p-delta+math.exp(-p))

def W(p,delta):
    v=math.exp(-p)
    return (delta-v)*B(p)/(p-delta+v)

def simpson(f,a,b,n=2048):
    if n%2: raise ValueError('even n required')
    h=(b-a)/n
    s=f(a)+f(b)
    for i in range(1,n):
        s+=(4 if i%2 else 2)*f(a+i*h)
    return s*h/3

def peak(delta):
    h=math.log(1/delta)
    lo=max(0.001, h)
    hi=max(18.0, 2*h+20.0)
    # Independent bounded direct grid search, then golden-section local refine.
    m=2500
    idx=max(range(m+1),key=lambda j:W(lo+(hi-lo)*j/m,delta))
    a=lo+(hi-lo)*max(0,idx-2)/m
    b=lo+(hi-lo)*min(m,idx+2)/m
    gr=(math.sqrt(5)-1)/2
    c=b-gr*(b-a)
    d=a+gr*(b-a)
    for _ in range(130):
        if W(c,delta)<W(d,delta):
            a=c;c=d;d=a+gr*(b-a)
        else:
            b=d;d=c;c=b-gr*(b-a)
    return (a+b)/2

# Independent stationary density, normalized second moment, and boundary flux.
for p in [0.6,1.25,2.7,5.5,8.0,15.0]:
    for beta in [0.07,0.35,0.82,1.0,1.8,3.0]:
        f=lambda y:density_y(y,p,beta)
        norm=simpson(f,-.5,.5)
        moment=simpson(lambda y:y*y*f(y),-.5,.5)
        check(close(norm,1,rel=1e-9),('density normalization',p,beta,norm))
        check(close(moment,V(p,beta),rel=1e-8),('variance',p,beta,moment,V(p,beta)))
        check(min(f(y) for y in [-.5,-.37,0,.21,.49,.5])>=-1e-12,'density nonnegative')
        c=coeff(p,beta)
        # Set L=D=1, so v=p, alpha=p^2/beta and boundary reaction kappa=alpha*(1-exp(-p))/v.
        v=p
        alpha=p*p/beta
        kappa=alpha*(-math.expm1(-p))/v
        plus_right=((1-c)*p*math.exp(p)/(math.expm1(p)) + c)/2
        check(close(v*c/2,kappa*plus_right,rel=3e-12),'boundary reaction flux')

# Check B and B' independently by numerical integration/differentiation.
for p in [0.5,1,2,3,4,5,8,12,20,40]:
    bd=simpson(lambda y:y*y*(p*math.cosh(p*y)/(2*math.sinh(p/2))),-.5,.5)-1/12
    check(0<B(p)<1/6,'positive concentration factor')
    check(close(bd,B(p),rel=1e-8),'B integral')
    h=1e-5*max(p,1)
    check(close((B(p+h)-B(p-h))/(2*h),Bprime(p),rel=3e-6),'B prime')

# Sharp existence regimes and the first-order equation for optimized variance.
for beta in [0.04,0.2,0.5,0.9,0.99,0.999,0.999999]:
    delta=1-beta
    p=peak(delta)
    check(p>math.log(1/delta),'minimum occurs beyond shape transition')
    check(W(p,delta)>0,'nonzero confinement gain')
    u=math.exp(-p)
    residual=u/(delta-u)+Bprime(p)/B(p)-(1-u)/(p-delta+u)
    check(abs(residual)<2e-7,'critical equation residual')
    for k in range(1,60):
        ptest=math.log(1/delta)+k/8
        check(W(p,delta)>=W(ptest,delta)-2e-12,'grid global check')
for beta in [1.0,1.25,2.5]:
    for p in [0.5,1,2,4,7,10,15,25,40]:
        check((math.exp(-p)+(beta-1))*B(p)/(p-1+math.exp(-p)+beta)>0,'supercritical no sub-uniform variance')

# Multiplicative and logarithmic asymptotics in near-critical cases.
for delta in [1e-7,1e-9,1e-12,1e-15,1e-20,1e-25]:
    h=math.log(1/delta)
    p=peak(delta)
    approx=h+math.log(h)+(math.log(h)+7)/h
    check(abs(p-approx)<8*(math.log(h)**2+1)/h**2,'loglog plus constant 7 expansion')
    deep=W(p,delta)
    approx_deep=delta/(6*h)*(1-(math.log(h)+7)/h)
    check(abs(deep-delta/(6*h))<8*delta*(math.log(h)+8)/(6*h*h),'leading optimized gain')
    check(deep>approx_deep,'positive second-order remainder in tested cases')

print('PASS', checks, 'independent scalar checks')
print('critical examples:')
for delta in [1e-4,1e-9,1e-15,1e-25]:
    p=peak(delta); h=math.log(1/delta)
    print('delta={:.0e} p*={:.10f}, H+logH+correction={:.10f}, gain={:.10e}'.format(delta,p,h+math.log(h)+(math.log(h)+7)/h,W(p,delta)))
