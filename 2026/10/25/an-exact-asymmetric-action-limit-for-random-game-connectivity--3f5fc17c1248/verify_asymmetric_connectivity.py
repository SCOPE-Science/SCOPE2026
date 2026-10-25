#!/usr/bin/env python3
"""Exhaustive finite check of the 2-by-k response-map theorem for 3 <= k <= 7.
This corroborates the proof; it does not prove the infinite family."""
from itertools import product


def connected(k, R, C):
    vertices = [(i, j) for i in (0, 1) for j in range(k)]
    edges = {v: [] for v in vertices}
    for i, j in vertices:
        if R[j] != i:
            edges[(i, j)].append((R[j], j))
        if C[i] != j:
            edges[(i, j)].append((i, C[i]))
    sinks = [v for v in vertices if not edges[v]]
    if not sinks:
        return False
    for v in vertices:
        if v in sinks:
            continue
        seen, todo = {v}, [v]
        while todo:
            x = todo.pop()
            for y in edges[x]:
                if y not in seen:
                    seen.add(y)
                    todo.append(y)
        if any(s not in seen for s in sinks):
            return False
    return True


def main():
    for k in range(3, 8):
        total = 0
        conn = 0
        ne = 0
        for R in product((0, 1), repeat=k):
            for C in product(range(k), repeat=2):
                total += 1
                F = (R[C[0]], R[C[1]])
                has_ne = (F[0] == 0 or F[1] == 1)
                is_connected = connected(k, R, C)
                assert is_connected == (F[0] == F[1])
                conn += int(is_connected)
                ne += int(has_ne)
        expected_conn = (2 ** (k - 1)) * k * (k + 1)
        expected_ne = (2 ** (k - 2)) * k * (3 * k + 1)
        assert conn == expected_conn, (k, conn, expected_conn)
        assert ne == expected_ne, (k, ne, expected_ne)
        assert conn / ne == 2 * (k + 1) / (3 * k + 1)
        print(f"k={k}: total={total}, connected={conn}, with_NE={ne}, conditional={conn/ne:.12f}")
    print("PASS: all enumerated cases agree with the analytic formulas.")


if __name__ == '__main__':
    main()
