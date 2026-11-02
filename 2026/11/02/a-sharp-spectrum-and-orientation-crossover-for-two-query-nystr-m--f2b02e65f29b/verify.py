"""Exact-symbolic and deterministic-quadrature checks for a two-query trace-estimation comparison.

Run with Python 3.10+ and SymPy. All random sampling is avoided in the checker;
quadrature tests are independent of the closed-form moment derivation.
"""
import math
import sympy as sp


def equals_zero(expression):
    assert sp.simplify(sp.factor(expression)) == 0, sp.factor(expression)


a, b, c, x, y = sp.symbols('a b c x y', real=True)
A = sp.Matrix([[a, c], [c, b]])
u = sp.Matrix([x, y])
Au = A * u
den = (u.T * Au)[0]
R = A - Au * Au.T / den
J = sp.Matrix([-y, x])
certificate = (a * b - c ** 2) * J * J.T / den
for i in range(2):
    for j in range(2):
        equals_zero(R[i, j] - certificate[i, j])

t = sp.symbols('t', positive=True)
q = sp.symbols('q', real=True)  # q = sin^2(2 theta), 0 <= q <= 1
Jx = 1 / (t * (t + 1))
Jy = 1 / (t + 1)
Ixx = -sp.diff(Jx, t) / (2 * t)
Ixy = Jx - t ** 2 * Ixx
Iyy = Jy - t ** 2 * Ixy
equals_zero(Ixx - (2*t + 1)/(2*t**3*(t+1)**2))
equals_zero(Ixy - 1/(2*t*(t+1)**2))
equals_zero(Iyy - (t+2)/(2*(t+1)**2))

W = Ixy * (1-q) + (Ixx + Iyy - 2 * Ixy) * q / 4
nystrom_var = sp.factor(4 * t**4 * W)
hutch_var = (t**2-1)**2*q/2
expected_nystrom = (2*t**3/(t+1)**2
                    + t*(t-1)**2*(t*t+4*t+1)*q/(2*(t+1)**2))
expected_difference = (2*t**3/(t+1)**2
                       - (t-1)**2*(t*t+1)*(t*t+3*t+1)*q/(2*(t+1)**2))
equals_zero(nystrom_var-expected_nystrom)
equals_zero(nystrom_var-hutch_var-expected_difference)

Q = 4*t**3/((t-1)**2*(t*t+1)*(t*t+3*t+1))
Qprime = (-4*t*t*(t+1)*(3*t**4+2*t**3+2*t+3)
          /((t-1)**3*(t*t+1)**2*(t*t+3*t+1)**2))
equals_zero(sp.diff(Q, t)-Qprime)
assert sp.simplify(Q.subs(t,2)) == sp.Rational(32,55)
assert sp.simplify(nystrom_var.subs({t:2,q:1})) == sp.Rational(29,9)
assert sp.simplify(hutch_var.subs({t:2,q:1})) == sp.Rational(9,2)
assert sp.simplify(nystrom_var.subs({t:2,q:0})) == sp.Rational(16,9)
assert sp.simplify(hutch_var.subs({t:2,q:0})) == 0
assert sp.simplify(nystrom_var.subs(t,1)) == sp.Rational(1,2)
assert sp.simplify(hutch_var.subs(t,1)) == 0

# Simpson's rule on a full circle integrates the homogeneous angular expectations.
def quad_var(L, angle, count=16384):
    co, si = math.cos(angle), math.sin(angle)
    a11 = L*co*co+si*si
    a12 = (L-1)*co*si
    a22 = L*si*si+co*co
    def term(phi):
        v1, v2 = math.cos(phi), math.sin(phi)
        den = a11*v1*v1 + 2*a12*v1*v2 + a22*v2*v2
        off = a12-(a11*v1+a12*v2)*(a12*v1+a22*v2)/den
        return 4*off*off
    step = 2*math.pi/count
    total = term(0.0)+term(2*math.pi)
    for j in range(1,count):
        total += (4 if j%2 else 2)*term(j*step)
    return total*step/(3*2*math.pi)

checked = 0
for L in (1.0, 1.5, 2.0, 4.0, 9.0, 20.0, 100.0):
    tt = math.sqrt(L)
    for angle in (0.0, 0.11, 0.39, math.pi/4):
        qq = math.sin(2*angle)**2
        expected = float(nystrom_var.subs({t:tt,q:qq}))
        measured = quad_var(L,angle)
        assert abs(expected-measured) <= 2e-9 * max(1.0, expected), (L,angle,expected,measured)
        checked += 1

polynomial = (t-1)**2*(t*t+1)*(t*t+3*t+1)-4*t**3
critical = float(sp.nsolve(polynomial, 1.75))
assert 1.75293 < critical < 1.75294
assert 3.07276 < critical**2 < 3.07278
print(f'VERIFY_OK: symbolic identities=16, angular quadratures={checked}, critical_sqrt_ratio={critical:.12f}, critical_ratio={critical**2:.12f}, example_N=29/9_H=9/2')
