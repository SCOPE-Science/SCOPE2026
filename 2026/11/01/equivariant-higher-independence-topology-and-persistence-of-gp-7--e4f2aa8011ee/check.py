#!/usr/bin/env python3
"""Exact check of four higher-independence stages of GP(7,2). Python 3 stdlib."""
from collections import Counter, defaultdict, deque
import hashlib, json

N=7
V=14
EDGES=set()
for i in range(N):
    for a,b in ((i,(i+1)%N),(i,N+i),(N+i,N+(i+2)%N)):
        EDGES.add(tuple(sorted((a,b))))
assert len(EDGES)==21
ADJ=[0]*V
for a,b in EDGES:
    ADJ[a]|=1<<b
    ADJ[b]|=1<<a
assert all(a.bit_count()==3 for a in ADJ)

def threshold(mask):
    """Maximum size of a connected component of the induced subgraph."""
    rem=mask;mx=0
    while rem:
        seed=rem&-rem;rem^=seed;group=seed;front=seed
        while front:
            nex=0;f=front
            while f:
                v=f&-f;f^=v
                nex|=ADJ[v.bit_length()-1]
            nex&=rem;rem^=nex;group|=nex;front=nex
        mx=max(mx,group.bit_count())
    return mx

def threshold_independently(mask):
    """Independent union-find calculation using the edge list."""
    selected=[i for i in range(V) if mask>>i&1]
    parent={i:i for i in selected};sizes={i:1 for i in selected}
    def root(a):
        while parent[a]!=a:a=parent[a]
        return a
    for a,b in EDGES:
        if a in parent and b in parent:
            a=root(a);b=root(b)
            if a!=b:
                parent[b]=a;sizes[a]+=sizes[b]
    return max([sizes[i] for i in selected if parent[i]==i], default=0)

THRESHOLD=[]
for mask in range(1<<V):
    a=threshold(mask)
    b=threshold_independently(mask)
    assert a==b,(mask,a,b)
    THRESHOLD.append(a)

ORDERS={
 1:[1,10,9,5,11,2,3,7,8,4,0,12,6,13],
 2:[13,10,0,12,6,5,3,8,7,11,4,1,9,2],
 3:[1,10,9,5,11,2,3,7,8,4,0,12,6,13],
 4:[11,12,6,10,13,0,4,1,7,5,2,8,9,3]
}
EXPECTED={1:{0:1,3:1},2:{0:1,5:1},3:{0:1,5:8},4:{0:1,6:6}}
EXPECTED_BETTI={1:{0:1,3:1},2:{0:1,5:1},3:{0:1,5:8},4:{0:1,6:6}}


def face_morse(stage):
    faces=set(m for m in range(1,1<<V) if THRESHOLD[m]<=stage)
    remaining=set(faces);pairs=[]
    for v in ORDERS[stage]:
        bit=1<<v
        for a in sorted(x for x in remaining if not (x&bit) and (x|bit) in remaining):
            b=a|bit
            if a in remaining and b in remaining:
                remaining.remove(a);remaining.remove(b);pairs.append((a,b))
    critical=Counter(x.bit_count()-1 for x in remaining)
    assert dict(critical)==EXPECTED[stage],(stage,critical)
    assert len(faces)==len(pairs)*2+len(remaining)
    lower_upper=set(pairs)
    indegree={m:0 for m in faces}; direct={m:[] for m in faces};count=0
    for high in faces:
        bits=high
        while bits:
            one=bits&-bits;bits^=one
            lo=high^one
            if not lo:continue
            if (lo,high) in lower_upper:
                src,dst=lo,high
            else:
                src,dst=high,lo
            direct[src].append(dst)
            indegree[dst]+=1
            count+=1
    qq=deque(m for m in indegree if indegree[m]==0)
    visited=0
    while qq:
        v=qq.popleft();visited+=1
        for w in direct[v]:
            indegree[w]-=1
            if indegree[w]==0:qq.append(w)
    assert visited==len(faces),(stage,visited,len(faces))
    rank=Counter(m.bit_count()-1 for m in faces)
    # The Morse Euler characteristic equals the simplex Euler characteristic.
    assert sum((-1)**d*n for d,n in rank.items())==sum((-1)**d*n for d,n in critical.items())
    return {"stage":stage,"face_count_including_empty":len(faces)+1,
            "faces_by_dimension":dict(sorted(rank.items())),
            "matched_pairs":len(pairs),"hasse_incidence_count":count,
            "critical_by_dimension":dict(sorted(critical.items())),
            "critical_masks":sorted(remaining),
            "matching_sha256":hashlib.sha256(';'.join(f'{a}:{b}' for a,b in pairs).encode()).hexdigest()},faces


def f2_betti(faces):
    bd=defaultdict(list)
    for m in faces:bd[m.bit_count()-1].append(m)
    ranks={}
    for degree in sorted(bd):
        if degree==0:continue
        rows={m:i for i,m in enumerate(bd[degree-1])}
        pivots={}
        for high in bd[degree]:
            col=0;t=high
            while t:
                v=t&-t;t^=v
                col^=1<<rows[high^v]
            while col:
                i=col.bit_length()-1
                if i in pivots:col^=pivots[i]
                else:
                    pivots[i]=col;break
        ranks[degree]=len(pivots)
    b={d:len(bd[d])-ranks.get(d,0)-ranks.get(d+1,0) for d in bd}
    return {d:n for d,n in b.items() if n},ranks

def persistence(max_stage=4):
    simplices=[m for m in range(1,1<<V) if THRESHOLD[m]<=max_stage]
    simplices.sort(key=lambda m:(THRESHOLD[m],m.bit_count(),m))
    pos={m:i for i,m in enumerate(simplices)}
    pivots={};births={};deaths=Counter();zero_length=0
    for j,s in enumerate(simplices):
        col=0
        if s.bit_count()>1:
            rem=s
            while rem:
                one=rem&-rem;rem^=one
                col^=1<<pos[s^one]
        while col:
            pivot=col.bit_length()-1
            if pivot in pivots:
                col^=pivots[pivot]
            else:
                pivots[pivot]=col
                break
        if not col:
            births[j]=(s.bit_count()-1,THRESHOLD[s])
        else:
            pivot=col.bit_length()-1
            assert pivot in births,(j,pivot)
            dimension,birth=births.pop(pivot)
            assert dimension+1==s.bit_count()-1
            if birth==THRESHOLD[s]:zero_length+=1
            else:deaths[(dimension,birth,THRESHOLD[s])]+=1
    survivors=Counter(births.values())
    assert deaths==Counter({(3,1,2):1,(5,2,4):1,(5,3,4):7}),deaths
    assert survivors==Counter({(0,1):1,(6,4):6}),survivors
    return {'nonzero_finite_intervals':[{'degree':d,'birth':b,'death_exclusive':e,'multiplicity':n} for (d,b,e),n in sorted(deaths.items())],
            'survivors_through_cutoff_4':[{'degree':d,'birth':b,'multiplicity':n} for (d,b),n in sorted(survivors.items())],
            'zero_length_pairs':zero_length,
            'simplex_count':len(simplices)}


def sign_of_permutation(values):
    return -1 if sum(a>b for i,a in enumerate(values) for b in values[i+1:])%2 else 1

def lefschetz(faces,mp):
    total=0
    for f in faces:
        vertices=[v for v in range(V) if f>>v&1]
        image=[mp[v] for v in vertices]
        if sorted(image)==vertices:
            total+=(-1)**(len(vertices)-1)*sign_of_permutation(image)
    return total

def character(faces,stage):
    dim={1:3,2:5,3:5,4:6}[stage]
    traces=[]
    for power in [0,1,2,3]:
        mp=[(i+power)%N for i in range(N)]+[N+(i+power)%N for i in range(N)]
        assert {tuple(sorted((mp[a],mp[b]))) for a,b in EDGES}==EDGES
        traces.append((-1)**dim*(lefschetz(faces,mp)-1))
    mp=[(-i)%N for i in range(N)]+[N+(-i)%N for i in range(N)]
    assert {tuple(sorted((mp[a],mp[b]))) for a,b in EDGES}==EDGES
    traces.append((-1)**dim*(lefschetz(faces,mp)-1))
    assert traces=={1:[1,1,1,1,1],2:[1,1,1,1,-1],3:[8,1,1,1,-2],4:[6,-1,-1,-1,0]}[stage]
    return {'degree':dim,'traces_1_rotation_rotation2_rotation3_reflection':traces}


def main():
    # All maximal independent sets have cardinality five: a natural well-covered instance.
    ordinary={m for m in range(1,1<<V) if THRESHOLD[m]<=1}
    facets=[m for m in ordinary if all((m | (1<<v)) not in ordinary for v in range(V) if not (m>>v&1))]
    assert len(facets)==49 and {m.bit_count() for m in facets}=={5}
    stages=[]
    for k in range(1,5):
        st,faces=face_morse(k)
        betti,ranks=f2_betti(faces)
        assert betti==EXPECTED_BETTI[k],(k,betti)
        st['independent_gf2_betti']=betti
        st['independent_boundary_ranks']=ranks
        st['dihedral_character']=character(faces,k)
        stages.append(st)
    bars=persistence()
    output={'graph':'GP(7,2)','vertices':V,'edges':len(EDGES),'enumerated_vertex_subsets':1<<V,
            'all_thresholds_crosschecked_by_union_find':True,'ordinary_independence_facets':len(facets),'ordinary_independence_facet_sizes':[5], 'stages':stages,'persistence':bars,
            'conclusion':'GP7_2_EQUIVARIANT_HIGHER_INDEPENDENCE_PERSISTENCE_OK'}
    print(json.dumps(output,sort_keys=True,indent=2))

if __name__=='__main__':main()
