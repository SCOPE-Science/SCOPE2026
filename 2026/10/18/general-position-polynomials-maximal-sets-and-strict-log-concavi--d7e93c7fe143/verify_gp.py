"""Independent exhaustive verification for complements of simple cycles.

Run: python verify_gp.py
"""
from collections import Counter
from itertools import combinations
from math import comb


def predicted_ordinary(n):
    result = Counter({k: n * comb(n-k, k) // (n-k)
                      for k in range(n//2 + 1)})
    result[2] += n
    result[3] += n
    return result


def predicted_maximal(n):
    if n == 5:
        return Counter({3: 5})
    if n == 6:
        return Counter({2: 3, 3: 8})
    result = Counter({3: n})
    for k in range((n+2)//3, n//2+1):
        val = n * comb(k, n-2*k) // k
        result[k] += val
    return result


def compute(n):
    # Complement-of-cycle neighborhoods.
    neighbors = [set(range(n)) - {i, (i-1)%n, (i+1)%n}
                 for i in range(n)]
    distances = [[1000]*n for _ in range(n)]
    for v in range(n):
        distances[v][v] = 0
        todo = [v]
        for u in todo:
            for w in neighbors[u]:
                if distances[v][w] == 1000:
                    distances[v][w] = distances[v][u] + 1
                    todo.append(w)
    assert max(max(row) for row in distances) == 2
    forbidden = []
    for a, b, c in combinations(range(n), 3):
        if (distances[a][b] + distances[b][c] == distances[a][c] or
            distances[a][c] + distances[c][b] == distances[a][b] or
            distances[b][a] + distances[a][c] == distances[b][c]):
            forbidden.append((1<<a)|(1<<b)|(1<<c))
    ok = [True] * (1 << n)
    for mask in range(1 << n):
        ok[mask] = not any(mask & t == t for t in forbidden)
    total = Counter()
    maximal = Counter()
    for mask in range(1 << n):
        if ok[mask]:
            size = mask.bit_count()
            total[size] += 1
            if not any(ok[mask | (1<<v)] for v in range(n)
                       if not mask & (1<<v)):
                maximal[size] += 1
    return total, maximal, len(forbidden)


def main():
    total_masks = 0
    forbidden_count = 0
    for n in range(5, 15):
        ordinary, maximal, bad = compute(n)
        assert ordinary == predicted_ordinary(n), (n,'ordinary',ordinary,predicted_ordinary(n))
        assert maximal == predicted_maximal(n), (n,'maximal',maximal,predicted_maximal(n))
        total_masks += 1 << n
        forbidden_count += bad
        print('n=%02d gp=%d lower_gp=%d ordinary=%s maximal=%s' % (
            n, max(ordinary), min(maximal),
            list(sorted(ordinary.items())), list(sorted(maximal.items()))))
    print('VERIFICATION_OK n=5..14 examined_subsets=%d forbidden_triples=%d' %
          (total_masks, forbidden_count))

if __name__ == '__main__':
    main()
