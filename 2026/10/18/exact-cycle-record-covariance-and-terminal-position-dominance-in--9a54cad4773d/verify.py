"""Exact checks for the cycle-count/left-to-right record covariance theorem.
Run: python3 verify.py. Uses only Python's standard library.
Finite checks illustrate and independently challenge the proof; they do not replace it.
"""
from fractions import Fraction as F
from itertools import permutations
from math import comb, factorial

checks = 0

def equal(a, b, msg):
    global checks
    checks += 1
    assert a == b, (msg, a, b)

def cycle_count(p):
    seen = [False] * len(p)
    result = 0
    for start in range(len(p)):
        if not seen[start]:
            result += 1
            k = start
            while not seen[k]:
                seen[k] = True
                k = p[k] - 1
    return result

def record_positions(p):
    high = 0
    out = []
    for x in p:
        out.append(int(x > high))
        high = max(high, x)
    return out

# Independent enumeration with no appeal to the Ewens parameter or recurrence.
for n in range(2, 10):
    count = factorial(n)
    sumc = 0
    sumr = [0] * n
    sumcr = [0] * n
    sum_c2 = 0
    sum_r2 = 0
    for p in permutations(range(1, n + 1)):
        c = cycle_count(p)
        r = record_positions(p)
        sumc += c
        sum_c2 += c * c
        sum_r2 += sum(r) ** 2
        for j in range(n):
            sumr[j] += r[j]
            sumcr[j] += c * r[j]
    hn = sum((F(1, k) for k in range(1, n + 1)), F(0))
    variance = sum((F(k - 1, k * k) for k in range(1, n + 1)), F(0))
    equal(F(sumc, count), hn, f'mean cycles n={n}')
    equal(F(sum_c2, count) - hn * hn, variance, f'var cycles n={n}')
    equal(F(sum_r2, count) - hn * hn, variance, f'var records n={n}')
    covsum = F(0)
    for j in range(1, n + 1):
        cov = F(sumcr[j-1], count) - F(sumc * sumr[j-1], count*count)
        predicted = F(j - 1, j*j*comb(n, j))
        equal(F(sumr[j-1], count), F(1, j), f'P(record position {j},n={n})')
        equal(cov, predicted, f'cycle-record covariance j={j},n={n}')
        covsum += cov
    equal(covsum, sum((F(j-1, j*j*comb(n,j)) for j in range(1,n+1)), F(0)), f'global n={n}')
    print('enumeration n=',n,' permutations=',count,' covariance=',covsum)

# Independent checks of the analytically derived parameter perturbation recurrence.
for j in range(1, 31):
    p = F(1, j)
    q = F(j-1, j*j)
    for m in range(j, 41):
        equal(p, F(1, j), f'p({m},{j})')
        equal(q, F(j-1,j*j*comb(m,j)), f'derivative({m},{j})')
        if m < 40:
            # Evaluated at theta=1; formal derivative of rational recurrence.
            denom = m + 1
            a = F(denom-j,denom)
            aprime = F(j,denom*denom)
            bprime = -F(1,denom*denom)
            q, p = a*q + aprime*p + bprime, a*p+F(1,denom)

# Exact Ewens weighted permutations, providing a second route to the recurrence.
for n in range(1, 8):
    for theta in (2, 3):
        denominator = 1
        for k in range(n): denominator *= theta + k
        sums = [0] * n
        for p in permutations(range(1,n+1)):
            w = theta ** cycle_count(p)
            for j, ind in enumerate(record_positions(p)):
                sums[j] += w * ind
        equal(sum(theta ** cycle_count(p) for p in permutations(range(1,n+1))),denominator,f'Ewens norm n={n}, theta={theta}')
        # Recursive rational prediction p_{m,j}(theta)
        for j in range(1,n+1):
            predicted = F(theta,theta+j-1)
            for m in range(j+1,n+1):
                predicted = ((theta+m-1-j)*predicted+1)/F(theta+m-1)
            equal(F(sums[j-1],denominator),predicted,f'Ewens record n={n},j={j},theta={theta}')

print('CHECKS_OK:',checks)
