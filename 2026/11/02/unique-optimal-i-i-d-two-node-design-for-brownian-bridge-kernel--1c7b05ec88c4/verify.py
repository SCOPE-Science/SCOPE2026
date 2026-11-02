"""Standalone algebraic and numerical checks for the two-node Brownian-bridge quadrature theorem.

Run: python verify.py
Requires Python 3.10+, sympy, mpmath.
This program checks specified identities; the all-measure optimality argument is analytic.
"""
import sympy as sp
import mpmath as mp

x, y, h, t = sp.symbols('x y h t', positive=True)
q = x*x+(1-x)**2

# A Brownian bridge on an interval of length h has integrated covariance h^3/12.
conditional = 2*sp.integrate(sp.integrate(x*(1-y/h), (x, 0, y)), (y, 0, h))
assert sp.simplify(conditional-h**3/12) == 0

# In the interior of the proposed support p=C/q^2, V'''=0 identically.
p = t/q**2
qprime = sp.diff(q,x)
pprime = sp.diff(p,x)
assert sp.simplify(6*(1-2*x)*p - 3*(qprime*p+q*pprime)) == 0

# The normalization equation after the change u=2x-1.
r = sp.symbols('r', positive=True)
u = sp.symbols('u', real=True)
normal_integral = sp.integrate((1+r*r)/(1+u*u)**2, (u, -r, r))
assert sp.simplify(normal_integral - (r+(1+r*r)*sp.atan(r))) == 0
assert sp.simplify(sp.diff(r+(1+r*r)*sp.atan(r), r)-(2+2*r*sp.atan(r))) == 0

# The expected cubic spacing sum for two iid uniform nodes is 3/10.
K_xy = x**3+(y-x)**3+(1-y)**3  # 0 <= x <= y <= 1
uniform_spacings = 2*sp.integrate(sp.integrate(K_xy, (x, 0, y)), (y, 0, 1))
assert sp.simplify(uniform_spacings-sp.Rational(3,10)) == 0

# For two arbitrary rational interior knots, the Gram-inverse formula agrees
# with the exact sum of the cubed gaps divided by 12.
def kernel(a,b): return min(a,b)-a*b
for i in range(1,10):
    for j in range(i+1,11):
        a,b=sp.Rational(i,12),sp.Rational(j,12)
        K=sp.Matrix([[kernel(a,a),kernel(a,b)], [kernel(b,a),kernel(b,b)]])
        m=sp.Matrix([a*(1-a)/2,b*(1-b)/2])
        var=sp.Rational(1,12)-(m.T*K.inv()*m)[0]
        gaps=(a**3+(b-a)**3+(1-b)**3)/12
        assert sp.simplify(var-gaps)==0

mp.mp.dps = 55
rstar = mp.findroot(lambda rr:rr+(1+rr**2)*mp.atan(rr)-1, (mp.mpf('.4'), mp.mpf('.5')))
a=(1-rstar)/2
b=1-a
C=(1+rstar*rstar)/2
opt_cost=3*a-mp.mpf('1.5')*a*a-mp.mpf('.5')
assert mp.mpf('0.2663306131046') < a < mp.mpf('0.2663306131048')
assert mp.mpf('0.1925938460989') < opt_cost < mp.mpf('0.1925938460991')
assert abs((rstar+(1+rstar*rstar)*mp.atan(rstar))-1) < mp.mpf('1e-50')

def density(z):
    return C/(z*z+(1-z)*(1-z))**2 if a <= z <= b else mp.mpf('0')

def pair_cost(z,w):
    lo,hi=min(z,w),max(z,w)
    return lo**3+(hi-lo)**3+(1-hi)**3

mass=mp.quad(density,[a,mp.mpf('.5'),b])
second_moment=mp.quad(lambda z:z*z*density(z),[a,mp.mpf('.5'),b])
assert abs(mass-1)<mp.mpf('1e-48')
assert abs(second_moment-a)<mp.mpf('1e-48')
for z in [mp.mpf('0'),a/2,a,(a+b)/2,b,1-a/2,mp.mpf('1')]:
    V=mp.quad(lambda w:pair_cost(z,w)*density(w),[a,mp.mpf('.5'),b])
    expected=opt_cost + mp.mpf('1.5')*(max(a-z,mp.mpf('0'),z-b)**2)
    assert abs(V-expected)<mp.mpf('1e-45'),(z,V,expected)

# A direct two-variable quadrature independently reproduces the optimal cost.
value=mp.quad(lambda z:density(z)*mp.quad(lambda w:density(w)*pair_cost(z,w),[a,z,b]),[a,b])
assert abs(value-opt_cost)<mp.mpf('1e-43')

print('PASS: bridge covariance, 45 exact rational Gram cases, density and potential identities')
print('r =', mp.nstr(rstar,25), 'a =', mp.nstr(a,25))
print('minimum expected squared quadrature error =', mp.nstr(opt_cost/12,25))
print('uniform iid expected squared quadrature error = 0.025')
print('relative reduction =', mp.nstr(1-opt_cost/mp.mpf('.3'),23))
