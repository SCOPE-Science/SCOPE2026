"""Exact finite checks for isolated chords and connected induced motifs.
Run with Python 3, without third-party dependencies.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations
from math import comb, factorial


def double_factorial_odd(t):
    """Return (2t-1)!! for t >= 0."""
    out = 1
    for k in range(1, t + 1):
        out *= 2*k - 1
    return out


def perfect_matchings(points):
    if not points:
        yield ()
        return
    a = points[0]
    for j in range(1, len(points)):
        b = points[j]
        for rest in perfect_matchings(points[1:j] + points[j+1:]):
            yield ((a, b),) + rest


def crosses(e, f):
    a, b = e
    c, d = f
    return (a < c < b < d) or (c < a < d < b)


@lru_cache(None)
def permutations_of(r):
    return tuple(permutations(range(r)))


@lru_cache(None)
def canonical_signature(r, mask):
    pairs = tuple(combinations(range(r), 2))
    adj = [[0]*r for _ in range(r)]
    for j, (a,b) in enumerate(pairs):
        adj[a][b] = adj[b][a] = (mask >> j) & 1
    best = (1 << len(pairs)) - 1
    for perm in permutations_of(r):
        val = 0
        for j, (a,b) in enumerate(pairs):
            val |= adj[perm[a]][perm[b]] << j
        best = min(best, val)
    return best


def is_connected(r, signature):
    if r == 1:
        return True
    pairs = tuple(combinations(range(r), 2))
    adj = [set() for _ in range(r)]
    for j,(a,b) in enumerate(pairs):
        if (signature >> j) & 1:
            adj[a].add(b)
            adj[b].add(a)
    seen = {0}
    frontier = [0]
    while frontier:
        for v in adj[frontier.pop()]:
            if v not in seen:
                seen.add(v)
                frontier.append(v)
    return len(seen) == r


def pattern_counts(matching, max_r=4):
    n = len(matching)
    edges = [[crosses(matching[i], matching[j]) for j in range(n)] for i in range(n)]
    isolated = sum(not any(row) for row in edges)
    out = Counter()
    for r in range(2, min(max_r,n)+1):
        for subset in combinations(range(n),r):
            mask = 0
            for j,(a,b) in enumerate(combinations(range(r),2)):
                if edges[subset[a]][subset[b]]:
                    mask |= 1 << j
            out[(r,canonical_signature(r,mask))] += 1
    return isolated,out


def isolation_probability(n,k):
    return Fraction(double_factorial_odd(k)*double_factorial_odd(n-1-k),double_factorial_odd(n))


def normalized_covariance(n,r):
    total = Fraction(0)
    for k in range(n):
        count = 2*n-2*k-1
        loss = comb(k,r) + comb(n-1-k,r) - comb(n,r)
        total += count*isolation_probability(n,k)*loss
    return total / comb(n,r)


def verify():
    assertion_count = 0
    for n in range(2,7):
        totals = Counter()
        joint = Counter()
        total_isolated = 0
        count = 0
        for match in perfect_matchings(tuple(range(2*n))):
            isolated, cnt = pattern_counts(match)
            total_isolated += isolated
            count += 1
            totals.update(cnt)
            joint.update({t:isolated*v for t,v in cnt.items()})
        assert count == double_factorial_odd(n)
        assertion_count += 1
        ei = Fraction(total_isolated,count)
        assert ei == sum((2*n-2*k-1)*isolation_probability(n,k) for k in range(n))
        assertion_count += 1
        for key, total in totals.items():
            r, sig = key
            if not is_connected(r,sig):
                continue
            # p_H is the small-diagram induced frequency, with the same
            # probability on every chosen r-subset in a larger diagram.
            small_total = Counter()
            for match in perfect_matchings(tuple(range(2*r))):
                _, tmp = pattern_counts(match)
                small_total.update(tmp)
            p_h = Fraction(small_total[key],double_factorial_odd(r))
            ex = Fraction(total,count)
            assert ex == comb(n,r)*p_h, (n,key,ex,comb(n,r)*p_h)
            actual = Fraction(joint[key],count)-ei*ex
            predicted = ex*normalized_covariance(n,r)
            assert actual == predicted, (n,key,actual,predicted)
            assert actual < 0, (n,key,actual)
            assertion_count += 3
        # The disconnected two-vertex independent-set pattern has opposite sign.
        if n>=2:
            edgeless = (2,0)
            e_nonedge = Fraction(totals[edgeless],count)
            c_nonedge = Fraction(joint[edgeless],count)-ei*e_nonedge
            assert c_nonedge > 0
            assertion_count += 1
        print(f'n={n}: {count} matchings checked')
    # A separate algebraic identity: all connected motifs have the same
    # normalized factor regardless of their shape, and the factor is negative.
    for n in range(2,70):
        for r in range(2,min(n,10)+1):
            assert normalized_covariance(n,r) < 0
            assertion_count += 1
    print(f'PASS: {assertion_count} exact assertions')


if __name__ == '__main__':
    verify()
