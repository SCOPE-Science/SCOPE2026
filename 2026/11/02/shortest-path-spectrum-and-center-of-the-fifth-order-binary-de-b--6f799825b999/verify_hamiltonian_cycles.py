"""Independent Hamiltonian-cycle and chord-interlacement reconstruction.

We enumerate 32-state de Bruijn digraph Hamiltonian cycles starting at 00000,
not the 65,536 feedback tables. Neighbors are found by alternating positions
of two conjugate pairs around the cycle, not by precomputed graph edges.
"""
from collections import Counter, deque

n = 32
path=[0]
cycles=[]
count_search_nodes=0

def walk(v,seen):
    global count_search_nodes
    count_search_nodes += 1
    if len(path) == n:
        if (2*(v&15)) == 0 or (2*(v&15)+1) == 0:
            cycles.append(tuple(path))
        return
    for b in (0,1):
        nxt=2*(v&15)+b
        if not seen & (1<<nxt):
            path.append(nxt)
            walk(nxt, seen|(1<<nxt))
            path.pop()

walk(0,1)
assert len(cycles) == 2048
cycle_by_mask={}
positions={}
for cycle in cycles:
    succ={cycle[i]:cycle[(i+1)%n] for i in range(n)}
    assert len(succ)==n
    assert all(succ[x]>>1 == (x&15) for x in range(n))
    assert all(((succ[z]&1)^(succ[z+16]&1))==1 for z in range(16))
    mask=sum((succ[z]&1)<<z for z in range(16))
    assert mask not in cycle_by_mask
    cycle_by_mask[mask]=cycle
    positions[mask]={x:i for i,x in enumerate(cycle)}
assert len(cycle_by_mask)==2048
masks=sorted(cycle_by_mask)
idx={f:i for i,f in enumerate(masks)}
neighbor=[[] for _ in masks]
# Chord-crossing test: the two positions of conjugates of i separate
# those of conjugates of j on the circular Hamiltonian cycle.
for f in masks:
    p=positions[f]
    a=neighbor[idx[f]]
    for i in range(16):
        lo,hi=sorted((p[i],p[i+16]))
        for j in range(i+1,16):
            cross=((lo<p[j]<hi) != (lo<p[j+16]<hi))
            g=f^(1<<i)^(1<<j)
            assert cross == (g in idx)
            if cross:a.append(idx[g])
assert all(i in neighbor[j] for i,a in enumerate(neighbor) for j in a)
assert sum(map(len,neighbor))//2==38704
shells=Counter()
ecc=Counter()
for root in range(len(masks)):
    distances=[-1]*len(masks)
    distances[root]=0
    queue=deque([root])
    while queue:
        i=queue.popleft()
        for j in neighbor[i]:
            if distances[j]<0:
                distances[j]=distances[i]+1
                queue.append(j)
    assert -1 not in distances
    assert all(distances[j]==(masks[root]^masks[j]).bit_count()//2 for j in range(len(masks)))
    ecc[max(distances)]+=1
    for j in range(root+1,len(masks)):
        shells[distances[j]]+=1
assert [shells[i] for i in range(1,8)]==[38704,305376,758800,710976,254800,27104,368]
assert sorted(ecc.items())==[(5,48),(6,1264),(7,736)]
print('DIRECT_HAMILTONIAN_DFS_2048_CYCLES_AND_92636_PREFIX_NODES_PASS')
print('CIRCULAR_CONJUGATE_CHORD_INTERLACEMENT_38704_CROSS_JOINS_PASS')
print('ALL_2048_BFS_HAMMING_METRIC_AND_DISTANCE_SPECTRUM_PASS')
print('INDEPENDENT_RADIUS5_CENTER48_DIAMETER7_PASS')
