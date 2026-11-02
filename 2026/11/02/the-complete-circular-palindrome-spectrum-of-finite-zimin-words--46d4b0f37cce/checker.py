"""Standalone finite verification of cyclic palindromes in finite Zimin words.

This checks examples only. All-rank validity requires the mathematical proof.
Run with Python 3: python checker.py
"""
from collections import defaultdict


def zimin(rank):
    w = ""
    for j in range(rank):
        w = w + chr(97 + j) + w
    return w


def v2(k):
    assert k >= 1
    return (k & -k).bit_length() - 1


def predicted(rank):
    w = zimin(rank)
    length = len(w)
    out = set()
    # Explicit odd palindromes, with central marker of rank r.
    for r in range(1, rank + 1):
        for t in range(1 << (r - 1)):
            flank = "".join(chr(97 + v2(d)) for d in range(t, 0, -1))
            out.add(flank + chr(96 + r) + flank[::-1])
    # Explicit even palindromes, all centred at the circular seam.
    for t in range(1, (length - 1) // 2 + 1):
        out.add(w[-t:] + w[:t])
    return out


def exhaustive(rank):
    w = zimin(rank)
    length = len(w)
    doubled = w * 2
    out = set()
    bylength = defaultdict(set)
    for start in range(length):
        for ell in range(1, length + 1):
            sub = doubled[start:start + ell]
            if sub == sub[::-1]:
                out.add(sub)
                bylength[ell].add(sub)
    return out, bylength


def check():
    for rank in range(1, 9):
        w = zimin(rank)
        length = len(w)
        got, spectrum = exhaustive(rank)
        expected = predicted(rank)
        assert got == expected, (rank, sorted(expected - got), sorted(got - expected))
        assert len(got) == 3 * (1 << (rank - 1)) - 2
        assert all(len(wd) <= length for wd in got)
        for ell in range(1, length + 1):
            if ell % 2 == 0:
                expected_count = 1
            else:
                t = (ell - 1) // 2
                # ceil(log2(t+1)) = bit_length(t) for t >= 0.
                expected_count = rank - t.bit_length()
            assert len(spectrum[ell]) == expected_count, (rank, ell, len(spectrum[ell]), expected_count)
        linear = set()
        for start in range(length):
            for ell in range(1, length - start + 1):
                sub = w[start:start + ell]
                if sub == sub[::-1]:
                    linear.add(sub)
        assert all(len(s) % 2 for s in linear)
        assert linear == {p for p in got if len(p) % 2}
        print(f"rank={rank}, N={length}, cyclic_palindromes={len(got)}, odd={len(linear)}, even={len(got)-len(linear)}")
    print("CHECK_OK")


if __name__ == "__main__":
    check()
