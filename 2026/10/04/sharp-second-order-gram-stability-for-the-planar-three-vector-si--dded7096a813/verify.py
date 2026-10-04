import sympy as sp

x, y, z = sp.symbols("x y z", real=True)
a, b, c = x-sp.Rational(1,2), y-sp.Rational(1,2), z-sp.Rational(1,2)
G = sp.Matrix([[1,a,b],[a,1,c],[b,c,1]])
s = x+y+z
D2 = x*x+y*y+z*z
assert sp.expand(2*sp.det(G) - (3*s-D2-s*s+4*x*y*z)) == 0

# Four squared signed sums after the equilateral shift.
vals = [
    3+2*(a+b+c),
    3+2*(a-b-c),
    3+2*(-a+b-c),
    3+2*(-a-b+c),
]
expected = [2*s, 4+4*x-2*s, 4+4*y-2*s, 4+4*z-2*s]
assert all(sp.expand(v-w) == 0 for v,w in zip(vals, expected))

# Sharp symmetric family.
e = sp.symbols("e", positive=True)
theta = 2*sp.pi/3-e
xx = sp.cos(theta)+sp.Rational(1,2)
zz = sp.cos(2*theta)+sp.Rational(1,2)
Df2 = sp.expand_trig(2*xx**2+zz**2)
Mf = -2*zz
assert sp.series(Df2,e,0,5) == (sp.Rational(9,2)*e**2-sp.Rational(3,2)*sp.sqrt(3)*e**3-sp.Rational(27,8)*e**4+sp.Order(e**5))
assert sp.series(Mf,e,0,4) == (2*sp.sqrt(3)*e-2*e**2-sp.Rational(4,3)*sp.sqrt(3)*e**3+sp.Order(e**4))
D = sp.sqrt(Df2)
rem = sp.series(Mf-sp.sqrt(sp.Rational(8,3))*D+sp.Rational(2,9)*D**2,e,0,3)
assert rem == sp.Order(e**3)
print("VERIFY_OK")
