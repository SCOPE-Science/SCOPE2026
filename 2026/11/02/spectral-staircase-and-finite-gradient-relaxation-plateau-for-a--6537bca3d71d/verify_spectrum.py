"""Numerical checks of an exact smooth run-and-tumble spectral theorem.

The finite-difference computations validate example values, not the infinite-line proof.
Requires numpy, scipy, sympy.
"""
import math
import numpy as np
import sympy as sp
from scipy.linalg import eigh_tridiagonal

x,a,g=sp.symbols('x a g',positive=True,real=True)
u=sp.Function('f')(x)
T=sp.tanh(g*x)
F=(a/g)*sp.log(sp.cosh(g*x))
p=sp.exp(-F)*u
left=sp.simplify(sp.exp(F)*(sp.diff(p,x,2)+2*a*sp.diff(T*p,x)))
right=sp.diff(u,x,2)-(a*a-(a*a+a*g)/sp.cosh(g*x)**2)*u
assert sp.simplify(left-right)==0
print('conjugation: OK')

v=1.0
rate0=0.8
rate1=0.5
for steep in (0.2,0.3,0.65):
    nu=rate1/(v*steep)
    exact=[steep**2*n*(2*nu-n) for n in range(math.ceil(nu)) if n<nu]
    L=55.0
    count=2400
    dx=2*L/(count+1)
    xs=np.linspace(-L+dx,L-dx,count)
    potential=(rate1/v)**2-((rate1/v)**2+(rate1/v)*steep)/np.cosh(steep*xs)**2
    diagonal=2/dx**2+potential
    ev=eigh_tridiagonal(diagonal,np.full(count-1,-1/dx**2),select='i',select_range=(0,len(exact)+2),eigvals_only=True)
    for j,energy in enumerate(exact):
        assert abs(ev[j]-energy)<0.002,(steep,j,ev[j],energy)
        if j:
            root=-rate0+math.sqrt(rate0**2-v*v*energy)
            assert root<0
    assert len(exact)==math.ceil(nu)
    expected=rate0-math.sqrt(rate0**2-(v*v*exact[1] if len(exact)>1 else rate1**2))
    if steep>=rate1/v:
        assert len(exact)==1
        assert abs(expected-(rate0-math.sqrt(rate0**2-rate1**2)))<1e-12
    else:
        predicted=rate0-math.sqrt(rate0**2-2*v*rate1*steep+v*v*steep**2)
        assert abs(expected-predicted)<1e-12
    print('gradient=',steep,'bound_modes=',len(exact)-1,'spectral_gap=',round(expected,9),'checks: OK')
print('VERIFY_OK')
