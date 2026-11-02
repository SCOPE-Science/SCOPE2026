"""Independent arithmetic and finite-word checks of the block-width theorem.

Run with the Python 3 standard library: python3 verify.py
The infinite statements depend on the mathematical proof, not these finite checks.
"""
from collections import Counter
from functools import lru_cache
from itertools import product
from decimal import Decimal, localcontext


def unbordered_counts(q, maximum):
    u = [1]
    for n in range(1, maximum + 1):
        u.append(q * u[n-1] - (u[n//2] if n % 2 == 0 else 0))
    return u


def greedy_width(word):
    n = len(word)
    if n == 0:
        return 0
    for j in range(1, n // 2 + 1):
        if word[:j] == word[-j:]:
            return 2 + greedy_width(word[j:-j])
    return 1


def maximum_width_by_all_outer_borders(word):
    # Independent of the greedy rule: exhaust every possible outer block length.
    if not word:
        return 0
    possibilities = [1]
    n = len(word)
    for j in range(1, n // 2 + 1):
        if word[:j] == word[-j:]:
            possibilities.append(2 + maximum_width_by_all_outer_borders(word[j:-j]))
    return max(possibilities)


def theoretical_width_histogram(q, max_n):
    u = unbordered_counts(q, max_n)
    hist = [{0: 1}]
    for n in range(1, max_n + 1):
        row = Counter({1: u[n]})
        for j in range(1, n//2 + 1):
            for w, count in hist[n-2*j].items():
                row[w+2] += u[j] * count
        assert sum(row.values()) == q**n
        hist.append(dict(row))
    return hist


def composition_counts(m_max):
    # Recurrence by the final part: first part unrestricted; old < 2 * new.
    by_last = [[0]*(m_max+1) for _ in range(m_max+1)]
    b = [1] + [0]*m_max
    for total in range(1, m_max+1):
        for last in range(1, total+1):
            if total == last:
                by_last[total][last] = 1
            else:
                by_last[total][last] = sum(
                    by_last[total-last][previous]
                    for previous in range(1, total-last+1) if previous < 2*last
                )
        b[total] = sum(by_last[total])
    return b


def norm_unbordered_polynomials(max_n):
    # a[n][k] is [x^k] u_n(1/x) * x^n.
    a = [[1]]
    for n in range(1, max_n + 1):
        p = [1]+[0]*n
        for j in range(1, n//2+1):
            for d, coefficient in enumerate(a[j]):
                p[j+d] -= coefficient
        while len(p)>1 and p[-1]==0:
            p.pop()
        a.append(p)
    return a


def inverse_series(denominator, degree):
    # [x^n] (1 - sum_{j>=1} x^j a_j(x))^-1.
    inv = [1]+[0]*degree
    for n in range(1, degree+1):
        inv[n] = -sum(denominator[j]*inv[n-j] for j in range(1,n+1))
    return inv


def triangle_row(n):
    # OEIS A274190 g(n,k).
    rows = [[1]]
    for i in range(1,n+1):
        old = rows[-1]
        row = [1]+[0]*i
        for k in range(1,i+1):
            row[k] = (old[k-1] if k-1 < len(old) else 0) + (old[2*k] if 2*k<len(old) else 0)
        rows.append(row)
    return rows


def run_checks():
    samples = [(2,14),(3,9),(4,7)]
    checked = 0
    for q,max_n in samples:
        hist = theoretical_width_histogram(q,max_n)
        for n in range(1,max_n+1):
            actual = Counter(greedy_width(w) for w in product(range(q),repeat=n))
            assert actual == Counter(hist[n]), (q,n,actual,hist[n])
            checked += q**n
        u = unbordered_counts(q,max_n)
        for n in range(1,max_n+1):
            direct = sum(not any(w[:j] == w[-j:] for j in range(1,n))
                         for w in product(range(q),repeat=n))
            assert direct == u[n],(q,n,direct,u[n])

    # Separately check the published greedy-optimality premise against an
    # exhaustive search through all permissible outer border lengths.
    optimality_checked = 0
    for q, max_n in [(2,15),(3,9),(4,7)]:
        for n in range(1, max_n+1):
            for word in product(range(q),repeat=n):
                assert greedy_width(word) == maximum_width_by_all_outer_borders(word)
                optimality_checked += 1

    mmax = 75
    b = composition_counts(mmax)
    a = norm_unbordered_polynomials(mmax)
    denominator = [1]+[0]*mmax
    for j in range(1,mmax+1):
        for d,c in enumerate(a[j]):
            if j+d <= mmax:
                denominator[j+d] -= c
    inv = inverse_series(denominator,mmax)
    assert inv == b, (inv,b)
    assert b[:19] == [1,1,2,3,5,8,12,19,29,44,67,101,152,228,342,511,763,1138,1695]

    rows = triangle_row(80)
    for m in range(0,39):
        for n in range(max(1,2*m-1),81):
            assert rows[n][n-m] == b[m], (n,m,rows[n][n-m],b[m])

    with localcontext() as ctx:
        ctx.prec=35
        reference = {2:'6.4686',3:'2.5908',4:'1.9080',5:'1.6314'}
        for q,ref in reference.items():
            u = unbordered_counts(q,250)
            p = sum(Decimal(u[j])/(Decimal(q)**(2*j)) for j in range(1,251))
            E=(1+p)/(1-p)
            assert abs(E-Decimal(ref)) < Decimal('0.00006'), (q,E,ref)

    print('VERIFY_OK; exhaustive_words=%d; greedy_optimality_words=%d; coefficient_degree=%d; OEIS_rows=%d' %
          (checked,optimality_checked,mmax,len(rows)))


if __name__ == '__main__':
    run_checks()
