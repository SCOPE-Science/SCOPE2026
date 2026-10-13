#!/usr/bin/env python3
"""Exact edge-cycle certificates and spectral-projector checks for line-graph walks."""
from fractions import Fraction as F
from itertools import combinations, product


def Cartesian_edges(factors):
    """Each factor is (number of vertices, list of undirected edges)."""
    dims=[n for n,_ in factors]
    verts=list(product(*(range(n) for n in dims)))
    index={v:i for i,v in enumerate(verts)}
    edges=set()
    for v in verts:
        for j,(n,es) in enumerate(factors):
            for a,b in es:
                if v[j]==a:
                    w=tuple(b if k==j else v[k] for k in range(len(dims)))
                    edges.add(tuple(sorted((index[v],index[w]))))
                elif v[j]==b:
                    w=tuple(a if k==j else v[k] for k in range(len(dims)))
                    edges.add(tuple(sorted((index[v],index[w]))))
    return len(verts),sorted(edges)


def path(n):return n,[(i,i+1) for i in range(n-1)]
def complete(n):return n,list(combinations(range(n),2))
def complete_bipartite(p,q):return p+q,[(u,p+v) for u in range(p) for v in range(q)]


def cycles4(n,edges):
    idx={e:i for i,e in enumerate(edges)}
    near=[set() for _ in range(n)]
    for u,v in edges:near[u].add(v);near[v].add(u)
    found={}
    for u,v in combinations(range(n),2):
        for a,b in combinations(sorted(near[u]&near[v]),2):
            ordered=[tuple(sorted(e)) for e in ((u,a),(a,v),(v,b),(b,u))]
            names=tuple(idx[e] for e in ordered)
            found[frozenset(names)]=names
    return list(found.values())


def certificate(n,edges):
    cycles=cycles4(n,edges)
    sets=[frozenset(c) for c in cycles]
    m=len(edges)
    for i in range(m):
        pairs=[(a,b) for a,b in combinations(range(len(cycles)),2)
               if sets[a] & sets[b]=={i}]
        if not pairs:return len(cycles),False
        c,d=(cycles[j] for j in pairs[0])
        for cyc in (c,d):
            values=[0]*m
            for r,e in enumerate(cyc):values[e]=(-1)**r
            balances=[0]*n
            for e,(u,v) in enumerate(edges):balances[u]+=values[e];balances[v]+=values[e]
            assert not any(balances),('cycle sign',i,cyc)
        x={e:(-1)**r for r,e in enumerate(c)}
        y={e:(-1)**r for r,e in enumerate(d)}
        assert {e:x[e]*y[e] for e in x.keys()&y.keys()}=={i:x[i]*y[i]}
    return len(cycles),True


def rref_null(B):
    rows=len(B); cols=len(B[0]); A=[[F(t) for t in row] for row in B]
    pivots=[]; r=0
    for col in range(cols):
        p=next((p for p in range(r,rows) if A[p][col]),None)
        if p is None:continue
        A[r],A[p]=A[p],A[r]
        t=A[r][col]; A[r]=[x/t for x in A[r]]
        for k in range(rows):
            if k!=r and A[k][col]:
                t=A[k][col]; A[k]=[a-t*b for a,b in zip(A[k],A[r])]
        pivots.append(col);r+=1
        if r==rows:break
    free=[j for j in range(cols) if j not in pivots]
    vecs=[]
    for j in free:
        v=[F(0)]*cols;v[j]=F(1)
        for a,c in enumerate(pivots):v[c]=-A[a][j]
        vecs.append(v)
    return vecs


def invert(M):
    n=len(M)
    A=[[F(x) for x in row]+[F(int(i==j)) for j in range(n)] for i,row in enumerate(M)]
    for j in range(n):
        p=next(i for i in range(j,n) if A[i][j])
        A[j],A[p]=A[p],A[j]
        t=A[j][j]; A[j]=[x/t for x in A[j]]
        for i in range(n):
            if i!=j and A[i][j]:
                t=A[i][j];A[i]=[x-t*y for x,y in zip(A[i],A[j])]
    return [row[n:] for row in A]


def projector_and_psd(n,edges):
    m=len(edges)
    B=[[0]*m for _ in range(n)]
    for j,(u,v) in enumerate(edges):B[u][j]=B[v][j]=1
    basis=rref_null(B); r=len(basis)
    assert r>0
    gram=[[sum(basis[a][i]*basis[b][i] for i in range(m)) for b in range(r)] for a in range(r)]
    ginv=invert(gram)
    v=[[sum(basis[a][i]*ginv[a][b] for a in range(r)) for b in range(r)] for i in range(m)]
    P=[[sum(v[i][b]*basis[b][j] for b in range(r)) for j in range(m)] for i in range(m)]
    assert all(P[i][j]==P[j][i] for i in range(m) for j in range(m))
    assert all(sum(P[i][k]*P[k][j] for k in range(m))==P[i][j] for i in range(m) for j in range(m))
    assert all(sum(B[i][e]*P[e][j] for e in range(m))==0 for i in range(n) for j in range(m))
    # Exact LDL^T certificate for P◦P and its quantitative gap.
    A=[[P[i][j]**2 - (F(1,16*m) if i==j else F(0)) for j in range(m)] for i in range(m)]
    D=[F(0)]*m; L=[[F(0)]*m for _ in range(m)]
    for i in range(m):
        D[i]=A[i][i]-sum(L[i][k]**2*D[k] for k in range(i))
        if D[i]<=0:raise AssertionError(('not positive',i,D[i]))
        L[i][i]=F(1)
        for j in range(i+1,m):
            L[j][i]=(A[j][i]-sum(L[j][k]*L[i][k]*D[k] for k in range(i)))/D[i]
    return r, min(D),sum(P[i][i] for i in range(m))


def run():
    trials=[('cube3',Cartesian_edges([path(2)]*3)),
            ('cube4',Cartesian_edges([path(2)]*4)),
            ('triangle_square',Cartesian_edges([complete(3),path(2),path(2)])),
            ('rectangular_box',Cartesian_edges([path(3),path(2),path(2)])),
            ('biclique33',complete_bipartite(3,3))]
    ec=0;cc=0;pp=0
    for label,(n,edges) in trials:
        c,yes=certificate(n,edges)
        assert yes,(label,'missing edge witness')
        r,ldl,trace=projector_and_psd(n,edges)
        print('EXACT_OK',label,'vertices',n,'edges',len(edges),'four_cycles',c,'flatband_dim',r,'projector_trace',trace,'ldl_first_bound',float(ldl))
        ec+=len(edges);cc+=c;pp+=1
    for d in range(3,8):
        n,edges=Cartesian_edges([path(2)]*d)
        c,yes=certificate(n,edges)
        assert yes
        print('CYCLE_WITNESS_OK','cube_dim',d,'edges',len(edges),'cycles4',c)
        ec+=len(edges);cc+=c
    n,edges=Cartesian_edges([path(2)]*2)
    assert certificate(n,edges)[1] is False
    print('VERIFY_OK exact_projectors',pp,'certificate_edges',ec,'cycle_witnesses',cc,'nonexample_Q2_confirmed')

if __name__=='__main__':run()
