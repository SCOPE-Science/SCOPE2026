#!/usr/bin/env python3
"""Independent cyclic-rotation checks for period-doubling BWT."""
from __future__ import annotations


def period_word(m: int) -> str:
    w = '0'
    for _ in range(m):
        w = ''.join('01' if c == '0' else '00' for c in w)
    return w


def bwt_by_cyclic_rank_doubling(s: str) -> str:
    n = len(s)
    order = list(range(n))
    rank = [int(c) for c in s]
    length = 1
    while length < n:
        order.sort(key=lambda i: (rank[i], rank[(i + length) % n]))
        updated = [0] * n
        value = 0
        updated[order[0]] = 0
        for j in range(1, n):
            a, b = order[j - 1], order[j]
            if (rank[a], rank[(a + length) % n]) != (rank[b], rank[(b + length) % n]):
                value += 1
            updated[b] = value
        rank = updated
        length *= 2
    return ''.join(s[(i - 1) % n] for i in order)


def bwt_by_direct_rotations(s: str) -> str:
    # Independent, intentionally quadratic enumeration; used only up to 512 symbols.
    rotations = [(s[i:] + s[:i], s[(i - 1) % len(s)]) for i in range(len(s))]
    return ''.join(last for _, last in sorted(rotations))


def reverse_complement(s: str) -> str:
    return s.translate(str.maketrans('01', '10'))[::-1]


def run_count(s: str) -> int:
    return 1 + sum(a != b for a, b in zip(s, s[1:])) if s else 0


def run_lengths(s: str):
    out = []
    for c in s:
        if out and c == out[-1][0]:
            out[-1] = (c, out[-1][1] + 1)
        else:
            out.append((c, 1))
    return out


def main() -> None:
    t = '1'  # First-zero-rotation segment at m=1, for W_1=01.
    for m in range(1, 14):
        if m >= 2:
            ones_previous = (2**(m - 1) - (-1)**(m - 1)) // 3
            t = ('1' * ones_previous + '0' * ones_previous + reverse_complement(t))
        zeros_previous = (2 * 2**(m - 1) + (-1)**(m - 1)) // 3
        predicted = t + '0' * zeros_previous
        w = period_word(m)
        direct = bwt_by_cyclic_rank_doubling(w)
        assert predicted == direct, f'mismatch in BWT at m={m}'
        assert run_count(direct) == (2 if m == 1 else 2*m - 2)
        assert len(predicted) == len(w) == 2**m
        assert direct[-zeros_previous:] == '0' * zeros_previous
        if m <= 9:
            assert bwt_by_direct_rotations(w) == direct, f'independent rotation mismatch at m={m}'
        print(f'm={m:2} n={len(w):5} runs={run_count(direct):2} zeroes={w.count("0"):5} '
              f'ones={w.count("1"):5} BWT-run-lengths={run_lengths(direct) if m <= 8 else "omitted"}')
    print('PASS: complete BWT words and run counts through m=13; direct rotation sorting through m=9.')


if __name__ == '__main__':
    main()
