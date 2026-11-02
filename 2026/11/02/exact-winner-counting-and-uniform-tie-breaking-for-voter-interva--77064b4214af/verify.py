"""Exact winner-counting recurrence and independent exhaustive validation.

Input intervals are None (no supporters) or inclusive one-based voter intervals.
Distinct input positions represent distinct candidate labels, including duplicates of an interval.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations, product
from math import comb
from random import Random


def _choose(n, j):
    return comb(n, j) if 0 <= j <= n else 0


def _weighted_choice(options, rng):
    total = sum(weight for _, weight in options)
    assert total > 0
    q = rng.randrange(total)
    for obj, weight in options:
        if q < weight:
            return obj
        q -= weight
    raise AssertionError('unreachable')


def solve(intervals, k, voter_weights):
    """Return (optimal score, exact count, state), supporting uniform reconstruction."""
    M = len(intervals)
    n = len(voter_weights)
    assert 0 <= k <= M and n >= 1
    assert all(w >= 0 for w in voter_weights)
    assert all(v is None or (1 <= v[0] <= v[1] <= n) for v in intervals)
    lengths = defaultdict(list)
    empties = []
    for i, interval in enumerate(intervals):
        if interval is None:
            empties.append(i)
        else:
            lengths[interval].append(i)
    types = sorted(lengths, key=lambda x: (x[1], x[0]))
    dp = [dict() for _ in types]
    edges = [[] for _ in types]
    for c_idx, c in enumerate(types):
        c_pool = lengths[c]
        for p_idx in range(-1, c_idx):
            p = None if p_idx == -1 else types[p_idx]
            if p is not None and not (p[0] < c[0] and p[1] < c[1]):
                continue
            subordinate = [i for d, ids in lengths.items() if d != c
                           and c[0] <= d[0] and d[1] <= c[1]
                           and not (p is not None and p[0] <= d[0] and d[1] <= p[1])
                           for i in ids]
            H = len(subordinate)
            multiplicity = len(c_pool)
            lo = max(c[0], 1 if p is None else p[1] + 1)
            gain = sum(voter_weights[lo-1:c[1]], 0)
            edge = (p_idx, subordinate, c_pool, gain)
            edges[c_idx].append(edge)
            before = {0: (0, 1)} if p_idx == -1 else dp[p_idx]
            for used, (score, number) in before.items():
                for chosen in range(1, min(k-used, H + multiplicity) + 1):
                    coefficient = _choose(H + multiplicity, chosen) - _choose(H, chosen)
                    assert coefficient > 0
                    candidate = score + gain
                    key = used + chosen
                    prior = dp[c_idx].get(key)
                    if prior is None or candidate > prior[0]:
                        dp[c_idx][key] = (candidate, number*coefficient)
                    elif candidate == prior[0]:
                        dp[c_idx][key] = (candidate, prior[1] + number*coefficient)
    finals = []
    if k <= len(empties):
        finals.append((0, _choose(len(empties), k), -1, k))
    for e in range(min(k, len(empties)) + 1):
        for c_idx, states in enumerate(dp):
            if k-e in states:
                score, cnt = states[k-e]
                finals.append((score, cnt*_choose(len(empties), e), c_idx, e))
    optimum = max(score for score, _, _, _ in finals)
    winners = sum(cnt for score, cnt, _, _ in finals if score == optimum)
    assert 1 <= winners <= comb(M,k)
    return optimum, winners, (dp, edges, empties, finals)


def sample_uniform(intervals, k, voter_weights, rng=None):
    """Exact conditional-uniform sampler when rng.randrange is unbiased."""
    if rng is None:
        from secrets import SystemRandom
        rng = SystemRandom()
    optimum, count, (dp, edges, empties, finals) = solve(intervals,k,voter_weights)
    final = _weighted_choice([((c,e),ways) for score,ways,c,e in finals
                              if score == optimum], rng)
    c_idx,e = final
    selected = list(rng.sample(empties,e))
    used = k-e
    while c_idx >= 0:
        score_here, _ = dp[c_idx][used]
        options = []
        for edge in edges[c_idx]:
            p, subordinate, c_pool, gain = edge
            before = {0:(0,1)} if p == -1 else dp[p]
            H, M = len(subordinate), len(c_pool)
            for t in range(1, min(used,H+M)+1):
                old = before.get(used-t)
                if old is None or old[0] + gain != score_here:
                    continue
                ways = _choose(H+M,t)-_choose(H,t)
                options.append(((edge,t),old[1]*ways))
        edge,t = _weighted_choice(options,rng)
        p, subordinate, c_pool, gain = edge
        H,M = len(subordinate),len(c_pool)
        max_count = _weighted_choice([(a,_choose(M,a)*_choose(H,t-a))
                                      for a in range(1,min(M,t)+1)
                                      if 0 <= t-a <= H],rng)
        selected.extend(rng.sample(c_pool,max_count))
        selected.extend(rng.sample(subordinate,t-max_count))
        used -= t
        c_idx = p
    assert used == 0 and len(selected) == k and len(set(selected)) == k
    return frozenset(selected)


def brute(intervals,k,weights):
    optimum = None
    count = 0
    for committee in combinations(range(len(intervals)),k):
        covered = set()
        for c in committee:
            interval=intervals[c]
            if interval is not None:
                covered.update(range(interval[0],interval[1]+1))
        score=sum(weights[i-1] for i in covered)
        if optimum is None or score > optimum:
            optimum,count = score,1
        elif score == optimum:
            count += 1
    return (optimum,count)


def verify():
    rng = Random(1043)
    tested = 0
    for n in range(1,5):
        domain = [None]+[(i,j) for i in range(1,n+1) for j in range(i,n+1)]
        for m in range(1,6):
            for profile in product(domain,repeat=m):
                for k in range(m+1):
                    result = solve(profile,k,[1]*n)[:2]
                    reference = brute(profile,k,[1]*n)
                    assert result == reference, (n,profile,k,result,reference)
                    tested += 1
    random_tested=5000
    for _ in range(random_tested):
        n=rng.randrange(1,9)
        m=rng.randrange(15)
        domain=[None]+[(i,j) for i in range(1,n+1) for j in range(i,n+1)]
        profile=[rng.choice(domain) for i in range(m)]
        weights=[rng.randrange(7) for i in range(n)]
        k=rng.randrange(m+1)
        assert solve(profile,k,weights)[:2] == brute(profile,k,weights)
    profile=[(1,4),(2,3),(3,5),(3,5),(4,4),None]
    weights=[1,2,1,3,2]
    assert solve(profile,3,weights)[:2] == (9,7)
    valid=set()
    for C in combinations(range(6),3):
        seen=set()
        for c in C:
            if profile[c] is not None:
                seen.update(range(profile[c][0],profile[c][1]+1))
        if sum(weights[i-1] for i in seen) == 9:
            valid.add(frozenset(C))
    assert len(valid)==7
    draws=[sample_uniform(profile,3,weights,rng) for _ in range(7000)]
    assert set(draws)==valid
    print('PASS: '+str(tested)+' exhaustive profile-size cases; '
          +str(random_tested)+' seeded weighted cases; 7000 valid exact-choice samples; '
          'illustrative optimum 9, winner count 7.')

if __name__=='__main__':
    verify()
