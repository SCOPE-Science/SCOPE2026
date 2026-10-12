"""Reproducible finite-rank checks for an action-quandle automorphism theorem."""
import itertools
import collections
import math


def mul(p, q):
    """Product consistent with a right action: apply p then q."""
    return tuple(q[p[i]] for i in range(len(p)))


def inv(p):
    return tuple(p.index(i) for i in range(len(p)))


def conj(g, h):
    return mul(mul(inv(h), g), h)


def partition_data(n, floor=1):
    if n == 0:
        yield ()
    else:
        for first in range(floor, n + 1):
            for tail in partition_data(n-first, first):
                yield (first,) + tail


def partition_product(n):
    factors = []
    for lam in partition_data(n):
        c = collections.Counter(lam)
        factor = math.prod(d for d in c if d >= 2)
        if c[1] == 2:
            factor *= 2
        factors.append((lam, factor))
    return math.prod(x[1] for x in factors), factors


def compute(n):
    group = list(itertools.permutations(range(n)))
    one = tuple(range(n))
    members = set(group)
    reps = []
    while members:
        g = min(members)
        orbit = {conj(g, h) for h in group}
        assert orbit <= members
        members -= orbit
        reps.append(g)
    centers = []
    for g in reps:
        c = [h for h in group if mul(h, g) == mul(g, h)]
        z = [a for a in c if all(mul(a, h) == mul(h, a) for h in c)]
        centers.append(z)
    product = math.prod(map(len, centers))
    expected, _ = partition_product(n)
    assert product == expected
    # Exhaust all class-local centralizer choices, using independent group products.
    for choice in itertools.product(*centers):
        data = {}
        for g, a in zip(reps, choice):
            for h in group:
                target, moved = conj(g, h), conj(a, h)
                if target in data:
                    assert data[target] == moved
                else:
                    data[target] = moved
        assert len(data) == len(group)
        for g in group:
            for h in group:
                gh = mul(inv(g), h)
                gh_conj = conj(g, h)
                assert mul(gh, data[gh_conj]) == mul(data[g], gh)
        # A direct operation test at every x,g,h for selected orbit choices.
        if choice == tuple(z[0] for z in centers) or choice[-1] == centers[-1][-1]:
            for x in range(n):
                for g in group:
                    for h in group:
                        target_g = conj(g, h)
                        left = mul(mul(inv(g), h), data[target_g])[x]
                        right = mul(mul(data[g], inv(g)), h)[x]
                        assert left == right
        # All images are fiberwise permutations by construction.
        assert all(tuple(sorted(a)) == one for a in data.values())
    return product


def main():
    assert compute(3) == 6
    assert compute(4) == 96
    expected_outer = {3: 1, 4: 8, 5: 48}
    for n in range(3, 7):
        kernel, factors = partition_product(n)
        exponent = math.lcm(*range(1, n + 1))
        assert kernel % exponent == 0
        if n in expected_outer:
            assert kernel // exponent == expected_outer[n]
        print(f"n={n} partitions={len(factors)} |K|={kernel} |Aut|={math.factorial(n)*kernel} outer_index={kernel//exponent}")
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
