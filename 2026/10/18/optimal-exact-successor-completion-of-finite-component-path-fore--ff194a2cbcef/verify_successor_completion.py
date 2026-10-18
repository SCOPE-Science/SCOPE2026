"""Finite symbolic verification of the exact-successor completion formula.

Four component types: F (finite path), A (omega), B (omega-star),
Z (bi-infinite).  All tests are finite checks of the endpoint cost lemma;
the all-cardinality theorem requires the written proof.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations_with_replacement, permutations

TYPES = "FABZ"


def endpoint_cost(left, right):
    # Left block has a maximum precisely in F,B;
    # right block has a minimum precisely in F,A.
    return int(left in "FB" and right in "FA")


def formula(word):
    return max(0, word.count("F") - word.count("Z") - 1)


def canonical_word(word):
    c = Counter(word)
    f, a, b, z = (c[t] for t in TYPES)
    if not f:
        return "A" * a + "Z" * z + "B" * b
    core = "F"
    for i in range(1, f):
        if i <= z:
            core += "Z"
        core += "F"
    return "A" * a + core + "Z" * max(0, z - (f - 1)) + "B" * b


def cost(word):
    return sum(endpoint_cost(a, b) for a, b in zip(word, word[1:]))


@lru_cache(None)
def dynamic_minimum(counts, previous):
    if not any(counts):
        return 0
    values = []
    for i, k in enumerate(counts):
        if not k:
            continue
        next_counts = counts[:i] + (k - 1,) + counts[i + 1 :]
        step = 0 if previous == "" else endpoint_cost(previous, TYPES[i])
        values.append(step + dynamic_minimum(next_counts, TYPES[i]))
    return min(values)


def main():
    tests = 0
    distinct_orders = 0
    for n in range(1, 10):
        for multiset in combinations_with_replacement(TYPES, n):
            tests += 1
            w = "".join(multiset)
            wanted = formula(w)
            representative = canonical_word(w)
            assert Counter(representative) == Counter(w)
            assert cost(representative) == wanted, (w, representative)
            dynamic = dynamic_minimum(tuple(w.count(t) for t in TYPES), "")
            assert dynamic == wanted, (w, dynamic, wanted)
            minimum = n
            for p in set(permutations(multiset)):
                distinct_orders += 1
                minimum = min(minimum, cost(p))
            assert minimum == wanted, (w, minimum, wanted)
    assert tests == 714
    print(f"checked {tests} component multisets and {distinct_orders} distinct block orders")
    print("SUCCESSOR_COMPLETION_VERIFY_OK")


if __name__ == "__main__":
    main()
