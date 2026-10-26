#!/usr/bin/env python3
"""Exact characteristic and spectral-curvature checks for prism excitation."""
import sympy as s
x,z=s.symbols('x z')
states=[(a,b) for a in range(3) for b in range(3)]
def w(a,b):return int(a==0 and b==1)-int(a==1 and b==0)
def admissible(u,v):return w(u[0],v[0])+w(v[0],v[1])-w(u[1],v[1])-w(u[0],u[1])==0
m=s.Matrix([[z**w(u[0],v[0]) if admissible(u,v) else 0 for v in states] for u in states])
# Characteristic of z M(z) has polynomial entries; normalize by z^9.
q=s.cancel((z*m).charpoly(x).as_expr().subs(x,z*x)/z**9)
q0=s.factor(q.subs(z,1))
assert s.simplify(q0-(x-2)**3*(x+1)**4*(x**2-7*x+4))==0
qtt=s.factor((z*s.diff(z*s.diff(q,z),z)).subs(z,1))
assert s.simplify(qtt+2*(x-2)*(x+1)**2*(3*x**3+21*x-16))==0
lam=(7+s.sqrt(33))/2
sigma=2*(3*lam**3+21*lam-16)/(lam*(lam-2)**2*(lam+1)**2*(2*lam-7))
assert sigma>0
print('det(xI-M(1)) =',q0)
print('d^2/dt^2 det(xI-M(exp(t))) at t=0 =',qtt)
print('lambda=',s.N(lam,16),'sigma^2=',s.N(sigma,16))
print('prefactor=',s.N(1/s.sqrt(2*s.pi*sigma),16),'exp_rate=',s.N(lam/9,16))
print('SYMBOLIC CHECKS PASS')
