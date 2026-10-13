#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations_with_replacement, combinations

def gini(x):
    n=len(x); S=sum(x)
    assert n>=2 and S>0
    return Fraction(sum(abs(a-b) for a in x for b in x), 2*n*S)

def pietra(x):
    n=len(x); S=sum(x)
    assert n>=2 and S>0
    return sum(abs(Fraction(v,S)-Fraction(1,n)) for v in x)/2

def endpoint_form(x):
    assert len(x)==3
    a,b,c=sorted(map(Fraction,x)); S=a+b+c
    ell=Fraction(1,3)-a/S
    u=c/S-Fraction(1,3)
    assert ell>=0 and u>=0
    return ell,u,Fraction(2,3)*(ell+u),max(ell,u)

# Support two: exact identity G=P for arbitrary nonnegative rational pairs.
for a in range(0,31):
    for b in range(a,31):
        if a+b==0: continue
        x=(a,b)
        assert gini(x)==pietra(x)==Fraction(b-a,2*(a+b))

# Support three structural formulas.
for a in range(0,11):
    for b in range(a,11):
        for c in range(b,11):
            if a+b+c==0: continue
            ell,u,G,P=endpoint_form((a,b,c))
            assert gini((a,b,c))==G
            assert pietra((a,b,c))==P
            assert G>=P

A=(1,6,9)
B=(3,3,10)
assert sum(A)==sum(B)==16
assert gini(A)==Fraction(1,3)
assert pietra(A)==Fraction(13,48)
assert gini(B)==Fraction(7,24)
assert pietra(B)==Fraction(7,24)
assert gini(A)>gini(B)
assert pietra(A)<pietra(B)

# Optional finite check: among positive integer three-household profiles with a common
# total, no strict reversal occurs below total 16, and total 16 has the witness above.
for S in range(3,16):
    vals=[]
    for x in combinations_with_replacement(range(1,S+1),3):
        if sum(x)==S:
            vals.append((x,gini(x),pietra(x)))
    assert not any((p[1]-q[1])*(p[2]-q[2])<0 for p,q in combinations(vals,2))
vals=[]
for x in combinations_with_replacement(range(1,17),3):
    if sum(x)==16:
        vals.append((x,gini(x),pietra(x)))
rev=[(p,q) for p,q in combinations(vals,2) if (p[1]-q[1])*(p[2]-q[2])<0]
assert rev==[((A,Fraction(1,3),Fraction(13,48)),(B,Fraction(7,24),Fraction(7,24)))]

print('VERIFY_OK')
print('support_two_identity_G_equals_P')
print('support_three_endpoint_formula_checked')
print('witness_A', gini(A), pietra(A))
print('witness_B', gini(B), pietra(B))
print('positive_integer_common_total_first_reversal', 16)
