#!/usr/bin/env python3
"""Exact finite witness/obstruction verifier for bounded-run binary self-shuffles.

Python 3.10+ standard library only. Usage:
    python verify_four_run.py
Run from the directory containing the two TSV files.
"""
from collections import deque
from functools import lru_cache
from pathlib import Path

BASE = Path(__file__).resolve().parent
TARGETS = {38: 538, 40: 674, 42: 682, 44: 870}
NEGATIVE_COUNTS = {4: 2, 8: 6, 10: 4, 12: 14, 14: 12,
                   16: 16, 18: 4, 20: 20, 24: 8, 28: 4, 36: 4}


def derivative(word):
    """Finite C-infinity derivative, trimming boundary length-one runs."""
    if not word:
        return ''
    runs = []
    prior = None
    for ch in word:
        if ch == prior:
            runs[-1] += 1
        else:
            runs.append(1)
            prior = ch
    if max(runs) > 2:
        return None
    if runs[0] == 1:
        runs.pop(0)
    if runs and runs[-1] == 1:
        runs.pop()
    return ''.join(map(str, runs))


def smooth(word):
    while word:
        word = derivative(word)
        if word is None:
            return False
    return True


def inverse_derivative_words(max_len):
    """Enumerate all smooth words through max_len by exact inverse derivatives."""
    observed = {'1', '2', '12', '21'}
    queue = deque(sorted(observed))
    while queue:
        parent = queue.popleft()
        first_options = (True,) if parent[0] == '1' else (False, True)
        last_options = (True,) if parent[-1] == '1' else (False, True)
        for add_front in first_options:
            for add_back in last_options:
                lengths = ('1' if add_front else '') + parent + ('1' if add_back else '')
                for initial in ('1', '2'):
                    other = '2' if initial == '1' else '1'
                    word = ''.join((initial if j % 2 == 0 else other) * int(v)
                                   for j, v in enumerate(lengths))
                    if len(word) <= max_len and word not in observed:
                        assert derivative(word) == parent
                        observed.add(word)
                        queue.append(word)
    return observed


def prefix_extension_words(max_len):
    """Independent enumeration using factoriality and repeated differentiation."""
    current = {''}
    all_words = set()
    for _ in range(max_len):
        current = {w + c for w in current for c in '12' if smooth(w + c)}
        all_words.update(current)
    return all_words


def maximum_run(colors):
    last = '';length = 0;greatest = 0
    for c in colors:
        length = length + 1 if c == last else 1
        greatest = max(greatest, length)
        last = c
    return greatest


def bounded_coloring_exists(word, limit):
    """Complete state enumeration: two partial streams must be prefix-comparable.

    State: leading color (0 when tied), unmatched suffix, previous color,
    monochromatic-run length. Each next character goes to either stream.
    """
    n = len(word)
    assert n % 2 == 0
    states = {(0, '', 0, 0)}
    for i, ch in enumerate(word):
        following = set()
        for leader, suffix, last, run in states:
            for color in (1, 2):
                if color == last and run >= limit:
                    continue
                if not suffix or color == leader:
                    next_suffix = suffix + ch
                    next_leader = color
                else:
                    if suffix[0] != ch:
                        continue
                    next_suffix = suffix[1:]
                    next_leader = leader if next_suffix else 0
                # Both streams must finish equal, and be length n/2.
                if len(next_suffix) > min(n - i - 1, n // 2):
                    continue
                next_run = run + 1 if color == last else 1
                following.add((next_leader, next_suffix, color, next_run))
        states = following
        if not states:
            return False
    return any(not suffix for _, suffix, _, _ in states)


def main():
    by_inverse = inverse_derivative_words(44)
    by_prefix = prefix_extension_words(44)
    assert by_inverse == by_prefix, (len(by_inverse), len(by_prefix))
    print('independent smooth-word generators agree:', len(by_inverse))
    assert all(smooth(w) for w in by_inverse)
    relevant = {w for w in by_inverse if len(w) in TARGETS and w.count('1') % 2 == 0}
    assert {n: sum(len(w) == n for w in relevant) for n in TARGETS} == TARGETS

    lines = (BASE / 'four_run_witnesses.tsv').read_text(encoding='utf-8').splitlines()
    assert lines.pop(0) == 'word\tcoloring'
    certificate_words = set()
    for line in lines:
        word, colors = line.split('\t')
        assert word in relevant and word not in certificate_words
        certificate_words.add(word)
        assert len(word) == len(colors)
        assert set(colors) == {'U','D'}
        assert maximum_run(colors) <= 4
        left = ''.join(ch for ch, col in zip(word, colors) if col == 'U')
        right = ''.join(ch for ch, col in zip(word, colors) if col == 'D')
        assert left == right
    assert certificate_words == relevant
    print('witnesses verified:', len(certificate_words), TARGETS)

    failures = (BASE / 'four_run_lower_bound.tsv').read_text(encoding='utf-8').splitlines()
    assert failures.pop(0) == 'length\tmax_run\tword\tcount_failing_at_length'
    failure_lengths = []
    for line in failures:
        sn, slim, word, scount = line.split('\t')
        n, limit, count = int(sn), int(slim), int(scount)
        assert word in by_inverse and len(word) == n and word.count('1') % 2 == 0
        assert not bounded_coloring_exists(word, limit), (n, limit, word)
        failure_lengths.append(n)
        if n != 38:
            assert limit == 4 and NEGATIVE_COUNTS[n] == count
        else:
            assert limit == 3 and count == 8
    assert set(failure_lengths) == set(NEGATIVE_COUNTS) | {38}
    for threshold in range(2, 38, 2):
        assert any(threshold <= n <= threshold + 6 for n in NEGATIVE_COUNTS)
    print('obstruction witnesses verified:', len(failure_lengths),
          'and all shorter four-length windows are obstructed')
    print('PASS')


if __name__ == '__main__':
    main()
