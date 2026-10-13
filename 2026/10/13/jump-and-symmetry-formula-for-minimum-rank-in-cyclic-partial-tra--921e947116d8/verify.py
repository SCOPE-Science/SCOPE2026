#!/usr/bin/env python3
"""Finite checks for an exact partial-jump cyclic-automaton rank formula.
This program is supplemental evidence; the infinite theorem has a separate proof.
"""
from collections import deque
from math import gcd
from random import Random


def stabilizer(n, mask):
    return [t for t in range(n) if all(((mask >> i) & 1) == ((mask >> ((i + t) % n)) & 1) for i in range(n))]


def predicted(n, h, mask):
    s = len(stabilizer(n, mask))
    return s * gcd(n // s, h)


def image(mask, trans):
    out = 0
    while mask:
        low = mask & -mask
        mask ^= low
        i = low.bit_length() - 1
        out |= 1 << trans[i]
    return out


def bfs_minimum_rank(n, h, mask):
    letters = ([((i + 1) % n) for i in range(n)],
               [((i + h) % n if (mask >> i) & 1 else i) for i in range(n)])
    whole = (1 << n) - 1
    seen = {whole}
    queue = deque([whole])
    minimum = n
    while queue:
        state = queue.popleft()
        minimum = min(minimum, state.bit_count())
        for transition in letters:
            nxt = image(state, transition)
            if nxt not in seen:
                queue.append(nxt)
                seen.add(nxt)
    return minimum


def quotient_construction(n, h, mask):
    s = len(stabilizer(n, mask))
    m = n // s
    d = gcd(m, h)
    # The pattern's minimal period is m; quotient pattern is aperiodic.
    assert all(((mask >> i) & 1) == ((mask >> (i % m)) & 1) for i in range(n))
    M = mask & ((1 << m) - 1)
    assert len(stabilizer(m, M)) == 1

    def bt(i, t):
        return (i + h) % m if M >> ((i - t) % m) & 1 else i

    total_word = []
    expansions = 0
    for c in range(d):
        start = c
        L = m // d
        part = []
        for ell in range(1, L):
            # Current inverse image is the h-cyclic interval from start to its right endpoint.
            before = (start - h) % m
            right = (start + (ell - 1) * h) % m
            shifts = [t for t in range(m)
                      if ((M >> ((before - t) % m)) & 1)
                      and not ((M >> ((right - t) % m)) & 1)]
            assert shifts, (n, h, mask, c, ell)
            t = shifts[0]
            old_I = {(start + j * h) % m for j in range(ell)}
            new_I = {(start - h + j * h) % m for j in range(ell + 1)}
            assert {i for i in range(m) if bt(i, t) in old_I} == new_I
            part.insert(0, t)
            start = before
            expansions += 1
        # This word must collapse all points in this residue class mod d.
        cls = [i for i in range(m) if i % d == c]
        images = []
        for v in cls:
            for t in part:
                v = bt(v, t)
            images.append(v)
        assert len(set(images)) == 1
        total_word.extend(part)

    final_image = set()
    for i in range(m):
        v = i
        for t in total_word:
            v = bt(v, t)
        final_image.add(v)
    assert len(final_image) == d, (n, h, mask, final_image)
    # Every transformation commutes with shifts from the stabilizer.
    original_image = set()
    for i in range(n):
        v = i
        for t in total_word:
            v = (v + h) % n if ((mask >> ((v - t) % n)) & 1) else v
        original_image.add(v)
    assert len(original_image) == s * d
    return expansions, len(total_word)


def main():
    checked_bfs = 0
    checked_witness = 0
    checked_expansion = 0
    # Exhaustive binary patterns, nonzero jumps, and independent subset BFS.
    for n in range(2, 11):
        for h in range(1, n):
            for mask in range(1 << n):
                assert bfs_minimum_rank(n, h, mask) == predicted(n, h, mask), (n, h, mask)
                checked_bfs += 1
    # All quotients must admit the constructive extension, including degenerate patterns.
    for n in range(2, 13):
        for h in range(1, n):
            for mask in range(1 << n):
                steps, length = quotient_construction(n, h, mask)
                checked_expansion += steps
                checked_witness += 1
    # Unrestricted larger inputs, deterministic pseudorandom samples.
    rng = Random(20261009)
    for n in (13, 14, 15, 16, 20, 24, 31):
        for _ in range(200):
            h = rng.randrange(1, n)
            mask = rng.getrandbits(n)
            steps, length = quotient_construction(n, h, mask)
            checked_expansion += steps
            checked_witness += 1
    print(f'VERIFY_OK exhaustive_subset_bfs_cases={checked_bfs} '
          f'constructive_witness_cases={checked_witness} '
          f'certified_inverse_expansions={checked_expansion}')


if __name__ == '__main__':
    main()
