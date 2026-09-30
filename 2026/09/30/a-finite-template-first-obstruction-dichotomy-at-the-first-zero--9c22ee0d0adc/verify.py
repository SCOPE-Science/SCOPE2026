from itertools import product

def has_diagonal_point(size, unary, binary):
    return any((b in unary) and ((b, b) in binary) for b in range(size))

def has_hom(a_size, a_unary, a_binary, b_size, b_unary, b_binary):
    for f in product(range(b_size), repeat=a_size):
        if any(f[a] not in b_unary for a in a_unary):
            continue
        if any((f[a], f[b]) not in b_binary for a, b in a_binary):
            continue
        return True
    return False

for b_size in (1, 2):
    b_vertices = list(range(b_size))
    b_pairs = [(i, j) for i in b_vertices for j in b_vertices]
    unary_templates = [
        {i for i, bit in enumerate(bits) if bit}
        for bits in product((0, 1), repeat=b_size)
    ]
    binary_templates = [
        {pair for pair, bit in zip(b_pairs, bits) if bit}
        for bits in product((0, 1), repeat=len(b_pairs))
    ]

    for b_unary in unary_templates:
        for b_binary in binary_templates:
            diagonal = has_diagonal_point(
                b_size, b_unary, b_binary
            )

            if diagonal:
                a_vertices = (0, 1)
                a_pairs = [(i, j) for i in a_vertices for j in a_vertices]
                for unary_bits in product((0, 1), repeat=2):
                    a_unary = {
                        i for i, bit in enumerate(unary_bits) if bit
                    }
                    for binary_bits in product((0, 1), repeat=4):
                        a_binary = {
                            pair
                            for pair, bit in zip(a_pairs, binary_bits)
                            if bit
                        }
                        assert has_hom(
                            2, a_unary, a_binary,
                            b_size, b_unary, b_binary
                        )
            else:
                for pattern in product((0, 1), repeat=3):
                    a_unary = {
                        i for i, value in enumerate(pattern)
                        if value == 0
                    }
                    a_binary = {
                        (i, i) for i, value in enumerate(pattern)
                        if value == 0
                    }

                    first_failure = 0
                    for n in range(3):
                        prefix_unary = {i for i in a_unary if i <= n}
                        prefix_binary = {
                            (i, j) for i, j in a_binary
                            if i <= n and j <= n
                        }
                        if not has_hom(
                            n + 1, prefix_unary, prefix_binary,
                            b_size, b_unary, b_binary
                        ):
                            first_failure = n + 1
                            break

                    first_zero = next(
                        (i + 1 for i, value in enumerate(pattern)
                         if value == 0),
                        0
                    )
                    assert first_failure == first_zero

print("VERIFY_OK")
