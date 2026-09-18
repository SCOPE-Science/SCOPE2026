#!/usr/bin/env python3
"""Finite sanity checks for the binary synchronized code used in the theorem."""
from itertools import product


def encode(payload: str) -> str:
    h = ''.join('10' if b == '0' else '11' for b in payload)
    return '001' + h + '10'


def max_run_of_ones(s: str) -> int:
    return max((len(x) for x in s.split('0')), default=0)


def verify(beta: int) -> tuple[int, int, int]:
    payloads = [''.join(bits) for bits in product('01', repeat=beta)]
    code = [encode(x) for x in payloads]
    code_set = set(code)
    k = 2 * beta + 5
    assert all(len(c) == k for c in code)
    assert len(code_set) == 2 ** beta
    assert all(c.startswith('001') and c.endswith('0') for c in code)

    noncode_windows = set()
    for a in code:
        for b in code:
            s = a + b
            for i in range(k + 1):
                w = s[i:i + k]
                if len(w) != k:
                    continue
                if w in code_set:
                    assert i in (0, k), (beta, a, b, i, w)
                else:
                    noncode_windows.add(w)

    g = '1' * k
    for t in noncode_windows:
        s = g + t + g
        for i in range(len(s) - k + 1):
            assert s[i:i + k] not in code_set, (beta, t, i, s[i:i+k])

    # Any encoded source is a concatenation of codewords. It therefore avoids 1^k:
    # the worst single-codeword run is enough because every boundary contains zeroes.
    mr = max(max_run_of_ones(c) for c in code)
    assert mr == 2 * beta + 2
    assert mr < k
    return k, len(noncode_windows), mr


def main() -> None:
    print('binary synchronized-code sanity check')
    for beta in range(1, 7):
        k, r, mr = verify(beta)
        print(f'beta={beta} k={k} codewords={2**beta} noncode_windows={r} max_ones_run={mr}: PASS')
    print('ALL CHECKS PASS')


if __name__ == '__main__':
    main()
