#!/usr/bin/env python3
"""Independent numerical/symbolic consistency tests of renewal-reset OU cumulants.
Run: python3 verify.py. Requires mpmath and sympy.
This is not a proof of the all-parameter inequalities in RESULT.md.
"""
import mpmath as mp
import sympy as sp
mp.mp.dps = 45
checks=0

def close(a,b,tol=mp.mpf('1e-28')):
    global checks
    assert abs(a-b)<tol*(1+abs(a)+abs(b)),(a,b)
    checks+=1

def require(p):
    global checks
    assert bool(p)
    checks+=1

def moments_from_age(tau, scheme):
    tau=mp.mpf(tau)
    if scheme=='periodic':
        return ((-mp.expm1(-2*tau))/(2*tau),
                (-mp.expm1(-4*tau))/(4*tau))
    return (1/(1+2*tau),1/(1+4*tau))

def independent_integrals(tau,scheme):
    if scheme=='periodic':
        weight=lambda t: 1/tau
        upper=tau
    else:
        weight=lambda t: mp.exp(-t/tau)/tau
        upper=mp.inf
    mean=lambda n:mp.quad(lambda t:weight(t)*mp.exp(-2*n*t),[0,upper])
    return mean(1),mean(2)

x=sp.symbols('x',positive=True)
identity=sp.factor((1+2*x)**4-(1+x*x)*(1+4*x)**2)
require(sp.simplify(identity-x*x*(24*x+7))==0)
# Test the inequality using both analytic elementary lower bound and direct values.
for st in ('0.005','0.02','0.05','0.5','1','2','3','8','20','100'):
    t=mp.mpf(st)
    require(mp.tanh(t)>t/mp.sqrt(1+t*t))
    require(1/mp.sqrt(1+t*t)>(1+4*t)/(1+2*t)**2)
    Fp=4*t*t/(1+2*t)**2
    Fd=1-mp.tanh(t)/t
    require(Fp>Fd)

cases=[([(-1,mp.mpf(1)/2),(1,mp.mpf(1)/2)]),
       ([(-2,mp.mpf(1)/2),(1,mp.mpf(1)/3),(4,mp.mpf(1)/6)]),
       ([(-1,mp.mpf(1)/6),(0,mp.mpf(2)/3),(1,mp.mpf(1)/6)]),
       ([(-2,mp.mpf(1)/2),(2,mp.mpf(1)/2)])]
for R in cases:
    r1=sum(p*s for s,p in R)
    close(r1,0)
    v=sum(p*s*s for s,p in R)
    M4=sum(p*s**4 for s,p in R)
    kap=M4-3*v*v
    for q in ('0','0.12','1.5','9'):
        q=mp.mpf(q)
        for tau in ('0.2','1','3.5'):
            tau=mp.mpf(tau)
            for scheme in ('periodic','poisson'):
                z1,z2=moments_from_age(tau,scheme)
                t1,t2=independent_integrals(tau,scheme)
                close(z1,t1)
                close(z2,t2)
                # Moments computed independently by quadrature before cumulant subtraction.
                if scheme=='periodic':
                    weight=lambda t:1/tau
                    upper=tau
                else:
                    weight=lambda t:mp.exp(-t/tau)/tau
                    upper=mp.inf
                def E2(t):
                    z=mp.exp(-2*t)
                    return v*z+q*(1-z)
                def E4(t):
                    z=mp.exp(-2*t)
                    return M4*z*z+6*v*q*z*(1-z)+3*q*q*(1-z)**2
                second=mp.quad(lambda t:weight(t)*E2(t),[0,upper])
                fourth=mp.quad(lambda t:weight(t)*E4(t),[0,upper])
                inferred=fourth-3*second**2
                structural=kap*z2+3*(v-q)**2*(z2-z1*z1)
                close(inferred,structural)
                F=1-z1*z1/z2
                exact=1-mp.tanh(tau)/tau if scheme=='periodic' else 4*tau*tau/(1+2*tau)**2
                close(F,exact)

eta=mp.mpf(2)/3
root_P=mp.sqrt(eta)/(2*(1-mp.sqrt(eta)))
root_D=mp.findroot(lambda t:mp.tanh(t)/t-1+eta,(2,4))
close(root_P,mp.mpf('2.22474487139158904909864203735'))
close(root_D,mp.mpf('2.98470458535788681555979123462'))
require(root_D>root_P)
for tau in [root_P/2,(root_P+root_D)/2,root_D*mp.mpf('1.2')]:
    def delta(z,scheme):
        z1,z2=moments_from_age(z,scheme)
        return -2*z2+3*(z2-z1*z1)
    require((delta(tau,'poisson')>0)==(tau>root_P))
    require((delta(tau,'periodic')>0)==(tau>root_D))
print(f'PASS: {checks} independent arithmetic, quadrature, root and order assertions')
