"""Exact identities for the cubic complete-graph maximal bound.
Run: python3 check_cubic_maximal.py
"""
import sympy as sp
from scipy.optimize import minimize_scalar

r = sp.sqrt(7)
y = sp.Rational(3,2)
z = (1+2*r)/9
a = (32-4*r)/57
L = (613+16*r)/513
b = 1-a
assert sp.simplify(a*y+b*z-1)==0
assert sp.simplify((L-1)*y*y-L*z*z)==0
assert sp.simplify(L*z*z*(3-2*z)-1)==0
x=sp.symbols('x',real=True)
S_low=L*x**3-3*L*z*z*(x-1)-1
S_high=(L-1)*x**3-3*L*z*z*(x-1)
assert sp.simplify(S_low-L*(x-z)**2*(x+2*z))==0
assert sp.simplify(S_high-(L-1)*(x-y)**2*(x+2*y))==0

A,T=sp.symbols('A T',positive=True)
b0=1-A;m=A+b0*T
F=(A+b0*m**3)/(A+b0*T**3)
assert sp.simplify(sp.diff(F,T)-3*A*b0*(b0*m*m*(1-T*T)-T*T)/(A+b0*T**3)**2)==0
D=sp.simplify(a*y**3+b*z**3)
kap=sp.simplify(((y-z)**2/(a/(3*(L-1)*y)+b/(3*L*z)))/D)
assert sp.simplify(kap-(1-r/14))==0
# Schur-complement curvature from the unconstrained two-level quotient.
tstar=sp.simplify(z/y)
Faa=sp.diff(F,A,2).subs({A:a,T:tstar})
Fat=sp.diff(sp.diff(F,A),T).subs({A:a,T:tstar})
Ftt=sp.diff(F,T,2).subs({A:a,T:tstar})
assert sp.simplify(Ftt)<0
assert sp.simplify((Faa-Fat**2/Ftt)/2+kap)==0
# Numerical stress tests, not substitutes for the symbolic identities.
import math
an=float(a); lam=float(L); k=float(kap)
for n in (4,5,6,7,10,30,50,200):
    values=[]
    for j in range(1,n):
        u=j/n; v=1-u
        fun=lambda t:(u+v*(u+v*t)**3)/(u+v*t**3)
        opt=minimize_scalar(lambda t:-fun(t),bounds=(0,1),method='bounded',options={'xatol':1e-12})
        values.append((fun(opt.x),j))
    mx,j=max(values)
    delta=min(abs(h/n-an) for h in range(1,n))
    assert 0 < lam-mx and abs((lam-mx)/(k*delta*delta)-1)<.15
    print(f"n={n:3d}, k={j:3d}, gap={lam-mx:.10g}, gap/quadratic={(lam-mx)/(k*delta*delta):.8f}")
print('All exact identities PASS')
print('a*=',a, float(a),'lambda=',L,float(L),'kappa=',kap,float(kap))
