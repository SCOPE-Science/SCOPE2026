"""Standalone finite checks for a high-girth graph cut-complex theorem.
Run with Python 3 standard library: python3 verify.py
"""
from itertools import combinations
from math import comb
from collections import deque


def cycle(n):
    return n, [(i,(i+1)%n) for i in range(n)]


def path(n):
    return n, [(i,i+1) for i in range(n-1)]


def hex_chain(m):
    side=2*m+1
    edges=[(j*side+i,j*side+i+1) for j in range(2) for i in range(side-1)]
    edges.extend((i,side+i) for i in range(0,side,2))
    return 2*side,edges


def theta(a,b,c):
    # internally vertex-disjoint paths between 0 and 1
    edges=[];new=2
    for ell in (a,b,c):
        prev=0
        for _ in range(ell-1):
            edges.append((prev,new));prev=new;new+=1
        edges.append((prev,1))
    return new,edges


def petersen():
    edges=[(i,(i+1)%5) for i in range(5)]
    edges.extend((i,5+i) for i in range(5))
    edges.extend((5+i,5+((i+2)%5)) for i in range(5))
    return 10,edges


def heawood():
    # Incidence graph of the Fano plane: seven points and seven lines.
    lines=[(i,(i+1)%7,(i+3)%7) for i in range(7)]
    return 14,[(p,7+j) for j,line in enumerate(lines) for p in line]


def nbhood(n,edges):
    nb=[set() for _ in range(n)]
    for u,v in edges:
        assert u!=v and 0<=u<n and 0<=v<n
        nb[u].add(v);nb[v].add(u)
    return nb


def connected(vertices,nb):
    vertices=set(vertices);seen={next(iter(vertices))};todo=list(seen)
    while todo:
        u=todo.pop()
        for v in nb[u] & vertices:
            if v not in seen:
                seen.add(v);todo.append(v)
    return len(seen)==len(vertices)


def girth(n,nb):
    best=n+1
    for root in range(n):
        dist={root:0};parent={root:-1};todo=deque([root])
        while todo:
            u=todo.popleft()
            for v in nb[u]:
                if v not in dist:
                    dist[v]=dist[u]+1;parent[v]=u;todo.append(v)
                elif parent[u]!=v:
                    best=min(best,dist[u]+dist[v]+1)
    return best


def rank_mod2(vectors):
    piv={};rank=0
    for val in vectors:
        while val:
            bit=val.bit_length()-1
            if bit in piv:val^=piv[bit]
            else:piv[bit]=val;rank+=1;break
    return rank


def verify_case(label,G,k):
    n,edges=G;nb=nbhood(n,edges)
    assert 3<=k<=n-4 and girth(n,nb)>=k+2,(label,k,'girth')
    connected_k=[set(S) for S in combinations(range(n),k) if connected(S,nb)]
    connected_idx={frozenset(s) for s in connected_k}
    # Independently test the candidate private-face property.
    witnesses=set()
    for U in connected_k:
        assert sum(len(nb[v]&U) for v in U)==2*(k-1)
        for v in U:
            S=U-{v}
            if not connected(S,nb):
                assert sum(frozenset(S|{z}) in connected_idx for z in range(n) if z not in S)==1,(label,k,U,S)
                witnesses.add(frozenset(S));break
        else:raise AssertionError(('no private face',label,k,U))
    assert len(witnesses)==len(connected_k)
    # Independently test that Alexander dual has no faces of size k+1.
    for W in combinations(range(n),k+1):
        assert any(not connected(set(W)-{v},nb) for v in W)
    # Compute full mod-2 chain boundary ranks for Alexander dual.
    faces=[list(combinations(range(n),r)) for r in range(1,k)]
    faces.append([tuple(sorted(s)) for s in connected_k])
    # faces[r-1] consists of simplices with cardinality r.
    ranks={}
    for r in range(2,k+1):
        row={s:i for i,s in enumerate(faces[r-2])}
        vectors=[]
        for simplex in faces[r-1]:
            col=0
            for j in range(r):
                lower=simplex[:j]+simplex[j+1:]
                col^=1<<row[lower]
            vectors.append(col)
        ranks[r]=rank_mod2(vectors)
    assert ranks[k]==len(connected_k), (label,k,'rank',ranks[k],len(connected_k))
    predicted=comb(n-1,k-1)-len(connected_k)
    for r in range(1,k-1):
        beta=len(faces[r-1])-ranks.get(r,0)-ranks.get(r+1,0)
        if r==1:beta-=1 # reduced
        assert beta==0,(label,k,r,beta)
    betatop=len(faces[k-2])-ranks.get(k-1,0)-ranks[k]
    assert betatop==predicted,(label,k,betatop,predicted)
    if k==4:
        structural=sum((len(nb[u])-1)*(len(nb[v])-1) for u,v in edges)
        structural+=sum(comb(len(nb[v]),3) for v in range(n) if len(nb[v])>=3)
        assert structural==len(connected_k),(label,k,'four-set count')
    print('PASS',label,'n',n,'k',k,'girth',girth(n,nb),'connected_k',len(connected_k),'top_rank',predicted,flush=True)


def main():
    cases=[('C9',cycle(9),range(3,6)),('C10',cycle(10),range(3,7)),
           ('P10',path(10),range(3,7)),('Hex2',hex_chain(2),(3,4)),
           ('Hex3',hex_chain(3),(4,)),('Theta334',theta(3,3,4),(3,4)),
           ('Petersen',petersen(),(3,)),('Heawood',heawood(),(3,4)),
           ('Empty10',(10,[]),(3,4,5,6))]
    count=0
    for label,G,ks in cases:
        for k in ks:
            if girth(G[0],nbhood(*G))>=k+2:
                verify_case(label,G,k);count+=1
    print('VERIFY_OK',count,'complete finite graph/parameter checks')

if __name__=='__main__':main()
