from itertools import product
from math import comb


def graph_edges(kind, n):
    edges = [(i, i + 1) for i in range(n - 1)]
    if kind == "C":
        edges.append((n - 1, 0))
    return edges


def forces_three(kind, n, state):
    # state entries are -1 for uncoloured and 0,1,2 for colours.
    edges = graph_edges(kind, n)
    nbrs = [[] for _ in range(n)]
    for u, v in edges:
        nbrs[u].append(v)
        nbrs[v].append(u)

    col = list(state)
    while True:
        changed = False
        for v in range(n):
            if col[v] != -1:
                continue
            seen = {col[w] for w in nbrs[v] if col[w] != -1}
            if len(seen) == 2:
                missing = ({0, 1, 2} - seen).pop()
                col[v] = missing
                changed = True
        if not changed:
            break

    if any(c == -1 for c in col):
        return False
    return all(col[u] != col[v] for u, v in edges)


def brute_coefficients(kind, n):
    counts = [0] * (n + 1)
    for state in product((-1, 0, 1, 2), repeat=n):
        k = sum(c != -1 for c in state)
        if forces_three(kind, n, state):
            counts[k] += 1
    return counts


def predicted_path(n):
    out = [0] * (n + 1)
    for j in range((n - 1) // 2 + 1):
        k = n - j
        out[k] = 3 * (2 ** (n - 1 - j)) * comb(n - 1 - j, j)
    return out


def cycle_independent_sets(n, j):
    if j == 0:
        return 1
    return n * comb(n - j, j) // (n - j)


def predicted_cycle(n):
    out = [0] * (n + 1)
    for j in range(n // 2 + 1):
        k = n - j
        out[k] = cycle_independent_sets(n, j) * (
            2 ** (n - j) + 2 * ((-1) ** (n - j))
        )
    return out


def main():
    for n in range(2, 9):
        got = brute_coefficients("P", n)
        want = predicted_path(n)
        assert got == want, ("P", n, got, want)
        print(f"P{n}: {got}")

    for n in range(3, 9):
        got = brute_coefficients("C", n)
        want = predicted_cycle(n)
        assert got == want, ("C", n, got, want)
        print(f"C{n}: {got}")

    print("All path and cycle coefficient checks passed.")


if __name__ == "__main__":
    main()
