#!/usr/bin/env python3
"""Reproduce the exact algebraic and spectral checks in the accompanying result."""
from sympy import Matrix, Poly, Rational, diff, factor, sqrt, symbols, simplify
import numpy as np

x, gamma, m, lam = symbols('x gamma m lam')
mu = Rational(1, 100)
gam = (1-x)*(x+mu)/(2*x+mu)
r1 = gamma*x/(x+mu)
r2 = r1
s = gamma*mu/(x+mu)
J = Matrix([[-x,0,-x], [gamma-r1,-(x+mu),0], [0,mu,-mu]])
A = 2*(x+mu)
B = x*x + 3*x*mu + mu*mu
C = x*mu*(x+mu) + x*gamma*mu*mu/(x+mu)
assert simplify(J.charpoly(lam).as_expr() - (lam**3+A*lam**2+B*lam+C)) == 0
assert simplify((s+x+r1+r2-1).subs(gamma,gam)) == 0
assert simplify((x*x+(mu+2*gamma-1)*x+mu*(gamma-1)).subs(gamma,gam)) == 0
Qexpr = 200000000*x**4 + 8000000*x**3 + 110000*x*x - 4450*x + 1
Delta = factor((A*B-C).subs(gamma,gam))
assert simplify(Delta-Qexpr/(500000*(200*x+1))) == 0
assert simplify(diff(gam,x) - -(20000*x*x+200*x+101)/(200*x+1)**2) == 0
p=Poly(Qexpr,x)
assert p.eval(Rational(1,5000))>0
assert p.eval(Rational(1,4000))<0
assert p.eval(Rational(1,100))<0
assert p.eval(Rational(1,50))>0
assert p.count_roots(0,Rational(99,100)) == 2
roots = [complex(z) for z in p.nroots(maxsteps=200)]
real_pos = sorted([z.real for z in roots if abs(z.imag)<1e-12 and 0<z.real<.99])
assert len(real_pos)==2
lo_x, hi_x = real_pos
gamma_minus=float(gam.subs(x,hi_x))
gamma_plus=float(gam.subs(x,lo_x))
assert abs(gamma_minus-0.6121330228840222)<1e-12
assert abs(gamma_plus-0.9781559947036933)<1e-12

for g, unstable in [(0.5,False),(0.7,True),(0.9,True),(0.99,False)]:
    xx=float(((1-mu-2*gamma)+sqrt((mu+2*gamma-1)**2+4*mu*(1-gamma))).subs(gamma,g).evalf(35))/2
    rr=g*xx/(xx+float(mu))
    j=np.array([[-xx,0,-xx],[g-rr,-(xx+float(mu)),0],[0,float(mu),-float(mu)]])
    eigen=np.linalg.eigvals(j)
    if unstable:
        assert sum(z.real>1e-8 for z in eigen)==2
    else:
        assert all(z.real<-1e-8 for z in eigen)
    assert abs(eigen.sum()+float(A.subs(x,xx)))<1e-10

print('VERIFY_OK')
print('quartic:',Qexpr)
print('gamma_minus',format(gamma_minus,'.15f'))
print('gamma_plus',format(gamma_plus,'.15f'))
print('x_large',format(hi_x,'.15f'))
print('x_small',format(lo_x,'.15f'))
