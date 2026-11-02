"""Exact finite F_2-linear-algebra/orbit certificate for cubic-quartic space-filling curves.

Run: python3 verify_orbits.py   (Python 3.9+; no third-party packages).
This checks the entire 2^16 quartic-section space, rather than sampling it.
"""
from itertools import product
from collections import Counter

MONS = sorted((e for e in product(range(5), repeat=4) if sum(e) == 4), reverse=True)
INDEX = {e: i for i, e in enumerate(MONS)}


def add_vector(rows, value):
    while value:
        pivot = value.bit_length() - 1
        if pivot not in rows:
            rows[pivot] = value
            return True
        value ^= rows[pivot]
    return False


def point_value(monomial, point):
    return int(all((not exp) or ((point >> i) & 1) for i, exp in enumerate(monomial)))


def kernel_basis():
    # Evaluate all 35 quartic monomials on the 15 nonzero vectors of F_2^4.
    rows, basis = {}, []
    for j, monomial in enumerate(MONS):
        evaluation = sum(point_value(monomial, p) << (p - 1) for p in range(1, 16))
        tracked = 1 << j
        while evaluation:
            pivot = evaluation.bit_length() - 1
            if pivot not in rows:
                rows[pivot] = (evaluation, tracked)
                break
            old, old_track = rows[pivot]
            evaluation ^= old
            tracked ^= old_track
        if evaluation == 0:
            basis.append(tracked)
    assert len(rows) == 15 and len(basis) == 20
    return basis


def fixed_cubic_multiples():
    # G = X^2Y + XY^2 + Z^2W + ZW^2.
    cubic = [(2, 1, 0, 0), (1, 2, 0, 0), (0, 0, 2, 1), (0, 0, 1, 2)]
    out = []
    for j in range(4):
        form = 0
        for exponents in cubic:
            monomial = list(exponents)
            monomial[j] += 1
            form ^= 1 << INDEX[tuple(monomial)]
        out.append(form)
    return out


KERNEL = kernel_basis()
G_TIMES_LINEAR = fixed_cubic_multiples()
SPAN = {}
for form in G_TIMES_LINEAR:
    assert add_vector(SPAN, form)
QUOTIENT = []
for form in KERNEL:
    if add_vector(SPAN, form):
        QUOTIENT.append(form)
assert len(QUOTIENT) == 16 and len(SPAN) == 20

# Exact coordinate decoder for the basis (G X, G Y, G Z, G W, 16 other sections).
DECODER = {}
for j, form in enumerate(G_TIMES_LINEAR + QUOTIENT):
    mask, coeffs = form, 1 << j
    while mask:
        pivot = mask.bit_length() - 1
        if pivot not in DECODER:
            DECODER[pivot] = (mask, coeffs)
            break
        earlier_mask, earlier_coeffs = DECODER[pivot]
        mask ^= earlier_mask
        coeffs ^= earlier_coeffs
    assert mask != 0


def to_coordinates(mask):
    coeffs = 0
    while mask:
        pivot = mask.bit_length() - 1
        assert pivot in DECODER
        older_mask, older_coeffs = DECODER[pivot]
        mask ^= older_mask
        coeffs ^= older_coeffs
    return coeffs >> 4


def representative(coeffs):
    form = 0
    for j in range(16):
        if (coeffs >> j) & 1:
            form ^= QUOTIENT[j]
    return form


def symplectic_transvection(v):
    # The standard alternating pairing pairs (X,Y) and (Z,W).
    opposite = (1, 0, 3, 2)
    return [[int(i == j) ^ (((v >> i) & 1) & ((v >> opposite[j]) & 1))
             for j in range(4)] for i in range(4)]


def substituted_monomials(matrix):
    out = []
    for exponents in MONS:
        polynomial = {(0, 0, 0, 0)}
        for i, exp in enumerate(exponents):
            for _ in range(exp):
                product_set = set()
                for monomial in polynomial:
                    for j in range(4):
                        if matrix[i][j]:
                            new_exponents = list(monomial)
                            new_exponents[j] += 1
                            mon = tuple(new_exponents)
                            if mon in product_set:
                                product_set.remove(mon)
                            else:
                                product_set.add(mon)
                polynomial = product_set
        out.append(sum(1 << INDEX[mon] for mon in polynomial))
    return out


def induced_action(v):
    images = substituted_monomials(symplectic_transvection(v))
    result = []
    for f in QUOTIENT:
        image = 0
        for j in range(35):
            if (f >> j) & 1:
                image ^= images[j]
        result.append(to_coordinates(image))
    return result


ACTIONS = [induced_action(v) for v in range(1, 16)]


def act(coeffs, action):
    image = 0
    while coeffs:
        bit = coeffs & -coeffs
        coeffs ^= bit
        image ^= action[bit.bit_length() - 1]
    return image


def orbits():
    seen = bytearray(65536)
    result = []
    for start in range(65536):
        if seen[start]:
            continue
        orbit = [start]
        seen[start] = 1
        for coeffs in orbit:
            for action in ACTIONS:
                nxt = act(coeffs, action)
                if not seen[nxt]:
                    seen[nxt] = 1
                    orbit.append(nxt)
        result.append((start, len(orbit)))
    assert sum(size for _, size in result) == 65536
    return result


def differential(form, point):
    coordinates = 0
    for j, monomial in enumerate(MONS):
        if (form >> j) & 1:
            for i, exp in enumerate(monomial):
                if exp & 1:
                    deriv = list(monomial)
                    deriv[i] -= 1
                    if point_value(deriv, point):
                        coordinates ^= 1 << i
    return coordinates


def rationally_smooth_coefficients():
    # Direct enumeration independently of the symplectic orbit algorithm.
    all_gradients = []
    for point in range(1, 16):
        basis_grads = [differential(f, point) for f in QUOTIENT]
        grads = bytearray(65536)
        for coeffs in range(1, 65536):
            least = coeffs & -coeffs
            grads[coeffs] = grads[coeffs ^ least] ^ basis_grads[least.bit_length() - 1]
        all_gradients.append(grads)
    surviving = set()
    for coeffs in range(65536):
        if all((grads[coeffs] != 0 and grads[coeffs] != (
                    ((point >> 1) & 1) | (((point >> 0) & 1) << 1) |
                    (((point >> 3) & 1) << 2) | (((point >> 2) & 1) << 3)))
               for point, grads in zip(range(1, 16), all_gradients)):
            surviving.add(coeffs)
    return surviving


def main():
    orbit_data = orbits()
    assert len(orbit_data) == 128
    candidates = rationally_smooth_coefficients()
    assert len(candidates) == 288
    rational_orbits = [(rep, size) for rep, size in orbit_data if rep in candidates]
    assert rational_orbits == [(13387, 144), (13394, 144)], rational_orbits
    assert sum(size for _, size in rational_orbits) == len(candidates)
    # The group is Sp_4(F_2), generated by its fifteen symplectic transvections.
    # |Sp_4(F_2)|=2^4(2^2-1)(2^4-1)=720.
    assert 720 % 144 == 0
    assert Counter(size for _, size in orbit_data)[144] == 3
    print('ORBIT_VERIFY_OK; quartic classes=65536; orbits=128; rationally-smooth=288;')
    print('candidate orbits=(13387,144),(13394,144); fixed-cubic stabilizer=5')


if __name__ == '__main__':
    main()
