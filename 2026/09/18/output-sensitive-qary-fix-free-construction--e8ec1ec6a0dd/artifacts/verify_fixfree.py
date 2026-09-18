#!/usr/bin/env python3
import collections
import heapq
import itertools
import random

def score_order_naive(edges, a0, c0):
    chosen=set(); r=collections.Counter(); c=collections.Counter(); out=[]
    for _ in edges:
        best=None
        for i,j,k in edges:
            if k in chosen: continue
            d=c0[j]-r[j]-a0[i]-c[i]-(i==j)
            z=(d,k,i,j)
            if best is None or z<best: best=z
        d,k,i,j=best
        out.append((k,d)); chosen.add(k); r[i]+=1; c[j]+=1
    return out

def score_order_grouped(edges, a0, c0, side):
    if side=="Uc":
        group=lambda e:e[0]
        other=lambda e:e[1]
        uniform_label=lambda e:e[1]
        point_label=lambda e:e[0]
        unique_pos=1
    else:
        group=lambda e:e[1]
        other=lambda e:e[0]
        uniform_label=lambda e:e[0]
        point_label=lambda e:e[1]
        unique_pos=0

    E={k:(i,j,k) for i,j,k in edges}
    I={i for i,j,k in edges}; J={j for i,j,k in edges}
    active={k:True for i,j,k in edges}
    version=collections.Counter()
    local_key={}
    group_lazy=collections.Counter()
    local=collections.defaultdict(list)
    unique={}
    for i,j,k in edges:
        b=c0[j]-a0[i]-(i==j)
        local_key[k]=b
        g=group((i,j,k))
        heapq.heappush(local[g],(b,k,version[k]))
        lab=(i,j)[unique_pos]
        if lab in (I if side=="Uc" else J):
            assert lab not in unique
            unique[lab]=k

    gver=collections.Counter(); global_heap=[]
    def clean(g):
        h=local[g]
        while h and (not active[h[0][1]] or h[0][2]!=version[h[0][1]]
                     or h[0][0]!=local_key[h[0][1]]):
            heapq.heappop(h)
    def publish(g):
        clean(g); gver[g]+=1
        if local[g]:
            z,k,v=local[g][0]
            heapq.heappush(global_heap,(z-group_lazy[g],k,g,gver[g]))
    for g in list(local): publish(g)

    out=[]
    for _ in edges:
        while True:
            d,k,g,gv=heapq.heappop(global_heap)
            if gv!=gver[g]: continue
            clean(g)
            if not local[g]: continue
            z,k0,v=local[g][0]
            if (d,k)!=(z-group_lazy[g],k0):
                publish(g); continue
            break
        i,j,_=E[k]
        active[k]=False; version[k]+=1
        publish(g)

        ug=uniform_label((i,j,k))
        if ug in local:
            group_lazy[ug]+=1
            publish(ug)

        pk=unique.get(point_label((i,j,k)))
        if pk is not None and active[pk]:
            pi,pj,_=E[pk]
            pg=group((pi,pj,pk))
            local_key[pk]-=1; version[pk]+=1
            heapq.heappush(local[pg],(local_key[pk],pk,version[pk]))
            publish(pg)
        out.append((k,d))
    return out

def make_case(n, side, seed):
    rng=random.Random(seed)
    h=max(3,n//4+2)
    if side=="Uc":
        I=list(range(h)); outside=list(range(h,2*h)); used=set(); edges=[]
        for k in range(n):
            i=rng.choice(I)
            if rng.random()<.45 and len(used)<len(I):
                a=rng.choice([x for x in I if x not in used]); used.add(a); j=a
            else: j=rng.choice(outside)
            edges.append((i,j,k))
    else:
        J=list(range(h)); outside=list(range(h,2*h)); used=set(); edges=[]
        for k in range(n):
            j=rng.choice(J)
            if rng.random()<.45 and len(used)<len(J):
                a=rng.choice([x for x in J if x not in used]); used.add(a); i=a
            else: i=rng.choice(outside)
            edges.append((i,j,k))
    labs={x for i,j,k in edges for x in (i,j)}
    a0={x:rng.randrange(-10,11) for x in labs}
    c0={x:rng.randrange(-10,11) for x in labs}
    return edges,a0,c0

def brute_words(q,l1,l2,l3,F1,F2):
    F=set(F1)|set(F2); ans=set()
    for w in itertools.product(range(q),repeat=l3):
        if all(w[:len(f)]!=f and w[-len(f):]!=f for f in F): ans.add(w)
    return ans

def grouped_words(q,l1,l2,l3,F1,F2):
    F1=set(F1); F2=set(F2)
    W=list(itertools.product(range(q),repeat=l2))
    P=[w for w in W if w[:l1] not in F1 and w not in F2]
    S=[w for w in W if w[-l1:] not in F1 and w not in F2]
    ans=set()
    if l3>=2*l2:
        for u in P:
            for z in itertools.product(range(q),repeat=l3-2*l2):
                for v in S: ans.add(u+z+v)
    else:
        b=2*l2-l3; G=collections.defaultdict(list)
        for v in S: G[v[:b]].append(v)
        for u in P:
            for v in G[u[-b:]]: ans.add(u+v[b:])
    return ans

def main():
    for side in ("Uc","Ur"):
        for n in (1,2,5,10,25,50):
            for seed in range(20):
                e,a,c=make_case(n,side,1000*n+seed)
                assert score_order_grouped(e,a,c,side)==score_order_naive(e,a,c)
    cases=[
        (2,1,3,5,[(0,)],[(1,1,1)]),
        (2,1,3,6,[(0,)],[(1,1,1)]),
        (3,1,2,3,[(0,)],[(1,1),(1,2)]),
        (3,1,2,4,[(0,)],[(1,1),(1,2)]),
    ]
    for c in cases:
        assert grouped_words(*c)==brute_words(*c)
    print("PASS")

if __name__=="__main__":
    main()
