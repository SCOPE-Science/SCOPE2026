"""Symbolic algebra and numerical diagnostics for the 1:2 half-turn orbit classification."""
import math
import sympy as sp

A, b, eps, t, c, w = sp.symbols('a b epsilon t c w', real=True)
y = sp.symbols('y', real=True)
omega = A * (1-y*y) * (1-eps*y*y)
W = sp.diff(omega, y)
assert sp.factor(W + 2*A*y*(1+eps-2*eps*y*y)) == 0
assert sp.simplify(sp.expand(omega.subs(y,sp.sqrt(t))) - A*(1-t)*(1-eps*t)) == 0

# Jacobian of the kick-then-twist map. Here c=2*pi*b*cos(2*pi*x),
# w=omega'(y_next).
def J(cvalue, wvalue):
    return sp.Matrix([[1-cvalue*wvalue, wvalue], [-cvalue, 1]])
assert sp.simplify(J(c,w).det()-1)==0
P_const = J(-c,w)*J(c,w)
P_flip = J(-c,w)*J(c,-w)
assert sp.factor(sp.trace(P_const)-(2-c*c*w*w))==0
assert sp.factor(sp.trace(P_flip)-(2+c*c*w*w))==0
assert J(0,w)*J(0,-w)==sp.eye(2)
assert sp.simplify(sp.factor(2*sp.pi*t*((1+eps)-2*eps*t)/((1-t)*(1-eps*t))
                              -2*sp.pi*t*(1/(1-t)+eps/(1-eps*t))))==0

# epsilon=1 critical codimension-two coincidence.
t_c = 1/(4*sp.pi+1)
a_c = 1/(2*(1-t_c)**2)
assert sp.simplify(2*sp.pi*t_c*(2-2*t_c)/(1-t_c)**2 -1)==0
assert sp.simplify(a_c-(4*sp.pi+1)**2/(32*sp.pi**2))==0

# The numerically located 1/2-resonance collision in the 2023 study
# is consistent with the exact algebraic threshold (not a proof by data).
def central_root(aval, epsilon):
    disc=(1-epsilon)**2+2*epsilon/aval
    return math.sqrt(((1+epsilon)-math.sqrt(disc))/(2*epsilon))

def map_F(x,y,aval,bval,epsilon):
    y1=y-bval*math.sin(2*math.pi*x)
    return ((x+aval*(1-y1*y1)*(1-epsilon*y1*y1))%1),y1

def J_numeric(x, ynext, aval, bval, epsilon):
    cn=2*math.pi*bval*math.cos(2*math.pi*x)
    wn=-2*aval*ynext*(1+epsilon-2*epsilon*ynext*ynext)
    return sp.Matrix([[1-cn*wn,wn],[-cn,1]])

def check_pair(x0,y0,aval,bval,epsilon,expected_trace):
    x1,y1=map_F(x0,y0,aval,bval,epsilon)
    x2,y2=map_F(x1,y1,aval,bval,epsilon)
    assert abs(((x1-x0-.5+.5)%1)-.5)<1e-12
    assert min(abs(x2-x0),abs(x2-x0-1),abs(x2-x0+1))<1e-12
    assert abs(y2-y0)<1e-12
    P=J_numeric(x1,y2,aval,bval,epsilon)*J_numeric(x0,y1,aval,bval,epsilon)
    assert abs(float(sp.trace(P))-expected_trace)<1e-10
    assert abs(float(P.det())-1)<1e-10

# Example with both elliptic constant-height and hyperbolic reversing cycles.
for aval,epsilon,bval in [(.52,1.0,.75),(.515,.1,.46),(.6,1.0,.9),(.53,.1,.25)]:
    ystar=central_root(aval,epsilon)
    wstar=-2*aval*ystar*(1+epsilon-2*epsilon*ystar*ystar)
    cc=2*math.pi*bval*wstar
    for yy in (+ystar,-ystar):
        check_pair(0.0,yy,aval,bval,epsilon,2-cc*cc)
    if bval>2*ystar:
        theta=math.asin(2*ystar/bval)/(2*math.pi)
        for x in (theta,.5-theta):
            check_pair(x,ystar,aval,bval,epsilon,
                       2+(2*math.pi*wstar)**2*(bval*bval-4*ystar*ystar))
    print(f'a={aval:.5f} epsilon={epsilon:.5f} b={bval:.5f} '
          f'Y={ystar:.12f} b_collision={2*ystar:.12f} '
          f'trace_constant={2-cc*cc:.9f}')

Y2023=central_root(.515,.1)
assert abs(2*Y2023-.3259)<1e-4
print('2023 reported numerical threshold: 0.3259; algebraic threshold:',2*Y2023)
print('epsilon=1 crossover a:',float(a_c))
print('All symbolic and numerical diagnostics passed.')
