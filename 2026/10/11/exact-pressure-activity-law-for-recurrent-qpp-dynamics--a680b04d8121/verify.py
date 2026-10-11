from sympy import symbols, diff, simplify, factor

x,y,z,h,delta,eta,Z = symbols('x y z h delta eta Z', positive=True)
f1 = (z-1)*y - delta*x
f2 = x
f3 = eta*(h-z-y**2*z)
vars_ = (x,y,z)
F = (f1,f2,f3)

def L(expr):
    return simplify(sum(diff(expr,v)*F[i] for i,v in enumerate(vars_)))

assert simplify(L(y**2/2) - x*y) == 0
assert simplify(L(x*y) - (x**2 + y**2*(z-1) - delta*x*y)) == 0
assert simplify(L(z) - eta*(h-z-y**2*z)) == 0
assert simplify(L(z).subs(eta,1) - (h-z-y**2*z)) == 0
assert simplify(L(z).subs(eta,1)) == h-z-y**2*z
assert simplify(L(z**0)) == 0

# Logarithmic pressure identity is checked algebraically via L(log z)=L(z)/z.
logz_dot = simplify(f3/z)
assert simplify(logz_dot - eta*(h/z-1-y**2)) == 0

# Algebra behind the reciprocal-pressure variance decomposition.
# Pointwise: 1/z - 1/Z + (z-Z)/Z**2 = (z-Z)**2/(z*Z**2).
assert factor(1/z - 1/Z + (z-Z)/Z**2 - (z-Z)**2/(z*Z**2)) == 0

# Elimination check. Let X=<x^2>, Y=<y^2>, R=<1/z>.
X,Y,R = symbols('X Y R')
expr = simplify((Z + Y - h).subs(Y,h*R-1) - (Z+h*R-(h+1)))
assert expr == 0

# Mean/variance decomposition of X.
D = symbols('D')  # D = <(z-Z)^2/z>
R_decomp = 1/Z + D/Z**2
X_decomp = simplify(Z + h*R_decomp - (h+1))
expected = simplify((Z-1)*(Z-h)/Z + h*D/Z**2)
assert simplify(X_decomp-expected) == 0

print('LY2_OVER_2 =', L(y**2/2))
print('LXY =', L(x*y))
print('LZ =', L(z))
print('LLOGZ =', logz_dot)
print('X_IDENTITY = Z + h*R - (h+1)')
print('X_DECOMPOSITION = (Z-1)*(Z-h)/Z + h*D/Z**2')
print('VERIFY_OK')
