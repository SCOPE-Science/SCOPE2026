"""Reproduce the maximal clique classification of binary cross-join graphs.

Python 3 standard library only. Run: python3 verify_cliques.py
"""
from collections import Counter
from itertools import combinations


def transition(state, mask, n):
    half = 1 << (n - 1)
    first, tail = state // half, state % half
    return ((2 * state) % (1 << n)) | (first ^ ((mask >> tail) & 1))


def feedback_cycles(n):
    """Enumerate all 2^(2^(n-1)) truth tables and retain full cycles."""
    size, half = 1 << n, 1 << (n - 1)
    cycles = {}
    for mask in range(1 << half):
        orbit = [0]
        state = 0
        for _ in range(size):
            state = transition(state, mask, n)
            if state == 0:
                break
            orbit.append(state)
        if state != 0 or len(orbit) != size:
            continue
        assert len(set(orbit)) == size
        # Cyclic (n+1)-factor bitset, independently usable for adjacency.
        factors = 0
        for pos, state in enumerate(orbit):
            value = (state << 1) | (orbit[(pos + 1) % size] & 1)
            factors |= 1 << value
        assert factors.bit_count() == size
        cycles[mask] = factors
    return cycles


def euler_cycle_masks(n):
    """Independent enumeration of outgoing-edge orders and Euler tours."""
    size, half = 1 << n, 1 << (n - 1)
    answer = set()
    for orders in range(1 << half):
        used = [0] * half
        stack = [(0, -1)]
        backtrack = []
        while stack:
            v, incoming = stack[-1]
            if used[v] == 2:
                stack.pop()
                if incoming >= 0:
                    backtrack.append(incoming)
                continue
            edge = 2 * v + (used[v] ^ ((orders >> v) & 1))
            used[v] += 1
            stack.append((edge % half, edge))
        edges = backtrack[::-1]
        assert len(edges) == size and len(set(edges)) == size
        assert all(edges[(i+1) % size] >> 1 == edges[i] % half
                   for i in range(size))
        feedback = [None] * half
        for i, edge in enumerate(edges):
            u = edge % half
            bit = (edge >> (n-1)) ^ (edges[(i+1) % size] & 1)
            if feedback[u] is not None:
                assert feedback[u] == bit
            feedback[u] = bit
        answer.add(sum(bit << i for i, bit in enumerate(feedback)))
    return answer


def structural_maximum_cliques(masks, n):
    """All cliques saturating the combinatorial upper bound (n>=4)."""
    half = 1 << (n-1)
    coordinates = range(1, half-1)
    q = half - 2
    masks = set(masks)
    extremal = set()
    universal_pairs = 0
    witness = None
    for m in sorted(masks):
        for i in coordinates:
            clique = (m,) + tuple(m ^ (1 << i) ^ (1 << j)
                                   for j in coordinates if j != i)
            if all(u in masks for u in clique):
                assert len(set(clique)) == q
                universal_pairs += 1
                extremal.add(tuple(sorted(clique)))
                if witness is None:
                    witness = (m, i, tuple(sorted(clique)))
    if q >= 6:
        assert universal_pairs == q * len(extremal)
    return extremal, universal_pairs, witness


def generic_graph_cliques(bitsets, n):
    """Independent Bron--Kerbosch enumeration using direct factor intersection."""
    masks = list(bitsets)
    graph = {m: set() for m in masks}
    size = 1 << n
    for i, a in enumerate(masks):
        for b in masks[i+1:]:
            if (bitsets[a] & bitsets[b]).bit_count() == size - 4:
                graph[a].add(b)
                graph[b].add(a)
    hist = Counter()
    maxima = set()

    def visit(current, potential, excluded):
        if not potential and not excluded:
            hist[len(current)] += 1
            if len(current) == (1 << (n-1)) - 2:
                maxima.add(tuple(sorted(current)))
            return
        all_candidates = potential | excluded
        pivot = max(all_candidates, key=lambda u: len(potential & graph[u])) if all_candidates else None
        branching = sorted(potential - graph[pivot]) if pivot is not None else sorted(potential)
        for v in branching:
            visit(current + (v,), potential & graph[v], excluded & graph[v])
            potential.remove(v)
            excluded.add(v)

    visit((), set(masks), set())
    return graph, hist, maxima


def main():
    expected = {3: (2, 1, 4), 4: (16, 4, 24), 5: (2048, 16, 224)}
    for n in (3, 4, 5):
        bitsets = feedback_cycles(n)
        independent = euler_cycle_masks(n)
        assert set(bitsets) == independent
        expected_size, expected_cliques, expected_roots = expected[n]
        assert len(bitsets) == expected_size
        large, roots, witness = structural_maximum_cliques(bitsets, n)
        if n >= 4:
            assert len(large) == expected_cliques and roots == expected_roots
            graph, maximal, generic = generic_graph_cliques(bitsets, n)
            assert large == generic, (n, len(large), len(generic))
            assert max(maximal) == (1 << (n-1)) - 2
            print(f'order={n} cycles={len(bitsets)} edges={sum(map(len,graph.values()))//2} '
                  f'maximum_clique_size={max(maximal)} number_of_maximum_cliques={len(large)} '
                  f'rooted_certificates={roots}')
            if n == 5:
                assert sum(maximal.values()) > 20000
                assert maximal[14] == 16
                print('order_5_maximal_clique_spectrum', dict(sorted(maximal.items())))
                print('order_5_witness_mask', hex(witness[0]),
                      'common_table_coordinate', witness[1])
                print('order_5_witness_clique', ','.join(hex(m) for m in witness[2]))
                # Check every witness edge directly using its 6-mer sets.
                for a,b in combinations(witness[2], 2):
                    assert (bitsets[a] & bitsets[b]).bit_count() == 28
        else:
            assert len(large) == 1 and roots == 4
            print(f'order={n} cycles={len(bitsets)} (single cross-join edge)')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
