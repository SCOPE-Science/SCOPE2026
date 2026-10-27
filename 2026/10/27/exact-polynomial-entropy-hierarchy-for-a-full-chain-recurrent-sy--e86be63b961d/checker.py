"""Finite combinatorial checks for the two-transition symmetric-product entropy theorem.

All asymptotic and Hausdorff claims are proved analytically, not by this check.
"""
from itertools import product, combinations

def admissible_words(length):
    return [''.join(bits) for bits in product('01', repeat=length)
            if sum(bits[i] != bits[i+1] for i in range(length-1)) <= 2]

for length in range(1, 15):
    actual = len(admissible_words(length))
    expected = length * length - length + 2
    assert actual == expected, (length, actual, expected)
print('EXACT_WINDOW_COMPLEXITY_PASS', 14)

def local_word(start, stop, t, radius=2):
    return tuple(int(start <= i+t < stop) for i in range(-radius, radius + 1))

def profile(events, t):
    intervals = [(events[2*j], events[2*j+1]) for j in range(len(events)//2)]
    return tuple(local_word(a,b,t) for a,b in intervals)

def conspicuous(word):
    return len(set(word)) > 1

for k in range(1, 5):
    families = []
    for choices in product((0,1), repeat=2*k):
        events = tuple(10 + j*24 + 8*choices[j] for j in range(2*k))
        assert all(events[2*j] < events[2*j+1] for j in range(k))
        families.append(events)
    pairs = 0
    for a, b in combinations(families,2):
        distinct = set(a).symmetric_difference(b)
        assert distinct
        witnessed = False
        for t in distinct:
            pa=profile(a,t)
            pb=profile(b,t)
            if (any(map(conspicuous,pa)) and not any(map(conspicuous,pb))) or (any(map(conspicuous,pb)) and not any(map(conspicuous,pa))):
                witnessed=True
                break
        assert witnessed, (k,a,b)
        pairs+=1
    print('SYMMETRIC_PRODUCT_MARKER_SEPARATION_PASS',k,len(families),pairs)
print('INFINITE_TIME_ENTROPY_AND_QUOTIENT_TOPOLOGY_USE_ANALYTICAL_PROOF')
