"""Finite verification of the modal Kleene product-expansion census.

The identity checked is
    number of unary operations satisfying (MK), (Pos), (Con)
    on B_2^h x K_3^k = 2^(h*h)*(2^(h+k)+3^(h+k))^k.
All checks use exact finite arithmetic.  A general mathematical proof is required.
"""
from itertools import product
from math import comb


def local_checks(n, support):
    """Directly test the overlap and filter conditions for one output atom.

    The box-threshold 'None' means the output is never asserted;
    otherwise a mask P means the box holds exactly on supersets of P.
    A mask Q for diamond means the output holds exactly when it meets Q.
    """
    universe = (1 << n) - 1
    pairs = [(a, b) for a in range(1 << n) for b in range(1 << n)]
    admissible = {}
    for output in range(n):
        count = 0
        for p in [None] + list(range(1 << n)):
            for q in range(1 << n):
                def box(a):
                    return p is not None and (a & p) == p
                def diamond(b):
                    return (b & q) != 0
                overlap_ok = all(not (box(a) and diamond(b)) or (a & b) != 0
                                 for a, b in pairs)
                if not overlap_ok:
                    continue
                filter_ok = (not (support & (1 << output))) or all(
                    box(a) or diamond(b)
                    for a, b in pairs
                    if (a & b) == 0 and ((a | b) & support) == support)
                if filter_ok:
                    count += 1
        admissible[output] = count
        expected = ((1 << support.bit_count()) if support & (1 << output)
                    else ((1 << n) + 3**n))
        assert count == expected, (n, support, output, count, expected)
    return product_int(admissible.values())


def product_int(xs):
    out = 1
    for x in xs:
        out *= x
    return out


def brute_unary_operations(h, k):
    """Enumerate ALL functions on small fixed Kleene products and check axioms.

    This does not assume any representation or local-coordinate normal form.
    """
    els = list(product(*([range(2)] * h + [range(3)] * k)))
    size = len(els)
    ix = {a: i for i, a in enumerate(els)}
    meet = [[ix[tuple(min(x, y) for x, y in zip(a, b))]
             for b in els] for a in els]
    join = [[ix[tuple(max(x, y) for x, y in zip(a, b))]
             for b in els] for a in els]
    neg = [ix[tuple((1 if j < h else 2) - a[j]
                    for j in range(h + k))] for a in els]
    le = [[all(x <= y for x, y in zip(a, b))
           for b in els] for a in els]
    pos = [le[neg[z]][z] for z in range(size)]
    negative_part = [meet[z][neg[z]] for z in range(size)]
    positive_part = [join[z][neg[z]] for z in range(size)]
    count = 0
    for f in product(range(size), repeat=size):
        # (MK)
        if any(f[meet[x][y]] != meet[f[x]][f[y]]
               for x in range(size) for y in range(size)):
            continue
        # (Pos)
        if any(not pos[f[positive_part[z]]] for z in range(size)):
            continue
        # (Con)
        if any(not le[f[join[x][negative_part[z]]]][
            join[f[x]][neg[f[join[x][negative_part[z]]]]]]
            for x in range(size) for z in range(size)):
            continue
        count += 1
    return count


def main():
    local_cases = 0
    for n in range(1, 5):
        for support in range(1 << n):
            h = support.bit_count()
            computed = local_checks(n, support)
            expected = 2**(h*h) * ((2**n) + (3**n))**(n-h)
            assert computed == expected, (n, support, computed, expected)
            local_cases += 1
    independent_cases = 0
    for h, k in [(0, 1), (1, 0), (1, 1), (2, 0)]:
        computed = brute_unary_operations(h, k)
        expected = 2**(h*h) * (2**(h+k) + 3**(h+k))**k
        assert computed == expected, (h, k, computed, expected)
        independent_cases += 1
    print("ALL_CHECKS_OK", "filter_masks=", local_cases,
          "independent_full_unary_censuses=", independent_cases,
          "n_range=1..4", "carrier_sizes=2,3,4,6")


if __name__ == '__main__':
    main()
