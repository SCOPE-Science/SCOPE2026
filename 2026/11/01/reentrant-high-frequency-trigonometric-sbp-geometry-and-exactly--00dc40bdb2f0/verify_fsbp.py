#!/usr/bin/env python3
"""Independent algebraic and high-precision checks of the second-band three-node FSBP classification.

Requires SymPy and mpmath. This finite checker supplements the theorem's analytic proof.
Run: python verify_fsbp.py
"""
import math
import random
import sympy as sp
import mpmath as mp

mp.mp.dps = 65
checks = 0

# Symbolic identities modulo s**2+c**2=1.
k, s, c = sp.symbols('k s c', real=True, nonzero=True)
D0 = k * sp.Matrix([
    [-(1+2*c)/(2*s), s/(1-c), -1/(2*s)],
    [-1/(2*s), 0, 1/(2*s)],
    [1/(2*s), -s/(1-c), (1+2*c)/(2*s)]])
D1 = k * sp.Matrix([
    [(1-2*c)/(2*s), -s/(1+c), 1/(2*s)],
    [1/(2*s), 0, -1/(2*s)],
    [-1/(2*s), s/(1+c), (2*c-1)/(2*s)]])
B = sp.diag(-1, 0, 1)
for D, w, ratio in [(D0, s/(k*(1+2*c)), 2*(1+c)),
                     (D1, s/(k*(2*c-1)), 2*(1-c))]:
    P = sp.diag(w, ratio*w, w)
    error = P*D + D.T*P-B
    for x in error:
        z = sp.together(x).subs(s**2,1-c**2)
        assert sp.simplify(z)==0, (D,x,z)
        checks += 1

x = sp.symbols('x',real=True)
F0 = sp.Matrix([[1,sp.cos(k*xi),sp.sin(k*xi)] for xi in [-1,0,1]])
F0d = sp.Matrix([[0,-k*sp.sin(k*xi),k*sp.cos(k*xi)] for xi in [-1,0,1]])
# Check stated derivative forms via 65-digit unisolvent interpolation below.

def matrix_form(omega, variant):
    cc=mp.cos(omega); ss=mp.sin(omega)
    if variant=='mid':
        a=mp.mpf('0'); w=ss/(omega*(1+2*cc)); ratio=2*(1+cc)
        D=omega*mp.matrix([
            [-(1+2*cc)/(2*ss), ss/(1-cc), -1/(2*ss)],
            [-1/(2*ss),0,1/(2*ss)],
            [1/(2*ss),-ss/(1-cc),(1+2*cc)/(2*ss)]])
    else:
        a=mp.pi/omega*(1 if variant=='plus' else -1)
        w=ss/(omega*(2*cc-1)); ratio=2*(1-cc)
        D=omega*mp.matrix([
            [(1-2*cc)/(2*ss),-ss/(1+cc),1/(2*ss)],
            [1/(2*ss),0,-1/(2*ss)],
            [-1/(2*ss),ss/(1+cc),(2*cc-1)/(2*ss)]])
    return a, w, ratio, D

def collocation(omega,a):
    pts=[mp.mpf(-1),a,mp.mpf(1)]
    V=mp.matrix([[1,mp.cos(omega*t),mp.sin(omega*t)] for t in pts])
    Vd=mp.matrix([[0,-omega*mp.sin(omega*t),omega*mp.cos(omega*t)] for t in pts])
    return Vd*V**(-1)

# Test exact derivatives and SBP over all geometric branches, including signed P
# in inadmissible bands. Exclude narrow singular thresholds.
for wfloat in [3.2,3.45,3.7,3.98,4.08,4.3,4.65,4.9,5.04,5.19,5.32,5.65,6.01]:
    omega=mp.mpf(str(wfloat))
    for typ in ('mid','plus','minus'):
        a,w,ratio,D=matrix_form(omega,typ)
        direct=collocation(omega,a)
        assert max(abs(direct[i,j]-D[i,j]) for i in range(3) for j in range(3)) < mp.mpf('1e-56')
        checks +=9
        P=mp.diag([w,ratio*w,w]); BB=mp.diag([-1,0,1]); err=P*D+D.T*P-BB
        assert max(abs(err[i,j]) for i in range(3) for j in range(3))<mp.mpf('1e-55')
        checks +=9

# Positive-norm phase classification at a grid of subinterval points.
for i in range(1,150):
    omega=mp.pi + (mp.pi*i)/150
    for typ in ('mid','plus','minus'):
        _,w,ratio,_=matrix_form(omega,typ)
        positive=(w>0 and ratio*w>0)
        expected=(omega<4*mp.pi/3 if typ=='mid' else omega<5*mp.pi/3)
        assert positive==expected
        checks+=1

# Two rigorously characterized zero-mass-defect roots (bracketing and evaluation).
fm=lambda t: mp.sin(t)*(2+mp.cos(t))-t*(1+2*mp.cos(t))
fo=lambda t: mp.sin(t)*(2-mp.cos(t))-t*(2*mp.cos(t)-1)
r_m=mp.findroot(fm,(mp.mpf('4.0'),mp.mpf('4.1')))
r_o=mp.findroot(fo,(mp.mpf('5.0'),mp.mpf('5.1')))
assert mp.pi<r_m<4*mp.pi/3<r_o<5*mp.pi/3
for root, variant in ((r_m,'mid'),(r_o,'plus'),(r_o,'minus')):
    _,w,ratio,_=matrix_form(root,variant)
    assert abs(w*(2+ratio)-2)<mp.mpf('1e-56')
    checks+=1
assert abs(r_m-mp.mpf('4.02870132202536'))<mp.mpf('1e-13')
assert abs(r_o-mp.mpf('5.066777161070253'))<mp.mpf('1e-13')
checks+=2

# Verify the necessary interior-cardinal diagonal obstruction outside the three candidate nodes.
random.seed(90271)
for _ in range(150):
    omega=mp.pi+mp.pi*mp.mpf(random.uniform(0.01,0.98))
    a=mp.mpf(random.uniform(-0.9,0.9))
    if abs(mp.cos(omega)-mp.cos(omega*a))<mp.mpf('0.01'):
        continue
    diag=collocation(omega,a)[1,1]
    formula=omega*mp.sin(omega*a)/(mp.cos(omega)-mp.cos(omega*a))
    assert abs(diag-formula)<mp.mpf('1e-53')
    checks+=1

print('VERIFY_OK',checks)
print('CALIBRATED_MIDPOINT_FREQUENCY',mp.nstr(r_m,45))
print('CALIBRATED_OFFCENTER_FREQUENCY',mp.nstr(r_o,45))
print('CALIBRATED_OFFCENTER_POSITION',mp.nstr(mp.pi/r_o,45))
