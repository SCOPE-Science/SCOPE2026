"""Exact independent checks of near-unanimous random-priority allocation law.
Python 3.10+, standard library only. All integer arithmetic.
"""
from itertools import permutations
from collections import Counter
from fractions import Fraction
from math import factorial

def suffix_winner(pref,n,k):
    available=set(range(k+1,n+1))
    return next(x for x in pref if x in available)

def prediction(pref):
    n=len(pref)
    t=Counter(suffix_winner(pref,n,k) for k in range(n))
    return dict(t)

def run_priority(pref, priority):
    n=len(pref); prefs=[tuple(range(1,n+1)) for _ in range(n-1)]+[pref]
    available=set(range(1,n+1))
    alloc=[0]*n
    for a in priority:
        item=next(x for x in prefs[a] if x in available)
        alloc[a]=item; available.remove(item)
    return tuple(alloc)

def sd_distribution(pref):
    n=len(pref)
    out=Counter()
    for order in permutations(range(n)):
        out[run_priority(pref,order)]+=1
    return out

def records(pref):
    rank={x:j for j,x in enumerate(pref)}
    return [x for x in range(1,len(pref)+1) if rank[x]==min(rank[y] for y in range(x,len(pref)+1))]

def efficient(pref, matching):
    n=len(pref)
    own_ranks=[{x:x for x in range(1,n+1)} for _ in range(n-1)]+[{x:j for j,x in enumerate(pref)}]
    for y in permutations(range(1,n+1)):
        if y==matching:continue
        if all(own_ranks[i][y[i]]<=own_ranks[i][matching[i]] for i in range(n)) and any(own_ranks[i][y[i]]<own_ranks[i][matching[i]] for i in range(n)):
            return False
    return True

def unsigned_stirling(n):
    row=[1]
    for m in range(1,n+1):
        nxt=[0]*(m+1)
        for k in range(1,m+1):
            nxt[k]=row[k-1]+(m-1)*(row[k] if k<len(row) else 0)
        row=nxt
    return row

def compositions(n):
    if not n:yield ()
    else:
        for x in range(1,n+1):
            for rest in compositions(n-x):yield (x,)+rest

priority_checks=0; matching_checks=0; efficiency_checks=0; profile_checks=0
for n in range(2,7):
    outcomes=list(permutations(range(1,n+1)))
    expected_shapes=set()
    for pref in outcomes:
        profile_checks+=1
        mults=prediction(pref)
        assert set(mults)==set(records(pref))
        assert sum(mults.values())==n
        distribution=sd_distribution(pref)
        priority_checks+=factorial(n)
        matching_checks+=len(distribution)
        assert len(distribution)==len(mults)*factorial(n-1)
        for assignment in outcomes:
            exp=mults.get(assignment[-1],0)
            assert distribution[assignment]==exp,(n,pref,assignment,distribution[assignment],exp)
            if n<=5:
                assert (distribution[assignment]>0)==efficient(pref,assignment)
                efficiency_checks+=1
        expected_shapes.add(tuple(sorted(mults.values())))
    assert expected_shapes=={tuple(sorted(c)) for c in compositions(n)},(n,expected_shapes)
    actual=Counter(len(records(pref)) for pref in outcomes)
    assert all(actual[k]==unsigned_stirling(n)[k] for k in range(1,n+1))
    empirical=Fraction(sum(len(records(p))*factorial(n-1) for p in outcomes),factorial(n))
    theoretical=factorial(n-1)*sum((Fraction(1,j) for j in range(1,n+1)),Fraction())
    assert empirical==theoretical
    print('n',n,'profiles',len(outcomes),'R spectrum',sorted(actual.items()),'support expectation',empirical,'shapes',len(expected_shapes))

for n in (7,8):
    prefs=list(permutations(range(1,n+1)))
    for pref in [prefs[i] for i in range(0,len(prefs),max(1,len(prefs)//12))][:12]:
        predicted=prediction(pref)
        distribution=sd_distribution(pref)
        priority_checks+=factorial(n)
        matching_checks+=len(distribution)
        assert sum(distribution.values())==factorial(n)
        assert all(v==predicted[assignment[-1]] for assignment,v in distribution.items())
        assert len(distribution)==len(predicted)*factorial(n-1)

print('PASS',{'preference_profiles_exhaustive_n2_through6':profile_checks,
'priority_evaluations':priority_checks,
'supported_matching_comparisons':matching_checks,
'independent_pareto_exhaustive_comparisons':efficiency_checks})

# Independent complete check of exact ordered-composition multiplicities,
# with no priority-order enumeration, through seven objects.
for n in range(2,8):
    actual=Counter()
    for pref in permutations(range(1,n+1)):
        mults=prediction(pref)
        actual[tuple(mults[x] for x in sorted(mults))]+=1
    formula={}
    for c in compositions(n):
        denom=1; remaining=n
        for part in c:
            denom*=remaining
            remaining-=part
        formula[c]=factorial(n)//denom
        assert factorial(n)%denom==0
    assert dict(actual)==formula,(n, actual, formula)
    assert sum(actual.values())==factorial(n)
    assert len(actual)==2**(n-1)
    print('composition frequency verified n', n, 'ordered types',len(actual))
print('COMPOSITION FREQUENCY PASS')
