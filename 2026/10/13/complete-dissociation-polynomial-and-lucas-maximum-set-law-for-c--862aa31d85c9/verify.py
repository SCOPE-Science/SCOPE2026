#!/usr/bin/env python3
"""Exact integer verification of cyclic prism dissociation identities."""
from collections import Counter, defaultdict
from itertools import product

STATES = tuple(range(4))
WEIGHT = (0, 1, 1, 2)


def legal(a, b, c):
    if b == 3:
        return a == 0 and c == 0
    if b == 1:
        return not (a & 1 and c & 1)
    if b == 2:
        return not (a & 2 and c & 2)
    return True


def cyclic_trace(n):
    """Trace of the weighted 16-state two-column transition to power n."""
    if n <= 2:
        answer = Counter()
        for word in product(STATES, repeat=n):
            if all(legal(word[(i - 1) % n], word[i],
                         word[(i + 1) % n]) for i in range(n)):
                answer[sum(WEIGHT[a] for a in word)] += 1
        return answer
    answer = Counter()
    for a, b in product(STATES, repeat=2):
        counts = {(a, b, WEIGHT[a] + WEIGHT[b]): 1}
        for _ in range(2, n):
            updated = defaultdict(int)
            for (last2, last1, degree), count in counts.items():
                for c in STATES:
                    if legal(last2, last1, c):
                        updated[(last1, c, degree + WEIGHT[c])] += count
            counts = updated
        for (last2, last1, degree), count in counts.items():
            if legal(last2, last1, a) and legal(last1, a, b):
                answer[degree] += count
    return answer


def brute(n):
    """Exhaust all 2^(2n) vertex subsets using the actual prism edges."""
    nbrs = [0] * (2 * n)
    for i in range(n):
        for row in range(2):
            v = 2 * i + row
            for w in (2 * ((i - 1) % n) + row,
                      2 * ((i + 1) % n) + row,
                      2 * i + 1 - row):
                nbrs[v] |= 1 << w
    ans = Counter()
    for chosen in range(1 << (2 * n)):
        rest = chosen
        valid = True
        while rest:
            low = rest & -rest
            v = low.bit_length() - 1
            if (nbrs[v] & chosen).bit_count() > 1:
                valid = False
                break
            rest -= low
        if valid:
            ans[chosen.bit_count()] += 1
    return ans


def pmul(a, b):
    out = defaultdict(int)
    for i, x in a.items():
        for j, y in b.items():
            out[i + j] += x * y
    return {j: v for j, v in out.items() if v}


def candidate_determinant():
    """Q(t,z)=(1+tz+t^2 z^2)(1-(1+z)t-(z+2z^2)t^2+(z^3-z^2)t^3+z^4t^4)."""
    first = {0: {0: 1}, 1: {1: 1}, 2: {2: 1}}
    second = {0: {0: 1}, 1: {0: -1, 1: -1},
              2: {1: -1, 2: -2}, 3: {2: -1, 3: 1},
              4: {4: 1}}
    result = defaultdict(lambda: defaultdict(int))
    for i, a in first.items():
        for j, b in second.items():
            for deg, value in pmul(a, b).items():
                result[i + j][deg] += value
    return {k: {j: v for j, v in poly.items() if v}
            for k, poly in result.items()}


def determinant_certificate():
    """Newton identities reconstruct det(I-tT) from exact traces, no CAS."""
    p = [None] + [dict(cyclic_trace(n)) for n in range(1, 17)]
    q = [{0: 1}]
    for k in range(1, 17):
        numerator = defaultdict(int)
        for i in range(1, k + 1):
            for deg, val in pmul(q[k - i], p[i]).items():
                numerator[deg] -= val
        assert all(v % k == 0 for v in numerator.values()), k
        q.append({deg: val // k for deg, val in numerator.items() if val})
    expected = candidate_determinant()
    for k in range(17):
        assert q[k] == expected.get(k, {}), (k, q[k], expected.get(k, {}))
    return q


def max_count(n):
    luc_a, luc_b = 2, 1
    for _ in range(n):
        luc_a, luc_b = luc_b, luc_a + luc_b
    return luc_a + (2 if n % 3 == 0 else -1) + (2 if n % 2 == 0 else 0)


def main():
    determinant_certificate()
    total = 0
    for n in range(3, 11):
        actual = brute(n)
        total += 1 << (2 * n)
        expected = cyclic_trace(n)
        assert actual == expected, (n, actual, expected)
    for n in range(3, 41):
        polynomial = cyclic_trace(n)
        assert max(polynomial) == n, n
        assert polynomial[n] == max_count(n), (n, polynomial[n], max_count(n))
    print("VERIFY_OK determinant_degree_t=6 exact_Newton_orders=1..16"
          " brute_orders=3..10 vertex_subsets=" + str(total) +
          " all_coefficients_and_Lucas_maximum_orders=3..40")


if __name__ == "__main__":
    main()
