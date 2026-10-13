#!/usr/bin/env python3
"""Exact finite certificate for three-event Sahi positivity on the Boolean 3-cube.

Only the Python standard library is needed. Every input distribution with three
independent Bernoulli coordinates is handled by a coefficientwise polynomial
identity; finite sampling is not used.
"""
from itertools import combinations_with_replacement, product

DIM = 3
STATES = tuple(range(1 << DIM))


def is_upset(mask):
    return all(not ((mask >> v) & 1)
               or all((mask >> w) & 1 for w in STATES if (v & w) == v)
               for v in STATES)


def bernoulli_numerator(mask, pos, neg):
    total = 0
    for v in STATES:
        if (mask >> v) & 1:
            term = 1
            for i in range(DIM):
                term *= pos[i] if (v >> i) & 1 else neg[i]
            total += term
    return total


def main():
    upsets = tuple(mask for mask in range(1 << len(STATES)) if is_upset(mask))
    assert len(upsets) == 20
    assert upsets[0] == 0 and upsets[-1] == 255
    # G is the three-replica polarization of the triple correlation E3.
    # The indexing classifies each 3-by-3 binary array by its three
    # coordinate-wise counts among the rows.
    arrays = []
    for x, y, z in product(STATES, repeat=3):
        counts = tuple(((x >> i) & 1) + ((y >> i) & 1) + ((z >> i) & 1)
                       for i in range(DIM))
        idx = 16 * counts[0] + 4 * counts[1] + counts[2]
        arrays.append((x, y, z, idx))
    assert len(arrays) == 512
    assert len(set(q[3] for q in arrays)) == 64

    # An independent rational-parameter check: p = (1/3,2/5,3/7).
    denominator = 105 ** 3
    pos = (35, 42, 45)
    neg = (70, 63, 60)
    measure = {mask: bernoulli_numerator(mask, pos, neg) for mask in range(256)}
    weights = []
    for idx in range(64):
        k = (idx // 16, (idx // 4) % 4, idx % 4)
        weights.append(product_of(pos[i] ** k[i] * neg[i] ** (3-k[i])
                                  for i in range(DIM)))

    triples = 0
    nonnegative_coefficients = 0
    positive_coefficients = 0
    smallest_positive = None
    largest_coefficient = 0
    zero_polynomials = 0
    nonzero_polynomials = 0
    sum_numerators = 0

    for a, b, c in combinations_with_replacement(upsets, 3):
        coefficients = [0] * 64
        for x, y, z, idx in arrays:
            ax, ay, bx, by, cx, cy, cz = ((a >> x) & 1, (a >> y) & 1,
                                         (b >> x) & 1, (b >> y) & 1,
                                         (c >> x) & 1, (c >> y) & 1,
                                         (c >> z) & 1)
            # Exactly 2 E[ABC] + E[A]E[B]E[C]
            # - E[A]E[BC] - E[B]E[AC] - E[C]E[AB].
            g = (2 * ax * bx * cx
                 + ax * by * cz
                 - ax * by * cy
                 - bx * ay * cy
                 - cx * ay * by)
            coefficients[idx] += g
        assert len(coefficients) == 64
        assert min(coefficients) >= 0, (a, b, c, min(coefficients))
        nonnegative_coefficients += 64
        positives = [u for u in coefficients if u > 0]
        positive_coefficients += len(positives)
        if positives:
            nonzero_polynomials += 1
            smallest_positive = min(smallest_positive or min(positives), min(positives))
        else:
            zero_polynomials += 1
        largest_coefficient = max(largest_coefficient, max(coefficients))
        triples += 1

        # Independent evaluation through exact event probabilities.
        PA, PB, PC = measure[a], measure[b], measure[c]
        PAB, PAC, PBC = (measure[a & b], measure[a & c], measure[b & c])
        PABC = measure[a & b & c]
        direct = (2 * PABC * denominator ** 2 + PA * PB * PC
                  - denominator * PA * PBC
                  - denominator * PB * PAC - denominator * PC * PAB)
        via_coefficients = sum(coef * weight for coef, weight
                               in zip(coefficients, weights))
        assert direct == via_coefficients, (a, b, c, direct, via_coefficients)

        # Separate verification of normalization at p=(1/2,1/2,1/2).
        na, nb, nc = a.bit_count(), b.bit_count(), c.bit_count()
        direct_half = (2 * (a & b & c).bit_count() * 64
                       + na * nb * nc
                       - na * (b & c).bit_count() * 8
                       - nb * (a & c).bit_count() * 8
                       - nc * (a & b).bit_count() * 8)
        assert sum(coefficients) == direct_half
        sum_numerators += sum(coefficients)

    assert triples == 1540
    assert nonnegative_coefficients == 98560
    print(f"UPSETS {len(upsets)}")
    print(f"UNORDERED_TRIPLES {triples}")
    print(f"REPLICA_ARRAYS {len(arrays)}")
    print(f"BERNSTEIN_CELLS {nonnegative_coefficients}")
    print(f"STRICT_POSITIVE_CELLS {positive_coefficients}")
    print(f"ZERO_CELLS {nonnegative_coefficients-positive_coefficients}")
    print(f"SMALLEST_POSITIVE {smallest_positive}")
    print(f"LARGEST_COEFFICIENT {largest_coefficient}")
    print(f"NONZERO_TRIPLES {nonzero_polynomials}")
    print(f"ZERO_TRIPLES {zero_polynomials}")
    print(f"SUM_OF_ALL_COEFFICIENTS {sum_numerators}")
    print("EXACT_VERIFICATION PASS")


def product_of(values):
    result = 1
    for x in values:
        result *= x
    return result


if __name__ == '__main__':
    main()
