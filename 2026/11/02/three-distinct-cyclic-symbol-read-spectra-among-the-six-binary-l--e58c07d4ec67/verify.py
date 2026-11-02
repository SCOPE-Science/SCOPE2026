"""An independent-syndrome exact cyclic b-symbol enumerator for six length-31 Hamming codes."""
from collections import defaultdict
from pathlib import Path
import json


def multiply_x(v, polynomial, dimension):
    shifted = v * 2
    return shifted ^ (polynomial if shifted & (1 << dimension) else 0)


def primitive_polynomial(polynomial, dimension):
    orbit = []
    v = 1
    for _ in range((1 << dimension) - 1):
        if v in orbit:
            return False
        orbit.append(v)
        v = multiply_x(v, polynomial, dimension)
    return v == 1 and len(orbit) == (1 << dimension) - 1


def syndrome_enumerator(polynomial, dimension, block):
    length = (1 << dimension) - 1
    powers = [1]
    for _ in range(length - 1):
        powers.append(multiply_x(powers[-1], polynomial, dimension))
    result = [0] * (length + 1)
    for prefix_value in range(1 << (block - 1)):
        first = tuple((prefix_value >> j) & 1 for j in range(block - 1))
        syndrome = 0
        for j, bit in enumerate(first):
            if bit:
                syndrome ^= powers[j]
        states = {(syndrome, first, 0): 1}
        for i in range(block - 1, length):
            updated = defaultdict(int)
            for (old_syndrome, tail, weight), number in states.items():
                for next_bit in (0, 1):
                    new_syndrome = old_syndrome ^ (powers[i] if next_bit else 0)
                    new_tail = tail[1:] + (next_bit,)
                    new_weight = weight + (1 if next_bit or any(tail) else 0)
                    updated[(new_syndrome, new_tail, new_weight)] += number
            states = updated
        for (end_syndrome, tail, partial), number in states.items():
            if end_syndrome:
                continue
            boundary = tail + first
            wrap = sum(1 for j in range(block - 1) if any(boundary[j:j + block]))
            result[partial + wrap] += number
    return result


def main():
    data = json.loads(Path(__file__).with_name('spectra.json').read_text(encoding='utf-8'))
    expected_polys = (0x25, 0x29, 0x2f, 0x37, 0x3b, 0x3d)
    all_polys = tuple(p for p in range(33, 64, 2) if primitive_polynomial(p, 5))
    assert all_polys == expected_polys, (all_polys, expected_polys)
    assert set(data['profiles']) == {hex(p) for p in expected_polys}
    for poly in expected_polys:
        for block in (2, 3, 4):
            actual = syndrome_enumerator(poly, 5, block)
            assert actual == data['profiles'][hex(poly)][str(block)], (poly, block)
            assert sum(actual) == (1 << 26)
            assert actual[0] == 1
            assert len(actual) == 32
            assert sum(i * v for i, v in enumerate(actual)) == 31 * ((1 << 26) - (1 << (26 - block)))
    for block in (2, 3, 4):
        unique = {tuple(data['profiles'][hex(p)][str(block)]) for p in expected_polys}
        assert len(unique) == 3
        for left, right in ((0x25, 0x29), (0x2f, 0x3d), (0x37, 0x3b)):
            assert data['profiles'][hex(left)][str(block)] == data['profiles'][hex(right)][str(block)]
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
