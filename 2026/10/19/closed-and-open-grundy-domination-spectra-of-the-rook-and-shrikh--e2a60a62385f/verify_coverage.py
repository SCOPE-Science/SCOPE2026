"""Exact closed/open-neighborhood sequence enumerator on two 16-vertex graphs.

Vertex convention: vertex 4*r+c represents (r,c) in Z_4 x Z_4.
No external mathematical software is needed.
"""
import json
from functools import lru_cache
from pathlib import Path

N = 16
FULL = (1 << N) - 1
DIFFERENCES = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1))


def edges(kind):
    E = set()
    for i in range(N):
        r, c = divmod(i, 4)
        if kind == 'rook':
            neighbours = [j for j in range(N) if j != i and (j // 4 == r or j % 4 == c)]
        elif kind == 'shrikhande':
            neighbours = [4 * ((r + dr) % 4) + ((c + dc) % 4) for dr, dc in DIFFERENCES]
        else:
            raise ValueError(kind)
        for j in neighbours:
            if i != j:
                E.add(tuple(sorted((i, j))))
    return sorted(E)


def verify_srg(E):
    ad = [set() for _ in range(N)]
    for u, v in E:
        ad[u].add(v)
        ad[v].add(u)
    assert all(len(ad[v]) == 6 for v in range(N))
    for u in range(N):
        for v in range(u + 1, N):
            assert len(ad[u] & ad[v]) == 2
    return ad


def do_case(name, typ):
    E = edges(name)
    adj = verify_srg(E)
    open_masks = [sum(1 << v for v in adj[u]) for u in range(N)]
    bits = [(open_masks[u] | (1 << u)) if typ == 'closed' else open_masks[u] for u in range(N)]

    @lru_cache(maxsize=None)
    def f(mask):
        if mask == FULL:
            return (1,)  # One empty completion; coefficient index is additional length.
        polynomial = [0] * (N + 1)
        for i in range(N):
            nxt = mask | bits[i]
            if nxt != mask:
                coeffs = f(nxt)
                for j, count in enumerate(coeffs):
                    polynomial[j + 1] += count
        while polynomial and polynomial[-1] == 0:
            polynomial.pop()
        return tuple(polynomial)

    co = f(0)
    print(name, typ, 'states', f.cache_info().currsize,
          'spectrum', [(k, n) for k, n in enumerate(co) if n])
    largest = max(i for i, c in enumerate(co) if c)
    smallest = min(i for i, c in enumerate(co) if c)
    witness = []
    m = 0
    steps = largest
    while steps:
        for i in range(N):
            nxt = m | bits[i]
            if nxt != m and len(f(nxt)) >= steps and f(nxt)[steps - 1]:
                witness.append(i)
                m = nxt
                steps -= 1
                break
        else:
            raise AssertionError('No witness')
    assert m == FULL and len(witness) == largest

    all_masks = []
    # Compute reachable states explicitly in a separate forward walk.
    reachable = {0}
    pending = [0]
    while pending:
        s = pending.pop()
        for b in bits:
            t = s | b
            if t != s and t not in reachable:
                reachable.add(t)
                pending.append(t)
    assert len(reachable) == f.cache_info().currsize
    for mask in sorted(reachable):
        all_masks.append([mask, list(f(mask))])
    return {'graph': name, 'neighborhood': typ, 'edges': E,
            'states': len(all_masks), 'min_length': smallest,
            'max_length': largest, 'max_witness': witness,
            'spectrum': [[i, int(c)] for i, c in enumerate(co) if c],
            'state_polynomials': all_masks}


def main():
    cases = []
    for graph in ('rook', 'shrikhande'):
        for typ in ('closed', 'open'):
            cases.append(do_case(graph, typ))
    cert = {'n': N, 'vertex_convention': '(r,c) maps to 4*r+c', 'cases': cases}
    output = Path(__file__).with_name('coverage_certificate.json')
    output.write_text(json.dumps(cert, sort_keys=True, separators=(',', ':')) + '\n', encoding='utf-8')
    print('wrote', output.name, output.stat().st_size, 'bytes')

if __name__ == '__main__':
    main()
