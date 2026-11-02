#!/usr/bin/env python3
"""Independent exhaustive checks for circular maximal repetitions in binary B(2,5)."""
from collections import Counter

N = 32


def from_feedback():
    """Exhaust all 16-bit nonsingular 5-stage feedback tables."""
    answer = set()
    for g in range(1 << 16):
        state = 0
        seen = set()
        letters = []
        for _ in range(N):
            if state in seen:
                break
            seen.add(state)
            letters.append(str(state >> 4))
            state = ((state << 1) & 31) | ((state >> 4) ^ ((g >> (state & 15)) & 1))
        if len(seen) == N and state == 0:
            w = ''.join(letters)
            assert len({''.join(w[(i + j) % N] for j in range(5)) for i in range(N)}) == N
            answer.add(w)
    return answer


def from_euler_tours():
    """Exhaust local edge orders of the order-4 binary de Bruijn digraph."""
    answer = set()
    for choices in range(1 << 16):
        outgoing = []
        for v in range(16):
            edges = [(((v << 1) & 15) | bit, (v << 1) | bit) for bit in (0, 1)]
            if (choices >> v) & 1:
                edges.reverse()
            outgoing.append(edges)
        stack = [(0, -1)]
        tour = []
        while stack:
            v, _ = stack[-1]
            if outgoing[v]:
                dst, edge = outgoing[v].pop()
                stack.append((dst, edge))
            else:
                _, edge = stack.pop()
                if edge >= 0:
                    tour.append(edge)
        tour.reverse()
        assert len(tour) == 32 and len(set(tour)) == 32
        w = ''.join(str(e >> 4) for e in tour)
        start = next(i for i in range(32)
                     if ''.join(w[(i + j) % 32] for j in range(5)) == '00000')
        answer.add(w[start:] + w[:start])
    return answer


def runs_via_period_equalities(w):
    """Find each circular run as a maximal block of p-shift equalities."""
    output = set()
    n = len(w)
    for p in range(1, 5):
        agree = [w[i] == w[(i + p) % n] for i in range(n)]
        for start in range(n):
            if not agree[start] or agree[(start - 1) % n]:
                continue
            t = 0
            while t < n and agree[(start + t) % n]:
                t += 1
            if t < p:
                continue
            length = t + p
            if any(all(w[(start + j) % n] == w[(start + j + q) % n]
                       for j in range(length - q)) for q in range(1, p)):
                continue
            output.add((start, p, length))
    return output


def runs_via_interval_definition(w):
    """Independent direct minimal-period and two-sided-extension checks."""
    n = len(w)
    result = set()
    for start in range(n):
        for length in range(2, 9):
            for p in range(1, length // 2 + 1):
                if not all(w[(start + j) % n] == w[(start + j + p) % n]
                           for j in range(length - p)):
                    continue
                if any(all(w[(start + j) % n] == w[(start + j + q) % n]
                           for j in range(length - q)) for q in range(1, p)):
                    continue
                if w[(start - 1) % n] == w[(start - 1 + p) % n]:
                    continue
                if w[(start + length) % n] == w[(start + length - p) % n]:
                    continue
                result.add((start, p, length))
    return result


def fkm(k, n):
    """Independent Fredricksen-Kessler-Maiorana construction for q-ary sanity checks."""
    a = [0] * (k * n + 1)
    result = []
    def rec(t, p):
        if t > n:
            if n % p == 0:
                result.extend(a[1:p + 1])
        else:
            a[t] = a[t-p]
            rec(t+1, p)
            for j in range(a[t-p]+1, k):
                a[t] = j
                rec(t+1, t)
    rec(1, 1)
    return result


def check_general_small_instances():
    for q, order in ((2, 3), (2, 4), (2, 5), (2, 6), (3, 3), (3, 4)):
        w = fkm(q, order)
        n = len(w)
        assert n == q**order
        assert len({tuple(w[(i+j) % n] for j in range(order)) for i in range(n)}) == n
        for p in range(1, (order-1)//2+1):
            # Detect circular runs by p-shift equalities, without order-five assumptions.
            agree = [w[i] == w[(i+p) % n] for i in range(n)]
            found = 0
            for i in range(n):
                if not agree[i] or agree[(i-1) % n]:
                    continue
                t = 0
                while t<n and agree[(i+t) % n]:
                    t+=1
                if t < p:
                    continue
                L = t+p
                if any(all(w[(i+j) % n]==w[(i+j+d) % n]
                           for j in range(L-d)) for d in range(1,p)):
                    continue
                found += 1
            primitive = sum(all(tuple(w0) != tuple(w0[:d])*(p//d)
                                for d in range(1,p) if p%d==0)
                            for w0 in __import__('itertools').product(range(q), repeat=p))
            expected = (q-1)*primitive*q**(order-2*p-1)
            assert found == expected, (q, order, p, found, expected)


def main():
    by_feedback = from_feedback()
    by_euler = from_euler_tours()
    assert len(by_feedback) == len(by_euler) == 2048
    assert by_feedback == by_euler
    counts = Counter()
    profiles = Counter()
    lengths = Counter()
    for w in by_feedback:
        r1 = runs_via_period_equalities(w)
        r2 = runs_via_interval_definition(w)
        assert r1 == r2, (w, r1, r2)
        c = tuple(sum(period == p for _, period, _ in r1) for p in range(1, 5))
        assert c[0:2] == (8, 2)
        profiles[c] += 1
        counts[len(r1)] += 1
        lengths.update((p, length) for _, p, length in r1)
    assert counts == {12: 1008, 13: 736, 14: 304}, counts
    assert profiles == {
        (8, 2, 2, 0): 768, (8, 2, 2, 1): 608, (8, 2, 2, 2): 304,
        (8, 2, 1, 1): 224, (8, 2, 1, 2): 128, (8, 2, 0, 2): 16,
    }, profiles
    assert lengths == {
        (1, 2): 8192, (1, 3): 4096, (1, 5): 4096,
        (2, 4): 1536, (2, 5): 1024, (2, 6): 1536,
        (3, 6): 1792, (3, 7): 1920, (4, 8): 1728,
    }, lengths
    check_general_small_instances()
    print('cycles=2048; profile=', sorted(profiles.items()))
    print('total_run_counts=', sorted(counts.items()))
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
