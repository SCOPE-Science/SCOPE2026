"""Exact rational checks of a proposed Euclidean embedding theorem for hub-and-clique metrics.

No numerical solver and no external packages are required. This verifies finite instances;
the mathematical proof for arbitrary parameters is separate.
"""
from fractions import Fraction as F
from itertools import product


def rank_rational(a):
    a = [list(row) for row in a]
    if not a:
        return 0
    rows, cols, rank = len(a), len(a[0]), 0
    for c in range(cols):
        pivot = next((i for i in range(rank, rows) if a[i][c]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        x = a[rank][c]
        for j in range(c, cols):
            a[rank][j] /= x
        for i in range(rank+1, rows):
            if a[i][c]:
                x = a[i][c]
                for j in range(c, cols):
                    a[i][j] -= x*a[rank][j]
        rank += 1
        if rank == rows:
            break
    return rank


checks = 0
cases = 0
for k in range(2, 5):
    for sizes in product(range(1, 4), repeat=k):
        labels = [(i, a) for i, mi in enumerate(sizes) for a in range(mi)]
        N = len(labels)
        for r in [F(1), F(4, 3), F(2), F(3), F(4)]:
            v = [(F(mi-1, 2*mi)) for mi in sizes]
            b = [(r-F(1)+F(1, mi))/2 for mi in sizes]
            assert all(x > 0 for x in b)
            S = sum((1/x for x in b), F(0))
            p = [1/x/S for x in b]
            weights = [p[i]/sizes[i] for i, a in labels]
            R2 = r/2 - 1/S
            C2 = max(F(1), R2)
            assert R2 > 0
            # The sharp weighted variance certificate, computed independently.
            variance = sum((v[i]*p[i]**2 for i in range(k)), F(0))
            variance += r*sum((p[i]*p[j] for i in range(k) for j in range(i+1,k)), F(0))
            assert variance == R2
            checks += 1
            # Equilateral-cluster Euclidean realization: the explicit Gram form.
            gram=[]
            geom=[]
            for i,a in labels:
                row=[];grow=[]
                for j,c in labels:
                    d2 = F(0) if (i,a)==(j,c) else (F(1) if i==j else r)
                    row.append(C2 - d2/2)
                    grow.append((b[i] if i==j else F(0)) - F(1,S)
                                + ((F(1) if a==c else F(0))-F(1,sizes[i]))/2 if i==j
                                else -F(1,S))
                    assert row[-1] == grow[-1] + (C2-R2)
                    checks += 1
                gram.append(row);geom.append(grow)
            # Optimal hub distances are C when nonisometric and 1 when isometric.
            for u,(i,a) in enumerate(labels):
                assert gram[u][u] == C2
                for z,(j,c) in enumerate(labels):
                    d2 = F(0) if u==z else (F(1) if i==j else r)
                    assert gram[u][u]+gram[z][z]-2*gram[u][z] == d2
                    checks += 1
            # Optimal weighted barycenter vanishes in the centered leaf realization.
            for row in geom:
                assert sum((row[q]*weights[q] for q in range(N)), F(0)) == 0
                checks += 1
            # Exact rank characterizes the affine dimension and the transition.
            observed = rank_rational(gram)
            assert observed == (N if R2 < 1 else N-1), (sizes, r, observed, R2)
            checks += 1
            cases += 1

# Balanced-sizes formula and threshold: exact algebra.
for k in range(2, 11):
    for m in range(1, 11):
        threshold = F(2*k-1, k-1) + F(1, m*(k-1))
        for r in [F(1), F(3,2), F(2), F(3), F(4), threshold]:
            b = (r-1+F(1,m))/2
            R2 = r/2 - b/k
            assert R2 == ((k-1)*r+1-F(1,m))/(2*k)
            assert (R2 == 1) == (r == threshold)
            checks += 2
assert cases == 585, cases
print('CHECK_OK exact_cases=',cases,'exact_rational_assertions=',checks)
