#!/usr/bin/env python3
"""Exact finite-census verification of the two-peak singleton phenomenon.

Requires Python >= 3.9, standard library only.
Usage: python3 verify_singleton_peaks.py census.csv
       python3 verify_singleton_peaks.py --write-certificate census.csv
"""
import csv
import io
import itertools
import math
import pathlib
import sys
from fractions import Fraction


def partitions(total, ceiling=None):
    """Enumerate every positive-integer partition exactly once, nonincreasing."""
    if ceiling is None:
        ceiling = total
    if total == 0:
        yield ()
        return
    for first in range(min(total, ceiling), 0, -1):
        for rest in partitions(total-first, first):
            yield (first,) + rest


def partition_via_compositions(total):
    """Independent completeness check via all cuts of a row of `total` items."""
    outcomes = set()
    for cuts in itertools.product((0, 1), repeat=total-1):
        blocks = []
        running = 1
        for cut in cuts:
            if cut:
                blocks.append(running)
                running = 1
            else:
                running += 1
        blocks.append(running)
        outcomes.add(tuple(sorted(blocks, reverse=True)))
    return outcomes


def expectations_hypergeom(parts):
    n = sum(parts)
    result = []
    for m in range(1, n+1):
        count = sum(
            a * math.comb(n-a, m-1)
            for a in parts if m-1 <= n-a
        )
        result.append(Fraction(count, math.comb(n, m)))
    return tuple(result)


def expectations_subsets(parts):
    """Directly enumerate subsets of labeled individuals, independently."""
    labels = tuple(
        species for species, abundance in enumerate(parts)
        for _ in range(abundance)
    )
    n = len(labels)
    counts = [0] * (n+1)
    totals = [0] * (n+1)
    for mask in range(1, 1 << n):
        tally = [0] * len(parts)
        for j in range(n):
            if mask & (1 << j):
                tally[labels[j]] += 1
        m = mask.bit_count()
        counts[m] += sum(value == 1 for value in tally)
        totals[m] += 1
    return tuple(Fraction(counts[m], totals[m]) for m in range(1, n+1))


def peaks(sequence):
    return tuple(
        j+1 for j in range(1, len(sequence)-1)
        if sequence[j-1] < sequence[j] > sequence[j+1]
    )


def generate():
    out = io.StringIO(newline="")
    writer = csv.writer(out, lineterminator="\n")
    writer.writerow(("N", "abundance_partition", "E_f1_m1_to_mN", "strict_interior_peak_m"))
    class_counts = []
    exceptional = []
    for n in range(1, 9):
        parts = list(partitions(n))
        assert len(parts) == (1, 2, 3, 5, 7, 11, 15, 22)[n-1]
        assert set(parts) == partition_via_compositions(n)
        counts = [0, 0, 0]
        for part in parts:
            x = expectations_hypergeom(part)
            y = expectations_subsets(part)
            assert x == y, (part, x, y)
            pk = peaks(x)
            assert len(pk) <= 2
            counts[len(pk)] += 1
            if len(pk) >= 2:
                exceptional.append((part, pk, x))
            writer.writerow((str(n), ";".join(map(str, part)),
                             ";".join(map(str, x)),
                             ";".join(map(str, pk))))
        class_counts.append((n, len(parts), *counts))
    assert class_counts == [
        (1, 1, 1, 0, 0),
        (2, 2, 2, 0, 0),
        (3, 3, 2, 1, 0),
        (4, 5, 4, 1, 0),
        (5, 7, 5, 2, 0),
        (6, 11, 6, 5, 0),
        (7, 15, 7, 8, 0),
        (8, 22, 12, 9, 1),
    ]
    assert len(exceptional) == 1
    part, pk, x = exceptional[0]
    assert part == (5, 2, 1) and pk == (2, 6)
    assert x == tuple(map(Fraction,
        ("1", "17/14", "33/28", "8/7", "65/56", "33/28", "9/8", "1")))
    return out.getvalue().encode("utf-8"), class_counts


def check_uniform_abundances():
    """Independent finite checks of the equal-abundance adjacent-ratio identity."""
    for a in range(1, 10):
        for species in range(1, 11):
            n = a*species
            part = (a,)*species
            z = expectations_hypergeom(part)
            for m in range(1, n):
                # Ratio only when both nonzero; use cross-multiplication instead.
                lhs = (m+1)*(n-a-m+1)
                rhs = m*(n-m)
                if z[m-1] > 0 and z[m] > 0:
                    assert (z[m] > z[m-1]) == (lhs > rhs)
                    assert (z[m] == z[m-1]) == (lhs == rhs)
    return True


def main():
    b, counts = generate()
    check_uniform_abundances()
    if len(sys.argv) != 3 or sys.argv[1] not in ("--write-certificate", "--verify-certificate"):
        raise SystemExit("Usage: python3 verify_singleton_peaks.py --verify-certificate census.csv")
    p = pathlib.Path(sys.argv[2])
    if sys.argv[1] == "--write-certificate":
        p.write_bytes(b)
    else:
        assert p.read_bytes() == b, "Census certificate differs from the recomputed exact table"
    print("PASS: 66 partitions of totals 1..8, partition-composition completeness checks,")
    print("two independent exact singleton expectations for every depth; unique (5,2,1)")
    print("at N=8, strict peaks 2 and 6; uniform-abundance ratio checks.")
    print("N,classes,zero_peaks,one_peak,two_peaks")
    for row in counts:
        print(",".join(map(str, row)))

if __name__ == "__main__":
    main()
