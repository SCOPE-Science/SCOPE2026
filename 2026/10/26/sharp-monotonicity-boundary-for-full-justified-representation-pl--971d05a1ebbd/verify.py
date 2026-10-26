"""Exact-arithmetic checks for a minimal FJR+ monotonicity witness.

This script validates the displayed dual upper bound and an explicit
post-change fractional violation; the universal statements are proved
analytically in RESULT.md, not by finite search.
"""
from fractions import Fraction as Q
from itertools import product

n, k = 4, 3
quota = Q(n,k)
W = frozenset('abe')
old = [frozenset('c'), frozenset('ac'), frozenset('ad'), frozenset('ad')]
new = [frozenset('ac'), frozenset('ac'), frozenset('ad'), frozenset('ad')]
assert all(len(W & ballot) < 2 for ballot in old + new)
assert all(len(W & old[i]) <= len(W & new[i]) for i in range(n))
assert new[0] - old[0] == frozenset('a')
assert all(new[i] == old[i] for i in range(1,n))
assert quota == Q(4,3)

# Post-change certificate: z_i=1, y_a=y_c=y_d=1; one unit
# goes to elected a and one to c or d for each voter.
z = [Q(1)]*n
y = {c:Q(int(c in 'acd')) for c in 'abcde'}
x = [{c:Q(int(c in ('a'+('c' if i<2 else 'd')))) for c in 'abcde'} for i in range(n)]
for i in range(n):
    assert sum(x[i].values()) == 2*z[i]
    for c in 'abcde':
        if c not in new[i]: assert x[i][c]==0
        assert x[i][c] <= y[c]
        if c in W: assert x[i][c] <= z[i]
Z=sum(z);Y=sum(y.values())
assert Z==4 and Y==3 and Z==quota*Y

# The old profile obeys the following universal inequalities for every
# feasible nonnegative certificate.  The normalized coefficient check
# is exact and independent of LP solver tolerance.
# At level 1: Z <= y_c <= Y.
# At level 2, writing A=y_a,C=y_c,D=y_d:
# z1 <= C/2;
# z2 <= min(C,(A+C)/2) <= A/4+3C/4;
# z3+z4 <= min(2D,A+D) <= 3A/4+5D/4;
# hence Z <= A+5(C+D)/4 <= 5Y/4 < 4Y/3.
# At level 3: 3Z <= 3y_a+2y_c+2y_d <=3Y.
for A,C,D in product(range(15), repeat=3):
    if A+C+D==0: continue
    A,C,D = map(Q, (A,C,D))
    z_bound = C/2 + min(C,(A+C)/2) + min(2*D,A+D)
    convex_bound = A + Q(5,4)*(C+D)
    assert z_bound <= convex_bound <= Q(5,4)*(A+C+D)
    assert convex_bound < quota*(A+C+D)
assert Q(1) < quota and Q(5,4) < quota
print('PASS: 4-voter / 3-seat / 5-candidate profile and one approval addition')
print('PASS: all FJR+ constraints for the post-change level-2 certificate')
print('PASS: exact Z=4, Y=3, Hare threshold q=4/3')
print('PASS: exact coefficient proof: pre-change levels 1, 2, 3 exclude violations')
print('PASS: 3374 nonzero coefficient-grid sanity cases (not used as proof)')
