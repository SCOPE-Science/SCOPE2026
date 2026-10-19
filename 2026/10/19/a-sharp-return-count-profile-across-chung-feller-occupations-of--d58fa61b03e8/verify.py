"""Exact independent checks for excursion-return regression in simple walk bridges.

Run: python verify.py
Only Python's standard library is required.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb, pi, sqrt

checks = 0

def check(condition, message):
    global checks
    if not condition:
        raise AssertionError(message)
    checks += 1


def catalans(n):
    return [comb(2*j, j) // (j + 1) for j in range(n + 2)]


def excursion_counts(nmax):
    """Positive/negative primitive Dyck excursions, separately weighted by Catalan numbers."""
    c = catalans(nmax)
    dp = [defaultdict(int) for _ in range(nmax + 1)]
    dp[0][(0, 0)] = 1  # (positive occupation half-length, number of returns)
    for n in range(nmax):
        for (a, k), count in list(dp[n].items()):
            for ell in range(1, nmax - n + 1):
                w = count * c[ell - 1]
                dp[n + ell][(a, k + 1)] += w        # negative excursion
                dp[n + ell][(a + ell, k + 1)] += w  # positive excursion
    return dp


def enumerated(n):
    counts = defaultdict(int)
    for up_indices in combinations(range(2 * n), n):
        up = set(up_indices)
        height = 0
        positive_steps = 0
        returns = 0
        for i in range(2 * n):
            step = 1 if i in up else -1
            if height + step / 2 > 0:
                positive_steps += 1
            height += step
            if height == 0:
                returns += 1
        check(height == 0 and positive_steps % 2 == 0, 'bridge convention')
        counts[(positive_steps // 2, returns)] += 1
    return dict(counts)


def theoretical_regression(n, j, c):
    return Fraction(sum(c[a+b] * c[n-a-b]
                        for a in range(j+1) for b in range(n-j+1)), c[n]) - 1


def theoretical_moments(n, counts):
    total = comb(2 * n, n)
    centered = Fraction(n, 2)
    ek = Fraction(sum(k*v for (a,k),v in counts.items()), total)
    e_quad = Fraction(sum((Fraction(a)-centered)**2 * v
                           for (a,k),v in counts.items()), total)
    ek_quad = Fraction(sum(k*(Fraction(a)-centered)**2 * v
                              for (a,k),v in counts.items()), total)
    return ek, e_quad, ek_quad - ek*e_quad


# Two independent constructions: direct walk enumeration and Catalan excursions.
dp = excursion_counts(18)
for n in range(1, 9):
    direct = enumerated(n)
    check(dict(dp[n]) == direct, f'independent path/excursion census n={n}')

for n in range(1, 19):
    c = catalans(n)
    b = comb(2*n,n)
    counts = dp[n]
    check(sum(counts.values()) == b, f'total bridge count n={n}')
    marg = [sum(v for (a,k),v in counts.items() if a==j)
            for j in range(n+1)]
    for j in range(n+1):
        check(marg[j] == c[n], f'Chung-Feller occupation n={n},j={j}')
        numer = sum(k*v for (a,k),v in counts.items() if a==j)
        check(Fraction(numer,marg[j]) == theoretical_regression(n,j,c),
              f'conditional return mean n={n},j={j}')
        check(numer * c[n-j if n-j<=n else n] >= 0,
              f'nonnegative count n={n},j={j}')
    check(theoretical_regression(n,0,c) == Fraction(3*n,n+2), f'endpoint n={n}')
    for j in range(n):
        diff = theoretical_regression(n,j+1,c)-theoretical_regression(n,j,c)
        if j < (n-1)/2:
            want = Fraction(sum(c[s]*c[n-s] for s in range(j+1,n-j)), c[n])
            check(diff == want and diff > 0, f'unimodal rise n={n},j={j}')
        elif j == (n-1)/2:
            check(diff==0, f'odd midpoint plateau n={n}')
        else:
            check(diff<0, f'unimodal fall n={n},j={j}')
    ek,eq,cov = theoretical_moments(n,counts)
    check(ek == Fraction(4**n,b)-1, f'mean returns n={n}')
    check(eq == Fraction(n*(n+2),12), f'occupation variance n={n}')
    check(cov == -Fraction(n*(n-1)*4**n,48*b), f'quadratic covariance n={n}')

# Independent high-order rational verification of the expected-return profile.
for n in range(19, 121):
    c = catalans(n)
    f=[c[s]*c[n-s] for s in range(n+1)]
    cumulative=[0]
    for v in f: cumulative.append(cumulative[-1]+v)
    current=Fraction(3*n,n+2)
    check(current == theoretical_regression(n,0,c), f'large-n endpoint n={n}')
    for j in range(0,n):
        new=Fraction(cumulative[n-j]-cumulative[j+1],c[n])
        current += new
        # Algebraic signed telescoping identity, not numerical fitting.
        check(current == theoretical_regression(n,j+1,c),
              f'large-n increment n={n},j={j}')
    check(current==Fraction(3*n,n+2), f'large-n reflected endpoint n={n}')

# Asymptotic quantities are checked numerically only; the proof is analytic.
for n in (400,800):
    c=catalans(n)
    f=[c[s]*c[n-s] for s in range(n+1)]
    prefix=[0]
    for v in f: prefix.append(prefix[-1]+v)
    mm=Fraction(3*n,n+2)
    for j in range(n//2):
        mm+=Fraction(prefix[n-j]-prefix[j+1],c[n])
        if j+1 in (n//10,n//4,n//2):
            t=Fraction(j+1,n)
            target=8/sqrt(pi)*sqrt(float(t*(1-t)))
            check(abs(float(mm)/sqrt(n)-target)<0.065,
                  f'central profile approximation n={n},j={j+1}')

print(f'PASS: {checks} independent exact and asymptotic checks; maximum direct bridge length 16')
