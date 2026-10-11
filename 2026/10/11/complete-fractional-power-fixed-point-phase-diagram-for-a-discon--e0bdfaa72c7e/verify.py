"""Exact spot-checks for the four-fixed-point classification.
The universal parameter theorem follows from a separate calculus proof.
"""
from fractions import Fraction as Q


def quartic(t):
    # For (a,b,c,d)=(1/20,1/2,19/20,1/4), both branches
    # reduce to this polynomial after the fourth-root substitution.
    return 10 + 10 * t**4 - 19 * t


assert quartic(Q(0)) > 0
assert quartic(Q(3, 4)) == -Q(139, 128) < 0
assert quartic(Q(1)) > 0
# Its derivative is 40t^3-19, strictly increasing for t>0;
# hence this 3-sign test forces exactly two roots in (0,1).
assert Q(19, 20)**4 > Q(16, 27)

# A second exact no-fixed-point example given by the original paper:
# d=1/3, b=1/2, a=1/10, c=9/10.
# Both thresholds have third-power = (1/8)/(4/27) = 27/32:
# (9/10)^3 = 729/1000 < 27/32.
assert Q(9, 10)**3 < Q(27, 32)

# A phase-boundary pair is non-overlapping at d>=1/2:
for d in (Q(1,2), Q(2,3), Q(3,4)):
    assert not(d < 1-d)

print('EXACT_RATIONAL_FIXED_POINT_WITNESSES_OK')
