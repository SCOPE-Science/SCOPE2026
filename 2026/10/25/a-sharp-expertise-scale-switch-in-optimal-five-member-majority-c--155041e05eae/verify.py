"""Exact verification for five-member majority committee assignment."""
from fractions import Fraction as F
from itertools import combinations, product
from math import prod
import json

ABILITIES = (1, 2, 3, 4, 5, 6, 7, 8, 11, 15)
LOW = ((0, 1, 3, 8, 9), (2, 4, 5, 6, 7))
HIGH = ((0, 1, 2, 8, 9), (3, 4, 5, 6, 7))


def elementary_three(values):
    return sum(prod(t) for t in combinations(values, 3))


def majority(values):
    n = len(values)
    z = F(0)
    for state in product((0, 1), repeat=n):
        if sum(state) > n // 2:
            z += prod(p if bit else 1-p for p, bit in zip(values, state))
    return z


def score(part):
    a = sum(elementary_three([ABILITIES[i] for i in group]) for group in part)
    b = sum(prod(ABILITIES[i] for i in group) for group in part)
    return a, b


def partitions():
    for left in combinations(range(10), 5):
        if 0 not in left:
            continue
        right = tuple(i for i in range(10) if i not in left)
        yield left, right


def expected_formula(q):
    if len(q) == 3:
        return F(1,2)+sum(q)/2-2*prod(q)
    if len(q) == 5:
        return F(1,2)+F(3,8)*sum(q)-F(1,2)*elementary_three(q)+6*prod(q)
    raise ValueError(len(q))


def main():
    interpolation_checks = 0
    for n in (3,5):
        for sample in product((F(0), F(1,4)), repeat=n):
            assert majority(tuple(F(1,2)+q for q in sample)) == expected_formula(sample)
            interpolation_checks += 1
    all_parts = list(partitions())
    assert len(all_parts) == 126 and len(set(all_parts)) == 126
    scored = {part: score(part) for part in all_parts}
    assert scored[LOW] == (3346,6360)
    assert scored[HIGH] == (3352,7710)
    t = F(1,2700)
    nodes = (F(0),t,F(1,900))
    # Piecewise affine lower envelopes: the following three nodes suffice.
    margins = []
    for u in nodes:
        total = {p:F(a)-12*u*b for p,(a,b) in scored.items()}
        best = min(total.values())
        opt = tuple(sorted(p for p,v in total.items() if v == best))
        expected = ((LOW,), (LOW,HIGH), (HIGH,))[len(margins)]
        assert set(opt) == set(expected), (u,opt)
        noncandidate = [v-best for p,v in total.items() if p not in (LOW,HIGH)]
        margin = min(noncandidate)
        assert margin > 0
        margins.append(str(margin))
    assert margins == ['36','112/3','52'], margins
    winners = {}
    probability_checks = 0
    for s,wanted in ((F(1,60), LOW), (F(1,32),HIGH)):
        values = {p:F(a)-12*s*s*b for p,(a,b) in scored.items()}
        optimum = min(values.values())
        assert [p for p,z in values.items() if z==optimum] == [wanted]
        winners[str(s)] = [list(map(lambda g: [i+1 for i in g],wanted)), str(optimum)]
        probabilities = tuple(F(1,2)+s*a for a in ABILITIES)
        assert all(F(1,2)<p<1 for p in probabilities)
        for left,right in all_parts:
            direct = majority(tuple(probabilities[i] for i in left))+majority(tuple(probabilities[i] for i in right))
            a,b = scored[(left,right)]
            formula = F(1)+F(3,8)*s*sum(ABILITIES)-F(1,2)*s**3*a+6*s**5*b
            assert direct == formula
            probability_checks += 1
    cert={
        'source_parameters':list(ABILITIES),
        'number_of_unordered_partitions':len(all_parts),
        'interpolation_checks':interpolation_checks,
        'direct_five_vote_probability_checks':probability_checks,
        'low_partition_one_based':[[i+1 for i in group] for group in LOW],
        'high_partition_one_based':[[i+1 for i in group] for group in HIGH],
        'low_A_B':list(scored[LOW]),'high_A_B':list(scored[HIGH]),
        'switch_squared_scale':'1/2700',
        'least_other_partition_margins_at_0_switch_endpoint':margins,
        'representative_scales':winners,
        'result':'all_exact_checks_passed',
    }
    print(json.dumps(cert,ensure_ascii=False,sort_keys=True,indent=2))

if __name__=='__main__':main()
