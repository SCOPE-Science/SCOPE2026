"""Exact integer-lattice checks for a cyclic bispectrum support theorem.

Requires Python 3.10+ and SymPy 1.12+. Run: python check.py
A finite check corroborates, but does not replace, the all-order proof.
"""
from itertools import product
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form


def phase_group(n, r):
    assert r >= 3 and n > 2 * r
    # Distinct signed integer frequency representatives; no aliasing.
    S = list(range(-r, -1)) + list(range(2, r + 1))
    indices = {k % n: i for i, k in enumerate(S)}
    rows = []
    for a, b in product(S, repeat=2):
        c_index = indices.get((a + b) % n)
        if c_index is None:
            continue
        row = [0] * len(S)
        row[indices[a % n]] += 1
        row[indices[b % n]] += 1
        row[c_index] -= 1
        if any(row):
            rows.append(row)
    A = Matrix(rows) if rows else Matrix.zeros(0, len(S))
    diag = smith_normal_form(A, domain=ZZ)
    factors = [abs(int(diag[i, i])) for i in range(min(diag.rows, diag.cols))
               if diag[i, i]]
    return (len(S) - len(factors), tuple(x for x in factors if x > 1))


def expected(n, r):
    if r >= 6:
        return (0, (n,)) if n <= 3*r else (1, ())
    if r == 5:
        if n <= 13:
            return (0, (n,))
        if n == 14:
            return (1, (2,))
        if n == 15:
            return (1, (3,))
        return (2, ())
    if r == 4:
        if n in (9, 10):
            return (0, (n,))
        if n == 11:
            return (1, ())
        if n == 12:
            return (2, (6,))
        return (3, ())
    if n in (7, 8):
        return (1, ())
    if n == 9:
        return (2, (3,))
    return (4, ())


def representative_relations(n, r):
    S = list(range(-r, -1)) + list(range(2, r + 1))
    out = []
    for a, b, c in product(S, repeat=3):
        if (a + b - c) % n == 0:
            out.append((a, b, c))
    return out


def main():
    checks = 0
    # Exhaustively enumerates ALL bispectral phase relations within each case.
    for r in range(3, 12):
        samples = (range(2*r+1, 3*r+8) if r <= 6
                   else (2*r+1, 2*r+2, (5*r)//2, 3*r, 3*r+1, 4*r+2))
        for n in samples:
            obtained = phase_group(n, r)
            target = expected(n, r)
            assert obtained == target, (n, r, obtained, target)
            checks += 1
    # Complete small-band wrap cases for the human-readable proof.
    for r in (3, 4, 5):
        for n in range(2*r+1, 3*r+1):
            rels = representative_relations(n, r)
            assert rels
            assert phase_group(n, r) == expected(n, r)
    # For r>=6, continuous-phase generators u(k)=z^k meet all
    # modular triple constraints exactly when no triple wraps.
    for r in range(6, 23):
        for n in (2*r+1, 3*r, 3*r+1, 4*r+2):
            S = list(range(-r, -1)) + list(range(2, r+1))
            defects = {a+b-c for a,b,c in representative_relations(n,r)}
            assert defects <= {0, n, -n}
            assert ((n in defects or -n in defects) == (n <= 3*r))
    print('PASS:', checks, 'exact Smith-form phase-group comparisons;')
    print('PASS: all small-band wrap cases and 68 analytic wrap witnesses.')

if __name__ == '__main__':
    main()
