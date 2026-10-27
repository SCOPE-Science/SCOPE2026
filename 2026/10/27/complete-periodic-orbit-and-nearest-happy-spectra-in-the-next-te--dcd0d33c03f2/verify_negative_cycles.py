"""Exact, finite certificate for the periodic-point spectra in negative bases -11 through -20.
Run alongside negative_cycles_witnesses.json with Python 3.10+.
"""
import json
from collections import deque
from pathlib import Path

HERE = Path(__file__).resolve().parent
RECORDS = json.loads((HERE / "negative_cycles_witnesses.json").read_text(encoding="utf-8"))


def squsum_divmod(n, p):
    acc = 0
    while n != 0:
        q, d = divmod(n, -p)
        if d < 0:
            q += 1
            d += p
        assert 0 <= d < p
        acc += d*d
        n = q
    return acc


def squsum_recurrence(n, p):
    # Distinct digit extraction: n = r - p*q with 0 <= r < p.
    acc = 0
    while n:
        r = n % p
        n = (r - n) // p
        acc += r*r
    return acc


def normalize(c):
    i = c.index(min(c))
    return c[i:] + c[:i]


def walk_cycles(edges):
    visited = set()
    output = []
    for seed in range(1, len(edges)):
        if seed in visited:
            continue
        path, seen = [], {}
        x = seed
        while x not in visited and x not in seen:
            seen[x] = len(path)
            path.append(x)
            x = edges[x]
        if x in seen:
            output.append(normalize(path[seen[x]:]))
        visited.update(path)
    return sorted(output, key=lambda c: (len(c), c))


def peel_cycles(edges):
    N = len(edges) - 1
    indegrees = [0]*(N+1)
    for x in range(1, N+1):
        indegrees[edges[x]] += 1
    queue = deque(x for x in range(1, N+1) if indegrees[x] == 0)
    while queue:
        v = queue.popleft()
        t = edges[v]
        indegrees[t] -= 1
        if indegrees[t] == 0:
            queue.append(t)
    remaining = {x for x in range(1, N+1) if indegrees[x] > 0}
    output = []
    while remaining:
        cur = min(remaining)
        cyc = []
        while cur in remaining:
            remaining.remove(cur)
            cyc.append(cur)
            cur = edges[cur]
        assert cur == cyc[0]
        output.append(normalize(cyc))
    return sorted(output, key=lambda c: (len(c), c))


def reaches_one(v, p):
    seen = set()
    while v not in seen:
        if v == 1:
            return True
        seen.add(v)
        v = squsum_recurrence(v, p)
    return False


def main():
    assert len(RECORDS) == 10
    for ix, row in enumerate(RECORDS):
        p = ix + 11
        assert row['base'] == -p
        B = (p-1)*(p*p-p+1)
        H = 3*(p-1)**2
        assert row['bound'] == B
        assert H < B
        assert (p**4-(p-1)*(p**3+p)) > B
        # Published descent bound B, coupled with the sharp one-step core H.
        for n in range(1, B+1):
            a = squsum_divmod(n,p)
            b = squsum_recurrence(n,p)
            assert a == b and 1 <= a <= H, (p,n,a,b)
        assert squsum_divmod(B,p) == H
        edges = [0]+[squsum_divmod(n,p) for n in range(1,H+1)]
        expected = sorted(row['cycles'], key=lambda c:(len(c),c))
        assert all(c == normalize(c) for c in expected)
        assert walk_cycles(edges) == expected
        assert peel_cycles(edges) == expected
        for cyc in expected:
            assert len(cyc) == len(set(cyc))
            for i, v in enumerate(cyc):
                assert edges[v] == cyc[(i+1)%len(cyc)]
        least = row['first_positive_happy_above_one']
        neg = row['largest_negative_happy_below_minus_one']
        assert least >= 2 and neg <= -2
        assert reaches_one(least,p)
        assert all(not reaches_one(k,p) for k in range(2,least))
        assert reaches_one(neg,p)
        assert all(not reaches_one(-k,p) for k in range(2,-neg))
        print(f'base=-{p}: sharp core={H}; graph checked (walk/peel); '
              f'{len(expected)} cycles, {sum(map(len,expected))} periodic points; '
              f'least happy >1 = {least}; greatest happy <-1 = {neg}')
    assert max(len(c) for r in RECORDS for c in r['cycles']) == 17
    row18 = next(r for r in RECORDS if r['base'] == -18)
    assert sum(1 for c in row18['cycles'] if len(c)==17) == 1
    print('VERIFIED: complete negative-base -11 through -20 cycle and nearest-happy spectra')

if __name__ == '__main__':
    main()
