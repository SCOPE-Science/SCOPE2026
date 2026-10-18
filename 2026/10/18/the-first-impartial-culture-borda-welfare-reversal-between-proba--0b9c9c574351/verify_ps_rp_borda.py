"""Exact two-method reproducibility check for finite probabilistic-serial rank welfare.

Requires Python 3.9+ standard library. Running this file prints a canonical JSON certificate.
"""
from collections import Counter
from fractions import Fraction as Q
from functools import lru_cache
from itertools import permutations, product
from math import factorial
import json


def ps_matrix(profile):
    n = len(profile)
    capacity = [Q(1)] * n
    assignment = [[Q(0)] * n for _ in range(n)]
    while any(capacity):
        demand = [next(j for j in pref if capacity[j]) for pref in profile]
        counts = Counter(demand)
        interval = min(capacity[j] / count for j, count in counts.items())
        for i, j in enumerate(demand):
            assignment[i][j] += interval
        for j, count in counts.items():
            capacity[j] -= interval * count
    return assignment


def rp_matrix(profile):
    n = len(profile)
    assignment = [[0] * n for _ in range(n)]
    for priority in permutations(range(n)):
        remaining = (1 << n) - 1
        for i in priority:
            j = next(j for j in profile[i] if (remaining >> j) & 1)
            remaining &= ~(1 << j)
            assignment[i][j] += 1
    return [[Q(x, factorial(n)) for x in row] for row in assignment]


def borda(assignment, profile):
    n = len(profile)
    return sum(assignment[i][j] * (n - r - 1)
               for i, order in enumerate(profile) for r, j in enumerate(order))


def delta_matrix(profile):
    return borda(ps_matrix(profile), profile) - borda(rp_matrix(profile), profile)


def delta_independent(profile):
    """Independent PS time-integral and RP Bellman recursion (no assignment matrices)."""
    n = len(profile)
    scores = [{j: n - r - 1 for r, j in enumerate(order)} for order in profile]
    available = {j: Q(1) for j in range(n)}
    ps_total = Q(0)
    while available:
        demanded = [next(j for j in order if j in available) for order in profile]
        counts = Counter(demanded)
        interval = min(available[j] / num for j, num in counts.items())
        ps_total += interval * sum(scores[i][j] for i, j in enumerate(demanded))
        for j, num in counts.items():
            available[j] -= interval * num
            if not available[j]:
                del available[j]

    @lru_cache(None)
    def value(agents, objects):
        if agents == 0:
            return Q(0)
        choices = []
        for i in range(n):
            if agents & (1 << i):
                j = next(j for j in profile[i] if objects & (1 << j))
                choices.append(scores[i][j] + value(agents ^ (1 << i), objects ^ (1 << j)))
        return sum(choices) / len(choices)

    return ps_total - value((1 << n) - 1, (1 << n) - 1)


def census(n):
    prefs = list(permutations(range(n)))
    multiplicity = factorial(n)
    histogram_a = Counter()
    histogram_b = Counter()
    for tail in product(prefs, repeat=n - 1):
        p = (prefs[0],) + tail
        a = delta_matrix(p)
        b = delta_independent(p)
        assert a == b, (n, p, a, b)
        histogram_a[a] += multiplicity
        histogram_b[b] += multiplicity
    assert histogram_a == histogram_b
    assert sum(histogram_a.values()) == factorial(n) ** n
    return histogram_a


def summary(hist):
    counts = {"negative": sum(c for v, c in hist.items() if v < 0),
              "zero": hist[Q(0)],
              "positive": sum(c for v, c in hist.items() if v > 0)}
    total = sum(v * c for v, c in hist.items())
    return {"sign_counts": counts, "total_delta": str(total),
            "mean_delta": str(total / sum(hist.values())),
            "histogram": {str(v): hist[v] for v in sorted(hist)}}


def main():
    data = {str(n): summary(census(n)) for n in (2, 3, 4)}
    assert data["2"]["sign_counts"] == {"negative": 0, "zero": 4, "positive": 0}
    assert data["3"]["sign_counts"] == {"negative": 36, "zero": 180, "positive": 0}
    assert data["3"]["mean_delta"] == "-1/72"
    assert data["4"]["sign_counts"] == {"negative": 115200, "zero": 129168, "positive": 87408}
    assert data["4"]["mean_delta"] == "1283/62208"
    positive = ((0, 1, 2, 3), (0, 3, 2, 1), (2, 1, 0, 3), (2, 3, 0, 1))
    negative = ((0, 1, 2, 3), (0, 2, 1, 3), (1, 0, 3, 2), (3, 0, 1, 2))
    assert delta_matrix(positive) == Q(1) == delta_independent(positive)
    assert delta_matrix(negative) == Q(-1, 3) == delta_independent(negative)
    data["four_agent_witnesses"] = {"positive": {"profile": positive, "delta": "1"},
                                    "negative": {"profile": negative, "delta": "-1/3"}}
    print(json.dumps(data, ensure_ascii=False, sort_keys=True, separators=(',', ':')))


if __name__ == "__main__":
    main()
