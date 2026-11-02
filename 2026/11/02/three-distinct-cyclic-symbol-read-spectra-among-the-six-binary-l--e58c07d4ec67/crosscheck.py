"""Independent signed-character derivation of cyclic b-read enumerators."""
import json
from collections import defaultdict
from pathlib import Path


def xor_multiply_by_x(value, polynomial, degree):
    value <<= 1
    if value & (1 << degree):
        value ^= polynomial
    return value


def character_enumerator(poly, degree, block):
    length = (1 << degree) - 1
    columns = [1]
    for _ in range(1, length):
        columns.append(xor_multiply_by_x(columns[-1], poly, degree))
    total = [0] * (length + 1)
    for mask in range(1 << degree):
        subtotal = [0] * (length + 1)
        for head in range(1 << (block - 1)):
            prefix = tuple((head >> j) & 1 for j in range(block - 1))
            sign = 1
            for j, bit in enumerate(prefix):
                if bit and ((mask & columns[j]).bit_count() & 1):
                    sign = -sign
            # A signed-character transfer requires only the trailing b-1 coordinates.
            states = {(prefix, 0): sign}
            for j in range(block - 1, length):
                new_states = defaultdict(int)
                char_one = -1 if ((mask & columns[j]).bit_count() & 1) else 1
                for (tail, weight), number in states.items():
                    for bit in (0, 1):
                        new_weight = weight + int(bit or any(tail))
                        new_tail = tail[1:] + (bit,)
                        new_states[(new_tail, new_weight)] += number * (char_one if bit else 1)
                states = new_states
            for (tail, weight), number in states.items():
                suffix_and_prefix = tail + prefix
                wrapping = sum(any(suffix_and_prefix[k:k+block]) for k in range(block - 1))
                subtotal[weight + wrapping] += number
        for weight, count in enumerate(subtotal):
            total[weight] += count
    assert all(v % (1 << degree) == 0 for v in total), 'character divisibility error'
    return [v // (1 << degree) for v in total]


def independently_enumerate_small(degree, poly, block):
    length = (1 << degree) - 1
    columns = [1]
    for _ in range(1, length):
        columns.append(xor_multiply_by_x(columns[-1], poly, degree))
    histogram = [0] * (length + 1)
    for word in range(1 << length):
        syndrome = 0
        for i, h in enumerate(columns):
            if (word >> i) & 1:
                syndrome ^= h
        if syndrome:
            continue
        weight = 0
        for j in range(length):
            if any((word >> ((j + k) % length)) & 1 for k in range(block)):
                weight += 1
        histogram[weight] += 1
    return histogram


def main():
    data = json.loads((Path(__file__).with_name('spectra.json')).read_text(encoding='utf-8'))
    for poly_hex, spectrum in data['profiles'].items():
        poly = int(poly_hex, 16)
        for block_text, array in spectrum.items():
            block = int(block_text)
            actual = character_enumerator(poly, 5, block)
            assert actual == array, (poly_hex, block)
    # Direct complete binary-word enumeration, distinct from both transfer methods.
    for degree, polys in ((3, [0x0b, 0x0d]), (4, [0x13, 0x19])):
        for poly in polys:
            for block in (2, 3, 4):
                assert independently_enumerate_small(degree, poly, block) == character_enumerator(poly, degree, block)
    print('CROSSCHECK_OK')


if __name__ == '__main__':
    main()
