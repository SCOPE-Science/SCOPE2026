"""Exact independent checks of indegree-parity acyclic orientations of fan graphs.

Run: python3 fan_parity_verify.py
Standard library only. The independent enumeration tests literal directed cycles.
"""
from collections import defaultdict
from itertools import product


def transfer_counts(rim_bits):
    """Return count of acyclic orientations with these path-vertex parities."""
    if not rim_bits:
        raise ValueError('A fan requires at least one path vertex')
    dp = {(0, 1): 1, (1, 1): 1}
    for p in rim_bits[:-1]:
        nxt = defaultdict(int)
        for (y, z), c in dp.items():
            x = p ^ y ^ z
            nxt[(y, x)] += c
            if x != y:
                nxt[(1 - y, x)] += c
        dp = nxt
    return sum(c for (y, z), c in dp.items() if (y ^ z) == rim_bits[-1])


def forbidden_pattern(rim_bits):
    n = len(rim_bits)
    return (n % 2 == 0 and rim_bits[0] == rim_bits[-1] == 1
            and all(rim_bits[i] == rim_bits[i + 1] for i in range(1, n - 1, 2)))


def brute(n):
    edges = [(i, i+1) for i in range(n-1)] + [(n, i) for i in range(n)]
    counts = defaultdict(int)
    allcounts = defaultdict(int)
    num_acyclic = 0
    for mask in range(1 << len(edges)):
        indeg = [0] * (n+1)
        successors = [[] for _ in range(n+1)]
        for j, (a, b) in enumerate(edges):
            if (mask >> j) & 1:
                a, b = b, a
            indeg[b] += 1
            successors[a].append(b)
        sig = tuple(x % 2 for x in indeg)
        allcounts[sig] += 1
        pending = indeg[:]
        queue = [i for i, d in enumerate(pending) if d == 0]
        t = 0
        while t < len(queue):
            a = queue[t]
            t += 1
            for b in successors[a]:
                pending[b] -= 1
                if pending[b] == 0:
                    queue.append(b)
        if len(queue) == n+1:
            counts[sig] += 1
            num_acyclic += 1
    return counts, allcounts, num_acyclic


def test():
    total_edge_orientations = 0
    total_parity_comparisons = 0
    for n in range(2, 11):
        got, allcounts, total = brute(n)
        assert total == 2 * 3**(n-1), ('global acyclic count', n, total)
        for rim in product((0,1), repeat=n):
            rim = tuple(rim)
            hub = (1 + sum(rim)) % 2
            signature = rim + (hub,)
            dp = transfer_counts(rim)
            assert got[signature] == dp, ('transfer mismatch',n,signature,got[signature],dp)
            assert (dp == 0) == forbidden_pattern(rim), ('forbidden condition',n,signature,dp)
            assert allcounts[signature] == 2**(n-1), ('uniform unrestricted fibre',n,signature)
            total_parity_comparisons += 1
        print(f'fan n={n}: {1 << (2*n-1):,} orientations; {2**n} parity fibres; {total:,} acyclic',flush=True)
        total_edge_orientations += 1 << (2*n-1)
    # Independently exercise transfer and exact obstruction count on longer instances.
    for n in range(11, 17):
        count_forbidden = 0
        sum_counts = 0
        for rim in product((0,1),repeat=n):
            c = transfer_counts(rim)
            assert (c == 0) == forbidden_pattern(rim), ('extended criterion',n,rim)
            count_forbidden += not c
            sum_counts += c
        assert count_forbidden == (2**(n//2-1) if n%2==0 else 0)
        assert sum_counts == 2 * 3**(n-1)
        print(f'fan n={n}: {2**n:,} transfer fibres; {count_forbidden} forbidden',flush=True)
    print('VERIFIED',f'{total_edge_orientations:,} literal orientations;',
          f'{total_parity_comparisons:,} exhaustive signature comparisons')


if __name__ == '__main__':
    test()
