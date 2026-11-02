"""Independent matrix-group traversal for the projective stabilizer.
Run: python3 verify_group.py (requires verify_orbits.py alongside it).
"""
from verify_orbits import (MONS, G_TIMES_LINEAR, representative, to_coordinates,
                           substituted_monomials, symplectic_transvection)


def pack(matrix):
    return tuple(sum(matrix[i][j] << j for j in range(4)) for i in range(4))


def multiply(a, b):
    c = []
    for i in range(4):
        row = 0
        for j in range(4):
            value = 0
            for k in range(4):
                value ^= ((a[i] >> k) & 1) & ((b[k] >> j) & 1)
            row |= value << j
        c.append(row)
    return tuple(c)


def apply_polynomial(form, matrix):
    expansion = substituted_monomials([[(matrix[i] >> j) & 1 for j in range(4)]
                                      for i in range(4)])
    value = 0
    for j in range(35):
        if (form >> j) & 1:
            value ^= expansion[j]
    return value


def main():
    identity = (1, 2, 4, 8)
    generators = [pack(symplectic_transvection(v)) for v in range(1, 16)]
    group = [identity]
    seen = {identity}
    for matrix in group:
        for generator in generators:
            nxt = multiply(matrix, generator)
            if nxt not in seen:
                seen.add(nxt)
                group.append(nxt)
    assert len(group) == 720
    f = representative(13394)
    images = set()
    stabilizer = []
    for matrix in group:
        class_image = to_coordinates(apply_polynomial(f, matrix))
        images.add(class_image)
        if class_image == 13394:
            stabilizer.append(matrix)
    assert len(images) == 144 and len(stabilizer) == 5
    generator = (4, 9, 6, 7)
    assert generator in stabilizer and generator != identity
    power = identity
    for _ in range(5):
        power = multiply(power, generator)
    assert power == identity
    # Applying this generator to F changes it by YG, without changing V(G,F).
    assert apply_polynomial(f, generator) ^ f == G_TIMES_LINEAR[1]
    for vector in range(1, 16):
        image = 0
        for i in range(4):
            image |= ((generator[i] & vector).bit_count() & 1) << i
        assert image != vector
    print('GROUP_VERIFY_OK; |Sp4(F2)|=720; smooth orbit size=144; projective stabilizer=C5')
    print('matrix rows', generator, '; F(Ax)+F(X)=Y G(X); A^5=I')


if __name__ == '__main__':
    main()
