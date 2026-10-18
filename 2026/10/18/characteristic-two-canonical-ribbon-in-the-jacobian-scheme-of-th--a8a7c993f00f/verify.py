"""Exact checks for a Hankel-determinant hypersurface in characteristic two.
Run: python chordal_ribbon_verify.py; requires sympy.
Finite computations support, but do not replace, the accompanying symbolic proof.
"""
import sympy as s
from math import comb
from itertools import product

a,b,c,d,e,t,u,q,v=s.symbols('a b c d e t u q v')
F=s.det(s.Matrix([[a,b,c],[b,c,d],[c,d,e]]))
# Integer defining determinant identity and its five partial derivatives.
assert s.expand(F-(a*c*e+2*b*c*d-a*d*d-b*b*e-c**3))==0
partials={x:s.diff(F,x) for x in [a,b,c,d,e]}
expected=[c*e-d*d,2*(c*d-b*e),a*e+2*b*d-3*c*c,2*(b*c-a*d),a*c-b*b]
assert all(s.expand(partials[z]-expected[i])==0 for i,z in enumerate([a,b,c,d,e]))
# Modulo two, the three nonzero derivatives generate three quadrics.
assert all(s.Poly(partials[z],a,b,c,d,e,modulus=2).is_zero for z in [b,d])
J=[c*e+d*d,a*e+c*c,a*c+b*b]
assert all(s.Poly(partials[z]-J[i],a,b,c,d,e,modulus=2).is_zero for i,z in enumerate([a,c,e]))
assert s.Poly(F-(a*J[0]+c*J[1]+e*J[2]),a,b,c,d,e,modulus=2).is_zero
# First affine chart of singular scheme: c=b^2, e=b^4, (d+b^3)^2=0.
# Use symbolic reduction mod (u^2) for all defining equations.
for polynomial in J:
    P=s.expand(polynomial.subs({a:1,c:b**2,e:b**4,d:b**3+u},simultaneous=True))
    assert s.Poly(P,u,b,modulus=2).rem(s.Poly(u*u,u,b,modulus=2)).is_zero
# Reverse patch e=1: c=d^2, a=d^4, (b+d^3)^2=0.
for polynomial in J:
    P=s.expand(polynomial.subs({e:1,c:d**2,a:d**4,b:d**3+v},simultaneous=True))
    assert s.Poly(P,v,d,modulus=2).rem(s.Poly(v*v,v,d,modulus=2)).is_zero
# Overlap: q=(t^3+u)/t^4, v=t^-6*u, characteristic two.
# Clear denominators before testing cube (u^2=0).
# t^12*((t^3+u)/t^4)^3 = (t^3+u)^3;
# t^12*(t^-3 + u*t^-6) = t^9 + u*t^6
polynomial=s.expand((t**3+u)**3-(t**9+u*t**6))
assert s.Poly(polynomial,u,t,modulus=2).rem(s.Poly(u*u,u,t,modulus=2)).is_zero
# Hilbert function of (2,2,2) complete intersection in P4.
def h(m):
    return sum((-1)**j*comb(3,j)*comb(m-2*j+4,4)
               for j in range(4) if m>=2*j)
assert [(m,h(m)) for m in range(2,11)]==[(m,8*m-4) for m in range(2,11)]
# Deopurkar-Fedorchuk-Swinarski's genus-five quadrics, reduced mod 2.
q_ribbon=[b*b-a*c,d*d-c*e,c*c-2*b*d+a*e]
assert all(s.Poly(q_ribbon[i]-J[[2,0,1][i]],a,b,c,d,e,modulus=2).is_zero for i in range(3))
# Exhaustive projective-rational support checks over small prime fields.
def normalize(point,p):
    i=next(i for i,x in enumerate(point) if x%p)
    inv=pow(point[i],-1,p)
    return tuple((inv*x)%p for x in point)
def projective_points(p):
    for i in range(5):
        for tail in product(range(p),repeat=4-i):
            yield tuple([0]*i+[1]+list(tail))
for p in [2,3,5,7]:
    found=set()
    for point in projective_points(p):
        dct=dict(zip((a,b,c,d,e),point))
        if all(int(z.subs(dct))%p==0 for z in partials.values()) and int(F.subs(dct))%p==0:
            found.add(point)
    expected={normalize([1,t,t*t,t**3,t**4],p) for t in range(p)}
    expected.add((0,0,0,0,1))
    assert found==expected, (p,found,expected)
print('VERIFY_OK jacobian=3_quadrics charts=ribbon overlap=O(-6) genus=5 degree=8 finite_prime_support=[2,3,5,7]')
