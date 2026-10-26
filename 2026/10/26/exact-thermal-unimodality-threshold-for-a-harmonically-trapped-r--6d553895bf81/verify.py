"""Numerical tests of a harmonic run-and-tumble thermal-modality theorem.

Only requires numpy and scipy. Checks analytic curvature/Kummer identities,
Gauss-Jacobi quadrature, modal geometry, and endpoint approaches.
"""
import math
import numpy as np
from scipy.special import hyp1f1, roots_jacobi
from scipy.optimize import brentq


def I_normalized(a,z):
    return hyp1f1(0.5,a+0.5,-z)

def F_normalized(a,z):
    return I_normalized(a,z)-z/(a+0.5)*hyp1f1(1.5,a+1.5,-z)

def root(a):
    assert 0<a<1
    lo,hi=0.0,1.0
    while F_normalized(a,hi)>0:
        hi *=2
        assert hi<1e8
    return brentq(lambda z:F_normalized(a,z),lo,hi,xtol=1e-13)

def density_derivatives(a,tau,x,n=160):
    u,w=roots_jacobi(n,a-1,a-1)
    w=w/sum(w)
    d=x-u
    phi=np.exp(-d*d/(2*tau))/np.sqrt(2*np.pi*tau)
    return (np.dot(w,phi),np.dot(w,-d/tau*phi),np.dot(w,(d*d/tau**2-1/tau)*phi))

def count_positive_modes(a,tau):
    # True mode count is proved analytically; finite sampling is a check only.
    xx=np.linspace(0.0005,1.6,1200)
    der=np.array([density_derivatives(a,tau,x,160)[1] for x in xx])
    # Ignore tiny rounding jitters by requiring macroscopic bracket.
    crossings=np.where((der[:-1]>1e-9)&(der[1:]<-1e-9))[0]
    return len(crossings),min(der),max(der)

def main():
    checks=0
    for a in [0.025,0.1,0.25,0.5,0.75,0.9,0.975]:
        z=root(a);tc=1/(2*z)
        assert abs(F_normalized(a,z))<1e-10
        # at a zero, the derivative of the Kummer curvature is exact
        h=1e-5*max(1,z)
        deriv=(F_normalized(a,z+h)-F_normalized(a,z-h))/(2*h)
        exact=(a-1)*I_normalized(a,z)/z
        assert abs(deriv-exact)<1e-7
        for fac,expect in [(0.55,1),(1.50,-1)]:
            tau=tc*fac
            gd2=density_derivatives(a,tau,0)[2]
            assert expect*gd2>1e-7,(a,tau,gd2)
            curv=-F_normalized(a,1/(2*tau))/(tau*math.sqrt(2*math.pi*tau))
            assert abs(gd2-curv) <5e-9,(a,tau,gd2,curv)
            checks+=3
        if a in [0.1,0.25,0.5,0.75,0.9]:
            # Independent finite mesh sign tests of the analytical mode conclusion.
            low=count_positive_modes(a,0.7*tc)
            high=count_positive_modes(a,1.3*tc)
            assert low[0]==1,(a,'below',low)
            assert high[0]==0,(a,'above',high)
            checks+=2
        print(f'a={a:.3f} critical_tau={tc:.12f} z={z:.12f}')
    assert abs(1/(2*root(1e-4))-1)<1e-3
    assert 1/(2*root(0.999))<0.06
    checks +=2
    print('PASS',checks,'checks (analytic identities, quadrature, mode sampling, endpoints)')

if __name__=='__main__':main()
