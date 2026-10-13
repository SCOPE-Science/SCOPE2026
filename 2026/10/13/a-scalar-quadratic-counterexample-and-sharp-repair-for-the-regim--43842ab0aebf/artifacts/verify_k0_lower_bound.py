from fractions import Fraction
import math

def k0_definition(lam, x, tau):
    g = lam*x
    xn = x - tau*g
    gn = lam*xn
    f = 0.5*lam*x*x
    fn = 0.5*lam*xn*xn
    D = (g+gn)**2 + 4*g*g
    return tau / math.sqrt(3.0 + 24.0*(fn-f)/(tau*D))

# Exact witness: f(x)=2x^2 means lambda=4.
lam = 4.0
x = 1.0
tau = 0.5
got = k0_definition(lam,x,tau)
exact = 1.0/(2.0*math.sqrt(3.0))
assert abs(got-exact) < 1e-15

xi = 4.0
Lambda1 = 4.0
L = 0.01
published = 2.0/math.sqrt(12.0*xi*L + 3.0*Lambda1)
assert got < published

# Strict inequality also by exact rational squares:
assert Fraction(1,12) < Fraction(25,78)

# Closed form on scalar quadratics.
for lam in (0.5,1.0,4.0,13.0):
    for z in (0.2,0.7,2.0,3.5,8.0):
        tau=z/lam
        direct=k0_definition(lam,1.3,tau)
        closed=math.sqrt((z-2.0)**2+4.0)/(lam*math.sqrt(3.0))
        assert abs(direct-closed) < 2e-13*max(1.0,abs(closed))

# The closed form is minimized at z=2, matching the corrected B^2 scale
# when B=lambda and the natural constant-Hessian Lipschitz constant is zero.
for lam in (0.5,1.0,4.0,13.0):
    sharp=2.0/(math.sqrt(3.0)*lam)
    at_two=math.sqrt(4.0)/(lam*math.sqrt(3.0))
    assert abs(sharp-at_two) < 1e-15
    for z in (0.01,0.2,1.0,1.9,2.0,2.1,5.0,20.0):
        val=math.sqrt((z-2.0)**2+4.0)/(lam*math.sqrt(3.0))
        assert val + 1e-15 >= sharp

print("VERIFY_OK")
