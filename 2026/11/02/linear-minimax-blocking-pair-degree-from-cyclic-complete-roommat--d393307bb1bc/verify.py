"""Finite exact checks for cyclic-preference stable-roommates profiles."""
from functools import lru_cache


def preferences(n):
    if n < 2:
        raise ValueError("n must be at least two")
    core = n if n % 2 else n - 1
    output = [tuple((i + t) % core for t in range(1, core)) for i in range(core)]
    if n % 2 == 0:
        dummy = n - 1
        output = [line + (dummy,) for line in output]
        output.append(tuple(range(core)))
    return tuple(output)


def block_degrees(preferences, matching):
    n = len(preferences)
    rank = [{candidate: pos for pos, candidate in enumerate(row)} for row in preferences]
    partner = list(range(n))
    for i, j in matching:
        assert i != j and partner[i] == i and partner[j] == j
        partner[i] = j
        partner[j] = i
    deg = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            if partner[i] == j:
                continue
            wants_i = partner[i] == i or rank[i][j] < rank[i][partner[i]]
            wants_j = partner[j] == j or rank[j][i] < rank[j][partner[j]]
            if wants_i and wants_j:
                deg[i] += 1
                deg[j] += 1
    return tuple(deg)


@lru_cache(None)
def matchings(vertices):
    if not vertices:
        return ((),)
    a, *rest = vertices
    outputs = list(matchings(tuple(rest)))
    for b in rest:
        remaining = tuple(v for v in rest if v != b)
        outputs.extend(((a, b),) + other for other in matchings(remaining))
    return tuple(outputs)


def proposed_matching(n):
    k = (n - 1) // 2 if n % 2 else (n - 2) // 2
    pairs = [(i, i + k) for i in range(k)]
    if n % 2 == 0:
        pairs.append((2*k, n - 1))
    return tuple(pairs)


def main():
    for n in range(2, 11):
        p = preferences(n)
        k = (n - 1) // 2
        explicit = proposed_matching(n)
        deg = block_degrees(p, explicit)
        assert max(deg) == k, (n, 'explicit', deg)
        allmatch = matchings(tuple(range(n)))
        smallest = min(max(block_degrees(p, m)) for m in allmatch)
        assert smallest == k, (n, smallest, k)
        # Circular triple lemma independently checked for all distinct triples.
        core = n if n % 2 else n - 1
        r = [{x: t for t, x in enumerate(line)} for line in p]
        for a in range(core):
            for b in range(core):
                for u in range(core):
                    if len({a,b,u}) == 3:
                        assert (r[a][u] < r[a][b]) != (r[b][u] < r[b][a])
        print(f'n={n}: all_matchings={len(allmatch)} optimal_max_block_degree={smallest}')
    print('All exact checks passed.')


if __name__ == '__main__':
    main()
