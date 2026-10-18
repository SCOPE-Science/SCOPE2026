"""Reproducible finite check of the wheel-matching dihedral character.

Build all matchings directly from graph edges. For each automorphism, compute
its signed action on oriented simplices and evaluate the reduced Lefschetz
number. With the proven one-degree concentration, this equals the character
up to the indicated homological sign. Independent of the induced-module proof.
"""

def all_matchings(n):
    edges = [(j, (j + 1) % n) for j in range(n)] + [(j, n) for j in range(n)]
    def build(start, used, face):
        yield tuple(face)
        for j in range(start, 2 * n):
            a, b = edges[j]
            if (used >> a) & 1 or (used >> b) & 1:
                continue
            yield from build(j + 1, used | (1 << a) | (1 << b), face + [j])
    return list(build(0, 0, []))


def oriented_trace(face, permutation):
    image = [permutation[j] for j in face]
    if set(image) != set(face):
        return 0
    inversions = sum(image[i] > image[j]
                     for i in range(len(image)) for j in range(i + 1, len(image)))
    return -1 if inversions % 2 else 1


def direct_trace(n, element, exponent, matchings):
    if element == 'rotation':
        rim_map = [(i + exponent) % n for i in range(n)]
        spoke_map = [(i + exponent) % n for i in range(n)]
    else:
        rim_map = [(exponent - i - 1) % n for i in range(n)]
        spoke_map = [(exponent - i) % n for i in range(n)]
    permutation = rim_map + [n + x for x in spoke_map]
    reduced_lefschetz = -1  # Empty augmented simplex.
    for face in matchings:
        if not face:
            continue
        tr = oriented_trace(face, permutation)
        if tr:
            reduced_lefschetz += (-1) ** (len(face) - 1) * tr
    return (-1) ** (n // 3) * reduced_lefschetz


def formula(n, element, exponent):
    assert n >= 4 and n % 3 in (1, 2)
    k = n // 3
    epsilon = n % 3
    alpha = (-1) ** (k * (k + 1) // 2) if epsilon == 1 else (-1) ** (k * (k - 1) // 2)
    rotation_line = (-1) ** (n + 1)
    reflection_line = alpha if epsilon == 1 else (-1) ** ((k + 1) * (k + 2) // 2)
    sign = -1 if epsilon == 1 else 1
    if element == 'rotation':
        return (n if exponent == 0 else 0) + sign * rotation_line ** exponent
    reflection_fixed_spokes = (1 if n % 2 else (2 if exponent % 2 == 0 else 0))
    return alpha * reflection_fixed_spokes + sign * rotation_line ** exponent * reflection_line


def main():
    for n in (4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20):
        faces = all_matchings(n)
        for element in ('rotation', 'reflection'):
            for exponent in range(n):
                actual = direct_trace(n, element, exponent, faces)
                expected = formula(n, element, exponent)
                assert actual == expected, (n, element, exponent, actual, expected)
        print(f'PASS n={n}, simplices_including_empty={len(faces)}, top_rank={formula(n, "rotation", 0)}')
    print('FINITE_CHARACTER_CHECK_OK')


if __name__ == '__main__':
    main()
