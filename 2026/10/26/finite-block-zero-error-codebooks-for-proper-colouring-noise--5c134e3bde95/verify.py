"""Finite checks for the proper-colouring additive-noise channel."""
from itertools import product


def words(q, n):
    return list(product(range(q), repeat=n))


def proper_noise(q, n):
    return [z for z in words(q, n) if all(z[i] != z[i + 1] for i in range(n - 1))]


def binary_check(n):
    universe = words(2, n)
    noise = proper_noise(2, n)
    assert len(noise) == 2
    assert all(tuple(1 - b for b in z) in noise for z in noise)
    pairs = []
    seen = set()
    for x in universe:
        if x not in seen:
            xb = tuple(1 - b for b in x)
            pairs.append((x, xb))
            seen.update((x, xb))
    assert len(pairs) == 2 ** (n - 1)
    # Each complement pair has a common output set; different pairs do not.
    pair_outputs = []
    for x, xb in pairs:
        ox = {tuple((a + b) % 2 for a, b in zip(x, z)) for z in noise}
        ob = {tuple((a + b) % 2 for a, b in zip(xb, z)) for z in noise}
        assert ox == ob
        pair_outputs.append(ox)
    assert len({frozenset(o) for o in pair_outputs}) == len(pairs)
    assert 2 ** len(pairs) == 2 ** (2 ** (n - 1))
    return len(noise), len(pairs), 2 ** len(pairs)


def qary_difference_check(q, n):
    # Check that every target difference is the difference of two proper words.
    zwords = proper_noise(q, n)
    diffs = {tuple((a - b) % q for a, b in zip(z, zp)) for z in zwords for zp in zwords}
    return len(diffs), q ** n


if __name__ == "__main__":
    for n in range(1, 6):
        print("binary", n, binary_check(n))
    for q in range(3, 6):
        for n in range(1, 5):
            got, total = qary_difference_check(q, n)
            assert got == total
            print("qary", q, n, got, total)
