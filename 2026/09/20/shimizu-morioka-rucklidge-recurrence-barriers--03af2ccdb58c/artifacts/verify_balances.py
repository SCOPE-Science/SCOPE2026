import sympy as sp

x, y, z, a, b, rho = sp.symbols('x y z a b rho', real=True)
f = sp.Matrix([y, x*(rho-z)-a*y, x**2-b*z])

def lie(expr):
    return sp.expand(sp.diff(expr,x)*f[0] + sp.diff(expr,y)*f[1] + sp.diff(expr,z)*f[2])

A = x*y + a*x**2/2 + z**2/2 - rho*z
B = x**2*z + y**2 - rho*x**2 - b*z**2/2
rA = sp.factor(lie(A) - (y**2 - b*z*(z-rho)))
rB = sp.factor(lie(B) - ((x**2-b*z)**2 - 2*a*y**2))

m, v = sp.symbols('m v', real=True)
Ez2 = v + m**2
variance_gap = sp.factor((Ez2-rho*m) - (v-m*(rho-m)))

print("SymPy version:", sp.__version__)
print("dA residual:", rA)
print("dB residual:", rB)
print("variance rewrite residual:", variance_gap)
assert rA == 0
assert rB == 0
assert variance_gap == 0
