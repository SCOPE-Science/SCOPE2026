"""Self-contained checks of weighted harmonic Toeplitz monomial semigroup defects.

Only finite algebraic identities and numerical convergence are tested here;
the accompanying proof establishes the assertions for all parameters.
"""
from fractions import Fraction
from math import exp, gamma, lgamma, pi

checks = 0

def verify(condition, description):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(description)

def moments_integer_a(a, stop):
    h = [Fraction(1)]
    for j in range(1, stop + 1):
        h.append(h[-1] * Fraction(j, j + a))
    return h

def action_z(k, h):
    if k >= 0:
        return k + 1, Fraction(1)
    j = -k
    return k + 1, h[j] / h[j - 1]

def action_z_power(N, k, h):
    target = k + N
    if k >= 0:
        return target, Fraction(1)
    j = -k
    if j > N:
        return target, h[j] / h[j - N]
    if j == N:
        return target, h[N]
    return target, h[N] / h[N - j]

def action_power_of_z(N, k, h):
    coefficient = Fraction(1)
    for _ in range(N):
        k, step = action_z(k, h)
        coefficient *= step
    return k, coefficient

# Exact rational-moment check against independently constructed Toeplitz
# projection and operator-power actions (not against the desired d formula).
for a in (1, 2, 3, 5):
    h = moments_integer_a(a, 90)
    for N in range(2, 22):
        for k in range(-2 * N, 2 * N + 1):
            idxA, coeffA = action_z_power(N, k, h)
            idxB, coeffB = action_power_of_z(N, k, h)
            verify(idxA == idxB == k + N, 'target angular degree')
            if -N < k < 0:
                j = -k
                verify(coeffA - coeffB == (h[N] - h[j] * h[N-j]) / h[N-j],
                       'finite central band exact coefficient')
                verify(coeffA > coeffB, 'strict covariance')
            else:
                verify(coeffA == coeffB, 'vanishing off the central band')
        q = [h[j] * h[N-j] for j in range(1, N)]
        verify(min(q) == q[(N - 1) // 2], 'central maximizer')
        verify(all(q[j] == q[N - j - 2] for j in range(len(q))),
               'singular reflection symmetry')
        verify(all(q[j + 1] <= q[j] for j in range((len(q) - 1) // 2)),
               'monotonicity toward center')

# Check the exact singular-value formulas against one simple closed case.
# When alpha = 0, moments are 1/(k+1).  The rank-three defect for N=4
# has singular values 3sqrt(2)/20, 4/15, 3sqrt(2)/20.
h = moments_integer_a(1, 4)
def coeff_from_h(N, j, h):
    P = float(h[j] * h[N-j])
    return float(h[N]) / P**.5 - P**.5
verify(abs(coeff_from_h(4, 1, h) - 3*(2**.5)/20) < 1e-14,
       'alpha zero degree-four edge coefficient')
verify(abs(coeff_from_h(4, 2, h) - 4/15) < 1e-14,
       'alpha zero degree-four central coefficient')

# Supplementary asymptotic tests; these do not prove any infinite limit.
def log_h(j, a):
    return lgamma(j+1) + lgamma(a+1) - lgamma(j+a+1)
for a in (1.0, 2.0, 3.0):
    N = 20000
    lN = log_h(N, a)
    singular = []
    for j in range(1, N):
        lp = log_h(j, a) + log_h(N-j, a)
        dj = exp(lN-lp/2) - exp(lp/2)
        singular.append(dj)
        verify(0 < dj < 1, 'strict positive singular value')
    verify(abs(max(singular)-2**(-a)) < .002, 'operator-norm asymptotic')
    for p in (0.5, 1.0, 2.0, 3.0):
        empirical = sum(x**p for x in singular)/N
        target = gamma(1+a*p/2)**2/gamma(2+a*p)
        verify(abs(empirical-target) < .002, 'Schatten bulk beta law')
    j = N//4
    predicted = ((j/N)*(1-j/N))**(a/2)
    verify(abs(singular[j-1]-predicted) < .003, 'bulk pointwise law')

verify(abs(gamma(1.5)**2/gamma(3)-pi/8) < 1e-14,
       'alpha-zero trace-class coefficient')
verify(abs(gamma(2)**2/gamma(4)-1/6) < 1e-14,
       'alpha-zero Hilbert-Schmidt coefficient squared')
print(f'PASS: {checks} exact and finite numerical checks')
