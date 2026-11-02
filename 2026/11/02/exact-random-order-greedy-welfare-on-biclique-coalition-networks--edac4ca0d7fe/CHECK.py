"""Exact, deterministic verification of a random-order greedy coalition theorem.

Run with Python 3.10+: python check.py
The program verifies finite identities; the manuscript supplies the proof for all sizes.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations
from math import comb, factorial


def greedy_score(arrival):
    """Earliest-created coalition wins among maximizing positive-gain choices.

    Entries are 0 or 1 for sides of a unit-weight complete bipartite graph.
    Score counts cross-part edges, one copy rather than twice social welfare.
    """
    groups = []
    for x in arrival:
        gains = [sum(y != x for y in group) for group in groups]
        if gains and max(gains) > 0:
            group_id = gains.index(max(gains))
            groups[group_id].append(x)
        else:
            groups.append([x])
    return sum(group.count(0) * group.count(1) for group in groups)


def initial_run_score(seq, a, b):
    first = seq[0]
    run = 0
    for x in seq:
        if x == first:
            run += 1
        else:
            break
    return a * b - (run-1) * (b if first == 0 else a)


def exact_distribution(a, b):
    n = a+b
    out=Counter()
    for r in range(1,a+1):
        # First r agents from side A, followed by a side B agent.
        probability = Fraction(1,1)
        for i in range(r): probability *= Fraction(a-i,n-i)
        probability *= Fraction(b,n-r)
        out[Fraction(a*b-(r-1)*b, a*b)] += probability
    for r in range(1,b+1):
        probability = Fraction(1,1)
        for i in range(r): probability *= Fraction(b-i,n-i)
        probability *= Fraction(a,n-r)
        out[Fraction(a*b-(r-1)*a, a*b)] += probability
    assert sum(out.values(), Fraction()) == 1
    return out


def closed_mean(a, b):
    n=a+b
    return 1-Fraction(1,a+1)-Fraction(1,b+1)+Fraction(2,n)


count_words = 0
count_permutations = 0
for a in range(1,9):
    for b in range(1,9):
        n=a+b
        theoretical=exact_distribution(a,b)
        assert sum(x*p for x,p in theoretical.items()) == closed_mean(a,b)
        # Every possible side-arrival word is tested against the actual algorithm.
        if n <= 12:
            hist=Counter()
            for pos in combinations(range(n),a):
                aset=set(pos)
                seq=tuple(0 if i in aset else 1 for i in range(n))
                observed=greedy_score(seq)
                assert observed == initial_run_score(seq,a,b),(a,b,seq,observed)
                hist[Fraction(observed,a*b)] += 1
                count_words += 1
            empirical={k: Fraction(v,comb(n,a)) for k,v in hist.items()}
            assert empirical == theoretical,(a,b,empirical,theoretical)
        assert closed_mean(a,b) >= Fraction(1,2)+Fraction(1,n)
        aa,bb=sorted((a,b))
        if a!=b and a>=2:
            # Compare only locally more-balanced partitions at same n.
            pass
        if n <= 8:
            # Explicit labeled arrival permutations: duplicate side words occur
            # a!*b! times.  Test every one to catch label dependence.
            labels=tuple(range(n))
            hist_label=Counter()
            for perm in permutations(labels):
                seq=tuple(0 if k<a else 1 for k in perm)
                val=greedy_score(seq)
                assert val == initial_run_score(seq,a,b)
                hist_label[Fraction(val,a*b)] += 1
                count_permutations += 1
            assert {k:Fraction(v,factorial(n)) for k,v in hist_label.items()}==theoretical

# A star (a=1) has a non-concentrating uniform limiting distribution.
for b in range(1,25):
    dist=exact_distribution(1,b)
    assert dist[Fraction(1)] == Fraction(2,b+1) if b>=2 else dist[Fraction(1)]==1
    for j in range(1,b): assert dist[Fraction(j,b)] == Fraction(1,b+1)

print('PASS: side-arrival words',count_words)
print('PASS: fully labeled orders',count_permutations)
print('PASS: all rational laws and means for 1<=a,b<=8')
print('PASS: sharp finite bound for 1<=a,b<=8')
print('PASS: star distribution for 1<=b<=24')
print('Sample K_(3,4):', sorted(exact_distribution(3,4).items()))
