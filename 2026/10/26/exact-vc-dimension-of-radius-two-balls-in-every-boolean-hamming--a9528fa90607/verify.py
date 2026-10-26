#!/usr/bin/env python3
"""Exact finite certificate for the radius-two Boolean Hamming-ball VC theorem.

No dependencies beyond Python 3.10+. All bit masks encode the complete center universe;
no randomness or heuristic pruning is used.
"""
from math import comb


def trace_mask(sample, dimension, radii):
    """Bit j indicates sample lies within the radius of center j.

    Centers are ordered as blocks indexed by radii then numeric binary center.
    """
    n_centers = 1 << dimension
    ans = 0
    for i, radius in enumerate(radii):
        base = i * n_centers
        for center in range(n_centers):
            if (sample ^ center).bit_count() <= radius:
                ans |= 1 << (base + center)
    return ans


def shattering_profile(dimension, radii, samples, max_size, anchored=False):
    """Count every shattered k-subset of samples for 2 <= k <= max_size.

    The sample list must have distinct elements. Lexicographic extension visits
    precisely every subset with a shattered predecessor; a shattered subset
    necessarily has a shattered predecessor.
    """
    assert len(samples) == len(set(samples))
    n_concepts = (1 << dimension) * len(radii)
    universe = (1 << n_concepts) - 1
    masks = [trace_mask(x, dimension, radii) for x in samples]
    assert all(mask and mask != universe for mask in masks)
    indices = (0,) if anchored else range(len(masks))
    states = [((i,), (masks[i], universe ^ masks[i])) for i in indices]
    counts = {}
    witnesses = {}
    for size in range(2, max_size + 1):
        next_states = []
        for selected, classes in states:
            for i in range(selected[-1] + 1, len(samples)):
                inc = masks[i]
                new_classes = []
                for c in classes:
                    a = c & inc
                    b = c & (universe ^ inc)
                    if a == 0 or b == 0:
                        break
                    new_classes.extend((a, b))
                else:
                    next_states.append((selected + (i,), tuple(new_classes)))
        counts[size] = len(next_states)
        if next_states:
            witnesses[size] = tuple(samples[i] for i in next_states[0][0])
        states = next_states
        if not states:
            break
    return counts, witnesses


def check_witness(dimension, points):
    traces = set()
    for center in range(1 << dimension):
        trace = sum(1 << i for i, x in enumerate(points)
                    if (center ^ x).bit_count() <= 2)
        traces.add(trace)
    assert len(traces) == 1 << len(points)


def main():
    samples = [x for x in range(1 << 10) if x.bit_count() <= 2]
    assert len(samples) == 1 + 10 + comb(10, 2) == 56
    kernel_counts, _ = shattering_profile(10, (0, 1, 2), samples, 5)
    assert [kernel_counts[i] for i in (2, 3, 4, 5)] == [1540, 27720, 49830, 0]
    print("UPPER_KERNEL dimension=10 center_radii=0,1,2 candidates=56",
          "counts=1540,27720,49830,0 PASS")

    expected = {1: 0, 2: 0, 3: 1, 4: 3, 5: 4, 6: 4, 7: 4, 8: 4}
    for d in range(1, 9):
        if d <= 2:
            assert all((center ^ x).bit_count() <= 2
                       for center in range(1 << d) for x in range(1 << d))
            got = 0
        elif d == 3:
            # Every closed two-ball in the 3-cube omits precisely its antipode.
            assert all(sum((center ^ x).bit_count() > 2
                           for x in range(1 << d)) == 1
                       for center in range(1 << d))
            got = 1
        else:
            # Translational symmetry moves one chosen sample point to zero.
            counts, _ = shattering_profile(d, (2,), list(range(1 << d)), 5, anchored=True)
            got = max(k for k, num in counts.items() if num > 0)
            assert counts.get(5, 0) == 0
        assert got == expected[d], (d, got)
        print("CUBE", d, "VC", got, "PASS")

    check_witness(4, (0, 1, 2))
    check_witness(5, (0, 1, 2, 4))
    print("WITNESSES dimensions=4,5 all_patterns=PASS")
    print("VERIFY_OK finite_kernel=PASS all_dimension_proof_reduction=MATHEMATICAL_LEMMA"
          " lower_witnesses=PASS independent_small_cubes=PASS")

if __name__ == '__main__':
    main()
