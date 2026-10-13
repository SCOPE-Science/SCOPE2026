#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations

EXPECTED_TABLES={2:0,3:1,4:3,5:6,6:10}
EXPECTED_REVERSALS={2:0,3:0,4:0,5:0,6:2}

def tables(m):
    # t=treated adverse events, c=control adverse events.
    # Every 2x2 cell positive and treatment beneficial.
    return [(t,c) for c in range(2,m) for t in range(1,c)]

def arr(m,x):
    t,c=x
    return Fraction(c-t,m)

def rrr(m,x):
    t,c=x
    return Fraction(c-t,c)

def nnt(m,x):
    return 1/arr(m,x)

revs={}
for m in range(2,7):
    ts=tables(m)
    assert len(ts)==EXPECTED_TABLES[m]
    rv=[]
    for a,b in combinations(ts,2):
        # Larger ARR and RRR are better; lower NNT is exactly larger ARR.
        da=arr(m,a)-arr(m,b)
        dr=rrr(m,a)-rrr(m,b)
        if da*dr < 0:
            rv.append((a,b))
    revs[m]=rv
    assert len(rv)==EXPECTED_REVERSALS[m], (m,rv)

assert revs[6] == [((1,2),(3,5)), ((1,3),(2,5))]

X=(1,2)
Y=(3,5)
assert arr(6,X)==Fraction(1,6)
assert rrr(6,X)==Fraction(1,2)
assert nnt(6,X)==6
assert arr(6,Y)==Fraction(1,3)
assert rrr(6,Y)==Fraction(2,5)
assert nnt(6,Y)==3
assert arr(6,X)<arr(6,Y)
assert rrr(6,X)>rrr(6,Y)

# Persistent family for every m>=6:
# X_m=(t,c)=(1,2) and Y_m=(m-3,m-1).
for m in range(6,501):
    X=(1,2)
    Y=(m-3,m-1)
    assert all(1 <= t < c <= m-1 for t,c in (X,Y))
    assert arr(m,X)==Fraction(1,m)
    assert rrr(m,X)==Fraction(1,2)
    assert arr(m,Y)==Fraction(2,m)
    assert rrr(m,Y)==Fraction(2,m-1)
    assert arr(m,X)<arr(m,Y)
    assert rrr(m,X)>rrr(m,Y)

# Algebraic reversal criterion in (d,c), d=c-t:
# ARR ranking uses d, RRR ranking uses d/c.
for m in range(3,40):
    ts=tables(m)
    for a,b in combinations(ts,2):
        da=a[1]-a[0]; db=b[1]-b[0]
        lhs=(da-db)*(Fraction(da,a[1])-Fraction(db,b[1]))
        assert (lhs<0)==((arr(m,a)-arr(m,b))*(rrr(m,a)-rrr(m,b))<0)

print("VERIFY_OK")
print("table_counts",EXPECTED_TABLES)
print("reversal_counts",EXPECTED_REVERSALS)
print("first_layer",revs[6])
print("witness_X_ARR_RRR_NNT",arr(6,(1,2)),rrr(6,(1,2)),nnt(6,(1,2)))
print("witness_Y_ARR_RRR_NNT",arr(6,(3,5)),rrr(6,(3,5)),nnt(6,(3,5)))
print("family_checked_m_6_to_500")
