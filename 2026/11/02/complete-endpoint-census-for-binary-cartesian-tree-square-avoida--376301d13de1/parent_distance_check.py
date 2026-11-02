#!/usr/bin/env python3
"""Separate exhaustive checker using Cartesian-tree parent distances.

For the leftmost-minimum Cartesian tree, PD(w)[i] is zero unless there
is a preceding index j<i with w[j] <= w[i]; in that case it is i-j
for the *rightmost* such j. Equality of parent-distance vectors is
exactly Cartesian-tree-shape equivalence (Park et al., 2019, Thm 3.2).
"""
import hashlib


def parent_distances(word):
    result = []
    stack = []
    for i, letter in enumerate(word):
        while stack and stack[-1][0] > letter:
            stack.pop()
        result.append(i - stack[-1][1] if stack else 0)
        stack.append((letter, i))
    return tuple(result)


def allowed_extension(candidate):
    length = len(candidate)
    for width in range(3, length // 2 + 1):
        left = candidate[length - 2 * width:length - width]
        right = candidate[length - width:length]
        if parent_distances(left) == parent_distances(right):
            return False
    return True


def run():
    layer = {''}
    counts = []
    for n in range(1, 31):
        layer = {p + bit for p in layer for bit in ('0', '1')
                 if allowed_extension(p + bit)}
        counts.append(len(layer))
        if n == 29:
            best = sorted(layer)
    assert counts[-2:] == [20, 0]
    assert len(best) == 20
    # Also retest all possible long factors within each extremizer, not
    # only newly ending factors.
    for word in best:
        for half in range(3, 15):
            for offset in range(30 - 2 * half):
                l = word[offset:offset + half]
                r = word[offset + half:offset + 2 * half]
                assert parent_distances(l) != parent_distances(r)
    digest = hashlib.sha256(('\n'.join(best) + '\n').encode()).hexdigest()
    print('COUNTS=' + ','.join(map(str, counts)))
    print('WORDS_SHA256=' + digest)
    print('PARENT_DISTANCE_CHECK_OK')
    return best

if __name__ == '__main__':
    run()
