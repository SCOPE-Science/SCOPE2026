"""Independent small-instance and construction checks for weight-two single-deletion codes.

Run: python verify.py
Python standard library only. This program verifies finite test cases; the all-n
assertion comes from the accompanying mathematical proof, not from this program.
"""
from itertools import combinations


def ball(n, ij):
    w = [0] * n
    for i in ij:
        w[i] = 1
    return {tuple(w[:t] + w[t + 1:]) for t in range(n)}


def construction(n):
    N = n - 1
    pairs = [(j, j + 1) for j in range(0, N, 2)]
    odds = list(range(1, N, 2))
    pairs += [(odds[t], odds[t + 1] + 1) for t in range(0, len(odds) - 1, 2)]
    return pairs


def brute_alpha(n):
    words = list(combinations(range(n), 2))
    balls = [ball(n, w) for w in words]
    adj = [0] * len(words)
    for i in range(len(words)):
        for j in range(i):
            if balls[i] & balls[j]:
                adj[i] |= 1 << j
                adj[j] |= 1 << i
    # A full maximum clique search in the complement of the confusability graph.
    M = (1 << len(words)) - 1
    comp = [M & ~(adj[i] | (1 << i)) for i in range(len(words))]
    best = 0
    nodes = 0

    def color_order(candidates):
        order, colors = [], []
        remaining = candidates
        color = 0
        while remaining:
            color += 1
            independent = remaining
            while independent:
                vbit = independent & -independent
                v = vbit.bit_length() - 1
                order.append(v)
                colors.append(color)
                remaining ^= vbit
                independent ^= vbit
                independent &= ~comp[v]
        return order, colors

    def expand(candidates, depth):
        nonlocal best, nodes
        nodes += 1
        if not candidates:
            best = max(best, depth)
            return
        order, colors = color_order(candidates)
        for k in range(len(order) - 1, -1, -1):
            if depth + colors[k] <= best:
                break
            v = order[k]
            expand(candidates & comp[v], depth + 1)
            candidates &= ~(1 << v)

    expand(M, 0)
    return best, nodes


def main():
    constructions = 0
    output_comparisons = 0
    for n in range(2, 201):
        C = construction(n)
        assert len(C) == (3 * n - 2) // 4, (n, C)
        assert len(set(C)) == len(C)
        seen = set()
        for i, j in C:
            assert 0 <= i < j < n
            for output in ball(n, (i, j)):
                assert output not in seen, (n, (i, j), output)
                seen.add(output)
                output_comparisons += 1
        constructions += 1
    brute_nodes = 0
    for n in range(2, 11):
        maximum, nodes = brute_alpha(n)
        assert maximum == (3 * n - 2) // 4, (n, maximum)
        brute_nodes += nodes
    print(f'VERIFY_OK constructed_n=2..200 distinct_outputs={output_comparisons} '
          f'exact_MIS_n=2..10 branch_nodes={brute_nodes}')

if __name__ == '__main__':
    main()
