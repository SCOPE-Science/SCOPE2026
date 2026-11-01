#!/usr/bin/env python3
"""Independent checks of primitive two-cycles on cycle graphs with leaves.
Scientific scope: standard synchronous degree-threshold chip-firing, no sink.
Run: python3 research30_sunlet_verify.py
"""
from itertools import product
from math import prod, isqrt


def graph(n, r):
    assert n >= 3 and r >= 1
    q = n * (r + 1)
    adj = [[] for _ in range(q)]
    for i in range(n):
        j = (i + 1) % n
        adj[i].append(j)
        adj[j].append(i)
        for b in range(r):
            u = n + i * r + b
            adj[i].append(u)
            adj[u].append(i)
    return adj


def step(x, adj, degree):
    f = [int(x[i] >= degree[i]) for i in range(len(x))]
    return tuple(x[i] - degree[i] * f[i] + sum(f[j] for j in adj[i])
                 for i in range(len(x)))


def direct_count(n, r):
    adj = graph(n, r)
    deg = [len(z) for z in adj]
    fixed_phases = 0
    hist = {}
    all_states = 0
    for state in product(*(range(2 * d) for d in deg)):
        all_states += 1
        nxt = step(state, adj, deg)
        if nxt != state and step(nxt, adj, deg) == state:
            fixed_phases += 1
            s = [int(state[i] >= deg[i]) for i in range(n)]
            cuts = sum(s[i] != s[(i+1) % n] for i in range(n))
            hist[cuts] = hist.get(cuts, 0) + 1
    assert fixed_phases % 2 == 0 and all(v % 2 == 0 for v in hist.values())
    return {c: v//2 for c, v in hist.items()}, all_states


def edge_histogram(n, r):
    # Even-parity edge boundaries encode a closed binary spin cycle.
    out = {}
    for e in product((0, 1), repeat=n):
        cuts = sum(e)
        if cuts % 2:
            continue
        ways = prod(r + e[(i-1) % n] + e[i] for i in range(n))
        out[cuts] = out.get(cuts, 0) + ways
    return out


def phase_sum_count(n, r):
    # Directly count heights for each core firing pattern, independently of
    # the edge-variable transfer-matrix derivation.
    phases = sum(prod(r + (s[i] != s[(i-1) % n]) +
                         (s[i] != s[(i+1) % n]) for i in range(n))
                 for s in product((0, 1), repeat=n))
    assert phases % 2 == 0
    return phases // 2


def signed_transfer_trace(n, r, sign):
    # Matrix M_s(a,b)=(r+a+b) s**b; independently multiply two-by-two.
    mat = ((r, sign * (r + 1)), (r + 1, sign * (r + 2)))
    p = ((1, 0), (0, 1))
    for _ in range(n):
        p = tuple(tuple(sum(p[i][k] * mat[k][j] for k in range(2))
                        for j in range(2)) for i in range(2))
    return p[0][0] + p[1][1]


def closed_integer(n, r):
    t0, t1 = 2, 2 * (r + 1)
    for _ in range(2, n + 1):
        t0, t1 = t1, 2 * (r + 1) * t1 + t0
    return (t1 + 2 * (-1)**n) // 2


def run():
    cases = [(3, 1), (4, 1), (5, 1), (3, 2), (4, 2), (3, 3)]
    total = 0
    for n, r in cases:
        expected = closed_integer(n, r)
        microhist, num = direct_count(n, r)
        micro = sum(microhist.values())
        edgehist = edge_histogram(n, r)
        assert microhist == edgehist, (n, r, microhist, edgehist)
        ph = phase_sum_count(n, r)
        trans = (signed_transfer_trace(n, r, 1)
                 + signed_transfer_trace(n, r, -1)) // 2
        assert micro == ph == trans == expected, (n, r, micro, ph, trans, expected)
        print(f'n={n} r={r} states={num} primitive_orbits={micro} interface_histogram={dict(sorted(microhist.items()))}')
        total += num
    for n in range(3, 31):
        for r in range(1, 16):
            ph = phase_sum_count(n, r) if n <= 15 else None
            trans = (signed_transfer_trace(n, r, 1)
                     + signed_transfer_trace(n, r, -1)) // 2
            z = closed_integer(n, r)
            assert trans == z and (ph is None or ph == z)
    print(f'FULL_MICROSCOPIC_CONFIGURATIONS_TESTED={total}')
    print('SUNLET_PRIMITIVE_TWO_CYCLE_VERIFY_OK')


if __name__ == '__main__':
    run()
