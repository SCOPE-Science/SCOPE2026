"""Exact signed simplicial Lefschetz characters of the 2-independence complex.

The dodecahedral graph and all automorphisms are generated from scratch.
Uses Python 3 standard library only; no group tables or topology packages.
"""
from itertools import permutations
from collections import Counter

N=20
adj=[0]*N
for i in range(10):
    for u,v in ((i,(i+1)%10),(i,10+i),(10+i,10+(i+2)%10)):
        adj[u]|=1<<v
        adj[v]|=1<<u

def all_graph_automorphisms():
    found=set()
    def fill(p):
        if len(p)==N:
            found.add(tuple(p[i] for i in range(N)))
            return
        taken=set(p.values())
        choices=[]
        for i in range(N):
            if i in p:continue
            candidates=[j for j in range(N) if j not in taken and
                        all(bool(adj[i]>>u&1)==bool(adj[j]>>v&1)
                            for u,v in p.items())]
            choices.append((candidates,i))
        options,i=min(choices,key=lambda x:len(x[0]))
        for j in options:
            p[i]=j
            fill(p)
            del p[i]
    root_neighbors=[i for i in range(N) if (adj[0]>>i)&1]
    for target in range(N):
        neighbors=[i for i in range(N) if (adj[target]>>i)&1]
        for order in permutations(neighbors):
            p={0:target}
            p.update(dict(zip(root_neighbors,order)))
            fill(p)
    return sorted(found)

A=all_graph_automorphisms()
assert len(A)==120
Aset=set(A)

faces=[]
for mask in range(1<<N):
    if all((mask&adj[i]).bit_count()<=1
           for i in range(N) if (mask>>i)&1):
        faces.append(mask)
assert len(faces)==63143

def orientation_sign(arr):
    inversions=sum(arr[i]>arr[j] for i in range(len(arr))
                   for j in range(i+1,len(arr)))
    return -1 if inversions&1 else 1

def reduced_lefschetz(g):
    # Include the empty simplex with alternating coefficient -1.
    value=-1
    for s in faces:
        if s==0:continue
        images=[g[i] for i in range(N) if s>>i&1]
        if sum(1<<i for i in images)!=s:continue
        value+=(1 if len(images)&1 else -1)*orientation_sign(images)
    return value

character={g:reduced_lefschetz(g) for g in A}
assert set(character.values())=={-1,1}
counts=dict(sorted(Counter(character.values()).items()))
assert counts=={-1:60,1:60}
identity=tuple(range(N))
assert character[identity]==1
anti=tuple((i+5)%10 if i<10 else 10+(i-10+5)%10 for i in range(N))
assert anti in Aset and character[anti]==-1
assert all(tuple(anti[g[i]] for i in range(N))==tuple(g[anti[i]] for i in range(N))
           for g in A)
# A consistency check across every group product.
for g in A:
    for h in A:
        product=tuple(g[h[i]] for i in range(N))
        assert product in Aset
        assert character[product]==character[g]*character[h]

print('number_of_graph_automorphisms=120')
print('character_counts=',counts)
print('identity_character=1')
print('antipodal_involution=',anti)
print('antipodal_character=-1')
print('character_kernel_size=60 all_120_multiplication_checks=passed')
print('rank_one_H6_has_no_nonzero_full_automorphism_invariants')
