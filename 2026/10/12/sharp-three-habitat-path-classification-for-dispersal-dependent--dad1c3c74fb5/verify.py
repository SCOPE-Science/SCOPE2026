#!/usr/bin/env python3
"""Exact checks for the three-patch resource-relocation growth-ranking theorem.
Requires Python 3 and SymPy 1.10+; all mathematical identities are exact.
"""
import sympy as S

a,b,c,d,z=S.symbols('a b c d z',real=True)
L3=S.Matrix([[1,-1,0],[-1,2,-1],[0,-1,1]])

def F(x,y,w):
    H=S.diag(x,y,w)-d*L3
    return S.Poly((z*S.eye(3)-H).det(method='berkowitz'),z).as_expr()

fa=F(a,b,c)
fb=F(a,c,b)
assert S.simplify(fa-fb-d*(z-a)*(b-c))==0
assert S.simplify(fa.subs(z,a)-d*((a-b)*(a-c)+d*(2*a-b-c)))==0

# Exact characteristic identities for all 6 permutations of the example
rates=(S.Integer(6),S.Integer(5),S.Integer(1))
import itertools
polys={perm:S.factor(F(*perm)) for perm in itertools.permutations(rates)}
assert len(polys)==6
assert S.factor(F(5,6,1)-F(5,1,6))==5*d*(z-5)
assert S.factor(F(5,6,1).subs(z,5))==d*(-4+3*d)
assert S.factor(F(5,1,6).subs(z,5))==d*(-4+3*d)
assert S.factor(F(5,6,1).subs(d,S.Rational(4,3)).subs(z,5))==0
assert S.factor(F(5,1,6).subs(d,S.Rational(4,3)).subs(z,5))==0

# The crossing eigenvalue is the largest, not a lower eigenvalue:
for p in [(5,6,1),(5,1,6)]:
    H=S.diag(*p)-S.Rational(4,3)*L3
    assert (5*S.eye(3)-H).det()==0
    assert all(S.N(root)<5 for root in H.eigenvals() if root != S.Integer(5))

# Check the signs at rational rates via rational isolating intervals
# for all three real roots (finite rational certificates, no floating point).
for diff,sign in [(S.Integer(1),-1),(S.Integer(2),1)]:
    polys=[]
    for profile in [(5,6,1),(5,1,6)]:
        H=S.diag(*profile)-diff*L3
        f=S.Poly((z*S.eye(3)-H).det(),z)
        intervals=S.polys.polytools.intervals(f,eps=S.Rational(1,1000000))
        assert len(intervals)==3 and all(mul==1 for (_,mul) in intervals)
        polys.append(intervals[-1][0])
    (alo,ahi),(blo,bhi)=polys
    if sign<0: assert ahi < blo
    else: assert bhi < alo

# n=2: exact permutation invariance by conjugation with the swap matrix.
L2=S.Matrix([[1,-1],[-1,1]])
P=S.Matrix([[0,1],[1,0]])
assert S.simplify(P*(S.diag(a,b)-d*L2)*P-(S.diag(b,a)-d*L2))==S.zeros(2)

print('VERIFY_OK characteristic_swap=1 median_level=1 witness_threshold=4/3 '
      'six_profiles=6 exact_two_patch_symmetry=1 strict_witness_sides=2')
