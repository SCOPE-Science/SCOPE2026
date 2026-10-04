from fractions import Fraction
import itertools
import math
import sympy as sp

q=sp.symbols('q', positive=True)

# Gram inverse and objective identities for several symbolic dimensions.
for d in range(2,11):
    n=d+1
    I=sp.eye(n)
    J=sp.ones(n)
    G=(q-1)*I-q*J
    Gi=I/(q-1)-q*J/((q-1)*(d*q+1))
    assert sp.simplify(G*Gi-I)==sp.zeros(n)
    c=q/(d*q+1)
    # Hessian restricted to a support face with one zero coordinate is positive definite:
    # eigenvalues 2 and 2*(1-d*c)=2/(d*q+1).
    assert sp.simplify(1-d*c-1/(d*q+1))==0
    for k in range(1,d+1):
        F=sp.simplify(k-c*k*k)
        expected=sp.simplify(k*((d-k)*q+1)/(d*q+1))
        assert sp.simplify(F-expected)==0
        if k<d:
            Fnext=sp.simplify((k+1)-c*(k+1)*(k+1))
            diff=sp.simplify(Fnext-F)
            target=sp.simplify(((d-2*k-1)*q+1)/(d*q+1))
            assert sp.simplify(diff-target)==0

# Exact discrete maximizers for rational q>1 reproduce k=ceil(d/2).
for d in range(2,13):
    kstar=(d+1)//2
    for qv in (Fraction(6,5), Fraction(3,2), Fraction(2), Fraction(7,2)):
        vals=[]
        for k in range(1,d+1):
            vals.append((Fraction(k)*((d-k)*qv+1)/(d*qv+1),k))
        m=max(v for v,k in vals)
        ks=[k for v,k in vals if v==m]
        assert ks==[kstar], (d,qv,ks,kstar)

# Tetrahedral specialization agrees algebraically with Lassak's edge-supported construction.
# Write ell=2x and q=cosh(2x), hence cosh(x)^2=(q+1)/2.
M2=sp.simplify((q-1)*(3*q+1)/(2*(q+1)))
coshx2=(q+1)/2
cosh_mn=sp.simplify(q/coshx2)
sinh_mn2=sp.simplify(cosh_mn**2-1)
source_M2=sp.simplify(sinh_mn2*coshx2)
assert sp.factor(M2-source_M2)==0

# Euclidean small-edge limit coefficient squared.
for d in range(2,10):
    k=(d+1)//2
    coeff2=sp.Rational(d+1,2*k*(d-k+1))
    assert coeff2>0

print('VERIFY_OK regular hyperbolic simplex Lassak thickness')
