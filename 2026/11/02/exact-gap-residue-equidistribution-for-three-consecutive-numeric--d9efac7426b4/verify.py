"""Independent finite check of the equidistribution classification.

Usage: python verify.py; stdlib only.
"""
from collections import Counter
from math import gcd


def gaps(n):
    # Dijkstra on residues modulo n from generators n+1 and n+2.
    import heapq
    w = [None] * n
    w[0] = 0
    queue = [(0, 0)]
    while queue:
        cost, r = heapq.heappop(queue)
        if w[r] != cost:
            continue
        for generator in (n+1, n+2):
            s = (r+generator) % n
            v = cost+generator
            if w[s] is None or v < w[s]:
                w[s] = v
                heapq.heappush(queue, (v, s))
    result = []
    for r in range(1, n):
        result.extend(range(r, w[r], n))
    return result


def theorem(n, m):
    if n % 2 == 0:
        return False
    h = (n-1)//2
    return (h+1) % m == 0 or (h % m == 0 and gcd(m, 3) == 1)


def verify():
    tests = 0
    for n in range(3, 171):
        gs = gaps(n)
        genus = ((n-1)//2)*((n+1)//2) if n%2 else (n//2)**2
        assert len(gs) == genus, (n, len(gs), genus)
        for m in range(2, min(3 * n, 220)):
            frequencies = Counter(g % m for g in gs)
            actual = len(gs) % m == 0 and all(frequencies[r] == len(gs)//m for r in range(m))
            predicted = theorem(n, m)
            assert actual == predicted, (n, m, actual, predicted)
            tests += 1
    print('VERIFY_OK: %d parameter-modulus pairs, n=3..170, all genus counts correct' % tests)


if __name__ == '__main__':
    verify()
