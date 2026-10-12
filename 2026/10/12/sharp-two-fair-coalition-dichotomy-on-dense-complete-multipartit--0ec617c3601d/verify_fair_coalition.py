"""Exhaustive checks for dense multipartite 2-fair coalition theorem.
The universal theorem is proved separately, not inferred from finite tests.
"""


def words_of_partitions(n):
    """Restricted growth words enumerate ALL set partitions exactly once."""
    def visit(prefix, upper):
        if len(prefix) == n:
            yield tuple(prefix)
        else:
            for z in range(upper + 2):
                prefix.append(z)
                yield from visit(prefix, max(upper, z))
                prefix.pop()
    yield from visit([0], 0)


def check(sizes, exhaustive_partitions):
    n = sum(sizes)
    colour = [j for j, x in enumerate(sizes) for _ in range(x)]
    masks = []
    for v in range(n):
        masks.append(sum(1 << u for u in range(n) if colour[u] != colour[v]))
    full = (1 << n) - 1
    fair = bytearray(1 << n)
    proper_fair = 0
    for chosen in range(1, full + 1):
        valid = all((masks[v] & chosen).bit_count() == 2
                    for v in range(n) if not chosen & (1 << v))
        fair[chosen] = valid
        proper_fair += valid and chosen != full
    expected = sum(sizes)-3 if len(sizes) == 3 else 2
    assert proper_fair == (sizes[0]*sizes[1]*sizes[2] if len(sizes)==3 else 0), (sizes, proper_fair)
    partitions_checked = 0
    optimal = 0
    maximum = -1
    if exhaustive_partitions:
        for parts in words_of_partitions(n):
            partitions_checked += 1
            k = max(parts) + 1
            if k < maximum:
                continue
            blocks = [0] * k
            for v, j in enumerate(parts): blocks[j] |= 1 << v
            valid = True
            for i, u in enumerate(blocks):
                if fair[u] and u.bit_count()==2:continue
                if fair[u] or not any(fair[u | v] for j, v in enumerate(blocks) if i != j):
                    valid = False
                    break
            if valid:
                if k > maximum:maximum, optimal = k, 0
                if k == maximum:optimal += 1
        assert maximum == expected, (sizes, maximum, expected)
    print(f'PASS sizes={sizes} N={n} proper-2-fair sets={proper_fair} predicted-coalition={expected} partitions={partitions_checked} optimal-partitions={optimal if exhaustive_partitions else "not enumerated"}')


if __name__ == '__main__':
    for s in [(3,3,3),(3,3,4),(3,4,4),(3,3,3,3),(3,3,3,4),(4,4,4),(3,3,3,3,3)]:
        check(s, exhaustive_partitions=(sum(s) <= 11 and len(s)==3))
    print('PASS all selected profiles; unlimited-order conclusion is established only in the written proof')

# Independent enumeration of every 3-pair matching on twelve vertices.
# Such matchings are precisely the partitions with nine blocks.
def verify_canonical_optima():
    sizes = (4,4,4)
    n = 12
    colors = [i//4 for i in range(12)]
    full = (1 << n)-1
    adj = [sum(1<<u for u in range(n) if colors[u]!=colors[v]) for v in range(n)]
    def fair(U):
        return all((adj[v]&U).bit_count()==2 for v in range(n) if not (U>>v&1))
    checked, accepted = 0, 0
    def match(available, pairs):
        nonlocal checked, accepted
        if len(pairs) == 3:
            checked+=1
            blocks = [((1<<a)|(1<<b)) for a,b in pairs]
            taken=set(u for pair in pairs for u in pair)
            blocks += [1<<u for u in range(n) if u not in taken]
            good = all(any(fair(u|v) for j,v in enumerate(blocks) if i!=j)
                       for i,u in enumerate(blocks))
            if good:
                accepted += 1
                assert sorted(tuple(sorted((colors[a],colors[b]))) for a,b in pairs)==[(0,1),(0,2),(1,2)]
            return
        a = available[0]
        match(available[1:], pairs) if len(available)>2*(3-len(pairs)) else None
        for b in available[1:]:
            match([u for u in available if u!=a and u!=b], pairs+[(a,b)])
    match(list(range(n)), [])
    assert accepted==8*6*6*6, accepted
    print(f'PASS canonical maximum-partition enumeration for (4,4,4): {accepted} valid of {checked} three-pair partitions')

if __name__=='__main__':
    verify_canonical_optima()
