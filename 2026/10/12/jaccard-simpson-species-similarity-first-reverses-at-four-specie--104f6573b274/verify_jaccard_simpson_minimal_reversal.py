#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations

EXPECTED_COUNTS = {1:1, 2:4, 3:9, 4:17}
EXPECTED_REVERSALS = {1:0, 2:0, 3:0, 4:3}
EXPECTED_PAIRS = {
    tuple(sorted(((1,0,2),(2,1,1)), reverse=True)),
    tuple(sorted(((1,0,3),(1,1,1)), reverse=True)),
    tuple(sorted(((1,0,3),(2,1,1)), reverse=True)),
}

def signatures(N):
    # (a,b,c) with a=shared species, b/c unique species and b<=c
    out=[]
    for a in range(N+1):
        for b in range(N-a+1):
            for c in range(b, N-a-b+1):
                if a+b+c == 0:
                    continue
                # both sites nonempty
                if a+b == 0 or a+c == 0:
                    continue
                out.append((a,b,c))
    return out

def J(sig):
    a,b,c=sig
    return Fraction(a,a+b+c)

def S(sig):
    a,b,c=sig
    return Fraction(a,a+min(b,c))

def reverse_pair(p,q):
    return (J(p)-J(q))*(S(p)-S(q)) < 0

def criterion(p,q):
    a,b,c=p; A,B,C=q
    if a==0 or A==0:
        return False
    left1 = b*A - B*a
    left2 = (b+c)*A - (B+C)*a
    return left1*left2 < 0


tables={}
for N in range(1,9):
    sigs=signatures(N)
    if N in EXPECTED_COUNTS:
        assert len(sigs)==EXPECTED_COUNTS[N], (N,len(sigs))
    rev=set()
    for p,q in combinations(sigs,2):
        assert reverse_pair(p,q) == criterion(p,q), (N,p,q)
        if reverse_pair(p,q):
            rev.add(tuple(sorted((p,q), reverse=True)))
    tables[N]=rev
    if N in EXPECTED_REVERSALS:
        assert len(rev)==EXPECTED_REVERSALS[N], (N,rev)

assert tables[4] == EXPECTED_PAIRS

# Exact boundary values.
vals = {
    (1,0,2):(Fraction(1,3),Fraction(1,1)),
    (1,0,3):(Fraction(1,4),Fraction(1,1)),
    (1,1,1):(Fraction(1,3),Fraction(1,2)),
    (2,1,1):(Fraction(1,2),Fraction(2,3)),
}
for sig,(j,s) in vals.items():
    assert J(sig)==j and S(sig)==s

# A structural infinite family: nested vs balanced.
# P_r=(1,0,r), Q_r=(r,1,1), r>=2.
for r in range(2,501):
    p=(1,0,r)
    q=(r,1,1)
    assert S(p) > S(q)
    assert J(p) < J(q)
    assert J(q)-J(p) == Fraction(r*r-2, (r+2)*(r+1))

# Concrete four-species witnesses.
U={1,2,3,4}
A={1}; B={1,2,3}
C={1,2,3}; D={1,2,4}
assert len(A|B)==3 and len(C|D)==4
assert Fraction(len(A&B),len(A|B)) == Fraction(1,3)
assert Fraction(len(A&B),min(len(A),len(B))) == 1
assert Fraction(len(C&D),len(C|D)) == Fraction(1,2)
assert Fraction(len(C&D),min(len(C),len(D))) == Fraction(2,3)

print("VERIFY_OK")
print("signature_counts", EXPECTED_COUNTS)
print("reversal_counts", EXPECTED_REVERSALS)
print("boundary_pairs", sorted(EXPECTED_PAIRS))
print("boundary_values", {str(k):(str(J(k)),str(S(k))) for k in vals})
print("criterion_checked_all_signatures_union_le_8")
print("family_checked_r_2_to_500")
