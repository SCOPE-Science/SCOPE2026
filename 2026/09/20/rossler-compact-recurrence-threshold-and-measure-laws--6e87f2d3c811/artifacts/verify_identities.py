import sympy as sp

x, y, z = sp.symbols('x y z', real=True)
a, b, c, m = sp.symbols('a b c m', positive=True, real=True)

f = sp.Matrix([-y-z, x+a*y, b+z*(x-c)])
vars_ = sp.Matrix([x,y,z])

def L(g):
    return sp.expand(sum(sp.diff(g, v)*fv for v, fv in zip(vars_, f)))

E = (x**2+y**2)/2 + z
assert sp.simplify(L(E) - (a*y**2+b-c*z)) == 0
assert sp.simplify(L(x) - (-y-z)) == 0
assert sp.simplify(L(y) - (x+a*y)) == 0
assert sp.simplify(L((x**2+y**2)/2) - (a*y**2-x*z)) == 0
assert sp.simplify(L(y**2/2) - (x*y+a*y**2)) == 0

D = c**2-4*a*b
zminus = (c-sp.sqrt(D))/(2*a)
zplus = (c+sp.sqrt(D))/(2*a)
variance = (c*m-a*m**2-b)/a
assert sp.simplify(variance - (m-zminus)*(zplus-m)) == 0
assert sp.simplify((zplus-zminus)**2/4 - D/(4*a**2)) == 0

# The harmonic-mean defect follows after using b E(1/z)=c-a m.
E_inv_z = (c-a*m)/b
assert sp.simplify(m*E_inv_z - 1 - a*variance/b) == 0

print('sympy_version =', sp.__version__)
print('energy_balance_residual = 0')
print('mean_balance_factorization_residual = 0')
print('variance_gap_residual = 0')
print('harmonic_defect_residual = 0')
