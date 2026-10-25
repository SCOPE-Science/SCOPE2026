"""Exact sample checks of the cubic projection-center identity.

These finite examples supplement, and do not replace, the general proof.
Requires Python 3 and SymPy.
"""
import sympy as sp
from math import factorial

x,y,z,c,s=sp.symbols('x y z c s', real=True)
X=sp.Matrix([x,y,z]); vars=(x,y,z)

def circle_average_monomial(pc,ps):
    if pc%2 or ps%2:
        return sp.S.Zero
    a,b=pc//2,ps//2
    return sp.Rational(factorial(2*a)*factorial(2*b),4**(a+b)*factorial(a)*factorial(b)*factorial(a+b))

def average(poly):
    P=sp.Poly(sp.expand(poly),c,s)
    return sp.simplify(sum(coef*circle_average_monomial(*powers)
                           for powers,coef in P.terms()))

def centered_first_coefficient(poly,e,f):
    u=e*c+f*s
    sub={x:u[0],y:u[1],z:u[2]}
    v=sp.expand(poly.subs(sub, simultaneous=True))
    return sp.simplify(2*average(v*c))*e+sp.simplify(2*average(v*s))*f

def center_prediction(poly,n):
    g=sp.Matrix([sp.diff(poly,v) for v in vars])
    u={x:n[0],y:n[1],z:n[2]}
    v=g.subs(u, simultaneous=True)
    # Homogeneity gives n dot grad poly(n) = 3 poly(n).
    return sp.simplify(-sp.Rational(1,4)*(v-n*(n.dot(v))))

def identical(a,b):
    return all(sp.simplify(a[i]-b[i])==0 for i in range(3))

polys=[x*y*z,sp.Rational(1,2)*(5*z**3-3*z*(x*x+y*y+z*z)),
       x**3-3*x*y*y, z*(x*x-y*y),x*y*z+2*(x**3-3*x*y*y)]
planes=[(sp.Matrix([0,0,1]),sp.Matrix([1,0,0]),sp.Matrix([0,1,0])),
        (sp.Matrix([0,sp.Rational(3,5),sp.Rational(4,5)]),
         sp.Matrix([1,0,0]),sp.Matrix([0,sp.Rational(4,5),-sp.Rational(3,5)])),
        (sp.Matrix([sp.Rational(4,5),0,sp.Rational(3,5)]),
         sp.Matrix([0,1,0]),sp.Matrix([-sp.Rational(3,5),0,sp.Rational(4,5)]))]
count=0
for poly in polys:
    lap=sp.expand(sum(sp.diff(poly,v,2) for v in vars))
    assert lap==0, (poly,lap)
    for n,e,f in planes:
        assert n.dot(n)==e.dot(e)==f.dot(f)==1
        assert n.dot(e)==n.dot(f)==e.dot(f)==0
        observed=centered_first_coefficient(poly,e,f)
        predicted=center_prediction(poly,n)
        assert identical(observed,predicted),(poly,n,observed,predicted)
        count+=1

# In the coordinate cubic, the normal (0,1,1)/sqrt(2) has
# center displacement (-1/8, 0, 0) in the projected plane.
normal=sp.Matrix([0,sp.sqrt(2)/2,sp.sqrt(2)/2])
assert identical(center_prediction(x*y*z,normal),sp.Matrix([-sp.Rational(1,8),0,0]))

# Extend the spherical center drift homogeneously of degree zero.
# Its ambient divergence at the unit sphere equals intrinsic divergence.
r2=x*x+y*y+z*z
for poly in polys:
    tangential=sp.Matrix([sp.diff(poly,v)/r2-3*poly*v/r2**2 for v in vars])
    assert sp.simplify(X.dot(tangential)) == 0
    drift=-tangential/4
    div=sp.simplify(sum(sp.diff(drift[i],vars[i]) for i in range(3)))
    assert sp.simplify(div-3*poly/r2**2)==0,(poly,div)
print(f"PASS: {count} exact cubic/plane first-Fourier-center identities; harmonicity; 5 inverse-divergence identities; axial exact example")
