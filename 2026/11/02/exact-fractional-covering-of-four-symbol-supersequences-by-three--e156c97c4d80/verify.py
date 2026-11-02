"""Exact rational checks for the fractional one-insertion covering certificates."""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product


def shadow(received):
    """Distinct one-deletion descendants, not a multiset."""
    return {received[:i] + received[i + 1:] for i in range(len(received))}


def center_type(w):
    a, b, c = w
    if a == b == c:
        return "A"
    if a == b or b == c:
        return "B"
    if a == c:
        return "C"
    return "D"


def primal_weight(w):
    t = center_type(w)
    return {"A": Fraction(1), "B": Fraction(1, 2),
            "C": Fraction(1, 4), "D": Fraction(1, 4)}[t]


def dual_weight(z, q):
    a, b, c, d = z
    if a == b == c == d:
        return Fraction(1)
    if a == b and c == d and a != c:
        return Fraction(1)
    if a == d and len(set(z)) == 3:
        return Fraction(1, 2 * (q - 2))
    if len(set(z)) == 4:
        return Fraction(1, 4 * (q - 2))
    return Fraction(0)


def canonical_pattern(z):
    relabel = {}
    return tuple(relabel.setdefault(v, len(relabel)) for v in z)


def verify_patterns():
    patterns = sorted({canonical_pattern(z) for z in product(range(4), repeat=4)})
    assert len(patterns) == 15
    profiles = {}
    for p in patterns:
        counts = Counter(center_type(w) for w in shadow(p))
        profile = tuple(counts[t] for t in "ABCD")
        assert sum(primal_weight(w) for w in shadow(p)) >= 1
        profiles[p] = profile
    assert len(set(profiles.values())) == 10
    expected = {
        (0, 0, 0, 0): (1, 0, 0, 0),
        (0, 0, 0, 1): (1, 1, 0, 0),
        (0, 0, 1, 0): (1, 1, 1, 0),
        (0, 0, 1, 1): (0, 2, 0, 0),
        (0, 0, 1, 2): (0, 2, 0, 1),
        (0, 1, 0, 1): (0, 2, 2, 0),
        (0, 1, 0, 2): (0, 1, 1, 2),
        (0, 1, 1, 0): (0, 2, 1, 0),
        (0, 1, 2, 0): (0, 0, 2, 2),
        (0, 1, 2, 3): (0, 0, 0, 4),
    }
    for p, count in expected.items():
        assert profiles[p] == count, (p, profiles[p], count)
    print("equality patterns: 15, distinct incidence profiles: 10")


def verify_q(q):
    centers = list(product(range(q), repeat=3))
    received = list(product(range(q), repeat=4))
    superseq = defaultdict(set)
    dual_total = Fraction(0)
    for z in received:
        outputs = shadow(z)
        assert sum((primal_weight(w) for w in outputs), Fraction(0)) >= 1
        dual_total += dual_weight(z, q)
        for w in outputs:
            superseq[w].add(z)
    primal_total = Fraction(0)
    for w in centers:
        primal_total += primal_weight(w)
        assert sum((dual_weight(z, q) for z in superseq[w]), Fraction(0)) == 1
    exact = Fraction(q * (q + 1) ** 2, 4)
    assert primal_total == dual_total == exact, (q, primal_total, dual_total)
    print("alphabet", q, "optimum", exact, "centers", len(centers),
          "receivers", len(received))


def verify_binary():
    alphabet = range(2)
    centers = list(product(alphabet, repeat=3))
    received = list(product(alphabet, repeat=4))
    covering = {(0, 0, 0), (0, 1, 1), (1, 0, 0), (1, 1, 1)}
    dual_support = {(0, 0, 0, 0), (1, 1, 1, 1),
                    (0, 0, 1, 1), (1, 1, 0, 0)}
    assert all(shadow(z) & covering for z in received)
    assert all(sum(w in shadow(z) for z in dual_support) <= 1 for w in centers)
    assert len(covering) == len(dual_support) == 4
    print("binary boundary optimum 4")


if __name__ == "__main__":
    verify_patterns()
    verify_binary()
    for alphabet_size in range(3, 10):
        verify_q(alphabet_size)
    print("VERIFY_OK")
