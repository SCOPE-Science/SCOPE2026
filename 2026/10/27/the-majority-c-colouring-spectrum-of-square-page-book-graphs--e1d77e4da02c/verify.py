"""Independent exhaustive verification of majority C-colouring on square-page books.

No nonstandard packages are required. Run with Python 3.8+.
"""
from collections import Counter
from math import comb, factorial


def stirling_second(n, k):
    if n == k == 0:
        return 1
    if n == 0 or k == 0 or k > n:
        return 0
    row = [1] + [0] * n
    for i in range(1, n + 1):
        new = [0] * (n + 1)
        for j in range(1, i + 1):
            new[j] = j * row[j] + row[j - 1]
        row = new
    return row[k]


def multinomial(parts):
    rem = sum(parts)
    ans = 1
    for a in parts:
        ans *= comb(rem, a)
        rem -= a
    return ans


def formula(n):
    a = n // 2  # minimum whole pages absorbed by equal-coloured spine
    h = (n + 2) // 2  # endpoint quota for differently coloured spine
    out = Counter()
    for u in range(a, n + 1):
        z = n - u
        for c in range(1, z + 2):
            out[c] += comb(n, u) * stirling_second(z, c - 1)
    for p in range(n + 1):
        for x in range(n - p + 1):
            for y in range(n - p - x + 1):
                z = n - p - x - y
                if p + x < h or p + y < h:
                    continue
                m = multinomial((p, x, y, z))
                for c in range(2, z + 3):
                    out[c] += m * stirling_second(z, c - 2)
    return {k: v for k, v in sorted(out.items()) if v}


def graph(n):
    adj = [set() for _ in range(2 * n + 2)]
    def edge(a, b):
        adj[a].add(b)
        adj[b].add(a)
    edge(0, 1)
    for i in range(n):
        u, v = 2 + 2 * i, 3 + 2 * i
        edge(0, u)
        edge(u, v)
        edge(v, 1)
    return adj


def brute(n):
    adj = graph(n)
    size = len(adj)
    counts = Counter()
    tested = 0
    labels = [0] * size

    def iterate(pos, largest):
        nonlocal tested
        if pos == size:
            tested += 1
            for v in range(size):
                matches = sum(labels[v] == labels[w] for w in adj[v])
                if 2 * matches < len(adj[v]):
                    return
            counts[largest + 1] += 1
            return
        for color in range(largest + 2):
            labels[pos] = color
            iterate(pos + 1, max(largest, color))

    iterate(1, 0)
    return dict(sorted(counts.items())), tested


if __name__ == '__main__':
    for n in range(1, 5):
        measured, tested = brute(n)
        predicted = formula(n)
        assert measured == predicted, (n, measured, predicted)
        max_colors = (n + 3) // 2
        assert max(predicted) == max_colors
        assert predicted[max_colors] == comb(n + 1, (n + 2) // 2)
        print(f'n={n}; set_partitions_checked={tested}; spectrum={measured}; max={max_colors}; optimal_unlabelled={predicted[max_colors]}; optimal_named={factorial(max_colors)*predicted[max_colors]}')
    for n in range(5, 21):
        predicted = formula(n)
        k = (n + 3) // 2
        assert max(predicted) == k
        assert predicted[k] == comb(n+1, (n+2)//2)
    print('VERIFY_OK: exhaustive graph partitions n=1..4; arithmetic identities n=5..20')
