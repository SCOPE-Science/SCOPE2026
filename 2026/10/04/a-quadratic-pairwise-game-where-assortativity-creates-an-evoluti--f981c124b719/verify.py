from sympy import symbols, Rational, diff, simplify

x, y, r = symbols("x y r", real=True)
h = Rational(1, 2)
pi = -Rational(1, 2)*(x-h)**2 - (x-h)*(y-h) + 2*(y-h)**2

def payoff(a, b):
    return simplify(pi.subs({x: a, y: b}, simultaneous=True))

phi = simplify(r*payoff(y, y) + (1-r)*payoff(y, x) - payoff(x, x))
D = simplify(diff(phi, y).subs(y, x))
Dprime = simplify(diff(D, x))
Bstar = simplify(diff(phi, y, 2).subs({x: h, y: h}))
phistar = simplify(phi.subs(x, h))

assert simplify(D - (-2 + 3*r)*(x-h)) == 0
assert simplify(Dprime - (-2 + 3*r)) == 0
assert simplify(Bstar - (-1 + 2*r)) == 0
assert simplify(phistar - (2*r-1)*Rational(1,2)*(y-h)**2) == 0

# Exact representatives from the ESS and branching regimes.
r_ess = Rational(2, 5)
r_branch = Rational(3, 5)
assert Dprime.subs(r, r_ess) < 0 and Bstar.subs(r, r_ess) < 0
assert Dprime.subs(r, r_branch) < 0 and Bstar.subs(r, r_branch) > 0
print("VERIFY_OK")
