#!/usr/bin/env python3
"""Reconstruct a higher-independence filtration and verify finite collapse/Morse certificates.

Run: python3 verify.py  (no third-party modules required).
"""
from collections import Counter, deque
from pathlib import Path
import json

N = 11
ROOT = Path(__file__).resolve().parent
ORDERS = {
    1: list(range(11)),
    4: [6, 4, 5, 10, 2, 8, 7, 3, 1, 0, 9],
    5: [1, 8, 9, 4, 10, 7, 6, 5, 3, 2, 0],
    6: [0, 8, 2, 4, 10, 9, 5, 1, 6, 3, 7],
    7: list(range(10, -1, -1)),
    8: list(range(10, -1, -1)),
    9: list(range(10, -1, -1)),
    10: list(range(10, -1, -1)),
}
SPHERES = {1: (2,1),2:(2,1),3:(2,1),4:(3,59),5:(4,151),
           6:(5,175),7:(6,115),8:(7,45),9:(8,10),10:(9,1)}
EXPECTED_TOTAL = {1:103,2:313,3:493,4:763,5:1135,6:1521,7:1821,8:1981,
                  9:2036,10:2047,11:2048}

def edge_set():
    # The Mycielski construction on a 5-cycle: originals 0...4,
    # twins 5...9, and the apex 10.
    ans=set()
    for i in range(5):
        j=(i+1)%5
        for a,b in ((i,j),(i,j+5),(i+5,j),(i+5,10)):
            ans.add(tuple(sorted((a,b))))
    return ans

def adjacency(edges):
    out=[0]*N
    for u,v in edges:
        out[u]|=1<<v
        out[v]|=1<<u
    return out

def largest_bfs(mask,adj):
    remaining=mask;mx=0
    while remaining:
        start=remaining & -remaining
        component=start
        frontier=start
        while frontier:
            new=0
            while frontier:
                bit=frontier & -frontier;frontier-=bit
                new |= adj[bit.bit_length()-1] & mask
            frontier = new & ~component
            component |= frontier
        remaining &= ~component
        mx=max(mx,component.bit_count())
    return mx

def largest_union_find(mask,edges):
    parent=list(range(N));size=[1]*N
    def find(x):
        while parent[x]!=x:
            x=parent[x]
        return x
    for u,v in edges:
        if (mask>>u)&1 and (mask>>v)&1:
            a=find(u);b=find(v)
            if a!=b:
                parent[b]=a
                size[a]+=size[b]
    return max((size[find(v)] for v in range(N) if mask>>v&1),default=0)

def faces_by_stage():
    edges=edge_set()
    assert len(edges)==20
    assert len({v for e in edges for v in e})==N
    adj=adjacency(edges)
    assert sorted(x.bit_count() for x in adj)==[3]*5+[4]*5+[5]
    assert all(not ((adj[u] & adj[v]).bit_count()) for u,v in edges) # triangle-free
    values=[]
    for mask in range(1<<N):
        a=largest_bfs(mask,adj)
        b=largest_union_find(mask,edges)
        assert a==b, (mask,a,b)
        values.append(a)
    stages={r:{m for m in range(1<<N) if values[m]<=r} for r in range(1,N+1)}
    for r,K in stages.items():
        assert len(K)==EXPECTED_TOTAL[r],(r,len(K))
        for f in K:
            q=f
            while q:
                b=q&-q;q-=b
                assert (f^b) in K
    return stages

def check_morse(K,order,expected_dimension,expected_number):
    assert sorted(order)==list(range(N))
    available=set(K)
    matched={}
    for v in order:
        b=1<<v
        for low in sorted(available):
            if low&b:continue
            high=low|b
            if high in available:
                matched[low]=high
                available.remove(low);available.remove(high)
    critical=Counter(mask.bit_count()-1 for mask in available)
    assert critical==Counter({expected_dimension:expected_number}),critical
    # Verify acyclicity by explicitly directing EVERY Hasse incidence.
    indegree={f:0 for f in K}
    forward={f:[] for f in K}
    incidence_count=0
    for high in K:
        q=high
        while q:
            bit=q&-q;q-=bit
            low=high^bit
            assert low in K
            u,v=(low,high) if matched.get(low)==high else (high,low)
            forward[u].append(v)
            indegree[v]+=1
            incidence_count+=1
    frontier=deque(m for m,d in indegree.items() if d==0)
    removed=0
    while frontier:
        a=frontier.popleft();removed+=1
        for b in forward[a]:
            indegree[b]-=1
            if indegree[b]==0:frontier.append(b)
    assert removed==len(K),(removed,len(K))
    assert len(matched)*2+sum(critical.values())==len(K)
    return len(matched),incidence_count

def check_collapse(upper,lower,certificate):
    assert lower <= upper
    pairs=json.loads((ROOT/certificate).read_text('utf-8'))
    current=set(upper)
    assert len(pairs)*2==len(upper)-len(lower)
    for step,(lo,hi) in enumerate(pairs):
        assert lo in current and hi in current and lo not in lower and hi not in lower,(step,lo,hi)
        assert (hi^lo).bit_count()==1 and lo & hi==lo,(step,lo,hi)
        immediate=[lo|(1<<j) for j in range(N) if not ((lo>>j)&1)
                    and (lo|(1<<j)) in current]
        assert immediate==[hi],(step,lo,hi,immediate)
        current.remove(lo)
        current.remove(hi)
    assert current==lower,(len(current),len(lower))
    return len(pairs)

def mod2_rank(columns):
    pivots={}
    for column in columns:
        value=column
        while value:
            pivot=value.bit_length()-1
            if pivot in pivots:value ^= pivots[pivot]
            else:
                pivots[pivot]=value
                break
    return len(pivots)

def mod2_reduced_homology(K):
    degrees={d:sorted(mask for mask in K if mask.bit_count()-1==d)
             for d in range(-1,N)}
    ranks={}
    for d in range(0,N):
        above=degrees[d]
        if not above:ranks[d]=0;continue
        below={mask:i for i,mask in enumerate(degrees[d-1])}
        cols=[]
        for cell in above:
            q=cell;column=0
            while q:
                b=q&-q;q-=b
                column ^= 1<<below[cell^b]
            cols.append(column)
        ranks[d]=mod2_rank(cols)
    return {d:len(degrees[d])-ranks.get(d,0)-ranks.get(d+1,0)
            for d in range(-1,N) if degrees[d] and len(degrees[d])-ranks.get(d,0)-ranks.get(d+1,0)!=0}

def main():
    stages=faces_by_stage()
    assert check_collapse(stages[2],stages[1],"gr_collapse_1_2.json")==105
    assert check_collapse(stages[3],stages[2],"gr_collapse_2_3.json")==90
    for r in ORDERS:
        dim,num=SPHERES[r]
        matched,incidences=check_morse(stages[r],ORDERS[r],dim,num)
        print(f"stage {r}: faces={len(stages[r])} paired={matched} critical={num} in dimension {dim}, incidences={incidences}")
    for r in range(1,12):
        betti=mod2_reduced_homology(stages[r])
        want={} if r==11 else {SPHERES[r][0]:SPHERES[r][1]}
        assert betti==want,(r,betti,want)
        print(f"stage {r}: reduced mod-two Betti numbers {betti}")
    print('GROETZSCH_HIGHER_INDEPENDENCE_FILTRATION_CHECKS_OK')

if __name__=='__main__':main()
