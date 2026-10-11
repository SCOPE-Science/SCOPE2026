#!/usr/bin/env python3
import sympy as s

eps = s.symbols("eps")
a, b, c, d = s.symbols("a b c d")

M = s.Matrix([[a,b],[c,d]])
expr = s.expand((s.eye(2) + eps*M).det())
assert s.expand(expr).coeff(eps, 1) == a + d

# Gegenbauer C_l^1 recurrence:
# C_0=1, C_1=2x,
# (l+1)C_{l+1}=2(l+1)x C_l-(l+1)C_{l-1} for lambda=1,
# hence C_{l+1}=2x C_l-C_{l-1}.
x = s.symbols("x")
C = [s.Integer(1), 2*x]
for ell in range(1, 30):
    C.append(s.expand(2*x*C[-1] - C[-2]))

for ell, poly in enumerate(C):
    val0 = s.expand(poly).subs(x,0)
    if ell % 2:
        assert val0 == 0
    else:
        assert val0 == (-1)**(ell//2)
    assert s.expand(poly).subs(x,1) == ell + 1

# Planar support-area first variation for a generic finite Fourier test.
theta = s.symbols("theta", real=True)
A0,A1,B1,A2,B2,A3,B3 = s.symbols("A0 A1 B1 A2 B2 A3 B3", real=True)
f = (A0 + A1*s.cos(theta)+B1*s.sin(theta)
     + A2*s.cos(2*theta)+B2*s.sin(2*theta)
     + A3*s.cos(3*theta)+B3*s.sin(3*theta))
h = 1 + eps*f
area_integrand = s.expand(h**2 - s.diff(h,theta)**2)/2
lin = s.expand(area_integrand).coeff(eps,1)
lin_int = s.integrate(s.expand_trig(lin),(theta,0,2*s.pi))
assert s.simplify(lin_int - 2*s.pi*A0) == 0
assert s.simplify(lin_int - s.integrate(f,(theta,0,2*s.pi))) == 0

# Odd Fourier modes integrate to zero on a great circle.
for k in range(1,8,2):
    assert s.integrate(s.cos(k*theta),(theta,0,2*s.pi)) == 0
    assert s.integrate(s.sin(k*theta),(theta,0,2*s.pi)) == 0

print("VERIFY_OK")
print("determinant_linear_term =", a+d)
print("gegenbauer_regression_degrees =", len(C)-1)
print("planar_first_variation =", 2*s.pi*A0)
