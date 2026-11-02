#!/usr/bin/env python3
"""Independent finite-path and numerical checks for the two-step A-correlation theorem.

Requires Python standard library only. Finite-path computations are exact rational
and do not substitute for the infinite-line proof.
"""
from fractions import Fraction
from functools import lru_cache
from math import cosh, sinh, sqrt, exp, factorial

COUNT = 0

def check(condition, message):
    global COUNT
    if not condition:
        raise AssertionError(message)
    COUNT += 1

def hs(a, t):
    b = 1-a
    g = sqrt(a*b)
    return cosh(g*t)-b/g*sinh(g*t), cosh(g*t)-a/g*sinh(g*t)

def int_h(a, t):
    b=1-a;g=sqrt(a*b)
    return sinh(g*t)/g - b/(g*g)*(cosh(g*t)-1)

def int_hsq(a, t):
    b=1-a;g=sqrt(a*b);c=b/g
    return (1-c*c)*t/2 + (1+c*c)*sinh(2*g*t)/(4*g) - c*sinh(g*t)**2/g

def simpson(func, lo, hi, n=600):
    step=(hi-lo)/n
    return step/3*(func(lo)+func(hi)+4*sum(func(lo+(2*i-1)*step) for i in range(1,n//2+1)) + 2*sum(func(lo+2*i*step) for i in range(1,n//2)))

def theory(a,t):
    b=1-a
    H=int_h(a,t)
    # M is the integral of h(u) h(v) min(u,v), and equals
    # integral_0^t (H(t)-H(s))^2 ds.
    M=simpson(lambda s:(H-int_h(a,s))**2,0,t)
    p=a*a*(H*H-b*M)
    rho=a*int_hsq(a,t)
    return p,rho,M

def finite_path(n,a,t):
    """Exact rational path law, independently enumerating random attempts and marks."""
    b=1-a
    left,right=n//2-1,n//2+1
    @lru_cache(None)
    def rec(state,pending):
        if pending==0:
            return {(state[left],state[right]):Fraction(1)}
        k=pending.bit_count()
        out={}
        for i in range(n):
            if not pending>>i & 1:
                continue
            for label,wt in ((1,a),(2,b)):
                blocked=(i>0 and state[i-1] in (1,2) and state[i-1]!=label) or (i<n-1 and state[i+1] in (1,2) and state[i+1]!=label)
                new=state[:i]+(3 if blocked else label,)+state[i+1:]
                for key,mass in rec(new,pending^(1<<i)).items():
                    out[key]=out.get(key,Fraction(0))+wt*mass/k
        return out
    joint={}
    for mask in range(1<<n):
        k=mask.bit_count(); weight=t**k*(1-t)**(n-k)
        if weight==0:continue
        for key,mass in rec((0,)*n,mask).items():
            joint[key]=joint.get(key,Fraction(0))+weight*mass
    check(sum(joint.values())==1,'finite path joint law normalization')
    check(all(v>=0 for v in joint.values()),'finite path negative weight')
    paa=joint.get((1,1),Fraction(0))
    pa=sum(v for (x,y),v in joint.items() if x==1)
    return float(paa),float(pa)

# Exact-source-density identity and positive sign on a broad parameter-time grid.
for ai in range(1,50):
    a=ai/50
    for j in range(1,31):
        t=j/30
        b=1-a;g=sqrt(a*b);theta=sqrt(a/b)
        hA,hB=hs(a,t)
        check(0<hA<1 and 0<hB<1,'one-sided shielding range')
        check(hA*hA+b*t<1+1e-11,'critical pointwise inequality')
        p,rho,M=theory(a,t)
        check(p>rho*rho,'distance-two covariance must be positive')
        check(0<p<rho,'pair probability bounds')
        check(M>=0 and M<=t*int_h(a,t)**2+1e-10,'minimum-time integral bounds')
        # Published one-point expression: independent evaluation of rho.
        pub=(2*theta+(theta*theta-1)*2*g*t+(theta*theta+1)*sinh(2*g*t)-2*theta*cosh(2*g*t))/(4*theta)
        check(abs(rho-pub)<4e-11,'2023 density identity')

for t in [0.05,0.2,0.5,0.9,1.0]:
    paa,rho,_=theory(0.5,t)
    exact_p=(1-(1+t)*exp(-t))/2
    exact_rho=(1-exp(-t))/2
    check(abs(paa-exact_p)<3e-10,'closed balanced pair law')
    check(abs(rho-exact_rho)<3e-12,'closed balanced one-point law')
    check(paa-rho**2>0,'balanced covariance')

# Exact-rational independent finite-path recursion (two random configurations).
for n,tol in ((5,.035),(7,.006),(9,.0006)):
    for a,t in ((Fraction(1,2),Fraction(1)),(Fraction(3,10),Fraction(1,2))):
        paa,pa=finite_path(n,a,t)
        p,rho,_=theory(float(a),float(t))
        check(abs(paa-p)<tol,'finite path second-neighbor joint mismatch')
        check(abs(pa-rho)<tol,'finite path marginal mismatch')

print('PASS',COUNT,'independent rational/numerical assertions')
