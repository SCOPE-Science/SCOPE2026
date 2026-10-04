from fractions import Fraction
from math import pi

# Canonical singleton increments s_j=1/((j+1)(j+2)).
def s(j):
    return Fraction(1, (j+1)*(j+2))

# Exact telescoping and the two-point prefix defect used in the proof.
for L in range(1, 501):
    canonical_prefix = sum(s(j) for j in range(L))
    assert canonical_prefix == Fraction(L, L+1)
    lower_uL = Fraction(2, 2*L+1)
    delta = lower_uL - Fraction(1, L+1)
    assert delta == Fraction(1, (L+1)*(2*L+1))
    jump = s(L-1) - s(L)
    assert jump == Fraction(2, L*(L+1)*(L+2))
    epsilon = delta * jump
    assert epsilon == Fraction(2, L*(L+1)**2*(L+2)*(2*L+1))
    assert epsilon > 0

# Finite Abel-summation identity behind the quantitative Schur-convexity step.
# We generate monotone probability sequences by Robin-Hood transfers from s.
for L in range(1, 25):
    N = 80
    base = [s(j) for j in range(N)]
    # Move an admissible rational amount from coordinate L-1 to L,
    # preserving monotonicity; this is only a sanity family for the identity.
    gap = base[L-1] - base[L]
    eta = gap / 4
    d = base[:]
    d[L-1] -= eta
    d[L] += eta
    assert all(d[j] >= d[j+1] for j in range(len(d)-1))
    e = [base[j]-d[j] for j in range(len(d))]
    E = []
    acc = Fraction(0)
    for x in e:
        acc += x
        E.append(acc)
    A = [base[j]+d[j] for j in range(len(d))]
    lhs = sum(base[j]**2-d[j]**2 for j in range(len(d)))
    rhs = sum(E[j]*(A[j]-A[j+1]) for j in range(len(d)-1)) + E[-1]*A[-1]
    assert lhs == rhs
    assert lhs >= 0

kappa2 = pi*pi/3.0 - 3.0
assert 0.28 < kappa2 < 0.30
print('formula_checks=500')
print('abel_identity_families=24')
print(f'kappa2={kappa2:.15f}')
print('VERIFY_OK')
