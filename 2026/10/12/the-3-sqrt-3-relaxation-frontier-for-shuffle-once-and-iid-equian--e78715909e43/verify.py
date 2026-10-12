"""Exact algebraic checks for an equiangular relaxed Kaczmarz rate theorem.

This script supplements, but does not replace, the analytic proof.
Requires SymPy (tested with the system-installed version).
"""
from itertools import permutations
from sympy import Matrix, Rational, Symbol, eye, sqrt, simplify, factor, trace, expand

eta = Symbol('eta', real=True)
u = (Matrix([1, 0]), Matrix([-Rational(1, 2), sqrt(3)/2]),
     Matrix([-Rational(1, 2), -sqrt(3)/2]))
assert simplify(sum((v*v.T for v in u), Matrix.zeros(2)) - Rational(3,2)*eye(2)) == Matrix.zeros(2)
P = [eye(2)-eta*v*v.T for v in u]
T=P[2]*P[1]*P[0]
a=1-eta+eta**2/2
tr=(eta-2)*(eta**2+8*eta-8)/8
d=-(eta-1)**3
assert simplify(trace(T)-tr)==0
assert simplify(T.det()-d)==0
assert simplify(tr**2-4*d-eta**4*(eta**2+12*eta-12)/64)==0
Q=7*eta**4-32*eta**3+84*eta**2-104*eta+52
assert factor((a**3+d)**2-tr**2*a**3) == factor(eta**4*(eta-2)**2*(eta**2-6*eta+6)*Q/512)
t=Symbol('t',real=True)
assert expand(Q.subs(eta,t+1)-t**2*(7*t**2-4*t+1)-(29*t**2-4*t+7))==0
# At the concrete overrelaxed witness, all six fixed orders have equal power norms.
v=Rational(3,2)
Ps=[x.subs(eta,v) for x in P]
T1=T.subs(eta,v)
for k in (1,2,3,4):
    norm1=simplify(trace((T1**k).T*(T1**k))/2)
    for perm in permutations(range(3)):
        A=eye(2)
        for j in perm: A=Ps[j]*A
        assert simplify(trace((A**k).T*(A**k))/2-norm1)==0
T2=T1**2
S2=simplify(trace(T2.T*T2)/2)
I2=simplify(a.subs(eta,v)**6)
assert S2==Rational(586697,8388608)
assert I2==Rational(15625,262144)
assert simplify(S2-I2)==Rational(86697,8388608)>0
print('VERIFY_OK exact polynomial, six-order invariance, and two-epoch witness')
