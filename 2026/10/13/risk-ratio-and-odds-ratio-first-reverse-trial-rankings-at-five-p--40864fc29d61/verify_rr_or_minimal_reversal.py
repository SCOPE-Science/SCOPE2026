#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations

EXPECTED_TABLE_COUNTS = {2:0,3:1,4:3,5:6}
EXPECTED_STRICT_REVERSALS = {2:0,3:0,4:0,5:1}

def protective_tables(n):
    # Equal arm size n; a treatment events, b control events.
    # All four cells positive and treatment is protective: 1 <= a < b <= n-1.
    return [(a,b) for a in range(1,n) for b in range(a+1,n)]

def rr(n,t):
    a,b=t
    return Fraction(a,b)

def odds_ratio(n,t):
    a,b=t
    return Fraction(a*(n-b), b*(n-a))

def sign(x):
    return (x>0)-(x<0)

def reversal_direct(n,t,u):
    return (rr(n,t)-rr(n,u))*(odds_ratio(n,t)-odds_ratio(n,u)) < 0

def reversal_cross(n,t,u):
    a,b=t
    c,d=u
    # Numerators of RR(t)-RR(u) and OR(t)-OR(u); denominators are positive.
    r_num = a*d - b*c
    o_num = a*d*(n-b)*(n-c) - b*c*(n-a)*(n-d)
    return r_num*o_num < 0

def order_mismatch(n,t,u):
    return sign(rr(n,t)-rr(n,u)) != sign(odds_ratio(n,t)-odds_ratio(n,u))

for n in range(2,10):
    tables=protective_tables(n)
    assert len(tables) == (n-1)*(n-2)//2
    for t,u in combinations(tables,2):
        assert reversal_direct(n,t,u) == reversal_cross(n,t,u)

for n,v in EXPECTED_TABLE_COUNTS.items():
    assert len(protective_tables(n)) == v

reversal_sets={}
mismatch_sets={}
for n in range(2,10):
    rev=[]
    mis=[]
    for t,u in combinations(protective_tables(n),2):
        if reversal_direct(n,t,u):
            rev.append((t,u))
        if order_mismatch(n,t,u):
            mis.append((t,u))
    reversal_sets[n]=rev
    mismatch_sets[n]=mis

for n,v in EXPECTED_STRICT_REVERSALS.items():
    assert len(reversal_sets[n]) == v

# First weak-order difference: n=4, a strict RR ordering becomes an OR tie.
assert len(mismatch_sets[2])==0
assert len(mismatch_sets[3])==0
assert mismatch_sets[4] == [((1,2),(2,3))]
assert rr(4,(1,2)) == Fraction(1,2)
assert rr(4,(2,3)) == Fraction(2,3)
assert odds_ratio(4,(1,2)) == Fraction(1,3)
assert odds_ratio(4,(2,3)) == Fraction(1,3)

# First strict reversal: unique at n=5.
assert reversal_sets[5] == [((2,3),(3,4))]
assert rr(5,(2,3)) == Fraction(2,3)
assert rr(5,(3,4)) == Fraction(3,4)
assert odds_ratio(5,(2,3)) == Fraction(4,9)
assert odds_ratio(5,(3,4)) == Fraction(3,8)

# Exhaustive table of all six protective n=5 trials.
expected5 = {
    (1,2):(Fraction(1,2),Fraction(3,8)),
    (1,3):(Fraction(1,3),Fraction(1,6)),
    (1,4):(Fraction(1,4),Fraction(1,16)),
    (2,3):(Fraction(2,3),Fraction(4,9)),
    (2,4):(Fraction(1,2),Fraction(1,6)),
    (3,4):(Fraction(3,4),Fraction(3,8)),
}
for t,(r,o) in expected5.items():
    assert rr(5,t)==r and odds_ratio(5,t)==o

# Structural family for every equal arm size n >= 5.
# T_n=(n-3,n-2), U_n=(n-2,n-1).
for n in range(5,501):
    t=(n-3,n-2)
    u=(n-2,n-1)
    assert rr(n,t) < rr(n,u)
    assert odds_ratio(n,t) > odds_ratio(n,u)
    # Cross-multiplied OR gap equals n(n-4) > 0:
    a,b=t; c,d=u
    o_num = a*d*(n-b)*(n-c) - b*c*(n-a)*(n-d)
    assert o_num == n*(n-4)
    assert o_num > 0

# Harmful effects are reciprocal mirrors: swapping treatment and control in
# each trial inverts both RR and OR and preserves the existence of reversal.
for n in range(5,30):
    for t,u in reversal_sets.get(n, []):
        a,b=t; c,d=u
        rt,ru=rr(n,t),rr(n,u)
        ot,ou=odds_ratio(n,t),odds_ratio(n,u)
        assert (Fraction(1,rt)-Fraction(1,ru))*(Fraction(1,ot)-Fraction(1,ou)) < 0

print("VERIFY_OK")
print("table_counts_n2_to_n5", EXPECTED_TABLE_COUNTS)
print("strict_reversal_counts_n2_to_n5", EXPECTED_STRICT_REVERSALS)
print("first_weak_mismatch_n4", mismatch_sets[4])
print("first_strict_reversal_n5", reversal_sets[5])
print("witness_RR", rr(5,(2,3)), rr(5,(3,4)))
print("witness_OR", odds_ratio(5,(2,3)), odds_ratio(5,(3,4)))
print("family_checked_n_5_to_500")
