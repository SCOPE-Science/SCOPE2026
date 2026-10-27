#!/usr/bin/env python3
"""Independent exact-identity and numerical diagnostics for a correlated TLS family.

Scientific claims of global optimality and asymptotic limits are established
analytically in RESULT.md, not by finite optimization diagnostics.
"""
import sympy as sp
import numpy as np
from scipy.optimize import minimize

u, v, gamma, beta = sp.symbols('u v gamma beta', real=True)
A = sp.Matrix([[1, gamma], [0, sp.sqrt(1-gamma**2)], [0, 0]])
b = sp.Matrix([0, 0, sp.sqrt(beta)])
x = sp.Matrix([u, v])
w = 1 + u**2 + v**2
F = sp.expand((A*x-b).dot(A*x-b))/w + u**2
K = beta-1-gamma**2
assert sp.simplify(A.T*A-sp.Matrix([[1,gamma],[gamma,1]])) == sp.zeros(2)
assert sp.simplify((F-1)*w-(K+(u*v+gamma)**2+u**2+u**4)) == 0
assert sp.simplify((u*v+gamma)**2+u**2-
      ((1+v**2)*(u+gamma*v/(1+v**2))**2+gamma**2/(1+v**2))) == 0
print('Exact Gram, square completion, and polynomial identities: PASS')

g=0.5
for k in [-0.25,0.0,0.25]:
    B2=1+g*g+k
    def valgrad(z,eps):
        u,v=map(float,z)
        w=1+u*u+v*v
        n=u*u+2*g*u*v+v*v+B2
        f=n/w+u*u+eps*(u*u+v*v)
        du=((2*u+2*g*v)*w-2*u*n)/w**2+2*(1+eps)*u
        dv=((2*v+2*g*u)*w-2*v*n)/w**2+2*eps*v
        return f,np.array([du,dv])
    for eps in [1.e-4,1.e-6,1.e-8]:
        V=(k/eps)**0.25 if k>0 else (2*g*g/eps)**(1/6) if k==0 else 3.0
        seeds=[[-g/V,V],[g/V,-V],[0,0],[0,1],[0,-1],[.25,-2],[-.25,2]]
        solutions=[minimize(lambda z:valgrad(z,eps),z0,jac=True,method='BFGS',
                            options={'gtol':1e-11,'maxiter':800}) for z0 in seeds]
        best=min(solutions,key=lambda r:r.fun)
        u0,v0=best.x
        assert np.isfinite(best.fun)
        assert np.linalg.norm(valgrad(best.x,eps)[1]) < 1e-6
        if k>=0 and eps<=1e-6: assert abs(u0*v0+g)<0.015
        if k<0 and eps<=1e-6: assert best.fun < 1
        if k==0 and eps<=1e-6:
            ratio=(best.fun-1)/(eps**(2/3))
            assert abs(ratio-3*(g*g/4)**(1/3))<0.03
        if k>0 and eps<=1e-6:
            ratio=(best.fun-1)/np.sqrt(eps)
            assert abs(ratio-2*np.sqrt(k))<0.01
        print('K={:+.2f} epsilon={:.0e} u={:.6g} v={:.6g} value={:.12g}'.format(
              k,eps,u0,v0,best.fun))
print('Representative finite-dimensional diagnostics: PASS')
