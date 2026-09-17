"""Exact threshold-two burning, with independently checkable schedules."""
import random


def solve(g):
    n = len(g)
    adj = [sum(1 << v for v in g[u]) for u in range(n)]
    full = (1 << n) - 1
    states = {0: (0, ())}
    for time in range(1, n + 1):
        nxt = {}
        for mask, (cost, seq) in states.items():
            spread = mask
            for u in range(n):
                if (mask & adj[u]).bit_count() >= 2:
                    spread |= 1 << u
            for u in [-1] + [u for u in range(n) if not mask >> u & 1]:
                new = spread if u < 0 else spread | (1 << u)
                val = (cost + (u >= 0), seq + (u,))
                if new not in nxt or val[0] < nxt[new][0]:
                    nxt[new] = val
        if full in nxt:
            return time, *nxt[full]
        states = nxt


if __name__ == '__main__':
    rng = random.Random(314159)
    for trial in range(10000):
        n = rng.randrange(5, 11)
        h = [set() for _ in range(n)]
        for v in range(1, n):
            u = rng.randrange(v)
            h[u].add(v)
            h[v].add(u)
        for u in range(n):
            for v in range(u + 1, n):
                if rng.random() < 0.15:
                    h[u].add(v)
                    h[v].add(u)
        bh, th, sh = solve(h)
        for u, v in [(u, v) for u in range(n) for v in range(u + 1, n) if v not in h[u]]:
            g = [s.copy() for s in h]
            g[u].add(v)
            g[v].add(u)
            bg, tg, sg = solve(g)
            if tg > th:
                print('H', [(u,v) for u in range(n) for v in h[u] if u<v], 'add', (u, v), flush=True)
                print('H:', (bh, th, sh), 'G:', (bg, tg, sg), flush=True)
                raise SystemExit
