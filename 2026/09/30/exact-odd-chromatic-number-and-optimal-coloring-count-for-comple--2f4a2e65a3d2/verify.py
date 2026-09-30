from itertools import product
from math import factorial


def predicted_k(parts):
    r = len(parts)
    o = sum(n % 2 for n in parts)
    return r + max(0, 2 - o)


def predicted_count(parts):
    r = len(parts)
    o = sum(n % 2 for n in parts)
    k = predicted_k(parts)
    if o >= 2:
        unlabeled = 1
    elif o == 1:
        unlabeled = sum(2 ** (n - 2) for n in parts if n % 2 == 0)
    else:
        unlabeled = sum(
            2 ** (parts[i] + parts[j] - 4)
            for i in range(r) for j in range(i + 1, r)
        )
    return factorial(k) * unlabeled


def is_odd_coloring(parts, colors):
    blocks = []
    start = 0
    for n in parts:
        blocks.append(range(start, start + n))
        start += n
    used_by_part = [{colors[v] for v in B} for B in blocks]
    for i in range(len(blocks)):
        for j in range(i + 1, len(blocks)):
            if used_by_part[i] & used_by_part[j]:
                return False
    for i in range(len(blocks)):
        counts = {}
        for j, B in enumerate(blocks):
            if j == i:
                continue
            for v in B:
                counts[colors[v]] = counts.get(colors[v], 0) + 1
        if not any(m % 2 for m in counts.values()):
            return False
    return True


def count_colorings(parts, k):
    n = sum(parts)
    total = 0
    for colors in product(range(k), repeat=n):
        if len(set(colors)) != k:
            continue
        if is_odd_coloring(parts, colors):
            total += 1
    return total


def exists_coloring(parts, k):
    if k <= 0:
        return False
    n = sum(parts)
    for colors in product(range(k), repeat=n):
        if is_odd_coloring(parts, colors):
            return True
    return False


def main():
    checked = 0
    for r in (2, 3):
        for parts in product((1, 2, 3), repeat=r):
            if sum(parts) > 7:
                continue
            k = predicted_k(parts)
            assert exists_coloring(parts, k), (parts, 'predicted k not feasible')
            assert not exists_coloring(parts, k - 1), (parts, 'smaller k feasible')
            actual = count_colorings(parts, k)
            expected = predicted_count(parts)
            assert actual == expected, (parts, actual, expected)
            checked += 1
    print(f'ALL_CHECKS_PASSED cases={checked}')


if __name__ == '__main__':
    main()
