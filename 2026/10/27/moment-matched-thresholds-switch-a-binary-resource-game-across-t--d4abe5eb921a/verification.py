from fractions import Fraction as Q

RATIO = Q(19, 50)

def law(t):
    return (Q(2, 5) - t,
            Q(1, 10) + 3 * t,
            Q(3, 10) - 3 * t,
            Q(1, 5) + t)

def moments(t):
    p = law(t)
    support = (1, 2, 3, 4)
    mean = sum(pi * x for pi, x in zip(p, support))
    second = sum(pi * x * x for pi, x in zip(p, support))
    return mean, second, second - mean * mean

def regime(t):
    p1, p2, _, _ = law(t)
    if p2 < RATIO < p1:
        return "coordination"
    if p1 < RATIO and p2 < RATIO and RATIO < p1 + p2:
        return "prisoners_dilemma"
    if p1 < RATIO < p2:
        return "anti_coordination"
    return "boundary"

expected = (Q(23, 10), Q(67, 10), Q(141, 100))
points = (Q(0), Q(1, 50), Q(1, 20), Q(7, 75), Q(1, 10))
for t in points:
    p = law(t)
    assert sum(p) == 1
    assert min(p) >= 0
    assert moments(t) == expected

assert regime(Q(0)) == "coordination"
assert regime(Q(1, 50)) == "boundary"
assert regime(Q(1, 20)) == "prisoners_dilemma"
assert regime(Q(7, 75)) == "boundary"
assert regime(Q(1, 10)) == "anti_coordination"
print("Exact rational checks passed; symbolic proof in RESULT.md establishes the full intervals.")
