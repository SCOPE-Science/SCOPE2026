"""Independent finite check for quaternary GC-balanced length-four non-overlapping codes.

Usage: python3 verify.py
Standard-library Python 3. No external files or packages.
"""
from itertools import product, combinations, permutations

SIGMA = "ACGT"
LOW = "AT"
HIGH = "CG"


def balanced(w):
    return len(w) == 4 and sum(x in HIGH for x in w) == 2


def compatible(a, b):
    return all(a[-k:] != b[:k] and b[-k:] != a[:k] for k in (1, 2, 3))


def constructions():
    codes = set()
    for left, right in ((LOW, HIGH), (HIGH, LOW)):
        forced = {a + b + c + d for a, b, c, d in product(left, left, right, right)}
        q = tuple(a + b for a, b in product(left, right))
        for p in combinations(q, 2):
            s = set(q).difference(p)
            codes.add(frozenset(forced | {x + y for x in p for y in s}))
    assert len(codes) == 12
    assert all(len(code) == 20 and all(balanced(w) for w in code) for code in codes)
    assert all(all(compatible(a, b) for a in code for b in code) for code in codes)
    return codes


def exhaustive_extremizers():
    words = [''.join(x) for x in product(SIGMA, repeat=4)
             if balanced(x) and all(x[-k:] != x[:k] for k in (1, 2, 3))]
    n = len(words)
    adj = [sum(1 << j for j, v in enumerate(words) if i != j and compatible(w, v))
           for i, w in enumerate(words)]
    best, bestcodes = 0, set()

    def color_order(mask):
        order, bounds, color = [], [], 0
        while mask:
            color += 1
            available = mask
            while available:
                bit = available & -available
                v = bit.bit_length() - 1
                order.append(v)
                bounds.append(color)
                mask ^= bit
                available ^= bit
                available &= ~adj[v]
        return order, bounds

    def search(mask, chosen):
        nonlocal best, bestcodes
        if not mask:
            length = len(chosen)
            if length >= best:
                if length > best:
                    best, bestcodes = length, set()
                bestcodes.add(frozenset(words[i] for i in chosen))
            return
        vertices, colors = color_order(mask)
        for k in range(len(vertices) - 1, -1, -1):
            if len(chosen) + colors[k] < best:
                return
            vertex = vertices[k]
            search(mask & adj[vertex], chosen + (vertex,))
            mask &= ~(1 << vertex)

    search((1 << n) - 1, ())
    return best, bestcodes, n


def symmetries(codes):
    letters = set(SIGMA)
    maps = []
    for images in permutations(SIGMA):
        d = dict(zip(SIGMA, images))
        if ({d[s] for s in LOW} in (set(LOW), set(HIGH))):
            maps.append(d)
    assert len(maps) == 8
    rem = set(codes)
    orbits = []
    while rem:
        code = next(iter(rem))
        orbit = set()
        for d in maps:
            transformed = frozenset(''.join(d[s] for s in w) for w in code)
            orbit.add(transformed)
            orbit.add(frozenset(w[::-1] for w in transformed))
        assert orbit <= codes
        orbits.append(len(orbit))
        rem.difference_update(orbit)
    return sorted(orbits)


def main():
    direct = constructions()
    best, brute, eligible = exhaustive_extremizers()
    assert len(SIGMA) ** 4 == 256
    assert sum(balanced(x) for x in map(''.join, product(SIGMA, repeat=4))) == 96
    assert eligible == 72, eligible
    assert best == 20
    assert brute == direct
    assert symmetries(brute) == [4, 8]
    print("VERIFY_OK: 96 balanced words; 72 unbordered words; optimum 20;")
    print("12 labeled optimal codes; two symmetry orbits of sizes 4 and 8.")


if __name__ == '__main__':
    main()
