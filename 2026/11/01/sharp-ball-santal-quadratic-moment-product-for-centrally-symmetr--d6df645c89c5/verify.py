"""Exact proof-certificate replay for the polar quadratic-moment bound on symmetric hexagons.

Requires Python 3 and SymPy. Reconstructs both polygon moments from their vertices.
All polynomial identities and coefficient signs are checked in exact arithmetic.
"""
import sympy as sp

p, q = sp.symbols('p q', positive=True)
a = sp.Matrix([1, 0]); b = sp.Matrix([0, 1]); c = sp.Matrix([p, q])
vertices = [-a-b-c, a-b-c, a-b+c, a+b+c, -a+b+c, -a+b-c]

def cross(v, w):
    return sp.det(sp.Matrix.hstack(v, w))

def area_moments(V):
    area = 0; xx = yy = xy = 0
    for v, w in zip(V, V[1:] + V[:1]):
        d = cross(v, w)
        area += d / 2
        xx += d * (v[0]**2 + v[0]*w[0] + w[0]**2)/12
        yy += d * (v[1]**2 + v[1]*w[1] + w[1]**2)/12
        xy += d * (2*v[0]*v[1]+v[0]*w[1]+w[0]*v[1]+2*w[0]*w[1])/24
    return sp.factor(area),sp.Matrix([[sp.factor(xx),sp.factor(xy)],[sp.factor(xy),sp.factor(yy)]])

def polar_vertices(V):
    W=[]
    for v,w in zip(V,V[1:]+V[:1]):
        A=sp.Matrix([[v[0],v[1]],[w[0],w[1]]])
        W.append(A.inv()*sp.ones(2,1))
    return W

area_K, m_K = area_moments(vertices)
polar = polar_vertices(vertices)
area_P, m_P = area_moments(polar)
B = sp.factor(sp.trace(m_K*m_P))
assert sp.simplify(area_K-4*(1+p+q))==0
assert sp.simplify(area_P-2*(p*q+p+q)/((1+p)*(p+q)*(1+q)))==0
assert sp.simplify(B.subs({p:1,q:1})-sp.Rational(25,24))==0
assert sp.simplify(sp.limit(B,p,0)-sp.Rational(8,9))==0

x,y,z=sp.symbols('x y z',nonnegative=True)
e1=x+y+z; e2=x*y+x*z+y*z; e3=x*y*z
D=((x+y)*(y+z)*(z+x))**3
N=e1**3*e2**3-e1**3*e3**2-e1**2*e2**2*e3+e1*e2*e3**2-e2**3*e3-3*e3**3
assert sp.cancel(B.subs({p:y/x,q:z/x})-sp.Rational(8,9)*N/D)==0
Q=11*e1**3*e2**3+64*e1**3*e3**2-161*e1**2*e2**2*e3+161*e1*e2*e3**2+64*e2**3*e3+117*e3**3
assert sp.cancel(72*D*(sp.Rational(25,24)-sp.Rational(8,9)*N/D)-Q)==0
assert sp.simplify(Q.subs({x:1,y:1,z:1}))==0

U,V,W=sp.symbols('U V W',nonnegative=True)
C=sp.Poly(sp.expand(Q.subs({x:W+U+V,y:W+U,z:W})),U,V,W)
assert len(C.terms())==46
assert all(c>0 for mon,c in C.terms())
assert any(mon[0]>0 for mon,c in C.terms())
assert any(mon[1]>0 for mon,c in C.terms())
# A universal strict certificate for unequal x,y,z: Q has positive
# terms proportional to W**7*(U**2+U*V+V**2).
assert C.coeff_monomial(U**2*W**7)==1024
assert C.coeff_monomial(U*V*W**7)==1024
assert C.coeff_monomial(V**2*W**7)==1024

# Exact lower endpoint: positive-coefficient polynomial in p,q.
lower=sp.factor(B-sp.Rational(8,9))
H=sp.factor(lower*9*(1+p)**3*(p+q)**3*(1+q)**3/(8*p*q))
Hpoly=sp.Poly(H,p,q)
assert len(Hpoly.terms())==19
assert all(c>0 for mon,c in Hpoly.terms())

# Independently evaluate finite rational values via the matrix integrals.
for pp in [sp.Rational(1,5),sp.Rational(1,2),sp.Integer(1),sp.Rational(5,2),sp.Integer(4)]:
    for qq in [sp.Rational(1,4),sp.Rational(3,5),sp.Integer(1),sp.Integer(3)]:
        v=sp.factor(B.subs({p:pp,q:qq}))
        assert sp.Rational(8,9)<v<=sp.Rational(25,24)
        assert (v==sp.Rational(25,24))==(pp==1 and qq==1)

print('PASS: exact facet geometry, polar moments, identity, 46 coefficient signs, strict equality, 19 lower-bound coefficients, and 20 rational samples')
print('affine-regular value =',B.subs({p:1,q:1}))
