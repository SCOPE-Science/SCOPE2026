"""Exact finite checks for subdivision projection identities.
Run with Python 3.10+: python verify_subdivision.py .
This program is corroborative; the theorem is proved algebraically.
"""
from fractions import Fraction as F
from itertools import combinations

def inv(A):
    n=len(A)
    T=[[F(x) for x in A[i]]+[F(i==j) for j in range(n)] for i in range(n)]
    for col in range(n):
        row=next((k for k in range(col,n) if T[k][col]),None)
        assert row is not None, 'Expected invertibility of a reduced connected Laplacian'
        T[col],T[row]=T[row],T[col]
        d=T[col][col]; T[col]=[v/d for v in T[col]]
        for k in range(n):
            if k != col:
                d=T[k][col]
                if d: T[k]=[T[k][j]-d*T[col][j] for j in range(2*n)]
    return [r[n:] for r in T]

def matmul(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))),F(0)) for j in range(len(B[0]))] for i in range(len(A))]

def projection(n,edges):
    # Direct orthogonal projection onto cycle space using the incidence Laplacian.
    m=len(edges); D=[[F(0) for _ in range(m)] for _ in range(n)]
    for j,(u,v) in enumerate(edges): D[u][j]-=1; D[v][j]+=1
    DR=D[:-1]
    L=matmul(DR,list(map(list,zip(*DR))))
    Li=inv(L)
    R=matmul(list(map(list,zip(*DR))),matmul(Li,DR))
    return [[F(i==j)-R[i][j] for j in range(m)] for i in range(m)]

def subdivisions(n,edges,lengths):
    out=[]; labels=[]; next_v=n
    for e,(u,v) in enumerate(edges):
        old=u
        for j in range(lengths[e]):
            new= v if j==lengths[e]-1 else next_v
            if new==next_v: next_v+=1
            out.append((old,new)); labels.append(e); old=new
    return next_v,out,labels

def test_case(name,n,edges,lengths):
    C=projection(n,edges)
    nn,new_edges,labels=subdivisions(n,edges,lengths)
    H=projection(nn,new_edges)
    m=len(edges)
    # Independently build the symmetric weighted graph-Laplacian expression.
    E=[[F(0) for _ in range(m)] for _ in range(n)]
    for j,(u,v) in enumerate(edges): E[u][j]-=1; E[v][j]+=1
    E=E[:-1]
    W=[[F(1,lengths[e]) if e==f else F(0) for f in range(m)] for e in range(m)]
    EW=matmul(E,W)
    L=matmul(EW,list(map(list,zip(*E))))
    A=matmul(W,matmul(list(map(list,zip(*E))),matmul(inv(L),matmul(E,W))))
    T=[[W[e][f]-A[e][f] for f in range(m)] for e in range(m)]
    for i in range(len(new_edges)):
        for j in range(len(new_edges)):
            assert H[i][j]==T[labels[i]][labels[j]],(name,i,j,H[i][j],T[labels[i]][labels[j]])
    for f in range(m):
        col=sum((lengths[e]*abs(T[e][f]) for e in range(m)),F(0))
        q_col=F(1)+col-2*T[f][f]
        actualC=sum(abs(H[i][labels.index(f)]) for i in range(len(new_edges)))
        actualQ=sum(abs(F(i==labels.index(f))-H[i][labels.index(f)]) for i in range(len(new_edges)))
        assert col==actualC,(name,'cycle',f)
        assert q_col==actualQ,(name,'cut',f)
    if len(set(lengths))==1:
        r=lengths[0]
        for e in range(m):
            for f in range(m): assert T[e][f]==C[e][f]/r
        origC=max((sum(abs(C[e][f]) for e in range(m)) for f in range(m)), default=F(0))
        newC=max((sum(lengths[e]*abs(T[e][f]) for e in range(m)) for f in range(m)),default=F(0))
        assert origC==newC
    if min(lengths)>=2:
        maxC=max((sum(lengths[e]*abs(T[e][f]) for e in range(m)) for f in range(m)),default=F(0))
        maxQ=max((F(1)+sum(lengths[e]*abs(T[e][f]) for e in range(m))-2*T[f][f] for f in range(m)),default=F(0))
        assert maxQ>maxC,(name,'dominance')
    return len(new_edges),len(new_edges)**2

def main():
    graphs={
       'K5':(5,list(combinations(range(5),2))),
       'K4':(4,list(combinations(range(4),2))),
       'C6':(6,[(i,(i+1)%6) for i in range(6)]),
       'theta':(5,[(0,2),(2,1),(0,3),(3,1),(0,4),(4,1)]),
       'two triangles with bridge':(6,[(0,1),(1,2),(0,2),(3,4),(4,5),(3,5),(2,3)]),
       'tree':(5,[(0,1),(1,2),(1,3),(3,4)]),
       'K3,3':(6,[(i,j) for i in range(3) for j in range(3,6)]),
    }
    cases=0; entries=0
    for name,(n,edges) in graphs.items():
        m=len(edges)
        for rr in (1,2,3):
            z,k=test_case(name+' uniform '+str(rr),n,edges,[rr]*m)
            cases+=1; entries+=k
        lengths=[2+(i*7+3)%3 for i in range(m)]
        z,k=test_case(name+' nonuniform all subdivided',n,edges,lengths)
        cases+=1; entries+=k
        z,k=test_case(name+' mixed old and subdivided',n,edges,[1+(i*5+1)%4 for i in range(m)])
        cases+=1; entries+=k
    # A discontinuous reversal example: before and after one subdivision.
    n,edges=graphs['K5']; C=projection(n,edges)
    c=max(sum(abs(C[i][j]) for i in range(len(edges))) for j in range(len(edges)))
    q=max(sum(abs(F(i==j)-C[i][j]) for i in range(len(edges))) for j in range(len(edges)))
    assert c==F(9,5) and q==F(8,5)
    nn,E,L=subdivisions(n,edges,[2]*len(edges)); S=projection(nn,E)
    cs=max(sum(abs(S[i][j]) for i in range(len(E))) for j in range(len(E)))
    qs=max(sum(abs(F(i==j)-S[i][j]) for i in range(len(E))) for j in range(len(E)))
    assert cs==F(9,5) and qs==F(11,5)
    print('PASS: %d exact-rational graphs/length configurations, %d full projection entries checked' % (cases,entries))
    print('PASS: K5 reversal: original (cut,cycle)=(8/5,9/5), subdivision (cut,cycle)=(11/5,9/5)')
if __name__=='__main__': main()
