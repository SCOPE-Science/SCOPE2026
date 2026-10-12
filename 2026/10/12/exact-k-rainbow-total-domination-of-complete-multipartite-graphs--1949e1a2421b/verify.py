from itertools import product


def integer_partitions(n, lo=1):
    if n == 0:
        yield ()
        return
    for first in range(lo, n + 1):
        for rest in integer_partitions(n - first, first):
            yield (first,) + rest


def formula(sizes, k):
    N = sum(sizes)
    s = min(sizes)
    q = k // 2
    h = k if s <= q else s + q + 1
    return min(N, 2 * k, h)


def valid_assignment(labels, part_of, k):
    r = max(part_of) + 1
    union_part = [0] * r
    for lab, p in zip(labels, part_of):
        union_part[p] |= lab
    full = (1 << k) - 1
    outside = [0] * r
    for i in range(r):
        u = 0
        for j in range(r):
            if i != j:
                u |= union_part[j]
        outside[i] = u
    for lab, p in zip(labels, part_of):
        if lab == 0:
            if outside[p] != full:
                return False
        elif lab & (lab - 1) == 0:
            if not (outside[p] & lab):
                return False
    return True


def brute_minimum(sizes, k):
    part_of = []
    for i, n in enumerate(sizes):
        part_of.extend([i] * n)
    masks = range(1 << k)
    best = sum(sizes)
    checked = 0
    for labels in product(masks, repeat=sum(sizes)):
        checked += 1
        w = sum(x.bit_count() for x in labels)
        if w >= best:
            continue
        if valid_assignment(labels, part_of, k):
            best = w
    return best, checked


def published_bipartite(a, b, k):
    if a > b:
        a, b = b, a
    if a + b <= k:
        return a + b
    if a <= k // 2:
        return k
    middle = a + (k + 2) // 2
    threshold = (3 * k - 2 + 1) // 2
    if a < threshold:
        return middle
    return 2 * k


def main():
    profiles = 0
    cases = 0
    assignments = 0
    for N in range(2, 6):
        for sizes in integer_partitions(N):
            if len(sizes) < 2:
                continue
            profiles += 1
            for k in (2, 3, 4):
                cases += 1
                got, checked = brute_minimum(sizes, k)
                assignments += checked
                want = formula(sizes, k)
                if got != want:
                    raise AssertionError((sizes, k, got, want))

    bip = 0
    for a in range(1, 21):
        for b in range(a, 21):
            for k in range(2, 13):
                bip += 1
                got = formula((a, b), k)
                want = published_bipartite(a, b, k)
                if got != want:
                    raise AssertionError(('bipartite', a, b, k, got, want))

    print('ALL CHECKS PASSED; '
          f'exhaustive_profiles={profiles}; exhaustive_cases={cases}; '
          f'assignments={assignments}; bipartite_specializations={bip}; '
          'orders=2..5; k=2..4')


if __name__ == '__main__':
    main()
