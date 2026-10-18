"""Exact, dependency-free checks for reciprocal-pair shell amplification."""
from collections import Counter
from itertools import product

BASE = 45045
FACTOR = ((3, 2), (5, 1), (7, 1), (11, 1), (13, 1))


def divisors_from_factorization(factorization):
    ds = [1]
    for prime, exp in factorization:
        ds = sorted(d * prime ** j for d in ds for j in range(exp + 1))
    return ds


def count_sums_dp(weights, target):
    dp = {0: 1}
    for w in weights:
        new = dp.copy()
        for value, count in dp.items():
            if value + w <= target:
                new[value + w] = new.get(value + w, 0) + count
        dp = new
    return dp.get(target, 0)


def subset_sums(weights):
    sums = Counter({0: 1})
    for weight in weights:
        plus = Counter({s + weight: c for s, c in sums.items()})
        sums += plus
    return sums


def make_internal(subset, pairs):
    return frozenset(d for i in subset for d in pairs[i])


def shell_representation(n, internal_list, selections):
    k = len(selections)
    if any(selections[j] != selections[k - 1 - j] for j in range(k)):
        raise ValueError('not a palindrome')
    return frozenset({1, n ** k}).union(
        *(frozenset(n ** j * d for d in internal_list[i]) for j, i in enumerate(selections))
    )


def verify():
    ds = divisors_from_factorization(FACTOR)
    assert len(ds) == 48 and ds[-1] == BASE
    assert sum(ds) == 104832
    assert sum(ds) - (BASE + 1) < 2 * BASE  # End pair is forced.
    pairs = [(d, BASE // d) for d in ds if 1 < d < BASE // d]
    assert len(pairs) == 23
    weights = [a + b for a, b in pairs]
    target = BASE - 1
    half = len(weights) // 2
    c0 = subset_sums(weights[:half])
    c1 = subset_sums(weights[half:])
    assert sum(c0[s] * c1[target - s] for s in c0) == 695
    assert count_sums_dp(weights, target) == 695  # Independently structured DP.

    # Collect three distinct admissible internal sets from an exhaustive
    # scan over 2^11 subsets and a lookup for the complementary half.
    right_map = {}
    for mask in range(1 << len(weights[half:])):
        s = sum(w for i, w in enumerate(weights[half:]) if mask & (1 << i))
        right_map.setdefault(s, []).append(mask)
    chosen = []
    for left in range(1 << half):
        lsum = sum(w for i, w in enumerate(weights[:half]) if left & (1 << i))
        for right in right_map.get(target - lsum, []):
            indexes = [i for i in range(half) if left & (1 << i)] + [half + i for i in range(len(weights[half:])) if right & (1 << i)]
            internal = make_internal(indexes, pairs)
            assert sum(internal) == target
            assert all((BASE // d) in internal for d in internal)
            chosen.append(internal)
            if len(chosen) >= 3:
                break
        if len(chosen) >= 3:
            break
    assert len(set(chosen)) == 3

    for k in range(1, 7):
        N = BASE ** k
        constructed = set()
        for choices in product(range(3), repeat=(k + 1) // 2):
            pal = tuple(choices[j] if j < len(choices) else choices[k - 1 - j] for j in range(k))
            T = shell_representation(BASE, chosen, pal)
            assert 1 in T and N in T
            assert sum(T) == 2 * N
            assert all(N % d == 0 for d in T)
            assert all((N // d) in T for d in T)
            constructed.add(T)
        assert len(constructed) == 3 ** ((k + 1) // 2)
    print('VERIFY_OK base=45045 internal_pairs=23 base_representations=695 independent_counts=2 sample_palindromic_shells_k=1..6')


if __name__ == '__main__':
    verify()
