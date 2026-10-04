#!/usr/bin/env python3
from itertools import product
from pathlib import Path
import csv, json

ROOT = Path(__file__).resolve().parent


def ball_string(s):
    out = {s}
    for i, ch in enumerate(s):
        if ch == "0":
            out.add(s[:i] + s[i+1:])
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            out.add(s[:i] + s[i+1] + s[i] + s[i+2:])
    return out


def ball_tuple(s):
    a = tuple(int(c) for c in s)
    out = {a}
    for i, bit in enumerate(a):
        if bit == 0:
            out.add(a[:i] + a[i+1:])
    for i in range(len(a)-1):
        if a[i] != a[i+1]:
            b = list(a)
            b[i], b[i+1] = b[i+1], b[i]
            out.add(tuple(b))
    return {"".join(map(str, t)) for t in out}


def compatible_graph(n):
    words = ["".join(p) for p in product("01", repeat=n)]
    balls = []
    for w in words:
        b1 = ball_string(w)
        b2 = ball_tuple(w)
        assert b1 == b2, (n, w, b1 ^ b2)
        balls.append(b1)
    N = len(words)
    adj = [0] * N
    for i in range(N):
        for j in range(i+1, N):
            if balls[i].isdisjoint(balls[j]):
                adj[i] |= 1 << j
                adj[j] |= 1 << i
    return words, balls, adj


def is_code(code, word_index, adj):
    inds = [word_index[w] for w in code]
    for p, i in enumerate(inds):
        for j in inds[:p]:
            if not ((adj[i] >> j) & 1):
                return False
    return True


def prove_max_clique(adj, lower_bound):
    N = len(adj)
    best = lower_bound
    nodes = 0

    def color_sort(P):
        order = []
        bounds = []
        uncolored = P
        color = 0
        while uncolored:
            color += 1
            available = uncolored
            while available:
                bit = available & -available
                v = bit.bit_length() - 1
                order.append(v)
                bounds.append(color)
                uncolored ^= bit
                available ^= bit
                available &= ~adj[v]
        return order, bounds

    def expand(size, P):
        nonlocal best, nodes
        nodes += 1
        if not P:
            if size > best:
                best = size
            return
        order, bounds = color_sort(P)
        for k in range(len(order)-1, -1, -1):
            if size + bounds[k] <= best:
                return
            v = order[k]
            bit = 1 << v
            expand(size + 1, P & adj[v])
            P &= ~bit

    expand(0, (1 << N) - 1)
    return best, nodes


def main():
    with open(ROOT / "artifacts" / "optimal_codes.json", encoding="utf-8") as f:
        witnesses = {int(k): v for k, v in json.load(f).items()}
    with open(ROOT / "artifacts" / "profile.csv", newline="", encoding="utf-8") as f:
        target = {int(r["n"]): int(r["optimum"]) for r in csv.DictReader(f)}

    assert sorted(target) == list(range(1, 8))
    assert sorted(witnesses) == list(range(1, 8))
    node_counts = {}
    for n in range(1, 8):
        words, balls, adj = compatible_graph(n)
        index = {w: i for i, w in enumerate(words)}
        code = witnesses[n]
        assert len(code) == target[n]
        assert len(set(code)) == len(code)
        assert all(len(w) == n and set(w) <= {"0", "1"} for w in code)
        assert is_code(code, index, adj), f"invalid witness at n={n}"

        exact, nodes = prove_max_clique(adj, len(code))
        assert exact == target[n], (n, exact, target[n])
        node_counts[n] = nodes
        print(f"n={n} vertices={len(words)} optimum={exact} nodes={nodes}")

    print("VERIFY_OK profile=" + ",".join(str(target[n]) for n in range(1, 8)))
    print("NODE_COUNTS " + ",".join(f"{n}:{node_counts[n]}" for n in range(1, 8)))

if __name__ == "__main__":
    main()
