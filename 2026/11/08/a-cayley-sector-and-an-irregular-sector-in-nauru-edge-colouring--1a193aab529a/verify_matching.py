"""Independent matching/2-factor enumeration for the named edge-Kempe graph of GP(12,5).
Run: python verify_matching.py  (Python >=3.9, standard library only).
"""
from collections import Counter, deque
from itertools import combinations

N=24
EDGES=tuple(sorted({tuple(sorted((i,(i+1)%12))) for i in range(12)} |
                   {tuple(sorted((i,i+12))) for i in range(12)} |
                   {tuple(sorted((12+i,12+(i+5)%12))) for i in range(12)}))
assert len(EDGES)==36
INC=[[] for _ in range(N)]
for j,(u,v) in enumerate(EDGES):
    INC[u].append((v,j)); INC[v].append((u,j))
assert all(len(x)==3 for x in INC)

# Every color-zero class must be a perfect matching.  Its complementary
# two-factor must have even cycles, which can be alternately colored 1 and 2.
matchings=[]
def extend(used, chosen):
    if used==(1<<N)-1:
        matchings.append(tuple(chosen)); return
    v=next(v for v in range(N) if not used&(1<<v))
    for w,e in INC[v]:
        if not used&(1<<w): extend(used|(1<<v)|(1<<w), chosen+[e])
extend(0,[])
assert len(matchings)==120

def comp_cycles(removed):
    removed=set(removed); visited=set(); out=[]
    for v in range(N):
        if v in visited: continue
        walk=[]; start=v; prev=-1
        while v not in visited:
            visited.add(v)
            choices=[(w,e) for w,e in INC[v] if e not in removed and w!=prev]
            assert len(choices)==(2 if prev==-1 else 1)
            w,e=choices[0]
            walk.append(e); prev,v=v,w
        assert v==start
        out.append(tuple(walk))
    assert sum(map(len,out))==24
    return out

config=set()
for m in matchings:
    cycles=comp_cycles(m)
    if any(len(x)%2 for x in cycles): continue
    for choices in range(1<<len(cycles)):
        table=[-1]*36
        for e in m: table[e]=0
        for j,cycle in enumerate(cycles):
            for k,e in enumerate(cycle): table[e]=1+((k+(choices>>j&1))%2)
        assert set(table)=={0,1,2}
        config.add(tuple(table))
state=sorted(config); index={c:i for i,c in enumerate(state)}
assert len(state)==504

#  A legal move swaps two colors on one WHOLE bichromatic cycle.
def cycles_of(c,p,q):
    active={e for e in range(36) if c[e] in (p,q)}
    visited=set(); out=[]
    for first in sorted(active):
        if first in visited: continue
        queue=[first]; visited.add(first); part=[]
        while queue:
            e=queue.pop(); part.append(e)
            for v in EDGES[e]:
                for _,a in INC[v]:
                    if a in active and a not in visited:
                        visited.add(a); queue.append(a)
        out.append(part)
    assert sum(map(len,out))==24
    return out

adj=[set() for _ in state]
types=Counter()
for j,c in enumerate(state):
    signature=[]
    for p,q in combinations((0,1,2),2):
        cycles=cycles_of(c,p,q)
        signature.append(tuple(sorted(len(t) for t in cycles)))
        for cycle in cycles:
            a=list(c)
            for e in cycle:a[e]=q if c[e]==p else p
            target=tuple(a)
            assert target in index
            adj[j].add(index[target])
    types[tuple(sorted(signature))]+=1
assert all(j in adj[i] for i,neigh in enumerate(adj) for j in neigh)
assert sum(map(len,adj))//2==1674
assert Counter(map(len,adj))=={6:354,8:144,12:6}

components=[]; done=set()
for start in range(len(state)):
    if start in done: continue
    found=[start]; done.add(start)
    for v in found:
        for w in sorted(adj[v]):
            if w not in done: done.add(w); found.append(w)
    components.append(found)
assert sorted(map(len,components))==[144,360]
short=next(c for c in components if len(c)==144)
large=next(c for c in components if len(c)==360)

# Bichromatic invariant: one 10-cycle occurs iff ALL 3 factors are 10+14.
def typ(c):return tuple(sorted(tuple(sorted(map(len,cycles_of(c,p,q))))
                               for p,q in combinations((0,1,2),2)))
tenfour=((10,14),)*3
assert all(typ(state[i])==tenfour for i in short)
assert all(10 not in [z for factor in typ(state[i]) for z in factor] for i in large)
assert types[tenfour]==144

pair_counts={}
for component in components:
    ecc=Counter(); pairs=Counter(); shells=Counter()
    for s in component:
        dist={s:0}; fifo=deque([s])
        while fifo:
            v=fifo.popleft()
            for w in adj[v]:
                if w not in dist:dist[w]=dist[v]+1;fifo.append(w)
        assert len(dist)==len(component)
        ecc[max(dist.values())]+=1
        shells[tuple(Counter(dist.values()).get(k,0) for k in range(max(dist.values())+1))]+=1
        pairs.update(d for d in dist.values() if d>0)
    pairs=tuple(pairs.get(i,0)//2 for i in range(1,max(ecc)+1))
    pair_counts[len(component)]=pairs
    if len(component)==144:
        assert ecc=={4:144}
        assert pairs==(432,1944,4752,3168)
        assert shells=={(1,6,27,66,44):144}
    else:
        assert ecc=={5:330,6:30}
        assert pairs==(1242,5904,18981,31401,6732,360)
assert len(short)==144 and len(large)==360
# A separate parity lift detects an odd cycle without relying on a graph library.
def odd_girth(component):
    best=10**9
    for start in component:
        distance={(start,0):0}; queue=deque([(start,0)])
        while queue:
            v,p=queue.popleft()
            for w in adj[v]:
                key=(w,1-p)
                if key not in distance:
                    distance[key]=distance[v,p]+1
                    queue.append(key)
        best=min(best,distance.get((start,1),10**9))
    return best
assert odd_girth(short)==10**9
assert odd_girth(large)==5

# Concrete automorphisms: shift of GP indices, reflection and alpha.
shift=tuple((i+1)%12 for i in range(12))+tuple(12+(i+1)%12 for i in range(12))
reflection=tuple((-i)%12 for i in range(12))+tuple(12+(-i)%12 for i in range(12))
alpha=(0,11,23,16,4,3,15,20,8,7,19,12,1,10,18,21,5,2,22,13,9,6,14,17)
G=(shift,reflection,alpha)
ES=set(EDGES)
for g in G:
    assert set(g)==set(range(N))
    assert {tuple(sorted((g[u],g[v]))) for u,v in EDGES}==ES

def mult(a,b): return tuple(a[b[v]] for v in range(N))
ID=tuple(range(N)); group={ID}; queue=[ID]
for h in queue:
    for g in G:
        f=mult(h,g)
        if f not in group:group.add(f);queue.append(f)
assert len(group)==144
edgeindex={e:i for i,e in enumerate(EDGES)}
def act(h,c):
    out=[None]*len(c)
    for i,(u,v) in enumerate(EDGES):
        e=edgeindex[tuple(sorted((h[u],h[v])))]
        out[e]=c[i]
    return tuple(out)
base=state[short[0]]
orbit={act(h,base):h for h in group}
assert len(orbit)==144 and set(orbit)=={state[i] for i in short}
# Thus the group is a regular subgroup of the small component's automorphism group.
nearby=[orbit[state[j]] for j in adj[index[base]]]
assert len(nearby)==6
for g in nearby:
    assert mult(g,g)==ID  # Six involutory Cayley generators.
print('NAURU_MATCHING_VERIFIER_PASS 120 matchings 504 named states 1674 edges')
print('NAURU_SECTORS_PASS 144_CAYLEY_6_REGULAR_DIAM4 360_MIXED_RADIUS5_DIAM6')
print('NAURU_SYMMETRY_PASS 144-element regular subgroup, six involutions')
print('NAURU_PAIR_DISTS_PASS',pair_counts)
