from fractions import Fraction

# Diffusion direction for one random transmission-rate parameter.
v = (-1, 1)
A_common = [[v[i] * v[j] for j in range(2)] for i in range(2)]
A_independent = [[1, 0], [0, 1]]

assert A_common == [[1, -1], [-1, 1]]
assert A_independent == [[1, 0], [0, 1]]

# Determinants/ranks in dimension two.
det_common = A_common[0][0] * A_common[1][1] - A_common[0][1] * A_common[1][0]
det_ind = A_independent[0][0] * A_independent[1][1] - A_independent[0][1] * A_independent[1][0]
assert det_common == 0
assert det_ind == 1

# Quadratic variation coefficient in the total direction e=(1,1).
e = (1, 1)
def quad(A, x):
    return sum(x[i] * A[i][j] * x[j] for i in range(2) for j in range(2))
assert quad(A_common, e) == 0
assert quad(A_independent, e) == 2

# Exact witness from q^2 = 0.02 * (S I)^2 with S=1/2, I=1/4, alpha=0.
S = Fraction(1, 2)
I = Fraction(1, 4)
variance = Fraction(1, 50)
q2 = variance * (S * I) ** 2
assert q2 == Fraction(1, 3200)
assert -q2 == Fraction(-1, 3200)  # common-driver cross covariance
assert 2 * q2 == Fraction(1, 1600)  # independent-driver QV rate of S+I

# Fokker--Planck second-derivative coefficient matrices are one half the covariance.
# The common model has a nonzero mixed coefficient; the independent model does not.
assert A_common[0][1] == -1
assert A_independent[0][1] == 0

print('VERIFY_OK')
print('q2=', q2)
print('common_cross_covariance=', -q2)
print('independent_total_qv_rate=', 2*q2)
