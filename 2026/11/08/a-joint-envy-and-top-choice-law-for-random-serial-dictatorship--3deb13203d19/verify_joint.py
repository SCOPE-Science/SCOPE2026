"""Exact finite checks of the random-priority joint envy-count theorem.

No third-party libraries. From the containing folder: python3 verify_joint.py.
This checker is only a finite diagnostic; the RESULT.md analytic proof is essential.
"""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import permutations, product
from math import factorial


def harmonic(n):
    return sum((Q(1, k) for k in range(1, n+1)), Q(0))


def probability(s, r, k):
    # Probability exactly k of the s still-unenvied allocated goods
    # outrank the most preferred one of r available goods.
    top = r
    bot = 1
    for i in range(k):
        top *= s-i
    for i in range(k+1):
        bot *= s+r-i
    return Q(top, bot)


def joint(n):
    current = {(0, 0): Q(1)}
    for j in range(1, n+1):
        r = n-j+1
        new = defaultdict(Q)
        for (s, t), w in current.items():
            assert sum((probability(s,r,k) for k in range(s+1)), Q(0)) == 1
            new[(s+1,t+1)] += w*Q(r,n)
            new[(s+1,t)] += w*(Q(r,s+r)-Q(r,n))
            for k in range(1, s+1):
                new[(s+1-k,t)] += w*probability(s,r,k)
        current = {key:w for key,w in new.items() if w}
        assert sum(current.values(), Q(0)) == 1
    return current


def independent_bruteforce(n):
    # Fix RSD priority order by exchangeability; enumerate all ordered profile tuples.
    ranks = list(permutations(range(n)))
    counts = defaultdict(int)
    both = 0
    total = factorial(n)**n
    for prefs in product(ranks, repeat=n):
        free = set(range(n))
        chosen = []
        for p in prefs:
            x = next(x for x in p if x in free)
            free.remove(x)
            chosen.append(x)
        pos = [{x:k for k,x in enumerate(p)} for p in prefs]
        unenvied = [all(pos[j][chosen[j]] < pos[j][chosen[i]] for j in range(i+1,n)) for i in range(n)]
        top = [pos[i][chosen[i]] == 0 for i in range(n)]
        both += sum(a and b for a,b in zip(unenvied,top))
        counts[(sum(unenvied),sum(top))] += 1
    return {key:Q(val,total) for key,val in counts.items()}, Q(both,total)


def verify(n):
    p = joint(n)
    expected_u = sum((Q(u)*w for (u,t),w in p.items()), Q(0))
    expected_t = sum((Q(t)*w for (u,t),w in p.items()), Q(0))
    mixed = sum((Q(u*t)*w for (u,t),w in p.items()), Q(0))
    cov = mixed-expected_u*expected_t
    h = harmonic(n)
    assert expected_u == h
    assert expected_t == Q(n+1,2)
    assert cov == Q(1)-h/n
    # First-choice indicators form an independent Bernoulli family with probabilities r/n.
    expected_tt = sum((Q(t*t)*w for (u,t),w in p.items()), Q(0))
    assert expected_tt-expected_t**2 == Q(n*n-1,6*n)
    if n <= 4:
        brute, overlap = independent_bruteforce(n)
        assert p == brute, (n, [(key,p.get(key),brute.get(key)) for key in p.keys()|brute.keys() if p.get(key) != brute.get(key)])
        assert overlap == 1, (n, overlap)
    print('PASS n=%d states=%d E(U)=%s E(T)=%s Cov(U,T)=%s%s' % (n,len(p),h,expected_t,cov,' exhaustive' if n<=4 else ''))


if __name__ == '__main__':
    for n in range(1,8):
        verify(n)
    print('ALL EXACT JOINT CHECKS PASSED')
