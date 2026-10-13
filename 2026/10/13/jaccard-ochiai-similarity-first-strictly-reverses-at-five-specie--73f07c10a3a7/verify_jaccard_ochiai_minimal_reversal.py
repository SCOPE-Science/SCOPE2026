#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations

EXPECTED_SIGNATURE_COUNTS = {1:1,2:3,3:7,4:13,5:22}
EXPECTED_MISMATCH_COUNTS = {1:0,2:0,3:1,4:5,5:12}
EXPECTED_STRICT_REVERSALS = {1:0,2:0,3:0,4:0,5:1}

def signatures_by_counts(N):
    out=set()
    for a in range(1,N+1):
        for b in range(0,N-a+1):
            for c in range(b,N-a-b+1):
                if a+b+c <= N:
                    out.add((a,b,c))
    return out

def signatures_by_sets(N):
    # Independent construction from all nonempty subset pairs of an N-species universe.
    U=range(N)
    subs=[]
    for mask in range(1,1<<N):
        subs.append({i for i in U if mask>>i & 1})
    out=set()
    for X in subs:
        for Y in subs:
            a=len(X&Y)
            if a==0:
                continue
            b=len(X-Y); c=len(Y-X)
            if b>c: b,c=c,b
            out.add((a,b,c))
    return out

def J(s):
    a,b,c=s
    return Fraction(a,a+b+c)

def O2(s):
    # Squared Ochiai similarity; sqrt is strictly increasing.
    a,b,c=s
    return Fraction(a*a,(a+b)*(a+c))

def criterion_keys(s):
    a,b,c=s
    # J decreases with u; O^2 decreases with u+v.
    u=Fraction(b+c,a)
    v=Fraction(b*c,a*a)
    return u,u+v

def sign(x):
    return (x>0)-(x<0)

all_rev={}
for N in range(1,9):
    A=signatures_by_counts(N)
    B=signatures_by_sets(N)
    assert A==B
    if N<=5:
        assert len(A)==EXPECTED_SIGNATURE_COUNTS[N]
    rev=[]
    mism=[]
    for x,y in combinations(sorted(A),2):
        sj=sign(J(x)-J(y))
        so=sign(O2(x)-O2(y))
        u1,w1=criterion_keys(x); u2,w2=criterion_keys(y)
        # Both similarities are strictly decreasing in their exact keys.
        assert sj == -sign(u1-u2)
        assert so == -sign(w1-w2)
        if sj!=so:
            mism.append((x,y,sj,so))
        if sj*so<0:
            rev.append((x,y))
    all_rev[N]=rev
    if N<=5:
        assert len(mism)==EXPECTED_MISMATCH_COUNTS[N], (N,mism)
        assert len(rev)==EXPECTED_STRICT_REVERSALS[N], (N,rev)

# First weak-order split.
A=signatures_by_counts(3)
m3=[]
for x,y in combinations(sorted(A),2):
    if sign(J(x)-J(y)) != sign(O2(x)-O2(y)):
        m3.append((x,y))
assert m3 == [((1,0,2),(1,1,1))]
assert J((1,0,2)) == J((1,1,1)) == Fraction(1,3)
assert O2((1,0,2)) == Fraction(1,3)
assert O2((1,1,1)) == Fraction(1,4)

# Unique first strict reversal.
assert all_rev[5] == [((1,0,4),(1,1,2))]
P=(1,0,4); Q=(1,1,2)
assert J(P)==Fraction(1,5)
assert J(Q)==Fraction(1,4)
assert O2(P)==Fraction(1,5)
assert O2(Q)==Fraction(1,6)
assert O2(P)>O2(Q) and J(P)<J(Q)

# Structural family P_r=(1,0,r+2), Q_r=(1,1,r), r>=2.
for r in range(2,501):
    P=(1,0,r+2)
    Q=(1,1,r)
    assert J(P) < J(Q)
    assert O2(P) > O2(Q)
    assert J(Q)-J(P) == Fraction(1,(r+2)*(r+3))
    assert O2(P)-O2(Q) == Fraction(r-1,2*(r+1)*(r+3))

print("VERIFY_OK")
print("signature_counts", EXPECTED_SIGNATURE_COUNTS)
print("mismatch_counts", EXPECTED_MISMATCH_COUNTS)
print("strict_reversal_counts", EXPECTED_STRICT_REVERSALS)
print("first_weak_split", ((1,0,2),(1,1,1)))
print("first_strict_reversal", (P,Q))
print("boundary_values_J", Fraction(1,5), Fraction(1,4))
print("boundary_values_O2", Fraction(1,5), Fraction(1,6))
print("family_checked_r_2_to_500")
