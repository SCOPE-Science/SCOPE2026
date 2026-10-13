#!/usr/bin/env python3
from itertools import combinations
from fractions import Fraction
from math import prod, gcd

EXPECTED_FIRST_TOTAL = 13
EXPECTED_FIRST_PAIR = {((8,3,2),(6,6,1))}

def recursive_partitions_3(total, cap=None, prefix=()):
    if cap is None:
        cap = total
    if len(prefix) == 2:
        x = total
        if 1 <= x <= cap:
            yield prefix + (x,)
        return
    remaining_slots = 2 - len(prefix)
    for x in range(min(cap, total-remaining_slots), 0, -1):
        yield from recursive_partitions_3(total-x, x, prefix+(x,))

def loop_partitions_3(total):
    out=set()
    for a in range(1,total-1):
        for b in range(1,total-a):
            c=total-a-b
            out.add(tuple(sorted((a,b,c), reverse=True)))
    return out

def gini(x):
    n=len(x); S=sum(x)
    num=sum(abs(a-b) for i,a in enumerate(x) for b in x[i+1:])
    return Fraction(num, n*S)

def theil_order_key(x):
    # At fixed n and fixed total S,
    # T(x) = (1/S) * log(prod_i x_i^{x_i}) + log(n/S).
    # Hence the product is an exact order key.
    return prod(v**v for v in x)

def primitive_pair(a,b):
    g=0
    for x in a+b:
        g=gcd(g,x)
    return g==1

def strict_reversal(a,b):
    ga,gb=gini(a),gini(b)
    pa,pb=theil_order_key(a),theil_order_key(b)
    sg=(ga>gb)-(ga<gb)
    st=(pa>pb)-(pa<pb)
    return sg*st < 0

first=None
all_tables={}
for S in range(3,31):
    p1=set(recursive_partitions_3(S))
    p2=loop_partitions_3(S)
    assert p1==p2
    pairs=[]
    tie_splits=0
    for a,b in combinations(sorted(p1, reverse=True),2):
        ga,gb=gini(a),gini(b)
        pa,pb=theil_order_key(a),theil_order_key(b)
        sg=(ga>gb)-(ga<gb)
        st=(pa>pb)-(pa<pb)
        if sg*st < 0:
            pairs.append(tuple(sorted((a,b), reverse=True)))
        if sg != st and sg*st == 0:
            tie_splits += 1
    all_tables[S]=(len(p1),len(pairs),tie_splits)
    if pairs and first is None:
        first=(S,set(pairs))

assert first[0] == EXPECTED_FIRST_TOTAL
assert first[1] == EXPECTED_FIRST_PAIR
for S in range(3,13):
    assert all_tables[S][1] == 0

A=(8,3,2)
B=(6,6,1)
assert gini(A) == Fraction(4,13)
assert gini(B) == Fraction(10,39)
assert gini(A) > gini(B)
PA=theil_order_key(A)
PB=theil_order_key(B)
assert PA == 1811939328
assert PB == 2176782336
assert PA < PB
assert primitive_pair(A,B)

# Infinite family:
# A_x=(x+2,x-3,2), B_x=(x,x,1), x>=6.
# Gini compares ranges x vs x-1.
# Theil reversal reduces to:
# x^(2x) > 4 (x+2)^(x+2) (x-3)^(x-3).
# Check a long exact prefix; the analytic proof uses
# f'(x)=log(x^2/((x+2)(x-3)))>0 for x>3
# and the x=6 base case.
for x in range(6,501):
    A=(x+2,x-3,2)
    B=(x,x,1)
    assert sum(A)==sum(B)==2*x+1
    assert gini(A)>gini(B)
    assert theil_order_key(A)<theil_order_key(B)

# Exact base case for the monotonic log-ratio proof.
assert 6**12 > 4 * 8**8 * 3**3

print("VERIFY_OK")
print("first_total", first[0])
print("first_pair", sorted(first[1]))
print("gini_A_B", gini((8,3,2)), gini((6,6,1)))
print("theil_keys_A_B", PA, PB)
print("tables_3_to_13", {S:all_tables[S] for S in range(3,14)})
print("family_checked_x_6_to_500")
