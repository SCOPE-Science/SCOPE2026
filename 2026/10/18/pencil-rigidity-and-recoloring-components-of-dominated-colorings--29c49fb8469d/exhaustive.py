#!/usr/bin/env python3
"""Exhaustive, independent class-partition search for projective planes of orders 2,3.
A color class is accepted only if it lies in the open neighborhood of some line vertex.
No pencil or extremal structure is used in candidate generation.
"""
import itertools, json, collections

def geometry(p):
    triples=[]
    for a,b,c in itertools.product(range(p),repeat=3):
        if (a,b,c)==(0,0,0): continue
        v=(a,b,c)
        n=next(z for z in v if z)
        inv=pow(n,-1,p)
        v=tuple(z*inv%p for z in v)
        if v not in triples: triples.append(v)
    triples.sort()
    lines=[sum(1<<j for j,y in enumerate(triples) if sum(x*y0 for x,y0 in zip(xv,y))%p==0)
           for xv in triples]
    assert len(set(lines)) == len(triples) == p*p+p+1
    return triples, sorted(lines)

def all_partitions(v, lines, blocks):
    full=(1<<v)-1
    valid=set()
    for m in lines:
        sub=m
        while sub:
            valid.add(sub)
            sub=(sub-1)&m
    by_point=[[m for m in sorted(valid) if (m>>i)&1] for i in range(v)]
    result=[]
    def rec(rem,chosen):
        if not rem:
            if len(chosen)==blocks: result.append(tuple(sorted(chosen)))
            return
        if len(chosen)>=blocks: return
        j=(rem&-rem).bit_length()-1
        for subset in by_point[j]:
            if subset&rem!=subset: continue
            rec(rem^subset,chosen+[subset])
    rec(full,[])
    assert len(set(result))==len(result)
    return sorted(result)

def exchange_graph(parts,v):
    idx={p:i for i,p in enumerate(parts)}
    E=set()
    for i,p in enumerate(parts):
        for k,a in enumerate(p):
            if a.bit_count()==1: continue
            for j,b in enumerate(p):
                if j==k: continue
                for bit in range(v):
                    if not (a>>bit)&1: continue
                    q=list(p)
                    q[k]=a^(1<<bit);q[j]=b|(1<<bit)
                    t=idx.get(tuple(sorted(q)))
                    if t is not None: E.add(tuple(sorted((i,t))))
    return sorted(E)

def comps(n,E):
    adj=[set() for _ in range(n)]
    for i,j in E: adj[i].add(j);adj[j].add(i)
    out=[];seen=set()
    for i in range(n):
        if i in seen:continue
        seen.add(i);Q=[i]; head=0
        while head<len(Q):
            x=Q[head];head+=1
            for y in adj[x]:
                if y not in seen: seen.add(y);Q.append(y)
        out.append(sorted(Q))
    return adj,sorted(out,key=lambda c:c[0])

def verify(p):
    pts,lines=geometry(p)
    v=len(pts);m=p+1
    parts=all_partitions(v,lines,m)
    edges=exchange_graph(parts,v)
    adj,cc=comps(len(parts),edges)
    assert len(parts)==v*m
    assert len(cc)==v and all(len(c)==m for c in cc)
    assert len(edges)==v*m*(m-1)//2
    assert all(len(adj[x])==m-1 for x in range(len(parts)))
    for cc0 in cc:
        for i in cc0: assert set(cc0)-{i}==adj[i]
    # Verify the pencil-center representation for *each* independently found partition.
    enc=[]
    for part in parts:
        centers=[]
        for center in range(v):
            pencil=[L for L in lines if (L>>center)&1]
            cores={L^(1<<center) for L in pencil}
            if {a & ~(1<<center) for a in part}==cores:
                if sum(bool(a&(1<<center)) for a in part)==1:centers.append(center)
        assert len(centers)==1
        enc.append(centers[0])
    assert all(len({enc[j] for j in c})==1 for c in cc)
    return {'order':p,'vertices_per_incidence_side':v,'minimum_color_classes_per_side':m,
            'unlabelled_one_side_color_partitions':len(parts),'one_side_recolor_edges':len(edges),
            'one_side_components':len(cc),'one_side_component_sizes':sorted([len(c) for c in cc]),
            'both_sides_unlabelled_partitions':len(parts)**2,'both_sides_components':v*v,
            'each_both_sides_component_vertices':m*m,'each_both_sides_component_edges':m*m*(m-1),
            'one_side_partitions':[[list(i for i in range(v) if (S>>i)&1) for S in P] for P in parts],
            'center_of_each_one_side_partition':enc}

if __name__=='__main__':
    ans={'verification':'brute-force unlabeled dominated-color partitions and exchanges',
         'checks':[verify(q) for q in (2,3)]}
    print(json.dumps(ans,sort_keys=True,separators=(',',':')))
