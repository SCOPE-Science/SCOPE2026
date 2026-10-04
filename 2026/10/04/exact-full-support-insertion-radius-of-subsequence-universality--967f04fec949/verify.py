#!/usr/bin/env python3
from itertools import product, combinations


def alphabet_size(block):
    return len(set(block))


def best_partition_coverage(word, k, q):
    """Maximum sum of distinct-symbol counts over k contiguous blocks; empty blocks allowed."""
    n = len(word)
    neg = -10**9
    dp = [neg] * (n + 1)
    dp[0] = 0
    for _ in range(k):
        ndp = [neg] * (n + 1)
        for i in range(n + 1):
            if dp[i] == neg:
                continue
            # empty next block
            if dp[i] > ndp[i]:
                ndp[i] = dp[i]
            seen = set()
            for j in range(i + 1, n + 1):
                seen.add(word[j - 1])
                cand = dp[i] + len(seen)
                if cand > ndp[j]:
                    ndp[j] = cand
        dp = ndp
    return dp[n]


def insertion_distance_partition(word, k, q):
    return q * k - best_partition_coverage(word, k, q)


def subsequences_of_length(word, k):
    return {tuple(word[i] for i in idx) for idx in combinations(range(len(word)), k)}


def is_k_universal(word, k, q):
    if k == 0:
        return True
    return len(subsequences_of_length(word, k)) == q ** k


def is_subsequence(shorter, longer):
    it = iter(longer)
    return all(any(y == x for y in it) for x in shorter)


def insertion_distance_literal(word, k, q):
    """Tiny-instance definition check: enumerate all supersequences up to the shortest possible universal length."""
    n = len(word)
    for length in range(n, q * k + n + 1):
        for target in product(range(q), repeat=length):
            if not is_subsequence(word, target):
                continue
            if is_k_universal(target, k, q):
                return length - n
    raise AssertionError("literal search failed")


def predicted_radius(q, n, k):
    return max(q * k - n, (q - 1) * (k - 1))


def witness(q, n):
    return (0,) * (n - q + 1) + tuple(range(1, q))


def check_literal_vs_partition():
    cases = 0
    for q, max_n, max_k in [(2, 5, 3), (3, 4, 2)]:
        for n in range(q, max_n + 1):
            for k in range(1, max_k + 1):
                for word in product(range(q), repeat=n):
                    if len(set(word)) != q:
                        continue
                    a = insertion_distance_partition(word, k, q)
                    b = insertion_distance_literal(word, k, q)
                    assert a == b, (q, n, k, word, a, b)
                    cases += 1
    return cases


def check_exhaustive_radius():
    cases = 0
    words_checked = 0
    for q, n_max, k_max in [(2, 9, 5), (3, 7, 4), (4, 6, 3)]:
        for n in range(q, n_max + 1):
            full = [w for w in product(range(q), repeat=n) if len(set(w)) == q]
            for k in range(1, k_max + 1):
                distances = [insertion_distance_partition(w, k, q) for w in full]
                got = max(distances)
                want = predicted_radius(q, n, k)
                assert got == want, (q, n, k, got, want)
                wstar = witness(q, n)
                assert insertion_distance_partition(wstar, k, q) == want
                # The coverage lemma used in the proof is checked objectwise here.
                lower_cov = min(n, q + k - 1)
                for w in full:
                    assert best_partition_coverage(w, k, q) >= lower_cov
                cases += 1
                words_checked += len(full)
    return cases, words_checked


def check_witness_symbolic_grid():
    cases = 0
    for q in range(2, 13):
        for n in range(q, q + 18):
            w = witness(q, n)
            for k in range(1, 13):
                # Direct DP on the extremal family, compared with the closed form.
                assert insertion_distance_partition(w, k, q) == predicted_radius(q, n, k)
                cases += 1
    return cases


def main():
    literal = check_literal_vs_partition()
    radius_cases, words = check_exhaustive_radius()
    witness_cases = check_witness_symbolic_grid()
    print(
        "VERIFY_OK "
        f"literal_cases={literal} exhaustive_parameter_cases={radius_cases} "
        f"full_support_words_checked={words} witness_grid_cases={witness_cases}"
    )


if __name__ == "__main__":
    main()
