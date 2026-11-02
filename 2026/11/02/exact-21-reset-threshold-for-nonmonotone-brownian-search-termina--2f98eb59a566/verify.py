"""Exact-rational certificate for the finite-reset Brownian turning-point threshold.

Only Python standard-library Fraction arithmetic is used for the proof checks.
"""
from fractions import Fraction as Q


def weighted_index(n, q):
    """Mean of j in {1,...,n}, with probabilities proportional to q**j."""
    s = Q(0)
    w = Q(0)
    p = q
    for j in range(1, n + 1):
        s += p
        w += j * p
        p *= q
    return w / s


def upper_log(q, terms=64):
    """Strict upper bound for -log(1-q), 0<q<1, in rational arithmetic.

    With s=q/(2-q), -log(1-q)=2*sum(k>=0) s**(2k+1)/(2k+1).
    Bound the tail from k=terms by a geometric series with its first
    denominator 2*terms+1.
    """
    s = q / (2 - q)
    sq = s * s
    p = s
    part = Q(0)
    for k in range(terms):
        part += p / (2 * k + 1)
        p *= sq
    tail_upper = p / ((2 * terms + 1) * (1 - sq))
    return 2 * (part + tail_upper)


def lower_log7(terms=7):
    """Strict rational lower bound for log 7 via artanh(3/4)."""
    s = Q(3, 4)
    sq = s * s
    p = s
    part = Q(0)
    for k in range(terms):
        part += p / (2 * k + 1)
        p *= sq
    return 2 * part


def certify_low_budget():
    """Show A_21(q)<2 for every 1/2<=q<=19/20.

    A_n(q)=(-log(1-q))*(1-q)*E_n(q)/q.
    The first factor (-log(1-q))*(1-q)/q decreases with q,
    while E_n(q) increases. On [a,b] it therefore suffices to show
    upper_log(a)*(1-a)/a*E_21(b)<2.
    """
    stack = [(Q(1, 2), Q(19, 20), 0)]
    nodes = leaves = max_depth = 0
    while stack:
        a, b, depth = stack.pop()
        nodes += 1
        bound = upper_log(a) * (1 - a) / a * weighted_index(21, b)
        if bound < 2:
            leaves += 1
            max_depth = max(max_depth, depth)
        else:
            assert depth < 11, "Exact interval coverage could not be certified"
            mid = (a + b) / 2
            stack.extend([(a, mid, depth + 1), (mid, b, depth + 1)])
    assert (nodes, leaves, max_depth) == (159, 80, 10)
    return nodes, leaves, max_depth


def certify_high_budget():
    """A_22(6/7)>2, using log 7>97/50 and rational index sums."""
    q = Q(6, 7)
    z_lower = lower_log7()
    assert z_lower > Q(97, 50)
    certificate = Q(97, 50) * (1 - q) / q * weighted_index(22, q)
    assert certificate > 2
    return z_lower, certificate


def main():
    nodes, leaves, depth = certify_low_budget()
    z_lower, certificate = certify_high_budget()
    print("PASS: exact rational cover", nodes, "nodes", leaves, "leaves", "maximum depth", depth)
    print("PASS: log(7) > 97/50; A_22(6/7) > 2, exact rational inequalities")
    print("PASS: all finite-budget cases follow by monotonicity in the allowed attempt count")


if __name__ == "__main__":
    main()
