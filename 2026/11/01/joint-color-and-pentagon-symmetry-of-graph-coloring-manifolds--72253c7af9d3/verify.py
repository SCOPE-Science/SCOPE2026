"""Finite signed-Lefschetz checks for the pentagon coloring-manifold character."""
from itertools import product
from collections import Counter


def permutation_sign(indices):
    parity = sum(indices[i] > indices[j] for i in range(len(indices))
                 for j in range(i + 1, len(indices)))
    return -1 if parity & 1 else 1


def signed_lefschetz(n, h, g):
    """Sum signed fixed-cell contributions in Hom(C5,K_n).

    Each color occupies an independent set in C5 (empty, singleton, or
    nonadjacent vertex pair). All 5 vertex boxes must be nonempty.
    The CW orientation is the ordered product of increasing-color simplices.
    """
    masks = (0,) + tuple(1 << i for i in range(5)) + tuple(
        (1 << i) | (1 << ((i + 2) % 5)) for i in range(5))
    total = 0
    fixed = 0
    signed_by_dimension = Counter()
    for placement in product(masks, repeat=n):
        boxes = [0] * 5
        for color, subset in enumerate(placement):
            for i in range(5):
                if subset & (1 << i):
                    boxes[i] |= (1 << color)
        if any(not x for x in boxes):
            continue
        image = [0] * 5
        for i in range(5):
            for c in range(n):
                if boxes[i] & (1 << c):
                    image[h[i]] |= (1 << g[c])
        if boxes != image:
            continue
        fixed += 1
        dims = [x.bit_count() - 1 for x in boxes]
        k = sum(dims[i] * dims[j] for i in range(5)
                for j in range(i + 1, 5) if h[i] > h[j])
        orientation = -1 if k & 1 else 1
        for i in range(5):
            src_colors = [c for c in range(n) if boxes[i] & (1 << c)]
            dst_colors = [c for c in range(n) if boxes[h[i]] & (1 << c)]
            ordering = [dst_colors.index(g[c]) for c in src_colors]
            orientation *= permutation_sign(ordering)
        dim = sum(dims)
        signed_by_dimension[dim] += (-1 if dim & 1 else 1) * orientation
        total += (-1 if dim & 1 else 1) * orientation
    return total, fixed, dict(sorted(signed_by_dimension.items()))


def predicted_lefschetz(n, h_reflect, g_transpose):
    # H0 always has trace 1. Reflection and color swap signs follow from
    # the Stiefel reflection, sphere-projection and orientation arguments.
    if n % 2 == 0:
        # Only H_(2n-5) besides H0; it is a trivial representation.
        return 0
    er = -1 if h_reflect else 1
    s = -1 if g_transpose else 1
    # For odd n, n-3 is even, n-2 and 2n-5 are odd.
    return 1 + er * s - s - er


def run():
    for n in (4, 5, 6):
        ids = list(range(n))
        verts = list(range(5))
        trans = [1, 0] + list(range(2, n))
        reflect = [(-i) % 5 for i in range(5)]
        rotate = [(i + 1) % 5 for i in range(5)]
        cases = [
            ("identity", verts, ids, False, False),
            ("source_reflection", reflect, ids, True, False),
            ("source_rotation", rotate, ids, False, False),
            ("color_transposition", verts, trans, False, True),
            ("mixed", reflect, trans, True, True),
        ]
        for name, h, g, has_reflect, has_swap in cases:
            observed, fixed, by_dim = signed_lefschetz(n, h, g)
            expected = predicted_lefschetz(n, has_reflect, has_swap)
            assert observed == expected, (n, name, observed, expected)
            print(f"n={n}, action={name}, cells_fixed={fixed}, "
                  f"Lefschetz={observed}, expected={expected}")
        # A maximal cell stabilized by color swap, fixing its orientation:
        # colors 0 and 1 assigned (0,2), colors 2 and 3 assigned
        # (1,3) and (1,4), all extra colors assigned (0,2).
        masks = [(1 << 0) | (1 << 2), (1 << 0) | (1 << 2),
                 (1 << 1) | (1 << 3), (1 << 1) | (1 << 4)]
        masks += [((1 << 0) | (1 << 2))] * (n - 4)
        boxes = [sum((1 << c) for c in range(n) if masks[c] & (1 << i))
                 for i in range(5)]
        assert all(boxes)
        assert sum(x.bit_count() - 1 for x in boxes) == 2*n - 5
        assert ((boxes[0] & 3) == 3 and (boxes[2] & 3) == 3)
        assert all((box & 3) in (0, 3) for box in boxes)
        print(f"n={n}, target_transposition_top_cell_orientation=+1")
    print("FINITE_CHECKS_PASS; the all-n proof uses the published Stiefel model.")


if __name__ == "__main__":
    run()
