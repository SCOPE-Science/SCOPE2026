"""Exact polynomial checks for the discriminant-completion freeness identity.

Run: python verify.py
The all-degree proof is algebraic and does not rely on the finite tests here.
"""
import sympy as sp

x,y,z = sp.symbols('x y z')
for d in (3,4,5):
    L = y**(d-2) + z**(d-2)
    Q = y**(d-1) + 2*z**(d-1)
    R = y**d + 3*y**(d-1)*z + 4*z**d
    F = sp.expand(x*x*L+x*Q+R)
    A = sp.diff(F,x)
    D = sp.expand(Q*Q-4*L*R)
    f = sp.expand(F*D)
    N = 3*d-2
    H = sp.expand(sp.diff(L,z)*sp.diff(F,y)-sp.diff(L,y)*sp.diff(F,z))
    T = sp.expand(2*(sp.diff(A,z)*sp.diff(F,y)-sp.diff(A,y)*sp.diff(F,z)))
    S1 = [sp.expand(x*A-N*F), y*A, z*A]
    S2 = [sp.expand(4*x*H-N*T), sp.expand(N*sp.diff(D,z)+4*y*H), sp.expand(-N*sp.diff(D,y)+4*z*H)]
    grad = [sp.diff(f,v) for v in (x,y,z)]
    zero = lambda p: sp.Poly(sp.expand(p),x,y,z).is_zero
    assert zero(D-(A*A-4*L*F))
    assert zero(sp.diff(D,z)*sp.diff(F,y)-sp.diff(D,y)*sp.diff(F,z)-(A*T-4*F*H))
    assert zero(sum(p*q for p,q in zip(S1,grad)))
    assert zero(sum(p*q for p,q in zip(S2,grad)))
    matrix = sp.Matrix([[x,y,z],S1,S2])
    assert zero(matrix.det(method='berkowitz')+N*N*(2*d-2)*f)
    print(f'd={d}: identities, syzygies and Saito determinant verified')
print('VERIFY_OK')
