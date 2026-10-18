"""Exact checks for the period-two theorem of a planar rational map.

Run with Python 3 and SymPy (see requirements.txt). Computation supports
but does not replace the parameter-uniform algebraic proof in RESULT.md.
"""
from fractions import Fraction
import sympy as s

checks = 0

def eq_zero(v, context):
    global checks
    checks += 1
    val = s.cancel(s.together(v))
    assert val == 0, f'{context}: {val}'

# Exact identity of the return derivative over the rational function field.
t, c, a = s.symbols('t c a', real=True)
M = s.Matrix([[-1, -8*t/(c*(1+t))], [c, 1]])
mu = (1-7*t)/(1+t)
for v in M*M-mu*s.eye(2):
    eq_zero(v, 'return scalar')
eq_zero(mu-(-7-16/a).subs(a, -2*(1+t)), 'parameter multiplier')
eq_zero(mu.subs(t,s.Rational(1,7)), 'superattracting')
eq_zero(mu.subs(t,s.Rational(1,3))+1, 'double -1')
eq_zero(s.diff(mu,t)+8/(1+t)**2, 'multiplier monotonicity')

# Independently check the full nonlinear map at an exact family of rational
# two-cycles, including both signs of c. No numerical tolerance is used.
x, y, aa, cc = s.symbols('x y aa cc')
F = s.Matrix([x*(1+aa/(1+y**2)), y+cc*x])
DF = F.jacobian((x,y))
for uu in [s.Rational(1,10),s.Rational(1,5),s.Rational(1,3),
           s.Rational(1,2),s.Rational(2,3),s.Rational(1),s.Rational(3)]:
    for cv in [s.Rational(1),s.Rational(-2),s.Rational(3,5),s.Rational(-7,3)]:
        av = -2*(1+uu**2)
        P = s.Matrix([-2*uu/cv,uu])
        Q = -P
        D = {aa:av, cc:cv}
        FP = F.subs({x:P[0],y:P[1],**D})
        FQ = F.subs({x:Q[0],y:Q[1],**D})
        for v in FP-Q: eq_zero(v, 'cycle forward')
        for v in FQ-P: eq_zero(v, 'cycle backward')
        JP = DF.subs({x:P[0],y:P[1],**D})
        JQ = DF.subs({x:Q[0],y:Q[1],**D})
        for v in JP-JQ: eq_zero(v, 'equal step derivatives')
        for v in JQ*JP-mu.subs(t,uu**2)*s.eye(2):
            eq_zero(v, 'two-step return')

# Compare the exact local contraction condition to its parameter window.
for num in range(201,401):
    av = -s.Rational(num,100)
    if av == -2: continue
    tv = -av/2-1
    if tv<=0: continue
    mv = mu.subs(t,tv)
    sink = abs(mv)<1
    eq = (-s.Rational(8,3) < av < -2)
    checks += 1
    assert sink == eq, (av,mv)

print(f'PASS: {checks} exact symbolic and rational checks')
