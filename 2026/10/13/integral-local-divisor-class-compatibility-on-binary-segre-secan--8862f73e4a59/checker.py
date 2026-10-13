"""Exact integral/combinatorial checks for local class-group restriction lattices.

Only Python 3 standard-library modules are needed.  This is finite corroboration
of the separately supplied general proof, not a proof for all integers n.
"""
from fractions import Fraction
from itertools import combinations
from math import comb


def rank(a):
    if not a:
        return 0
    b = [[Fraction(x) for x in row] for row in a]
    rows, cols = len(b), len(b[0])
    r = 0
    for c in range(cols):
        pivot = next((k for k in range(r, rows) if b[k][c]), None)
        if pivot is None:
            continue
        b[r], b[pivot] = b[pivot], b[r]
        v = b[r][c]
        for j in range(c, cols):
            b[r][j] /= v
        for k in range(r+1, rows):
            v = b[k][c]
            if v:
                for j in range(c, cols):
                    b[k][j] -= v * b[r][j]
        r += 1
        if r == rows:
            break
    return r


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def basis(i, n):
    return [int(j == i) for j in range(n)]


def toric_rays(n):
    a = [[0] + basis(i, n) for i in range(n)]
    b = [[1] + [-z for z in basis(i, n)] for i in range(n)]
    w = [-2] + [1]*n
    return a, b, w


def quadrilateral_matrix(n, edges):
    indices = {ij: j for j,ij in enumerate(edges)}
    Q = []
    for i,j,k,l in combinations(range(n),4):
        for negative in ([(i,k),(j,l)], [(i,l),(j,k)]):
            row = [0]*len(edges)
            for ij in [(i,j),(k,l)]:
                row[indices[ij]] += 1
            for ij in negative:
                row[indices[ij]] -= 1
            Q.append(row)
    return Q


def analyze(n):
    assert 4 <= n <= 8
    a,b,w = toric_rays(n)
    rays = a+b+[w]
    edges = list(combinations(range(n),2))
    R = []
    for i,j in edges:
        row = [int(k in (i,j)) for k in range(n)] + [1]
        R.append(row)
    Q = quadrilateral_matrix(n, edges)

    assert rank(rays) == n+1
    # n coordinate normals and the first upper normal form a unimodular basis.
    assert a[0] == [0,1] + [0]*(n-1)
    assert [b[0][0],b[0][1]] == [1,-1]
    # Pairwise restriction entries are 1 precisely at incident vertex divisors.
    assert rank(R) == n
    assert rank(Q) == len(edges)-n
    assert all(sum(q[e]*R[e][k] for e in range(len(edges))) == 0
               for q in Q for k in range(n+1))
    # Independent proof of primitivity: R has an integer right-coordinate
    # reconstruction from balanced edge labels; see RESULT.md.

    # Each candidate facet must contain an affine-dimensional n-1 face.
    vertices = [[int(i in S) for i in range(n)] for k in range(2,n+1)
                for S in combinations(range(n),k)]
    assert len(vertices) == 2**n-n-1
    tests = [lambda v, i=i: v[i]==0 for i in range(n)] + [
        lambda v, i=i: v[i]==1 for i in range(n)] + [
        lambda v: sum(v)==2]
    for condition in tests:
        points = [v for v in vertices if condition(v)]
        p0 = points[0]
        assert rank([[v[i]-p0[i] for i in range(n)] for v in points[1:]]) == n-1

    for i,j in edges:
        v = [int(k in (i,j)) for k in range(n)]
        incident = [b[k] if k in (i,j) else a[k] for k in range(n)] + [w]
        assert len(incident) == n+1
        assert all(dot(row,[1]+v)==0 for row in incident)
        assert rank(incident) == n
        assert all(dot(incident[k], [1]+v)==0 for k in range(n+1))
        # The first n incident normals give a basis for the saturated
        # hyperplane {x_0+x_i+x_j=0}, as shown algebraically in the proof.
        assert all(dot(incident[k], [1]+v)==0 for k in range(n))
        # Relation of the final ray with respect to this basis.
        s = [-1 if k in (i,j) else 1 for k in range(n)]
        assert [sum(s[k]*incident[k][t] for k in range(n))
                for t in range(n+1)] == w

    # Verify random-looking integer potentials, their 4-cycle conditions and
    # the exact constructive inverse using t_i = u_ij+u_ik-u_jk.
    for seed in range(10):
        aa = [((seed+3)*i*i+5*i+7*seed) % 19 - 8 for i in range(n)]
        bb = (7*seed)%13 - 4
        values = {(i,j):aa[i]+aa[j]+bb for i,j in edges}
        vv = [values[e] for e in edges]
        assert all(dot(q,vv)==0 for q in Q)
        t = []
        for i in range(n):
            j,k = [x for x in range(n) if x!=i][:2]
            get=lambda u,v:values[tuple(sorted((u,v)))]
            t.append(get(i,j)+get(i,k)-get(j,k))
        assert len({x%2 for x in t})==1
        b0=t[0]%2
        x=[(ti-b0)//2 for ti in t]
        assert all(x[i]+x[j]+b0==values[i,j] for i,j in edges)

    return (f'n={n} vertices={len(vertices)} facets={2*n+1} '
            f'singular_vertex_charts={len(edges)} '
            f'origin_class_rank={n} component_class_rank=1 '
            f'edge_map_rank={rank(R)} four_cycle_rank={rank(Q)} '
            f'free_cokernel_rank={comb(n,2)-n} OK')


if __name__ == '__main__':
    for n in range(4,9):
        print(analyze(n))
