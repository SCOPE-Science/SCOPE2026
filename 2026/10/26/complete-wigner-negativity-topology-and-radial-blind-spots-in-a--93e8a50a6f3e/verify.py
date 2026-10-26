#!/usr/bin/env python3
"""Numerical checks for the exact Wigner-negativity topology theorem.
Requires NumPy. The proof of all-parameter statements is analytic.
"""
import math
import numpy as np


def dissipator(jump, rho):
    n = jump.conj().T @ jump
    return jump @ rho @ jump.conj().T - (n @ rho + rho @ n) / 2


def rates(a, b):
    d = 2*a+3*b
    s = math.sqrt((a+3*b)**2+16)
    p = np.array([2*b,b,2*a])/d
    v = 4*math.sqrt(2)*a*b/(d*s)
    phi = math.atan2(4,a+3*b)
    rho = np.diag(p).astype(complex)
    rho[0,2] = v * np.exp(1j*phi)
    rho[2,0] = rho[0,2].conjugate()
    return rho,p,v,phi


def superoperator_matrix(a,b):
    raise_ = np.array([[0,0,0],[1,0,0],[0,math.sqrt(2),0]],complex)
    x = (raise_ + raise_.conj().T)/math.sqrt(2)
    J2 = x @ raise_.conj().T  # x a: annihilation is raise_.conj().T
    H = np.diag([0,1,2])
    def L(r):
        return -1j*(H@r-r@H)+a*dissipator(raise_,r)+b*dissipator(J2,r)
    S = np.column_stack([L(np.eye(3,dtype=complex)[i:i+1,:]*np.eye(3,dtype=complex)[:,j:j+1]).reshape(9) for i in range(3) for j in range(3)])
    return S,L


def analytic_sign_poly(a,b,z,theta):
    s=math.sqrt((a+3*b)**2+16)
    phi=math.atan2(4,a+3*b)
    return ((2*a+b)+4*(b-4*a)*z+16*a*z*z+32*a*b/s*z*math.cos(2*theta+phi))/(2*a+3*b)


def graph_class(a,b):
    S=math.sqrt((a+3*b)**2+16)
    c=2*math.sqrt(a*(2*a+b))
    hi=4*a-b+8*a*b/S
    lo=4*a-b-8*a*b/S
    return 'positive' if hi <= c else ('annulus' if lo > c else 'two_lobes')


def verify():
    checks=0
    for a,b in ((.05,.04),(.7,.7),(.25,.5),(.5,.25),(4,1),(10,.15),(.01,10),(30,.01),(1,1),(2,1),(7,20)):
        rho,p,v,phi=rates(a,b)
        S,L=superoperator_matrix(a,b)
        assert np.max(np.abs(L(rho))) < 4e-13
        assert abs(np.trace(rho)-1)<1e-13
        assert np.linalg.eigvalsh(rho).min() > -1e-12
        checks+=3
        e=np.linalg.eigvals(S)
        assert np.min(np.abs(e))<1e-11
        checks+=1
        for z in (.001,.02,.2,.7,1.,2.,4.):
            for t in (.0,.24,.91,1.4,2.,2.6):
                W= p[0]+p[1]*(4*z-1)+p[2]*(1-8*z+8*z*z)+4*math.sqrt(2)*v*z*math.cos(2*t+phi)
                assert abs(W-analytic_sign_poly(a,b,z,t)) < 8e-13
                checks+=1
        zvals=np.linspace(0,6,401)
        thvals=np.linspace(0,2*math.pi,365)
        neg= min(analytic_sign_poly(a,b,z,t) for z in zvals for t in thvals)
        case=graph_class(a,b)
        if case=='positive':assert neg>-1e-10
        else:assert neg < -1e-5
        checks+=1
    c=2*math.sqrt(3)-3
    t_onset=c/math.sqrt(4-c*c)
    h=7-2*math.sqrt(10)
    t_split=4*h/math.sqrt(256-25*h*h)
    assert graph_class(.95*t_onset,.95*t_onset)=='positive'
    assert graph_class(1.05*t_onset,1.05*t_onset)=='two_lobes'
    assert graph_class(2*.95*t_split,.95*t_split)=='annulus'
    assert graph_class(2*1.05*t_split,1.05*t_split)=='two_lobes'
    checks+=4
    print('VERIFIED',checks,'checks; equal-rate onset=',t_onset,'2:1 topology split=',t_split)

if __name__=='__main__':verify()
