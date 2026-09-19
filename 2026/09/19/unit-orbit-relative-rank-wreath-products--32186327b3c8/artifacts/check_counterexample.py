from itertools import combinations, product

def compose(f, g):
    return tuple(g[f[i]] for i in range(len(f)))

def close_maps(generators, degree):
    c = {tuple(range(degree)), *generators}
    changed = True
    while changed:
        old = list(c)
        for x in old:
            for y in old:
                c.add(compose(x, y))
        changed = len(c) > len(old)
    return frozenset(c)

g = (1, 0, 2)
a = (2, 2, 0)
R = close_maps([g, a], 3)
G = frozenset(r for r in R if len(set(r)) == 3)
elements = [(base, r) for base in product((0, 1), repeat=3) for r in R]
units = frozenset(((1, 1, 1), r) for r in G)

def multiply(x, y):
    bx, r = x
    by, t = y
    return tuple(bx[i] & by[r[i]] for i in range(3)), compose(r, t)

def generated(extra):
    c = set(units)
    c.update(extra)
    changed = True
    while changed:
        old = list(c)
        for x in old:
            for y in old:
                c.add(multiply(x, y))
        changed = len(c) > len(old)
    return c

nonunits = [x for x in elements if x not in units]
relative_rank = None
witness = None
for size in range(4):
    for extra in combinations(nonunits, size):
        if len(generated(extra)) == len(elements):
            relative_rank = size
            witness = extra
            break
    if relative_rank is not None:
        break

formula = 1 + 2 * 1
claimed_bound = 1 + 1
print(f"|R|={len(R)}")
print(f"|G|={len(G)}")
print(f"|S wr R|={len(elements)}")
print(f"|H wr G|={len(units)}")
print(f"relative_rank={relative_rank}")
print(f"orbit_formula={formula}")
print(f"bound_from_transitivity_only={claimed_bound}")
print(f"witness_size={len(witness)}")
assert relative_rank == formula == 3
assert claimed_bound == 2
