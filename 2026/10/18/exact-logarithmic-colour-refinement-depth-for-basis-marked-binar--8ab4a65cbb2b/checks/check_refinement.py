"""Direct 1-WL computation for basis-marked binary projective incidence graphs.

Usage: python checks/check_refinement.py
No external modules required.
"""
from collections import Counter
from math import ceil, log2, comb


def compress(signatures):
    lookup = {}
    return [lookup.setdefault(s, len(lookup)) for s in signatures]


def refinement(d):
    n = (1 << d) - 1
    lines = [(a, b, a ^ b) for a in range(1, n + 1)
             for b in range(a + 1, n + 1) if a ^ b > b]
    assert len(lines) == n * (n - 1) // 6
    edges = [[] for _ in range(n + len(lines))]
    for i, triple in enumerate(lines, n):
        for x in triple:
            edges[x-1].append(i)
            edges[i].append(x-1)
    colors = compress([('point', i) if i in [1 << j for j in range(d)]
                       else ('point', -1) for i in range(1, n+1)]
                      + [('line', -1)] * len(lines))
    if d == 2:
        predicted = 0
    else:
        k = ceil(log2(d - 1))
        t = 1 << (k - 1)
        predicted = 2*k if d <= t + 2 else 2*k + 1
    first_discrete = None
    for r in range(predicted + 1):
        if len(set(colors)) == len(colors) and first_discrete is None:
            first_discrete = r
        threshold = 1 << (r // 2)
        T = {x for x in range(1, n+1) if x.bit_count() <= threshold}
        for x in T:
            assert colors[x-1] not in [colors[y-1] for y in range(1,n+1) if y != x], (d,r,x)
        U = [colors[x-1] for x in range(1,n+1) if x not in T]
        assert len(set(U)) <= 1, (d,r,'nonuniform remainder')
        assert len(set(colors[:n])) == len(T) + int(bool(U)), (d,r,'unexpected points')
        if r == predicted:
            break
        nxt = [(colors[i], tuple(sorted(Counter(colors[v] for v in edges[i]).items())))
               for i in range(len(colors))]
        colors = compress(nxt)
    assert first_discrete == predicted, (d, first_discrete, predicted)
    return d, n, len(lines), predicted


def main():
    for d in range(2, 10):
        print('PASS', *refinement(d))
    print('PASS direct incidence refinement, dimensions 2..9')

if __name__ == '__main__':
    main()
