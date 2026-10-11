import sympy as sp

r, t = sp.symbols('r t', positive=True)
f_L = 2*r*sp.sin(t/2)
f_theta = 2*sp.asin(r*sp.sin(t/2))
assert sp.simplify(sp.diff(f_L,t,2) + r*sp.sin(t/2)/2) == 0
second_theta = -r*(1-r**2)*sp.sin(t/2)/(2*(1-r**2*sp.sin(t/2)**2)**sp.Rational(3,2))
assert sp.simplify(sp.diff(f_theta,t,2)-second_theta) == 0
assert sp.expand(sp.series(f_L,t,0,5).removeO()-(r*t-r*t**3/24)) == 0
assert sp.simplify(sp.series(f_theta,t,0,5).removeO()-(r*t-r*(1-r**2)*t**3/24)) == 0

# The tetrahedral dual pair: chord s=1, circle radius sqrt(3)/2,
# exposed minor arc central angle 2 asin(1/sqrt(3)).
rho = sp.sqrt(3)/2
phi = 2*sp.asin(1/sp.sqrt(3))
assert sp.simplify(2*rho*sp.sin(phi/2)-1) == 0
import math
rv = math.sqrt(3)/2
ph = 2*math.asin(1/math.sqrt(3))
funs = (lambda z: 2*rv*math.sin(z/2), lambda z: 2*math.asin(rv*math.sin(z/2)))
for fun in funs:
    delta2 = 2*fun(ph/2)-fun(ph)
    delta3 = 3*fun(ph/3)-fun(ph)
    assert 0 < delta2 < delta3
for m in (2,3,5,10,40):
    # A refinement is asymptotic to the circle's arc length.
    for fun in funs:
        assert m*fun(ph/m) < rv*ph
print('VERIFY_OK')
print('two_strict_second_derivatives=symbolic')
print('two_cubic_Taylor_coefficients=symbolic')
print('tetrahedral_equal_arc_gain=positive')
