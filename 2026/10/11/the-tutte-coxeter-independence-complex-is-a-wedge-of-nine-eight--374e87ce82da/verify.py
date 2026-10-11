from itertools import combinations
from collections import deque, Counter
import hashlib, json, time

# Canonical duad-syntheme model of the Tutte-Coxeter graph.
base=range(6)
duads=list(combinations(base,2))
# perfect matchings of K6, canonical tuples of sorted pairs

def perfect_matchings(items):
    items=tuple(items)
    if not items:
        yield (); return
    a=items[0]
    for i in range(1,len(items)):
        b=items[i]
        rest=items[1:i]+items[i+1:]
        for tail in perfect_matchings(rest):
            yield tuple(sorted(((min(a,b),max(a,b)),)+tail))
synthemes=sorted(set(perfect_matchings(tuple(base))))
assert len(duads)==15 and len(synthemes)==15
labels=[f'd{a}{b}' for a,b in duads]+['s'+'.'.join(f'{a}{b}' for a,b in s) for s in synthemes]
N=30
adj=[0]*N
edges=[]
for i,d in enumerate(duads):
    for j,s in enumerate(synthemes):
        if d in s:
            u,v=i,15+j
            adj[u]|=1<<v; adj[v]|=1<<u; edges.append((u,v))
assert len(edges)==45
assert all(a.bit_count()==3 for a in adj)
# girth via BFS from each root
INF=10**9
girth=INF
for root in range(N):
    dist=[-1]*N; par=[-1]*N; dist[root]=0; q=deque([root])
    while q:
        u=q.popleft()
        nb=adj[u]
        while nb:
            bit=nb & -nb; v=bit.bit_length()-1; nb-=bit
            if dist[v]<0:
                dist[v]=dist[u]+1; par[v]=u; q.append(v)
            elif par[u]!=v:
                girth=min(girth,dist[u]+dist[v]+1)
assert girth==8

# Enumerate every independent set, including the empty set.
faces=[]
def enum_ind(avail, chosen):
    if not avail:
        faces.append(chosen); return
    b=avail & -avail; v=b.bit_length()-1
    enum_ind(avail ^ b, chosen)
    enum_ind((avail ^ b) & ~adj[v], chosen | b)
enum_ind((1<<N)-1,0)
assert len(faces)==476187
face_set=set(faces)
assert len(face_set)==len(faces)
counts=Counter(m.bit_count() for m in faces)
face_vector=tuple(counts[k] for k in range(1,max(counts)+1))
EXPECTED_F=(30,390,2890,13515,41736,86610,120690,111225,66090,24948,6420,1370,240,30,2)
assert face_vector==EXPECTED_F
chi=sum(((-1)**(k-1))*counts[k] for k in range(1,max(counts)+1))
assert chi==10 and chi-1==9

# Successive element-toggle matching on the nonempty face poset.
unpaired=set(face_set); unpaired.remove(0)
low_to_high={}; high_to_low={}; stage={}
for v in range(N):
    bit=1<<v
    # Snapshot is important: only currently-unmatched faces can be paired.
    lows=[]
    for m in unpaired:
        if m & bit: continue
        h=m|bit
        if h in unpaired and (adj[v] & m)==0:
            lows.append(m)
    for m in lows:
        h=m|bit
        if m in unpaired and h in unpaired:
            unpaired.remove(m); unpaired.remove(h)
            low_to_high[m]=h; high_to_low[h]=m; stage[m]=stage[h]=v
assert len(low_to_high)==238088
critical=sorted(unpaired)
crit_sizes=Counter(m.bit_count() for m in critical)
assert crit_sizes==Counter({1:1,9:9})

# Every matching pair is a valid Hasse edge.
for lo,hi in low_to_high.items():
    x=hi^lo
    assert x and x&(x-1)==0 and (lo & x)==0
    assert lo in face_set and hi in face_set
    assert hi.bit_count()==lo.bit_count()+1

# Direct acyclicity verification by Kahn topological sorting of the entire Morse-oriented Hasse graph.
nonempty=[m for m in faces if m]
idx={m:i for i,m in enumerate(nonempty)}
indeg=[0]*len(nonempty)
hasse=0
for hi in nonempty:
    t=hi
    while t:
        b=t&-t; lo=hi^b; t-=b
        if not lo: continue
        hasse+=1
        if low_to_high.get(lo)==hi:
            indeg[idx[lo]]+=1  # matched edge reverses hi -> lo
        else:
            indeg[idx[hi]]+=1  # unmatched edge lo -> hi
assert hasse==3461400
q=deque(i for i,d in enumerate(indeg) if d==0)
seen=0
while q:
    i=q.popleft(); m=nonempty[i]; seen+=1
    # reversed matched edge from an upper cell to its lower partner
    lo=high_to_low.get(m)
    if lo is not None:
        j=idx[lo]; indeg[j]-=1
        if indeg[j]==0:q.append(j)
    # unmatched upward Hasse edges
    forbidden=0
    mm=m
    while mm:
        b=mm&-mm; forbidden |= adj[b.bit_length()-1]; mm-=b
    addable=((1<<N)-1) & ~m & ~forbidden
    t=addable
    while t:
        b=t&-t; t-=b
        hi=m|b
        if hi not in face_set: raise AssertionError('addable face missing')
        if low_to_high.get(m)==hi:
            continue
        j=idx[hi]; indeg[j]-=1
        if indeg[j]==0:q.append(j)
assert seen==len(nonempty), (seen,len(nonempty))
assert all(x==0 for x in indeg)

crit_labels=[]
for m in critical:
    crit_labels.append([labels[i] for i in range(N) if (m>>i)&1])
summary={
 'graph':'Tutte-Coxeter graph as duad-syntheme incidence graph',
 'vertices':N,'edges':len(edges),'girth':girth,
 'nonempty_faces':len(nonempty),'face_vector':face_vector,
 'matched_pairs':len(low_to_high),'critical_cell_dimensions':{str(k-1):v for k,v in sorted(crit_sizes.items())},
 'hasse_covers':hasse,'euler_characteristic':chi,'reduced_euler_characteristic':chi-1,
 'critical_simplices':crit_labels,
}
print(json.dumps(summary,sort_keys=True))
print('ACYCLIC_MATCHING_OK')
print('VERIFY_OK')
