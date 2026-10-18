#!/usr/bin/env python3
"""Exact facet and S5 x C2 orbit checks for the T5 transportation ball."""
from itertools import combinations, permutations, product
from collections import Counter
V = tuple(combinations(range(5), 2))
I = {p:i for i,p in enumerate(V)}
E = tuple((i,j) for i in range(10) for j in range(i+1,10) if set(V[i]) & set(V[j]))
assert len(V)==10 and len(E)==30


def tight_data(f):
    if min(f)!=0 or max(f)==0: return None
    if any(abs(f[i]-f[j])>1 for i,j in E): return None
    adj = [[] for _ in V]
    for i,j in E:
        if abs(f[i]-f[j])==1:
            adj[i].append(j)
            adj[j].append(i)
    touched = {0}
    todo = [0]
    while todo:
        for j in adj[todo.pop()]:
            if j not in touched:
                touched.add(j)
                todo.append(j)
    if len(touched)!=10: return None
    return sum(len(xs) for xs in adj)//2

# Global finite search: normalization by the minimum makes all extreme
# potentials belong to {0,1,2}^10, since T5 has diameter two.
facets = {}
for f in product((0,1,2),repeat=10):
    t=tight_data(f)
    if t is not None: facets[f]=t
assert len(facets)==1032
assert Counter(facets.values())=={12:110,14:300,16:330,18:280,20:12}
assert Counter(max(f) for f in facets)=={1:922,2:110}

# Independent candidate enumeration of the two- and three-level cases.
cut_facets={}
for mask in range(1,(1<<10)-1):
    f=tuple((mask>>i)&1 for i in range(10))
    t=tight_data(f)
    if t is not None:cut_facets[f]=t
assert len(cut_facets)==922

triple_facets={}
for a_mask in range(1,1<<10):
    A={i for i in range(10) if (a_mask>>i)&1}
    possible=[j for j in range(10) if j not in A and all((min(i,j),max(i,j)) not in E for i in A)]
    for b_mask in range(1,1<<len(possible)):
        B={possible[k] for k in range(len(possible)) if (b_mask>>k)&1}
        f=tuple(0 if i in A else 2 if i in B else 1 for i in range(10))
        t=tight_data(f)
        if t is not None: triple_facets[f]=t
assert len(triple_facets)==110
assert facets==dict(cut_facets,**{}) | triple_facets

# The true graph automorphism group is S5: a clique of size four in T5
# is exactly a star of four pairs through one ground-set point.
perms=[]
for sigma in permutations(range(5)):
    p=tuple(I[tuple(sorted((sigma[i],sigma[j])))] for i,j in V)
    perms.append(p)
assert len(set(perms))==120

def image(f,p):
    g=[0]*10
    for i,j in enumerate(p):g[j]=f[i]
    return tuple(g)

def negate(f):
    h=max(f)
    return tuple(h-x for x in f)

visited=set()
orbits=[]
for f in sorted(facets):
    if f in visited:continue
    orb=set()
    for p in perms:
        g=image(f,p)
        orb.add(g)
        orb.add(negate(g))
    assert orb.issubset(facets)
    assert not (orb & visited)
    assert len({facets[x] for x in orb})==1
    visited.update(orb)
    orbits.append((len(orb),facets[f],max(f)+1, f))
assert visited==set(facets)
assert len(orbits)==17
assert Counter(n for n,t,h,f in orbits)=={120:5,60:4,40:1,30:3,20:2,12:1,10:1}
assert sum(n for n,t,h,f in orbits)==1032

# Independent Burnside count for all 240 symmetries.
fixed=0
for p in perms:
    for s in (0,1):
        fixed+=sum((negate(image(f,p)) if s else image(f,p))==f for f in facets)
assert fixed==17*240

# The maximally incident facets are the two-colorings into complementary
# Hamiltonian five-cycles of K5.
maxfac={f for f,t in facets.items() if t==20}
cycles=[]
for edge_set in combinations(range(10),5):
    deg=[0]*5
    for i in edge_set:
        a,b=V[i];deg[a]+=1;deg[b]+=1
    if deg==[2]*5:
        cycles.append(frozenset(edge_set))
assert len(cycles)==12
max_by_cycles={tuple(int(i not in C) for i in range(10)) for C in cycles}
assert maxfac==max_by_cycles

print('ALL EXACT CHECKS PASSED')
print('facets',len(facets),'orbits',len(orbits),'max_incidence',max(facets.values()))
print('incidence',sorted(Counter(facets.values()).items()))
print('levels',sorted(Counter(max(f)+1 for f in facets).items()))
print('orbit_sizes',sorted((n for n,t,h,f in orbits),reverse=True))
print('orbit_data (size, facet-vertex-count, levels, representative)')
for row in sorted(orbits,key=lambda x:(-x[0],x[1],x[3])): print(row)
