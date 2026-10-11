#!/usr/bin/env python3
from collections import Counter, defaultdict, deque

N = 6
ORDER = [16, 2, 9, 22, 17, 14, 3, 18, 12, 20, 24, 0, 21, 13, 15, 1, 7, 6, 11, 10, 8, 5, 23, 4, 19]
EXPECTED_F = {0:25,1:244,2:1195,3:3139,4:4377,5:3001,6:846,7:72,8:1}
EXPECTED_RANKS = {1:24,2:220,3:975,4:2164,5:2213,6:775,7:71,8:1}


def categorical_graph(n):
    vertices=[(i,j) for i in range(n) for j in range(n)]
    edges=[]
    for i,j in vertices:
        for di in (-1,1):
            for dj in (-1,1):
                u=(i+di,j+dj)
                if 0 <= u[0] < n and 0 <= u[1] < n and (i,j) < u:
                    edges.append(((i,j),u))
    return vertices, sorted(edges)


def connected(vertices, edges):
    if not vertices:
        return True
    adj={v:set() for v in vertices}
    for a,b in edges:
        adj[a].add(b); adj[b].add(a)
    seen={vertices[0]}; stack=[vertices[0]]
    while stack:
        u=stack.pop()
        for v in adj[u]-seen:
            seen.add(v); stack.append(v)
    return len(seen)==len(vertices)


def even_component(n):
    vertices=[(i,j) for i in range(n) for j in range(n) if (i+j)%2==0]
    V=set(vertices)
    edges=[]
    for i,j in vertices:
        for di in (-1,1):
            for dj in (-1,1):
                u=(i+di,j+dj)
                if u in V and (i,j) < u:
                    edges.append(((i,j),u))
    return vertices, sorted(edges)


def matching_faces(edges):
    m=len(edges)
    conflict=[0]*m
    for a,e in enumerate(edges):
        se=set(e)
        for b,f in enumerate(edges):
            if a != b and se.intersection(f):
                conflict[a] |= 1<<b
    faces=[]
    def rec(avail, chosen):
        if avail == 0:
            if chosen:
                faces.append(chosen)
            return
        lb=avail & -avail
        k=lb.bit_length()-1
        rec(avail ^ lb, chosen)
        rec((avail ^ lb) & ~conflict[k], chosen | lb)
    rec((1<<m)-1, 0)
    return faces


def staged_matching(faces, order):
    remaining=set(faces)
    pairs=[]
    for v in order:
        bit=1<<v
        lows=[f for f in remaining if not(f&bit) and (f|bit) in remaining]
        for f in lows:
            hi=f|bit
            if f in remaining and hi in remaining:
                remaining.remove(f); remaining.remove(hi); pairs.append((f,hi))
    return pairs, remaining


def hasse_acyclic(faces, pairs):
    faces=set(faces)
    matched={(lo,hi) for lo,hi in pairs}
    adj={f:[] for f in faces}
    indeg={f:0 for f in faces}
    covers=0
    for hi in faces:
        x=hi
        while x:
            lb=x&-x; x-=lb
            lo=hi^lb
            if lo==0 or lo not in faces:
                continue
            covers += 1
            if (lo,hi) in matched:
                a,b=lo,hi
            else:
                a,b=hi,lo
            adj[a].append(b); indeg[b]+=1
    q=deque([f for f,d in indeg.items() if d==0])
    seen=0
    while q:
        u=q.popleft(); seen+=1
        for v in adj[u]:
            indeg[v]-=1
            if indeg[v]==0:q.append(v)
    return seen==len(faces), covers


def rank_mod2(cols, row_index):
    piv={}; rank=0
    for s in cols:
        col=0; x=s
        while x:
            lb=x&-x; x-=lb
            col ^= 1<<row_index[s^lb]
        while col:
            p=col.bit_length()-1
            if p in piv: col ^= piv[p]
            else:
                piv[p]=col; rank+=1; break
    return rank


def main():
    V,E=categorical_graph(N)
    assert len(V)==36 and len(E)==50
    evenV=[v for v in V if sum(v)%2==0]
    oddV=[v for v in V if sum(v)%2==1]
    evenE=[e for e in E if e[0] in evenV]
    oddE=[e for e in E if e[0] in oddV]
    assert len(evenV)==len(oddV)==18
    assert len(evenE)==len(oddE)==25
    assert connected(evenV,evenE) and connected(oddV,oddE)
    assert sorted(ORDER)==list(range(25))
    # Reflection in the second coordinate is an explicit component isomorphism.
    refl=lambda v:(v[0],N-1-v[1])
    mapped={tuple(sorted((refl(a),refl(b)))) for a,b in evenE}
    assert mapped==set(oddE)

    CV,CE=even_component(N)
    assert set(CV)==set(evenV) and CE==evenE
    faces=matching_faces(CE)
    bydim=defaultdict(list)
    for f in faces: bydim[f.bit_count()-1].append(f)
    fvec={d:len(v) for d,v in sorted(bydim.items())}
    assert fvec==EXPECTED_F

    pairs,critical=staged_matching(faces,ORDER)
    crit=Counter(f.bit_count()-1 for f in critical)
    assert len(pairs)==6443
    assert crit==Counter({5:13,0:1})
    acyclic,covers=hasse_acyclic(faces,pairs)
    assert acyclic

    ranks={}
    for d in range(1,max(bydim)+1):
        rows={f:i for i,f in enumerate(bydim[d-1])}
        ranks[d]=rank_mod2(bydim[d],rows)
    assert ranks==EXPECTED_RANKS
    betti={}
    for d in range(max(bydim)+1):
        b=len(bydim[d])-ranks.get(d,0)-ranks.get(d+1,0)
        if d==0:b-=1
        betti[d]=b
    assert betti=={0:0,1:0,2:0,3:0,4:0,5:13,6:0,7:0,8:0}
    euler=sum(((-1)**d)*len(fs) for d,fs in bydim.items())
    assert euler==-12

    print('VERIFY_OK')
    print('P6xP6 vertices=36 edges=50 components=2x(18 vertices,25 edges)')
    print('component matching faces=',len(faces),'f_vector=',fvec)
    print('hasse_covers=',covers,'morse_pairs=',len(pairs),'critical=',dict(sorted(crit.items())))
    print('mod2_boundary_ranks=',ranks,'reduced_betti=',betti,'euler=',euler)
    print('component homotopy: wedge of 13 S^5')
    print('full join homotopy: wedge of 169 S^11')

if __name__=='__main__': main()
