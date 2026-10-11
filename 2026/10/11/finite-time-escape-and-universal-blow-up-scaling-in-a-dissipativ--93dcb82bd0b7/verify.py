"""Algebraic reproducer for the finite-time escape theorem.

Requires SymPy 1.14.0. The infinite-time invariant-set arguments
are in RESULT.md and are not replaced by this finite computation.
"""
import sympy as sp

x, y, z, a, b, c, d, eps = sp.symbols(
    "x y z a b c d eps", real=True
)
U, V = sp.symbols("U V", real=True)

rhs = {x: y, y: z, z: eps - a*x - b**2*y - c*z + d*sp.sinh(x)}

def derivative(expr):
    return sp.expand(sum(sp.diff(expr, variable)*rate
                         for variable, rate in rhs.items()))

scaled_y = y*sp.exp(-x/3)
scaled_z = z*sp.exp(-2*x/3)
back = {y: U*sp.exp(x/3), z: V*sp.exp(2*x/3)}
Yprime = derivative(scaled_y)/sp.exp(x/3)
Zprime = derivative(scaled_z)/sp.exp(x/3)
error = (-c*V*sp.exp(-x/3) - b**2*U*sp.exp(-2*x/3)
         + (eps-a*x)*sp.exp(-x) - d*sp.exp(-2*x)/2)
assert sp.simplify(Yprime.subs(back) - (V-U**2/3)) == 0
assert sp.simplify(
    (Zprime.subs(back) - (d/2 - 2*U*V/3 + error)).rewrite(sp.exp)
) == 0

h, eta = sp.symbols("h eta", positive=True)
k = h**2/3
assert sp.simplify((h**3).subs(h**3, sp.Rational(9, 4)*d)
                   - sp.Rational(9, 4)*d) == 0
# Lower/upper face signs, evaluated at the correct extrema.
y_low = sp.factor(k*(1-3*eta/2) - h**2*(1-eta)**2/3)
y_high = sp.factor(k*(1+3*eta/2) - h**2*(1+eta)**2/3)
z_low = sp.factor(d/2 * (1-(1+eta)*(1-3*eta/2)))
z_high = sp.factor(d/2 * (1-(1-eta)*(1+3*eta/2)))
assert sp.simplify(y_low - k*(eta/2-eta**2)) == 0
assert sp.simplify(y_high + k*(eta/2+eta**2)) == 0
assert sp.simplify(z_low - d/2*(eta/2+3*eta**2/2)) == 0
assert sp.simplify(z_high - d/2*(-eta/2+3*eta**2/2)) == 0

u, v, E = sp.symbols("u v E", real=True)
K = 2*h**2/9
uprime = v-2*h*u/3-u**2/3
vprime = -K*u-2*h*v/3-2*u*v/3+E
W = K*u**2+v**2
Wprime = sp.expand(2*K*u*uprime+2*v*vprime)
formula = sp.expand(-4*h*W/3-2*K*u**3/3-4*u*v**2/3+2*v*E)
assert sp.simplify(Wprime-formula) == 0
assert sp.simplify(27/(sp.Rational(9, 4)*d)-12/d) == 0
print("CHECK_OK")
