"""Exact-polytope integration checks for uniform complete-bipartite Lipschitz potentials.

Requires scipy for boundary triangulations; determinants, volumes and moments
are recomputed using integer and rational arithmetic, not floating geometry.
"""
from fractions import Fraction as F
from itertools import product
from math import factorial
from scipy.spatial import ConvexHull


def det_integer(rows):
    n = len(rows)
    if n == 0:
        return 1
    a = [list(map(int, row)) for row in rows]
    previous = 1
    sign = 1
    for k in range(n-1):
        if a[k][k] == 0:
            pivot = next((j for j in range(k+1, n) if a[j][k]), None)
            if pivot is None:
                return 0
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k+1, n):
            for j in range(k+1, n):
                numerator = pivot*a[i][j]-a[i][k]*a[k][j]
                assert numerator % previous == 0
                a[i][j] = numerator//previous
        for i in range(k+1, n):
            a[i][k] = 0
        previous = pivot
    return sign*a[-1][-1]


def vertices(p, q):
    ans = set()
    for ss in product((-1, 1), repeat=q):
        ans.add(tuple([0]*(p-1) + list(ss)))
    for ss in product((-1, 1), repeat=p):
        ans.add(tuple([v-ss[0] for v in ss[1:]] + [-ss[0]]*q))
    return sorted(ans)


def matrices(p, q):
    N = p+q
    I = [[F(i==j) for j in range(N)] for i in range(N)]
    A = [[F(i==j and i<p)-F(i<p and j<p, p) for j in range(N)] for i in range(N)]
    B = [[F(i==j and i>=p)-F(i>=p and j>=p, q) for j in range(N)] for i in range(N)]
    C = [[I[i][j]-F(1,N)-A[i][j]-B[i][j] for j in range(N)] for i in range(N)]
    return [[F((p+1)*(p+2))*A[i][j]/(3*N*(N+1))+
             F((q+1)*(q+2))*B[i][j]/(3*N*(N+1))+
             F(p*q+2)*C[i][j]/(3*N*(N+1)) for j in range(N)] for i in range(N)]


def check(p, q):
    N = p+q
    d = N-1
    vertices_list = vertices(p, q)
    hull = ConvexHull(vertices_list)
    sum_vol = F(0)
    sum_mom = [[F(0) for j in range(N)] for i in range(N)]
    active_simplices = 0
    # Each boundary simplex, joined to the origin, is a full-dimensional
    # simplex. Distinct cones intersect only on zero-volume boundaries.
    for face in hull.simplices:
        coordinate_rows = [vertices_list[int(index)] for index in face]
        determinant = abs(det_integer(coordinate_rows))
        if determinant == 0:
            continue
        volume = F(determinant, factorial(d))
        sum_vol += volume
        active_simplices += 1
        # The zero vertex and d boundary vertices, written as centered ambient
        # numerators: Z_i=(N*w_i-sum(w))/N.
        numerators = [[0]*N]
        for coords in coordinate_rows:
            ambient = [0]+list(coords)
            total = sum(ambient)
            numerators.append([N*z-total for z in ambient])
        column_sums = [sum(row[i] for row in numerators) for i in range(N)]
        for i in range(N):
            for j in range(N):
                diagonal_sum = sum(row[i]*row[j] for row in numerators)
                sum_mom[i][j] += volume*F(
                    diagonal_sum+column_sums[i]*column_sums[j],
                    N*N*(d+1)*(d+2)
                )
    expected_vol = F(2**d*factorial(p)*factorial(q), factorial(d))
    assert sum_vol == expected_vol, (p, q, sum_vol, expected_vol)
    target = matrices(p, q)
    assert all(sum_mom[i][j]/sum_vol == target[i][j]
               for i in range(N) for j in range(N)), (p, q)
    return len(vertices_list), active_simplices


if __name__ == '__main__':
    suite = [(2,2),(2,3),(3,2),(3,3),(2,4),(4,2),(3,4),(4,3)]
    for p,q in suite:
        v,s = check(p,q)
        print('PASS', 'K_%d,%d'%(p,q), 'vertices',v, 'simplices',s)
    print('EXACT_BIPARTITE_BULK_MOMENTS_PASS', len(suite), 'cases')
