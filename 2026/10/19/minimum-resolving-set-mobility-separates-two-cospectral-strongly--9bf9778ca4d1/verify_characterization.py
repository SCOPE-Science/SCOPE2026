"""Independent pair-separation-mask proof and explicit basis classification.
All loops have exact finite bounds; standard library only.
"""
from itertools import combinations
from collections import Counter

V=tuple((a,b) for a in range(4) for b in range(4))
STEPS={(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}
P=list(combinations(range(16),2));ALL=(1<<len(P))-1

def check(kind):
    edges={(i,j) for i in range(16) for j in range(i+1,16)
        if ((V[i][0]==V[j][0] or V[i][1]==V[j][1]) if kind=='rook'
        else (((V[i][0]-V[j][0])%4,(V[i][1]-V[j][1])%4) in STEPS))}
    A=[set() for _ in range(16)]
    for u,v in edges: A[u].add(v); A[v].add(u)
    # Independently obtain shortest-path distances by breadth-first search.
    from collections import deque
    D=[]
    for src in range(16):
        dis={src:0}; q=deque([src])
        while q:
            u=q.popleft()
            for v in A[u]:
                if v not in dis:dis[v]=dis[u]+1;q.append(v)
        assert len(dis)==16 and max(dis.values())==2
        D.append(dis)
    covers=[]
    for z in range(16):
        b=0
        for p,(u,v) in enumerate(P):
            if D[z][u]!=D[z][v]:b|=(1<<p)
        covers.append(b)
    def resolves(s):
        x=0
        for z in s:x|=covers[z]
        return x==ALL
    B={s for s in combinations(range(16),4) if resolves(s)}
    assert all(not resolves(s) for k in (1,2,3) for s in combinations(range(16),k))
    if kind=='rook':
        predicted=set()
        for r in range(4):
            for c in range(4):
                for unused_row in range(4):
                    if unused_row==r:continue
                    for unused_col in range(4):
                        if unused_col==c:continue
                        s=tuple(sorted({4*r+y for y in range(4) if y not in (c,unused_col)}|
                                       {4*x+c for x in range(4) if x not in (r,unused_row)}))
                        assert len(s)==4
                        predicted.add(s)
        assert len(predicted)==144 and B==predicted
        families=Counter()
        for s in B:
            rr=Counter(V[i][0] for i in s);cc=Counter(V[i][1] for i in s)
            hr=next(r for r in rr if rr[r]==2)
            hc=next(c for c in cc if cc[c]==2)
            families[(hr,hc)]+=1
        assert len(families)==16 and set(families.values())=={9}
        print('rook 144 bases as 16 central-row/column families, 9 each')
    else:
        reps=[((0,0),(0,1),(2,0),(2,3)),
              ((0,0),(0,2),(1,0),(3,2)),
              ((0,0),(0,2),(1,1),(3,1))]
        predicted=set();orbit_sizes=[]
        for rep in reps:
            o={tuple(sorted(4*((x+a)%4)+((y+b)%4) for x,y in rep))
               for a in range(4) for b in range(4)}
            orbit_sizes.append(len(o));predicted|=o
        assert orbit_sizes==[16,16,16] and len(predicted)==48 and B==predicted
        assert all(sum(j in A[i] for i,j in combinations(s,2))==2 for s in B)
        assert all(len(set(s)&set(t))<=2 for s,t in combinations(sorted(B),2))
        print('shrikhande 48 bases in 3 disjoint translation orbits of size 16; pairwise overlaps <=2')
    # A second independent route to the two-exchange statistics, operating on
    # the basis bitmasks rather than on stored tuples of vertices.
    bits=[sum(1<<i for i in b) for b in sorted(B)]
    aj=[set() for _ in bits]
    for i in range(len(bits)):
        for j in range(i+1,len(bits)):
            if (bits[i]&bits[j]).bit_count()==2:
                aj[i].add(j); aj[j].add(i)
    from collections import deque
    n=len(bits); diam=0
    for src in range(n):
        D={src:0}; Q=deque([src])
        while Q:
            v=Q.popleft()
            for w in aj[v]:
                if w not in D:D[w]=D[v]+1;Q.append(w)
        assert len(D)==n
        diam=max(diam,max(D.values()))
    assert diam==3
    assert {len(a) for a in aj}==({26} if kind=='rook' else {10})
    assert sum(map(len,aj))//2==(1872 if kind=='rook' else 240)
    print(kind,'two-exchange connected regular-degree',len(aj[0]),'diameter',diam)
    return B

if __name__=='__main__':
    check('rook');check('shrikhande');print('INDEPENDENT_VERIFY_OK')
