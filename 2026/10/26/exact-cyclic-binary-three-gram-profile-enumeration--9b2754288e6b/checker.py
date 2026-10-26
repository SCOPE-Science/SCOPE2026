"""Independent checks for the cyclic binary three-gram profile generating function."""
from collections import defaultdict
from itertools import product
from math import comb


def profile(word):
    n = len(word)
    counts = [0] * 8
    for i in range(n):
        idx = 4 * word[i] + 2 * word[(i + 1) % n] + word[(i + 2) % n]
        counts[idx] += 1
    return tuple(counts)


def by_words(n):
    return len({profile(bits) for bits in product((0, 1), repeat=n)})


def connected(edges):
    active = set()
    adjacency = [set() for _ in range(4)]
    for t, multiplicity in enumerate(edges):
        if not multiplicity:
            continue
        v, u = t // 2, t % 4
        adjacency[v].add(u)
        adjacency[u].add(v)
        active.update((v, u))
    if not active:
        return False
    stack = [next(iter(active))]
    visited = set(stack)
    while stack:
        for u in adjacency[stack.pop()]:
            if u not in visited:
                visited.add(u)
                stack.append(u)
    return visited == active


def by_flows(n):
    """Enumerate balance solutions, then test connectivity directly, no five-case split."""
    result = 0
    for a in range(n + 1):
        for h in range(n - a + 1):
            for p in range((n - a - h) // 2 + 1):
                for q in range((n - a - h - 2 * p) // 2 + 1):
                    # Flow constraints force x001=x100=p, x011=x110=q,
                    # and x101 = x010+q-p.
                    # From n=a+h+2p+2q+r+s and s=r+q-p,
                    # 2r = n-a-h-p-3q.
                    top = n - a - h - p - 3 * q
                    if top < 0 or top % 2:
                        continue
                    r = top // 2
                    s = r + q - p
                    if s < 0:
                        continue
                    edges = (a, p, r, q, p, s, q, h)
                    if sum(edges) == n and connected(edges):
                        result += 1
    return result


def coefficients(n_max):
    """Power-series multiplication of five disjoint structural generating series."""
    cs = [0] * (n_max + 1)
    for n in range(1, n_max + 1):
        cs[n] += 2
    for n in range(2, n_max + 1, 2):
        cs[n] += 1
    for base in range(2):
        for p in range(1, n_max // 3 + 1):
            for r in range(n_max // 2 + 1):
                for t in range(n_max - 3 * p - 2 * r + 1):
                    cs[3 * p + 2 * r + t] += 1
    for p in range(1, n_max // 4 + 1):
        for t in range((n_max - 4 * p) // 3 + 1):
            for k in range((n_max - 4 * p - 3 * t) // 2 + 1):
                for a in range(n_max - 4 * p - 3 * t - 2 * k + 1):
                    for h in range(n_max - 4 * p - 3 * t - 2 * k - a + 1):
                        cs[4 * p + 3 * t + 2 * k + a + h] += 1
    for q in range(1, n_max // 4 + 1):
        for t in range(1, (n_max - 4 * q) // 3 + 1):
            for k in range((n_max - 4 * q - 3 * t) // 2 + 1):
                for a in range(n_max - 4 * q - 3 * t - 2 * k + 1):
                    for h in range(n_max - 4 * q - 3 * t - 2 * k - a + 1):
                        cs[4 * q + 3 * t + 2 * k + a + h] += 1
    return cs


def run():
    # GF enumerated independently by expanding five geometric families.
    gf = coefficients(19)
    for n in range(1, 20):
        brute = by_flows(n)
        assert brute == gf[n], ("balanced flow", n, brute, gf[n])
    for n in range(1, 16):
        brute = by_words(n)
        assert brute == gf[n], ("binary words", n, brute, gf[n])
    assert gf[1:19] == [2,3,4,6,8,13,18,27,38,53,72,98,128,167,214,271,338,419]
    print("CYCLIC_BINARY_TRIGRAM_PASS direct_n=1..15 flow_n=1..19 sequence=" + ",".join(map(str, gf[1:19])))


if __name__ == "__main__":
    run()
