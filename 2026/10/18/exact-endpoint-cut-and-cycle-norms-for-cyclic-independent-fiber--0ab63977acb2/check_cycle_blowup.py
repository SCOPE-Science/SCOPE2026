"""Exact rational tests for canonical cut/cycle projections of cyclic independent-fiber blowups.
Uses a grounded Laplacian inverse, independently of the tensor-product proof.
Python 3 standard library only: python check_cycle_blowup.py
"""
from fractions import Fraction as F


def inverse(A):
    n = len(A)
    T = [[F(A[i][j]) for j in range(n)] + [F(i == j) for j in range(n)] for i in range(n)]
    for j in range(n):
        k = next(k for k in range(j, n) if T[k][j])
        T[j], T[k] = T[k], T[j]
        pivot = T[j][j]
        T[j] = [z / pivot for z in T[j]]
        for i in range(n):
            if i != j:
                c = T[i][j]
                if c:
                    T[i] = [u - c*v for u,v in zip(T[i],T[j])]
    return [row[n:] for row in T]


def check(n, r):
    verts = n*r
    edges = [((x*r+a), (((x+1)%n)*r+b))
             for x in range(n) for a in range(r) for b in range(r)]
    m = len(edges)
    L = [[0]*verts for _ in range(verts)]
    for u,v in edges:
        L[u][u] += 1; L[v][v] += 1
        L[u][v] -= 1; L[v][u] -= 1
    inv = inverse([row[:-1] for row in L[:-1]])
    Q = [[F(0) for _ in range(m)] for _ in range(m)]
    # Fix the last potential to zero; this preserves all edge currents.
    for k,(u,v) in enumerate(edges):
        phi = [((inv[i][u] if u<verts-1 else F(0))
                -(inv[i][v] if v<verts-1 else F(0))) for i in range(verts-1)] + [F(0)]
        for j,(a,b) in enumerate(edges):
            Q[j][k] = phi[a]-phi[b]
    expected_q = 4-F(2,r)-F(4,n)+F(2,n*r*r)
    expected_c = 5-F(4,r)-F(4,n)+F(4,n*r*r)
    expected_diag = F(1,r)-F(1,n*r*r)
    for j in range(m):
        assert Q[j][j] == expected_diag,(n,r,j,'diag')
        assert sum(abs(Q[i][j]) for i in range(m)) == expected_q,(n,r,j,'cut')
        assert sum(abs(F(i==j)-Q[i][j]) for i in range(m)) == expected_c,(n,r,j,'cycle')
        for k in range(m):
            assert Q[j][k]==Q[k][j],(n,r,j,k,'symmetry')
    # Projector verification from incidence: BQ=B, hence Q is the orthogonal cut projector.
    for x in range(verts):
        for j in range(m):
            div = sum((F(x==u)-F(x==v))*Q[k][j]
                      for k,(u,v) in enumerate(edges))
            assert div == (F(x==edges[j][0])-F(x==edges[j][1])),(n,r,x,j,'divergence')
    return m


def main():
    samples = [(4,1),(4,2),(4,3),(5,2),(5,3),(6,2),(7,2),(8,2),(6,3)]
    counts=[]
    for n,r in samples:
        m=check(n,r);counts.append(m)
        print('PASS',n,r,'edge columns',m)
    print('EXACT_RATIONAL_PASS',len(samples),'graphs',sum(counts),'edge columns')


if __name__ == '__main__':
    main()
