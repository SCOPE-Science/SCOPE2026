"""Independent signed-face trace test for independence complexes of cycles.

No external dependencies. Tests all dihedral elements on n=3,...,20.
"""
from math import gcd


def independent_masks(n):
    def rec(i, prev, first, mask):
        if i == n:
            if not (first and prev):
                yield mask
            return
        yield from rec(i + 1, 0, first, mask)
        if not prev and not (i == n - 1 and first):
            yield from rec(i + 1, 1, first or (i == 0), mask | (1 << i))
    return list(rec(0, 0, False, 0))


def pf(k):
    a, b = 1, 0
    if k == 0:
        return a
    for _ in range(2, k + 1):
        a, b = b, b - a
    return b


def cyc(k):
    if k < 2:
        raise ValueError('cycle at least two')
    a, b = -1, -2
    if k == 2:
        return a
    if k == 3:
        return b
    for _ in range(4, k + 1):
        a, b = b, b-a
    return b


def predicted(n, j, reflected):
    d = (n - 2) // 3
    sign = (-1) ** (d + 1)
    if not reflected:
        return sign * (cyc(gcd(n, j)) if gcd(n, j) >= 2 else 1)
    if n & 1:
        return sign * pf((n - 1) // 2)
    return sign * (pf(n // 2 + 1) if j % 2 == 0 else pf(n // 2 - 2))


def act(n, j, reflection, mask):
    order = [i for i in range(n) if mask & (1 << i)]
    moved = [(j - i if reflection else j + i) % n for i in order]
    newmask = sum(1 << x for x in moved)
    parity = sum(a > b for i, a in enumerate(moved) for b in moved[i+1:]) & 1
    return newmask, -1 if parity else 1


def main():
    cases = 0
    for n in range(3, 21):
        faces = independent_masks(n)
        for refl in (False, True):
            for j in range(n):
                signed_sum = 0
                for mask in faces:
                    image, parity = act(n, j, refl, mask)
                    if image == mask:
                        signed_sum += (-1 if mask.bit_count() & 1 else 1) * parity
                got = (-1) ** (((n - 2) // 3) + 1) * signed_sum
                expected = predicted(n, j, refl)
                assert got == expected, (n, j, refl, got, expected)
                cases += 1
        inv = sum(predicted(n,j,refl) for refl in (False,True) for j in range(n)) // (2*n)
        assert inv == (1 if n % 12 in (1,11) else 0), (n, inv)
    print('FIXED_FACES_OK', cases, 'dihedral elements tested n=3..20')

if __name__ == '__main__':
    main()
