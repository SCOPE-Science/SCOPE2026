"""Exact-rational checks of conductance-perturbed complete bipartite projections.

Run: python3 weighted_edge_checker.py
No third-party packages are required. Finite checks supplement an analytical proof.
"""
from fractions import Fraction as F
from math import sqrt


def inverse(a):
    n = len(a)
    aug = [[F(z) for z in row] + [F(i == j) for j in range(n)]
           for i, row in enumerate(a)]
    for col in range(n):
        pivot = next(i for i in range(col, n) if aug[i][col])
        aug[col], aug[pivot] = aug[pivot], aug[col]
        val = aug[col][col]
        aug[col] = [z / val for z in aug[col]]
        for i in range(n):
            if i != col and aug[i][col]:
                k = aug[i][col]
                aug[i] = [u-k*v for u, v in zip(aug[i], aug[col])]
    return [row[n:] for row in aug]


def weighted_projection(n, sqroot_conductance):
    edges = [(i,j) for i in range(n) for j in range(n)]
    # Delete the last vertex coordinate, forming a reduced full-row-rank incidence matrix.
    b = []
    for i,j in edges:
        s = sqroot_conductance if (i,j)==(0,0) else F(1)
        full = [F(0)]*(2*n)
        full[i] = -s
        full[n+j] = s
        b.append(full[:-1])
    k = 2*n-1
    lap = [[sum(b[e][i]*b[e][j] for e in range(n*n)) for j in range(k)] for i in range(k)]
    li = inverse(lap)
    z = [[sum(b[e][h]*li[h][j] for h in range(k)) for j in range(k)] for e in range(n*n)]
    q = [[sum(z[a][j]*b[bidx][j] for j in range(k)) for bidx in range(n*n)] for a in range(n*n)]
    return edges,q


def predicted_entry(n,s,edge_a,edge_b):
    def base(a,b):
        return F(n*(a[0]==b[0])+n*(a[1]==b[1])-1,n*n)
    e=(0,0)
    h=base(e,e)
    d=1+(s*s-1)*h
    if edge_a == e and edge_b == e:
        return s*s*h/d
    if edge_a == e:
        return s*base(e,edge_b)/d
    if edge_b == e:
        return s*base(edge_a,e)/d
    return base(edge_a,edge_b)-(s*s-1)*base(edge_a,e)*base(e,edge_b)/d


checked = 0
for n in (3,4,5,6,8):
    for s in (F(1,4),F(1,2),F(1),F(3,2),F(2),F(5)):
        edges,q=weighted_projection(n,s)
        for a,ea in enumerate(edges):
            for b,eb in enumerate(edges):
                assert q[a][b] == predicted_entry(n,s,ea,eb), (n,s,ea,eb)
                assert q[a][b] == q[b][a]
                checked += 1
        eidx=0
        h=F(2*n-1,n*n)
        k=F((n-1)**2,2*n-1)
        qsum=sum(abs(q[a][eidx]) for a in range(n*n))
        psum=sum(abs(F(a==eidx)-q[a][eidx]) for a in range(n*n))
        assert qsum == (s*s+3*k*s)/(k+s*s)
        assert psum == (k+3*k*s)/(k+s*s)
        if s==1:
            assert max(sum(abs(q[a][j]) for a in range(n*n)) for j in range(n*n)) == F(3*n*n-4*n+2,n*n)
            assert max(sum(abs(F(a==j)-q[a][j]) for a in range(n*n)) for j in range(n*n)) == F(4*n*n-8*n+4,n*n)

for n in range(29,100):
    k=(n-1)**2/(2*n-1)
    assert (1+sqrt(1+9*k))/2 > 6
    sQ=(1+sqrt(1+9*k))/3
    sP=(sqrt(1+9*k)-1)/3
    valQ=(sQ*sQ+3*k*sQ)/(sQ*sQ+k)
    valP=(k+3*k*sP)/(sP*sP+k)
    val=(1+sqrt(1+9*k))/2
    assert abs(valQ-val)<2e-12 and abs(valP-val)<2e-12
    assert abs(sQ*sP-k)<2e-12
print('WEIGHTED_BIPARTITE_CERTIFICATE_OK', 'matrix_entries='+str(checked), 'dimensions=5', 'weights=6', 'asymptotic_parameters=71')
