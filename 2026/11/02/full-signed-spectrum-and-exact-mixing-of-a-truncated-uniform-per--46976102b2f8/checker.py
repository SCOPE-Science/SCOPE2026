#!/usr/bin/env python3
"""Deterministic verification of explicit eigenpairs for a symmetric killed Markov kernel.

Model: uniform innovations on [-a,1], 0<a<1, with allowed pairs x+y>0.
Computations test finite algebraic identities; the accompanying analytic proof handles
all real a and the infinite-dimensional spectral assertion.
"""
import math

COUNTS = 0

def near(actual, expected, tol=2e-9, label=''):
    global COUNTS
    assert math.isfinite(actual) and math.isfinite(expected), (label,actual,expected)
    assert abs(actual-expected) <= tol*(1+abs(expected)), (label,actual,expected)
    COUNTS += 1


def root(a, k):
    assert 0 < a < 1
    r = (1-a)/a
    lo=k*math.pi-math.pi/4+1e-10
    hi=(k+1)*math.pi-math.pi/4-1e-10
    def eq(t):
        return math.cos(t+math.pi/4)/math.sin(t+math.pi/4)-r*t
    assert eq(lo)>0 and eq(hi)<0,(a,k,eq(lo),eq(hi))
    for _ in range(100):
        md=(lo+hi)/2
        if eq(md)>0: lo=md
        else: hi=md
    t=(lo+hi)/2
    near(math.cos(t+math.pi/4)-r*t*math.sin(t+math.pi/4),0,3e-10,'root')
    return t


def phi(a,t,x):
    b=t/a
    return math.cos(b*min(x,a))+math.sin(b*min(x,a))


def kernel_phi(a,t,x):
    beta=t/a
    lo=max(-a,-x)
    primitive=lambda y:(math.sin(beta*y)-math.cos(beta*y))/beta
    return (primitive(a)-primitive(lo)+(1-a)*phi(a,t,a))/(1+a)


def norm2(a,t):
    return 2*a+(1-a)*phi(a,t,a)**2


def pair_integral(a,t1,t2):
    b1,b2=t1/a,t2/a
    delta=b1-b2
    tr=2*a if abs(delta)<1e-10 else 2*math.sin(delta*a)/delta
    return tr+(1-a)*phi(a,t1,a)*phi(a,t2,a)


def run():
    for a in (.005,.01,.025,.05,.1,.2,.35,.5,.75,.9,.99,.999):
        ts={k:root(a,k) for k in range(-4,5)}
        assert 0 < ts[0] < math.pi/4
        assert -3*math.pi/4 < ts[-1] < -math.pi/4
        assert ts[1] >3*math.pi/4
        assert ts[-2]<-5*math.pi/4
        assert ts[0] < abs(ts[-1]) < ts[1]
        for j,t in ts.items():
            lam=a/((1+a)*t)
            near(phi(a,t,a),phi(a,t,1),label='plateau')
            for i in range(101):
                x=-a+(1+a)*i/100
                near(kernel_phi(a,t,x),lam*phi(a,t,x),1.5e-9,'eigen')
            # Analytic norm identities from parity cancellation.
            near(pair_integral(a,t,t),norm2(a,t),3e-10,'norm')
        for k in range(-4,5):
            for l in range(k+1,5):
                near(pair_integral(a,ts[k],ts[l]),0,3e-9,'orthogonal')
        t0,tm=ts[0],ts[-1]
        rho=t0/(-tm)
        assert 0<rho<1 and rho>ts[0]/ts[1]  # negative mode is the next largest in modulus
        # Stationary density integrates to one using parity.
        h=phi(a,t0,a)
        c=norm2(a,t0)
        near((2*a+(1-a)*h*h)/c,1,1e-12,'stationary normalization')
        # Symmetric detailed balance of the h-transform.
        lam0=a/((1+a)*t0)
        for i in range(16):
            x=-a+(1+a)*(i+.5)/16
            for j in range(16):
                y=-a+(1+a)*(j+.5)/16
                if x+y<=0:continue
                pi_x=phi(a,t0,x)**2/c
                pi_y=phi(a,t0,y)**2/c
                pxy=phi(a,t0,y)/(lam0*(1+a)*phi(a,t0,x))
                pyx=phi(a,t0,x)/(lam0*(1+a)*phi(a,t0,y))
                near(pi_x*pxy,pi_y*pyx,2e-11,'detailed balance')
        print('a=',a,'lambda0=',format(lam0,'.12f'),'rho=',format(rho,'.12f'),'rho/a=',format(rho/a,'.9f'))
    for a in (.00005,.0001,.0002,.0005,.001,.002):
        ratio=root(a,0)/(-root(a,-1))/a
        near(ratio,4/math.pi,.015,'small a ratio')
    # At a=1 the exact eigenvalue ratio is 1/3, but this boundary is not new.
    near((math.pi/4)/(3*math.pi/4),1/3,1e-13,'boundary')
    print('PASS',COUNTS,'finite deterministic assertions; analytic results separately proved')

if __name__=='__main__':
    run()
