#!/usr/bin/env python3
"""Exact census of cubic eight-vertex graphs and elliptic Boolean transforms.
Uses only Python standard library, no tables beyond six explicit witnesses.
"""
from itertools import combinations, permutations

N=8
EDGES=list(combinations(range(N),2))
EID={e:i for i,e in enumerate(EDGES)}
REPS=[
[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3),(4,5),(4,6),(4,7),(5,6),(5,7),(6,7)],
[(0,1),(0,2),(0,3),(1,2),(1,3),(2,4),(3,5),(4,6),(4,7),(5,6),(5,7),(6,7)],
[(0,1),(0,2),(0,3),(1,2),(1,4),(2,5),(3,4),(3,6),(4,7),(5,6),(5,7),(6,7)],
[(0,1),(0,2),(0,3),(1,2),(1,4),(2,5),(3,6),(3,7),(4,6),(4,7),(5,6),(5,7)],
[(0,1),(0,2),(0,3),(1,4),(1,5),(2,4),(2,6),(3,5),(3,6),(4,7),(5,7),(6,7)],
[(0,1),(0,2),(0,3),(1,4),(1,5),(2,4),(2,6),(3,5),(3,7),(4,7),(5,6),(6,7)]
]
EXPECTED_ORBITS=[35,2520,10080,3360,840,2520]
EXPECTED_COUNT=[54,26,17,6,0,5]


def edge_mask(edges):
    mask=0
    for a,b in edges:
        if a>b: a,b=b,a
        mask|=1<<EID[a,b]
    return mask

def enumerate_cubic():
    answers=set()
    def recurse(degrees,mask):
        try: u=next(i for i in range(N) if degrees[i]<3)
        except StopIteration:
            answers.add(mask)
            return
        need=3-degrees[u]
        candidates=[v for v in range(u+1,N) if degrees[v]<3]
        for vs in combinations(candidates,need):
            newdeg=list(degrees);newdeg[u]=3
            newmask=mask
            for v in vs:
                newdeg[v]+=1;newmask |= 1<<EID[u,v]
            if sum(3-d for d in newdeg) != 2*(12-newmask.bit_count()):
                raise AssertionError('degree bookkeeping')
            recurse(newdeg,newmask)
    recurse([0]*N,0)
    return answers


def orbit_partition():
    classes={}
    orbit_sizes=[]
    for k,edges in enumerate(REPS):
        orbit=set()
        for perm in permutations(range(N)):
            orbit.add(edge_mask([(perm[a],perm[b]) for a,b in edges]))
        for mask in orbit:
            assert mask not in classes, 'overlapping isomorphism orbits'
            classes[mask]=k
        orbit_sizes.append(len(orbit))
    return classes,orbit_sizes


def subgraph_elliptic_count(edges):
    """Direct Gauss-sum calculation, independent for every edge subset."""
    m=len(edges)
    total=0
    for emask in range(1<<m):
        neighbors=[0]*N
        for i,(a,b) in enumerate(edges):
            if emask>>i & 1:
                neighbors[a]|=1<<b
                neighbors[b]|=1<<a
        q=bytearray(1<<N)
        count1=0
        for x in range(1,1<<N):
            low=x&-x; v=low.bit_length()-1; rest=x^low
            q[x]=q[rest]^((rest&neighbors[v]).bit_count()&1)
            count1+=q[x]
        gauss=(1<<N)-2*count1
        if gauss==-16:
            total+=1
    return total


def independently_transform(edges):
    """Second calculation by Walsh transform on the edge-index incidence image."""
    m=len(edges)
    w=[0]*(1<<m)
    for x in range(1<<N):
        pos=0
        for j,(a,b) in enumerate(edges):
            if x>>a&1 and x>>b&1:
                pos|=1<<j
        w[pos]+=1
    for k in range(m):
        step=1<<k
        for i in range(1<<m):
            if i&step==0:
                a=w[i];b=w[i|step]
                w[i]=a+b;w[i|step]=a-b
    return sum(gauss==-16 for gauss in w)


def connected(edges):
    reached={0}
    while True:
        grow=reached|{v if u in reached else u for u,v in edges if (u in reached)!=(v in reached)}
        if grow==reached: break
        reached=grow
    return len(reached)==N




def check_six_vertex_regression():
    """Reproduce the published six-vertex transform's complete edge-count profile."""
    small_edges=list(combinations(range(6),2))
    m=len(small_edges)
    transform=bytearray(1<<m)
    for edge_mask_value in range(1<<m):
        neighbors=[0]*6
        for j,(a,b) in enumerate(small_edges):
            if edge_mask_value>>j&1:
                neighbors[a]|=1<<b;neighbors[b]|=1<<a
        q=bytearray(64);ones=0
        for x in range(1,64):
            l=x&-x;v=l.bit_length()-1;r=x^l
            q[x]=q[r]^((r&neighbors[v]).bit_count()&1)
            ones+=q[x]
        transform[edge_mask_value]=int(64-2*ones==-8)
    for bit in range(m):
        for mask in range(1<<m):
            if mask>>bit&1:
                transform[mask]^=transform[mask^(1<<bit)]
    histogram={7:0,8:0,9:0}
    for mask,is_member in enumerate(transform):
        if not is_member:continue
        length=mask.bit_count()
        assert length in histogram,'unexpected six-vertex edge count'
        histogram[length]+=1
        for v in range(6):
            assert sum(int(mask>>j&1) for j,e in enumerate(small_edges) if v in e)<=3
    assert histogram=={7:105,8:180,9:60},histogram
    print('n6_published_regression=PASS support_labeled=345 edges_7=105 edges_8=180 edges_9=60')


def main():
    check_six_vertex_regression()
    enumeration=enumerate_cubic()
    assert len(enumeration)==19355,len(enumeration)
    partition,orbits=orbit_partition()
    assert len(partition)==19355,len(partition)
    assert set(partition)==enumeration,'missing cubic graphs'
    assert orbits==EXPECTED_ORBITS,(orbits,EXPECTED_ORBITS)
    counts=[]
    for k,edges in enumerate(REPS):
        assert all(sum(v in e for e in edges)==3 for v in range(N))
        a=subgraph_elliptic_count(edges)
        b=independently_transform(edges)
        assert a==b==EXPECTED_COUNT[k],(k,a,b)
        counts.append(a)
        print(f'class={k} labeled_orbit={orbits[k]} connected={connected(edges)} elliptic_subgraphs={a} parity={a%2}')
    assert [int(connected(e)) for e in REPS]==[0,1,1,1,1,1]
    assert [k for k,c in enumerate(counts) if c%2]==[2,5]
    print('VERIFY_OK graphs=19355 classes=6 orbit_cover=exact two_independent_Gauss_transforms=agree selected_classes=2,5')

if __name__=='__main__':main()
