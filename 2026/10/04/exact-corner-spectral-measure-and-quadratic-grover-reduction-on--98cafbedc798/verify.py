#!/usr/bin/env python3
from fractions import Fraction
from math import comb


def matvec(A, v):
    return [sum(A[i][j] * v[j] for j in range(len(v))) for i in range(len(A))]


def check_equal(u, v, label):
    if u != v:
        raise AssertionError(f"{label}: {u!r} != {v!r}")


def base_matrix(p):
    return [
        [Fraction(1), Fraction(-1), Fraction(0), Fraction(0)],
        [p - 1, Fraction(1), -p, Fraction(0)],
        [Fraction(0), -p, Fraction(1), p - 1],
        [Fraction(0), Fraction(0), Fraction(-1), Fraction(1)],
    ]


def base_spectral_data(p):
    # Eigenpairs of the source four-state probabilistic Laplacian.
    eig = [
        (Fraction(0), [1, 1, 1, 1]),
        (p, [-1, p - 1, 1 - p, 1]),
        (2 - p, [1, p - 1, p - 1, 1]),
        (Fraction(2), [-1, 1, -1, 1]),
    ]
    mu = [Fraction(1), 1 / (1 - p), 1 / (1 - p), Fraction(1)]
    weights = []
    A = base_matrix(p)
    for lam, f in eig:
        f = [Fraction(x) for x in f]
        check_equal(matvec(A, f), [lam * x for x in f], f"eigenpair lambda={lam}")
        norm2 = sum(mu[i] * f[i] * f[i] for i in range(4))
        weights.append(f[0] * f[0] / norm2)
    return [x[0] for x in eig], weights


def convolve_atoms(atoms, d):
    # Spectral measure of the normalized d-fold Kronecker sum at the corner.
    dist = {Fraction(0): Fraction(1)}
    for _ in range(d):
        nxt = {}
        for s, ws in dist.items():
            for x, wx in atoms:
                y = s + x
                nxt[y] = nxt.get(y, Fraction(0)) + ws * wx
        dist = nxt
    return {s / d: w for s, w in dist.items()}


def direct_ST_distribution(p, d):
    a = (1 - p) / (2 * (2 - p))
    b = 1 / (2 * (2 - p))
    # Single-coordinate sign-pair law: same signs have weight a, opposite signs b.
    dist = {(0, 0): Fraction(1)}
    for _ in range(d):
        nxt = {}
        for (S, T), w in dist.items():
            for ds, dt, q in [(-1, -1, a), (1, -1, b), (-1, 1, b), (1, 1, a)]:
                key = (S + ds, T + dt)
                nxt[key] = nxt.get(key, Fraction(0)) + w * q
        dist = nxt
    atoms = {}
    for (S, T), w in dist.items():
        lam = 1 + (p * S + (2 - p) * T) / (2 * d)
        atoms[lam] = atoms.get(lam, Fraction(0)) + w
    return dist, atoms


def moments(dist):
    mean = sum(x * w for x, w in dist.items())
    var = sum((x - mean) * (x - mean) * w for x, w in dist.items())
    return mean, var


def verify_case(p, max_d=6):
    eigenvalues, weights = base_spectral_data(p)
    a = (1 - p) / (2 * (2 - p))
    b = 1 / (2 * (2 - p))
    check_equal(weights, [a, b, b, a], f"corner weights p={p}")
    check_equal(sum(weights), Fraction(1), f"weight sum p={p}")
    atoms = list(zip(eigenvalues, weights))
    for d in range(1, max_d + 1):
        conv = convolve_atoms(atoms, d)
        st, st_atoms = direct_ST_distribution(p, d)
        check_equal(conv, st_atoms, f"product law p={p}, d={d}")
        check_equal(sum(conv.values()), Fraction(1), f"mass p={p}, d={d}")
        mean, var = moments(conv)
        check_equal(mean, Fraction(1), f"mean p={p}, d={d}")
        check_equal(var, (1 - p) / d, f"variance p={p}, d={d}")
        if len(conv) > (d + 1) ** 2:
            raise AssertionError("quadratic support bound failed")


def homogeneous_support_count(d):
    p = Fraction(1, 2)
    _, atoms = direct_ST_distribution(p, d)
    return len(atoms)


def main():
    for p in [Fraction(1, 10), Fraction(2, 5), Fraction(1, 2), Fraction(91, 100), Fraction(7, 13)]:
        verify_case(p)

    # Source's d=5 test parameters. Exact active dimensions are far below 4^5=1024.
    expected = {
        Fraction(91, 100): 36,
        Fraction(1, 2): 21,
        Fraction(2, 5): 26,
        Fraction(1, 10): 36,
    }
    for p, target in expected.items():
        _, atoms = direct_ST_distribution(p, 5)
        check_equal(len(atoms), target, f"d=5 support count p={p}")

    # For p=1/2, d>=2, support is exactly {0,1,...,4d}/(2d), hence 4d+1 atoms.
    for d in range(2, 9):
        check_equal(homogeneous_support_count(d), 4 * d + 1, f"homogeneous count d={d}")

    # The zero atom has weight a^d = 1/vol(G_d), matching the squared corner overlap
    # of the normalized constant ground state.
    for p in [Fraction(1, 10), Fraction(2, 5), Fraction(1, 2), Fraction(91, 100)]:
        a = (1 - p) / (2 * (2 - p))
        base_vol = 2 + 2 / (1 - p)
        check_equal(a, 1 / base_vol, f"base zero weight p={p}")
        for d in [1, 2, 5]:
            _, atoms = direct_ST_distribution(p, d)
            check_equal(atoms[Fraction(0)], a ** d, f"zero weight p={p}, d={d}")

    print("VERIFY_OK")


if __name__ == "__main__":
    main()
