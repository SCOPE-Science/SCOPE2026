#!/usr/bin/env python3
"""Reproducible independent finite tests for period-doubling scattered subsequences."""
from itertools import product


def word(rank):
    w = "0"
    for _ in range(rank):
        w = "".join("01" if c == "0" else "00" for c in w)
    return w


def subsequence(pattern, text):
    at = 0
    for char in text:
        if at < len(pattern) and char == pattern[at]:
            at += 1
    return at == len(pattern)


def expected(rank, number_ones):
    q = number_ones
    if rank % 2 == 0:
        return {"1" * (q + 1)}
    return {"1" * (q - 1) + "00", "1" * q + "0", "1" * (q + 1)}


def canonical_tests():
    for q in range(1, 10):
        U = "01" * q + "0"
        absent = {"".join(t) for t in product("01", repeat=q + 1)
                  if not subsequence("".join(t), U)}
        assert absent == {"1" * (q + 1)}, (q, "U")
    for q in range(2, 10):
        V = "01" * (q - 2) + "00101"
        absent = {"".join(t) for t in product("01", repeat=q + 1)
                  if not subsequence("".join(t), V)}
        assert absent == {"1" * (q - 1) + "00", "1" * q + "0", "1" * (q + 1)}, (q, "V")
        S = "1" + V
        assert all(subsequence("".join(t), S) for t in product("01", repeat=q + 1)), (q, "S")


def brute_prefix_tests():
    # Brute force every binary word at the two critical lengths.
    for k in range(1, 6):
        p = word(k)
        q = p.count("1")
        assert q == (2**k - (-1)**k) // 3
        assert all(subsequence("".join(t), p) for t in product("01", repeat=q))
        absent = {"".join(t) for t in product("01", repeat=q + 1)
                  if not subsequence("".join(t), p)}
        assert absent == expected(k, q), (k, absent, expected(k, q))


def count_shortest_absent_greedy(p, q):
    # Independent DP over greedy leftmost embeddings of present length-q patterns.
    n = len(p)
    nxt = [[n, n] for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        nxt[i] = nxt[i + 1].copy()
        nxt[i][int(p[i])] = i
    dp = {0: 1}
    for _ in range(q):
        following = {}
        for pos, count in dp.items():
            for c in (0, 1):
                j = nxt[pos][c]
                assert j < n  # q-universality of prefix implies no early failure
                following[j + 1] = following.get(j + 1, 0) + count
        dp = following
    assert sum(dp.values()) == 2**q
    return sum(count * sum(nxt[pos][c] == n for c in (0, 1))
               for pos, count in dp.items())


def large_prefix_tests():
    for k in range(1, 12):
        p = word(k)
        q = p.count("1")
        assert q == (2**k - (-1)**k) // 3
        assert p.startswith("0") and "11" not in p
        if k % 2 == 0:
            assert p.endswith("00")
            assert subsequence("01" * q + "0", p)
        elif k >= 3:
            assert p.endswith("01000101")
            assert subsequence("01" * (q - 2) + "00101", p)
        assert count_shortest_absent_greedy(p, q) == (1 if k % 2 == 0 else 3)
        assert all(not subsequence(s, p) for s in expected(k, q))


if __name__ == "__main__":
    canonical_tests()
    brute_prefix_tests()
    large_prefix_tests()
    print("PASS: canonical witnesses q=1..9; full binary enumeration ranks 1..5; "
          "greedy-DP counts and predicted strings ranks 1..11")
