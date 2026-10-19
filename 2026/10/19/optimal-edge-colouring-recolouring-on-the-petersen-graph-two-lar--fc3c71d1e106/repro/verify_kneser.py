#!/usr/bin/env python3
"""Independent enumerator using the Kneser KG(5,2) construction and vertex-incidence bitmasks.
Tests one-edge recolouring components, frozen orbit and the parity action of graph automorphisms.
Only the Python standard library is required.
"""
from itertools import combinations, permutations
from collections import Counter
V = tuple(combinations(range(5), 2))
N = len(V)
E = tuple((a,b) for a in range(N) for b in range(a+1,N) if set(V[a]).isdisjoint(V[b]))
assert N == 10 and len(E) == 15
used = [0] * N
assignment = [0] * 15
S=[]

def enumerate_states(i):
    if i==len(E):
        S.append(tuple(assignment)); return
    a,b=E[i]
    forbidden=used[a]|used[b]
    for c in range(4):
        bit=1<<c
        if forbidden & bit:continue
        assignment[i]=c
        used[a]|=bit;used[b]|=bit
        enumerate_states(i+1)
        used[a]^=bit;used[b]^=bit

enumerate_states(0)
assert len(S)==49920
key={s:i for i,s in enumerate(S)}
assert len(key)==len(S)
parent=list(range(len(S)))
sizes=[1]*len(S)

def find(i):
    while parent[i]!=i:
        parent[i]=parent[parent[i]];i=parent[i]
    return i

def join(i,j):
    i,j=find(i),find(j)
    if i==j:return
    if sizes[i]<sizes[j]:i,j=j,i
    parent[j]=i;sizes[i]+=sizes[j]

edge_count2=0
missing_colour_degree_histogram=Counter()
for state_i,s in enumerate(S):
    palette=[0]*N
    for ei,(a,b) in enumerate(E):
        flag=1<<s[ei]
        assert not(palette[a]&flag) and not(palette[b]&flag)
        palette[a]|=flag;palette[b]|=flag
    missing = [next(c for c in range(4) if not (palette[v] & (1<<c))) for v in range(N)]
    missing_colour_degree_histogram[sum(missing[a]==missing[b] for a,b in E)]+=1
    for ei,(a,b) in enumerate(E):
        possible=(15^(palette[a]|palette[b]))
        for new in range(4):
            if not (possible & (1<<new)):continue
            t=list(s);t[ei]=new;t=tuple(t)
            assert t in key
            join(state_i,key[t]);edge_count2+=1
assert edge_count2%2==0
C=Counter(find(i) for i in range(len(S)))
hist=Counter(C.values())
assert edge_count2//2==109440
assert missing_colour_degree_histogram[0]==960
assert sum(k*v for k,v in missing_colour_degree_histogram.items())==edge_count2
assert hist==Counter({1:960,24480:2})
frozen={S[i] for i in range(len(S)) if C[find(i)]==1}
assert len(frozen)==960

v_index={v:i for i,v in enumerate(V)}
e_index={frozenset(x):i for i,x in enumerate(E)}
perm4=list(permutations(range(4)))
perm5=list(permutations(range(5)))

def edge_permutation(p):
    vimage=[v_index[tuple(sorted((p[a],p[b])))] for a,b in V]
    return [e_index[frozenset((vimage[a],vimage[b]))] for a,b in E]

def transformed(s,pedge,pcolors=(0,1,2,3)):
    t=[0]*len(E)
    for i in range(len(E)):
        t[pedge[i]]=pcolors[s[i]]
    return tuple(t)

# The first frozen state generates the entire frozen locus under S5 times S4.
seed=min(frozen)
orbit=set()
for p in perm5:
    edge_map=edge_permutation(p)
    for pc in perm4:
        orbit.add(transformed(seed,edge_map,pc))
assert orbit == frozen

large_roots=[r for r,size in C.items() if size==24480]
reps={r:next(s for s in S if find(key[s])==r) for r in large_roots}
for r,rep in reps.items():
    # All palette relabellings preserve each large component.
    for pc in perm4:
        assert find(key[tuple(pc[c] for c in rep)])==r
    even=odd=0
    for p in perm5:
        image=transformed(rep,edge_permutation(p))
        target=find(key[image])
        inversions=sum(p[i]>p[j] for i in range(5) for j in range(i+1,5))
        if inversions%2:
            odd+=1
            assert target!=r and C[target]==24480
        else:
            even+=1
            assert target==r
    assert even==60 and odd==60
assert len(large_roots)==2
print('representation=Kneser KG(5,2)')
print('vertices=' + repr(V))
print('edges=' + repr(E))
print('states=49920')
print('reconfiguration_edges=109440')
print('components=962')
print('component_size_histogram=' + repr(sorted(hist.items())))
print('missing_colour_degree_histogram=' + repr(sorted(missing_colour_degree_histogram.items())))
print('frozen_orbit_size=' + str(len(orbit)))
print('frozen_seed=' + repr(seed))
print('palette_permutations_preserve_large_components=True')
print('even_S5_preserves_odd_S5_interchanges_large_components=True')
print('large_component_internal_edges=54720_each')
print('VERIFY_OK')
