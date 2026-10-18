#!/usr/bin/env python3
"""Reproducible consistency checks for bistable weak-activity response.
The infinite-dimensional statements follow analytically, not from this finite grid.
"""
import numpy as np
from scipy.integrate import quad
from scipy.sparse import diags
from scipy.sparse.linalg import spsolve


def exact_variance(a,b,T):
    return 2*(T/b)**2 + 2*a*a/(2-np.exp(-a*b/T))


def grid(a,b,T,n=801):
    xmax=a+14*T/b
    x=np.linspace(-xmax,xmax,n)
    h=x[1]-x[0]
    U=b*np.abs(np.abs(x)-a)
    pi=np.exp(-(U-np.min(U))/T)
    pi/=sum(pi)
    edges=T/h**2*np.sqrt(pi[:-1]*pi[1:])
    lo=-edges/pi[1:]
    hi=-edges/pi[:-1]
    diag=np.zeros(n)
    diag[:-1]+=edges/pi[:-1]
    diag[1:]+=edges/pi[1:]
    K=diags((lo,diag,hi),(-1,0,1),format='csr')
    return x,pi,K


def inner(x,y,pi):return np.dot(x*pi,y)


def check():
    count=0
    for a,b,T in [(0.4,1.0,1.0),(1.0,1.0,1.0),(1.8,0.7,1.0),(0.9,2.5,0.8)]:
        z=quad(lambda x: np.exp(-b*abs(abs(x)-a)/T),-a-60*T/b,a+60*T/b,points=[-a,0,a],epsabs=1.e-11)[0]
        second=quad(lambda x:x*x*np.exp(-b*abs(abs(x)-a)/T),-a-60*T/b,a+60*T/b,points=[-a,0,a],epsabs=1.e-10)[0]/z
        assert abs(second-exact_variance(a,b,T))<3e-8
        count+=1
        x,pi,K=grid(a,b,T)
        xc=x-inner(x,np.ones_like(x),pi)
        force=K@xc
        vdis=inner(xc,xc,pi)
        assert abs(vdis-exact_variance(a,b,T))/exact_variance(a,b,T)<0.006
        count+=1
        energy=inner(xc,force,pi)
        assert abs(energy/T-1)<0.006
        count+=1
        force2=inner(force,force,pi)
        assert abs(force2/(b*b)-1)<0.06
        count+=1
        vals=[]
        for r in [0.03,0.08,0.2,0.5,1,2,5,20]:
            sol=spsolve(K+2*r*diags(np.ones(len(x)),0,format='csr'),force)
            chi=(energy-inner(force,sol,pi))/(T*T)
            via_spectral=(2*r)/(T*T)*inner(xc,sol,pi)
            assert abs(chi-via_spectral)<3e-8, (chi,via_spectral)
            count+=1
            assert 0<chi<energy/T**2
            count+=1
            vals.append(chi)
        assert np.all(np.diff(vals)>0)
        count+=1
        for r in [0.05,0.2,0.8,2,7]:
            mat=K+2*r*diags(np.ones(len(x)),0,format='csr')
            z1=spsolve(mat,force)
            z2=spsolve(mat,z1)
            z3=spsolve(mat,z2)
            deriv=2/T**2*inner(force,z2,pi)
            deriv2=-8/T**2*inner(force,z3,pi)
            assert deriv>0 and deriv2<0
            count+=1
        tiny=1e-4
        val_small=(tiny/T**2)*inner(xc,spsolve(K+tiny*diags(np.ones(len(x)),0,format='csr'),force),pi)
        assert abs(val_small/tiny-vdis/T**2)/(vdis/T**2)<0.02
        count+=1
        large=1e4
        high=large*inner(force,spsolve(K+large*diags(np.ones(len(x)),0,format='csr'),force),pi)
        assert abs(high-force2)/force2<0.04
        count+=1
        # Exact weak-rate/infinite-rate coefficients follow by spectral dominated convergence.
        assert exact_variance(a+0.001,b,T)>exact_variance(a,b,T)
        count+=1
    print('PASSED',count,'standalone assertions; finite grid is illustrative, not proof')

if __name__=='__main__':check()
