"""Independent direct-matrix and local-symmetry checks for quarter-phase states.
Run: python3 verify_independent.py. No third-party packages.
"""
from itertools import permutations, product

FREE = tuple(x for x in range(16) if x not in (0, 1, 2, 4, 8))
REPRESENTATIVE = 389625


def unpack(code):
    phase = [0] * 16
    for x in FREE:
        phase[x] = code % 4
        code //= 4
    assert code == 0
    return phase


def canon(phase):
    common = phase[0]
    slopes = [(phase[1 << j] - common) % 4 for j in range(4)]
    adjusted = [
        (phase[x] - common - sum(slopes[j] for j in range(4) if x & (1 << j))) % 4
        for x in range(16)
    ]
    assert all(adjusted[x] == 0 for x in (0, 1, 2, 4, 8))
    return sum(adjusted[x] * 4 ** j for j, x in enumerate(FREE))


def purity_times_256(phase, other):
    left = (0, other)
    right = tuple(j for j in range(4) if j not in left)
    M = [[0j] * 4 for _ in range(4)]
    for a in range(4):
        for b in range(4):
            x = (((a >> 0) & 1) << left[0]) | (((a >> 1) & 1) << left[1])
            x |= (((b >> 0) & 1) << right[0]) | (((b >> 1) & 1) << right[1])
            M[a][b] = (1j) ** phase[x]
    G = [[sum(M[a][c] * M[b][c].conjugate() for c in range(4)) for b in range(4)] for a in range(4)]
    value = sum(abs(G[a][b]) ** 2 for a in range(4) for b in range(4))
    assert value == int(value)
    return int(value)


def one_qubit_coherence(phase, j):
    z = [(1j) ** v for v in phase]
    return sum(z[x] * z[x ^ (1 << j)].conjugate() for x in range(16) if not x & (1 << j))


def spinflip_tau_times_256(phase):
    z = [(1j) ** v for v in phase]
    t = sum((-1) ** (x.bit_count()) * z[x] * z[15 ^ x] for x in range(16))
    assert abs(t) ** 2 == int(abs(t) ** 2)
    return int(abs(t) ** 2)


def transformed(code, perm, flips, conjugate):
    f = unpack(code)
    h = []
    for y in range(16):
        x = flips
        for j in range(4):
            if (y >> j) & 1:
                x ^= 1 << perm[j]
        h.append(((-1 if conjugate else 1) * f[x]) % 4)
    return canon(h)


def main():
    f = unpack(REPRESENTATIVE)
    assert f == [0, 0, 0, 1, 0, 2, 3, 3, 0, 1, 0, 3, 3, 1, 1, 0]
    assert [purity_times_256(f, j) for j in range(1, 4)] == [88, 88, 88]
    orbit = {
        transformed(REPRESENTATIVE, perm, flips, conj)
        for perm in permutations(range(4))
        for flips in range(16)
        for conj in (0, 1)
    }
    assert len(orbit) == 96
    for m in orbit:
        state = unpack(m)
        assert [purity_times_256(state, j) for j in range(1, 4)] == [88, 88, 88]
        assert all(one_qubit_coherence(state, j) == 0 for j in range(4))
        assert spinflip_tau_times_256(state) == 16
    best_real = 300
    real_count = 0
    for digits in product((0, 2), repeat=11):
        state = [0] * 16
        for k, x in enumerate(FREE):
            state[x] = digits[k]
        maximum = max(purity_times_256(state, j) for j in range(1, 4))
        if maximum < best_real:
            best_real = maximum
            real_count = 0
        if maximum == best_real:
            real_count += 1
    assert (best_real, real_count) == (96, 272)
    print("CROSSCHECK_OK quarter_phase_witness=88/256 orbit=96 1_uniform=yes spinflip=1/16 real_min=96/256")


if __name__ == "__main__":
    main()
