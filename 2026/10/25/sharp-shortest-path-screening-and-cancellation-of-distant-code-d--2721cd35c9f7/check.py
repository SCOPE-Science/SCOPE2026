from fractions import Fraction

# Exact Taylor coefficients of the stationary cubic equation on long test rings.
def coefficients(bits, order, a=Fraction(1,3)):
    size = len(bits)
    rows = [[Fraction(b)] + [Fraction(0)] * order for b in bits]
    for degree in range(1, order + 1):
        for i in range(size):
            c = rows[i]
            quadratic = sum(c[k] * c[degree-k] for k in range(degree+1))
            cubic = sum(c[k] * c[l] * c[degree-k-l]
                        for k in range(degree+1)
                        for l in range(degree-k+1))
            lap = rows[(i-1) % size][degree-1] - 2*c[degree-1] + rows[(i+1) % size][degree-1]
            slope = a if bits[i] == 0 else 1-a
            rows[i][degree] = ((1+a)*quadratic - cubic + lap)/slope
    return rows

a = Fraction(1,3)
size = 41
center = size // 2
base = [0] * size
reference = coefficients(base, 7, a)
for radius in range(1, 7):
    changed = base.copy()
    changed[center+radius] = 1
    observed = coefficients(changed, 7, a)
    assert all(observed[center][k] == reference[center][k] for k in range(radius))
    assert observed[center][radius] - reference[center][radius] == a**(-radius)
print('SINGLE_REMOTE_FLIP_EXACT_PASS', 6)

pattern = [(7*j + j//3) % 2 for j in range(size)]
for radius in range(1, 6):
    changed = pattern.copy()
    changed[center+radius] = 1 - changed[center+radius]
    before = coefficients(pattern, radius, a)
    after = coefficients(changed, radius, a)
    denominator = Fraction(1)
    for j in range(center, center+radius):
        denominator *= a if pattern[j] == 0 else 1-a
    expected = Fraction(pattern[center+radius] - changed[center+radius])/denominator
    assert all(before[center][k] == after[center][k] for k in range(radius))
    assert before[center][radius] - after[center][radius] == expected
print('HETEROGENEOUS_PATH_WEIGHTS_EXACT_PASS', 5)

radius = 5
left = base.copy()
right = base.copy()
left[center-radius] = 1
right[center+radius] = 1
p = coefficients(left, radius, a)
q = coefficients(right, radius, a)
assert all(p[center][k] == q[center][k] for k in range(radius+1))
print('OPPOSITE_FLIP_CANCELLATION_EXACT_PASS')

# The real-variable contraction bounds are monotone over 0 < m <= 1/2.
for m in (Fraction(1,100), Fraction(1,5), Fraction(1,3), Fraction(1,2)):
    r = m/16
    rho = m*m/256
    image_bound = (rho*(2+4*r) + (2+r)*r*r)/m
    lip = (4*rho+4*r+3*r*r)/m
    assert image_bound < r and lip < Fraction(1,2)
print('UNIFORM_CONTRACTION_SAMPLE_CHECKS_PASS')
print('CHECKS_PASS')
