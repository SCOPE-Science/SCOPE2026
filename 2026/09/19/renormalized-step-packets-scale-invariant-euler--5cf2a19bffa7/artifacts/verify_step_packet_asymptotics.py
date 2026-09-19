import math
import sympy as sp
from scipy.integrate import solve_ivp

# Symbolic checks for the one-step endpoint system.
a,b,c,th,R = sp.symbols('a b c th R', positive=True)
S = sp.sin(2*th)
C = sp.cos(2*th)
ap = -(c/(2*S))*sp.sin(2*a)*(sp.cos(2*(th-b))-sp.cos(2*(th-a)))
bp = (c/(2*S))*sp.sin(2*(th-b))*(sp.cos(2*b)-sp.cos(2*a))

# If a = R b^2, the outer endpoint has the expansion used in the proof.
uprime = sp.simplify(-bp/b**2)
u_series = sp.series(uprime.subs(a,R*b**2), b, 0, 3).removeO()
expected_u = c - 2*c*sp.cot(2*th)*b - c*(R**2 + sp.Rational(7,3))*b**2
assert sp.simplify(sp.expand_trig(u_series - expected_u)) == 0

# Exact derivative of log(tan(a)/tan(b)^2).
H = sp.simplify(2*ap/sp.sin(2*a) - 4*bp/sp.sin(2*b))
H_formula = (2*c*sp.sin(b-a)/sp.sin(2*b)) * (
    -sp.sin(b-a) + (sp.sin(2*(th-b))/S)*sp.sin(a+b)
)
# Numerical symbolic substitution avoids branch-sensitive trigonometric simplification.
for vals in [
    {a:sp.Rational(1,10), b:sp.Rational(3,10), c:sp.Rational(7,10), th:sp.Rational(3,5)},
    {a:sp.Rational(3,100), b:sp.Rational(1,5), c:sp.Rational(6,5), th:sp.Rational(39,50)},
]:
    assert abs(float((H-H_formula).subs(vals).evalf(40))) < 1e-30

# Numerical illustration for m=5, c=0.7, a(0)=0.12, b(0)=0.45.
m = 5
cv = 0.7
thv = math.pi/m
Sv = math.sin(2*thv)
kappa = 1/math.tan(2*thv)

def rhs(t,y):
    av,bv = y
    return [
        -(cv/(2*Sv))*math.sin(2*av)*(math.cos(2*(thv-bv))-math.cos(2*(thv-av))),
        (cv/(2*Sv))*math.sin(2*(thv-bv))*(math.cos(2*bv)-math.cos(2*av)),
    ]

T = 20000.0
sol = solve_ivp(rhs, (0.0,T), (0.12,0.45), rtol=1e-11, atol=1e-13,
                dense_output=True, max_step=10.0)
assert sol.success

print('symbolic_checks_passed=True')
print('m=5 c=0.7 a0=0.12 b0=0.45')
print('theory: c*t*b -> 1; t*c*(b-a) -> 1; t^2*int(sin(2theta)g)dtheta -> 1/c')
print('theory: a/b^2 -> positive constant; 1/b-c*t+2*cot(2*pi/m)*log(t) -> constant')
for t in [1000.0, 3000.0, 10000.0, 20000.0]:
    av,bv = sol.sol(t)
    sine_moment = cv*0.5*(math.cos(2*av)-math.cos(2*bv))
    corrected = 1/bv - cv*t + 2*kappa*math.log(t)
    print(f't={t:.0f} ctb={cv*t*bv:.12f} a_over_b2={av/bv**2:.12f} '
          f'corrected_denominator={corrected:.12f} mass_clock={t*cv*(bv-av):.12f} '
          f'sine_moment_clock={t*t*sine_moment:.12f}')
print('target_sine_moment_clock=',1/cv)
