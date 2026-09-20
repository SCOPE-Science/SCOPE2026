from itertools import combinations, product


def hamming(x, y):
    return sum(a != b for a, b in zip(x, y))


def build_code(q):
    if q <= 4:
        return [(a, a, a) for a in range(q)]
    if q % 2:
        r = (q - 1) // 2
        sizes = (r, r, r)
    else:
        r = q // 2
        sizes = (r, r - 1, r - 1)
    group = []
    for g, s in enumerate(sizes):
        group.extend([g] * s)
    n = len(group)
    words = [[None] * 3 for _ in range(n)]
    for coord in range(3):
        next_symbol = 1
        for idx, g in enumerate(group):
            if g == coord:
                words[idx][coord] = 0
            else:
                words[idx][coord] = next_symbol
                next_symbol += 1
        assert next_symbol - 1 <= q - 1
    return [tuple(w) for w in words]


def descendants(parents):
    choices = [sorted({p[i] for p in parents}) for i in range(3)]
    return set(product(*choices))


def is_two_traceability(code):
    n = len(code)
    for s in (1, 2):
        for ids in combinations(range(n), s):
            parents = [code[i] for i in ids]
            parent_ids = set(ids)
            for w in descendants(parents):
                dist = [hamming(w, x) for x in code]
                best = min(dist)
                nearest = {i for i, d in enumerate(dist) if d == best}
                if not nearest <= parent_ids:
                    return False, (ids, w, nearest)
    return True, None


def target(q):
    return max(q, (3 * q - 3) // 2)


for q in range(2, 31):
    code = build_code(q)
    ok, witness = is_two_traceability(code)
    assert len(code) == target(q), (q, len(code), target(q))
    assert ok, (q, witness)
    used = [len({x[i] for x in code}) for i in range(3)]
    assert max(used) <= q
    print(f"q={q:2d} size={len(code):2d} target={target(q):2d} symbols={used} verified=yes")
