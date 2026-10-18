"""Finite checks for prime-power length predicates and bipartite-cactus automata.

Run with Python 3. No third-party dependencies. These finite checks complement,
but do not replace, the general combinatorial proof.
"""
from itertools import product
from math import gcd, lcm


def primitive_residue_sets(m):
    """Residue masks whose smallest positive shift period is m."""
    for mask in range(1 << m):
        if all(any(bool(mask & (1 << i)) != bool(mask & (1 << ((i + t) % m)))
                   for i in range(m)) for t in range(1, m)):
            yield mask


def graph_is_bipartite(q, rows):
    # Ignore loop edges, exactly as for a simple underlying state graph.
    undirected = [0] * q
    for i, row in enumerate(rows):
        for j in range(q):
            if j != i and (row >> j) & 1:
                undirected[i] |= 1 << j
                undirected[j] |= 1 << i
    coloring = [-1] * q
    for start in range(q):
        if coloring[start] >= 0:
            continue
        coloring[start] = 0
        stack = [start]
        while stack:
            u = stack.pop()
            for v in range(q):
                if (undirected[u] >> v) & 1:
                    if coloring[v] < 0:
                        coloring[v] = 1 - coloring[u]
                        stack.append(v)
                    elif coloring[v] == coloring[u]:
                        return False
    return True


def check_witnesses():
    cases = 0
    residue_sets = 0
    for m in (2, 3, 4, 5, 7, 8, 9, 11, 16, 25, 27):
        ring = lcm(m, 2)
        # Enumerate all primitive sets for m <= 9, and reproducible varied sets above.
        if m <= 9:
            masks = list(primitive_residue_sets(m))
        else:
            masks = sorted(set([1, 1 << (m-1),
                sum(1 << i for i in range(m) if i*i % 7 in (0, 1, 2)),
                sum(1 << i for i in range(m) if i % 3 == 0)]))
            masks = [mask for mask in masks if all(
                any(bool(mask & (1 << i)) != bool(mask & (1 << ((i+t) % m)))
                    for i in range(m)) for t in range(1, m))]
        # A directed cycle of even length has a bipartite cactus underlying graph.
        assert ring % 2 == 0
        assert ring == m or ring == 2*m
        for mask in masks:
            finals = sum(1 << j for j in range(ring) if mask & (1 << (j % m)))
            for length in range(4*ring + 1):
                # Every input symbol advances the same cycle position.
                accepted = bool(finals & (1 << (length % ring)))
                expected = bool(mask & (1 << (length % m)))
                assert accepted == expected, (m, mask, length)
                cases += 1
            residue_sets += 1
        if m <= 9:
            # p^k prime-power periods: number of primitive predicates.
            p = next(a for a in range(2, m+1) if m % a == 0)
            # Only values in our test suite that are prime powers.
            pk = m // p
            assert len(masks) == 2**m - 2**pk, (m, len(masks))
    return residue_sets, cases


def check_small_nfas():
    """Exhaust all <=4-state unary NFAs with bipartite underlying graphs.

    Search every transition relation and every accepting set; a language
    disagreement is tested through the product of the subset DFA with the
    modulus-3 cycle, which has at most 3*2^q states.
    """
    tested = 0
    for q in range(1, 5):
        desired = []
        T = 3 * (1 << q)
        for residue_mask in range(1, 7):
            if residue_mask == 0b000 or residue_mask == 0b111:
                continue
            desired.append(tuple(bool(residue_mask & (1 << (n % 3)))
                                 for n in range(T)))
        for rowtuple in product(range(1 << q), repeat=q):
            if not graph_is_bipartite(q, rowtuple):
                continue
            reach = [1]
            for n in range(1, T):
                s = 0
                for i in range(q):
                    if reach[-1] >> i & 1:
                        s |= rowtuple[i]
                reach.append(s)
            for finals in range(1 << q):
                pattern = tuple(bool(s & finals) for s in reach)
                assert pattern not in desired, (q, rowtuple, finals)
                tested += 1
    return tested


def main():
    num_masks, num_lengths = check_witnesses()
    nfa_tests = check_small_nfas()
    print(f"PRIMITIVE_PREDICATES_CHECKED={num_masks}")
    print(f"CONSTRUCTION_LENGTH_CHECKS={num_lengths}")
    print(f"BIPARTITE_UNARY_NFA_EXHAUSTIVE_TESTS={nfa_tests}")
    print("CHECKS_PASSED")


if __name__ == "__main__":
    main()
