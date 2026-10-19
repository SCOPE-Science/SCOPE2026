"""Reproduce exact orbit identities and local stability for a smoothed quadratic Nesterov iteration.

Run: python3 artifacts/verify_scalar_soft_muesterov.py
Standard library only; numerical checks supplement the analytic proof.
"""
import math


def F(y,a):
    return y*(1-a/math.hypot(1.,y))

def deriv(y,a):
    return 1-a/(1+y*y)**1.5

def threshold(beta):
    return 2*(1+beta)/(1+2*beta)

def amp(a,beta):
    v=(a/(2*(1+beta)))**2-1/(1+2*beta)**2
    return math.sqrt(max(v,0))

def step(x,xprev,a,beta):
    return F((1+beta)*x-beta*xprev,a)

def schur(tr,det):
    return 1-tr+det>0 and 1+tr+det>0 and 1-det>0

count=0
for beta in [0,.01,.1,.3,.5,.7,.9,.99]:
    ac=threshold(beta)
    for ratio in [.02,.1,.5,.9,.999,1.001,1.01,1.1,2.,10.,100.]:
        a=ac*ratio
        p=1-a
        stable_zero=schur(p*(1+beta),p*beta)
        assert stable_zero == (a<ac)
        count+=1
        if a>ac:
            h=amp(a,beta)
            assert math.isclose(step(h,-h,a,beta),-h,abs_tol=2e-10*max(1,h))
            assert math.isclose(step(-h,h,a,beta),h,abs_tol=2e-10*max(1,h))
            q=deriv((1+2*beta)*h,a)
            assert math.isclose(q,1-ac**3/a**2,rel_tol=5e-12,abs_tol=1e-12)
            assert schur(q*(1+beta),q*beta)
            # Every nearby perturbed state approaches the displayed cycle.
            for sign in [-1,1]:
                x0=sign*h*(1+1e-3)
                xp=-sign*h*(1-1e-3)
                x,xprev=x0,xp
                for _ in range(2000 if ratio <= 10 else 100):
                    nxt=step(x,xprev,a,beta)
                    xprev,x=x,nxt
                if ratio <= 10:
                    assert math.isclose(abs(x),h,rel_tol=5e-5,abs_tol=2e-6), (a,beta,x,h)
                else:
                    assert abs(abs(x)-h) < 0.01*h, (a,beta,x,h)
            count+=1

# Strict distance to the global attractor in the no-momentum scalar subcase.
for a in [2.00001,2.01,2.1,2.5,3.,4.,8.,15.,30.]:
    h=math.sqrt((a/2)**2-1)
    top=math.sqrt(a*a-1)
    for j in range(1,1000):
        t=top*j/1000
        g=a*t/math.hypot(t,1)-t
        assert 0<g<top
        if abs(t-h)>1e-12:
            assert abs(g-h) < abs(t-h)+1e-12,(a,t,g,h)
        count+=1

# Globally attracting critical boundary with inverse-square decay.
for z0 in [.01,.25,1.,10.,100.]:
    z=z0
    for i in range(1,250001):
        z=F(z,2.)
    assert abs(math.sqrt(i)*abs(z)-1/math.sqrt(2))<1e-2,(z0,z)
    count+=1

# Finite-difference directional derivative on exact period two.
for beta in [.03,.25,.75,.96]:
    a=threshold(beta)*1.37
    h=amp(a,beta)
    q=deriv((1+2*beta)*h,a)
    eps=1e-6
    base=step(h,-h,a,beta)
    d_x=(step(h+eps,-h,a,beta)-base)/eps
    d_xprev=(step(h,-h+eps,a,beta)-base)/eps
    assert math.isclose(d_x,q*(1+beta),abs_tol=2e-5)
    assert math.isclose(d_xprev,-q*beta,abs_tol=2e-5)
    count+=2
print('PASS:',count,'deterministic identities, stability checks, interval contractions and critical limits')
