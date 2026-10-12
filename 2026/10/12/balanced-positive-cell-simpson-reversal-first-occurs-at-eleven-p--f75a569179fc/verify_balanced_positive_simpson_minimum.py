#!/usr/bin/env python3
from fractions import Fraction


def enumerate_tables(m):
    # a,b: treatment/control totals in stratum 1.
    # x,y: adverse events in stratum 1.
    # u,v: adverse events in stratum 2.
    # Overall treatment and control totals are both m.
    total = 0
    rev = []
    for a in range(2, m-1):
        A2 = m-a
        if A2 < 2:
            continue
        for b in range(2, m-1):
            B2 = m-b
            if B2 < 2:
                continue
            for x in range(1, a):
                for y in range(1, b):
                    for u in range(1, A2):
                        for v in range(1, B2):
                            total += 1
                            if not (Fraction(x,a) < Fraction(y,b)):
                                continue
                            if not (Fraction(u,A2) < Fraction(v,B2)):
                                continue
                            if not (x+u > y+v):
                                continue
                            rev.append((a,b,x,y,u,v))
    return total, rev

expected_totals = {4:1,5:16,6:100,7:400,8:1225,9:3136,10:7056,11:14400}
expected_rev = {4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:4}
all_rev = {}
for m in range(4,12):
    total, rev = enumerate_tables(m)
    assert total == expected_totals[m], (m,total)
    assert len(rev) == expected_rev[m], (m,rev)
    all_rev[m] = rev

first = all_rev[11]
assert first == [
    (3,8,1,3,5,2),
    (4,7,1,2,5,3),
    (7,4,5,3,1,2),
    (8,3,5,2,1,3),
]

# Stratum exchange sends (a,b,x,y,u,v) to
# (m-a,m-b,u,v,x,y). The four labeled tables form two orbits.
def swap_strata(t,m=11):
    a,b,x,y,u,v=t
    return (m-a,m-b,u,v,x,y)

orbits=[]
unseen=set(first)
while unseen:
    t=min(unseen)
    orb={t,swap_strata(t)}
    unseen -= orb
    orbits.append(tuple(sorted(orb)))
assert len(orbits)==2

# Verify the two orbit representatives in full 2x2 form.
for t in [first[0], first[1]]:
    a,b,x,y,u,v=t
    A2=11-a; B2=11-b
    assert all(z>0 for z in [x,a-x,y,b-y,u,A2-u,v,B2-v])
    assert Fraction(x,a) < Fraction(y,b)
    assert Fraction(u,A2) < Fraction(v,B2)
    assert Fraction(x+u,11) == Fraction(6,11)
    assert Fraction(y+v,11) == Fraction(5,11)

# Association-sign robustness: for a 2x2 table, treatment adverse risk < control adverse risk
# iff the cross product x*(control non-event) - (treatment non-event)*y is negative.
def assoc_cross(events_t,total_t,events_c,total_c):
    return events_t*(total_c-events_c) - (total_t-events_t)*events_c
for t in first:
    a,b,x,y,u,v=t
    A2=11-a; B2=11-b
    assert assoc_cross(x,a,y,b) < 0
    assert assoc_cross(u,A2,v,B2) < 0
    assert assoc_cross(x+u,11,y+v,11) > 0

print('VERIFY_OK')
print('balanced_arm_sizes_checked', list(range(4,12)))
print('candidate_table_counts', expected_totals)
print('strict_reversal_counts', expected_rev)
print('first_layer_labeled', first)
print('first_layer_stratum_swap_orbits', orbits)
print('orbit_rep_1_rates', '1/3<3/8', '5/8<2/3', '6/11>5/11')
print('orbit_rep_2_rates', '1/4<2/7', '5/7<3/4', '6/11>5/11')
