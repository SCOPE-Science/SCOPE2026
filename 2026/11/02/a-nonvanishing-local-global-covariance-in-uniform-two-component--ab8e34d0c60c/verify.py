"""Independent finite enumeration of two-component Cayley-forest degree laws."""
from fractions import Fraction
from itertools import combinations
from collections import Counter
from math import comb


def tree_count(k):
    return 1 if k == 1 else k**(k-2)


def normalizer(n):
    return Fraction((n-1)*(n+6), 2) * Fraction(n, 1)**(n-4)


def conditional_degree(q, d):
    if q == 1:
        return Fraction(int(d == 0), 1)
    if not (1 <= d <= q-1):
        return Fraction(0, 1)
    return (Fraction(comb(q-2, d-1), 1)
            * Fraction(1, q)**(d-1)
            * Fraction(q-1, q)**(q-d-1))


def forest_counts(n):
    edges = list(combinations(range(n), 2))
    hist = Counter()
    total = 0
    for chosen in combinations(edges, n-2):
        parents = list(range(n))
        def root(x):
            while parents[x] != x:
                x = parents[x]
            return x
        ok = True
        for u, v in chosen:
            a, b = root(u), root(v)
            if a == b:
                ok = False
                break
            parents[a] = b
        if not ok:
            continue
        q = sum(root(v) == root(0) for v in range(n))
        degree = sum(0 in e for e in chosen)
        hist[(q, degree)] += 1
        total += 1
    return hist, total


def run():
    checks = 0
    for n in range(2, 9):
        hist, total = forest_counts(n)
        assert Fraction(total) == normalizer(n), (n,total,normalizer(n))
        checks += 1
        for q in range(1, n):
            q_mass = Fraction(comb(n-1, q-1)*tree_count(q)*tree_count(n-q), total)
            for d in range(0, n):
                exact = Fraction(hist[(q,d)], total)
                predicted = q_mass * conditional_degree(q, d)
                assert exact == predicted, (n,q,d,exact,predicted)
                checks += 1
        e_s = sum((Fraction(count,total) * (n-q)
                   for (q,d),count in hist.items()), Fraction())
        e_d = sum((Fraction(count,total) * d
                   for (q,d),count in hist.items()), Fraction())
        e_sd = sum((Fraction(count,total) * d * (n-q)
                    for (q,d),count in hist.items()), Fraction())
        e_s2 = sum((Fraction(count,total)*(n-q)**2
                    for (q,d),count in hist.items()), Fraction())
        assert e_s == Fraction(4*n,n+6)
        assert e_s2 == Fraction(2*n*n,n+6)
        assert e_s2-e_s**2 == Fraction(2*n*n*(n-2),(n+6)**2)
        checks += 2
        assert e_d == 2 - Fraction(4,n)
        assert e_sd - e_s * e_d == Fraction(-2*(n-2),n+6)
        checks += 3
        for q in range(2,n-1):
            ratios = [conditional_degree(q+1,d)/conditional_degree(q,d)
                      for d in range(1,q)]
            assert all(a<b for a,b in zip(ratios,ratios[1:]))
            assert conditional_degree(q+1,q)>0
            checks += 2
        print('n=',n,'forests=',total,'covariance=',e_sd-e_s*e_d)
    print('PASS; exact forest matching assertions =',checks)


if __name__ == '__main__':
    run()
