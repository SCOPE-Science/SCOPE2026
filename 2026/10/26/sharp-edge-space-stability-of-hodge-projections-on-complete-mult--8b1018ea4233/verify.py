"""Exact rational checks for endpoint gradient projections on complete multipartite graphs."""
from fractions import Fraction as F
from itertools import combinations

def partitions(total, blocks, least=1):
    if blocks == 0:
        if total == 0: yield ()
        return
    for s in range(least, total//blocks+1):
        for tail in partitions(total-s,blocks-1,s):
            yield (s,)+tail

def inverse(A):
    n=len(A)
    M=[[F(x) for x in row]+[F(i==j) for j in range(n)] for i,row in enumerate(A)]
    for j in range(n):
        p=next(i for i in range(j,n) if M[i][j]); M[j],M[p]=M[p],M[j]
        d=M[j][j]; M[j]=[z/d for z in M[j]]
        for i in range(n):
            if i==j:continue
            d=M[i][j]
            if d: M[i]=[a-d*b for a,b in zip(M[i],M[j])]
    return [row[n:] for row in M]

def f(N,a):
    return F(a,N)-F(2*(N-1),N*(N-a))

def predicted(N,a,b): return 2+f(N,a)+f(N,b)

def fq(N,a): return F(a,N)-F(4*(N-1),N*(N-a))
def predicted_q(N,a,b): return 3+fq(N,a)+fq(N,b)

def graph(parts):
    owner=[]
    for i,n in enumerate(parts): owner.extend([i]*n)
    edges=[(u,v) for u in range(len(owner)) for v in range(u+1,len(owner)) if owner[u]!=owner[v]]
    return owner,edges

def exact_projection(parts):
    owner,edges=graph(parts)
    N=len(owner); M=N-1
    L=[[F(0) for _ in range(M)] for __ in range(M)]
    for u,v in edges:
        if u: L[u-1][u-1]+=1
        if v: L[v-1][v-1]+=1
        if u and v: L[u-1][v-1]-=1;L[v-1][u-1]-=1
    R=inverse(L)
    evecs=[]
    for u,v in edges:
        e=[F(0) for _ in range(M)]
        if u: e[u-1]+=1
        if v: e[v-1]-=1
        evecs.append(e)
    projected=[[sum(R[i][k]*e[k] for k in range(M)) for i in range(M)] for e in evecs]
    P=[[sum(evecs[i][k]*projected[j][k] for k in range(M)) for j in range(len(edges))] for i in range(len(edges))]
    return owner,edges,P

def candidate_row_values(parts, owner, edge):
    N=len(owner); u,v=edge; a=parts[owner[u]];b=parts[owner[v]]
    pu=F(1,N*(N-a)); qv=F(1,N*(N-b))
    U=F(1,N)+(a-1)*pu; V=F(1,N)+(b-1)*qv
    vals=[F(0) for _ in owner]
    for k in range(N):
        if owner[k]==owner[u]: vals[k]=U if k==u else -pu
        if owner[k]==owner[v]: vals[k]=-V if k==v else qv
    return vals

def check():
    claims=0; configurations=0; edge_rows=0
    for N in range(2,11):
        for r in range(2,N+1):
            for parts in partitions(N,r):
                configurations+=1
                owner,edges,P=exact_projection(parts)
                E=len(edges)
                for i,(u,v) in enumerate(edges):
                    a,b=parts[owner[u]],parts[owner[v]]
                    row=P[i]; vals=candidate_row_values(parts,owner,(u,v))
                    expect=sum(abs(x) for x in row)
                    assert expect==predicted(N,a,b); claims+=1
                    qrow=[(F(i==j)-row[j]) for j in range(E)]
                    assert sum(abs(x) for x in qrow)==predicted_q(N,a,b); claims+=1
                    edge_rows+=1
                    for j,(x,y) in enumerate(edges):
                        assert row[j]==vals[x]-vals[y];claims+=1
                    assert sum(row[j]*P[j][i] for j in range(E))==row[i];claims+=1
                a,b=sorted(parts,reverse=True)[:2]
                assert max(sum(abs(x) for x in row) for row in P)==predicted(N,a,b);claims+=1
                qmax=max(predicted_q(N,parts[owner[u]],parts[owner[v]]) for u,v in edges)
                assert qmax==max(sum(abs((F(i==j)-P[i][j])) for j in range(E)) for i in range(E));claims+=1
                assert all(P[i][j]==P[j][i] for i in range(E) for j in range(E));claims+=E*E
                cap=N-r+2;top=(cap//2,cap-cap//2)
                winner=predicted(N,*top)
                assert winner>=predicted(N,a,b);claims+=1
    print('MULTIPARTITE_GRADIENT_EXACT_OK',claims,'configurations',configurations,'edge_rows',edge_rows)

if __name__=='__main__': check()
