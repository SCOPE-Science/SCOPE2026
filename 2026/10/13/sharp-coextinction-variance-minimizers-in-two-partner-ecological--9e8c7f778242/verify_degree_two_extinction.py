"""Exact finite verification of degree-two ecological coextinction variance identities.

Python 3 standard library only. Every computation uses integers or fractions.
The general theorem is proved algebraically in RESULT.md; finite checks are auxiliary.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, combinations_with_replacement
from math import comb


def pair_prob(n, h, j):
    if not 0 <= j <= n or not 0 <= h <= n:
        raise ValueError((n, h, j))
    return Fraction(comb(n-j, h-j), comb(n, h)) if h >= j else Fraction(0)


def invariants(n, edges):
    degrees = [0]*n
    multiplicity = Counter(edges)
    for u, v in edges:
        assert 0 <= u < v < n
        degrees[u] += 1
        degrees[v] += 1
    wedge = sum(comb(d, 2) for d in degrees)
    duplicates = sum(comb(c, 2) for c in multiplicity.values())
    return degrees, wedge, duplicates


def formula_fixed(n, edges, h):
    m = len(edges)
    _, w, d = invariants(n, edges)
    t2, t3, t4 = (pair_prob(n, h, j) for j in (2, 3, 4))
    return (m*t2*(1-t2) + m*(m-1)*(t4-t2*t2)
            + 2*(t3-t4)*w + 2*(t2-2*t3+t4)*d)


def formula_bernoulli(n, edges, q):
    m = len(edges)
    _, w, d = invariants(n, edges)
    return (m*q*q*(1-q*q) + 2*q**3*(1-q)*w
            + 2*q*q*(1-q)**2*d)


def actual_fixed(n, edges, h):
    states = [sum(u in gone and v in gone for u, v in edges)
              for gone in (set(s) for s in combinations(range(n), h))]
    mean = Fraction(sum(states), len(states))
    return sum((Fraction(k)-mean)**2 for k in states)/len(states)


def actual_bernoulli(n, edges, q):
    mean = Fraction(0)
    second = Fraction(0)
    for h in range(n+1):
        for gone in combinations(range(n), h):
            gone = set(gone)
            count = sum(u in gone and v in gone for u, v in edges)
            prob = q**h*(1-q)**(n-h)
            mean += prob*count
            second += prob*count**2
    return second-mean*mean


def lower(n, m, h):
    r, s = divmod(2*m, n)
    wmin = (n-s)*comb(r, 2)+s*comb(r+1, 2)
    t2, t3, t4 = (pair_prob(n, h, j) for j in (2, 3, 4))
    return (m*t2*(1-t2) + m*(m-1)*(t4-t2*t2)
            + 2*(t3-t4)*wmin)


def independently_checked():
    profiles = states = equality_cases = 0
    for n, lower_m, upper_m in ((4,2,5),(5,3,5),(6,3,4)):
        pairs = list(combinations(range(n), 2))
        for m in range(lower_m, upper_m+1):
            for idx in combinations_with_replacement(range(len(pairs)), m):
                edges = [pairs[i] for i in idx]
                degrees, w, d = invariants(n, edges)
                r, s = divmod(2*m,n)
                wmin = (n-s)*comb(r, 2)+s*comb(r+1,2)
                balanced = (w == wmin)
                distinct = (d == 0)
                for h in range(n+1):
                    actual = actual_fixed(n, edges, h)
                    theoretical = formula_fixed(n, edges, h)
                    assert actual == theoretical, (n,m,idx,h,actual,theoretical)
                    assert theoretical >= lower(n, m, h), (n,m,idx,h)
                    if h == 2:
                        equal_expected = distinct
                    elif h == n-1:
                        equal_expected = balanced
                    elif 3 <= h <= n-2:
                        equal_expected = distinct and balanced
                    else:
                        equal_expected = True
                    assert (theoretical == lower(n,m,h)) == equal_expected, (n,m,idx,h)
                    equality_cases += bool(equal_expected)
                    states += comb(n,h)
                for q in (Fraction(1,4),Fraction(1,2),Fraction(3,4)):
                    exact = actual_bernoulli(n, edges, q)
                    assert exact == formula_bernoulli(n, edges, q)
                    minv = (m*q*q*(1-q*q)+2*q**3*(1-q)*wmin)
                    assert exact >= minv
                    assert (exact == minv) == (balanced and distinct)
                    states += 2**n
                profiles += 1
    n=6
    cycle=[(0,1),(1,2),(2,3),(3,4),(4,5),(0,5)]
    concentrated=[(0,1),(0,1),(0,2),(0,3),(0,4),(0,5)]
    assert formula_bernoulli(n,cycle,Fraction(1,2)) == Fraction(15,8)
    assert formula_bernoulli(n,concentrated,Fraction(1,2)) == Fraction(13,4)
    assert actual_fixed(n,cycle,3) == Fraction(9,25)
    assert actual_fixed(n,concentrated,3) == Fraction(39,25)
    print(f"VERIFY_OK profiles={profiles} exact_event_contributions={states} equality_cases={equality_cases}")


if __name__ == '__main__':
    independently_checked()
