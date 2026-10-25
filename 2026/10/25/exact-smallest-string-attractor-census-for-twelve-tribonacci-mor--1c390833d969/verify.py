#!/usr/bin/env python3
"""Exhaustive finite string-attractor certificate verifier (stdlib only)."""
import hashlib
import json
from pathlib import Path

RULE = {48: b'01', 49: b'02', 50: b'0'}


def factor_masks(w):
    n = len(w)
    masks = {}
    for length in range(1, n + 1):
        window = (1 << length) - 1
        for start in range(n - length + 1):
            factor = w[start:start + length]
            masks[factor] = masks.get(factor, 0) | (window << start)
    return masks


def essential_masks(all_masks):
    result = []
    for mask in sorted(set(all_masks), key=lambda m: (m.bit_count(), m)):
        if not any(mask & keep == keep for keep in result):
            result.append(mask)
    return result


def compute_attractors(w):
    letters = sorted(set(w))
    if len(letters) < 3:
        return [[i for i in range(len(w))]], len(letters), 0
    by_letter = {v: [i for i, ch in enumerate(w) if ch == v] for v in letters}
    # Every size-three attractor must use each of the three letters exactly once.
    ordered = sorted(letters, key=lambda c: (len(by_letter[c]), c))
    third = sum(1 << i for i in by_letter[ordered[2]])
    coverage = factor_masks(w)
    essential = essential_masks(coverage.values())
    result = []
    for first in by_letter[ordered[0]]:
        uncovered = [m for m in essential if not ((m >> first) & 1)]
        for second in by_letter[ordered[1]]:
            third_options = third
            for mask in uncovered:
                if not ((mask >> second) & 1):
                    third_options &= mask
                    if not third_options:
                        break
            while third_options:
                bit = third_options & -third_options
                last = bit.bit_length() - 1
                result.append(sorted((first, second, last)))
                third_options -= bit
    result.sort()
    return result, 3, len(essential)


def run():
    path = Path(__file__).resolve().parent / 'certificates' / 'attractors.json'
    obj = json.loads(path.read_text(encoding='utf-8'))
    assert obj['index_range'] == [0, 11]
    w = b'0'
    for stage in obj['stages']:
        k = stage['index']
        assert k == obj['stages'].index(stage)
        found, minimum_size, essential = compute_attractors(w)
        assert len(w) == stage['length'], (k, 'length')
        assert hashlib.sha256(w).hexdigest() == stage['word_sha256'], (k, 'word')
        assert found == stage['attractors'], (k, 'attractor collection differs')
        assert len(found) == stage['number_of_smallest_attractors'], (k, 'count')
        assert minimum_size == stage['smallest_attractor_size'], (k, 'minimum size')
        assert essential == stage['essential_mask_count'], (k, 'essential mask count')
        print(f"order={k:2d} length={len(w):4d} size={minimum_size} count={len(found):4d} essential_masks={essential}")
        w = b''.join(RULE[c] for c in w)
    assert len(obj['stages']) == 12
    print('All twelve exact finite counts and complete attractor lists verified.')

if __name__ == '__main__':
    run()
