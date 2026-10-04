from sympy import symbols, Matrix, diff, simplify, factor, sqrt

x,y,z,w,a,b = symbols("x y z w a b", positive=True)
f = Matrix([
    a*y + x*z,
    -b*x + y*z,
    1 - x**2 - y**2,
    z*(w-1),
])
vars_ = (x,y,z,w)
Q = b*x**2 + a*y**2

def L(expr):
    return simplify(sum(diff(expr, v)*f[i] for i,v in enumerate(vars_)))

qdot = factor(L(Q))
assert simplify(qdot - 2*z*Q) == 0

I = (w-1)**2/Q
assert simplify(L(I)) == 0

# Signed fiber ratio; multiplying by sqrt(Q) avoids any branch simplification issue.
R = (w-1)/sqrt(Q)
assert simplify(L(R)) == 0

J = f.jacobian(vars_)
expected = Matrix([
    [z,  a,   x, 0],
    [-b, z,   y, 0],
    [-2*x, -2*y, 0, 0],
    [0,  0, w-1, z],
])
assert J == expected

div3 = simplify(sum(diff(f[i], vars_[i]) for i in range(3)))
div4 = simplify(sum(diff(f[i], vars_[i]) for i in range(4)))
assert div3 == 2*z
assert div4 == 3*z

# The pure fourth-coordinate direction is invariant and evolves with scalar rate z.
ew = Matrix([0,0,0,1])
assert J*ew == z*ew

# The upper-right 3x1 block vanishes, so the quotient cocycle is the base Jacobian.
assert J[:3,3] == Matrix([0,0,0])

print("VERIFY_OK")
print("Qdot =", qdot)
print("L(I) =", simplify(L(I)))
print("div_base =", div3)
print("div_full =", div4)
print("J*e_w =", list(J*ew))
