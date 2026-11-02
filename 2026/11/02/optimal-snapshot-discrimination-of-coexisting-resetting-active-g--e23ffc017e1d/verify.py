#!/usr/bin/env python3
"""Independent numerical probes for a two-branch active-matter phase-discrimination theorem.

Run: python verify.py
Requires: numpy, scipy. Numerical tests are bounded checks, not proof.
"""
import math
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import lambertw


def flux(z,Q): return z-z*z/Q
def F(z,Q): return math.log(z)-2*z/Q

def param(Q,m):
    if not 4<Q or not 1<m<Q/4: raise ValueError("coexistence only")
    a=Q/2*(1-math.sqrt(1-4*m/Q))
    b=math.log(m)/Q
    q=Q/2*(1-math.sqrt(1-4/Q))
    z=brentq(lambda z: F(z,Q)-F(a,Q)+b,1e-12,a,xtol=1e-13)
    return a,b,q,z

def gas(y,Q,z0):
    w=lambertw(-(2*z0/Q)*math.exp(-2*z0/Q-y),k=0)
    assert abs(w.imag)<1e-11
    return -Q/2*w.real

def tv_formula(Q,m):
    a,b,q,z=param(Q,m)
    return (flux(z,Q)-1)/m

def gsign(Q,m):
    a,b,q,z=param(Q,m)
    return 1-z*(a+1-z)/Q

def density(y,Q,m,kind):
    a,b,q,z=param(Q,m)
    if kind=='pure': return gas(y,Q,a)/m
    if y<=b: return Q*math.exp(-Q*y)
    return gas(y-b,Q,q)/m

def tv_quad(Q,m):
    _,b,_,_=param(Q,m)
    f=lambda y: abs(density(y,Q,m,'drop')-density(y,Q,m,'pure'))/2
    A=quad(f,0,b,epsabs=1e-12,epsrel=5e-10)[0]
    B=quad(f,b,max(40,b+40),epsabs=1e-12,epsrel=5e-10)[0]
    return A+B

def endpoint(Q):
    s=Q/4
    fs=F(Q/2,Q)-math.log(s)/Q
    z=brentq(lambda z:F(z,Q)-fs,1e-12,Q/2-1e-10)
    Ts=(flux(z,Q)-1)/s
    As=Ts+z/s*(1/Q-0.5)
    Gs=1-z*(Q/2+1-z)/Q
    return z,Ts,As,Gs


def main():
    count=0
    for Q in [4.2,5,8,10,12,20,50,100]:
        s=Q/4
        for j in range(1,18):
            m=1+(s-1)*j/18
            a,b,q,z=param(Q,m)
            assert q<z<a<Q/2 and 0<b
            assert 0<tv_formula(Q,m)<1-1/m
            assert abs(tv_quad(Q,m)-tv_formula(Q,m))<2e-9, (Q,m)
            for y in [0.0,b*0.3,b*0.9]:
                assert density(y,Q,m,'drop')>density(y,Q,m,'pure')
                count+=1
            for y in [b+0.1,b+1,b+4]:
                assert density(y,Q,m,'drop')<density(y,Q,m,'pure')
                count+=1
            h=1e-5*(s-1)
            dm=min(h,0.24*(m-1),0.24*(s-m))
            derivative=(tv_formula(Q,m+dm)-tv_formula(Q,m-dm))/(2*dm)
            assert abs(derivative-gsign(Q,m)/m**2)<2e-5, (Q,m,derivative)
            count+=4
        z,Ts,As,Gs=endpoint(Q)
        vals=[gsign(Q,1+(s-1)*j/100) for j in range(1,100)]
        assert all(vals[i]>vals[i+1] for i in range(len(vals)-1))
        count+=99
        if Gs<0:
            root=brentq(lambda m:gsign(Q,m),1+1e-9,s-1e-9)
            assert 1<root<s
            assert tv_formula(Q,root)>tv_formula(Q,s-1e-7)
            count+=2
    for Q in [5.0,12.0,20.0,100.0]:
        z,Ts,As,Gs=endpoint(Q)
        s=Q/4
        coeff=-z/(3*s)
        residuals=[]
        for eps in [.12,.09,.06,.04,.03]:
            m=s*(1-eps**2)
            if m<=1:continue
            empirical=(tv_formula(Q,m)-Ts-As*eps**2)/eps**3
            residuals.append(abs(empirical-coeff))
            count+=1
        assert residuals[-1]<residuals[0]
    print(f"PASS: {count} bounded checks across coexisting profiles, TV quadratures, derivative, monotonicity, and spinodal asymptotics")
    for Q in [5,10,12,20,100]:
        z,Ts,As,Gs=endpoint(Q)
        print(f"Q={Q}, upper spinodal TV={Ts:.9f}, G_endpoint={Gs:+.9f}, cusp coefficient={-z/(3*(Q/4)):+.9f}")
        if Gs<0:
            root=brentq(lambda m:gsign(Q,m),1+1e-9,Q/4-1e-9)
            print(f"  unique interior maximum: m={root:.9f}, TV={tv_formula(Q,root):.9f}")

if __name__=='__main__': main()
