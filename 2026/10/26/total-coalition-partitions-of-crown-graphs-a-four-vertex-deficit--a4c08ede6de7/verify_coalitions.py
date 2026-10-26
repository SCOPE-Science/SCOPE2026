"""Exact independent checks for total-coalition partitions of crown graphs.

No optional dependencies. Run: python verify_coalitions.py
"""
from collections import Counter
from math import factorial


def profile_partitions(n, limit):
    """All admissible part-size multisets of deficit <= limit, with counts.

    Unlabelled block profiles (a,b) have a+b>0, a<2 or b<2.
    Singleton blocks are added from unused vertices and have zero deficit.
    """
    types = [(a, b) for a in range(n + 1) for b in range(n + 1)
             if 2 <= a + b <= limit + 1 and (a < 2 or b < 2)]
    types.sort(key=lambda x: (sum(x) - 1, x))
    results = []

    def admissible(ps):
        for i, (a, b) in enumerate(ps):
            if not any(j != i and a + c >= 2 and b + d >= 2
                       for j, (c, d) in enumerate(ps)):
                return False
        return True

    def walk(start, ua, vb, deficit, nontrivial):
        if ua > n or vb > n or deficit > limit:
            return
        profiles = nontrivial + [(1, 0)] * (n - ua) + [(0, 1)] * (n - vb)
        if admissible(profiles):
            mult = Counter(profiles)
            denominator = 1
            for (a, b), freq in mult.items():
                denominator *= factorial(a) ** freq * factorial(b) ** freq * factorial(freq)
            num = factorial(n) ** 2 // denominator
            assert num * denominator == factorial(n) ** 2
            results.append((len(profiles), tuple(sorted(profiles)), num))
        for i in range(start, len(types)):
            a, b = types[i]
            c = a + b - 1
            if deficit + c > limit:
                break
            if ua + a <= n and vb + b <= n:
                nontrivial.append((a, b))
                walk(i, ua + a, vb + b, deficit + c, nontrivial)
                nontrivial.pop()

    walk(0, 0, 0, 0, [])
    return results


def directly_enumerate(n):
    """Every unlabelled set partition, tested against actual graph adjacency."""
    neighbors = []
    for i in range(n):
        neighbors.append(sum(1 << (n + j) for j in range(n) if i != j))
    for j in range(n):
        neighbors.append(sum(1 << i for i in range(n) if i != j))
    all_mask = (1 << (2 * n)) - 1
    top, count = 0, 0

    def is_td(mask):
        return all(mask & nbr for nbr in neighbors)

    def recurse(v, blocks):
        nonlocal top, count
        if v == 2 * n:
            if any(is_td(b) for b in blocks):
                return
            if any(not any(i != j and is_td(a | b)
                           for j, b in enumerate(blocks))
                   for i, a in enumerate(blocks)):
                return
            k = len(blocks)
            if k > top:
                top, count = k, 0
            if k == top:
                count += 1
            return
        for i in range(len(blocks)):
            blocks[i] |= 1 << v
            recurse(v + 1, blocks)
            blocks[i] ^= 1 << v
        blocks.append(1 << v)
        recurse(v + 1, blocks)
        blocks.pop()

    recurse(0, [])
    return top, count


def main():
    expected = {3: (3, 48), 4: (4, 857)}
    for n in range(3, 10):
        limit = min(2 * n - 1, 4)
        all_ps = profile_partitions(n, limit)
        assert all_ps
        top = max(k for k, _, _ in all_ps)
        count = sum(c for k, _, c in all_ps if k == top)
        want = expected.get(n, (2 * n - 4, (n * (n - 1) * (n - 2) // 2) ** 2))
        assert (top, count) == want, (n, top, count, want)
        if n >= 5:
            winners = [(p, c) for k, p, c in all_ps if k == top]
            assert len(winners) == 1
            a, b = (1, 2), (2, 1)
            assert winners[0][0].count(a) == 1 and winners[0][0].count(b) == 1
        print(f'profile n={n}: TC={top}, optimal={count}')
    for n in range(3, 6):
        direct = directly_enumerate(n)
        assert direct == expected.get(n, (2 * n - 4, (n * (n - 1) * (n - 2) // 2) ** 2))
        print(f'direct n={n}: TC={direct[0]}, optimal={direct[1]}')


if __name__ == '__main__':
    main()
