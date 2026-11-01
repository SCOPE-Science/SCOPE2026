#!/usr/bin/env python3
"""Reproducible finite simplicial and Morse certificate for a Coxeter-graph Rips filtration.

Uses only Python standard library; all faces are generated from the stated Fano construction.
"""
from collections import Counter, deque
from itertools import combinations

N = 28
PIVOTS = (9,27,18,7,21,0,1,17,8,3,19,5,26,4,13,25,11,6,
          12,23,22,2,15,14,10,24,16,20)

def construct_graph():
    lines = {frozenset((a,b,a^b)) for a in range(1,8)
             for b in range(a+1,8)}
    assert len(lines) == 7 and all(len(x)==3 for x in lines)
    nonlines = [frozenset(t) for t in combinations(range(1,8),3)
                if frozenset(t) not in lines]
    assert len(nonlines)==N
    adj=[set() for _ in range(N)]
    for i,j in combinations(range(N),2):
        if nonlines[i].isdisjoint(nonlines[j]):
            adj[i].add(j);adj[j].add(i)
    assert all(len(a)==3 for a in adj)
    assert sum(len(a) for a in adj)==84
    return adj

def graph_girth(adj):
    smallest=N+1
    for a in range(N):
        for b in adj[a]:
            if a >= b: continue
            queue=deque([a]); distance=[-1]*N;distance[a]=0
            while queue:
                x=queue.popleft()
                for y in adj[x]:
                    if (x==a and y==b) or (x==b and y==a): continue
                    if distance[y]<0:
                        distance[y]=distance[x]+1;queue.append(y)
            assert distance[b]>=0
            smallest=min(smallest,distance[b]+1)
    return smallest

def graph_distances(adj):
    distances=[]
    for u in range(N):
        d=[-1]*N;d[u]=0;queue=deque([u])
        while queue:
            v=queue.popleft()
            for w in adj[v]:
                if d[w]<0:d[w]=d[v]+1;queue.append(w)
        assert all(x>=0 for x in d)
        assert Counter(d)==Counter({0:1,1:3,2:6,3:12,4:6})
        distances.append(d)
    assert all(distances[i][j]==distances[j][i] for i,j in combinations(range(N),2))
    return distances

def clique_faces(distances,r):
    adjmask=[sum(1<<j for j in range(N) if j!=i and distances[i][j]<=r)
             for i in range(N)]
    faces=[]
    def branch(mask,available):
        while available:
            vbit=available & -available
            available -= vbit
            v=vbit.bit_length()-1
            new=mask|vbit
            faces.append(new)
            branch(new,available & adjmask[v])
    branch(0,(1<<N)-1)
    assert len(faces)==len(set(faces))
    return faces

def faces_by_dim(faces):
    return dict(sorted(Counter(s.bit_count()-1 for s in faces).items()))

def verify_morse(faces):
    residual=set(faces); matched_up={};order=PIVOTS
    assert len(order)==N and set(order)==set(range(N))
    for v in order:
        b=1<<v
        for lower in sorted(tuple(residual),key=lambda s:(s.bit_count(),s)):
            if lower not in residual or lower&b: continue
            upper=lower|b
            if upper in residual:
                residual.remove(lower);residual.remove(upper)
                assert lower not in matched_up
                matched_up[lower]=upper
    critical=faces_by_dim(residual)
    assert critical=={0:1,4:87}, critical
    assert len(matched_up)==5404
    assert len(faces)==2*len(matched_up)+len(residual)
    # Entire gradient-arrow orientation: matched facets upward, others downward.
    allfaces=set(faces)
    successors={s:[] for s in allfaces}
    indegree={s:0 for s in allfaces}
    incidence_count=0
    for upper in allfaces:
        v=upper
        while v:
            bit=v&-v;v-=bit
            lower=upper^bit
            if lower==0:continue
            assert lower in allfaces
            incidence_count+=1
            if matched_up.get(lower)==upper:
                src,dst=lower,upper
            else:
                src,dst=upper,lower
            successors[src].append(dst);indegree[dst]+=1
    todo=deque(s for s in allfaces if indegree[s]==0)
    processed=0
    while todo:
        s=todo.popleft();processed+=1
        for t in successors[s]:
            indegree[t]-=1
            if indegree[t]==0:todo.append(t)
    assert processed==len(faces),(processed,len(faces))
    return critical,len(matched_up),incidence_count,processed

def mod2_ranks(faces):
    # Secondary check; rank is not used in the discrete-Morse homotopy proof.
    bydim={}
    for s in faces: bydim.setdefault(s.bit_count()-1,[]).append(s)
    ranks=[]
    for k in range(1,max(bydim)+1):
        cod=sorted(bydim[k-1]); row={s:i for i,s in enumerate(cod)}
        basis={}
        for t in bydim[k]:
            col=0;x=t
            while x:
                bit=x&-x;x-=bit
                col ^= 1<<row[t^bit]
            while col:
                p=col.bit_length()-1
                if p in basis:col^=basis[p]
                else:basis[p]=col;break
        ranks.append(len(basis))
    betti=[len(bydim[k])-(ranks[k-1] if k>0 else 0)-(ranks[k] if k<len(ranks) else 0)
           for k in range(max(bydim)+1)]
    return ranks,betti

def main():
    adj=construct_graph()
    assert graph_girth(adj)==7
    print('graph vertices',N,'edges',42,'girth',7,'diameter',4)
    D=graph_distances(adj)
    for r,expected in [(1,{0:28,1:42}),
                       (2,{0:28,1:126,2:112,3:28}),
                       (3,{0:28,1:294,2:1456,3:3514,4:3864,5:1596,6:144})]:
        faces=clique_faces(D,r)
        fvector=faces_by_dim(faces)
        assert fvector==expected,(r,fvector)
        ranks,betti=mod2_ranks(faces)
        print('scale',r,'faces',len(faces),'f_vector',fvector,
              'mod2_boundary_ranks',ranks,'mod2_betti',betti)
        if r==2:
            # Exhaustively check maximal cliques = 28 closed vertex neighborhoods.
            face_set=set(faces)
            maximal=[s for s in faces if not any((s|(1<<v)) in face_set
                        for v in range(N) if not (s>>v)&1)]
            stars={sum(1<<j for j in (set(adj[v])|{v})) for v in range(N)}
            assert set(maximal)==stars and len(stars)==N
            # Every extra distance-two edge belongs to exactly one 3-neighbor star.
            for i,j in combinations(range(N),2):
                if D[i][j]==2:
                    assert sum(i in adj[v] and j in adj[v] for v in range(N))==1
            print('scale 2: each of 28 tetrahedra collapses to its original star')
        if r==3:
            crit,npairs,arrows,processed=verify_morse(faces)
            assert betti==[1,0,0,0,87,0,0]
            print('scale 3 Morse: pairs',npairs,'critical',crit,
                  'nonempty_face_incidences',arrows,
                  'topological_sort_visited',processed)
    # Graph diameter 4, so every pair has distance <=4 and VR scale 4 is a simplex.
    assert max(max(row) for row in D)==4
    print('scale 4: full 27-simplex; integral homotopy types and barcodes established')

if __name__=='__main__':main()
