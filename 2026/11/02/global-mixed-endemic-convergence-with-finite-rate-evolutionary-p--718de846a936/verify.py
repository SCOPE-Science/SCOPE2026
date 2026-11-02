#!/usr/bin/env python3
"""Exact algebra and supplementary rational/numerical checks for an SIS protection system.

Run with SymPy installed. The proof of global convergence is in RESULT.md;
this program certifies its nontrivial algebraic identity and a sample equilibrium.
"""
from sympy import symbols, factor, Rational, simplify, diff

Y, Z, W, q, p = symbols('Y Z W q p', real=True)
alpha, beta_p, beta_u, gamma, L, c, rho_S = symbols(
    'alpha beta_p beta_u gamma L c rho_S', positive=True)
u = 1-alpha
delta = beta_u-beta_p
A = alpha+u*Z
B = beta_p+delta*W
fy = Y*((1-Y)*A*B-gamma)
fz = rho_S*Z*(1-Z)*(c-L*u*B*Y)
# Differentiate the entropy exactly; the constants q,p are fixed.
V_y = 1-q/Y
V_z = (1-q)/(rho_S*L)*(Z-p)/(Z*(1-Z))
Vdot = V_y*fy + V_z*fz
Vdot = Vdot.subs({c:L*u*beta_p*q, gamma:beta_p*(1-q)*(alpha+u*p)})
claimed = -beta_p*A*(Y-q)**2 + delta*W*((Y-q)*(1-Y)*A-(1-q)*u*Y*(Z-p))
assert factor(Vdot-claimed) == 0
print('Exact symbolic entropy identity: PASS')

v = {alpha:Rational(1,2), beta_p:Rational(3,4),
     beta_u:Rational(7,8),gamma:Rational(27,64),
     L:Rational(4),c:Rational(3,8),rho_S:Rational(2,3)}
qv = simplify((c/(L*u*beta_p)).subs(v))
# In p expression q must be replaced by the computed rational first.
pv=simplify((((gamma/(beta_p*(1-q))-alpha)/u).subs(q,qv)).subs(v))
assert qv == Rational(1,4) and pv == Rational(1,2)
assert (v[alpha]*v[beta_p]*(1-qv)<v[gamma]<v[beta_p]*(1-qv))
assert simplify(fy.subs({Y:qv,Z:pv,W:0}).subs(v))==0
assert simplify(fz.subs({Y:qv,Z:pv,W:0}).subs(v))==0
print('Exact rational equilibrium and strict parameter inequalities: PASS')

# Supplementary explicit fourth-order Runge–Kutta trajectories: finite time
# only, without any claim of proof by numerical experiment.
import math
params = dict(al=float(v[alpha]),bp=float(v[beta_p]),
              bu=float(v[beta_u]),gm=float(v[gamma]),
              loss=float(v[L]),cost=float(v[c]),rs=float(v[rho_S]),
              ri=4.0,kap=0.2)

def vector(x):
    yy,zz,ww = x
    a=params['al']+(1-params['al'])*zz
    b=params['bp']+(params['bu']-params['bp'])*ww
    return (yy*((1-yy)*a*b-params['gm']),
            params['rs']*zz*(1-zz)*(params['cost']-params['loss']*(1-params['al'])*b*yy),
            -params['ri']*params['kap']*ww*(1-ww))

def run(x,dt=0.05,steps=20000):
    for _ in range(steps):
        a=vector(x)
        b=vector(tuple(x[i]+dt*a[i]/2 for i in range(3)))
        d=vector(tuple(x[i]+dt*b[i]/2 for i in range(3)))
        e=vector(tuple(x[i]+dt*d[i] for i in range(3)))
        x=tuple(x[i]+dt*(a[i]+2*b[i]+2*d[i]+e[i])/6 for i in range(3))
        assert all(math.isfinite(t) for t in x)
    return x

for x0 in [(0.02,0.08,0.95),(0.98,0.92,0.2),(0.4,0.2,0.7)]:
    x=run(x0)
    assert max(abs(x[i]-target) for i,target in enumerate((0.25,0.5,0.0)))<1e-7,(x0,x)
print('Three finite-time RK4 convergence diagnostics: PASS')
