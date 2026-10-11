#!/usr/bin/env python3
import itertools, math

SQ2=math.sqrt(2.0)

def solve(A,b,eps=1e-11):
    n=len(A)
    M=[list(map(float,A[i]))+[float(b[i])] for i in range(n)]
    for c in range(n):
        p=max(range(c,n),key=lambda r:abs(M[r][c]))
        if abs(M[p][c])<eps:
            return None
        M[c],M[p]=M[p],M[c]
        q=M[c][c]
        M[c]=[x/q for x in M[c]]
        for r in range(n):
            if r==c: continue
            q=M[r][c]
            if abs(q)>eps:
                M[r]=[M[r][j]-q*M[c][j] for j in range(n+1)]
    return [M[i][-1] for i in range(n)]

def graph(n,roots):
    nodes=list(range(-n,0))+[0]+list(range(1,n+1))
    arcs=[]
    signs={i:[] for i in range(1,n+1)}
    for root in roots:
        supp=[i+1 for i,a in enumerate(root) if a]
        for i in supp:
            signs[i].append(root[i-1])
        if len(supp)==1:
            i=supp[0]; s=root[i-1]
            arcs += [(-s*i,0,1.0),(0,s*i,1.0)]
        elif len(supp)==2:
            i,j=supp; si=root[i-1]; sj=root[j-1]
            arcs += [(-sj*j,si*i,SQ2),(-si*i,sj*j,SQ2)]
        else:
            raise AssertionError('root support')
    indeg={v:0 for v in nodes}; outdeg={v:0 for v in nodes}
    outgoing={v:[] for v in nodes}
    for u,v,w in arcs:
        indeg[v]+=1; outdeg[u]+=1; outgoing[u].append((v,w))
    sources=[v for v in nodes if v!=0 and indeg[v]==0]
    sinks=[v for v in nodes if v!=0 and outdeg[v]==0]
    q=[v for v in nodes if indeg[v]==0]
    indeg2=dict(indeg); topo=[]
    while q:
        u=q.pop(); topo.append(u)
        for v,w in outgoing[u]:
            indeg2[v]-=1
            if indeg2[v]==0: q.append(v)
    assert len(topo)==len(nodes), 'cycle in test data'
    d={v:float('-inf') for v in nodes}
    for s in sources: d[s]=0.0
    for u in topo:
        if not math.isfinite(d[u]): continue
        for v,w in outgoing[u]:
            d[v]=max(d[v],d[u]+w)
    H=max(d[t] for t in sinks)
    pmax=[i for i in range(1,n+1) if all(s>0 for s in signs[i])]
    nmax=[i for i in range(1,n+1) if all(s<0 for s in signs[i])]
    return arcs,sources,sinks,d,H,pmax,nmax

def formula(n,roots):
    arcs,sources,sinks,d,H,pmax,nmax=graph(n,roots)
    r=2/(2+H)
    c=[r*(d[i]-d[-i])/2 for i in range(1,n+1)]
    return r,c,pmax,nmax

def brute(n,roots):
    _,_,_,_,_,pmax,nmax=graph(n,roots)
    rows=[]
    # variables c_1,...,c_n,r; rows encode lhs >= rhs
    for root in roots:
        norm=math.sqrt(sum(a*a for a in root))
        row=list(root)+[-norm]
        rows.append((row,0.0))
    for i in pmax:
        row=[0.0]*(n+1); row[i-1]=-1.0; row[-1]=-1.0
        rows.append((row,-1.0))
    for i in nmax:
        row=[0.0]*(n+1); row[i-1]=1.0; row[-1]=-1.0
        rows.append((row,-1.0))
    row=[0.0]*(n+1); row[-1]=1.0
    rows.append((row,0.0))
    best=-1.0
    for active in itertools.combinations(range(len(rows)),n+1):
        z=solve([rows[j][0] for j in active],[rows[j][1] for j in active])
        if z is None: continue
        if all(sum(a*x for a,x in zip(row,z)) >= rhs-2e-9 for row,rhs in rows):
            best=max(best,z[-1])
    return best

cases=[
    (2,[]),
    (2,[(-1,1)]),
    (3,[(-1,1,0),(0,-1,1)]),
    (3,[(1,0,0),(-1,1,0),(0,-1,1)]),
    (2,[(1,1),(-1,1)]),
    (3,[(1,1,0),(0,-1,1)]),
    (3,[(-1,1,0),(0,1,1)]),
    (3,[(1,0,0),(0,-1,1)]),
]

for n,roots in cases:
    r,c,pmax,nmax=formula(n,roots)
    rb=brute(n,roots)
    assert abs(r-rb)<=2e-8*max(1.0,r),(n,roots,r,rb)
    for root in roots:
        norm=math.sqrt(sum(a*a for a in root))
        assert sum(a*x for a,x in zip(root,c)) >= r*norm-2e-9
    for i in pmax:
        assert c[i-1] <= 1-r+2e-9
    for i in nmax:
        assert c[i-1] >= -1+r-2e-9

print(f'VERIFY_OK signed-order-inradius cases={len(cases)} active_set_lp=yes')
