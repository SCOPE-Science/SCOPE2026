"""Reproduce symbolic identities and finite graph checks for a polynomial predator-prey network model.

Requires Python 3, sympy, and numpy. The symbolic bifurcation argument
in the accompanying mathematical text is not replaced by finite tests.
"""
import math
import numpy as np
import sympy as s

count = 0
def check(x, message='check'):
    global count
    assert x, message
    count += 1

U,V,z,r=s.symbols('U V z r', real=True)
u,v=1+U,1+V
f=u*(-u*u+3*u-1-v)
g=v*(4*u-3*v-1)
check(s.expand(f-(U-V-U*V-U**3))==0,'prey Taylor identity')
check(s.expand(g-(4*U-3*V+4*U*V-3*V**2))==0,'predator Taylor identity')
J=s.Matrix([[1,-1],[4,-3]])
check(J.trace()==-2 and J.det()==1,'homogeneous Jacobian')
M=J-s.diag(z,r*z)
check(s.expand(M.det()-(1-(r-3)*z+r*z*z))==0,'dispersion polynomial')
check(s.expand(M.trace()+2+(r+1)*z)==0,'modal trace')
h=s.symbols('h',real=True)
# Spatial mean second-order equations: A-B=h and 4A-3B=-4h+3h^2.
A,B=s.symbols('A B')
sol=s.solve([A-B-h,4*A-3*B+4*h-3*h*h],[A,B]);
check(s.simplify(sol[A]+7*h-3*h*h)==0,'prey quadratic mean coefficient')
check(s.simplify(sol[B]+8*h-3*h*h)==0,'predator quadratic mean coefficient')
# Exact finite amplitude mean balance identities from stationary average equations.
p,q,c=s.symbols('p q c')  # means of UV, V^2, U^3
sol2=s.solve([A-B-p-c,4*A-3*B+4*p-3*q],[A,B]);
check(s.simplify(sol2[A]+7*p-3*q+3*c)==0)
check(s.simplify(sol2[B]+8*p-3*q+4*c)==0)
rr=s.Rational(91,10)
zminus=s.Rational(2,7);zplus=s.Rational(5,13)
check(s.factor(M.det().subs({r:rr,z:zminus}))==0)
check(s.factor(M.det().subs({r:rr,z:zplus}))==0)
check(zminus>0 and zplus<1 and zplus/zminus<s.Integer(3))
# For paths of orders 2..40, spectra match elementary trigonometric values,
# ratios strictly decrease, and sufficiently small r>9 separates all modal windows.
for n in range(2,41):
    L=np.zeros((n,n))
    for i in range(n-1):
        L[i,i]+=1;L[i+1,i+1]+=1;L[i,i+1]-=1;L[i+1,i]-=1
    lambdas=np.linalg.eigvalsh(L)[1:]
    exact=np.array([2-2*math.cos(math.pi*j/n) for j in range(1,n)])
    check(np.max(np.abs(lambdas-exact))<3e-13, f'path eigenspectrum n={n}')
    if n>3:
        ratios=lambdas[1:]/lambdas[:-1]
        check(np.all(np.diff(ratios)<0),f'path ratios decrease n={n}')
    gamma_min=np.min(lambdas[1:]/lambdas[:-1]) if n>2 else float('inf')
    epsilon=1e-6 if n<=15 else 1e-9
    # r-9 small enough to ensure the disjoint-window regime numerically.
    while True:
        rrval=9+epsilon
        discriminant=(rrval-1)*(rrval-9)
        zmi=(rrval-3-math.sqrt(discriminant))/(2*rrval)
        zpl=(rrval-3+math.sqrt(discriminant))/(2*rrval)
        if zpl/zmi < gamma_min: break
        epsilon *= .1
        if epsilon<1e-13: raise AssertionError('numerical tiny epsilon limit')
    intervals=sorted([(zmi/lam,zpl/lam) for lam in lambdas])
    check(all(intervals[j][1]<intervals[j+1][0] for j in range(len(intervals)-1)),f'disjoint windows n={n}')
# Nonlinear CR transversality: first derivative of the determinant at each root nonzero.
zz=s.symbols('zz',positive=True)
det_poly=s.expand(M.det())
for z0 in (zminus,zplus):
    deriv=s.diff(det_poly,z).subs({r:rr,z:z0})
    check(deriv!=0,'transversality')
print(f'PASS: {count} symbolic and finite graph checks')
