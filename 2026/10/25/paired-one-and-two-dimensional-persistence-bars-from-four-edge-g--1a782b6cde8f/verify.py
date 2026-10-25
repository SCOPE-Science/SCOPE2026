"""Reproduce finite checks for a four-edge-ear graph-metric Rips theorem.
Python 3, standard library only. Not a proof for arbitrary graphs.
"""
from itertools import combinations
from collections import deque

def construct(h_edges,pairs):
    old=sorted({v for e in h_edges for v in e}); E={frozenset(e) for e in h_edges}; ears=[]; j=max(old)+1
    for x,y in pairs:
        b,c,d=range(j,j+3);j+=3
        for u,v in [(x,b),(b,c),(c,d),(d,y)]: E.add(frozenset((u,v)))
        ears.append((x,b,c,d,y))
    return old,E,ears

def distances(E):
    vertices=set().union(*E); N={v:set() for v in vertices}
    for e in E:
        a,b=tuple(e);N[a].add(b);N[b].add(a)
    D={}
    for v in vertices:
        d={v:0}; Q=deque([v]);
        while Q:
            u=Q.popleft()
            for w in N[u]:
                if w not in d:d[w]=d[u]+1;Q.append(w)
        assert len(d)==len(vertices)
        D[v]=d
    return D

def nbr(D,verts,r,v):return {u for u in verts if u!=v and D[u][v]<=r}
def dominated(D,verts,r,v,a):
    return v!=a and v in verts and a in verts and all(D[a][w]<=r for w in nbr(D,verts,r,v))
def gf2_rank(columns):
    piv={}
    for x in columns:
        while x:
            b=x.bit_length()-1
            if b in piv:x^=piv[b]
            else:piv[b]=x;break
    return len(piv)
def bettis(D,r):
    vs=sorted(D);faces={0:[(v,) for v in vs]}
    for d in range(1,len(vs)):
        prev=faces[d-1]; higher=[]
        for f in prev:
            for v in vs:
                if v>f[-1] and all(D[v][u]<=r for u in f):higher.append(f+(v,))
        if not higher:break
        faces[d]=higher
    ranks={0:0}
    for d in range(1,len(faces)):
        rows={f:i for i,f in enumerate(faces[d-1])}
        columns=[]
        for face in faces[d]:
            c=0
            for i in range(len(face)):c ^= 1<<rows[face[:i]+face[i+1:]]
            columns.append(c)
        ranks[d]=gf2_rank(columns)
    return [len(faces[d])-ranks[d]-ranks.get(d+1,0) for d in range(len(faces))]
def check(h,pairs):
    old,E,ears=construct(h,pairs); D=distances(E);Dh=distances({frozenset(e) for e in h});
    assert all(D[x][y]==Dh[x][y] for x in old for y in old)
    for x,b,c,d,y in ears:
        assert Dh[x][y]==2
        a=next(v for v in old if Dh[x][v]==1 and Dh[v][y]==1)
        assert nbr(D,D.keys(),2,c)=={x,b,d,y}
        assert all(D[u][v]<=2 for u,v in [(x,b),(b,d),(d,y),(y,x)])
        assert all(D[u][v]>2 for u,v in [(x,d),(b,y)])
        assert all(D[u][v]<=2 for u,v in [(a,x),(a,b),(a,d),(a,y)])
        assert all(D[u][v]<=3 for u,v in combinations((x,b,c,d,y,a),2))
    centers={e[2] for e in ears}; remain=set(D)-centers
    for x,b,c,d,y in ears:
        a=next(v for v in old if Dh[x][v]==1 and Dh[v][y]==1)
        assert dominated(D,set(D),3,c,a),('center r3',x,y)
        assert dominated(D,remain,2,b,a),('end b r2',x,y)
        assert dominated(D,remain,2,d,a),('end d r2',x,y)
        assert dominated(D,remain,3,b,a),('end b r3',x,y)
        assert dominated(D,remain,3,d,a),('end d r3',x,y)
    for r in [1,2,3]:
        A=bettis(D,r);B=bettis(Dh,r)
        pad=lambda xs,n:xs+[0]*(n-len(xs))
        l=max(len(A),len(B),3);A,B=pad(A,l),pad(B,l)
        expected=B[:]
        if r==1:expected[1]+=len(ears)
        if r==2:expected[2]+=len(ears)
        assert A==expected,(r,A,expected)
    return f'{len(old)} old, {len(ears)} ears, {len(D)} total; OK'

if __name__=='__main__':
    cases=[
        ([(0,1),(1,2)],[(0,2)]),
        ([(0,1),(1,2)],[(0,2),(0,2)]),
        ([(0,1),(1,2),(2,3),(3,4),(4,0)],[(0,2)]),
        ([(0,1),(1,2),(2,3),(3,4),(4,0)],[(0,2),(1,3)]),
        ([(0,1),(1,2),(2,3),(3,0),(0,2)],[(1,3),(1,3)])
    ]
    for h,p in cases:print(check(h,p))
    print('CHECKS_PASS')
