"""Exact arithmetic checks for Borda party-score envelopes.

Run: python3 verify.py
No dependencies beyond Python 3 standard library.
"""
from fractions import Fraction
from itertools import permutations, combinations
from random import Random


def endpoints(m, r, k, t):
    den = m * (m - 1)
    low = r * (r - 1) + t * (m - r - k + t)
    high = r * (2 * m - r - k - 1) + t * (r + k - t)
    return Fraction(low, den), Fraction(high, den)


def feasible(m, r, k, t):
    return 2 <= m and 1 <= r < m and 1 <= k <= m and max(0, k - (m - r)) <= t <= min(r, k)


def tally(votes, m):
    z = [0] * m
    for vote in votes:
        assert sorted(vote) == list(range(m))
        for p, c in enumerate(vote):
            z[c] += m - 1 - p
    return z


def construct(m, r, k, t, side):
    assert feasible(m, r, k, t)
    Awin = list(range(t))
    Alose = list(range(t, r))
    Bwin = list(range(r, r + k - t))
    Blose = list(range(r + k - t, m))
    if side == 'high':
        top = Awin
        middle = Alose + Bwin
        bottom = Blose
    else:
        top = Bwin
        middle = Blose + Awin
        bottom = Alose
    q = len(middle)
    votes = []
    for shift in range(max(1,q)):
        rotated = middle[shift:] + middle[:shift]
        votes.append(top + rotated + bottom)
    assert all(len(v) == m for v in votes)
    return votes, set(Awin + Bwin)


def check(m, r, k, t, votes, elected):
    scores = tally(votes, m)
    assert len(elected) == k
    assert len(elected & set(range(r))) == t
    assert all(scores[u] >= scores[v] for u in elected for v in set(range(m)) - elected)
    psi = Fraction(sum(scores[:r]), len(votes) * m * (m - 1) // 2)
    lo, hi = endpoints(m, r, k, t)
    assert lo <= psi <= hi, (m,r,k,t,psi,lo,hi)
    return psi


def run():
    assertions = 0
    for m in range(2, 13):
        for r in range(1,m):
            for k in range(1,m+1):
                for t in range(max(0,k-m+r), min(r,k)+1):
                    lo, hi = endpoints(m,r,k,t)
                    assert 0 <= lo <= hi <= 1
                    a,e = construct(m,r,k,t,'low')
                    b,f = construct(m,r,k,t,'high')
                    assert e == f
                    assert check(m,r,k,t,a,e) == lo
                    assert check(m,r,k,t,b,f) == hi
                    # The convex midpoint is attainable by finite, exact ballots.
                    # Replicate each cyclic profile so its contribution weighs one-half.
                    mixed = a * len(b) + b * len(a)
                    assert check(m,r,k,t,mixed,e) == (lo+hi)/2
                    assertions += 4
    # Independently enumerate all one- and two-voter ballots at small orders.
    for m in range(2,6):
        perms = list(permutations(range(m)))
        for votes in ([p] for p in perms):
            scores = tally(votes,m)
            for r in range(1,m):
                for k in range(1,m+1):
                    for E in combinations(range(m),k):
                        elected=set(E)
                        if all(scores[u]>=scores[v] for u in elected for v in set(range(m))-elected):
                            check(m,r,k,len(elected&set(range(r))),votes,elected)
                            assertions+=1
        for p in perms:
            for q in perms:
                votes=[p,q]
                scores=tally(votes,m)
                for r in range(1,m):
                    for k in range(1,m+1):
                        E=set(sorted(range(m), key=lambda c:(-scores[c],c))[:k])
                        check(m,r,k,len(E&set(range(r))),votes,E)
                        assertions+=1
    rng=Random(314159)
    for _ in range(800):
        m=rng.randrange(3,11)
        r=rng.randrange(1,m)
        k=rng.randrange(1,m+1)
        vs=[rng.sample(list(range(m)),m) for _ in range(rng.randrange(1,22))]
        sc=tally(vs,m)
        E=set(sorted(range(m),key=lambda c:(-sc[c],c))[:k])
        check(m,r,k,len(E&set(range(r))),vs,E)
        assertions+=1
    # 51-voter party with near 80% normalized Borda score but no seats.
    m,r,k,t=10,8,2,0
    vote_base=list(range(10))
    all_votes=[vote_base[j:]+vote_base[:j] for _ in range(5) for j in range(10)]
    all_votes.append([8,9]+list(range(8)))
    sc=tally(all_votes,m)
    E={8,9}
    assert min(sc[j] for j in E)>max(sc[j] for j in range(8))
    assert check(m,r,k,t,all_votes,E) == Fraction(1828,2295)
    assert Fraction(1828,2295)>Fraction(79,100)
    assertions+=3
    print('PASS',assertions,'exact arithmetic assertions')


if __name__=='__main__':
    run()
