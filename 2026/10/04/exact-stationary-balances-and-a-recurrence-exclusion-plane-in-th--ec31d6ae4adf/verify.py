#!/usr/bin/env python3
import sympy as sp

x1,x2,y1,y2,z,a,b,c1,c2 = sp.symbols('x1 x2 y1 y2 z a b c1 c2', real=True)
vars_ = (x1,x2,y1,y2,z)
F = (
    a*(y1-x1),
    a*(y2-x2),
    (c1-a)*x1-c2*x2-z*x1+c1*y1-c2*y2,
    c2*x1+(c1-a)*x2-z*x2+c2*y1+c1*y2,
    x1*y1+x2*y2-b*z,
)

def L(f):
    return sp.expand(sum(sp.diff(f,v)*fv for v,fv in zip(vars_,F)))

def check(expr, name):
    if sp.expand(expr) != 0:
        raise AssertionError(name + ': ' + str(sp.expand(expr)))

s = x1**2+x2**2
R = x1*y1+x2*y2
I = x1*y2-x2*y1
speed2 = F[0]**2+F[1]**2
G = a*R-sp.Rational(1,2)*(a+c1)*s
V = s-2*a*z

check(L(s)-2*a*(R-s), 'Ls')
check(L(I)-((c1-a)*I+c2*(s+R)), 'LI')
check(L(G)-(speed2-a*c2*I+a*(2*c1-a-z)*s), 'LG')
check(L(V)-(-2*a*s+2*a*b*z), 'LV')

S,E,M,J = sp.symbols('S E M J', real=True)
eq_phase = (c1-a)*J+2*c2*S
eq_height = M-(2*c1-a)*S-E/a+c2*J
eliminated = sp.expand((c1-a)*eq_height-c2*eq_phase)
check(eliminated-((c1-a)*(M-(2*c1-a)*S-E/a)-2*c2**2*S), 'elimination')

omega = 2*a*c2/(a-28)
theta = 56-a-2*c2**2/(a-28)
height_from_law = sp.factor(theta+omega**2/a)
height_published = 56-a+2*(a+28)*c2**2/(a-28)**2
check(sp.together(height_from_law-height_published), 'rotating orbit specialization')

print('VERIFY_OK')
