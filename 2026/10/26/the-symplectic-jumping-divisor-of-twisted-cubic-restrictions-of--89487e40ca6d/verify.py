"""Exact rational linear-algebra spot checks for the rank-nine bundle's twisted-cubic restrictions.
The universal statements are proved geometrically in RESULT.md; finite checks are not a proof.
Requires only the Python 3 standard library.
"""
from fractions import Fraction
from itertools import combinations

# Coordinates x,y,z,t,u,v. Signed (index+1), 0 denoting a zero linear form.
N = [
 [2,3,4,5,6,0,0,0,0,0,0,0,0,0],
 [-1,0,0,0,0,3,4,5,6,0,0,0,0,0],
 [4,-1,0,0,0,-2,0,0,0,5,6,0,0,4],
 [-3,0,-1,0,0,0,-2,0,0,0,0,5,6,-3],
 [0,0,0,-1,0,0,0,-2,0,-3,0,-4,0,6],
 [0,0,0,0,-1,0,0,0,-2,0,-3,0,-4,-5],
]


def rank(rows):
    m = [[Fraction(x) for x in row] for row in rows]
    h, w, piv = len(m), len(m[0]), 0
    for j in range(w):
        i = next((k for k in range(piv, h) if m[k][j]), None)
        if i is None:
            continue
        m[piv], m[i] = m[i], m[piv]
        q = m[piv][j]
        m[piv] = [v / q for v in m[piv]]
        for k in range(piv + 1, h):
            if m[k][j]:
                q = m[k][j]
                m[k] = [v - q * b for v, b in zip(m[k], m[piv])]
        piv += 1
        if piv == h:
            break
    return piv


def coefficient_matrix(P, m):
    """Map H0(O(m))^14 -> H0(O(m+3))^6 on a parametrized cubic."""
    a = [[0] * (14 * (m + 1)) for _ in range(6 * (m + 4))]
    for i in range(6):
        for j in range(14):
            v = N[i][j]
            if v:
                sg, idx = (1 if v > 0 else -1), abs(v) - 1
                for k in range(4):
                    for q in range(m + 1):
                        a[i * (m + 4) + k + q][j * (m + 1) + q] += sg * P[idx][k]
    return a


def cubic_coordinates(ind):
    a = [[0] * 4 for _ in range(6)]
    for j, i in enumerate(ind):
        a[i][j] = 1
    return a


def verify():
    # Every N column is a Koszul section: (x,y,z,t,u,v) * N = 0.
    for j in range(14):
        coef = {}
        for i in range(6):
            v = N[i][j]
            if v:
                key = tuple(sorted((i, abs(v) - 1)))
                coef[key] = coef.get(key, 0) + (1 if v > 0 else -1)
        assert all(v == 0 for v in coef.values())
    # The missing three basis Koszul sections have coefficients (1,-1,1)
    # under the functional defining the hyperplane W.
    symp_pairs = {(0, 1), (2, 3), (4, 5)}
    observed = {"generic": 0, "isotropic": 0}
    for I in combinations(range(6), 4):
        P = cubic_coordinates(I)
        h0 = 14 - rank(coefficient_matrix(P, 0))
        h1 = 28 - rank(coefficient_matrix(P, 1))
        J = tuple(i for i in range(6) if i not in I)
        isotropic = J not in symp_pairs
        assert h0 == int(isotropic), (I, h0)
        assert h1 == 6, (I, h1)
        observed['isotropic' if isotropic else 'generic'] += 1
    assert observed == {'generic': 3, 'isotropic': 12}
    print('Euler-Koszul identities verified for 14 columns.')
    print('All 15 coordinate four-planes: 3 nonisotropic / 12 isotropic;')
    print('h^0(E|C(-3)) = 0 / 1 and h^0(E|C(-2)) = 6 in every case.')
    print('The geometric proof, not this finite enumeration, covers all cubic curves.')


if __name__ == '__main__':
    verify()
