"""Exact arithmetic certificate for a two-branch affine horseshoe.

Run: python3 verify_horseshoe.py
All rational arithmetic uses Python's standard-library Fraction.
"""
from fractions import Fraction as Q

J = (Q(-21, 10), Q(-4, 5))
C0 = (Q(-1023, 500), Q(-1791, 1000))
C1 = (Q(-197, 200), Q(-841, 1000))
L_RATES = (-Q(32, 27), -Q(19, 9))
R_RATES = (Q(2, 3), -Q(1))
ITINERARIES = ('LR' + 'L' * 11, 'L' * 13)
assert all(len(w) == 13 for w in ITINERARIES)

checks = 0

def require(condition, why):
    global checks
    if not condition:
        raise AssertionError(why)
    checks += 1

def lin_image(interval, slope, offset):
    u, v = interval
    return tuple(sorted((slope * u + offset, slope * v + offset)))

require(C0[0] < C0[1] < C1[0] < C1[1], 'disjoint initial domains')
for C in (C0, C1):
    require(J[0] < C[0] < C[1] < J[1], 'domains within return interval')

# The interval I maps into itself under both prescribed branches.
I = (Q(-19, 9), Q(95, 243))
require(I[0] < J[0] < J[1] < I[1], 'J subset I')
require(lin_image((I[0], Q(0)), *L_RATES) == I,
        'negative branch image of I')
right_image = lin_image((Q(0), I[1]), *R_RATES)
require(I[0] < right_image[0] < right_image[1] < I[1],
        'nonnegative branch image in I')

for i, (C, word) in enumerate(zip((C0, C1), ITINERARIES)):
    interval = C
    slope, intercept = Q(1), Q(0)
    for step, symbol in enumerate(word):
        lo, hi = interval
        if symbol == 'L':
            require(hi < -Q(1, 200),
                    f'branch {i}, stage {step}: strict negative margin')
            branch_slope, branch_intercept = L_RATES
        else:
            require(lo > Q(1, 200),
                    f'branch {i}, stage {step}: strict positive margin')
            branch_slope, branch_intercept = R_RATES
        interval = lin_image(interval, branch_slope, branch_intercept)
        slope, intercept = (branch_slope * slope,
                            branch_slope * intercept + branch_intercept)
    require(abs(slope) > 5, f'branch {i}: expanding iterate')
    require(interval[0] < J[0] - Q(1, 500),
            f'branch {i}: lower covering margin')
    require(interval[1] > J[1] + Q(1, 500),
            f'branch {i}: upper covering margin')
    inverse_J = lin_image(J, 1 / slope, -intercept / slope)
    require(C[0] < inverse_J[0] < inverse_J[1] < C[1],
            f'branch {i}: genuine interior inverse of J')
    print(f'branch {i}: word={word}, slope={slope}, '
          f'image={interval}, inverse_J={inverse_J}')
print(f'PASS: {checks} exact-rational assertions')

# Uniform interval-arithmetic certificate over the complete rational band.
# All interval endpoints are exact fractions; multiplication encloses all
# dependencies and is never evaluated by floating-point sampling.

def enclose(value):
    return value if isinstance(value, tuple) else (value, value)

def interval_add(x, y):
    x, y = enclose(x), enclose(y)
    return (x[0] + y[0], x[1] + y[1])

def interval_neg(x):
    x = enclose(x)
    return (-x[1], -x[0])

def interval_mul(x, y):
    x, y = enclose(x), enclose(y)
    corners = [u * v for u in x for v in y]
    return (min(corners), max(corners))

def parameter_branches(a):
    one_plus_a = interval_add(1, a)
    negative_slope = interval_neg(interval_mul(
        one_plus_a, interval_mul(interval_add(a, -1), interval_add(a, -1))))
    negative_offset = interval_neg(interval_add(
        interval_add(interval_mul(a, a), interval_mul(3, a)), 3))
    return ((negative_slope, negative_offset),
            (one_plus_a, enclose(-1)))

def enclose_iterate(domain, itinerary, a):
    left, right = parameter_branches(a)
    value = domain
    for step, symbol in enumerate(itinerary):
        if symbol == 'L':
            require(value[1] < 0, f'uniform negative stage {step}')
            slope, offset = left
        else:
            require(value[0] > 0, f'uniform positive stage {step}')
            slope, offset = right
        value = interval_add(interval_mul(slope, value), offset)
    return value

PARAMETER_BAND = (Q(-1, 3) - Q(1, 1000000),
                  Q(-1, 3) + Q(1, 1000000))
left, right = parameter_branches(PARAMETER_BAND)
for i, (domain, word) in enumerate(zip((C0, C1), ITINERARIES)):
    entire = enclose_iterate(domain, word, PARAMETER_BAND)
    # Endpoint propagation gives a tighter enclosure than initial-interval
    # propagation, proving that the two images straddle J for *every* a.
    lower_endpoint = enclose_iterate((domain[0], domain[0]), word, PARAMETER_BAND)
    upper_endpoint = enclose_iterate((domain[1], domain[1]), word, PARAMETER_BAND)
    if i == 0:  # right branch reverses once, producing positive orientation
        require(lower_endpoint[1] < J[0], 'uniform first image covers lower J')
        require(upper_endpoint[0] > J[1], 'uniform first image covers upper J')
    else:  # thirteen negative slopes produce negative orientation
        require(upper_endpoint[1] < J[0], 'uniform second image covers lower J')
        require(lower_endpoint[0] > J[1], 'uniform second image covers upper J')
    derivative = enclose(1)
    for symbol in word:
        derivative = interval_mul(derivative, left[0] if symbol == 'L' else right[0])
    require(min(abs(derivative[0]), abs(derivative[1])) > 5,
            f'uniform expanding branch {i}')
    print('uniform band branch', i, 'image enclosure:', entire,
          'endpoint images:', lower_endpoint, upper_endpoint,
          'slope enclosure:', derivative)
print(f'PASS: {checks} exact-rational assertions (point and closed band)')
