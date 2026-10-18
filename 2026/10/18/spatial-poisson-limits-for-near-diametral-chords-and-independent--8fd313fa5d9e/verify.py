"""Exact finite consistency checks for near-antipodal chords and crossings.

Python 3, standard library only. Enumerates every perfect matching through n=7;
checks known crossing moments and a newly derived joint covariance formula.
Finite checks do not establish weak convergence.
"""
from collections import Counter
from fractions import Fraction


def matchings(vertices):
    if not vertices:
        yield ()
        return
    v = vertices[0]
    for i in range(1, len(vertices)):
        w = vertices[i]
        rest = vertices[1:i] + vertices[i+1:]
        for tail in matchings(rest):
            yield ((v, w),) + tail


def crosses(e, f):
    a, b = sorted(e)
    c, d = sorted(f)
    return (a < c < b < d) or (c < a < d < b)


def color(edge, n):
    a, b = edge
    delta = (b - a) % (2*n)
    return n - min(delta, 2*n - delta)


def possible_edges(n, j):
    if j == 0:
        return {tuple(sorted((i, i+n))) for i in range(n)}
    if not 1 <= j < n:
        raise ValueError('requires 1 <= j < n')
    d = n-j
    return {tuple(sorted((i, (i+d)%(2*n)))) for i in range(2*n)}


def falling(v, r):
    out = 1
    for k in range(r):
        out *= v-k
    return out


def verify():
    checks = 0
    total_matchings = 0
    for n in range(2, 8):
        m = n if n < 3 else 3
        classes = [possible_edges(n,j) for j in range(m)]
        for j, edges in enumerate(classes):
            assert len(edges) == (n if j == 0 else 2*n)
            checks += 1
        counts = [0]*m
        moments = [0]*m
        sc = sc2 = 0
        factorial_mixed = 0
        size = 0
        for matching in matchings(tuple(range(2*n))):
            size += 1
            c = sum(crosses(a,b) for i,a in enumerate(matching) for b in matching[i+1:])
            cnt = Counter(color(edge,n) for edge in matching)
            sc += c
            sc2 += c*c
            for j in range(m):
                counts[j] += cnt[j]
                moments[j] += cnt[j]*c
            if m >= 2:
                factorial_mixed += falling(cnt[0],2)*cnt[1]
        total_matchings += size
        expected = 1
        for v in range(1,2*n,2):
            expected *= v
        assert size == expected
        checks += 1
        mean_cross = Fraction(sc,size)
        var_cross = Fraction(sc2,size)-mean_cross**2
        assert mean_cross == Fraction(n*(n-1),6)
        assert var_cross == Fraction(n*(n-1)*(n+3),45)
        checks += 2
        for j in range(m):
            expectation = Fraction(counts[j],size)
            assert expectation == Fraction(n if j==0 else 2*n,2*n-1)
            cov = Fraction(moments[j],size)-expectation*mean_cross
            formula = expectation * Fraction(n*(n-1)-3*j*j,3*(2*n-3))
            assert cov == formula, (n,j,cov,formula)
            checks += 2
        if m >= 2:
            edges0,edges1=classes[:2]
            admissible=0
            for e in edges0:
                for f in edges0:
                    if f == e or set(e)&set(f):
                        continue
                    for g in edges1:
                        if not(set(g)&set(e)) and not(set(g)&set(f)):
                            admissible += 1
            denom=1
            for h in range(3):
                denom *= 2*n-(2*h+1)
            observed = Fraction(factorial_mixed,size)
            expected = Fraction(admissible,denom)
            assert observed == expected,(n,observed,expected)
            checks += 1
        print('n',n,'matchings',size,'checks',checks)
    print('VERIFY_OK', 'perfect_matchings',total_matchings,'assertions',checks)

if __name__ == '__main__':
    verify()
