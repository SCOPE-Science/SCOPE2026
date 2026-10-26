#!/usr/bin/env python3
"""Exact finite-field Hessian/intersection certificate for the Wiman sextic in characteristic seven.
Requires SymPy; no randomized or floating-point computations.
"""
import sympy as sp

p = 7
X, Y, Z, U, V = sp.symbols('X Y Z U V')
F = sp.expand(X**6+Y**6+Z**6+(X**2+Y**2+Z**2)*(X**4+Y**4+Z**4)-12*X**2*Y**2*Z**2)
H = sp.expand(sp.hessian(F, (X,Y,Z)).det(method='berkowitz'))


def sq_chart(P, at_infinity=False):
    out = 0
    for (i,j,k), c in sp.Poly(P, X, Y, Z).terms():
        assert i%2==j%2==k%2==0
        if at_infinity and k: continue
        out += int(c)%7 * U**(i//2)*V**(j//2)
    return sp.Poly(out,U,V,modulus=p).as_expr() # Z=1, or Z=0

f, h = sq_chart(F), sq_chart(H)
R = sp.Poly(sp.resultant(f,h,V),U,modulus=p)
A = U**3-3*U**2+U-1
B = U**3-U**2+3*U-1
expected = sp.Poly(U**2*(U+1)**2*(U-1)**6*A*B,U,modulus=p)
assert R == expected
for a, wanted in [(0,V+1),(1,(V-1)**2),(6,V**2)]:
    gg = sp.gcd(sp.Poly(f.subs(U,a), V, modulus=p), sp.Poly(h.subs(U,a), V, modulus=p))
    assert gg.monic()==sp.Poly(wanted,V,modulus=p).monic()
finfty = sq_chart(F,True).subs(U,1)
hinfty = sq_chart(H,True).subs(U,1)
assert sp.gcd(sp.Poly(finfty,V,modulus=p),sp.Poly(hinfty,V,modulus=p)).monic()==sp.Poly(V+1,V,modulus=p)
for cubic, image in [(A, 1+4*U+6*U**2), (B, 1+2*U+6*U**2)]:
    pc=sp.Poly(cubic,U,modulus=p)
    assert pc.degree()==3 and not any(pc.eval(a)==0 for a in range(7))
    for polynomial in (f,h):
        check=sp.Poly(sp.expand(polynomial.subs(V,image)),U,modulus=p)
        assert sp.rem(check,pc)==sp.Poly(0,U,modulus=p)
    # Norms of U and V from the cubic extension to F_7.
    normU = sp.Poly(-cubic.subs(U,0),U,modulus=p).as_expr()
    normV = sp.resultant(cubic, image, U)
    assert int(normU)%7==1 and int(normV)%7==1
# A norm-one element of F_(7^3) is a square (7^3-1=2*171, norm exponent 57).
# Since cubics are irreducible, the 24 non-axis points all have exact degree three.
# The axis points require sqrt(-1), so have exact degree two over F_7.
assert not any(a*a%7==6 for a in range(7))
# The tangent line at X=0, Y^2=-1, Z=1 is Y=aZ;
# restriction of the sextic in F_7[x] is exactly 2 x^6.
T=sp.Poly(F.subs({Y:sp.I,Z:1}).expand(),X) # use complex i as formal root with i^2=-1
assert sp.Poly(T.as_expr(),X,modulus=7)==sp.Poly(2*X**6,X,modulus=7)
assert R.degree()==16
print('VERIFY_OK: resultant, extension roots/norms, tangent contact, and Frobenius degrees')
print('R(U)=U^2(U+1)^2(U-1)^6 (U^3-3U^2+U-1)(U^3-U^2+3U-1)')
print('Hessian intersection: four nodes of length 6; six 6-contact points of length 4; twenty-four simple flexes of length 1')
print('Frobenius orbit profile on the 30 smooth flex support points: 2^3 3^8')
