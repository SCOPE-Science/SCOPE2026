"""Exact binary variable-length cross-bifix-free code capacity/length census.

Runs with Python 3.9+ standard library; no external solvers are required.
"""
from itertools import product
from time import monotonic


def overlap_free(w):
    return all(w[:k] != w[-k:] for k in range(1, len(w)))


def compatible(u, v):
    for x, y in ((u, v), (v, u)):
        if any(x[:k] == y[-k:] for k in range(1, min(len(x), len(y)))):
            return False
    if len(u) < len(v) and u in v:
        return False
    if len(v) < len(u) and v in u:
        return False
    return True


def candidate_words(n):
    # By the one-symbol overlap test and binary complementation symmetry,
    # every nonempty feasible family has one fixed initial symbol and its
    # opposite fixed final symbol. It suffices to take initial 0, final 1.
    return ["".join(x) for length in range(2, n + 1)
            for x in product("01", repeat=length)
            if x[0] == "0" and x[-1] == "1" and overlap_free(x)]


def exact_solve(n):
    words = candidate_words(n)
    N = len(words)
    neighbors = [sum(1 << j for j in range(N)
                     if j != i and compatible(words[i], words[j]))
                 for i in range(N)]
    lengths = [len(w) for w in words]
    all_candidates = (1 << N) - 1
    counts = [0, 0]

    def coloring(candidates):
        """Sequential proper coloring of the induced COMPATIBILITY graph.

        Every color class is an independent set: a feasible clique contains
        at most one vertex from each class. Returned colors are nondecreasing.
        """
        order, colors = [], []
        c = 0
        while candidates:
            c += 1
            available = candidates
            while available:
                bit = available & -available
                i = bit.bit_length() - 1
                order.append(i)
                colors.append(c)
                candidates ^= bit
                available &= ~(bit | neighbors[i])
        return order, colors

    max_size = 0
    size_witness = []

    def maximize(candidates, chosen):
        nonlocal max_size, size_witness
        counts[0] += 1
        if len(chosen) > max_size:
            max_size = len(chosen)
            size_witness = chosen[:]
        order, colors = coloring(candidates)
        for k in range(len(order) - 1, -1, -1):
            if len(chosen) + colors[k] <= max_size:
                return
            i = order[k]
            maximize(candidates & neighbors[i], chosen + [i])
            candidates &= ~(1 << i)

    maximize(all_candidates, [])
    best_length = sum(lengths[i] for i in size_witness)
    best_witness = size_witness[:]

    def minimize(candidates, chosen, total_length):
        nonlocal best_length, best_witness
        counts[1] += 1
        need = max_size - len(chosen)
        if need == 0:
            if total_length < best_length:
                best_length = total_length
                best_witness = chosen[:]
            return
        if candidates.bit_count() < need:
            return
        # Any extension must take at least 'need' available words,
        # irrespective of conflicts; their cheapest length sum is a lower bound.
        possible_lengths = sorted(lengths[i] for i in range(N)
                                  if candidates & (1 << i))
        if total_length + sum(possible_lengths[:need]) >= best_length:
            return
        order, colors = coloring(candidates)
        for k in range(len(order) - 1, -1, -1):
            if len(chosen) + colors[k] < max_size:
                return
            i = order[k]
            minimize(candidates & neighbors[i], chosen + [i],
                     total_length + lengths[i])
            candidates &= ~(1 << i)

    minimize(all_candidates, [], 0)
    code = tuple(sorted(words[i] for i in best_witness))
    assert len(code) == max_size
    assert sum(map(len, code)) == best_length
    assert all(overlap_free(w) and w[0] == "0" and w[-1] == "1"
               for w in code)
    assert all(compatible(u, v) for j, u in enumerate(code)
               for v in code[j+1:])
    return max_size, best_length, code, N, tuple(counts)


def main():
    begin = monotonic()
    expected = {
        2: (1, 2), 3: (1, 2), 4: (1, 2),
        5: (2, 9), 6: (3, 16), 7: (5, 32),
        8: (8, 59), 9: (14, 119), 10: (24, 227),
    }
    for n in range(2, 11):
        size, total_length, witness, N, nodes = exact_solve(n)
        assert (size, total_length) == expected[n], (n, size, total_length)
        print(f"n={n} candidates={N} max_size={size} "
              f"minimum_total_length={total_length} "
              f"search_nodes={nodes} witness={','.join(witness)}")
    print("VERIFY_OK binary lengths 2..10, exact maximum sizes and minimum "
          f"total codeword lengths ({monotonic()-begin:.2f}s)")


if __name__ == "__main__":
    main()
