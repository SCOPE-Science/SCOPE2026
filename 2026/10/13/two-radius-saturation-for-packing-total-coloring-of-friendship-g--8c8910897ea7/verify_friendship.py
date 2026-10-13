"""Independent finite checks of distance thresholds on friendship graph total-elements.

Run: python3 verify_friendship.py
No external dependencies.
"""
from collections import deque


def graph(n):
    # Shared vertex 0; triangle i has vertices 2*i+1 and 2*i+2.
    nv = 2*n+1
    edges = []
    for i in range(n):
        a,b = 2*i+1,2*i+2
        edges.extend([(0,a),(0,b),(a,b)])
    elements = [('v',j) for j in range(nv)] + [('e',i) for i in range(len(edges))]
    H = [set() for _ in elements]
    def adj(i,j):
        H[i].add(j);H[j].add(i)
    for i in range(nv):
        for j in range(i+1,nv):
            if (i,j) in edges or (j,i) in edges: adj(i,j)
    for ei,ab in enumerate(edges):
        for endpoint in ab: adj(nv+ei,endpoint)
        for ej,cd in enumerate(edges[:ei]):
            if set(ab)&set(cd): adj(nv+ei,nv+ej)
    distances=[]
    for i in range(len(H)):
        d=[999]*len(H); d[i]=0
        Q=deque([i])
        while Q:
            x=Q.popleft()
            for y in H[x]:
                if d[y]==999:
                    d[y]=d[x]+1;Q.append(y)
        assert max(d)<999
        distances.append(d)
    return nv,edges,elements,distances


def construction(n,q):
    nv,edges,els,D=graph(n)
    N=len(els)
    c={}
    if n==1:
        c[nv+0]=1;c[2]=1
    elif q==0:
        c[0]=1
        for i in range(n):c[nv+3*i+2]=1
    else:
        c[nv]=1                 # First spoke edge (0,a_1).
        for i in range(n): c[2*i+2]=1 # One outer vertex per triangle.
        if q==1:
            for i in range(n):c[nv+3*i+2]=2
        else:
            c[1]=2                 # Outer vertex a_1.
            c[3]=3                 # Outer vertex a_2.
            c[nv+2]=3              # First rim edge.
            for i in range(1,n): c[nv+3*i+2]=2
    i=2 if n==1 or q==0 else (3 if q==1 else 4)
    for x in range(N):
        if x not in c: c[x]=i; i+=1
    used=max(c.values())
    expected=(5 if n==1 else 4*n+1 if q==0 else 3*n+2 if q==1 else 3*n+1)
    assert used==expected,(n,q,used,expected)
    assert set(c)==set(range(N))
    assert set(c.values())==set(range(1,used+1))
    for x in range(N):
        for y in range(x+1,N):
            if c[x]!=c[y]:continue
            a=1 if c[x]==1 else 2 if c[x]<=q+1 else 3
            assert D[x][y]>a,(n,q,x,y,c[x],D[x][y],a)
    return used


def check_endpoint_distance(n):
    nv,edges,_,D=graph(n)
    G=[set() for _ in range(nv)]
    for u,v in edges: G[u].add(v);G[v].add(u)
    DV=[]
    for u in range(nv):
        d=[999]*nv; d[u]=0; queue=deque([u])
        while queue:
            x=queue.popleft()
            for y in G[x]:
                if d[y]==999: d[y]=d[x]+1;queue.append(y)
        DV.append(d)
    for x in range(len(D)):
        for y in range(x+1,len(D)):
            if x<nv and y<nv: expected=DV[x][y]
            elif x<nv:
                a,b=edges[y-nv]
                expected=min(DV[x][a],DV[x][b])+1
            else:
                a,b=edges[x-nv];c,d=edges[y-nv]
                expected=min(DV[a][c],DV[a][d],DV[b][c],DV[b][d])+1
            assert D[x][y]==expected,(n,x,y,D[x][y],expected)


def exact_independence(D,threshold,allowed=None):
    # Maximum pairwise distance > threshold, via exact branch-and-bound.
    V=list(range(len(D))) if allowed is None else sorted(allowed)
    # Candidate masks in the allowed-vertex ordering.
    neighbors=[]
    for i,x in enumerate(V):
        mask=0
        for j,y in enumerate(V):
            if i!=j and D[x][y]<=threshold: mask|=1<<j
        neighbors.append(mask)
    best=0
    def search(mask,number):
        nonlocal best
        if not mask:
            if number>best:best=number
            return
        if number+mask.bit_count()<=best:return
        # Pivot: most incompatibilities among current candidates.
        s=mask;choice=-1;score=-1
        while s:
            v=(s&-s).bit_length()-1;s&=s-1
            z=(neighbors[v]&mask).bit_count()
            if z>score:choice=v;score=z
        bit=1<<choice
        search(mask&~bit&~neighbors[choice],number+1)
        search(mask&~bit,number)
    search((1<<len(V))-1,0)
    return best


if __name__=='__main__':
    for n in range(1,15):
        check_endpoint_distance(n)
        nv,edges,els,D=graph(n)
        if n>1:assert max(max(row) for row in D)==3
        for q in (0,1,2,3,8):construction(n,q)
        print(f'n={n}: constructions OK; q=0,1,2,3,8')
    for n in range(1,7):
        nv,edges,els,D=graph(n)
        i1=exact_independence(D,1)
        i2=exact_independence(D,2)
        J=list(range(nv))+[nv+3*i+j for i in range(n) for j in (0,1)]
        assert all(D[x][y]<=2 for ix,x in enumerate(J) for y in J[ix+1:])
        assert exact_independence(D,1,J)==n+1
        assert i1==n+1,(n,'alpha1',i1)
        assert i2==(1 if n==1 else n),(n,'alpha2',i2)
        print(f'n={n}: maximum distance>1 class={i1}; maximum distance>2 class={i2}')
    print('ALL_CHECKS_PASS')
