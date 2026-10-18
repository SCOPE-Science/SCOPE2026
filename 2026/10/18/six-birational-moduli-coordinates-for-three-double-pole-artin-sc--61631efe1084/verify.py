#!/usr/bin/env python3
"""Exact polynomial identities for six birational invariants in characteristic three."""
import itertools
import sympy as sp

x = sp.Symbol('x')
q = [x-sp.Rational(1,2), sp.Rational(1,2)-1/x, -sp.Rational(1,2)-1/(x-1)]
# Both generators interchange two of the marked branch points.
for subs, mapping in [(1-x, (0,2,1)), (1/x, (1,0,2))]:
    for i in range(3):
        assert sp.cancel(q[i].subs(x,subs)+q[mapping[i]]) == 0

A=sp.symbols('A0:3')
B=sp.symbols('B0:3')
V=sp.Matrix([[1,A[i],A[i]**2] for i in range(3)])
Delta=sp.expand(V.det())
T=[]
for j in range(3):
    W=V.copy()
    W[:,j]=sp.Matrix(B)
    T.append(sp.expand(W.det()))
e1=sum(A)
e2=A[0]*A[1]+A[0]*A[2]+A[1]*A[2]
e3=A[0]*A[1]*A[2]
I=[e2,T[0],T[2],e1**2,e1*e3,e1*T[1]]
I=[sp.expand(z) for z in I]

def check(f):
    p=sp.Poly(sp.expand(f), *(A+B), modulus=3)
    return p.is_zero

for perm in itertools.permutations(range(3)):
    parity=sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3))%2
    sgn=-1 if parity else 1
    for scalar in (-1,1):
        subs={A[i]:scalar*A[perm[i]] for i in range(3)}
        subs.update({B[i]:scalar*sgn*B[perm[i]] for i in range(3)})
        for k,f in enumerate(I):
            assert check(f.xreplace(subs)-f), (perm,scalar,k)

# Cramer's rule: Delta times the interpolation coefficients are T.
formal_c=sp.symbols('c0:3')
b_from_c=[sum(formal_c[j]*V[i,j] for j in range(3)) for i in range(3)]
for j in range(3):
    lhs=sp.expand(T[j].xreplace({B[i]:b_from_c[i] for i in range(3)}))
    assert sp.expand(lhs-Delta*formal_c[j])==0

# Generic differential independence: the nonzero determinant confirms
# that the six invariants are algebraically independent and separable.
J=sp.Matrix([[sp.diff(z,t) for t in A+B] for z in I])
Jdet=sp.factor(J.det())
assert not check(Jdet)
print('VERIFY_OK marked_poles=3 symmetries=12 invariants=6 generic_jacobian_nonzero=True')
print('jacobian_det_factorization=',Jdet)
