"""Reproduce exact cyclic zero-run and window-read tables of the binary Golay code.

Requires Python 3 standard library. From this directory: python GENERATE.py
"""
from collections import Counter
import csv

N = 23
G = sum(1 << j for j in (0, 2, 4, 5, 6, 10, 11))
MASK = (1 << N) - 1


def codeword(message):
    word = 0
    for j in range(12):
        if message & (1 << j):
            word ^= G << j
    return word


def zero_run_partition(word):
    if word == 0:
        return "ALL_ZERO"
    if word == MASK:
        return "ALL_ONE"
    runs = []
    for i in range(N):
        if not (word >> i) & 1 and (word >> ((i - 1) % N)) & 1:
            j = i
            length = 0
            while not ((word >> j) & 1):
                length += 1
                j = (j + 1) % N
            runs.append(length)
    return ".".join(map(str, sorted(runs, reverse=True)))


def weight_from_partition(partition, b):
    if partition == "ALL_ZERO":
        return 0
    if partition == "ALL_ONE":
        return N
    return N - sum(max(int(s) - b + 1, 0) for s in partition.split("."))


def generate():
    histogram = Counter(zero_run_partition(codeword(m)) for m in range(1 << 12))
    assert len(histogram) == 81
    with open("ZERO_RUN_CENSUS.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow(["zero_run_partition", "number_of_codewords"])
        for part in sorted(histogram, key=lambda p: (p == "ALL_ZERO", p == "ALL_ONE", p)):
            writer.writerow([part, histogram[part]])
    with open("B_SYMBOL_SPECTRA.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow(["b"] + [f"A_{j}" for j in range(N + 1)])
        for b in range(1, N + 1):
            spectrum = Counter()
            for part, multiplicity in histogram.items():
                spectrum[weight_from_partition(part, b)] += multiplicity
            writer.writerow([b] + [spectrum[j] for j in range(N + 1)])
    print("GENERATED: 81 run types, 23 complete window spectra")


if __name__ == "__main__":
    generate()
