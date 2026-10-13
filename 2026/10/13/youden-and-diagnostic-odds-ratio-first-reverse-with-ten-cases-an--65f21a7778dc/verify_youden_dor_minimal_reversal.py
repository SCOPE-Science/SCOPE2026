#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations

EXPECTED_POSITIVE_TABLES = {2:0,3:1,4:3,5:6,6:10,7:15,8:21,9:28,10:36}
EXPECTED_REVERSALS = {2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:6}

def tests(m):
    # Balanced diagnostic study:
    # m diseased, m controls; every 2x2 cell positive.
    # A table is encoded by (TP,TN). Positive discrimination means J>0.
    return [(tp,tn) for tp in range(1,m) for tn in range(1,m) if tp+tn>m]

def youden(m,t):
    tp,tn=t
    return Fraction(tp,m)+Fraction(tn,m)-1

def dor(m,t):
    tp,tn=t
    fn=m-tp
    fp=m-tn
    return Fraction(tp*tn, fn*fp)

def direct_metrics(m,t):
    tp,tn=t
    fn=m-tp
    fp=m-tn
    sensitivity=Fraction(tp,tp+fn)
    specificity=Fraction(tn,tn+fp)
    J=sensitivity+specificity-1
    D=Fraction(tp*tn,fp*fn)
    return J,D

def reversal(m,a,b):
    Ja,Da=direct_metrics(m,a)
    Jb,Db=direct_metrics(m,b)
    return (Ja-Jb)*(Da-Db) < 0

def dor_extrema_at_sum(m,s):
    # For fixed s=TP+TN>m, DOR=p/(p-m(s-m)), p=TP*TN,
    # so it decreases with p.
    lo=(m-1, s-(m-1))  # minimum product -> maximum DOR
    a=s//2
    hi=(a,s-a)          # maximum product -> minimum DOR
    assert 1 <= lo[1] <= m-1
    return dor(m,lo), dor(m,hi), lo, hi

reversal_sets={}
for m in range(2,11):
    ts=tests(m)
    assert len(ts)==EXPECTED_POSITIVE_TABLES[m]
    for t in ts:
        J,D=direct_metrics(m,t)
        assert J==youden(m,t)
        assert D==dor(m,t)
        assert (J>0) == (D>1)
    rev=[]
    for a,b in combinations(ts,2):
        if reversal(m,a,b):
            rev.append((a,b))
    reversal_sets[m]=rev
    assert len(rev)==EXPECTED_REVERSALS[m], (m,rev)

# First strict layer.
assert reversal_sets[10] == [
    ((3,9),(6,7)),
    ((3,9),(7,6)),
    ((4,9),(7,7)),
    ((6,7),(9,3)),
    ((7,6),(9,3)),
    ((7,7),(9,4)),
]

A=(3,9)
B=(6,7)
assert youden(10,A)==Fraction(1,5)
assert youden(10,B)==Fraction(3,10)
assert dor(10,A)==Fraction(27,7)
assert dor(10,B)==Fraction(7,2)
assert youden(10,A)<youden(10,B)
assert dor(10,A)>dor(10,B)

# Check the extremal argument for every J-level through the boundary.
for m in range(3,11):
    for s in range(m+1,2*m-1):
        vals=[dor(m,t) for t in tests(m) if sum(t)==s]
        if not vals:
            continue
        mx,mn,lo,hi=dor_extrema_at_sum(m,s)
        assert mx==max(vals)
        assert mn==min(vals)
    mins=[]
    for s in range(m+1,2*m-1):
        vals=[dor(m,t) for t in tests(m) if sum(t)==s]
        if vals:
            mins.append((s,min(vals)))
    assert all(mins[i][1] < mins[i+1][1] for i in range(len(mins)-1))

# Structural family for every m>=10:
# A_m=(3,m-1) has J=2/m and DOR=3(m-1)/(m-3).
# B_m=(6,m-3) has J=3/m and DOR=2(m-3)/(m-6).
# DOR(A_m)>DOR(B_m) iff m(m-9)>0.
for m in range(10,501):
    A=(3,m-1)
    B=(6,m-3)
    assert all(1 <= x <= m-1 for x in A+B)
    assert youden(m,A)==Fraction(2,m)
    assert youden(m,B)==Fraction(3,m)
    assert dor(m,A)==Fraction(3*(m-1),m-3)
    assert dor(m,B)==Fraction(2*(m-3),m-6)
    assert youden(m,A)<youden(m,B)
    assert dor(m,A)>dor(m,B)

print("VERIFY_OK")
print("positive_table_counts", EXPECTED_POSITIVE_TABLES)
print("strict_reversal_counts", EXPECTED_REVERSALS)
print("first_strict_m", 10)
print("first_layer_pairs", reversal_sets[10])
print("witness_J", youden(10,(3,9)), youden(10,(6,7)))
print("witness_DOR", dor(10,(3,9)), dor(10,(6,7)))
print("family_checked_m_10_to_500")
