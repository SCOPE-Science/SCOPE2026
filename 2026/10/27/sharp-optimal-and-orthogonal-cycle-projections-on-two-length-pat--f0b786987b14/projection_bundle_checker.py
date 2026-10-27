"""Exact rational checks for cycle-space projections on two-terminal path bundles.

Run: python projection_bundle_checker.py
No external packages required. Finite tests support, but do not replace, the proof.
"""
from fractions import Fraction as F
from itertools import product


def inverse(matrix):
    n = len(matrix)
    A = [[F(v) for v in matrix[i]] + [F(i == j) for j in range(n)] for i in range(n)]
    for j in range(n):
        pivot = next(k for k in range(j, n) if A[k][j])
        A[j], A[pivot] = A[pivot], A[j]
        q = A[j][j]
        A[j] = [v/q for v in A[j]]
        for i in range(n):
            if i == j: continue
            q = A[i][j]
            A[i] = [u-q*v for u,v in zip(A[i],A[j])]
    return [row[n:] for row in A]


def optimal_weight(a, b, r):
    R = F(b, a)
    gam = F(a, b)-F(r-2, r)
    if gam <= 0:
        s = F(1)
    else:
        s = (R-1+F(2,r))/(R+1/R+F(2,r))
    return [s]+[(1-s)/r]*r


def predicted(a, b, r):
    if r>=3 and b*(r-2)>=a*r:
        return 1+F(a,b)
    return F((a+b)**2, a*a+b*b)+F(0) if False else F((a+b)**2*r, r*(a*a+b*b)+2*a*b)


def matrices(a,b,r,w):
    lengths=[a]+[b]*r
    paths=[]
    for i,L in enumerate(lengths):
        paths.extend([i]*L)
    m=len(paths)
    assert sum(w)==1
    P=[[F(int(paths[row]==paths[col]))-w[paths[row]] for col in range(m)] for row in range(m)]
    for row in range(m):
        for col in range(m):
            P[row][col]/=lengths[paths[col]]
    return P,paths


def norm(P):
    return max(sum(abs(P[i][j]) for i in range(len(P))) for j in range(len(P)))


def verify_idempotent(P,paths):
    m=len(paths);k=max(paths)+1
    # Every column has identical entries within each path and zero total path current.
    for col in range(m):
        vals=[P[paths.index(i)][col] for i in range(k)]
        assert sum(vals)==0
        assert all(P[row][col]==vals[paths[row]] for row in range(m))
        for row in range(m):
            lhs=sum(P[row][q]*P[q][col] for q in range(m))
            assert lhs==P[row][col]


def orthogonal(a,b,r):
    L=[a]+[b]*r
    w=[F(1,t) for t in L]; T=sum(w); w=[v/T for v in w]
    P,p=matrices(a,b,r,w)
    # Independently reconstruct Z (Z^T Z)^{-1} Z^T with signed cycle vectors.
    m=len(p)
    Z=[[F(-1 if p[e]==0 else (1 if p[e]==j+1 else 0)) for j in range(r)] for e in range(m)]
    gram=[[sum(Z[e][i]*Z[e][j] for e in range(m)) for j in range(r)] for i in range(r)]
    inv=inverse(gram)
    for x in range(m):
        for y in range(m):
            v=sum(Z[x][i]*inv[i][j]*Z[y][j] for i in range(r) for j in range(r))
            assert v==P[x][y]
    return P


def main():
    count=0
    for r in (2,3,4,5):
        for a,b in ((2,2),(2,3),(2,4),(2,6),(3,6),(3,9)):
            P,paths=matrices(a,b,r,optimal_weight(a,b,r))
            actual=norm(P)
            assert actual==predicted(a,b,r),(a,b,r,actual,predicted(a,b,r))
            verify_idempotent(P,paths)
            # Exact inequalities at a grid of independently chosen competitors.
            for s_num in range(-12,37):
                s=F(s_num,24)
                Q,_=matrices(a,b,r,[s]+[(1-s)/r]*r)
                assert norm(Q)>=actual
            count+=1
    for r in (3,4,5,6):
        a=2;b=2*r
        w=optimal_weight(a,b,r)
        Q,paths=matrices(a,b,r,w)
        assert w[0]==1 and all(v==0 for v in w[1:])
        P=orthogonal(a,b,r)
        assert norm(Q)==1+F(1,r)
        assert norm(P)==F(r+1,2)
        assert norm(P)/norm(Q)==F(r,2)
        count+=1
    print('VERIFY_OK',count,'exact-rational cases; matrices, orthogonal Gram inverses, projection identity, and candidate norms')

if __name__=='__main__': main()
