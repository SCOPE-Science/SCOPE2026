"""Exact algebra and rational endpoint checks for a weak-Allee harvesting model.

Requires Python 3 and SymPy. Run `python verify.py`.
"""
import sympy as sp

u, v = sp.symbols('u v', real=True)
alpha, A, beta, eta, E = sp.symbols('alpha A beta eta E', positive=True)
F = alpha*u*(1-u)*(u+A) - alpha*u*v/(1+beta*u) - E*u
G = beta*u*v/(1+beta*u) - eta*v*v/(1+eta*v)
h = (1-u)*(u+A) - beta*u/(eta*(1+beta*u))
J = sp.Matrix([F, G]).jacobian([u, v])
Je = sp.simplify(J.subs({v: beta*u/eta, E:alpha*h}))
assert sp.simplify(G.subs(v, beta*u/eta)) == 0
assert sp.simplify(F.subs({v:beta*u/eta,E:alpha*h})) == 0
assert sp.simplify(sp.det(Je) + alpha*beta*u*u*sp.diff(h,u)/(1+beta*u)**2) == 0
assert sp.simplify(sp.diff(h,u,2)-(-2+2*beta**2/(eta*(1+beta*u)**3))) == 0
params = {alpha:sp.Integer(1), A:sp.Rational(1,5), beta:sp.Integer(8), eta:sp.Integer(6), E:sp.Rational(39,200)}
hw = h.subs(params)
P = -4800*u**3 + 3240*u**2 - 296*u + 3
Q = 960*u**3 - 144*u**2 - 161*u + 54
assert sp.simplify(600*(1+8*u)*(hw-sp.Rational(39,200))-P)==0
assert sp.simplify(Je.trace().subs(params)+2*u*Q/(15*(1+8*u)**2))==0
assert sp.factor(sp.diff(Q,u)) == (24*u-7)*(120*u+23)
assert Q.subs(u,sp.Rational(7,24)) == sp.Rational(335,18)
intervals=[(sp.Rational(11,1000),sp.Rational(12,1000)),
           (sp.Rational(94,1000),sp.Rational(96,1000)),
           (sp.Rational(568,1000),sp.Rational(569,1000))]
for i,(lo,hi) in enumerate(intervals):
    sign_lo = sp.sign(P.subs(u,lo));sign_hi = sp.sign(P.subs(u,hi))
    assert (sign_lo,sign_hi) in ((1,-1),(-1,1))
    assert 0<lo<hi<1
    # Signs of h' at each root are those of P's crossings.
    print('root interval',i+1,str(lo),str(hi),'signs',sign_lo,sign_hi)
assert sp.simplify(sp.diff(h,u).subs(params).subs(u,0)) == -sp.Rational(8,15)
assert sp.Rational(39,200) < sp.Rational(1,5)
print('VERIFY_OK')
