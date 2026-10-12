"""Finite checks for affine stabilizers of three-point evaluation sets.

Run: python3 verify.py
Only the Python standard library is needed.
The symbolic proof in RESULT.md covers every finite field; these tests
independently enumerate selected finite fields and unordered RS outputs.
"""
from itertools import combinations
from math import comb


class Field:
    def __init__(self, p, modulus=None):
        self.p = p
        self.modulus = modulus
        self.degree = len(modulus) - 1 if modulus else 1
        self.q = p ** self.degree

    def coordinates(self, x):
        return [(x // (self.p ** j)) % self.p for j in range(self.degree)]

    def pack(self, v):
        return sum((int(c) % self.p) * self.p ** j for j, c in enumerate(v))

    def add(self, a, b):
        return self.pack([(x + y) % self.p for x, y in
                          zip(self.coordinates(a), self.coordinates(b))])

    def mul(self, a, b):
        if self.modulus is None:
            return (a * b) % self.p
        aa, bb = self.coordinates(a), self.coordinates(b)
        c = [0] * (2 * self.degree - 1)
        for i, ai in enumerate(aa):
            for j, bj in enumerate(bb):
                c[i + j] = (c[i + j] + ai * bj) % self.p
        for i in range(len(c) - 1, self.degree - 1, -1):
            coefficient = c[i]
            for j in range(self.degree):
                c[i - self.degree + j] = (
                    c[i - self.degree + j] - coefficient * self.modulus[j]
                ) % self.p
        return self.pack(c[:self.degree])

    def normed_output(self, a, b, triple):
        return tuple(sorted(self.add(self.mul(a, x), b) for x in triple))


def expected_counts(p, q):
    arithmetic_progressions = (
        0 if p == 2 else q * (q - 1) // (6 if p == 3 else 2)
    )
    order_three = q * (q - 1) // 3 if p != 3 and (q - 1) % 3 == 0 else 0
    d = ({6: arithmetic_progressions, 1: comb(q, 3) - arithmetic_progressions}
         if p == 3 else
         {2: arithmetic_progressions, 3: order_three,
          1: comb(q, 3) - arithmetic_progressions - order_three})
    return {k: v for k, v in d.items() if v}


def main():
    configurations = (
        (2, None), (3, None), (2, [1, 1, 1]), (5, None),
        (7, None), (2, [1, 1, 0, 1]), (3, [1, 0, 1]),
        (11, None), (13, None), (2, [1, 1, 0, 0, 1]),
    )
    for p, modulus in configurations:
        F = Field(p, modulus)
        counts = {}
        rigid = []
        for E in combinations(range(F.q), 3):
            unordered_E = frozenset(E)
            stabilizer = sum(
                frozenset(F.add(F.mul(a, x), b) for x in E) == unordered_E
                for a in range(1, F.q) for b in range(F.q)
            )
            counts[stabilizer] = counts.get(stabilizer, 0) + 1
            if stabilizer == 1:
                rigid.append(E)
            # Directly group all q^2 codewords by their unordered outputs.
            if F.q <= 9:
                fibers = {}
                for a in range(F.q):
                    for b in range(F.q):
                        output = F.normed_output(a, b, E)
                        fibers[output] = fibers.get(output, 0) + 1
                assert sorted(fibers.values()) == sorted(
                    [1] * F.q + [stabilizer] * (F.q * (F.q - 1) // stabilizer)
                )
        assert counts == expected_counts(p, F.q), (F.q, counts, expected_counts(p, F.q))
        print('q=%2d: stabilizer distribution %s; rigid triples %d' %
              (F.q, dict(sorted(counts.items())), len(rigid)))
        if F.q in (2, 3, 4, 5, 7):
            assert not rigid
        if F.q == 8:
            assert len(rigid) == comb(8, 3) == 56
            assert (0, 1, 2) in rigid
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
