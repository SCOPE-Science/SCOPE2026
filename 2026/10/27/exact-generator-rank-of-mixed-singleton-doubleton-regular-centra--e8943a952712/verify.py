"""Bounded checks of semigroup (nonempty-word) generation."""
from itertools import combinations, product


def then(f, g):
    return tuple(g[i] for i in f)


def closure(gens):
    seen = set(gens)
    pending = list(seen)
    while pending:
        f = pending.pop()
        for g in gens:
            h = then(f, g)
            if h not in seen:
                seen.add(h)
                pending.append(h)
    return seen


def check(b):
    # Points: 0, followed by pairs (2i-1, 2i), i = 1, ..., b.
    I = tuple(range(2*b+1))
    e = (0,) + tuple(2*i-1 for i in range(1, b+1) for _ in range(2))
    t = (1, 0, 0) + I[3:]
    z = (1,) + I[1:]
    if b == 1:
        gens = (I, t, z)
    else:
        s = (0, 3, 4, 1, 2) + I[5:]
        c = I[:3] + (1, 2) + I[5:]
        gens = (s, t, z, c)
        if b >= 3:
            cycle = (0,) + I[3:] + (1, 2)
            gens += (cycle,)
    assert all(then(f,e) == then(e,f) for f in gens)
    got = closure(gens)
    assert len(got) == (b+1)*(2*b+1)**b
    if b <= 2:
        expected = {f for f in product(I, repeat=len(I)) if then(f,e) == then(e,f)}
        assert got == expected
        if b == 1:
            assert closure((t,z)) == expected-{I}
            assert all(closure(pair) != expected for pair in combinations(expected,2))
        else:
            nonunits = expected-{I,s}
            assert all(closure((s,x,y)) != expected for x,y in combinations(nonunits,2))
    print(f'b={b}: {len(gens)} generators, closure size {len(got)}')


if __name__ == '__main__':
    for b in range(1,5):
        check(b)
