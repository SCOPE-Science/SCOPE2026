"""Independent, standard-library verifier for finite Rips complexes of L(GP(10,2)).
Run with Python >=3.9: python verify_icosidodeca_rips.py.
Every collapsed pair is checked to be an elementary simplicial collapse.
"""
from collections import defaultdict, Counter, deque
from itertools import combinations
from heapq import heappush, heappop

def data():
    n=10
    edges=set()
    def add(a,b): edges.add(tuple(sorted((a,b))))
    for i in range(n):
        add(i,(i+1)%n)
        add(i,10+i)
        add(10+i,10+(i+2)%n)
    E=sorted(edges)
    assert len(E)==30
    adj=[set() for _ in E]
    for i,j in combinations(range(len(E)),2):
        if set(E[i]).intersection(E[j]):
            adj[i].add(j);adj[j].add(i)
    dist=[]
    for start in range(len(E)):
        ds=[-1]*len(E);ds[start]=0;q=deque([start])
        while q:
            x=q.popleft()
            for y in sorted(adj[x]):
                if ds[y]<0:ds[y]=ds[x]+1;q.append(y)
        dist.append(ds)
    assert set(map(max,dist))=={5}
    return E,dist

def faces_at(dist,r):
    n=len(dist)
    adj=[{j for j in range(n) if j!=i and dist[i][j]<=r} for i in range(n)]
    faces=set()
    def recurse(prefix,candidates):
        for j,v in enumerate(candidates):
            f=prefix+(v,);faces.add(f)
            recurse(f,[w for w in candidates[j+1:] if w in adj[v]])
    recurse((),list(range(n)))
    return faces

def boundary(face):
    return [(face[:i]+face[i+1:],1 if i%2==0 else -1) for i in range(len(face))]

def free_collapse_pass(live):
    up={f:set() for f in live}
    for c in live:
        if len(c)>1:
            for f,_ in boundary(c):
                assert f in up
                up[f].add(c)
    queue=[]
    def nominate(f):
        if f in live and len(up[f])==1:
            c=next(iter(up[f]))
            if c in live and len(up[c])==0:
                heappush(queue,(len(f),f,c))
    for f in live:nominate(f)
    pairs=[]
    while queue:
        _,f,c=heappop(queue)
        if f not in live or c not in live or len(up[f])!=1 or c not in up[f] or up[c]:
            continue
        assert len(c)==len(f)+1 and f in dict(boundary(c))
        live.remove(f);live.remove(c);pairs.append((f,c))
        for rem in (f,c):
            if len(rem)>1:
                for t,_ in boundary(rem):
                    up[t].discard(rem)
                    nominate(t)
    return pairs

def full_collapse(faces):
    live=set(faces);total=[];passes=0
    while True:
        pairs=free_collapse_pass(live)
        if not pairs:break
        total.extend(pairs);passes+=1
        assert passes<50
    return live,total,passes

def sphere_signs(live):
    bydim=Counter(len(f)-1 for f in live)
    tri=sorted(f for f in live if len(f)==3)
    edges={f for f in live if len(f)==2}
    vertices={f[0] for f in live if len(f)==1}
    assert len(tri)*3==len(edges)*2
    assert len(vertices)-len(edges)+len(tri)==2
    E=defaultdict(list)
    for t in tri:
        for e,s in boundary(t):E[e].append((t,s))
    assert set(E)==edges and all(len(x)==2 for x in E.values())
    neighboring=defaultdict(list)
    for e,con in E.items():
        (t,a),(u,b)=con
        neighboring[t].append((u,-a*b))
        neighboring[u].append((t,-a*b))
    signs={tri[0]:1};q=deque([tri[0]])
    while q:
        t=q.popleft()
        for u,factor in neighboring[t]:
            x=signs[t]*factor
            if u in signs:assert signs[u]==x
            else:signs[u]=x;q.append(u)
    assert len(signs)==len(tri)
    for v in vertices:
        lk=defaultdict(set)
        for t in tri:
            if v in t:
                a,b=[x for x in t if x!=v]
                lk[a].add(b);lk[b].add(a)
        assert lk and all(len(x)==2 for x in lk.values())
        seen={next(iter(lk))};q=deque(seen)
        while q:
            x=q.popleft()
            for y in lk[x]:
                if y not in seen:seen.add(y);q.append(y)
        assert len(seen)==len(lk)
    return signs,bydim

def transfer(z,pairs):
    z=dict(z)
    for f,c in pairs:
        if len(f)==3:
            coefficient=z.pop(f,0)
            if coefficient:
                terms=dict(boundary(c));u=terms[f]
                assert abs(u)==1
                for g,sign in terms.items():
                    if g!=f:
                        z[g]=z.get(g,0)-coefficient*u*sign
                        if z[g]==0:z.pop(g)
        elif len(c)==3:
            z.pop(c,None)
    return z

def main():
    E,dist=data()
    print('graph=GP(10,2)_line_graph vertices=30 edges=60 diameter=5')
    r1=faces_at(dist,1)
    assert Counter(len(x)-1 for x in r1)=={0:30,1:60,2:20}
    tri=[f for f in r1 if len(f)==3]
    count=Counter(e for t in tri for e,_ in boundary(t))
    assert len(count)==60 and all(x==1 for x in count.values())
    print('scale1: face_vector=(30,60,20),20 disjoint triangle-edge collapses, graph rank=11')
    F2=faces_at(dist,2)
    K2,pairs2,passes2=full_collapse(F2)
    z2,d2=sphere_signs(K2)
    assert d2=={0:16,1:42,2:28} and len(pairs2)==468
    assert len(F2)==1022
    print('scale2: original_f=(30,180,380,330,102) elementary_pairs=%d passes=%d residue=(16,42,28) S2'%(len(pairs2),passes2))
    F3=faces_at(dist,3)
    K3,pairs3,passes3=full_collapse(F3)
    z3,d3=sphere_signs(K3)
    assert d3=={0:16,1:42,2:28} and len(pairs3)==(15966-86)//2
    zz=transfer(z2,pairs3)
    assert set(zz).issubset(set(z3)) and len(zz)==len(z3)
    degrees={zz[t]*z3[t] for t in z3}
    assert degrees in ({1},{-1}), degrees
    print('scale3: original_f=(30,300,1340,3150,4374,3800,2100,720,140,12) elementary_pairs=%d passes=%d residue=(16,42,28) S2'%(len(pairs3),passes3))
    print('inclusion H2(scale2)->H2(scale3) integer_degree=%d'%(next(iter(degrees))))
    unmatched={}
    for i in range(30):
        remote=[j for j in range(30) if dist[i][j]>4]
        assert len(remote)==1
        unmatched[i]=remote[0]
    assert all(unmatched[unmatched[i]]==i for i in unmatched)
    assert len({tuple(sorted((i,unmatched[i]))) for i in unmatched})==15
    print('scale4: complement=15_disjoint_edges, crosspolytope_boundary=S14')
    print('scale5: full_29_simplex, contractible')
    print('integral_barcodes: H0_reduced 29x[0,1); H1 11x[1,2); H2 1x[2,4); H14 1x[4,5)')
    print('VERIFIED_OK')

if __name__=='__main__':main()
