"""Independent finite checks of Zimin circular-conjugacy transport.

Usage: python checker.py
Only the Python standard library is required.
"""
from collections import defaultdict


def zimin(n):
    w = ""
    for i in range(1, n + 1):
        w = w + chr(64 + i) + w
    return w


def canonical_rotation(word):
    return min(word[i:] + word[:i] for i in range(len(word)))


def circular_classes(word, length):
    doubled = word + word
    return {canonical_rotation(doubled[i:i + length]) for i in range(len(word))}


def new_marker_classes(word, symbol, length):
    u = word
    representatives = defaultdict(list)
    for j in range(length):
        p = u[:length - 1 - j] + (u[-j:] if j else "")
        representatives[symbol + p].append(j)
    return representatives


def odd_part(n):
    while n % 2 == 0:
        n //= 2
    return n


def run():
    windows_checked = 0
    for n in range(2, 8):
        u = zimin(n - 1)
        w = zimin(n)
        for m in range(1, len(u) + 1):
            new = new_marker_classes(u, chr(64 + n), m)
            block = m // odd_part(m)
            expected_groups = [list(range(i, min(i + block, m)))
                               for i in range(0, m, block)]
            assert list(new.values()) == expected_groups, (n, m, new)
            old_classes = circular_classes(u, m)
            current = circular_classes(w, m)
            assert len(current) - len(old_classes) == odd_part(m), (n, m)
            marker_canon = {canonical_rotation(s) for s in new}
            assert current == old_classes | marker_canon, (n, m)
            assert old_classes.isdisjoint(marker_canon)
            windows_checked += len(w)
        print(f"rank {n} (length {len(w)}): all {len(u)} admissible lengths passed")
    assert len(zimin(7)) == 127
    print(f"All finite checks passed; {windows_checked} circular starts examined.")


if __name__ == '__main__':
    run()
