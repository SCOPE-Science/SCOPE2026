from fractions import Fraction

N = 4


def h_one_excitation(v):
    """Exact one-excitation action of the four-site periodic Heisenberg Hamiltonian."""
    return tuple(2 * (v[(j - 1) % N] + v[(j + 1) % N]) for j in range(N))


def norm2_gaussian(v):
    return sum(int(round(z.real)) ** 2 + int(round(z.imag)) ** 2 for z in v)


def mw_q_from_one_excitation(v):
    total = norm2_gaussian(v)
    p = [Fraction(int(round(z.real)) ** 2 + int(round(z.imag)) ** 2, total) for z in v]
    return Fraction(1, 1) - sum(x * x for x in p)


phi_plus = (1 + 0j, 0 + 1j, -1 + 0j, 0 - 1j)
phi_minus = (1 + 0j, 0 - 1j, -1 + 0j, 0 + 1j)
standing = (1 + 0j, 0 + 0j, -1 + 0j, 0 + 0j)
zero = (0j, 0j, 0j, 0j)

assert h_one_excitation(phi_plus) == zero
assert h_one_excitation(phi_minus) == zero
assert h_one_excitation(standing) == zero

q_plane = mw_q_from_one_excitation(phi_plus)
q_standing = mw_q_from_one_excitation(standing)
q_source = Fraction(4 * 1 * (N - 1), N * N)

assert q_plane == Fraction(3, 4)
assert q_standing == Fraction(1, 2)
assert q_source == Fraction(3, 4)
assert q_standing != q_source

print(f"VERIFY_OK plane_Q={q_plane} standing_Q={q_standing} source_Q={q_source}")
