"""Independent finite diagnostics for reverse Bessel polynomial zero-ratio theorem.
Run: python3 rational_bessel_zero_checker.py. Analytic proof is essential.
"""
import sympy as sp
import numpy as np
from scipy.special import spherical_jn
from scipy.optimize import brentq

z=sp.symbols('z')
checks=0
for ell in range(1,9):
    # polynomial P_ell(t)=sum a_k t**(ell-k), i.e. z**ell Q_ell(1/z)
    a=[sp.factorial(ell+k)/(2**k*sp.factorial(k)*sp.factorial(ell-k)) for k in range(ell+1)]
    U=sum(a[k]*sp.I**k*z**(ell-k) for k in range(ell+1))
    V=sum(a[k]*(-sp.I)**k*z**(ell-k) for k in range(ell+1))
    # R(z)=(-1)^ell * V(z) / U(z)
    R=sp.cancel((-1)**ell * V / U)
    assert sp.simplify(R.subs(z,0)-1)==0
    assert sp.simplify(sp.diff(R,z))!=0
    for p,q in [(2,1),(3,2),(5,3),(4,7)]:
        D=sp.together(R.subs(z,p*z)**q-R.subs(z,q*z)**p)
        assert sp.together(D)!=0 and sp.fraction(sp.cancel(D))[0]!=0
        checks+=1
    # root checks: scan using sign changes; roots of j_ell(x), positive x up to 70
    grid=np.linspace(1.e-2,70,15001)
    vals=spherical_jn(ell,grid)
    roots=[]
    for i in range(len(grid)-1):
        if vals[i]*vals[i+1]<0:
            roots.append(brentq(lambda s: spherical_jn(ell,s),grid[i],grid[i+1]))
    for x in roots:
        rr=complex(R.subs(z,x).evalf(18))
        assert abs(np.exp(2j*x)-rr)<2.e-8
        checks+=1
    for i,x in enumerate(roots):
        for y in roots[i+1:]:
            r=x/y
            assert min(abs(r-a/b) for b in range(1,7) for a in range(1,7*b+1))>1.e-8, (ell,x,y)
            checks+=1
print('PASS',checks,'finite exact-identity, spherical Bessel and ratio diagnostics')
