#!/usr/bin/env python3
"""Independent face oracle: DFS cycle detection rather than union/find.
Also independently checks the complete 2-skeleton and Euler characteristics.
"""
from collections import Counter

N = 16
ADJ = [[w for w in range(N) if (v ^ w).bit_count() == 1] for v in range(N)]


def is_forest_by_dfs(mask):
    seen = set()
    for v in range(N):
        if not ((mask >> v) & 1) or v in seen:
            continue
        seen.add(v)
        stack = [(v, -1, iter(ADJ[v]))]
        while stack:
            x, parent, it = stack[-1]
            try:
                y = next(it)
            except StopIteration:
                stack.pop()
                continue
            if not ((mask >> y) & 1) or y == parent:
                continue
            if y in seen:
                return False
            seen.add(y)
            stack.append((y, x, iter(ADJ[y])))
    return True


def face(mask, d):
    for v in range(N):
        if (mask >> v) & 1 and d is not None:
            if sum((mask >> w) & 1 for w in ADJ[v]) > d:
                return False
    return is_forest_by_dfs(mask)


def main():
    c2, ci = Counter(), Counter()
    counts = [0, 0]
    for mask in range(1 << N):
        x = face(mask, 2)
        y = face(mask, None)
        assert not x or y
        if x:
            c2[mask.bit_count() - 1] += 1
            counts[0] += 1
        if y:
            ci[mask.bit_count() - 1] += 1
            counts[1] += 1
        if mask.bit_count() <= 3:
            assert x, 'Every three-element subset must be a 2-forest face'
    assert tuple(c2[k] for k in range(8)) == (16, 120, 560, 1732, 3552, 4616, 3392, 922)
    assert tuple(ci[k] for k in range(10)) == (16, 120, 560, 1796, 4080, 6488, 6848, 4090, 1008, 8)
    assert c2[-1] == ci[-1] == 1
    assert counts == [14911, 25015], counts
    print('DFS_independent_face_counts=14911,25015_including_empty_face')
    print('Complete_two_skeleton=yes')
    print('Euler_reduced=129,9')
    print('INDEPENDENT_FACE_CHECK_PASSED')


if __name__ == '__main__':
    main()
