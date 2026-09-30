from itertools import product

class UP:
    def __init__(self, prefix, cycle):
        assert cycle
        self.prefix = tuple(prefix)
        self.cycle = tuple(cycle)

    def value(self, n):
        if n < len(self.prefix):
            return self.prefix[n]
        return self.cycle[(n - len(self.prefix)) % len(self.cycle)]

    def persistent(self):
        return set(self.cycle)

    def min_ect_bound(self):
        inf = self.persistent()
        last_finite = -1
        for i, c in enumerate(self.prefix):
            if c not in inf:
                last_finite = i
        return last_finite + 1

    def valid_ect_bound(self, b):
        return b >= self.min_ect_bound()


def combine_f_h(f, h, ell):
    t0 = max(len(f.prefix), len(h.prefix))
    period_blocks = (len(f.cycle) * len(h.cycle)) // __import__("math").gcd(
        len(f.cycle), len(h.cycle)
    )
    prefix = []
    for t in range(t0):
        prefix.extend((4 * ell, 4 * f.value(t) + 1, 4 * h.value(t) + 2))
    cycle = []
    for t in range(t0, t0 + period_blocks):
        cycle.extend((4 * ell, 4 * f.value(t) + 1, 4 * h.value(t) + 2))
    return UP(prefix, cycle)


def combine_binary_tuple(ps):
    m = len(ps)
    if m == 0:
        return UP((), (0,))
    period = 1
    import math
    for p in ps:
        period = period * len(p.cycle) // math.gcd(period, len(p.cycle))
    cycle = []
    for t in range(period):
        cycle.append(3 * m)
        for i, p in enumerate(ps):
            cycle.append(3 * i + (1 if p.value(t) == 1 else 2))
    return UP((), cycle)


# Strong reduction isInfinite* <= CB on periodic binary inputs.
binary_cycles = [(0,), (1,), (0, 1), (1, 0)]
for m in range(4):
    for cycles in product(binary_cycles, repeat=m):
        ps = [UP((), cyc) for cyc in cycles]
        h = combine_binary_tuple(ps)
        S = h.persistent()
        markers = sorted(c for c in S if c % 3 == 0)
        assert markers == [3 * m]
        decoded_m = markers[0] // 3
        assert decoded_m == m
        got = [(3 * i + 1) in S for i in range(m)]
        want = [1 in set(p.cycle) for p in ps]
        assert got == want

# Strong reduction ECT x CB <= PECT on small ultimately periodic inputs.
def all_up(k):
    vals = range(k)
    for prefix in product(vals, repeat=2):
        for cycle_len in (1, 2):
            for cycle in product(vals, repeat=cycle_len):
                yield UP(prefix, cycle)

for k in (1, 2):
    for ell in (1, 2):
        for f in all_up(k):
            for h in all_up(ell):
                g = combine_f_h(f, h, ell)
                S = g.persistent()

                zero_mod_4 = sorted(c for c in S if c % 4 == 0)
                assert zero_mod_4 == [4 * ell]
                decoded_ell = zero_mod_4[0] // 4
                assert decoded_ell == ell

                got_basis = {j for j in range(ell) if 4 * j + 2 in S}
                assert got_basis == h.persistent()

                b0 = g.min_ect_bound()
                for b in (b0, b0 + 1, b0 + 2, b0 + 5):
                    assert g.valid_ect_bound(b)
                    B = (b + 1) // 3
                    assert f.valid_ect_bound(B)

print("VERIFY_OK")
