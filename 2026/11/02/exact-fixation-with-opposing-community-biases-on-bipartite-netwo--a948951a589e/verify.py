from fractions import Fraction as F
from itertools import product


def exact_formula(nu,nw,du,dw,ku,kw,pU,qU,pW,qW):
    Q=qU*qW/(pU*pW)
    if Q==1:
        return (F(du)*qW/pU*ku + F(dw)*kw)/(F(du)*qW/pU*nu+F(dw)*nw)
    A=qW*du/(pU*dw)
    zW=(Q+A)/(1+A)
    zU=Q/zW
    return (1-zU**ku*zW**kw)/(1-zU**nu*zW**nw)

def test_graph(nu,nw,edges,params):
    nn=nu+nw
    adj=[[] for _ in range(nn)]
    for x,y in edges:
        assert 0<=x<nu and nu<=y<nn
        adj[x].append(y);adj[y].append(x)
    du=len(adj[0]);dw=len(adj[nu])
    assert all(len(adj[v])==du for v in range(nu)) and all(len(adj[v])==dw for v in range(nu,nn))
    assert nu*du==nw*dw
    pU,qU,pW,qW=params
    rate=lambda v,bit: (pU if bit==0 else qU) if v<nu else (pW if bit==0 else qW)
    nb=0
    for state in range(1<<nn):
        ku=sum((state>>v)&1 for v in range(nu));kw=sum((state>>v)&1 for v in range(nu,nn))
        f=exact_formula(nu,nw,du,dw,ku,kw,*params)
        drift=F(0)
        for v in range(nn):
            bv=(state>>v)&1
            for w in adj[v]:
                if bv==((state>>w)&1): continue
                state2=state^(1<<v)
                ku2=ku+(1-2*bv if v<nu else 0)
                kw2=kw+(1-2*bv if v>=nu else 0)
                f2=exact_formula(nu,nw,du,dw,ku2,kw2,*params)
                drift+=rate(v,bv)*F(1,nn*len(adj[v]))*(f2-f)
        assert drift==0,(nu,nw,params,state,drift)
        nb+=1
    return nb

if __name__=='__main__':
    graphs=[(1,4,[(0,i) for i in range(1,5)]), (2,3,[(i,j) for i in range(2) for j in range(2,5)]), (3,3,[(i,3+i) for i in range(3)]+[(i,3+(i+1)%3) for i in range(3)]), (6,4,[(i,6+i%4) for i in range(6)]+[(i,6+(i+1)%4) for i in range(6)])]
    # last 6x4 graph above not biregular, replace with incidence graph of K4, U=6 edges, W=4 vertices
    graphs[-1]=(6,4,[(i,6+a) for i,(a,b) in enumerate([(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)])]+[(i,6+b) for i,(a,b) in enumerate([(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)])])
    params=[tuple(map(F,vals)) for vals in [('3/4','1/4','1/2','1/3'),('1','1/4','1/4','1'),('2/3','1/3','2/3','1/3'),('1/4','3/4','1/3','2/3'),('1','1/4','1/3','1')]]
    total=0
    for nU,nW,edges in graphs:
        for ps in params:
            total+=test_graph(nU,nW,edges,ps)
    print('PASS: exact Markov harmonicity on',total,'state-parameter cases across 4 biregular graphs and 5 four-rate regimes')

def independent_linear_system(nu,nw,edges,params):
    # Independently compute absorption probabilities from the transition matrix.
    n=nu+nw
    adj=[[] for _ in range(n)]
    for a,b in edges:
        adj[a].append(b);adj[b].append(a)
    pU,qU,pW,qW=params
    states=list(range(1,(1<<n)-1))
    idx={s:i for i,s in enumerate(states)}
    N=len(states)
    A=[[F(0) for _ in range(N+1)] for _ in range(N)]
    for r,s in enumerate(states):
        A[r][r]=0
        for v in range(n):
            bit=(s>>v)&1
            rate=(pU if not bit else qU) if v<nu else (pW if not bit else qW)
            for w in adj[v]:
                if bit == ((s>>w)&1):continue
                t=s^(1<<v)
                a=rate/F(n*len(adj[v]))
                A[r][r]+=a
                if t==(1<<n)-1:A[r][-1]+=a
                elif t!=0:A[r][idx[t]]-=a
    # Fractional Gauss-Jordan elimination, without invoking the martingale.
    for col in range(N):
        k=next(i for i in range(col,N) if A[i][col]); A[col],A[k]=A[k],A[col]
        fac=A[col][col]
        for j in range(col,N+1):A[col][j]/=fac
        for row in range(N):
            if row==col:continue
            fac=A[row][col]
            if fac:
                for j in range(col,N+1):A[row][j]-=fac*A[col][j]
    for state,r in idx.items():
        ku=sum((state>>v)&1 for v in range(nu))
        kw=sum((state>>v)&1 for v in range(nu,n))
        result=exact_formula(nu,nw,len(adj[0]),len(adj[nu]),ku,kw,*params)
        assert A[r][-1] == result, (state,A[r][-1],result)
    return N

if __name__=='__main__':
    tally=0
    for g in [graphs[0],graphs[1],graphs[2]]:
        for par in [params[0],params[1],params[3]]:
            tally += independent_linear_system(*g,par)
    print('PASS: independent exact-rational Markov-chain solves for',tally,'nonabsorbing states')

def test_irregular_critical(graph,partU,params):
    n=len(graph); U=set(partU); pU,qU,pW,qW=params
    assert pU*pW==qU*qW
    degrees=[len(nei) for nei in graph]
    weights=[F(qW,pU)*degrees[v] if v in U else F(degrees[v]) for v in range(n)]
    denom=sum(weights)
    states=list(range(1,(1<<n)-1)); inds={s:i for i,s in enumerate(states)}; N=len(states)
    A=[[F(0) for _ in range(N+1)] for _ in range(N)]
    for r,s in enumerate(states):
        expected=sum(weights[v] for v in range(n) if (s>>v)&1)/denom
        for v in range(n):
            b=(s>>v)&1
            rate=(pU if b==0 else qU) if v in U else (pW if b==0 else qW)
            for w in graph[v]:
                if b==((s>>w)&1): continue
                t=s^(1<<v); a=rate/F(n*degrees[v]);A[r][r]+=a
                if t==(1<<n)-1:A[r][-1]+=a
                elif t!=0:A[r][inds[t]]-=a
        # Direct linear probability is harmonic independent of inversion.
        drift=sum(A[r][j]*(sum(weights[v] for v in range(n) if (states[j]>>v)&1)/denom) for j in range(N)) - A[r][-1]
        assert drift==0,(r,s,drift)
    for k in range(N):
        h=next(i for i in range(k,N) if A[i][k]!=0); A[k],A[h]=A[h],A[k]
        f=A[k][k]
        for j in range(k,N+1):A[k][j]/=f
        for i in range(N):
            if i==k:continue
            f=A[i][k]
            if f:
                for j in range(k,N+1):A[i][j]-=f*A[k][j]
    for s,r in inds.items():
        expected=sum(weights[v] for v in range(n) if (s>>v)&1)/denom
        assert expected==A[r][-1]
    return N

if __name__=='__main__':
    # Connected non-biregular bipartite path, degrees 1,2,2,2,1.
    path=[[1],[0,2],[1,3],[2,4],[3]]
    print('PASS: critical exact absorption probabilities on',test_irregular_critical(path,[0,2,4],tuple(map(F,('1/2','1/4','1/2','1')))),'nonabsorbing states of a non-biregular path')
