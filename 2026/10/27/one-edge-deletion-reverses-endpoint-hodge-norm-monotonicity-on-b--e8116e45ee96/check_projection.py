"""Exact rational verification of the balanced tripartite edge-deletion formulas.

Run: python check_projection.py
Uses only the Python standard library. Finite checks corroborate the proof,
not an all-parameter substitute.
"""
from fractions import Fraction as F


def inverse(mat):
    n = len(mat)
    arr = [[F(x) for x in row] + [F(i == j) for j in range(n)]
           for i, row in enumerate(mat)]
    for j in range(n):
        pivot = next(i for i in range(j, n) if arr[i][j])
        arr[j], arr[pivot] = arr[pivot], arr[j]
        v = arr[j][j]
        arr[j] = [z / v for z in arr[j]]
        for i in range(n):
            if i != j and arr[i][j]:
                v = arr[i][j]
                arr[i] = [x - v*y for x, y in zip(arr[i], arr[j])]
    return [row[n:] for row in arr]


def get_edges(m, deleted):
    edges = [(u, v) for u in range(3*m) for v in range(u+1, 3*m)
             if u//m != v//m]
    return [e for e in edges if e != (0, m)] if deleted else edges


def calc(m, deleted):
    N=3*m
    edges=get_edges(m, deleted)
    L=[[0]*N for _ in range(N)]
    for u,v in edges:
        L[u][u]+=1;L[v][v]+=1
        L[u][v]-=1;L[v][u]-=1
    G=inverse([row[:-1] for row in L[:-1]])
    qcols=[];pcols=[]
    for u,v in edges:
        z=[F(int(i==u)-int(i==v)) for i in range(N-1)]
        pot=[sum(G[i][j]*z[j] for j in range(N-1)) for i in range(N-1)]+[F(0)]
        q=[pot[a]-pot[b] for a,b in edges]
        qnorm=sum(map(abs,q));pdiag=pot[u]-pot[v]
        pnorm=1+qnorm-2*pdiag
        qcols.append(qnorm);pcols.append(pnorm)
    return max(qcols),max(pcols),sum(1 for x in qcols if x==max(qcols)),sum(1 for x in pcols if x==max(pcols)),len(edges)


def formulas(m):
    den=3*m*m-3*m+1
    Q0=F(2*(4*m*m-3*m+1),3*m*m)
    P0=F(11*m*m-12*m+4,3*m*m)
    QY=F(8*m**3-14*m*m+11*m-4,m*den)
    QZ=F(16*m**4-26*m**3+16*m*m-5*m+1,2*m*m*den)
    PY=F((m-1)*(11*m*m-12*m+8),m*den)
    PZ=F((m-1)*(22*m**3-22*m*m+9*m-2),2*m*m*den)
    return Q0,P0, (QY if m==2 else QZ),(PY if m<=3 else PZ)


def main():
    total=0
    for m in range(2,7):
        Q0,P0,Q1,P1=formulas(m)
        a=calc(m,False); b=calc(m,True)
        assert a[:2] == (Q0,P0),(m,'intact',a, Q0,P0)
        assert b[:2] == (Q1,P1),(m,'deleted',b,Q1,P1)
        assert Q1>Q0
        assert P1>=P0
        assert (P1==P0)==(m==2)
        total+=a[-1]+b[-1]
        print('m=',m,'edges=',a[-1],b[-1], 'Q0=',Q0,'Q1=',Q1, 'P0=',P0,'P1=',P1)
    print('EXACT_TRIPARTITE_CHECKS_OK',total,'complete columns')

if __name__=='__main__': main()
