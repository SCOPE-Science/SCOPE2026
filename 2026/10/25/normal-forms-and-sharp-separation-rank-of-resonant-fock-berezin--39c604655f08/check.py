"""Finite symbolic diagnostics for resonant Fock fixed-point normal forms.
This is supplementary evidence, not a replacement for the all-degree proof.
Requires sympy. Run: python check.py
"""
import sympy as sp
z,w,u,v,A,B=sp.symbols('z w u v A B', nonzero=True)
kappa=A*B
count=0
for degree in range(9):
    def Q(poly):
        return sp.expand(kappa*sum(sp.diff(poly,u,j+2) for j in range(degree+1)))
    poly=u**degree
    transformed=0
    for k in range(degree//2+1):
        transformed+=v**k*poly/sp.factorial(k)
        poly=Q(poly)
    R=sp.expand(transformed.subs({u:A*z-B*w,v:z/B}, simultaneous=True))
    D=sp.expand(sp.diff(R,z,w)+B*sp.diff(R,z)+A*sp.diff(R,w))
    assert sp.simplify(D)==0, degree
    matrix=sp.Matrix([[R.coeff(z,i).coeff(w,j) for j in range(degree+1)] for i in range(degree+1)])
    determinant=sp.factor(matrix.det())
    assert determinant!=0,degree
    expected=(A*B)**(degree*(degree+1)//2)
    for j in range(degree+1): expected*=sp.binomial(degree,j)
    assert sp.simplify(determinant/expected)==1,degree
    count+=2
print('PASS:',count,'symbolic identities (degrees 0 through 8)')
