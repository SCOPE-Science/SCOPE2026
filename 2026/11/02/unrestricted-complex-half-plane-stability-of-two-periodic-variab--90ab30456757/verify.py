#!/usr/bin/env python3
"""Reproduce symbolic Floquet and Schur identities for two-periodic BDF2.
Dependencies: Python 3, sympy, numpy.  All random checks are deterministic.
"""
import math
import numpy as np
import sympy as sp

def verify():
    checks=0
    r,t,z=sp.symbols('r t z', positive=True)
    chi=r+1/r
    def T(q,w):
        den=1+2*q+(1+q)*w
        return sp.Matrix([[(1+q)**2/den, -q**2/den],[1,0]])
    # Full-period parameter z=kappa*h*(1+r), first step rh then h.
    P=T(1/r,z/(1+r))*T(r,r*z/(1+r))
    D=z*z+(chi+4)*z+2*chi+5
    N=2*chi+6-chi*z
    assert sp.factor(P.det()-1/D)==0;checks+=1
    assert sp.factor(sp.trace(P)-N/D)==0;checks+=1
    assert sp.simplify(D-(2*chi+5)-z*(z+chi+4))==0;checks+=1
    assert sp.factor((2*chi+6)-(2*chi+5)-1)==0;checks+=1
    # Complex variable z=x+iy and positive chi replaced independent C>=2
    x,y,C=sp.symbols('x y C', real=True)
    zz=x+sp.I*y
    Dc=zz**2+(C+4)*zz+2*C+5
    Nc=2*C+6-C*zz
    dd=sp.expand(Dc*sp.conjugate(Dc))
    nn=sp.expand((Nc*sp.conjugate(Dc)-sp.conjugate(Nc))*(sp.conjugate(Nc)*Dc-Nc))
    q=x*x+y*y
    F=q*q+2*(C+4)*x*q+4*(2*C+5)*x*x+8*(C+2)*x
    G=F+(C+2)*(C+6)*q+12*(C+2)**2*x+4*(C+2)**2*(C+3)
    assert sp.expand((dd-1)**2-nn-F*G)==0;checks+=1
    assert sp.expand(dd-1-(q*q+2*(C+4)*x*q+(C*C+4*C+6)*q+4*(2*C+5)*x*x+2*(C+4)*(2*C+5)*x+(2*C+5)**2-1))==0;checks+=1
    # Algebraic extreme ratio and symmetric ratio scalar limits.
    assert sp.limit(N/D,r,sp.oo)==(2-z)/(2+z);checks+=1
    assert sp.limit(1/D,r,sp.oo)==0;checks+=1
    assert sp.simplify(chi.subs(r,1)-2)==0;checks+=1
    rng=np.random.default_rng(20261025)
    for _ in range(100):
        rr=float(np.exp(rng.uniform(-12,12)))
        xx=float(np.exp(rng.uniform(-8,5))) if rng.random()<0.5 else 0.0
        yy=float(rng.normal(0,8))
        z0=complex(xx,yy)
        if z0==0: z0=1j
        c=rr+1/rr
        den=z0*z0+(c+4)*z0+2*c+5
        num=2*c+6-c*z0
        roots=np.roots([den,-num,1])
        assert max(abs(roots))<1+1e-9,(rr,z0,roots)
        checks+=1
    # Full real period and direct numerical monodromy match.
    for _ in range(100):
        rr=float(np.exp(rng.uniform(-7,7)))
        zz0=complex(rng.uniform(0,20),rng.uniform(-30,30))
        def Ta(qq,ww):
            den=1+2*qq+(1+qq)*ww
            return np.array([[(1+qq)**2/den,-qq*qq/den],[1,0]],dtype=np.complex128)
        P0=Ta(1/rr,zz0/(1+rr))@Ta(rr,rr*zz0/(1+rr))
        c=rr+1/rr
        de=zz0*zz0+(c+4)*zz0+2*c+5
        nu=2*c+6-c*zz0
        assert abs(np.linalg.det(P0)-1/de)<1e-8
        assert abs(np.trace(P0)-nu/de)<1e-8
        checks+=2
    for rr in (1,4,1000):
        z0=2j
        c=rr+1/rr
        roots=np.roots([z0*z0+(c+4)*z0+2*c+5,-(2*c+6-c*z0),1])
        print('r=',rr,'magnitudes=',sorted(map(abs,roots),reverse=True))
        checks+=1
    print('PASS',checks,'identities and deterministic numerical checks')

if __name__=='__main__':
    verify()
