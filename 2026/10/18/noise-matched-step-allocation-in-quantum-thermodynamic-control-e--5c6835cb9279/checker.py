"""Numerical cross-checks for noise-matched thermodynamic step protocols.

Run: python3 checker.py
No external packages are required. The analytic statements are proved in RESULT.md;
finite tests here are not substitutes for those proofs.
"""
import math
import random

checks=0

def check(test, message):
    global checks
    if not test:
        raise AssertionError(message)
    checks += 1

def simpson(f,a,b,n=12000):
    assert n % 2 == 0
    h=(b-a)/n
    total=f(a)+f(b)
    for j in range(1,n):
        total+=(4 if j%2 else 2)*f(a+j*h)
    return total*h/3

def g(x,beta):
    return beta/4 / math.cosh(beta*x/2)**2

def G_formula(a,b,beta):
    return (math.tanh(beta*b/2)-math.tanh(beta*a/2))/2

# The Gibbs metric is tested against two independent representations:
# an integrated closed form and the curvature of the exact Gibbs KL cost.
for beta in (0.4, 1.0, 2.5, 5.0):
    for a,b in ((-1.0,1.5), (-2.0,2.0), (-0.7, 0.8)):
        check(abs(simpson(lambda x:g(x,beta),a,b)-G_formula(a,b,beta))<1e-10,
              'Gibbs metric integral')

def binary_kl_per_beta(x,y,beta):
    p=1/(1+math.exp(beta*x))
    q=1/(1+math.exp(beta*y))
    return (p*math.log(p/q)+(1-p)*math.log((1-p)/(1-q)))/beta
for beta in (0.7,1.5,3.0):
    for x in (-0.5,0.0,0.6):
        h=1e-3
        # Centered second difference cancels cubic terms.
        c=(binary_kl_per_beta(x,x+h,beta)+binary_kl_per_beta(x,x-h,beta))/(2*h*h)
        check(abs(c-g(x,beta)/2)<8e-7,'metric equals local KL curvature')

# The continuous cost has an exact linear-ramp optimizer when increment
# noise variance is spatially constant, irrespective of the Gibbs metric.
for beta in (0.5,1.0,3.0):
    a,b=-1.5,1.5
    s=0.09
    target=s*G_formula(a,b,beta)
    N=(b-a)/s
    for p in (1.0,1.5,2.0,3.0):
        def integrand(t):
            x=a+(b-a)*t**p
            v=(b-a)*p*t**(p-1)
            return 0.5*g(x,beta)*(v*v/N+N*s*s)
        value=simpson(integrand,0,1)
        check(value>=target-1e-9,'continuous lower bound')
        if p==1.0:
            check(abs(value-target)<1e-9,'linear ramp exact equality')
        else:
            check(value>target+1e-6,'nonlinear ramp strict gap')

# For nonconstant local noise, the exact matched velocity is v'=N sqrt(phi(v)).
for beta in (0.8,2.0):
    a,b=-1.2,1.6
    s=0.04
    aa,bb=math.asinh(a),math.asinh(b)
    N=(bb-aa)/s
    def x_of_t(t):return math.sinh(aa+(bb-aa)*t)
    def matched(t):
        x=x_of_t(t)
        v=(bb-aa)*math.cosh(aa+(bb-aa)*t)
        phi=s*s*(1+x*x)
        return .5*g(x,beta)*(v*v/N+N*phi)
    target=simpson(lambda x:g(x,beta)*s*math.sqrt(1+x*x),a,b)
    check(abs(simpson(matched,0,1)-target)<1e-8,'variable-noise matching')
    check(abs(N-simpson(lambda x:1/(s*math.sqrt(1+x*x)),a,b))<1e-8,
          'variable-noise duration')

# A thermodynamic-arc-length schedule is strictly more expensive, even
# after separately optimizing the total duration, if the metric varies.
for beta in (0.5,1.0,2.0,5.0,9.0):
    a,b=-2.0,2.0
    GG=simpson(lambda x:g(x,beta),a,b)
    L=simpson(lambda x:math.sqrt(g(x,beta)),a,b)
    J=simpson(lambda x:g(x,beta)**1.5,a,b)
    ratio=math.sqrt(L*J)/GG
    check(ratio>1.0+1e-8,'strict geodesic scheduling loss')
    check(ratio<math.pi/(2*math.sqrt(2))+1e-8,'expected limiting ratio')
check(abs(math.pi/(2*math.sqrt(2))-1.1107207345395915)<1e-14,
      'wide-control quantum advantage')

# Exact pointwise discrete identity; a Riemann-sum estimate underpins
# the rigorous small-noise integer-step theorem.
random.seed(1729)
for beta in (0.5,1.0,2.0):
    a,b=-1.,1.
    lip=beta*beta/4
    for N in (4,9,20,40):
        for _ in range(6):
            raw=[random.random()+0.01 for i in range(N)]
            raw=[(b-a)*q/sum(raw) for q in raw]
            points=[a]
            for di in raw:points.append(points[-1]+di)
            points[-1]=b
            dd=[points[i+1]-points[i] for i in range(N)]
            s=0.07
            E=.5*sum(g(points[i],beta)*(dd[i]**2+s*s) for i in range(N))
            identity=s*sum(g(points[i],beta)*dd[i] for i in range(N)) + .5*sum(
                g(points[i],beta)*(dd[i]-s)**2 for i in range(N))
            check(abs(E-identity)<1e-12,'discrete equipartition identity')
            check(E>=s*G_formula(a,b,beta)-s*lip*sum(z*z for z in dd)/2-1e-12,
                  'discrete Gibbs-Riemann bound')

# Test the constructive near-optimal sequence with the exact count
# N=ceil((b-a)/s): cost - leading term is at most proportional to s^2.
for beta in (0.5,1.0,2.0):
    a,b=-1.5,1.5
    for s in (0.2,0.1,0.05,0.025):
        N=math.ceil((b-a)/s)
        dd=(b-a)/N
        EE=.5*(dd*dd+s*s)*sum(g(a+i*dd,beta) for i in range(N))
        target=s*G_formula(a,b,beta)
        check(abs(EE-target)/s**2<3.0,'constructive finite-step error')
        check(abs(N*s-(b-a))<=s+1e-13,'integer count error')

# Constant-metric case permits independent exhaustive integer minimization.
for s in (0.5,0.2,0.08,0.031):
    length=2.7
    def cost(N):return .5*(length*length/N+N*s*s)
    Nstar=min(range(1,500),key=cost)
    check(abs(Nstar*s-length)<s+1e-12,'discrete integer optimum near continuum')
    check(cost(Nstar)>=s*length-1e-12,'discrete sharp lower bound')

print(f'PASS: {checks} numerical assertions; all checks are finite tests, not an infinite proof.')
