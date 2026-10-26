"""Independent finite-size checks of toroidal modular Laplacian extinction.

Only Python's standard library is required.  Run: python3 artifacts/verify.py
"""
from itertools import product


def is_prime(p):
    return p >= 2 and all(p % k for k in range(2, int(p ** .5) + 1))


def step(grid, p, na, nb):
    """Direct cell-by-cell simultaneous stencil, periodic with multiplicities."""
    result = [[0] * nb for _ in range(na)]
    for i in range(na):
        for j in range(nb):
            result[i][j] = (
                grid[(i - 1) % na][j] + grid[(i + 1) % na][j]
                + grid[i][(j - 1) % nb] + grid[i][(j + 1) % nb]
                - 4 * grid[i][j]
            ) % p
    return result


def theorem_time(p, a, b):
    assert is_prime(p) and a >= b >= 1
    return 2 ** (a - 1) if p == 2 else (p ** a + p ** b) // 2


def test_case(p, a, b):
    na, nb = p ** a, p ** b
    period = theorem_time(p, a, b)
    grid = [[0] * nb for _ in range(na)]
    grid[0][0] = 1
    for t in range(period):
        assert any(any(row) for row in grid), (p, a, b, t, "premature extinction")
        if t == period - 1 and p % 2:
            c = (-1 if (b * (p - 1) // 2) % 2 else 1) % p
            assert all(value == c for row in grid for value in row), (
                p, a, b, "last nonzero iterate is not rank-one constant"
            )
        grid = step(grid, p, na, nb)
    assert not any(any(row) for row in grid), (p, a, b, "not extinct")

    if p % 2 and na * nb <= 30:
        # Verify linearity of last step for several nontrivial initial arrays:
        # direct iterates must be c times the total initial mass.
        for z in (0, 1, 2, 3):
            sample = [[(17*i + 5*j + z*i*j + 3*z) % p for j in range(nb)]
                      for i in range(na)]
            mass = sum(map(sum, sample)) % p
            c = ((-1 if (b * (p - 1) // 2) % 2 else 1) * mass) % p
            for _ in range(period - 1):
                sample = step(sample, p, na, nb)
            assert all(value == c for row in sample for value in row), (p, a, b, z)


def main():
    cases = [
        (2,1,1),(2,2,1),(2,2,2),(2,3,1),(2,3,2),(2,3,3),
        (2,4,1),(2,4,2),(2,4,4),
        (3,1,1),(3,2,1),(3,2,2),(3,3,1),(3,3,2),
        (5,1,1),(5,2,1),(5,2,2),(7,1,1),(11,1,1),
    ]
    for p,a,b in cases:
        test_case(p,a,b)
    print(f"VERIFY_OK cases={len(cases)} direct_stencil=passed last_nonzero=passed")

if __name__ == '__main__':
    main()
