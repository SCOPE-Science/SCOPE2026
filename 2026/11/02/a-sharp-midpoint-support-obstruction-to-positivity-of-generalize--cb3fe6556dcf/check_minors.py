"""Finite rational and asymptotic checks for the midpoint-support theorem.

No infinite theorem is inferred from these tests; see RESULT.md for the proof.
Run: python check_minors.py
"""
from fractions import Fraction
from math import comb, lgamma, log, sqrt


def entry_two_point(s, n, k):
    return Fraction(comb(n + k, k), 2) * (
        (1 - s) ** n * s ** k + s ** n * (1 - s) ** k
    )


def exact_witness(s, n, k):
    a = entry_two_point(s, n, n)
    b = entry_two_point(s, k, k)
    c = entry_two_point(s, n, k)
    assert c == entry_two_point(s, k, n)
    assert c * c > a * b, (s, n, k)
    return c * c / (a * b)


cases = [
    (Fraction(1, 4), 3, 1),
    (Fraction(1, 3), 8, 4),
    (Fraction(2, 5), 18, 12),
    (Fraction(9, 20), 77, 63),
]
for s, n, k in cases:
    ratio_sq = exact_witness(s, n, k)
    print('EXACT_NEGATIVE_MINOR', str(s), n, k, 'ratio_sq=', float(ratio_sq))

# Confirm exact positivity of the first few midpoint compressions by
# a rational Gram reduction: all leading determinants are positive.
# At the midpoint, G = A A^T where the infinite Gram representation
# is proved in RESULT.md. The finite leading determinants can also be
# checked symbolically via the Pascal matrix: det G[0:N] = 2^{-N(N-1)}.
from fractions import Fraction

def determinant(mat):
    n=len(mat); a=[row[:] for row in mat]; out=Fraction(1)
    for k in range(n):
        j=next((j for j in range(k,n) if a[j][k]!=0),None)
        if j is None:return Fraction(0)
        if j!=k:a[k],a[j]=a[j],a[k];out=-out
        t=a[k][k];out*=t
        for i in range(k+1,n):
            scale=a[i][k]/t
            for col in range(k+1,n):a[i][col]-=scale*a[k][col]
            a[i][k]=Fraction(0)
    return out
for size in range(1, 8):
    gram = [[Fraction(comb(i + j, j), 2 ** (i + j)) for j in range(size)] for i in range(size)]
    det = determinant(gram)
    assert det > 0, (size, det)
    print('MIDPOINT_POSITIVE_DETERMINANT', size, str(det))

# Asymptotic log-ratio is checked numerically at moderate dimensions.
# Use log-gamma rather than huge integer conversions for this diagnostic.
def logsumexp(a, b):
    import math
    h = max(a, b)
    return h + math.log(math.exp(a - h) + math.exp(b - h))


def logcomb(m, k):
    return lgamma(m + 1) - lgamma(k + 1) - lgamma(m - k + 1)


def log_two_point(s, n, k):
    s = float(s)
    return logcomb(n + k, k) - log(2) + logsumexp(
        n * log(1 - s) + k * log(s),
        n * log(s) + k * log(1 - s),
    )

for s in [Fraction(1, 4), Fraction(1, 3), Fraction(2, 5)]:
    h = float(s * (1 - s))
    target = -log(2 * sqrt(h))
    for m in [300, 1000, 3000]:
        k = int(float(s) * m)
        n = m - k
        logr = log_two_point(s, n, k) - (
            log_two_point(s, n, n) + log_two_point(s, k, k)
        ) / 2
        assert abs(logr / m - target) < 0.02
        print('RATE_DIAGNOSTIC', str(s), m, 'measured=', logr/m, 'target=', target)
print('CHECKS_OK')
