"""Exact checks for the tree shortcut purchase threshold."""
from fractions import Fraction as F
from random import Random
from collections import deque

def mat_inv(a):
    n=len(a)
    q=[[F(a[i][j]) for j in range(n)]+[F(int(i==j)) for j in range(n)] for i in range(n)]
    for j in range(n):
        k=next((i for i in range(j,n) if q[i][j]),None)
        assert k is not None
        q[j],q[k]=q[k],q[j]
        z=q[j][j]
        q[j]=[v/z for v in q[j]]
        for i in range(n):
            if i!=j:
                z=q[i][j]
                if z: q[i]=[q[i][h]-z*q[j][h] for h in range(2*n)]
    return [row[n:] for row in q]

def side(N,edges,a,b):
    ad=[[] for _ in range(N)]
    for x,y in edges:
        if (x,y)==(a,b) or (x,y)==(b,a):continue
        ad[x].append(y);ad[y].append(x)
    todo=[a];seen={a}
    for x in todo:
        for y in ad[x]:
            if y not in seen:seen.add(y);todo.append(y)
    return seen

def path(N,edges,u,v):
    ad=[[] for _ in range(N)]
    for i,(a,b) in enumerate(edges):ad[a].append((b,i));ad[b].append((a,i))
    par={u:(-1,-1)};queue=deque([u])
    while queue and v not in par:
        a=queue.popleft()
        for b,i in ad[a]:
            if b not in par:par[b]=(a,i);queue.append(b)
    p=[];cur=v
    while cur!=u:
        a,i=par[cur];p.append(i);cur=a
    return p[::-1]

def exact_case(N,edges,u,v,ks):
    P=path(N,edges,u,v)
    assert len(P)>1
    sides={i:side(N,edges,*edges[i]) for i in range(N-1)}
    counts={i:len(sides[i]) for i in range(N-1)}
    b={i:counts[i]*(N-counts[i]) for i in range(N-1)}
    costs={i:b[i]*ks[i]**2 for i in range(N-1)}
    S=sum(b[i]*ks[i] for i in range(N-1))
    g={i:F(1,ks[i]*S) for i in range(N-1)}
    assert sum(costs[i]*g[i] for i in range(N-1))==1
    L=[[F(0) for _ in range(N)] for __ in range(N)]
    for i,(a,c) in enumerate(edges):
        w=g[i];L[a][a]+=w;L[c][c]+=w;L[a][c]-=w;L[c][a]-=w
    M=mat_inv([[L[i][j]+F(1,N) for j in range(N)] for i in range(N)])
    K=N*(sum(M[i][i] for i in range(N))-1)
    assert K==S*S,(K,S*S)
    # Compare cut-size formula to potential variance (edge sides must all contain u)
    h=[sum(ks[e] for e in P if a in (side(N,edges,*edges[e]) if u in side(N,edges,*edges[e]) else set(range(N))-side(N,edges,*edges[e]))) for a in range(N)]
    mean=F(sum(h),N)
    theta=N*sum((a-mean)**2 for a in h)
    bvec=[F(int(a==u)-int(a==v)) for a in range(N)]
    psi=[sum(M[i][j]*bvec[j] for j in range(N)) for i in range(N)]
    d=F(N)*sum(q*q for q in psi)
    assert d==S*S*theta,(d,S*S*theta)
    # strict universal price envelope
    C=sum(costs[e] for e in P)
    # upper bound integer via squared roots: sqrt(c_e)=sqrt(b_e)*k_e generally irrational; use numeric only
    assert theta>C
    # exact cut cross formula, using rational identity when costs=b_e*k_e**2
    ordered=[]
    for e in P:
        U=side(N,edges,*edges[e]);U=U if u in U else set(range(N))-U
        ordered.append((len(U),e))
    assert [x for x,_ in ordered]==sorted(x for x,_ in ordered)
    theta2=sum(costs[e] for e in P)
    for x,(si,e) in enumerate(ordered):
        for sj,f in ordered[x+1:]:theta2+=2*ks[e]*ks[f]*si*(N-sj)
    assert theta2==theta,(theta2,theta)
    # superadditivity for every intermediate path cut
    for split in range(1,len(P)):
        left=P[:split];right=P[split:]
        def value(E):
            q=[sum(ks[e] for e in E if a in (side(N,edges,*edges[e]) if u in side(N,edges,*edges[e]) else set(range(N))-side(N,edges,*edges[e]))) for a in range(N)]
            mu=F(sum(q),N)
            return N*sum((z-mu)**2 for z in q)
        assert theta>value(left)+value(right)
    return theta

rng=Random(271828)
ct=0
for N in range(3,10):
    for j in range(22):
        edges=[(i,rng.randrange(i)) for i in range(1,N)]
        pairs=[(a,b) for a in range(N) for b in range(a+1,N) if tuple((a,b)) not in [tuple(sorted(e)) for e in edges]]
        if not pairs:continue
        u,v=rng.choice(pairs)
        ks=[rng.randrange(1,5) for _ in edges]
        exact_case(N,edges,u,v,ks)
        ct+=1
# Full finite two-hop extremal comparison in squared correlation (rational).
for N in range(3,50):
    values=[F(a*b,(N-a)*(N-b)) for a in range(1,N-1) for b in range(1,N-a)]
    assert min(values)==F(1,(N-1)**2)
    a=(N-1)//2
    b=N-1-a
    assert max(values)==F(a*b,(N-a)*(N-b))
print('VERIFY_OK',ct,'exact tree/chord KKT tests; 47 finite two-hop extremal checks')
