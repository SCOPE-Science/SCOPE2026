"""Exact rational verification for diagonal pinned-row Kaczmarz theorem.
Run using: python verify.py
All assertions are finite checks; the theorem itself is proved analytically in RESULT.md.
"""
from fractions import Fraction as Q
from itertools import combinations, combinations_with_replacement, product

checks = 0

def assert_equal(actual, expected):
    global checks
    assert actual == expected, (actual, expected)
    checks += 1


def contraction_rate(weights, indices):
    w = [weights[i] for i in indices]
    return Q(1) - Q(min(w), sum(w))


def coupon_expectation(weights, indices):
    w = [weights[i] for i in indices]
    s = sum(w)
    return sum(((-1)**(r+1)*Q(s, sum(j))
                for r in range(1, len(w)+1)
                for j in combinations(w, r)), Q(0))


def coupon_cdf(weights, indices, t):
    w = [weights[i] for i in indices]
    p = [Q(v, sum(w)) for v in w]
    return sum(((-1)**r*(1-sum(p[i] for i in j))**t
                for r in range(len(w)+1)
                for j in combinations(range(len(w)), r)), Q(0))

# Exhaustive consecutive-block optimality of the *sharp* rate, including ties.
for n in range(3, 8):
    for weights in combinations_with_replacement(range(1, 8), n):
        for k in range(2, n):
            subsets = tuple(combinations(range(n), k))
            best = min(contraction_rate(weights, I) for I in subsets)
            sliding_best = min(contraction_rate(weights, tuple(range(j, j+k)))
                               for j in range(n-k+1))
            assert_equal(best, sliding_best)
            if len(set(weights)) == n:
                assert_equal(all(I == tuple(range(I[0], I[0]+k))
                                 for I in subsets if contraction_rate(weights, I) == best), True)

# Direct enumeration of short independent sampling sequences: exact residual and completion probabilities.
for weights in ((1, 2, 3), (2, 3, 6, 8), (1, 1, 4, 5), (1, 4, 9, 16)):
    n = len(weights)
    for k in range(2, n+1):
        for I in combinations(range(n), k):
            p = {i:Q(weights[i], sum(weights[j] for j in I)) for i in I}
            initial_sq = {i:Q(1+i, 2+i) for i in I}
            for t in range(5):
                exact_residual = Q(0)
                exact_completion = Q(0)
                for seq in product(I, repeat=t):
                    probability = Q(1)
                    for i in seq: probability *= p[i]
                    visited = set(seq)
                    exact_residual += probability*sum(initial_sq[i] for i in I if i not in visited)
                    if len(visited) == k: exact_completion += probability
                formula_residual = sum(initial_sq[i]*(1-p[i])**t for i in I)
                assert_equal(exact_residual, formula_residual)
                assert_equal(exact_completion, coupon_cdf(weights, I, t))

# Four-site exact rational disagreement of sharp contraction and mean completion.
w = (2, 3, 6, 8)
I_rate = (0, 1, 2)
I_completion = (1, 2, 3)
assert_equal(contraction_rate(w, I_rate), Q(9, 11))
assert_equal(contraction_rate(w, I_completion), Q(14, 17))
assert_equal(coupon_expectation(w, I_rate), Q(2593, 360))
assert_equal(coupon_expectation(w, I_completion), Q(38677, 5544))
assert_equal(min(combinations(range(4),3),key=lambda I:contraction_rate(w,I)),I_rate)
assert_equal(min(combinations(range(4),3),key=lambda I:coupon_expectation(w,I)),I_completion)

# Minimal three-coordinate family with exact small-mode obstruction to Frobenius pivoting.
for j in range(3, 81):
    eps2=Q(1,j*j)
    weights=(eps2,Q(1),Q(4))
    opt=Q(4,5)
    proxy=Q(1,1+eps2)
    assert_equal(contraction_rate(weights,(1,2)),opt)
    assert_equal(contraction_rate(weights,(0,1)),proxy)
    assert_equal(all(contraction_rate(weights,(1,2))<contraction_rate(weights,I)
                     for I in ((0,1),(0,2))),True)
    # Global Frobenius-residual minimizer pins the largest weight (last index).
    assert_equal(min(range(3),key=lambda j:sum(weights[i] for i in range(3) if i!=j)),2)
    assert_equal(Q(1,5)/Q(eps2,1+eps2), (1+eps2)/(5*eps2))

print(f"PASS: {checks} exact rational assertions")
