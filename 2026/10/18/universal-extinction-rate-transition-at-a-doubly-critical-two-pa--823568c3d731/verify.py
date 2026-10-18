"""Checks of finite symbolic identities and illustrative trajectories.

Requirements: sympy, scipy. Run: python verify.py
The mathematical asymptotic statements require the accompanying proof.
"""
from fractions import Fraction
from math import isfinite
from sympy import symbols, Rational, factor, simplify, diff
from scipy.integrate import solve_ivp

checks = 0
u, v, s, d, h, m = symbols('u v s d h m', positive=True)
e = s*d/(s+d)
B = e
H = h+B
a = d/(s+d)
vbar = s/(s+d)
w = v-vbar-a*u
F = u*(u/(m+u)-e-h*u+d*(v-u))
J = v*(s*(1-v)+d*(u-v))
assert simplify(F-u*(u/(m+u)-H*u+d*w)) == 0; checks += 1
assert simplify(J+(s+d)*v*w) == 0; checks += 1
assert simplify(J-a*F-(-(s+d)*v*w-a*F)) == 0; checks += 1
assert simplify((u/(m+u)-H*u).subs(m,1/H)+H*H*u*u/(1+H*u)) == 0; checks += 1
assert simplify(diff(F,v)-d*u)==0; checks += 1
assert simplify(diff(J,u)-d*v)==0; checks += 1
for sv, dv, hv in [(1, Rational(1,2), Rational(1,6)),
                   (1, Rational(2,3), Rational(1,2)),
                   (2, Rational(1,4), Rational(3,4)),
                   (Rational(3,2), Rational(1,5), Rational(2,3))]:
    b = sv*dv/(sv+dv)
    hh = hv+b
    aa = dv/(sv+dv)
    vv = sv/(sv+dv)
    for mv in (1/hh, 1/hh+Rational(1,2)):
        assert (1/mv-hh) <= 0; checks += 1
        assert simplify((u/(m+u)-H*u).subs({s:sv,d:dv,h:hv,m:mv})-
                        (u/(mv+u)-hh*u)) == 0; checks += 1
        assert simplify((-(s+d)*v*w-a*F).subs({s:sv,d:dv,h:hv,m:mv,v:vv+aa*u})+
                        aa*F.subs({s:sv,d:dv,h:hv,m:mv,v:vv+aa*u})) == 0; checks += 1

# Independent numerical integration illustrates the stated limits.
sv,dv,hv = 1.0,0.5,1.0/6
bb=sv*dv/(sv+dv); hh=hv+bb
for mv in (2.0,3.0):
    def rhs(t,y):
        uu,vv=y
        return [uu*(uu/(mv+uu)-bb-hv*uu+dv*(vv-uu)),
                vv*(sv*(1-vv)+dv*(uu-vv))]
    solution = solve_ivp(rhs,(0,100000),(0.8,0.3),method='BDF',
                         rtol=2e-11,atol=1e-13)
    assert solution.success; checks += 1
    uu,vv=solution.y[:,-1]
    ww=vv-sv/(sv+dv)-dv/(sv+dv)*uu
    assert 0<uu<0.1 and isfinite(vv); checks += 1
    if mv==2.0:
        assert abs(1e5*uu**2-2.0)<0.025; checks += 1
        assert abs(ww/uu**3-1.0/12.0)<0.001; checks += 1
    else:
        assert abs(1e5*uu-6.0)<0.01; checks += 1
        assert abs(ww/uu**2-1.0/18.0)<0.001; checks += 1
print(f'PASS: {checks} exact/symbolic and finite numerical assertions')
