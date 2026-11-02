#!/usr/bin/env python3
"""Reproducible exhaustive certificate for binary order-five circular attractors.

No external packages or datasets are needed. Execute: python3 checker.py
"""
from collections import Counter

ORDER = 5
PERIOD = 1 << ORDER


def feedback_cycles():
    """All cyclic de Bruijn words, canonically rooted at their unique 00000."""
    for choice in range(1 << 16):
        state = 0
        seen = set()
        letters = []
        while state not in seen:
            seen.add(state)
            letters.append(str(state >> 4))
            next_letter = (state >> 4) ^ ((choice >> (state & 15)) & 1)
            state = ((state & 15) << 1) | next_letter
        if state == 0 and len(seen) == PERIOD:
            yield ''.join(letters)


def euler_cycles():
    """Independent exhaustive search through all Euler tours of the 4-bit graph."""
    edges = [0]
    def visit(vertex, used):
        if len(edges) == PERIOD:
            if vertex == 0:
                yield ''.join(str(edge >> 4) for edge in edges)
            return
        for b in (0, 1):
            edge = 2 * vertex + b
            if not (used >> edge) & 1:
                edges.append(edge)
                yield from visit(edge & 15, used | (1 << edge))
                edges.pop()
    yield from visit(0, 1)


def tight_candidates():
    """Seven positions hitting every length-five cyclic window."""
    def weak_compositions(total, count):
        if count == 1:
            yield (total,)
        else:
            for first in range(total + 1):
                for tail in weak_compositions(total - first, count - 1):
                    yield (first,) + tail
    candidates = set()
    for deficits in weak_compositions(3, 7):
        gaps = [5 - z for z in deficits]
        for offset in range(PERIOD):
            pos = offset
            bits = 0
            for gap in gaps:
                bits |= 1 << pos
                pos = (pos + gap) % PERIOD
            assert pos == offset and bits.bit_count() == 7
            candidates.add(bits)
    assert len(candidates) == 384
    return sorted(candidates)


def factor_position_unions(word):
    """For each short factor, bits covered by all its cyclic occurrences."""
    all_masks = []
    for m in range(1, ORDER):
        masks = {}
        for start in range(PERIOD):
            factor = ''.join(word[(start + j) % PERIOD] for j in range(m))
            occupied = sum(1 << ((start + j) % PERIOD) for j in range(m))
            masks[factor] = masks.get(factor, 0) | occupied
        assert len(masks) == 2**m
        all_masks.extend(masks.values())
    assert len(all_masks) == 30
    return all_masks


def direct_validate(word, positions):
    """Independent factor-by-factor verification, including wrapping factors."""
    for size in range(1, ORDER + 1):
        needed = set()
        covered = set()
        for start in range(PERIOD):
            factor = ''.join(word[(start + j) % PERIOD] for j in range(size))
            needed.add(factor)
            if any((start + j) % PERIOD in positions for j in range(size)):
                covered.add(factor)
        if needed != covered:
            return False
    return True


def direct_validate_all_lengths(word, positions):
    for size in range(1, PERIOD + 1):
        needed = set()
        covered = set()
        for start in range(PERIOD):
            factor = ''.join(word[(start + j) % PERIOD] for j in range(size))
            needed.add(factor)
            if any((start + j) % PERIOD in positions for j in range(size)):
                covered.add(factor)
        if needed != covered:
            return False
    return True


def main():
    fb = list(feedback_cycles())
    eu = list(euler_cycles())
    assert len(fb) == len(eu) == 2048
    assert len(set(fb)) == len(set(eu)) == 2048
    assert set(fb) == set(eu)
    for word in fb:
        assert len(word) == PERIOD and word.startswith('00000')
        factors = {''.join(word[(i+j)%PERIOD] for j in range(ORDER))
                   for i in range(PERIOD)}
        assert len(factors) == PERIOD
    candidates = tight_candidates()
    freq = Counter()
    witnesses = {}
    examples = {}
    total = 0
    for word in sorted(fb):
        masks = factor_position_unions(word)
        passing = [s for s in candidates if all(s & x for x in masks)]
        number = len(passing)
        assert number > 0
        freq[number] += 1
        total += number
        examples.setdefault(number, word)
        witnesses[word] = passing[0]
    assert (min(freq), max(freq)) == (216, 368)
    assert (freq[216], freq[368]) == (4, 2)
    assert total == 589120
    assert len(freq) == 120
    # Test one selected optimum against all 32 circular factor lengths in every word.
    for word, bits in witnesses.items():
        positions = {i for i in range(PERIOD) if (bits >> i) & 1}
        assert len(positions) == 7
        assert direct_validate(word, positions)
    # Fully verify all circular lengths for the sharp extremal examples.
    for word in (examples[216], examples[368]):
        positions = {i for i in range(PERIOD) if (witnesses[word] >> i) & 1}
        assert direct_validate_all_lengths(word, positions)
    print('PASS; cycles=2048; tight_sets=384; optimum=7 for all')
    print('minimum optimal-set count=216 (4 cycles); maximum=368 (2 cycles)')
    print('total optimal size-seven sets=589120; distinct counts=120')
    print('minimum example=' + examples[216])
    print('maximum example=' + examples[368])

if __name__ == '__main__':
    main()
