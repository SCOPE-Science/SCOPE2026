"""Numerical checks for optical single-rail Wigner-negativity extremal laws.
Run: python verify.py. Requires numpy and scipy; no external inputs.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import i0e


def width(eta, bath):
    return eta + (1-eta)*(2*bath+1)


def wigner(x, y, p, c, eta, bath):
    A=width(eta,bath)
    z=x+1j*y
    poly=1-2*eta*p/A+4*eta*p*(x*x+y*y)/(A*A)+4*math.sqrt(eta)*np.real(c*z)/A
    return 2/(math.pi*A)*np.exp(-2*(x*x+y*y)/A)*poly


def exact_fock(eta,bath):
    A=width(eta,bath)
    if A>=2*eta: return 0.
    k=2*eta/A
    return k*math.exp(-1+1/k)-1


def exact_pure(p,eta,bath):
    assert 0<p<=1
    A=width(eta,bath)
    if A>=2*eta: return 0.
    R=math.sqrt(A*(2*eta-A)/(4*eta))
    s=A*math.sqrt(1-p)/(2*math.sqrt(eta*p))
    def f(r):
        t=4*r*s/A
        return (R*R-r*r)*r*math.exp(-2*(r-s)**2/A)*i0e(t)
    return 16*eta*p/(A**3)*quad(f,0,R,epsabs=1.e-14,epsrel=1.e-12,limit=250)[0]


def grid_integral(p,c,eta,bath,M=600):
    A=width(eta,bath)
    radius=math.sqrt(max(0,A*(2*eta-A)/(4*eta))) if eta>0 else 0.
    ctr= A*abs(c)/(2*math.sqrt(eta)*p) if p>0 and eta>0 else 0.
    # Full negative-support disk lies inside [-L,L]^2 for pure states;
    # for mixed states, the disk is smaller.
    L=max(5.5*math.sqrt(A),ctr+radius+0.4)
    dx=2*L/M
    arr=(np.arange(M)+.5)*dx-L
    X,Y=np.meshgrid(arr,arr,indexing='ij')
    W=wigner(X,Y,p,c,eta,bath)
    return dx*dx*np.maximum(-W,0).sum()

# Normalize, threshold, purity, energy-bound, fixed-energy optimizer.
checks=0
for eta,bath in [(1,0),(.9,0),(.6,0),(.87,.2),(.75,.1),(.5,0),(.35,.05),(.99,.8)]:
    A=width(eta,bath)
    fock=exact_fock(eta,bath)
    if A < 2*eta:
        assert fock>0
        assert abs(fock-exact_pure(1,eta,bath))<3e-13
        checks+=2
        for p in [.12,.35,.65,.90]:
            v=exact_pure(p,eta,bath)
            assert 0<v<p*fock
            checks+=1
            if p>=.35:
                numerical=grid_integral(p,math.sqrt(p*(1-p)),eta,bath,M=950)
                assert abs(numerical-v)<2e-5,(eta,bath,p,numerical,v)
                checks+=1
        p=.65
        r=math.sqrt(p*(1-p))
        vals=[grid_integral(p,t*r,eta,bath,M=900) for t in (0,.5,1)]
        assert vals[0]<=vals[1]+1e-12 and vals[1]<vals[2]
        checks+=1
    else:
        assert fock==0
        assert grid_integral(.8,math.sqrt(.8*.2),eta,bath,M=400)==0
        checks+=2

# Generic mixed density test of the strict energy bound.
for eta,bath in [(1.,0.),(.85,.13),(.72,.2)]:
    fock=exact_fock(eta,bath)
    for p in [.1,.3,.65,.95]:
        for ratio in [0,.4,.9,1.]:
            c=ratio*math.sqrt(p*(1-p))
            num=grid_integral(p,c,eta,bath,M=900)
            assert num<=p*fock+1e-5,(eta,bath,p,ratio,num,p*fock)
            if ratio==1 and eta*2>width(eta,bath):
                assert num>0
            checks+=1
print(f'VERIFY_OK all_checks={checks} Wigner_formula_direct_grid=48 exact_pure_vs_Fock and strict_energy_and_fixed_p_bounds')
