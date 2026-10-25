"""Deterministic reproducibility checks for the weak-restart quantum-walk profile."""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import k0

def profile(ell, x):
    u = math.sqrt(ell/(ell+2))
    return (1+x*x*math.sqrt((1-u*u)/(1+u*u*x*x)))/(1+x*x)

def density(ell, y):
    u = math.sqrt(ell/(ell+2))
    c = math.sqrt(1-u*u)/math.pi
    return quad(lambda t: c*math.exp(-abs(y)/(u*math.sin(t))) /
                ((1-u*u*math.sin(t)**2)*u*math.sin(t)),
                0, math.pi/2, epsabs=1e-11)[0]

def walk_cf(ell, q, maxage, xi):
    r=math.sqrt(ell)
    C=np.array([[-ell,2*r,2],[2*r,ell-2,2*r],[2,2*r,-ell]])/(ell+2)
    chi=np.array([r,-2,r])/math.sqrt(2*(ell+2))
    L=2*maxage+3
    state=np.zeros((L,3),dtype=complex)
    state[maxage+1]=chi
    xs=np.arange(L)-maxage-1
    total=0.
    wt=q
    for age in range(maxage+1):
        p=np.sum(np.abs(state)**2,axis=1)
        total+=wt*np.dot(p,np.cos(q*xi*xs))
        if age==maxage: break
        moved=state@C.T
        state=np.zeros_like(state)
        state[:-1,0]=moved[1:,0]
        state[:,1]=moved[:,1]
        state[1:,2]=moved[:-1,2]
        wt*=1-q
    return total,(1-q)**(maxage+1)

def main():
    checks=0
    for ell in [0.15,1.,2.,8.,60.]:
        u=math.sqrt(ell/(ell+2));c=math.sqrt(1-u*u)/math.pi
        norm=2*quad(lambda t:c/(1-u*u*math.sin(t)**2),0,math.pi/2)[0]
        assert abs(norm-1)<2e-12
        checks+=1
        for x in [0,.25,1,2,7]:
            integral=2*quad(lambda t:c/((1-u*u*math.sin(t)**2)*(1+x*x*u*u*math.sin(t)**2)),0,math.pi/2)[0]
            assert abs(integral-profile(ell,x))<3e-12
            checks+=1
    ell=2.;u=math.sqrt(ell/(ell+2));cusp=math.sqrt(2/ell)/math.pi
    tail=math.sqrt((ell+2)/(4*math.pi*u))
    assert abs(density(ell,1e-7)/(cusp*math.log(1e7))-1)<.05
    checks+=1
    assert abs(density(ell,20)/(tail*math.exp(-20/u)/math.sqrt(20))-1)<.06
    checks+=1
    for ell in [1e-4,1e-5]:
        u=math.sqrt(ell/(ell+2))
        assert abs(profile(ell,2/u)-1/math.sqrt(5))<.01
        checks+=1
    for ell in [1e4,1e5]:
        assert abs(profile(ell,2)-1/5)<.01
        checks+=1
    for q,T,tol in [(0.05,350,.018),(.02,880,.008)]:
        got,rem=walk_cf(2,q,T,1.)
        assert rem<1e-6
        assert abs(got-profile(2,1))<tol
        checks+=2
    assert abs(k0(1)/math.pi - quad(lambda v:math.exp(-1/v)/(math.pi*v*math.sqrt(1-v*v)),0,1)[0])<1e-9
    checks+=1
    print(f"PASS: {checks} deterministic numerical checks; finite-q estimates are approximations, not proof")

if __name__=='__main__':
    main()
