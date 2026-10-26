"""Independent exhaustive finite algebra-generation checks over GF(4).

The field is F_2[t]/(t^2+t+1). A radical component with twist 0 has
right action by a, while twist 1 has right action by a^2. The square of
the radical is zero. Computations enumerate algebra closures, not the
matrix-rank formulas used in the theorem.
"""
from collections import Counter
from itertools import product


def field_mul(a, b):
    c0 = (a & 1) * (b & 1)
    c1 = ((a & 1) * ((b >> 1) & 1)) ^ (((a >> 1) & 1) * (b & 1))
    c2 = ((a >> 1) & 1) * ((b >> 1) & 1)
    return (c0 ^ c2) | ((c1 ^ c2) << 1)


def algebra_product(x, y, twists):
    a, b = x[0], y[0]
    return (field_mul(a, b),) + tuple(
        field_mul(a, y[j + 1]) ^ field_mul(x[j + 1], field_mul(b, b) if twist else b)
        for j, twist in enumerate(twists)
    )


def pack(v):
    return sum(c << (2 * j) for j, c in enumerate(v))


def unpack(v, length):
    return tuple((v >> (2 * j)) & 3 for j in range(length))


def insert(vec, basis):
    for pivot in sorted(basis, reverse=True):
        if (vec >> pivot) & 1:
            vec ^= basis[pivot]
    if vec == 0:
        return False
    basis[vec.bit_length() - 1] = vec
    return True


def belongs(vec, basis):
    for pivot in sorted(basis, reverse=True):
        if (vec >> pivot) & 1:
            vec ^= basis[pivot]
    return vec == 0


def generated_linear_basis(generators, twists):
    length = len(twists) + 1
    basis = {}
    for v in [pack((1,) + (0,) * len(twists))] + list(generators):
        insert(v, basis)
    while True:
        before = len(basis)
        vectors = list(basis.values())
        for x in vectors:
            for y in vectors:
                insert(pack(algebra_product(unpack(x, length), unpack(y, length), twists)), basis)
        if len(basis) == before:
            return basis


def all_tuples(twists, arity):
    vals = [pack(v) for v in product(range(4), repeat=len(twists) + 1)]
    return product(vals, repeat=arity), len(vals) ** arity


def check_generation(twists, arity, expected_count):
    tuples, total = all_tuples(twists, arity)
    full_dimension = 2 * (len(twists) + 1)
    count = sum(len(generated_linear_basis(gs, twists)) == full_dimension for gs in tuples)
    assert count == expected_count, (twists, arity, count, expected_count)
    print('full generation', twists, arity, count, '/', total)


def check_distinct_twists_profile():
    counts = Counter()
    tuples, _ = all_tuples((0, 1), 2)
    for gs in tuples:
        if all((g & 3) in (0, 1) for g in gs):
            continue
        basis = generated_linear_basis(gs, (0, 1))
        h0 = int(belongs(pack((0, 1, 0)), basis))
        h1 = int(belongs(pack((0, 0, 1)), basis))
        counts[(h0, h1)] += 1
    assert counts == {(0, 0): 48, (0, 1): 144, (1, 0): 720, (1, 1): 2160}
    print('distinct-twist conditional profile', sorted(counts.items()))


def check_repeated_twist_profile():
    counts = Counter()
    tuples, _ = all_tuples((1, 1), 2)
    for gs in tuples:
        if all((g & 3) in (0, 1) for g in gs):
            continue
        basis = generated_linear_basis(gs, (1, 1))
        size = sum(belongs(pack((0, x, y)), basis) for x in range(4) for y in range(4))
        assert size in (1, 4, 16)
        counts[{1: 0, 4: 1, 16: 2}[size]] += 1
    assert counts == {0: 192, 1: 2880}
    print('repeated-twist conditional ranks', sorted(counts.items()))


def main():
    for twists, arity, expected in [
        ((), 2, 12), ((0,), 2, 180), ((1,), 2, 144),
        ((0, 1), 2, 2160), ((1, 1), 2, 0), ((0, 0), 2, 2160),
        ((0, 1), 1, 0), ((1, 1), 1, 0),
    ]:
        check_generation(twists, arity, expected)
    check_distinct_twists_profile()
    check_repeated_twist_profile()
    print('PASS: all exhaustive finite checks')


if __name__ == '__main__':
    main()
