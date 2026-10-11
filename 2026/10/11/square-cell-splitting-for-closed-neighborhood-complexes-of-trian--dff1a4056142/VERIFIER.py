"""Exhaustive finite checks for closed-neighborhood collapse onto 4-cycle sphere boundaries."""
from itertools import combinations
from collections import defaultdict

def build(n, edges):
    adj=[set() for _ in range(n)]
    for u,v in edges:
        assert u!=v
        adj[u].add(v);adj[v].add(u)
    for v in range(n):
        for a,b in combinations(adj[v],2):
            assert b not in adj[a], 'triangle present'
    for a,b in combinations(range(n),2):
        assert len(adj[a]&adj[b])<=2,'K2,3 present'
    return adj

def allfaces(adj):
    out=set()
    for v in range(len(adj)):
        ball=sorted(adj[v]|{v})
        for sz in range(1,len(ball)+1):
            for F in combinations(ball,sz):out.add(frozenset(F))
    return out

def squares(adj):
    out=set();n=len(adj)
    for a,b in combinations(range(n),2):
        comm=adj[a]&adj[b]
        if len(comm)==2:out.add(frozenset((a,b,*comm)))
    return out

def collapsed(adj):
    faces=allfaces(adj); orig=len(faces); pairs=0
    for k in range(max(map(len,adj)),1,-1):
        for v in range(len(adj)):
            for tup in combinations(sorted(adj[v]),k):
                if k==2 and len(adj[tup[0]]&adj[tup[1]])==2:continue
                F=frozenset(tup); H=F|{v}
                assert F in faces and H in faces, ('missing pair',F,H)
                cofaces=[X for X in faces if X>F]
                assert cofaces==[H],('not free',F,H,cofaces)
                faces.remove(F);faces.remove(H);pairs+=1
    expected={frozenset((u,)) for u in range(len(adj))}
    expected|={frozenset((u,v)) for u in range(len(adj)) for v in adj[u] if u<v}
    sq=squares(adj)
    for cell in sq:
        for k in (2,3):
            for F in combinations(cell,k):expected.add(frozenset(F))
    assert faces==expected,('residual mismatch',len(faces^expected),faces^expected)
    return orig,len(faces),pairs,len(sq)

def grid(m,n):
    edges=[]
    for i in range(m):
        for j in range(n):
            v=i*n+j
            if i+1<m:edges.append((v,v+n))
            if j+1<n:edges.append((v,v+1))
    return build(m*n,edges)

def cube(n):
    return build(2**n,[(v,v^(1<<i)) for v in range(2**n) for i in range(n) if not v&(1<<i)])

def cycle(n):return build(n,[(i,(i+1)%n) for i in range(n)])

def petersen():
    return build(10,[(i,(i+1)%5) for i in range(5)]+[(5+i,5+(i+2)%5) for i in range(5)]+[(i,5+i) for i in range(5)])

def rank_mod2(cols):
    pivots={}
    for x in cols:
        while x:
            j=x.bit_length()-1
            if j in pivots:x^=pivots[j]
            else:pivots[j]=x;break
    return len(pivots)

def betti_faces(faces):
    bydim={d:sorted((tuple(sorted(F)) for F in faces if len(F)==d+1)) for d in range(max(len(F) for F in faces))}
    ranks={}
    for d in range(1,len(bydim)):
        rows={F:i for i,F in enumerate(bydim[d-1])}
        cols=[]
        for F in bydim[d]:
            x=0
            for j in range(len(F)):
                x ^= 1 << rows[F[:j]+F[j+1:]]
            cols.append(x)
        ranks[d]=rank_mod2(cols)
    return [len(bydim[d])-ranks.get(d,0)-ranks.get(d+1,0) - (1 if d==0 else 0) for d in bydim]

def betti2(adj):return betti_faces(allfaces(adj))

def filled_squares(adj):
    faces={frozenset((v,)) for v in range(len(adj))}
    faces|={frozenset((v,u)) for v in range(len(adj)) for u in adj[v] if u<v}
    for sq in squares(adj):
        a,b,c,d=sorted(sq)
        # A diagonal is a nonedge in the graph.
        pairs=[(u,v) for u,v in combinations(sorted(sq),2) if v not in adj[u]]
        assert len(pairs)==2
        u,v=pairs[0]
        faces.add(frozenset((u,v)))
        for w in sq-{u,v}:faces.add(frozenset((u,v,w)))
    return faces

if __name__=='__main__':
    trials=0
    for m in range(2,5):
        for n in range(2,7):
            A=grid(m,n);info=collapsed(A);trials+=1
            if m*n<=16:
                bb=betti2(A)
                assert bb[0]==0 and bb[1]==0 and bb[2]==(m-1)*(n-1) and all(x==0 for x in bb[3:]),(m,n,bb)
            print('GRID',m,n,info)
    for n in range(1,5):
        A=cube(n);info=collapsed(A);trials+=1
        if n<=3:
            bb=betti2(A); q=info[3];b=sum(map(len,A))//2-len(A)+1
            assert bb[2]==2*q-b if n>=2 else bb[0]==0,(n,bb)
        print('CUBE',n,info)
    for n in range(5,13):
        A=cycle(n);info=collapsed(A);trials+=1
        bb=betti2(A);assert bb[1]==1 and sum(bb)==1,(n,bb)
    collapsed(petersen()); trials+=1
    import random
    rng=random.Random(211014)
    accepted=0; attempts=0
    while accepted<90 and attempts<5000:
        attempts+=1
        n=rng.randrange(4,11)
        # Trees and sparse square-rich samples are both tested.
        p=rng.uniform(.13,.35)
        E=[(u,v) for u,v in combinations(range(n),2) if rng.random()<p]
        if not E:continue
        try:A=build(n,E)
        except AssertionError:continue
        visited={0}; todo=[0]
        while todo:
            v=todo.pop()
            for w in A[v]-visited:visited.add(w);todo.append(w)
        if len(visited)<n:continue
        orig,remaining,pairs,q=collapsed(A)
        bb=betti2(A); xx=betti_faces(filled_squares(A))
        bb += [0]*max(0,4-len(bb));xx += [0]*max(0,4-len(xx))
        assert bb[0]==0 and xx[0]==0
        assert bb[1]==xx[1] and bb[2]==xx[2]+q and all(x==0 for x in bb[3:]),(n,E,bb,xx,q)
        accepted+=1;trials+=1
    assert accepted==90
    print('VERIFY_OK',trials,'graph instances; 90 seeded random admissible connected graphs with homology-splitting tests; complete free-face and residual tests')
