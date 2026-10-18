"""Exact finite verification for the graph-metric Rips filtration of the icosidodecahedral graph.
Run with Python 3.10+; no third-party dependencies.
"""
from collections import Counter, defaultdict, deque
from heapq import heappush, heappop
from pathlib import Path
import json


def dodecahedron():
    # Generalized Petersen GP(10,2): outer vertices 0..9, inner 10..19.
    ee=set()
    for i in range(10):
        for a,b in ((i,(i+1)%10),(i,10+i),(10+i,10+(i+2)%10)):
            ee.add((min(a,b),max(a,b)))
    assert len(ee)==30
    return sorted(ee)


def rectification():
    E=dodecahedron()
    # Vertices of L(G) are the thirty edges of G.
    adj=[set() for _ in E]
    for i,(a,b) in enumerate(E):
        for j,(c,d) in enumerate(E[:i]):
            if len({a,b,c,d})<4:
                adj[i].add(j);adj[j].add(i)
    assert len(adj)==30 and all(len(n)==4 for n in adj)
    dist=[]
    for root in range(30):
        row={root:0};q=deque([root])
        while q:
            i=q.popleft()
            for j in adj[i]:
                if j not in row:
                    row[j]=row[i]+1;q.append(j)
        assert len(row)==30
        dist.append(row)
    assert Counter(d for row in dist for d in row.values())=={0:30,1:120,2:240,3:240,4:240,5:30}
    return E,adj,dist


def vertices(mask):
    return [i for i in range(30) if mask&(1<<i)]


def codimension_one(mask):
    rem=mask
    while rem:
        bit=rem&-rem
        yield mask^bit
        rem^=bit


def simplices(dist,r):
    # Enumerate ALL cliques in the graph with edges of metric length <=r.
    neighbors=[sum(1<<j for j in range(i+1,30) if dist[i][j]<=r) for i in range(30)]
    faces=set()
    def extend(mask,candidates):
        while candidates:
            bit=candidates&-candidates
            candidates^=bit
            i=bit.bit_length()-1
            nxt=mask|bit
            assert nxt not in faces
            faces.add(nxt)
            extend(nxt,candidates&neighbors[i])
    extend(0,(1<<30)-1)
    return faces


def elementary_collapse(faces):
    # Every (f,F) is a genuine simplicial free-face elementary collapse.
    faces=set(faces)
    up={f:set() for f in faces}
    for F in faces:
        if F.bit_count()==1:continue
        for f in codimension_one(F):
            assert f in faces
            up[f].add(F)
    alive=set(faces);queue=[]
    def offer(f):
        if f in alive and len(up[f])==1:
            F=next(iter(up[f]))
            if not up[F]:heappush(queue,(-f.bit_count(),f))
    for f in faces:offer(f)
    matching=[]
    while queue:
        _,f=heappop(queue)
        if f not in alive or len(up[f])!=1:continue
        F=next(iter(up[f]))
        if F not in alive or up[F]:continue
        assert f.bit_count()+1==F.bit_count() and f&F==f
        for removed in (f,F):
            alive.remove(removed)
            for sub in codimension_one(removed):
                if not sub or sub not in alive:continue
                assert removed in up[sub]
                up[sub].remove(removed)
                offer(sub)
                if len(up[sub])==0:
                    for lower in codimension_one(sub):
                        if lower in alive:offer(lower)
        matching.append((f,F))
    for f in alive:
        if f.bit_count()>1:
            assert set(codimension_one(f)) <= alive
    return alive,matching


def boundary_sign(face,sub):
    diff=face^sub
    assert diff and diff&(diff-1)==0 and face&sub==sub
    return (-1)**vertices(face).index(diff.bit_length()-1)


def oriented_sphere(faces):
    by=defaultdict(list)
    for f in faces:by[f.bit_count()].append(f)
    assert not set(by)-{1,2,3}
    V,E,T=(by[1],by[2],by[3])
    assert len(V)-len(E)+len(T)==2
    by_edge=defaultdict(list)
    for t in T:
        for e in codimension_one(t):by_edge[e].append(t)
    assert set(by_edge)==set(E)
    assert all(len(pair)==2 for pair in by_edge.values())
    # A connected closed combinatorial 2-manifold: every vertex link is a cycle.
    for v in V:
        link=defaultdict(set)
        for t in T:
            if v&t:
                a,b=vertices(t^v)
                link[a].add(b);link[b].add(a)
        assert link and all(len(ns)==2 for ns in link.values())
        seen={min(link)};stack=list(seen)
        for a in stack:
            for b in link[a]:
                if b not in seen:seen.add(b);stack.append(b)
        assert len(seen)==len(link)
    signs={min(T):1};q=deque(signs)
    while q:
        t=q.popleft()
        for e in codimension_one(t):
            other=next(s for s in by_edge[e] if s!=t)
            s=-signs[t]*boundary_sign(t,e)*boundary_sign(other,e)
            if other in signs:assert signs[other]==s
            else:signs[other]=s;q.append(other)
    assert len(signs)==len(T)
    assert all(sum(signs[t]*boundary_sign(t,e) for t in by_edge[e])==0 for e in E)
    return signs, (len(V),len(E),len(T))


def project_cycle(cycle,matching):
    # The integral cellular chain retraction for successive free-face collapses.
    c=dict(cycle)
    nonzero_substitutions=0
    for f,F in matching:
        if f.bit_count()==3:
            coefficient=c.pop(f,0)
            if coefficient:
                nonzero_substitutions+=1
                sign=boundary_sign(F,f)
                for h in codimension_one(F):
                    if h==f:continue
                    c[h]=c.get(h,0)-coefficient*boundary_sign(F,h)*sign
                    if not c[h]:del c[h]
        elif F.bit_count()==3:
            # A free edge belongs to just one triangle, so a cycle has zero coefficient there.
            assert not c.get(F,0)
    return c,nonzero_substitutions


def action_on_cycle(cycle,permutation):
    result=defaultdict(int)
    for t,c in cycle.items():
        image=[permutation[i] for i in vertices(t)]
        inverted=sum(a>b for k,a in enumerate(image) for b in image[k+1:])
        s=(-1)**inverted
        target=sum(1<<i for i in image)
        result[target]+=s*c
    return {t:c for t,c in result.items() if c}


def integral_degree(cycle,generator,matching):
    projected,changes=project_cycle(cycle,matching)
    assert set(projected)<=set(generator)
    ratios={projected.get(t,0)*sgn for t,sgn in generator.items()}
    assert len(ratios)==1,ratios
    return next(iter(ratios)),changes


def run():
    E,G,d=rectification()
    ff={};mm={};zz={}
    expected={1:(110,20,70),2:(1022,471,80),3:(15966,7964,38)}
    for r in (1,2,3):
        f=simplices(d,r)
        remainder,pairs=elementary_collapse(f)
        assert (len(f),len(pairs),len(remainder))==expected[r]
        assert len(remainder)+2*len(pairs)==len(f)
        ff[r]=f;mm[r]=pairs
        print('radius',r,'faces',len(f),'collapse_pairs',len(pairs),'remainder_vector',dict(sorted(Counter(s.bit_count() for s in remainder).items())))
        if r==1:
            assert all(x.bit_count()<=2 for x in remainder)
            # This graph is connected and has 30 vertices and 40 edges.
            adj=defaultdict(set)
            for e in remainder:
                if e.bit_count()==2:
                    u,v=vertices(e);adj[u].add(v);adj[v].add(u)
            seen={0};stack=[0]
            for i in stack:
                for j in adj[i]:
                    if j not in seen:seen.add(j);stack.append(j)
            assert len(seen)==30 and len(adj)==30 and len([x for x in remainder if x.bit_count()==2])==40
        else:
            zz[r],vec=oriented_sphere(remainder)
            assert vec==({2:(15,39,26),3:(8,18,12)}[r])
    degree,steps=integral_degree(zz[2],zz[3],mm[3])
    assert abs(degree)==1
    # The unique graph-distance-five partner defines the central antipodal symmetry.
    antipode=[]
    for i in range(30):
        mates=[j for j in range(30) if d[i][j]==5]
        assert len(mates)==1
        antipode.append(mates[0])
    assert all(antipode[antipode[i]]==i for i in range(30))
    assert all(set(antipode[j] for j in G[i])==G[antipode[i]] for i in range(30))
    antipodal_degrees=[]
    for r in (2,3):
        changed=action_on_cycle(zz[r],antipode)
        sign,_=integral_degree(changed,zz[r],mm[r])
        assert sign in (-1,1)
        antipodal_degrees.append(sign)
    assert antipodal_degrees==[-1,-1]
    # Scale four is join of 15 copies of S^0; scale five is full simplex.
    pairs={tuple(sorted((i,antipode[i]))) for i in range(30)}
    assert len(pairs)==15 and all(d[a][b]==5 for a,b in pairs)
    assert all(d[i][j]<5 for i in range(30) for j in range(i+1,30) if (i,j) not in pairs)
    print('inclusion_H2_degree',degree,'substitutions',steps)
    print('antipodal_H2_degrees',antipodal_degrees)
    print('scale4_antipodal_pairs',len(pairs),'H14_sign',(-1)**15)
    print('barcode_Z',{'H0':[(0,1,29)],'H1':[(1,2,11)],'H2':[(2,4,1)],'H14':[(4,5,1)]})
    print('VERIFY_OK')



def replay_certificate():
    # Second check: replay the furnished ordered collapse pairs rather than finding pairs.
    record=json.loads(Path(__file__).with_name('collapse_certificate.json').read_text(encoding='utf-8'))
    E,_,d=rectification()
    assert record['graph_edges']==[list(e) for e in E]
    assert set(record['radii'])=={'1','2','3'}
    for r in (1,2,3):
        faces=simplices(d,r)
        up={f:set() for f in faces}
        for F in faces:
            if F.bit_count()>1:
                for f in codimension_one(F):up[f].add(F)
        alive=set(faces)
        block=record['radii'][str(r)]
        assert block['full_face_counts']=={str(k):v for k,v in Counter(f.bit_count() for f in faces).items()}
        for f,F in block['collapse_pairs']:
            assert f in alive and F in alive
            assert f.bit_count()+1==F.bit_count() and f&F==f
            assert up[f]=={F} and not up[F]
            for removed in (f,F):
                alive.remove(removed)
                for sub in codimension_one(removed):
                    if sub in alive:
                        assert removed in up[sub]
                        up[sub].remove(removed)
        assert alive==set(block['remaining_faces'])
        if r>=2:
            z,_=oriented_sphere(alive)
            assert [[t,z[t]] for t in sorted(z)]==block['fundamental_cycle']
    print('EXPLICIT_CERTIFICATE_REPLAY_OK')

if __name__=='__main__':
    replay_certificate()
    run()

