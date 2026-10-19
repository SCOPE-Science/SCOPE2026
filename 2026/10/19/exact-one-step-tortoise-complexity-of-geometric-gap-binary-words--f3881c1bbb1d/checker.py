#!/usr/bin/env python3
"""Independent checks for tortoise complexity of geometric-gap binary words.

The direct method enumerates image sets from a long finite prefix.
The interval method counts two-one images and windows with at least three ones.
Both are compared with the closed formula; finite tests do not prove it.
"""

def predicted(b, n):
    assert b >= 2 and n >= 1
    if n < b:
        return 2
    if n <= b*(b-1):
        return 3
    d, k = b*(b-1), 1
    while n >= b*d:
        d *= b
        k += 1
    return 2 + b**(k-1) + min((b-1)*b**(k-1), n-d)


def union_size(intervals):
    total, last = 0, -1
    for left, right in sorted(intervals):
        if left <= right:
            total += max(0, right-max(left, last+1)+1)
            last = max(last, right)
    return total


def interval_count(b, n):
    positions = [0]
    while positions[-1] < 4*n+10:
        positions.append(b*(positions[-1]+1)-1)
    triple = []
    two = []
    for k in range(len(positions)-2):
        left = max(0, positions[k+2]-n+1)
        triple.append((left, positions[k]))
    for k in range(len(positions)-1):
        first, second = positions[k:k+2]
        left = max(0, (positions[k-1]+1) if k else 0, second-n+1)
        right = min(first, (positions[k+2]-n) if k+2 < len(positions) else first)
        if left <= right:
            two.append((second-right-1, second-left-1))
    return 2 + union_size(triple) + union_size(two)


def direct_count(b, n):
    N = 16*n+80
    support = set()
    power = 1
    while power-1 < N:
        support.add(power-1)
        power *= b
    mask = (1 << n)-1
    value = 0
    images = set()
    for t in range(N):
        value = ((value << 1) | int(t in support)) & mask
        if t+1 < n:
            continue
        if value:
            j = value.bit_length()-1
            image = ((value ^ (1 << j)) << 1) | 1
        else:
            image = 0
        images.add(image)
    # The long finite prefix has all multi-one factors; no reliance on it for one-one cases.
    images.add(0)
    images.add(1)
    return len(images)


def main():
    interval_cells=0
    direct_cells=0
    for b in range(2, 13):
        for n in range(1, 2001):
            a = interval_count(b, n)
            f = predicted(b, n)
            assert a == f, (b, n, a, f)
            interval_cells += 1
    for b in range(2, 9):
        for n in range(1, 201):
            direct = direct_count(b, n)
            formula = predicted(b, n)
            assert direct == formula, (b, n, direct, formula)
            direct_cells += 1
    for b in range(2, 10):
        for k in range(1, 10):
            d = (b-1)*b**k
            h = (b*b-1)*b**(k-1)
            for n in [d-1, d, d+1, h-1, h, h+1, b*d-1, b*d, b*d+1]:
                if n > 0:
                    assert interval_count(b,n) == predicted(b,n), (b,k,n)
                    interval_cells += 1
    print(f"direct enumeration cells: {direct_cells}")
    print(f"independent interval cells: {interval_cells}")
    for b in (2,3,4,5):
        print('base', b, 'n=1..20', [predicted(b,n) for n in range(1,21)])
    print('All finite checks passed.')


if __name__ == '__main__':
    main()
