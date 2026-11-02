"""Exact polynomial identities for a characteristic-five genus-six cyclic triple cover.

Run: python verify_symbolic.py. Requires sympy.
The coefficient basis and semilinear twist are explained in RESULT.md.
"""
import sympy as S
x,a,b,z=S.symbols('x a b z')
def F(v):
    return S.Poly(S.expand(v),a,b,modulus=5).as_expr()
def Fa(v):
    return S.Poly(S.expand(v),a,modulus=5)
def equal(u,v):
    return F(u-v)==0
f=x**7+a*x**3+b*x+1
D=2*a**7-a**6*b**3-a**3*b**5+a**2*b-2*a*b**4+b**7-2
assert equal(S.resultant(f,S.diff(f,x),x),D)
fp=S.Poly(f,x)
f3=S.Poly(S.expand(f**3),x)
A=S.Matrix(4,2,lambda k,i:F(f3.coeff_monomial(x**(5*(k+1)-(i+1)))))
B=S.Matrix(2,4,lambda k,i:F(fp.coeff_monomial(x**(5*(k+1)-(i+1)))))
Aexpected=S.Matrix([[a*b,-2*a+b**3],[a**3-2*b**2,b],[-2,-2*a**2],[0,0]])
Bexpected=S.Matrix([[0,a,0,b],[0,0,1,0]])
assert all(equal(x,y) for x,y in zip(A,Aexpected))
assert all(equal(x,y) for x,y in zip(B,Bexpected))
P=(B.applyfunc(lambda x:F(x**5))*A).applyfunc(F)
Pexpected=S.Matrix([[a**8-2*a**5*b**2,a**5*b],[-2,-2*a**2]])
assert all(equal(x,y) for x,y in zip(P,Pexpected))
H=a**5-2*a**2*b**2-b
E=b**3-2*a-a**3*b
assert equal(P.det(),-2*a**5*H)
# Rank(A)=1 precisely at H=E=0. The following basis exhibits
# all intersections; all except the origin violate squarefreeness.
G=S.groebner([H,E],b,a,order='lex',modulus=5)
assert len(G.polys)==2
assert any(equal(u.as_expr(),b-2*a**12-2*a**5) for u in G.polys)
q=a**15-2*a**8-2*a
assert any(equal(u.as_expr(),q) for u in G.polys)
B_of_a=2*a**12+2*a**5
assert Fa(S.rem(S.Poly(D.subs(b,B_of_a),a,modulus=5),Fa(q)).as_expr()- (a**14-2*a**7-2)).is_zero
# On H with a != 0, P=(a^3*b,-2)^t(1,a^2), so the
# semilinear stable rank drops precisely when b=2*a^47.
assert equal(P[0,0]-a**3*b,a**3*H)
assert equal(P[0,1]-a**5*b,0)
R=1+2*z**13-2*z**6
Q=Fa(R.subs(z,a**7))
assert Fa(H.subs(b,2*a**47)-a**5*Q.as_expr()).is_zero
assert S.gcd(Q,Q.diff()).degree()==0
assert Q.degree()==91
Dspecial=Fa(D.subs(b,2*a**47))
assert S.gcd(Q,Dspecial).degree()==0
# Parameter H=0 is smooth: H_a = a*b^2, H_b=a^2*b-1 in F5.
assert equal(S.diff(H,a),a*b**2)
assert equal(S.diff(H,b),a**2*b-1)
# Hyperelliptic change of variables on H, Y=4a^2b+1.
assert equal((4*a*a*b+1)**2-(1+3*a**7),-3*a*a*H)
print('SYMBOLIC_GENUS6_OK: discriminant, Cartier blocks, semilinear stable ranks, 91 reduced smooth exceptional parameters')
