#!/usr/bin/env python3
from functools import lru_cache


def cyclic_tournament(c):
    assert c >= 5 and c % 2 == 1
    m = (c - 1) // 2
    return [[i != j and ((j - i) % c) in range(1, m + 1) for j in range(c)] for i in range(c)]


def paley_tournament(q):
    assert q % 4 == 3
    residues = {pow(x, 2, q) for x in range(1, q)}
    return [[i != j and ((j - i) % q) in residues for j in range(q)] for i in range(q)]


def check_tournament_regular(A):
    n = len(A)
    target = (n - 1) // 2
    assert n % 2 == 1
    for i in range(n):
        assert not A[i][i]
        for j in range(i + 1, n):
            assert A[i][j] ^ A[j][i]
        assert sum(A[i]) == target


def find_cycle(A, u, v, length):
    n = len(A)
    assert A[u][v]
    path = [u, v]
    used = {u, v}

    def dfs():
        if len(path) == length:
            return tuple(path) if A[path[-1]][u] else None
        last = path[-1]
        for w in range(n):
            if w in used or not A[last][w]:
                continue
            used.add(w)
            path.append(w)
            out = dfs()
            if out is not None:
                return out
            path.pop()
            used.remove(w)
        return None

    return dfs()


def decompose_length(total, c, alpha):
    for k in range(1, alpha + 1):
        if 3 * k <= total <= c * k:
            vals = [3] * k
            remainder = total - 3 * k
            for i in range(k):
                add = min(c - 3, remainder)
                vals[i] += add
                remainder -= add
            assert remainder == 0
            return vals
    raise AssertionError((total, c, alpha))


def lifted_arc(A, x, y):
    return x[0] != y[0] and A[x[0]][y[0]]


def splice(A, u, v, base_cycles, lengths, alpha):
    assert len(base_cycles) == len(lengths) <= alpha
    cycle = []
    for layer, C in enumerate(base_cycles):
        assert len(C) == lengths[layer]
        assert C[0] == u and C[1] == v
        cycle.extend((part, layer) for part in C)
    return cycle


def verify_one_base(name, A, alpha_max=4):
    check_tournament_regular(A)
    c = len(A)
    base_cycles = {}
    arc_count = 0
    target_cases = 0
    for u in range(c):
        for v in range(c):
            if not A[u][v]:
                continue
            arc_count += 1
            for t in range(3, c + 1):
                C = find_cycle(A, u, v, t)
                assert C is not None, (name, u, v, t)
                base_cycles[(u, v, t)] = C
            for alpha in range(1, alpha_max + 1):
                # Degree check for the blow-up.
                assert alpha * sum(A[u]) == alpha * (c - 1) // 2
                for total in range(3, c * alpha + 1):
                    lengths = decompose_length(total, c, alpha)
                    Cs = [base_cycles[(u, v, t)] for t in lengths]
                    cyc = splice(A, u, v, Cs, lengths, alpha)
                    assert len(cyc) == total
                    assert len(set(cyc)) == total
                    assert cyc[0] == (u, 0) and cyc[1] == (v, 0)
                    for i in range(total):
                        assert lifted_arc(A, cyc[i], cyc[(i + 1) % total]), (name, u, v, alpha, total, i)
                    target_cases += 1
    return arc_count, target_cases


def main():
    bases = []
    for c in (5, 7, 9, 11, 13):
        bases.append((f"cyclic_{c}", cyclic_tournament(c)))
    for q in (7, 11):
        bases.append((f"paley_{q}", paley_tournament(q)))

    total_arcs = 0
    total_cases = 0
    for name, A in bases:
        arcs, cases = verify_one_base(name, A)
        total_arcs += arcs
        total_cases += cases
    print(f"ALL CHECKS PASSED; base_tournaments={len(bases)}; base_arcs={total_arcs}; lifted_cycle_cases={total_cases}; alpha_max=4; max_base_order=13")


if __name__ == "__main__":
    main()
