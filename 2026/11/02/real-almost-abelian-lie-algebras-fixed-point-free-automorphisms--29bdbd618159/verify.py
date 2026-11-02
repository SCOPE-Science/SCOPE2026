#!/usr/bin/env python3
"""Exact finite-dimensional test instances for real almost-abelian Lie automorphisms.
The general classification is proved in RESULT.md; these tests do not certify all sizes.
"""
import sympy as sp
from itertools import product

I=sp.eye

def njordan(j):
    return sp.Matrix(j,j,lambda a,b: 1 if b==a+1 else 0)

def rot_jordan(j,omega=1):
    # A acting on C^j as multiplication by i*omega+nilpotent, realified
    M=sp.I*omega*I(j)+njordan(j)
    P=sp.re(M).applyfunc(sp.expand)
    Q=sp.im(M).applyfunc(sp.expand)
    return P.row_join(-Q).col_join(Q.row_join(P))

def complex_conj_sign(j):
    D=sp.diag(*[(-1)**k for k in range(j)])
    return sp.diag(D,-D)  # realification of D*conjugation

def swap_with_K(A,K):
    d=A.rows
    assert K*A == -A*K
    O=sp.zeros(d)
    AA=sp.diag(A,A)
    BB=O.row_join(-K).col_join(K.row_join(O))
    return AA,BB

def confirm(A,B,finite):
    d=A.rows
    assert A.det()!=0
    assert B*A == -A*B
    assert (B-I(d)).det()!=0
    # Affine extension v -> -v, V -> B is an automorphism, free of fixed points
    ph=sp.diag(sp.Integer(-1), *([1]*d))
    ph[1:,1:]=B
    assert (ph-I(d+1)).det()!=0
    if finite:
        assert B**2 == -I(d) and ph**4 == I(d+1) and ph**2 != I(d+1)
    return True

cases=0
# paired nonzero real spectra, including nontrivial Jordan chains
for j in range(1,5):
    P=2*I(j)+njordan(j)
    N=-2*I(j)+njordan(j)
    D=sp.diag(*[(-1)**k for k in range(j)])
    # D P = - N D, D^2 = I
    assert D*P == -N*D
    A=sp.diag(P,N)
    Z=sp.zeros(j)
    B=Z.row_join(-D).col_join(D.row_join(Z))
    confirm(A,B,True);cases+=1

# paired pure-imaginary real Jordan blocks: even number of each length
for j in range(1,5):
    for omega in (1,3):
        R=rot_jordan(j,omega)
        K=complex_conj_sign(j)
        A,B=swap_with_K(R,K)
        confirm(A,B,True);cases+=1

# single imaginary block: still has fpf automorphism of infinite order
for j in range(1,5):
    R=rot_jordan(j,2)
    K=complex_conj_sign(j)
    B=2*K
    confirm(R,B,False)
    assert B**2 != I(R.rows)
    cases+=1

# off-axis complex quartet, represented by real 2x2 blocks paired with negatives
for j in range(1,4):
    c=sp.Matrix([[2,-3],[3,2]])
    D=sp.diag(*[(-1)**t for t in range(j)])
    N=njordan(j)
    Plus=sp.kronecker_product(I(j),c)+sp.kronecker_product(N,I(2))
    Minus=sp.kronecker_product(I(j),-c)+sp.kronecker_product(N,I(2))
    K=sp.kronecker_product(D,I(2))
    assert K*Plus == -Minus*K
    z=sp.zeros(Plus.rows)
    A=sp.diag(Plus,Minus)
    B=z.row_join(-K).col_join(K.row_join(z))
    confirm(A,B,True);cases+=1

# An anti-complex map on a single 2D imaginary block has negative determinant.
# Finite order + fixed-point-free on even real dimension forces determinant +1.
a,b=sp.symbols('a b', real=True)
K=sp.Matrix([[a,b],[b,-a]])
R=sp.Matrix([[0,-1],[1,0]])
assert K*R==-R*K and sp.factor(K.det())==-(a*a+b*b)

print(f'VERIFY_OK exact_matrix_constructions={cases} parity_obstruction_symbolic=1')
