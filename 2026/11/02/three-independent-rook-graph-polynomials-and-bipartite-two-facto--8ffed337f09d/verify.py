#!/usr/bin/env python3
"""Finite reproducibility checks of the three-independence enumerator of rook graphs.

Uses a connected-component recurrence and direct subset enumeration.
Only the mathematical invariant is checked; no external data are loaded.
"""
from collections import Counter
from functools import lru_cache
from math import comb, factorial


def component_counts(m, n):
    out = Counter()
    # Edge-free isolated vertices.
    if m == 1 and n == 0:
        out[0] = 1
    if m == 0 and n == 1:
        out[0] = 1
    # Alternating paths.
    if m and n and abs(m-n) <= 1:
        if m == n:
            out[m+n-1] += factorial(m) * factorial(n)
        else:
            out[m+n-1] += factorial(m) * factorial(n) // 2
    # Even cycles (length at least four).
    if m == n and m >= 2:
        out[2*m] += factorial(m) * factorial(n) // (2*m)
    # 3-stars.
    if (m, n) in ((1, 3), (3, 1)):
        out[3] += 1
    return dict(out)


@lru_cache(None)
def coefficient_polynomial(m, n):
    """Component containing a distinguished left-side vertex."""
    if m == 0:
        return (1,)
    out = Counter()
    for a in range(1, m+1):
        for b in range(n+1):
            components = component_counts(a, b)
            if not components:
                continue
            choices = comb(m-1, a-1) * comb(n, b)
            smaller = coefficient_polynomial(m-a, n-b)
            for edge_count, component_ways in components.items():
                for k, ways in enumerate(smaller):
                    if ways:
                        out[edge_count+k] += choices * component_ways * ways
    return tuple(out[k] for k in range(max(out, default=0)+1))


def brute(m, n):
    """Enumerate every selected rook-graph vertex subset, without species."""
    N = m*n
    out = Counter()
    total_outer = Counter()
    for mask in range(1<<N):
        selected = [(i,j) for i in range(m) for j in range(n) if (mask>>(i*n+j))&1]
        count_by_row = [0]*m
        count_by_col = [0]*n
        for i,j in selected:
            count_by_row[i] += 1
            count_by_col[j] += 1
        if any(count_by_row[i]+count_by_col[j]-2 > 2 for i,j in selected):
            continue
        out[len(selected)] += 1
        # Check that the complement is total-dominating directly.
        nons = set(selected)
        if all(any((k,l) not in nons and ((i==k and j!=l) or (j==l and i!=k))
                   for k in range(m) for l in range(n)) for i in range(m) for j in range(n)):
            total_outer[N-len(selected)] += 1
    return out, total_outer


def balanced_top(m):
    from fractions import Fraction
    # [t^m] exp(sum_{j>=2} t^j/(2j)) via exact recursion.
    coef = [Fraction(1)]
    for k in range(1,m+1):
        coef.append(sum((Fraction(j,1)*Fraction(1,2*j)*coef[k-j] for j in range(2,k+1)), Fraction(0))/k)
    return factorial(m)**2 * coef[m]



def analytic_egf(m, n):
    """Expand the displayed EGF directly with rational arithmetic."""
    from fractions import Fraction
    terms = Counter()
    terms[(1,0,0)] += Fraction(1)
    terms[(0,1,0)] += Fraction(1)
    for k in range(min(m,n)):
        a = b = k+1
        if a<=m and b<=n:
            terms[(a,b,2*k+1)] += Fraction(1)
    for k in range(1,max(m,n)+1):
        for a,b in ((k+1,k),(k,k+1)):
            if a<=m and b<=n:
                terms[(a,b,2*k)] += Fraction(1,2)
    for k in range(2,min(m,n)+1):
        terms[(k,k,2*k)] += Fraction(1,2*k)
    if m>=1 and n>=3:
        terms[(1,3,3)] += Fraction(1,6)
    if m>=3 and n>=1:
        terms[(3,1,3)] += Fraction(1,6)
    series = {(0,0,0):Fraction(1)}
    power = {(0,0,0):Fraction(1)}
    for degree in range(1,m+n+1):
        next_power = Counter()
        for (a,b,k),c in power.items():
            for (u,v,j),t in terms.items():
                if a+u<=m and b+v<=n:
                    next_power[(a+u,b+v,k+j)] += c*t
        power = next_power
        for key,c in power.items():
            series[key] = series.get(key,Fraction(0)) + c / factorial(degree)
    result = Counter()
    for (a,b,k),c in series.items():
        if a==m and b==n:
            result[k]+=factorial(m)*factorial(n)*c
    assert all(v.denominator==1 for v in result.values())
    return tuple(int(result[k]) for k in range(max(result,default=0)+1))

def main():
    tested=0
    count=0
    for m,n in ((1,1),(1,2),(1,3),(1,4),(2,2),(2,3),(2,4),
                (2,5),(2,6),(3,3),(3,4),(3,5),(4,4)):
        raw, outer = brute(m,n)
        proposed = coefficient_polynomial(m,n)
        assert all(raw[k] == (proposed[k] if k<len(proposed) else 0)
                   for k in range(m*n+1)), (m,n, raw, proposed)
        assert sum(raw.values()) == sum(proposed)
        if max(m,n) >= 5 and m+n>=6:
            assert all(outer[m*n-k] == raw[k] for k in range(m*n+1)), (m,n)
        tested+=1
        count+=1<<(m*n)
    for m,n in ((2,2),(3,3),(3,4),(4,4),(3,5)):
        assert analytic_egf(m,n)==coefficient_polynomial(m,n), (m,n)
    for m in range(2,9):
        poly = coefficient_polynomial(m,m)
        assert poly[2*m] == balanced_top(m)
        assert poly[2*m+1:] == (), (m,poly)
    print('VERIFY_OK direct_graphs=%d tested_subsets=%d analytic_EGF_cases=5 balanced_top_orders=2..8' % (tested,count))
    for m,n in ((3,3),(3,4),(4,4),(3,5),(4,5),(5,5)):
        p=coefficient_polynomial(m,n)
        print('D_%d_%d='%(m,n), p)
    print('SQUARE_COUNTS=', [(m,int(balanced_top(m))) for m in range(2,9)])

if __name__=='__main__':
    main()
