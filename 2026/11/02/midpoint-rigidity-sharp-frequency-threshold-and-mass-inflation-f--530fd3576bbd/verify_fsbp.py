"""Symbolic and numerical corroboration of a three-node trigonometric FSBP criterion.

Run: python verify_fsbp.py
Dependency: SymPy (for exact symbolic checks).
No floating-point experiment is used as a substitute for the proof.
"""
import math
import random
import sympy as sp

w = sp.symbols('w', positive=True, real=True)
s = sp.sin(w)
c = sp.cos(w)
V = sp.Matrix([[1, c, -s], [1, 1, 0], [1, c, s]])
Vp = sp.Matrix([[0, w*s, w*c], [0, 0, w], [0, -w*s, w*c]])
D = Vp * V.inv()
D_expected = w * sp.Matrix([
    [-(1+2*c)/(2*s), s/(1-c), -1/(2*s)],
    [-1/(2*s), 0, 1/(2*s)],
    [1/(2*s), -s/(1-c), (1+2*c)/(2*s)],
])
p_end = s / (w*(1+2*c))
p_mid = 2*(1+c)*p_end
P = sp.diag(p_end, p_mid, p_end)
B = sp.diag(-1, 0, 1)

checks=0

def check(condition, message):
    global checks
    if not condition:
        raise AssertionError(message)
    checks += 1


def zero(expression):
    return sp.trigsimp(sp.factor(sp.together(expression))) == 0

for i in range(3):
    for j in range(3):
        check(zero(D[i,j]-D_expected[i,j]), f'D formula {i},{j}')
        check(zero((P*D+D.T*P-B)[i,j]), f'SBP formula {i},{j}')
for i in range(3):
    for j in range(3):
        check(zero((D*V - Vp)[i,j]), f'collocation {i},{j}')
check(zero(sp.det(V)-2*s*(1-c)), 'sampling determinant')
M=2*p_end+p_mid
check(zero(M-2*(2+c)*s/(w*(1+2*c))), 'mass formula')
H=(2+c)*s-w*(1+2*c)
check(zero(sp.diff(H,w)-2*s*(w-s)), 'mass gap derivative')
check(sp.limit(p_end,w,0)==sp.Rational(1,3), 'Simpson endpoint limit')
check(sp.limit(p_mid,w,0)==sp.Rational(4,3), 'Simpson midpoint limit')
check(sp.limit((M-2)/w**4,w,0)==sp.Rational(2,45), 'small frequency mass defect')
wc=2*sp.pi/3
check(sp.limit((wc-w)*p_end,w,wc,dir='-') == 3/(4*sp.pi), 'endpoint blowup')
check(sp.limit((wc-w)*M,w,wc,dir='-') == 9/(4*sp.pi), 'mass blowup')
check(sp.trigsimp(M.subs(w,sp.pi/2)-8/sp.pi)==0, 'midpoint calibration')

# Off-center interior collocation forces a nonzero center diagonal.
a = sp.symbols('a', real=True)
cardinal = (sp.cos(w) - sp.cos(w*sp.Symbol('x'))) / (sp.cos(w) - sp.cos(w*a))
dcard = sp.diff(cardinal, sp.Symbol('x')).subs(sp.Symbol('x'),a)
check(zero(dcard - w*sp.sin(w*a)/(sp.cos(w)-sp.cos(w*a))), 'interior cardinal derivative')
check(zero(dcard.subs(a,0)), 'midpoint only allowed stationary cardinal')

rng = random.Random(20261026)
for k in range(180):
    xmid = rng.uniform(-0.999, 0.999)
    if abs(xmid) < 0.005:
        xmid += 0.02
    omega = rng.uniform(0.02, math.pi-0.01)
    diag = omega*math.sin(omega*xmid)/(math.cos(omega)-math.cos(omega*xmid))
    check(abs(diag)>1e-10, f'off-center SBP diagonal obstruction {k}')
for region in (0,1):
    for k in range(150):
        q = (0.001+(2*math.pi/3-0.003)*rng.random()) if region==0 else (2*math.pi/3+0.001 + (math.pi-2*math.pi/3-0.002)*rng.random())
        # Evaluable directly from the trigonometric formula.
        sw, cw = math.sin(q), math.cos(q)
        p0 = sw/(q*(1+2*cw))
        p1 = 2*(1+cw)*p0
        check((p0>0 and p1>0) if region==0 else (p0<0 and p1<0), f'positivity region {k}')
        if region == 0:
            check(2*p0+p1 > 2, f'constant integral defect {k}')
print(f'PASS: {checks} algebraic, boundary, and seeded finite checks.')
