#!/usr/bin/env python3
import sympy as sp
from itertools import product

print('SYMPY_VERSION', sp.__version__)

n=5
# Basis e1,...,e5, indexed 0,...,4. Nonzero products of pi_3.
PRODS={(0,0):{1:sp.Integer(1)},
       (0,1):{2:sp.Integer(1)},
       (1,0):{2:sp.Integer(1)},
       (0,3):{4:sp.Integer(1)},
       (3,3):{4:sp.Integer(1)}}
E=[sp.eye(n)[:,j] for j in range(n)]

def mul(u,v):
    out=sp.zeros(n,1)
    for i in range(n):
        for j in range(n):
            if u[i] != 0 and v[j] != 0 and (i,j) in PRODS:
                for k,c in PRODS[(i,j)].items():
                    out[k] += u[i]*v[j]*c
    return sp.simplify(out)

# 1. Reconstruct Der(pi_3) from the Leibniz rule, with exact rational arithmetic.
dvars=sp.symbols('d0:25')
D=sp.Matrix(5,5,dvars)
eqs=[]
for i,j in product(range(5), repeat=2):
    eqs += list(D*mul(E[i],E[j]) - mul(D*E[i],E[j]) - mul(E[i],D*E[j]))
C,_=sp.linear_eq_to_matrix(eqs,dvars)
der_basis=[sp.Matrix(5,5,list(v)) for v in C.nullspace()]
assert len(der_basis)==6
print('DERIVATION_SPACE_DIM', len(der_basis))

# 2. Necessary form of a local derivation from finitely many pointwise tests.
# If M is local then Mv lies in {Dv:D in Der(pi_3)} for every v.  It is
# enough for necessity to impose this on the ten vectors below.
witnesses=[
(0,0,0,0,1),
(0,0,0,1,-1),
(0,0,1,-1,-1),
(0,0,1,0,-1),
(0,0,1,0,0),
(0,1,-1,-1,-1),
(0,1,-1,0,-1),
(0,1,-1,0,0),
(1,-1,-1,-1,-1),
(1,-1,-1,0,-1),
]
mvars=sp.symbols('m0:25')
M=sp.Matrix(5,5,mvars)
constraints=[]
for tup in witnesses:
    v=sp.Matrix(tup)
    W=sp.Matrix.hstack(*[Di*v for Di in der_basis])
    for f in W.T.nullspace():
        constraints.append(sp.expand((f.T*M*v)[0]))
L,_=sp.linear_eq_to_matrix(constraints,mvars)
local_necessary_basis=L.nullspace()
assert len(local_necessary_basis)==7

# Expected seven-dimensional matrix space:
# [[x,0,0,0,0],[p,2x,0,0,0],[r,q,3x,s,0],[0,0,0,x,0],[t,0,0,u,2x]]
x,p,r,q,s,t,u=sp.symbols('x p r q s t u')
Expected=sp.Matrix([[x,0,0,0,0],
                    [p,2*x,0,0,0],
                    [r,q,3*x,s,0],
                    [0,0,0,x,0],
                    [t,0,0,u,2*x]])
expected_vectors=[]
for z in (x,p,r,q,s,t,u):
    expected_vectors.append(sp.Matrix(25,1,[sp.diff(entry,z) for entry in list(Expected)]))
N=sp.Matrix.hstack(*local_necessary_basis)
X=sp.Matrix.hstack(*expected_vectors)
assert N.rank()==7 and X.rank()==7 and sp.Matrix.hstack(N,X).rank()==7
print('LOCAL_NECESSARY_SPACE_DIM', N.rank())
print('LOCAL_NECESSARY_FORM_OK')
print('WITNESSES', witnesses)

# 3. Verify the one-parameter counterfamily Phi_tau is an algebra automorphism.
tau=sp.symbols('tau')
Phi=sp.Matrix([[-1,0,0,0,0],
               [0,1,0,0,0],
               [0,0,-1,tau,0],
               [0,0,0,-1,0],
               [0,0,0,0,1]])
assert sp.factor(Phi.det()) != 0
for i,j in product(range(5), repeat=2):
    assert sp.simplify(Phi*mul(E[i],E[j]) - mul(Phi*E[i],Phi*E[j])) == sp.zeros(5,1)
print('PHI_TAU_AUTOMORPHISM_OK')

# 4. Verify the relevant exponential block exactly.
z,ss,tt=sp.symbols('z ss tt', nonzero=True)
B=sp.Matrix([[3*z,ss],[0,z]])
Et=sp.Matrix([[sp.exp(3*z*tt), ss*(sp.exp(3*z*tt)-sp.exp(z*tt))/(2*z)],
              [0,sp.exp(z*tt)]])
assert sp.simplify(Et.subs(tt,0)-sp.eye(2))==sp.zeros(2)
assert sp.simplify(sp.diff(Et,tt)-B*Et)==sp.zeros(2)
print('EXPONENTIAL_BLOCK_FORMULA_OK')
# If a=e^z=-1 then the off-diagonal coefficient is ss*(a^3-a)/(2z)=0.
a=sp.symbols('a')
coefficient=ss*(a**3-a)/(2*z)
assert sp.simplify(coefficient.subs(a,-1))==0
print('MINUS_ONE_RESONANCE_B34_ZERO_OK')

# 5. The tau=0 boundary member is indeed an exponential of a genuine derivation.
D0=sp.diag(sp.I*sp.pi,2*sp.I*sp.pi,3*sp.I*sp.pi,sp.I*sp.pi,2*sp.I*sp.pi)
# Check Leibniz rule directly on basis products.
for i,j in product(range(5), repeat=2):
    assert sp.simplify(D0*mul(E[i],E[j]) - mul(D0*E[i],E[j]) - mul(E[i],D0*E[j])) == sp.zeros(5,1)
assert sp.simplify(D0.exp()-Phi.subs(tau,0))==sp.zeros(5)
print('TAU_ZERO_SHARP_BOUNDARY_OK')
print('CHECK_OK')
