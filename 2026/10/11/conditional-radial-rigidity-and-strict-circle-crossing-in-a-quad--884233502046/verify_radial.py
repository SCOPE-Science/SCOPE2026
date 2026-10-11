"""Exact algebraic checks for the circular-equilibrium radial identities.

Requires SymPy. This code verifies polynomial identities and substitutions,
not the measure-theoretic arguments supplied in RESULT.md.
"""
import sympy as s

x, y, z = s.symbols("x y z", real=True)
a, b, c, d, r = s.symbols("a b c d r", real=True, nonzero=True)
flow = (a*z, z*(b*x+c*z**2), x**2+y**2-r**2+d*x*z)
rho2 = x**2+y**2
phi = z-d*x**2/(2*a)
psi = x*z-d*x**3/(3*a)


def lie(q):
    return s.expand(sum(s.diff(q, u)*v for u,v in zip((x,y,z),flow)))


assert s.cancel(lie(phi)-(rho2-r**2)) == 0
assert s.cancel(lie(psi)-(a*z**2+x*(rho2-r**2))) == 0
source = {a:-s.Rational(1,10), b:3, c:-s.Rational(11,5),
          d:-s.Rational(1,10), r:1}
assert s.simplify(phi.subs(source)-(z-x**2/s.Integer(2))) == 0
assert s.simplify(psi.subs(source)-(x*z-x**3/s.Integer(3))) == 0

# Nonvacuous periodic witness: on y=0 at a=-1,b=c=d=0,r=1.
witness = {a:-1,b:0,c:0,d:0,r:1,y:0}
assert s.simplify(flow[0].subs(witness)+z) == 0
assert s.simplify(flow[1].subs(witness)) == 0
assert s.simplify(flow[2].subs(witness)-(x**2-1)) == 0
H = z**2/2+x**3/3-x
LH = s.diff(H,x)*(-z)+s.diff(H,z)*(x**2-1)
assert s.expand(LH) == 0
assert s.diff(H,x).subs({x:1,z:0}) == 0
assert s.diff(H,x,2).subs({x:1,z:0}) == 2
assert H.subs({x:1,z:0}) == -s.Rational(2,3)
assert H.subs({x:-1,z:0}) == s.Rational(2,3)
print("VERIFY_OK")
