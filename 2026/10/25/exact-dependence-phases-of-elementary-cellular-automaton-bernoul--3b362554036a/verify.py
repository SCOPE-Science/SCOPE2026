"""Reproduce an exact Bernoulli-image dependence classification for elementary binary cellular automata.

Requires Python 3.10+ and SymPy. Computes all 256 rules by exact rational
polynomials and checks 3-block disjointness directly at rational biases.
"""
from __future__ import annotations

import csv
from collections import Counter, defaultdict
from itertools import product
from fractions import Fraction
from pathlib import Path

from sympy import Poly, Rational, factor, gcd, solve, symbols

p = symbols('p')
B = (0, 1)


def output(rule: int, a: int, b: int, c: int) -> int:
    return (rule >> (4*a + 2*b + c)) & 1


def boundary_polynomials(rule: int) -> tuple[Poly, Poly]:
    """Conditional difference gcds: past vs last input; future vs first input.

    The four-state pair transducer proves that testing words of lengths
    0 through 3 suffices for infinite output half-lines; length 0 is zero.
    """
    lists = [[], []]
    for m in (1, 2, 3):
        past = defaultdict(lambda: [0, 0])
        future = defaultdict(lambda: [0, 0])
        for xs in product(B, repeat=m+2):
            word = tuple(output(rule, xs[i], xs[i+1], xs[i+2]) for i in range(m))
            k = sum(xs)
            weight = p**k * (1-p)**(m+2-k)
            past[word][xs[-1]] += weight
            future[word][xs[0]] += weight
        for tab, destination in ((past, lists[0]), (future, lists[1])):
            for joint0, joint1 in tab.values():
                difference = Poly((1-p)*joint1-p*joint0, p)
                if not difference.is_zero:
                    destination.append(difference)
    answer = []
    for polynomials in lists:
        current = polynomials[0] if polynomials else Poly(0, p)
        for g in polynomials[1:]:
            current = gcd(current, g)
        answer.append(current.monic() if not current.is_zero else current)
    return answer[0], answer[1]


def pair_differences(rule: int):
    right = sum(p**(a+b)*(1-p)**(2-a-b)
                * (output(rule,a,b,1)-output(rule,a,b,0))
                for a in B for b in B)
    left = sum(p**(b+c)*(1-p)**(2-b-c)
               * (output(rule,1,b,c)-output(rule,0,b,c))
               for b in B for c in B)
    return Poly(right,p), Poly(left,p)


def roots_inside(poly: Poly):
    if poly.is_zero:
        return None
    return {str(x) for x in solve(poly.as_expr(), p)
            if x.is_real and 0 < x < 1}


def direct_three_block_test(rule: int, numerator: int, denominator: int) -> bool:
    """Independent univariate fixed-bias check, not using the polynomial gcds.

    Simultaneously enumerate all joint six-output blocks at positions
    (0,1,2,4,5,6) from 9 independent input bits. Their two 3-block
    margins are independent iff this identity holds in exact integers.
    """
    joint = Counter()
    marg_a = Counter()
    marg_b = Counter()
    for xs in product(B, repeat=9):
        w = tuple(output(rule, xs[j], xs[j+1], xs[j+2])
                  for j in (0,1,2,4,5,6))
        k = sum(xs)
        weight = numerator**k * (denominator-numerator)**(9-k)
        joint[(w[:3], w[3:])] += weight
        marg_a[w[:3]] += weight
        marg_b[w[3:]] += weight
    normalization = denominator**9
    return all(joint[(a,b)] * normalization == marg_a[a]*marg_b[b]
               for a in product(B,repeat=3) for b in product(B,repeat=3))



def verify_rule22_witness():
    """Independent exact seven-bit count for two separated two-output events."""
    density = Fraction(1, 3)
    def event_probability(event):
        start = min(i-1 for i in event)
        stop = max(i+1 for i in event)
        result = Fraction(0)
        for xs in product(B, repeat=stop-start+1):
            if all(output(22, xs[i-1-start], xs[i-start], xs[i+1-start]) == v
                   for i, v in event.items()):
                count = sum(xs)
                result += density**count*(1-density)**(len(xs)-count)
        return result
    left_event = {-1: 0, 0: 0}
    right_event = {2: 0, 3: 0}
    a = event_probability(left_event)
    b = event_probability(right_event)
    ab = event_probability({**left_event, **right_event})
    assert (a, b, ab, ab-a*b) == (Fraction(29,81), Fraction(29,81),
                                  Fraction(97,729), Fraction(32,6561))


def main():
    generic = []
    fair = []
    generic_pairs = set()
    phase = defaultdict(set)
    rows = []
    for rule in range(256):
        past, future = boundary_polynomials(rule)
        always = past.is_zero or future.is_zero
        at_half = always or past.eval(Rational(1,2)) == 0 or future.eval(Rational(1,2)) == 0
        if always:
            generic.append(rule)
        if at_half:
            fair.append(rule)
        for g in (past, future):
            interior = roots_inside(g)
            assert interior is None or interior.issubset({'1/2'}), (rule, g)
        right, left = pair_differences(rule)
        pair_always = right.is_zero or left.is_zero
        if pair_always:
            generic_pairs.add(rule)
        for g in (right, left):
            interior = roots_inside(g)
            if interior:
                for root in interior:
                    phase[root].add(rule)
        rows.append({
            'rule': rule,
            'past_boundary_gcd': str(factor(past.as_expr())),
            'future_boundary_gcd': str(factor(future.as_expr())),
            'past_halfline_shield_all_biases': int(past.is_zero),
            'future_halfline_shield_all_biases': int(future.is_zero),
            'one_dependent_all_biases': int(always),
            'one_dependent_at_half': int(at_half),
            'pairwise_lag_two_all_biases': int(pair_always),
            'pairwise_lag_two_at_half': int(pair_always or (right.eval(Rational(1,2))*left.eval(Rational(1,2))==0)),
        })
    assert len(generic)==32, generic
    assert len(fair)==56, fair
    assert len(generic_pairs)==42, len(generic_pairs)
    expected_pairs = {
        '1/2':104, '1/3':48, '2/3':48,
        '-1/2 + sqrt(5)/2':56, '3/2 - sqrt(5)/2':56,
        '1 - sqrt(2)/2':46, 'sqrt(2)/2':46,
    }
    pair_counts = {root: len(generic_pairs|set(rules)) for root,rules in phase.items()}
    assert pair_counts == expected_pairs, pair_counts
    for numerator, denominator, expected in ((1,2,56),(1,3,32),(1,4,32),(2,3,32)):
        found = [r for r in range(256) if direct_three_block_test(r,numerator,denominator)]
        assert len(found)==expected, (numerator,denominator,len(found))
        if numerator*2==denominator:
            assert found==fair
        else:
            assert found==generic
    verify_rule22_witness()
    destination = Path(__file__).with_name('classification.csv')
    with destination.open('w',encoding='utf-8',newline='') as stream:
        writer=csv.DictWriter(stream,fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print('VERIFY_OK: 256 rules; one-dependent for every 0<p<1 exactly 32 rules;')
    print('at p=1/2 exactly 56 rules; no other exceptional one-dependence bias;')
    print('pairwise lag-2 independence generic 42, 7 exceptional biases:')
    print(pair_counts)
    print('independent 9-bit exact enumeration confirms 56/32/32/32 at 1/2,1/3,1/4,2/3;')
    print('Rule-22 p=1/3 block witness verified: covariance 32/6561;')
    print('classification CSV regenerated: 256 rows.')

if __name__=='__main__':
    main()
