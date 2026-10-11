#!/usr/bin/env python3
"""Finite combinatorial certificate for the intrinsic radius-one Čech complex of H(3,3)."""
from itertools import product, combinations
from collections import Counter, deque

def main():
    vertices=list(product(range(3),repeat=3)); index={v:i for i,v in enumerate(vertices)}
    centers=[]
    for v in vertices:
        ball={index[v]}
        for i in range(3):
            for x in range(3):
                w=list(v);w[i]=x;ball.add(index[tuple(w)])
        assert len(ball)==7
        centers.append(tuple(sorted(ball)))
    faces=set()
    for ball in centers:
        for k in range(1,len(ball)+1):
            for comb in combinations(ball,k):faces.add(sum(1<<j for j in comb))
    sizes=Counter(f.bit_count()-1 for f in faces)
    assert [sizes[d] for d in range(7)]==[27,243,891,945,567,189,27]
    free=set(faces);match={};pairs=[]
    # Sequential toggle: at the stage for vertex v, match every still-free
    # pair (sigma,sigma U {v}) whose elements are both still free.
    for v in range(27):
        bit=1<<v
        for f in sorted(f for f in free if not (f&bit)):
            g=f|bit
            if g in free and f in free:
                free.remove(f);free.remove(g)
                match[(f,g)]=True;pairs.append((f,g))
    assert len(pairs)==1377
    assert Counter(f.bit_count()-1 for f in free)=={0:1,2:134}
    # Independently reconstruct every oriented incidence; matched Hasse
    # arrows ascend; all other Hasse arrows descend.
    indegree={f:0 for f in faces};arrows={f:[] for f in faces};cover_count=0
    for g in faces:
        t=g
        while t:
            bit=t & -t; t-=bit
            f=g^bit
            if not f:continue
            cover_count+=1
            if (f,g) in match:src,dst=f,g
            else:src,dst=g,f
            arrows[src].append(dst);indegree[dst]+=1
    q=deque(f for f in faces if indegree[f]==0);processed=0
    while q:
        f=q.popleft();processed+=1
        for g in arrows[f]:
            indegree[g]-=1
            if indegree[g]==0:q.append(g)
    assert processed==len(faces),(processed,len(faces))
    chi=sum((-1)**d*count for d,count in sizes.items())
    assert chi==135
    print('graph=H(3,3)=K_3 Cartesian K_3 Cartesian K_3')
    print('closed-radius-one-ball-count=27; cardinality-each=7')
    print('f-vector='+str([sizes[d] for d in range(7)]))
    print('faces='+str(len(faces))+'; hasse-covers='+str(cover_count))
    print('paired-hasse-edges='+str(len(pairs)))
    print('critical-cell-vector='+str(sorted(Counter(f.bit_count()-1 for f in free).items())))
    print('acyclic-directed-vertices='+str(processed))
    print('Euler-characteristic='+str(chi)+'; reduced-Euler-characteristic='+str(chi-1))
    print('Conclusion: one critical 0-cell and 134 critical 2-cells, hence wedge of 134 S^2.')
if __name__=='__main__':main()
