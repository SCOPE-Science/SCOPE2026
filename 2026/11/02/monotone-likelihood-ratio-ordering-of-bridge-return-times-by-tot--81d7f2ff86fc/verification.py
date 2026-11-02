"""Exact finite consistency checks for conditional return-time ordering.

All comparisons use integer arithmetic; no external packages are required.
"""
from collections import Counter
from itertools import combinations
from math import comb

checks = 0


def check(condition, description):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(description)


def catalan(m):
    return comb(2 * m, m) // (m + 1)


def forest(n, k):
    """Coefficient of z**n in (z*C(z))**k."""
    if n == k == 0:
        return 1
    if k < 1 or n < k:
        return 0
    return k * comb(2 * n - k, n - k) // (2 * n - k)


def moments(n, k, r):
    return [(t, forest(t, r) * forest(n - t, k - r))
            for t in range(r, n - k + r + 1)]


def bridge_exact_enumeration(n):
    count = Counter()
    counts = Counter()
    for positions in combinations(range(2 * n), n):
        upward = set(positions)
        height = 0
        returns = []
        for index in range(2 * n):
            height += 1 if index in upward else -1
            if height == 0:
                returns.append((index + 1) // 2)
        k = len(returns)
        counts[k] += 1
        for r, t in enumerate(returns, 1):
            count[k, r, t] += 1
    check(sum(counts.values()) == comb(2 * n, n), (n, "bridge total"))
    for k in range(1, n + 1):
        check(counts[k] == (2 ** k) * forest(n, k),
              (n, k, "excursion total"))
        for r in range(1, k):
            for t, weighted in moments(n, k, r):
                check(count[k, r, t] == 2 ** k * weighted,
                      (n, k, r, t, "return joint count"))
    return counts, count


def check_all_finite(n):
    total = comb(2 * n, n)
    check(sum(2 ** k * forest(n, k) for k in range(1, n + 1)) == total,
          (n, "bridge partition"))
    for k in range(2, n + 1):
        for r in range(1, k):
            masses = moments(n, k, r)
            denom = forest(n, k)
            check(sum(x for _, x in masses) == denom,
                  (n, k, r, "normalization"))
            check(sum(t*x for t,x in masses)*k == denom*r*n,
                  (n, k, r, "exchangeable mean"))
            if k == n:
                continue
            q = k - r
            mass_l = dict(masses)
            mass_h = dict(moments(n, k+1, r))
            den_h = forest(n, k+1)
            xs = list(range(r, n-q+1))
            # Verify the exact likelihood ratio, point-by-point, without division.
            for t in mass_h:
                u = n-t
                check(mass_h[t]*denom*(k+1)*(n-k)*q*(2*u-q-1)
                      ==mass_l[t]*den_h*k*(2*n-k-1)*(q+1)*(u-q),
                      (n,k,r,t,"closed likelihood ratio"))
            # Compare all conditional CDF thresholds with exact integers.
            low_cdf=high_cdf=0
            for t in xs:
                low_cdf += mass_l[t]
                high_cdf += mass_h.get(t,0)
                check(high_cdf*denom >= low_cdf*den_h,
                      (n,k,r,t,"stochastic order"))
            # Consecutive K comparison in monotone likelihood-ratio order,
            # zero extending the larger-K law at the excluded largest time.
            for t in xs[:-1]:
                lhs = mass_h[t]*mass_l[t+1]
                rhs = mass_h.get(t+1,0)*mass_l[t]
                check(lhs >= rhs,(n,k,r,t,"likelihood-ratio"))
                if q>1 and t+1 in mass_h:
                    check(lhs > rhs,(n,k,r,t,"strict ratio"))
            # Strict stochastic ordering at the rightmost point.
            check(mass_h.get(xs[-1],0)==0 and mass_l[xs[-1]]>0,
                  (n,k,r,"rightmost support"))
            if q == 1:
                # The (k+1)-conditioned law is (k)-law truncated at n-2.
                tail_numerator = mass_l[n-1]
                check(tail_numerator*k*(2*n-k-1)==denom*n*(k-1),
                      (n,k,"sharp total variation"))
                for t in mass_h:
                    check(mass_h[t]*(denom-tail_numerator)
                          ==mass_l[t]*den_h,
                          (n,k,r,t,"truncation"))


def main():
    for n in range(2, 11):
        bridge_exact_enumeration(n)
    for n in range(2, 41):
        check_all_finite(n)
    print(f"PASS: {checks:,} exact assertions; exhaustive bridges through 20 steps; conditional laws through semilength 40")


if __name__ == '__main__':
    main()
