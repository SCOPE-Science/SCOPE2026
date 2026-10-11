"""Exact finite checks for minimal tight Fourier sampling of a four-point simplex.

Requires only Python 3.9+ standard library; all arithmetic is integral.
The infinite family of prime-field claims is proved algebraically in RESULT.md;
this program certifies only the finite cases p=2,3.
"""
from itertools import combinations, product

D3 = ((1, 0, 0), (0, 1, 0), (0, 0, 1),
      (1, 2, 0), (1, 0, 2), (0, 1, 2))
B0 = ((0, 0, 0), (0, 1, 1), (1, 0, 2),
      (1, 2, 0), (2, 1, 2), (2, 2, 1))


def dot(x, y, p):
    return sum(a * b for a, b in zip(x, y)) % p


def differences(p):
    e = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    return e + tuple(tuple((e[i][k] - e[j][k]) % p
                             for k in range(3))
                     for i, j in ((0, 1), (0, 2), (1, 2)))


def is_tight(B, p):
    """Equivalently M_B M_B* == |B| I_4 for the cube-root Fourier matrix."""
    if not B or len(set(B)) != len(B) or len(B) % p:
        return False
    target = len(B) // p
    for d in differences(p):
        histogram = [0] * p
        for b in B:
            histogram[dot(d, b, p)] += 1
        if histogram != [target] * p:
            return False
    return True


def translate(B, t, p):
    return tuple(sorted(tuple((b[i] + t[i]) % p for i in range(3))
                        for b in B))


def group(p):
    return tuple(product(range(p), repeat=3))


def verify_binary():
    G = group(2)
    all_four = {B for B in combinations(G, 4) if is_tight(B, 2)}
    even = tuple(x for x in G if sum(x) % 2 == 0)
    odd = tuple(x for x in G if sum(x) % 2 == 1)
    assert all_four == {even, odd}, (len(all_four), all_four)
    assert len(all_four) == 2
    assert len(tuple(combinations(G, 4))) == 70
    return 70, len(all_four)


def verify_ternary():
    G = group(3)
    assert len(G) == 27
    assert is_tight(B0, 3)
    all_six = {B for B in combinations(G, 6) if is_tight(B, 3)}
    assert len(all_six) == 27, len(all_six)
    translated = {translate(B0, t, 3) for t in G}
    assert len(translated) == 27
    assert all_six == translated

    zero = (0, 0, 0)
    zero_six = {tuple(sorted((zero,) + B))
                for B in combinations(G[1:], 5)
                if is_tight((zero,) + B, 3)}
    translates_with_zero = {B for B in translated if zero in B}
    assert len(zero_six) == len(translates_with_zero) == 6
    assert zero_six == translates_with_zero

    # Additional exact matrix proof: each off-diagonal row inner product
    # is represented in Z[omega] as (c0-c2)+(c1-c2)*omega.
    A = ((0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1))
    for B in all_six:
        for i in range(4):
            for j in range(4):
                counts = [0, 0, 0]
                for b in B:
                    exponent = (dot(A[i], b, 3) - dot(A[j], b, 3)) % 3
                    counts[exponent] += 1
                if i == j:
                    assert counts == [6, 0, 0]
                else:
                    assert counts == [2, 2, 2]
    return 296010, len(all_six), 65780, len(zero_six)


def verify_large_prime_witnesses():
    # Checks illustrate, but do NOT replace the symbolic proof for all p >= 5.
    for p in (5, 7, 11, 13):
        v = (1, 2, 3)
        B = tuple(tuple((t * vi) % p for vi in v) for t in range(p))
        assert is_tight(B, p)


if __name__ == '__main__':
    n2, t2 = verify_binary()
    n3, t3, nz, tz = verify_ternary()
    verify_large_prime_witnesses()
    print('p=2: tested', n2, 'four-frequency sets; optimizers:', t2)
    print('p=3: tested', n3, 'six-frequency sets; optimizers:', t3)
    print('p=3 normalized: tested', nz, 'six-frequency sets through zero; optimizers:', tz)
    print('p>=5: integer witness checks p=5,7,11,13 passed; general proof is symbolic.')
