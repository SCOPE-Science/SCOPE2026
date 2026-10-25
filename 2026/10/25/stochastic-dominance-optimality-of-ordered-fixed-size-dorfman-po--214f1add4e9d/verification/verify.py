"""Exact finite checks for heterogeneous fixed-size Dorfman pooling.

Run with Python 3 standard library; no packages, network, or external data.
These checks supplement rather than replace the general majorization proof.
"""
from fractions import Fraction as F
from itertools import combinations, product
from functools import reduce
import json
from pathlib import Path


def partitions(items, k):
    if not items:
        yield ()
        return
    first = items[0]
    for remaining in combinations(items[1:], k - 1):
        group = (first,) + remaining
        leftover = tuple(i for i in items if i not in group)
        for rest in partitions(leftover, k):
            yield (group,) + rest


def neg_probs(a, groups):
    result = []
    for group in groups:
        r = F(1)
        for i in group:
            r *= a[i]
        result.append(r)
    return result


def pmf(a, groups):
    mass = [F(1)]
    for u in neg_probs(a, groups):
        nxt = [F(0)] * (len(mass) + 1)
        for j, prob in enumerate(mass):
            nxt[j] += prob * u
            nxt[j + 1] += prob * (1-u)
        mass = nxt
    return mass


def direct_pmf(a, groups):
    mass = [F(0)] * (len(groups) + 1)
    for state in product((0,1), repeat=len(a)):
        w = F(1)
        for infected, prob_neg in zip(state, a):
            w *= (1-prob_neg) if infected else prob_neg
        positive_pools = sum(any(state[i] for i in group) for group in groups)
        mass[positive_pools] += w
    return mass


def tails(d):
    return [sum(d[j:],F(0)) for j in range(1,len(d))]


def variance_of_positive_pools(a, groups):
    return sum((u * (1-u) for u in neg_probs(a,groups)),F(0))


def profiles(n):
    return [
        [F(j+1,n+3) for j in range(n)],
        [F(j+2,3*n+6) for j in range(n)],
        [F(2*n+j+2,3*n+6) for j in range(n)],
        [F((j+3)**2,(n+5)**2) for j in range(n)],
        [F(n+1,n+3) for _ in range(n)],
        sorted([F(1)] + [F(j+1,n+3) for j in range(1,n)]),
    ]


def run():
    comparisons = 0
    enumerations = 0
    direct_comparisons = 0
    case_summary = []
    for m,k in [(2,2),(3,2),(2,3),(4,2),(3,3)]:
        n = m*k
        groups = list(partitions(tuple(range(n)),k))
        ordered = tuple(tuple(range(j*k,(j+1)*k)) for j in range(m))
        assert ordered in groups
        for a in profiles(n):
            assert a == sorted(a) and all(F(0)<z<=1 for z in a)
            best = tails(pmf(a,ordered))
            for grouping in groups:
                other = tails(pmf(a,grouping))
                assert all(x<=y for x,y in zip(best,other)), (m,k,a,grouping,best,other)
                comparisons += m
                if n==6 and k==2:
                    assert pmf(a,grouping)==direct_pmf(a,grouping)
                    direct_comparisons += m+1
            enumerations += len(groups)
        case_summary.append({'individuals':n,'pool_size':k,'pools':m,
                             'partitions_per_profile':len(groups),'profiles':len(profiles(n))})

    high_prevalence = [F(1,10),F(1,5),F(3,10),F(2,5)]
    low_prevalence = [F(3,5),F(7,10),F(4,5),F(9,10)]
    adjacent=((0,1),(2,3))
    extremes=((0,3),(1,2))
    variance_reversal={}
    for label,a in [('all_infection_probabilities_above_half',high_prevalence),
                    ('all_infection_probabilities_below_half',low_prevalence)]:
        best=pmf(a,adjacent)
        other=pmf(a,extremes)
        assert tails(best)[0]==tails(other)[0]
        assert all(x<=y for x,y in zip(tails(best),tails(other)))
        av=variance_of_positive_pools(a,adjacent)
        ev=variance_of_positive_pools(a,extremes)
        if label.startswith('all_infection_probabilities_above'):
            assert av>ev
        else:
            assert av<ev
        variance_reversal[label]={
            'negative_probabilities':[str(v) for v in a],
            'ordered_variance_positive_pools':str(av),
            'opposite_pairing_variance_positive_pools':str(ev),
            'ordered_expected_positive_pools':str(sum((1-u for u in neg_probs(a,adjacent)),F(0))),
            'opposite_expected_positive_pools':str(sum((1-u for u in neg_probs(a,extremes)),F(0))),
            'common_at_least_one_positive_pool_probability':str(tails(best)[0]),
            'ordered_at_least_two_positive_pools_probability':str(tails(best)[1]),
            'opposite_at_least_two_positive_pools_probability':str(tails(other)[1]),
        }

    variance_checks = 0
    for n in (4,6,8):
        ordered=tuple((j,j+1) for j in range(0,n,2))
        for a in (
            [F(j+1,2*n+4) for j in range(n)],
            [F(n+2+j,2*n+4) for j in range(n)],
        ):
            vals=[variance_of_positive_pools(a,g) for g in partitions(tuple(range(n)),2)]
            val=variance_of_positive_pools(a,ordered)
            if max(a) <= F(1,2):
                assert val==max(vals)
            else:
                assert min(a)>= F(1,2) and val==min(vals)
            variance_checks+=len(vals)

    result={
        'schema_version':1,
        'method':'exact rational enumeration of partitions and independent infection states',
        'general_theorem_tested':False,
        'all_partition_tail_comparisons':comparisons,
        'all_partition_evaluations':enumerations,
        'direct_infection_state_pmf_comparisons':direct_comparisons,
        'pairwise_variance_extremum_partitions_checked':variance_checks,
        'cases':case_summary,
        'variance_reversal_examples':variance_reversal,
        'status':'finite_checks_passed',
        'limitation':'Finite enumeration is not a proof of the all-population theorem; see the mathematical majorization proof.',
    }
    return result


if __name__=='__main__':
    print(json.dumps(run(),sort_keys=True,indent=2))
