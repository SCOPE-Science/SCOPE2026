"""Reproducible symbolic replay for the conservative Gumowski--Mira period-two theorem.

Requires SymPy 1.12 or newer. The accompanying proof establishes the global
root count by an analytic sign argument and Descartes' rule; numerical roots
here serve only as consistency checks, not as proof of exhaustive counting.
"""
import sympy as sp

x,t,u,v,w,e=sp.symbols('x t u v w e', real=True)
mu=-1-t
N=mu*x*(1+x*x)+2*(1-mu)*x*x
D=1+x*x
H=D*D+N*N
q=-t*(t+1)**2*x**6+4*t*(t+1)*(t+2)*x**5-t*(6*t*t+20*t+19)*x**4+2*t*(t+2)*(2*t+1)*x**3+(-t**3+2*t*t+13*t+16)*x*x-2*t*(t+2)*x-t
h=N/D
composition=sp.cancel((mu*h+2*(1-mu)*h*h/(1+h*h)-x)*D*H)
assert sp.factor(composition-x*(mu-1)*(x-1)**2*q)==0
pivot=sp.factor(q.subs(x,-1/(1+t)))
assert sp.simplify(pivot-2*(t**4+4*t**3+8*t*t+8*t+8)/(t+1)**4)==0
assert q.subs(x,0)==-t
assert sp.simplify(sp.limit(q.subs(x,sp.sqrt(t)*u)/t,t,0,dir='+')-(16*u*u-1))==0
assert sp.factor(sp.limit(e**2*q.subs({x:v/e,t:e**4}),e,0))==-v**2*(v-2)*(v+2)*(v*v+4)
out_plus=sp.Poly(sp.expand(e**2*q.subs({x:2/e+w,t:e**4})),e)
out_minus=sp.Poly(sp.expand(e**2*q.subs({x:-2/e+w,t:e**4})),e)
assert sp.simplify(out_plus.coeff_monomial(e)+128*(w-2))==0
assert sp.simplify(out_minus.coeff_monomial(e)-128*(w-2))==0
# Descartes certification: all Q_t(-u) terms of degrees 3 through 6 are
# strictly negative for t>0, degree 1 is positive, degree 0 negative;
# the degree-2 coefficient is unrestricted. Both possible sign patterns
# have exactly two changes, hence at most two negative real roots.
qu=sp.Poly(sp.expand(q.subs(x,-u)),u)
assert sp.factor(qu.nth(0))==-t
assert sp.factor(qu.nth(1))==2*t*(t+2)
assert sp.factor(qu.nth(3))==-2*t*(t+2)*(2*t+1)
assert sp.factor(qu.nth(4))==-t*(6*t*t+20*t+19)
assert sp.factor(qu.nth(5))==-4*t*(t+1)*(t+2)
assert sp.factor(qu.nth(6))==-t*(t+1)**2
# Check scalar map formula at fixed roots 0 and 1.
g=mu*x+2*(1-mu)*x*x/(1+x*x)
assert sp.simplify((g-x)-(mu-1)*x*(x-1)**2/(1+x*x))==0
assert sp.factor(g.subs(x,1)-1)==0
print('All exact polynomial, rational, endpoint and asymptotic identities verified.')
