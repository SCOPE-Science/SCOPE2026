import sympy as sp

u, t, D, r = sp.symbols('u t D r')
d = u**2 - 1
A = sp.Integer(16)
B = 8*u*(9-u**2)
C = -27*d**2
Delta = sp.expand(B**2 - 4*A*C)

assert sp.factor(Delta - 64*(u**2 + 3)**3) == 0
assert sp.factor(Delta/(4*A) - (u**2 + 3)**3) == 0

modulus = sp.Poly(D**2 + 3, D)
def reduce_D(expr):
    return sp.rem(sp.Poly(sp.expand(expr), D), modulus).as_expr()

assert reduce_D((2*(u + D))**3 - (24*d*D - B)) == 0
assert reduce_D((2*(u - D))**3 - (-24*d*D - B)) == 0

ratio = sp.factor(Delta/(4*C))
cube_factor = (-(u**2 + 3)/3)**3
assert sp.factor(ratio/cube_factor - 16/d**2) == 0

# Two explicit rational sections on the original surface.
f = A*t**6 + B*t**3 + C
x1 = u**2 + 3
y1 = 4*t**3 + u*(9-u**2)
assert sp.factor(y1**2 - x1**3 - f) == 0

x2 = sp.Rational(9,4)*d**2/t**2 - 4*u*t
y2 = -4*t**3 + 9*u*d - sp.Rational(27,8)*d**3/t**3
assert sp.factor(sp.together(y2**2 - x2**3 - f)) == 0

# The residual E3 cube condition maps to the Mordell curve Y^2=X^3+16.
X = 4*r
Y = 4*u
assert sp.factor(Y**2 - X**3 - 16 - 16*(u**2 - 1 - 4*r**3)) == 0

print('sympy', sp.__version__)
print('discriminant identity: verified')
print('two Q(sqrt(-3)) cube identities: verified')
print('E3 cube-obstruction reduction: verified')
print('two displayed rational sections: verified')
print('Mordell-curve substitution identity: verified')
