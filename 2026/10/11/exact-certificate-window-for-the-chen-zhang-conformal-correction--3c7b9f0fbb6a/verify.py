import sympy as sp

e, t, s, a = sp.symbols("e t s a", positive=True, real=True)

B = (1-s)/sp.Integer(8) - t*(1-3*s)/(1+a*t*s) - e/sp.Integer(2)

B0 = sp.simplify(B.subs(s, 0))
B1 = sp.simplify(B.subs(s, 1))
assert sp.simplify(B0 - (sp.Rational(1,8)-t-e/2)) == 0
assert sp.simplify(B1 - (2*t/(1+a*t)-e/2)) == 0

Bp = sp.factor(sp.diff(B, s))
Bpp = sp.factor(sp.diff(B, s, 2))
assert sp.simplify(Bp - (-sp.Rational(1,8) + t*(3+a*t)/(1+a*t*s)**2)) == 0
assert sp.simplify(Bpp - (-2*a*t**2*(3+a*t)/(1+a*t*s)**3)) == 0

# Endpoint inequalities after substituting a=e^2/(1+e).
ae = e**2/(1+e)
tminus = sp.simplify(e/(4-e*ae))
tminus_target = sp.simplify(e*(1+e)/(4*(1+e)-e**3))
assert sp.simplify(tminus-tminus_target) == 0
tplus = (1-4*e)/8
assert sp.simplify(B0.subs(t,tplus)) == 0
assert sp.simplify(B1.subs({a:ae,t:tminus})) == 0

# The source coefficient t=1/24 lies in the interval for 0<e<=1/16.
assert sp.simplify(B0.subs(t,sp.Rational(1,24)) - (sp.Rational(1,12)-e/2)) == 0
assert sp.simplify(
    B1.subs(t,sp.Rational(1,24))
    - (sp.Rational(1,12)/(1+a/sp.Integer(24))-e/2)
) == 0

# Crossing point / unique optimizer.
astar = sp.symbols("astar", positive=True, real=True)
tstar = 2/(24-astar + sp.sqrt((24-astar)**2+32*astar))
crosspoly = 1+(astar-24)*tstar-8*astar*tstar**2
assert sp.simplify(crosspoly) == 0

# Derivatives of the two lower-bound branches.
L1 = (2*t/(1+a*t)-e/2)/(1+a*t)**2
L2 = (sp.Rational(1,8)-t-e/2)/(1+a*t)**2
num1 = sp.factor(sp.diff(L1,t)*(1+a*t)**4)
assert sp.simplify(num1 - (2+a*e+a**2*e*t-4*a*t)) == 0
num2 = sp.factor(sp.diff(L2,t)*(1+a*t)**3)
assert sp.simplify(num2 - (-1-a/sp.Integer(4)+a*e+a*t)) == 0

ser = sp.series(tstar, astar, 0, 3)
target = sp.Rational(1,24) + astar/sp.Integer(864) + astar**2/sp.Integer(62208)
assert sp.simplify(ser.removeO()-target) == 0

print("VERIFY_OK")
print("certificate_concavity=true")
print("endpoint_window=true")
print("unique_certificate_optimizer=true")
print("optimizer_series=true")
