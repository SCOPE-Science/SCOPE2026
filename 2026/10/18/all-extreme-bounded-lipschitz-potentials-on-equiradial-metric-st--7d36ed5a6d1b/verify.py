"""Reproducibility checks for the equiradial star bounded-Lipschitz ball.

Run: python verify.py
Standard library suffices for exact tests. Optional numpy/scipy add independent LP and hull tests.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import prod


def predicted_vertices(m, rho):
    a = rho / (rho + 2)
    b = rho / (rho + 1)
    ret = {tuple([F(1)] * (m + 1)), tuple([F(-1)] * (m + 1))}
    for s in product((-1, 1), repeat=m + 1):
        if any(s[i] != s[0] for i in range(1, m + 1)):
            ret.add(tuple(a * u for u in s))
    for s in product((-1, 1), repeat=m):
        if min(s) < max(s):
            ret.add((F(0),) + tuple(b * u for u in s))
    assert len(ret) == 3 * 2**m - 2
    return ret


def direct_halfspaces(m, rho):
    d = m + 1
    rows = set()
    for v in range(d):
        for i in range(1, d):
            for sa, sb in product((-1, 1), repeat=2):
                row = [F(0)] * d
                row[v] += sa
                row[i] += F(sb) / rho
                row[0] -= F(sb) / rho
                rows.add(tuple(row))
    return sorted(rows)


def unique_solve(rows):
    """Solve A x = 1 over rationals, returning None if singular."""
    d = len(rows)
    z = [list(row) + [F(1)] for row in rows]
    for col in range(d):
        pivot = next((k for k in range(col, d) if z[k][col]), None)
        if pivot is None:
            return None
        z[col], z[pivot] = z[pivot], z[col]
        p = z[col][col]
        z[col] = [v / p for v in z[col]]
        for k in range(d):
            if k == col or not z[k][col]:
                continue
            p = z[k][col]
            z[k] = [u - p * v for u, v in zip(z[k], z[col])]
    return tuple(z[i][-1] for i in range(d))


def enumerated_vertices(m, rho):
    # Exhaustive vertex enumeration is used only in low dimensions.
    H = direct_halfspaces(m, rho)
    vertices = set()
    for active in combinations(H, m + 1):
        v = unique_solve(active)
        if v is not None and all(sum(a*b for a,b in zip(row,v)) <= 1 for row in H):
            vertices.add(v)
    return vertices


def mixed_sign_max(a):
    total = sum(abs(z) for z in a)
    if all(z > 0 for z in a) or all(z < 0 for z in a):
        return total - 2 * min(abs(z) for z in a)
    return total


def norm_formula(mu, rho):
    a = rho/(rho + 2)
    b = rho/(rho + 1)
    return max(abs(sum(mu)), a*mixed_sign_max(mu), b*mixed_sign_max(mu[1:]))


def run_exact():
    count = 0
    for m, rho in [(1,F(1)), (2,F(1,2)), (2,F(1)), (2,F(3,2)), (3,F(1))]:
        exp = predicted_vertices(m,rho)
        got = enumerated_vertices(m,rho)
        assert got == exp, (m,rho,len(got),len(exp),got ^ exp)
        count += 1
    for m in range(2,6):
        for rho in (F(1,3),F(1),F(5,2)):
            vertices = predicted_vertices(m,rho)
            assert len(vertices) == 3*2**m-2
            for mu in product(range(-2,3),repeat=min(m+1,3)):
                mu = tuple(F(z) for z in mu) + (F(0),)*(m+1-min(m+1,3))
                direct = max(sum(a*b for a,b in zip(mu,v)) for v in vertices)
                assert direct == norm_formula(mu,rho), (m,rho,mu,direct,norm_formula(mu,rho))
                count += 1
    return count


def run_optional_lp():
    try:
        import numpy as np
        from scipy.optimize import linprog
        from scipy.spatial import HalfspaceIntersection
    except ImportError:
        return 'not installed'
    num=0
    for m in range(2,8):
        for rho in (F(1,4),F(1),F(7,2)):
            H = direct_halfspaces(m,rho)
            A=np.array([[float(a) for a in row] for row in H])
            hs=np.c_[A,-np.ones(len(H))]
            got=np.unique(np.round(HalfspaceIntersection(hs,np.zeros(m+1)).intersections,8),axis=0)
            pred=predicted_vertices(m,rho)
            assert len(got)==len(pred), (m,rho,len(got),len(pred))
            for v in got:
                assert min(np.max(np.abs(v-np.array([float(z) for z in w]))) for w in pred)<2e-7
            # Independently count facets from equality-face affine ranks.
            face_count = 0
            for h in H:
                coeff = np.array([float(z) for z in h])
                active = np.flatnonzero(np.abs(got @ coeff - 1) < 2e-7)
                if len(active) >= m + 1 and np.linalg.matrix_rank(got[active] - got[active[0]], tol=1e-7) == m:
                    face_count += 1
            assert face_count == 2*m*(m+1), (m, rho, face_count)
            for k in range(16):
                mu=np.array([((7*k+11*j*j+3*j+5*m)%23)-11 for j in range(m+1)])
                res=linprog(-mu,A_ub=A,b_ub=np.ones(len(H)),bounds=[(None,None)]*(m+1),method='highs')
                assert res.success and abs(-res.fun-float(norm_formula(list(map(F,mu)),rho)))<1e-7
                num += 1
    return num


if __name__ == '__main__':
    exact=run_exact()
    optional=run_optional_lp()
    print('PASS: 5 exact rational full-hull enumerations; exact dual comparisons:', exact-5)
    print('PASS: optional SciPy hull/LP comparisons:',optional)
