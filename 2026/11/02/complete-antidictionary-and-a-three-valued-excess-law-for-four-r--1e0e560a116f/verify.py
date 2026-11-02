"""Independent finite checks for an exact four-run binary antidictionary theorem.

Usage: python3 verify.py
Pure Python 3, no third-party dependencies.
"""
from itertools import product
from collections import Counter
import random


def proposed_families(a, b, c, d):
    assert min(a, b, c, d) >= 1
    sets = [
        {'0' * (max(a, c) + 1), '1' * (max(b, d) + 1)},
        {'0' + '1' * t + '0' for t in range(1, b)},
        {'1' + '0' * t + '1' for t in range(1, c)},
    ]
    extra = []
    if b < d:
        extra.append('1' * (b + 1) + '0')
    if c < a:
        extra.append('1' + '0' * (c + 1))
    if (a-c)*(b-d) < 0:
        extra.append('0' * (min(a,c)+1) + '1' * (min(b,d)+1))
    if a < c and b <= d:
        extra.append('0' * (a+1) + '1' * b + '0')
    if c <= a and d < b:
        extra.append('1' + '0' * c + '1' * (d+1))
    if c <= a and b <= d:
        extra.append('1' + '0' * c + '1' * b + '0')
    sets.extend({x} for x in extra)
    return sets


def literal_maws(a, b, c, d):
    w = '0'*a+'1'*b+'0'*c+'1'*d
    fac = {w[i:j] for i in range(len(w)) for j in range(i+1,len(w)+1)}
    result = set()
    # By the prefix-suffix definition, every MAW is alpha + factor + beta,
    # where the middle factor may be empty. This loops over all such candidates.
    for v in fac | {''}:
        for alpha in '01':
            for beta in '01':
                word = alpha + v + beta
                if word in fac:
                    continue
                if v:
                    present = (alpha+v in fac and v+beta in fac)
                else:
                    present = (alpha in fac and beta in fac)
                if present:
                    result.add(word)
    return result


def offset(a,b,c,d):
    return (int(b<d)+int(c<a)+int((a-c)*(b-d)<0)
            +int(a<c and b<=d)+int(c<=a and d<b)
            +int(c<=a and b<=d))


def expected_offset(a,b,c,d):
    if a>c and b<d:
        return 4
    if a<=c and b>=d:
        return 1
    return 2


def verify():
    count = total_maws = sum_lengths = 0
    for a,b,c,d in product(range(1,9),repeat=4):
        families = proposed_families(a,b,c,d)
        predicted = set().union(*families)
        assert len(predicted) == sum(map(len,families)), (a,b,c,d,'duplicate family')
        actual = literal_maws(a,b,c,d)
        assert predicted == actual, (a,b,c,d,predicted-actual,actual-predicted)
        assert len(actual) == b+c+offset(a,b,c,d)
        assert offset(a,b,c,d) == expected_offset(a,b,c,d)
        assert Counter(map(len,predicted)) == Counter(map(len,actual))
        count += 1
        total_maws += len(actual)
        sum_lengths += sum(map(len,actual))
    rng=random.Random(20260228)
    large_count=0
    for _ in range(120):
        a,b,c,d = (rng.randrange(1,31) for __ in range(4))
        expected=set().union(*proposed_families(a,b,c,d))
        observed=literal_maws(a,b,c,d)
        assert expected==observed,(a,b,c,d,expected-observed,observed-expected)
        large_count += 1
    # All 9 comparison combinations realized to check the indicator trichotomy.
    categories={}
    for a,b,c,d in product(range(1,4),repeat=4):
        key=('<' if a<c else '>' if a>c else '=', '<' if b<d else '>' if b>d else '=')
        categories.setdefault(key,expected_offset(a,b,c,d))
    assert len(categories)==9 and set(categories.values())=={1,2,4}
    print('VERIFY_OK exhaustive_quadruples=%d verified_maws=%d total_maw_lengths=%d larger_quadruples=%d comparison_regions=%d offset_values=%s' %
          (count,total_maws,sum_lengths,large_count,len(categories),sorted(set(categories.values()))))

if __name__=='__main__':
    verify()
