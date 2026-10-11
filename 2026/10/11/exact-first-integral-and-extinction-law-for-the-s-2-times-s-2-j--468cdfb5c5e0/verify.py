import sympy as sp

A,B = sp.symbols("A B", positive=True)
S,D,c,S0,t = sp.symbols("S D c S0 t", real=True)
A0,B0 = sp.symbols("A0 B0", positive=True)
tau,x = sp.symbols("tau x", real=True)

Ap = (B-2*A)/(3*A*B)
Bp = (A-2*B)/(3*A*B)
Sp = sp.simplify(Ap+Bp)
Dp = sp.simplify(Ap-Bp)

assert sp.simplify(Sp + (A+B)/(3*A*B)) == 0
assert sp.simplify(Dp + (A-B)/(A*B)) == 0
assert sp.simplify(Dp/Sp - 3*(A-B)/(A+B)) == 0

# Direct first-integral derivative along the vector field.
I = (A-B)/(A+B)**3
Idot = sp.simplify(sp.diff(I,A)*Ap + sp.diff(I,B)*Bp)
assert Idot == 0

As = S*(1+c*S**2)/2
Bs = S*(1-c*S**2)/2
P = sp.simplify(As*Bs)
assert P == S**2*(1-c**2*S**4)/4

Sdot = sp.simplify(-S/(3*P))
assert sp.simplify(Sdot + 4/(3*S*(1-c**2*S**4))) == 0

clock = sp.Rational(3,8)*(S0**2-S**2) - c**2*sp.Rational(1,8)*(S0**6-S**6)
assert sp.simplify(sp.diff(clock,S) - (-sp.Rational(3,4)*S*(1-c**2*S**4))) == 0

c0 = (A0-B0)/(A0+B0)**3
T = sp.simplify(sp.Rational(3,8)*(A0+B0)**2 - sp.Rational(1,8)*c0**2*(A0+B0)**6)
T_target = (A0**2+4*A0*B0+B0**2)/4
assert sp.simplify(T-T_target) == 0

delta = c*S**2
remaining = sp.Rational(3,8)*S**2 - c**2*sp.Rational(1,8)*S**6
assert sp.simplify(remaining - S**2*(3-delta**2)/8) == 0
assert sp.simplify(remaining.subs(S**2, sp.Symbol("d")/c) - sp.Symbol("d")*(3-sp.Symbol("d")**2)/(8*c)) == 0

# Inverse series x=S^2 as a function of tau from tau=3x/8-c^2 x^3/8.
a1,a2,a3 = sp.symbols("a1 a2 a3")
xser = a1*tau+a2*tau**2+a3*tau**3
expr = sp.expand(sp.Rational(3,8)*xser - c**2*sp.Rational(1,8)*xser**3 - tau)
sol = sp.solve([sp.expand(expr).coeff(tau,k) for k in (1,2,3)], [a1,a2,a3], dict=True)[0]
assert sol[a1] == sp.Rational(8,3)
assert sol[a2] == 0
assert sp.simplify(sol[a3] - sp.Rational(512,81)*c**2) == 0

# Diagonal consistency.
a = sp.symbols("a", positive=True)
assert sp.simplify(T_target.subs({A0:a,B0:a}) - sp.Rational(3,2)*a**2) == 0

print("VERIFY_OK")
print("first_integral=true")
print("exact_extinction_time=true")
print("anisotropy_clock=true")
print("extinction_series=true")
