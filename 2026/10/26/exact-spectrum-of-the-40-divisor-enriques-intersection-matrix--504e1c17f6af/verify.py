"""Exact standard-library certificate for the Enriques 40-divisor Gram matrix.

The incidence rules are those in Katsura--Kondo, arXiv:1411.3079v1, Sections 5--6.
"""
from itertools import combinations

LETTERS = tuple(range(6))
ALL = frozenset(LETTERS)

def all_matchings(items):
    items = tuple(items)
    if not items:
        return [()]
    a = items[0]
    out = []
    for j in range(1, len(items)):
        b = items[j]
        rest = items[1:j] + items[j+1:]
        for tail in all_matchings(rest):
            out.append(((a, b),) + tail)
    return out

duads = list(combinations(LETTERS, 2))
synthemes = sorted({tuple(sorted(tuple(sorted(pair)) for pair in m)) for m in all_matchings(LETTERS)})
seen = set(); totals = []
for A in combinations(LETTERS, 3):
    B = tuple(sorted(ALL - set(A)))
    key = tuple(sorted((tuple(A), B)))
    if key not in seen:
        seen.add(key); totals.append(key)
totals.sort()
assert (len(duads), len(synthemes), len(totals)) == (15, 15, 10)
vertices = [('duad', x) for x in duads] + [('syntheme', x) for x in synthemes] + [('total', x) for x in totals]
n = len(vertices)
G = [[0]*n for _ in range(n)]
for i, (kind, a) in enumerate(vertices):
    G[i][i] = -2
    for j in range(i+1, n):
        kind2, b = vertices[j]
        w = 0
        if kind == kind2 == 'duad':
            w = 1 if len(set(a) & set(b)) == 1 else 0
        elif kind == kind2 == 'syntheme':
            w = 1 if len(set(a) & set(b)) == 0 else 0
        elif {kind, kind2} == {'duad', 'syntheme'}:
            d = a if kind == 'duad' else b
            s = b if kind == 'duad' else a
            w = 2 if d in s else 0
        elif {kind, kind2} == {'duad', 'total'}:
            d = a if kind == 'duad' else b
            A, B = b if kind == 'duad' else a
            w = 2 if set(d).issubset(A) or set(d).issubset(B) else 0
        elif {kind, kind2} == {'syntheme', 'total'}:
            s = a if kind == 'syntheme' else b
            A, B = b if kind == 'syntheme' else a
            w = 2 if all((x in A and y in B) or (y in A and x in B) for x, y in s) else 0
        elif kind == kind2 == 'total':
            w = 2
        G[i][j] = G[j][i] = w

assert all(G[i][j] == G[j][i] for i in range(n) for j in range(n))

def mm(A, B):
    m, k, p = len(A), len(B), len(B[0])
    out = [[0]*p for _ in range(m)]
    for i in range(m):
        for r in range(k):
            if A[i][r]:
                ar = A[i][r]
                for j in range(p):
                    out[i][j] += ar * B[r][j]
    return out

def sub(A, B): return [[x-y for x,y in zip(ra,rb)] for ra,rb in zip(A,B)]
def scale(A, c): return [[c*x for x in row] for row in A]
def eye(n): return [[int(i==j) for j in range(n)] for i in range(n)]
G2 = mm(G, G)
G3 = mm(G2, G)
identity_poly = sub(sub(G3, scale(G2, 16)), scale(G, 336))
assert all(x == 0 for row in identity_poly for x in row)
trace = sum(G[i][i] for i in range(n))
trace2 = sum(G2[i][i] for i in range(n))
assert trace == -80
assert trace2 == 2080
# The matrix is real symmetric and satisfies G(G-28I)(G+12I)=0,
# so its eigenvalues lie in {0, 28, -12}. Trace and trace-square determine multiplicities.
assert n == 40
print('PASS: constructed the 40-divisor intersection matrix from the published incidence rules')
print('PASS: exact matrix identity G^3 - 16 G^2 - 336 G = 0')
print('PASS: trace(G) = -80 and trace(G^2) = 2080')
print('CONCLUSION: spectrum 28^1, (-12)^9, 0^30; rank 10; inertia (1, 9, 30)')
print('LIMIT: the spectrum proves full rank in Num(X), not index one of the generated sublattice')
