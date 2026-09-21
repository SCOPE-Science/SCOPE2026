from itertools import combinations


def paley_graph(p):
    residues = {pow(x, 2, p) for x in range(1, p)}
    nbr = []
    for a in range(p):
        mask = 0
        for b in range(p):
            if a != b and (a - b) % p in residues:
                mask |= 1 << b
        nbr.append(mask)
    return nbr


def metric_line(nbr, a, b):
    adjacent = (nbr[a] >> b) & 1
    if adjacent:
        # In a diameter-two graph, a third vertex is on the line exactly when
        # it is adjacent to exactly one endpoint.
        return (nbr[a] ^ nbr[b]) | (1 << a) | (1 << b)
    # For a nonedge, a third vertex is on the line exactly when it is a
    # common neighbor of the endpoints.
    return (nbr[a] & nbr[b]) | (1 << a) | (1 << b)


def verify(p=17):
    nbr = paley_graph(p)
    pairs = list(combinations(range(p), 2))
    lines = [metric_line(nbr, a, b) for a, b in pairs]
    closed = [nbr[a] | (1 << a) for a in range(p)]

    # Diameter exactly two: every nonedge has a common neighbor, and the
    # graph is not complete.
    assert any(not ((nbr[a] >> b) & 1) for a, b in pairs)
    for a, b in pairs:
        if not ((nbr[a] >> b) & 1):
            assert nbr[a] & nbr[b]

    # Distinct generated lines form an antichain.
    for i, Li in enumerate(lines):
        for j, Lj in enumerate(lines):
            if i != j:
                assert Li & ~Lj

    # Closed neighborhoods form an antichain.
    for a, Na in enumerate(closed):
        for b, Nb in enumerate(closed):
            if a != b:
                assert Na & ~Nb

    # Every line and every closed neighborhood are incomparable.
    for Na in closed:
        for L in lines:
            assert Na & ~L
            assert L & ~Na

    edge_count = sum(mask.bit_count() for mask in nbr) // 2
    line_sizes = {}
    for L in lines:
        line_sizes[L.bit_count()] = line_sizes.get(L.bit_count(), 0) + 1

    print(f"P({p}) verified super geometric dominant")
    print(f"vertices={p}")
    print(f"edges={edge_count}")
    print(f"generated_lines={len(lines)}")
    print(f"distinct_lines={len(set(lines))}")
    # The sufficient 4-e.c. condition is not necessary: P(17) has no vertex
    # outside {0,1,2,3} nonadjacent to all four.
    witness_set = {0, 1, 2, 3}
    common_nonneighbors = [
        x for x in range(p)
        if x not in witness_set
        and all(not ((nbr[x] >> w) & 1) for w in witness_set)
    ]
    assert common_nonneighbors == []

    print("line_size_distribution=" + repr(dict(sorted(line_sizes.items()))))
    print("all four defining conditions passed")
    print("not_4_ec_certificate=W={0,1,2,3} has no outside common nonneighbor")


if __name__ == "__main__":
    verify()
