from itertools import product
from math import comb, factorial


def whitney(m, r, n, k):
    if k < 0 or k > n:
        return 0
    if k == 0:
        return r ** n
    # explicit inclusion-exclusion formula
    s = 0
    for j in range(k + 1):
        s += (-1) ** (k - j) * comb(k, j) * (r + m * j) ** n
    return s // (factorial(k) * (m ** k))


def embedding_formula(u, v, a, c):
    return sum(
        (-1) ** (u - j) * comb(u, j) * (c + a * j) ** v
        for j in range(u + 1)
    )


def brute_descriptors(u, v, a, c):
    # One target coordinate is either a constant idempotent ('c',q)
    # or an automorphic copy ('a',source,auto-label).
    alphabet = [('c', q) for q in range(c)] + [
        ('a', j, alpha) for j in range(u) for alpha in range(a)
    ]
    count = 0
    for desc in product(alphabet, repeat=v):
        used = {x[1] for x in desc if x[0] == 'a'}
        if len(used) == u:
            count += 1
    return count


def z2_points(u):
    return list(product((0, 1), repeat=u))


def add3(x, y, z):
    return tuple((a ^ b ^ c) for a, b, c in zip(x, y, z))


def mul(x, y):
    return tuple((a & b) for a, b in zip(x, y))


def coordinate_homs_z2(u):
    dom = z2_points(u)
    idx = {x:i for i,x in enumerate(dom)}
    homs = []
    # maps A^u -> A, A={0,1}; at u<=3 at most 256 maps
    for bits in product((0,1), repeat=len(dom)):
        ok = True
        for x in dom:
            for y in dom:
                xy = mul(x,y)
                if bits[idx[xy]] != (bits[idx[x]] & bits[idx[y]]):
                    ok = False
                    break
            if not ok:
                break
        if not ok:
            continue
        for x in dom:
            for y in dom:
                for z in dom:
                    xyz = add3(x,y,z)
                    if bits[idx[xyz]] != (bits[idx[x]] ^ bits[idx[y]] ^ bits[idx[z]]):
                        ok = False
                        break
                if not ok:
                    break
            if not ok:
                break
        if ok:
            homs.append(bits)
    return dom, homs


def main():
    checks = 0

    # Check the r-Whitney recurrence over a broad exact integer grid.
    for m in range(1, 7):
        for r in range(0, 5):
            assert whitney(m, r, 0, 0) == 1
            checks += 1
            for n in range(0, 11):
                assert whitney(m, r, n, 0) == r ** n
                checks += 1
                for k in range(1, n + 1):
                    lhs = whitney(m, r, n + 1, k)
                    rhs = whitney(m, r, n, k - 1) + (r + m * k) * whitney(m, r, n, k)
                    assert lhs == rhs
                    checks += 1

    # Exhaustive symbolic coordinate-descriptor counts for small parameters.
    for a in range(1, 4):
        for c in range(0, 3):
            for u in range(1, 4):
                for v in range(0, 6):
                    brute = brute_descriptors(u, v, a, c)
                    formula = embedding_formula(u, v, a, c)
                    assert brute == formula
                    checks += 1
                    assert formula == factorial(u) * (a ** u) * whitney(a, c, v, u)
                    checks += 1

    # Concrete algebra A=(Z2, x-y+z, multiplication) from Mayr--Ruskuc Example 1.2.
    # Its automorphism group is trivial (a=1) and its idempotents are 0,1 (c=2).
    for u in range(1, 4):
        dom, homs = coordinate_homs_z2(u)
        expected_maps = []
        expected_maps.append(tuple(0 for _ in dom))
        expected_maps.append(tuple(1 for _ in dom))
        for j in range(u):
            expected_maps.append(tuple(x[j] for x in dom))
        assert set(homs) == set(expected_maps)
        checks += 1

        for v in range(1, 5):
            emb_count = 0
            images = set()
            for coords in product(homs, repeat=v):
                table = tuple(tuple(coord[i] for coord in coords) for i in range(len(dom)))
                if len(set(table)) == len(dom):
                    emb_count += 1
                    images.add(frozenset(table))
            assert emb_count == embedding_formula(u, v, 1, 2)
            checks += 1
            assert len(images) == whitney(1, 2, v, u)
            checks += 1

    # Automorphism-count consequence E_{u,u}=u! a^u.
    for a in range(1, 11):
        for c in range(0, 6):
            for u in range(1, 9):
                assert embedding_formula(u, u, a, c) == factorial(u) * (a ** u)
                checks += 1

    print(f"VERIFY_OK {checks} exact assertions")


if __name__ == '__main__':
    main()
