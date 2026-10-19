"""Independent exhaustive checks for the order-five cyclic 2-adic spectrum.

Run: python verify.py [cycles.csv]
Requires only the Python standard library.
"""
from __future__ import annotations
import csv
import math
import sys
from collections import Counter
from pathlib import Path

ORDER = 5
LENGTH = 1 << ORDER
MODULUS = (1 << LENGTH) - 1
FERMAT_FACTORS = (3, 5, 17, 257, 65537)
EXPECTED_GCD = {1: 1138, 3: 450, 5: 214, 15: 118, 17: 62,
                51: 28, 85: 8, 255: 26, 257: 2, 3855: 2}
EXPECTED_REVERSE = {
    (1, 1): 924, (1, 5): 332, (1, 17): 76, (1, 85): 16,
    (1, 257): 4, (3, 3): 364, (3, 15): 116, (3, 51): 48,
    (3, 255): 4, (3, 3855): 4, (5, 5): 36, (5, 17): 24,
    (15, 15): 56, (15, 51): 8, (17, 17): 12, (255, 255): 24
}
EXPECTED_LINEAR = {21: 8, 23: 12, 24: 20, 25: 32, 26: 36,
                   27: 64, 28: 180, 29: 224, 30: 448, 31: 1024}


def de_bruijn_check(word: str) -> bool:
    return (len(word) == LENGTH and set(word) == {'0', '1'}
            and len({(word + word)[i:i + ORDER] for i in range(LENGTH)}) == LENGTH)


def canonical(word: str) -> str:
    """Unique rotation whose leading five characters are all zero."""
    doubled = word + word
    j = doubled.find('0' * ORDER)
    if not 0 <= j < LENGTH:
        raise ValueError('not a de Bruijn word')
    return doubled[j:j + LENGTH]


def via_local_pairings():
    """All bijections at the 16 indegree-two/outdegree-two vertices."""
    out = set()
    for mask in range(1 << 16):
        def successor(edge: int) -> int:
            vertex = edge & 15
            incoming_side = edge >> 4
            return (vertex << 1) | (incoming_side ^ ((mask >> vertex) & 1))
        path = []
        current = 0  # the unique five-bit edge 00000
        seen = 0
        for _ in range(LENGTH):
            if (seen >> current) & 1:
                break
            seen |= 1 << current
            path.append(current)
            current = successor(current)
        if len(path) == LENGTH and current == 0:
            word = ''.join(str(edge & 1) for edge in path)
            out.add(canonical(word))
    return out


def via_eulerian_dfs():
    """Independent backtracking through labeled edges with fixed first edge zero."""
    solutions = set()
    # Edge e runs from (e >> 1) to (e & 15).
    # Starting with edge zero fixes rotation without excluding circuits.
    path = [0]
    def extend(vertex: int, visited: int) -> None:
        if len(path) == LENGTH:
            if vertex == 0:
                word = ''.join(str(e & 1) for e in path)
                solutions.add(canonical(word))
            return
        for e in ((vertex << 1), (vertex << 1) | 1):
            if visited & (1 << e):
                continue
            path.append(e)
            extend(e & 15, visited | (1 << e))
            path.pop()
    extend(0, 1)
    return solutions


def word_integer(word: str) -> int:
    return sum((ch == '1') << i for i, ch in enumerate(word))


def denominator_gcd(word: str) -> int:
    return math.gcd(MODULUS, word_integer(word))


def denominator_gcd_by_primes(word: str) -> int:
    n = word_integer(word)
    # 2^32-1 is the product of five distinct Fermat primes.
    d = 1
    for p in FERMAT_FACTORS:
        if n % p == 0:
            d *= p
    return d


def linear_complexity_polynomial(word: str) -> int:
    """x+1 multiplicity in the binary generating polynomial."""
    p = word_integer(word)
    mult = 0
    while p.bit_count() % 2 == 0:
        # Divide the GF(2) polynomial by x+1 by descending long division.
        q = 0
        for k in range(p.bit_length() - 1, 0, -1):
            if (p >> k) & 1:
                q |= 1 << (k - 1)
                p ^= 3 << (k - 1)
        assert p == 0
        p = q
        mult += 1
    return LENGTH - mult


def linear_complexity_berlekamp_massey(word: str) -> int:
    """Separate BM recurrence over two whole periods."""
    sequence = [int(b) for b in (word + word)]
    connection = [0] * (len(sequence) + 1)
    backup = [0] * (len(sequence) + 1)
    connection[0] = backup[0] = 1
    span = 0
    previous = -1
    for n in range(len(sequence)):
        discrepancy = sequence[n]
        for j in range(1, span + 1):
            discrepancy ^= connection[j] & sequence[n - j]
        if discrepancy:
            old = connection.copy()
            shift = n - previous
            for j in range(len(sequence) + 1 - shift):
                connection[j + shift] ^= backup[j]
            if 2 * span <= n:
                span = n + 1 - span
                backup = old
                previous = n
    return span


def analyze():
    a = via_local_pairings()
    b = via_eulerian_dfs()
    assert len(a) == len(b) == 2048 and a == b
    assert all(de_bruijn_check(s) and canonical(s) == s for s in a)
    assert math.prod(FERMAT_FACTORS) == MODULUS
    gcounts, reversal, linear = Counter(), Counter(), Counter()
    rows = []
    for s in sorted(a):
        g = denominator_gcd(s)
        assert g == denominator_gcd_by_primes(s)
        reverse = canonical(s[::-1])
        rg = denominator_gcd(reverse)
        assert rg == denominator_gcd_by_primes(reverse)
        assert reverse in b
        complement = canonical(''.join('1' if x == '0' else '0' for x in s))
        assert denominator_gcd(complement) == g
        c = linear_complexity_polynomial(s)
        assert c == linear_complexity_berlekamp_massey(s)
        assert c == linear_complexity_polynomial(reverse)
        assert c == linear_complexity_berlekamp_massey(reverse)
        assert c == linear_complexity_polynomial(complement)
        assert g * (MODULUS // g) == MODULUS
        gcounts[g] += 1
        reversal[tuple(sorted((g, rg)))] += 1
        linear[c] += 1
        rows.append((s, g, rg, c))
    assert dict(gcounts) == EXPECTED_GCD
    assert dict(reversal) == EXPECTED_REVERSE
    assert dict(linear) == EXPECTED_LINEAR
    assert sum(1 for _, g, rg, _ in rows if g != rg) == 632
    assert max(max(g, rg) / min(g, rg) for _, g, rg, _ in rows) == 1285
    assert sum(c == 31 and g == 3855 for _, g, rg, c in rows) == 2
    assert sum(c == 31 and g == 1 for _, g, rg, c in rows) == 640
    assert sum(c == 21 and g == 255 for _, g, rg, c in rows) == 8
    assert sum(g == 1 for _, g, rg, c in rows) == 1138
    assert sum(g == 3855 for _, g, rg, c in rows) == 2
    return rows, gcounts, reversal


def compare_csv(rows, csv_path):
    with csv_path.open(newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        assert reader.fieldnames == ['cycle', 'gcd', 'reverse_gcd', 'linear_complexity']
        from_file = [(d['cycle'], int(d['gcd']), int(d['reverse_gcd']),
                      int(d['linear_complexity'])) for d in reader]
    assert from_file == rows


if __name__ == '__main__':
    rows, gcds, revs = analyze()
    if len(sys.argv) > 1:
        compare_csv(rows, Path(sys.argv[1]))
    print('VERIFY_OK exhaustive_pairings=65536 independent_Eulerian_DFS=2048')
    print('VERIFY_OK gcd_methods=2 linear_complexity_methods=2 cycles=2048')
    print('VERIFY_OK gcd_levels=10 reversal_pair_types=16 reversal_discrepant_cycles=632')
    print('VERIFY_OK gcd_min=1:1138 gcd_max=3855:2 max_reversal_denominator_ratio=1285')
    print('VERIFY_OK maximum_LFSR_complexity_at_minimum_FCSR_denominator=31:2')
