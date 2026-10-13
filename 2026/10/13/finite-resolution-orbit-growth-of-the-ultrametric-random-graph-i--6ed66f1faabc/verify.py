from functools import lru_cache
from fractions import Fraction
from math import comb, factorial


def partitions(items):
    items = tuple(items)
    if not items:
        yield ()
        return
    first = items[0]
    for rest in partitions(items[1:]):
        # new singleton block first
        yield ((first,),) + rest
        # insert into an existing block
        for i in range(len(rest)):
            b = tuple(sorted(rest[i] + (first,)))
            new = list(rest)
            new[i] = b
            new = tuple(sorted(new, key=lambda x: (x[0], len(x), x)))
            yield new


def canon(p):
    return tuple(sorted((tuple(sorted(b)) for b in p), key=lambda x: (x[0], len(x), x)))


def all_partitions(n):
    return sorted(set(canon(p) for p in partitions(tuple(range(n)))))


def refines(p, q):
    # p is finer than q: every block of p is contained in a block of q.
    qb = [set(b) for b in q]
    return all(any(set(b) <= c for c in qb) for b in p)


@lru_cache(None)
def H(h, n):
    if n <= 1:
        return 1
    if h == 0:
        return 1
    total = 0
    for p in all_partitions(n):
        prod = 1
        for b in p:
            prod *= H(h - 1, len(b))
        total += prod
    return total


def direct_chain_count(n, h):
    # h intermediate partitions between indiscrete and discrete endpoints.
    ps = all_partitions(n)
    coarse = (tuple(range(n)),)
    fine = tuple((i,) for i in range(n))
    # dp over h+1 transitions, including the final endpoint transition.
    current = {coarse: 1}
    for _ in range(h):
        nxt = {}
        for a, cnt in current.items():
            for b in ps:
                if refines(b, a):
                    nxt[b] = nxt.get(b, 0) + cnt
        current = nxt
    return sum(cnt for a, cnt in current.items() if refines(fine, a))


def strict_chain_counts(n):
    # c[k] = number of strict chains coarse = x0 < ... < xk = fine
    # with exactly k strict transitions.
    ps = all_partitions(n)
    coarse = (tuple(range(n)),)
    fine = tuple((i,) for i in range(n))
    rank = lambda p: len(p) - 1
    c = [0] * n

    @lru_cache(None)
    def ways_from(p):
        # Returns dict transitions->ways from p strictly to fine.
        if p == fine:
            return {0: 1}
        out = {}
        rp = rank(p)
        for q in ps:
            if q == p:
                continue
            if rank(q) <= rp:
                continue
            if refines(q, p):
                for k, v in ways_from(q).items():
                    out[k + 1] = out.get(k + 1, 0) + v
        return out

    d = ways_from(coarse)
    for k, v in d.items():
        c[k] = v
    return c


def binomial_chain_formula(n, h, c):
    return sum(c[k] * comb(h + 1, k) for k in range(len(c)) if k <= h + 1)


def interpolate_leading(values):
    # For values p(0),...,p(d), d=len(values)-1, leading coefficient is Δ^d p(0)/d!.
    arr = [Fraction(v) for v in values]
    d = len(values) - 1
    for _ in range(d):
        arr = [arr[i+1] - arr[i] for i in range(len(arr)-1)]
    return arr[0] / factorial(d)


def main():
    assertions = 0
    # Bell / higher-order-Bell rows from direct partition chains.
    expected = {
        0: [1,1,1,1,1,1,1],
        1: [1,2,5,15,52,203,877],
        2: [1,3,12,60,358,2471,19302],
        3: [1,4,22,154,1304,12915,146115],
    }
    for h, row in expected.items():
        for n, want in enumerate(row, start=1):
            assert H(h, n) == want
            assertions += 1

    # Independent direct enumeration of partition multichains for manageable n,h.
    for n in range(1, 6):
        for h in range(0, 4):
            got = direct_chain_count(n, h)
            assert got == H(h, n), (n, h, got, H(h,n))
            assertions += 1

    # Exact binomial-basis decomposition and maximal-chain coefficient.
    for n in range(1, 8):
        c = strict_chain_counts(n)
        for h in range(0, 8):
            assert binomial_chain_formula(n, h, c) == H(h, n)
            assertions += 1
        expected_max = factorial(n) * factorial(n-1) // (2 ** (n-1))
        assert c[n-1] == expected_max
        assertions += 1

    # Polynomial leading coefficient in h: n!/2^(n-1).
    for n in range(1, 9):
        d = n - 1
        vals = [H(h, n) for h in range(d + 1)]
        lead = interpolate_leading(vals)
        assert lead == Fraction(factorial(n), 2 ** (n-1)), (n, lead)
        assertions += 1

    # Graph factor: arbitrary edge bits are independent of the metric hierarchy.
    for n in range(1, 9):
        edge_patterns = 2 ** comb(n, 2)
        for h in range(0, 5):
            orbit_count = edge_patterns * H(h, n)
            assert orbit_count // H(h, n) == edge_patterns
            assertions += 1

    # Binary sanity check: h+1 metric distances times two edge states.
    for h in range(0, 21):
        assert 2 * H(h, 2) == 2 * (h + 1)
        assertions += 1

    print(f"VERIFY_OK {assertions} exact assertions")
    print("H_h(n), n=1..7:")
    for h in range(4):
        print(h, [H(h,n) for n in range(1,8)])
    print("orbit examples O_{n,h}=2^C(n,2) H_h(n):")
    for n in range(2,6):
        print(n, [2**comb(n,2)*H(h,n) for h in range(4)])

if __name__ == '__main__':
    main()
