"""Definition-level verification of fixed-priority serial dictatorship.
All priorities and ballot orders are fixed in advance. Preferences are iid uniform.
"""
from itertools import permutations
from fractions import Fraction
from collections import defaultdict
from math import factorial


def by_definition(n, order):
    rankings = list(permutations(range(n)))
    states = {((), 0): 1}  # allocated school sequence; binary mask of envious positions
    for t, agent in enumerate(order):
        nxt = defaultdict(int)
        for (prefix, mask), weight in states.items():
            unavailable = set(prefix)
            for ranking in rankings:
                house = next(s for s in ranking if s not in unavailable)
                # Common priorities use rank 0 as highest priority.  Earlier
                # assigned schools with lower-priority assignees can block.
                rank = {s: j for j, s in enumerate(ranking)}
                envied = any((agent < order[j] and rank[prefix[j]] < rank[house])
                             for j in range(t))
                nxt[(prefix + (house,), mask | (int(envied) << t))] += weight
        states = nxt
    ans = defaultdict(int)
    for (_, mask), weight in states.items():
        ans[mask] += weight
    denominator = factorial(n) ** n
    assert sum(ans.values()) == denominator
    return {j: Fraction(ans[j], denominator) for j in range(1 << n)}


def formula(n, order):
    p = []
    for t, agent in enumerate(order):
        earlier_lower = sum(order[j] > agent for j in range(t))
        k = n - t
        p.append(Fraction(earlier_lower, k + earlier_lower))
    probabilities = {}
    for mask in range(1 << n):
        probability = Fraction(1)
        for t in range(n):
            probability *= p[t] if mask & (1 << t) else 1 - p[t]
        probabilities[mask] = probability
    return probabilities, p


def run():
    checked = 0
    distributions = {}
    for n in range(1, 5):
        for order in permutations(range(n)):
            found = by_definition(n, order)
            predicted, _ = formula(n, order)
            assert found == predicted, (n, order, found, predicted)
            distributions[(n, order)] = found
            checked += 1
        print('ALL',n,'common-priority serial orders verified',factorial(n))
    swaps=0
    for n in range(2,5):
        for order in permutations(range(n)):
            baseline=distributions[(n,order)]
            for t in range(n-1):
                if order[t] < order[t+1]: continue # already correctly priority ordered
                correction=list(order)
                correction[t],correction[t+1]=correction[t+1],correction[t]
                improved=distributions[(n,tuple(correction))]
                for threshold in range(1,n+1):
                    p_before=sum(v for mask,v in baseline.items() if mask.bit_count()>=threshold)
                    p_after=sum(v for mask,v in improved.items() if mask.bit_count()>=threshold)
                    assert p_after <= p_before, (n,order,correction,threshold,p_before,p_after)
                swaps+=1
    print('ALL',swaps,'adjacent priority corrections for n<=4 verified for every tail threshold')
    original=(1,2,4,3,0)  # three higher agents, then rank-4, then rank-1
    repaired=(1,2,4,0,3)
    n=5
    for order in (original,repaired):
        found = by_definition(n, order)
        predicted,p=formula(n,order)
        assert found==predicted
        multi=sum(x for mask,x in found.items() if mask.bit_count()>=2)
        any_envious=sum(x for mask,x in found.items() if mask.bit_count()>=1)
        print('WITNESS',order,'Bernoulli parameters',p,
              'P(2+)',multi,'P(1+)',any_envious, 'P(0)',1-any_envious)
        checked +=1
    for order in permutations(range(5)):
        _,p=formula(5,order)
        assert all(Fraction(0)<=x<=Fraction(1) for x in p)
    print('EXACT DEFINITIONAL VERIFICATION PASSED:',checked,'orders; each jointly all binary envy patterns')

if __name__=='__main__':run()
