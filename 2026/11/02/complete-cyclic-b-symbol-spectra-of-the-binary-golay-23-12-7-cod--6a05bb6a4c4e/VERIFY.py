"""Independent exhaustive check using polynomial division and direct windows.

Requires Python 3 standard library. From this directory: python VERIFY.py
"""
import csv
from collections import Counter

N = 23
K = 12
G = 0xC75
MASK = (1 << N) - 1


def polynomial_remainder(polynomial, divisor):
    while polynomial and polynomial.bit_length() >= divisor.bit_length():
        polynomial ^= divisor << (polynomial.bit_length() - divisor.bit_length())
    return polynomial


def systematic_word(message):
    shifted = message << (N - K)
    return shifted ^ polynomial_remainder(shifted, G)


def direct_weight(word, b):
    bits = tuple((word >> i) & 1 for i in range(N))
    return sum(any(bits[(i + j) % N] for j in range(b)) for i in range(N))


def direct_run_partition(word):
    if word == 0:
        return "ALL_ZERO"
    if word == MASK:
        return "ALL_ONE"
    runs = []
    for i in range(N):
        if (word >> i) & 1:
            continue
        if not (word >> ((i - 1) % N)) & 1:
            continue
        k = 0
        while not ((word >> ((i + k) % N)) & 1):
            k += 1
        runs.append(k)
    return ".".join(map(str, sorted(runs, reverse=True)))


def rotate(word, steps):
    return ((word << steps) | (word >> (N - steps))) & MASK if steps else word


def verify():
    with open("B_SYMBOL_SPECTRA.csv", newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    assert len(rows) == N
    given = {int(row["b"]): tuple(int(row[f"A_{j}"]) for j in range(N + 1)) for row in rows}
    assert set(given) == set(range(1, N + 1))
    with open("ZERO_RUN_CENSUS.csv", newline="", encoding="utf-8") as f:
        runs = list(csv.DictReader(f))
    expected_parts = {r["zero_run_partition"]: int(r["number_of_codewords"]) for r in runs}
    assert len(runs) == len(expected_parts) == 81
    assert expected_parts["ALL_ZERO"] == expected_parts["ALL_ONE"] == 1
    assert sum(expected_parts.values()) == (1 << K)
    assert sum(v for k, v in expected_parts.items() if k not in ("ALL_ZERO", "ALL_ONE")) == 4094
    assert all(v % N == 0 for k, v in expected_parts.items() if k not in ("ALL_ZERO", "ALL_ONE"))
    assert polynomial_remainder((1 << N) ^ 1, G) == 0
    words = [systematic_word(m) for m in range(1 << K)]
    assert len(set(words)) == (1 << K)
    assert all(0 <= w <= MASK and polynomial_remainder(w, G) == 0 for w in words)
    actual_parts = Counter(map(direct_run_partition, words))
    assert actual_parts == expected_parts
    assert Counter(w.bit_count() for w in words) == {0: 1, 7: 253, 8: 506, 11: 1288, 12: 1288, 15: 506, 16: 253, 23: 1}
    assert Counter((min(rotate(w, i) for i in range(N)) for w in words if w not in (0, MASK))).__len__() == 178
    target_orbit = {rotate(G, i) for i in range(N)}
    assert len(target_orbit) == N
    for b in range(1, N + 1):
        spectrum = Counter(direct_weight(w, b) for w in words)
        assert given[b] == tuple(spectrum.get(j, 0) for j in range(N + 1)), b
        assert spectrum[0] == 1 and sum(spectrum.values()) == (1 << K)
        nonzero = [w for w in words if w]
        distance = min(direct_weight(w, b) for w in nonzero)
        expected_distance = {1: 7, 2: 11, 3: 13}.get(b, min(23, b + 11))
        assert distance == expected_distance, b
        minimizers = {w for w in nonzero if direct_weight(w, b) == distance}
        expected_count = 253 if b == 1 else 115 if b == 2 else N if b <= 11 else 4095
        assert len(minimizers) == expected_count
        if 3 <= b <= 11:
            assert minimizers == target_orbit
    print("VERIFY_OK: 4096 codewords, 81 zero-run classes, all 23 read lengths")


if __name__ == "__main__":
    verify()
