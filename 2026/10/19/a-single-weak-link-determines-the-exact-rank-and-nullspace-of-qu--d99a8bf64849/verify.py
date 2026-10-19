"""Reproducible checks for a one-bond quantum-ring average-mixing rank theorem.

Run: python verify.py (Python 3 with NumPy for independent spectral checks).
The exact moment witness is computed over fractions.Fraction.
"""
from fractions import Fraction


def h_action(v, g):
    n = len(v)
    out = []
    for j in range(n):
        left = v[(j - 1) % n] * (g if j == 0 else 1)
        right = v[(j + 1) % n] * (g if j == n - 1 else 1)
        out.append(left + right)
    return out


def moment_matrix(n, g):
    g = Fraction(g)
    q = (n + 1) // 2
    data = [[Fraction(0) for _ in range(q)] for __ in range(q)]
    for start in range(q):
        v = [Fraction(int(j == start)) for j in range(n)]
        data[start][0] = Fraction(1)
        for k in range(1, q):
            v = h_action(h_action(v, g), g)
            data[start][k] = v[start]
    return data


def exact_det(a):
    a = [row[:] for row in a]
    n = len(a)
    det = Fraction(1)
    for j in range(n):
        t = next((k for k in range(j, n) if a[k][j]), None)
        if t is None:
            return Fraction(0)
        if j != t:
            a[j], a[t] = a[t], a[j]
            det = -det
        pivot = a[j][j]
        det *= pivot
        for k in range(j + 1, n):
            f = a[k][j] / pivot
            for h in range(j + 1, n):
                a[k][h] -= f * a[j][h]
            a[k][j] = Fraction(0)
    return det


def exact_checks():
    count = 0
    for n in range(3, 26):
        q = (n + 1) // 2
        for g in [Fraction(0), Fraction(1, 3), Fraction(1, 2),
                  Fraction(4, 5), Fraction(1), Fraction(6, 5),
                  Fraction(2), Fraction(3)]:
            a = moment_matrix(n, g)
            # Identity triangularizes after subtracting central-binomial baseline.
            from math import comb
            for r in range(q):
                for k in range(q):
                    if r >= k:
                        assert a[r][k] == comb(2*k, k), (n, g, r, k)
                    if k == r + 1:
                        assert a[r][k] - comb(2*k,k) == g*g-1
            d = exact_det(a)
            want = (-1)**(q-1) * (g*g-1)**(q-1)
            assert d == want, (n, g, d, want)
            count += 1
    return count


def spectral_checks():
    import numpy as np
    spectral_count = 0
    entries = 0
    for n in range(3, 19):
        q = (n + 1) // 2
        for g in [0.0, 0.4, 0.8, 1.0, 1.25, 2.0, 3.5]:
            h = np.zeros((n,n), dtype=float)
            for j in range(n):
                k = (j+1)%n
                h[j,k] = h[k,j] = (g if j==n-1 else 1.0)
            lam, v = np.linalg.eigh(h)
            groups = []
            for k, val in enumerate(lam):
                if not groups or abs(val-lam[groups[-1][-1]])>1e-8:
                    groups.append([k])
                else:
                    groups[-1].append(k)
            if abs(g-1.0)>1e-12:
                assert len(groups)==n, (n,g,lam)
            m = np.zeros((n,n))
            for group in groups:
                p = v[:,group]@v[:,group].T
                m += p*p
            eig=np.linalg.eigvalsh(m)
            rank=sum(eig>1e-7)
            want= (n if n%2 else n//2) if g==1 else q
            assert rank==want, (n,g,rank,want,eig)
            assert abs(np.max(np.sum(m,axis=1)-1)) <1e-8
            if g!=1:
                # A defect-eigenspace has a unique reflection-parity sign.
                refl=np.arange(n-1,-1,-1)
                assert np.max(abs(m[refl,:]-m))<1e-8
                for j in range(n):
                    assert np.max(abs(m[:,j]-m[:,n-1-j]))<1e-8
            spectral_count += 1
            entries += n*n
    return spectral_count, entries

if __name__=='__main__':
    num=exact_checks()
    cnt,entries=spectral_checks()
    print(f'VERIFY_OK exact_moment_profiles={num} independent_spectral_profiles={cnt} spectral_entries={entries} orders=3..25')
