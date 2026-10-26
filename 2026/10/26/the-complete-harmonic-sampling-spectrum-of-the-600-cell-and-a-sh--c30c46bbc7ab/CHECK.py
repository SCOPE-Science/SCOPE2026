"""Exact McKay recurrence and independent 600-cell Gram diagonalization."""
import itertools
import math
import numpy as np

D = [1, 2, 3, 4, 5, 6, 4, 2, 3]
EDGES = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (5, 8)]
A = [[0] * 9 for _ in range(9)]
for i, j in EDGES:
    A[i][j] = A[j][i] = 1
assert sum(t*t for t in D) == 120
assert all(sum(A[i][j]*D[j] for j in range(9)) == 2*D[i] for i in range(9))

m = [[1] + [0]*8, [0, 1] + [0]*7]
for ell in range(2, 242):
    m.append([sum(A[i][j] * m[-1][j] for j in range(9)) - m[-2][i]
              for i in range(9)])
for ell, vec in enumerate(m):
    assert all(v >= 0 and (v == 0 if (ell-j)%2 else True) for j,v in enumerate(vec))
    assert sum(v*D[j] for j,v in enumerate(vec)) == ell+1
for ell in range(180):
    assert all(m[ell+60][j] == m[ell][j] + (D[j] if (ell-j)%2 == 0 else 0)
               for j in range(9))
rank = lambda ell: sum(D[j]**2 for j in range(9) if m[ell][j] > 0)
assert [rank(x) for x in (0,1,13,20,28,29,46,58,59,60,61)] == [1,4,60,60,59,60,59,59,60,60,60]
assert all(rank(ell) == 60 for ell in range(59, 242))
assert m[58] == [0,0,3,0,5,0,4,0,3]
assert m[59] == [0,2,0,4,0,6,0,2,0]
assert all(m[29][j] == (D[j]//2 if j%2 else 0) for j in range(9))

phi = (1 + math.sqrt(5)) / 2
points = []
for axis in range(4):
    for sign in (-1,1):
        x = [0.]*4
        x[axis] = float(sign)
        points.append(x)
for signs in itertools.product((-1,1), repeat=4):
    points.append([s/2 for s in signs])
for perm in itertools.permutations(range(4)):
    inversions = sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))
    if inversions%2:
        continue
    for signs in itertools.product((-1,1),repeat=3):
        base = [0., 0.5, phi/2, 1/(2*phi)]
        row = [base[i] for i in perm]
        sign_iter = iter(signs)
        points.append([v*next(sign_iter) if v else 0. for v in row])
X = np.array(points)
assert X.shape == (120,4)
assert np.max(np.abs(np.sum(X*X,axis=1)-1)) < 1e-13
T = np.clip(X @ X.T, -1., 1.)
U0 = np.ones_like(T)
U1 = 2*T
max_error = 0.
sampled = [0,1,2,3,4,8,12,13,14,19,20,21,28,29,30,46,58,59,60]
for ell in range(max(sampled)+1):
    if ell == 0:
        U = U0
    elif ell == 1:
        U = U1
    else:
        U0,U1 = U1,2*T*U1-U0
        U = U1
    if ell not in sampled:
        continue
    eig = np.linalg.eigvalsh(U/(ell+1))
    target = sorted([120*m[ell][j]/((ell+1)*D[j]) for j in range(9) for _ in range(D[j]**2)])
    err = np.max(np.abs(eig - np.array(target)))
    max_error = max(max_error,err)
    assert err < 1e-9, (ell,err)
print('Graph dimensions, integer decompositions, and sixty-step recurrence: PASS')
print('Rank at degree 58: 59; rank at 59: 60; all degrees 59..241: 60')
print('Tight multiplicity at degrees 29 and 59: PASS')
print('Direct 120-vertex Gram spectra matched at', len(sampled), 'degrees')
print('Maximum eigenvalue discrepancy: %.3g' % max_error)
print('PASS')
