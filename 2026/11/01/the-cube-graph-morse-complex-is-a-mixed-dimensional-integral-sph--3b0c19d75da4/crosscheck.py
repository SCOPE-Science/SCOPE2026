"""Independent edge-state enumeration and binary boundary-rank cross-check."""
from collections import Counter
V = tuple(range(8))
E = tuple((u,v) for u in V for v in V if u<v and (u^v).bit_count()==1)
ARCS = tuple((u,v) for u,v in E for u,v in ((u,v),(v,u)))
ARCINDEX = {arc:i for i,arc in enumerate(sorted(ARCS))}
F=[set() for _ in range(7)]
next_vertex=[-1]*8

def add_edge(i,chosen):
    if i==len(E):
        if chosen:
            simplex=tuple(sorted(chosen))
            F[len(simplex)-1].add(simplex)
        return
    u,v=E[i]
    add_edge(i+1,chosen)
    for tail,head in ((u,v),(v,u)):
        if next_vertex[tail]!=-1:
            continue
        z=head
        while z!=-1 and z!=tail:
            z=next_vertex[z]
        if z==tail:
            continue
        next_vertex[tail]=head
        chosen.append(ARCINDEX[(tail,head)])
        add_edge(i+1,chosen)
        chosen.pop()
        next_vertex[tail]=-1

add_edge(0,[])
assert [len(s) for s in F]==[24,240,1296,4080,7488,7424,3072]

def binary_rank(k):
    rows={face:i for i,face in enumerate(sorted(F[k-2]))}
    pivots={}
    for face in sorted(F[k-1]):
        x=0
        for i in range(len(face)):
            sub=face[:i]+face[i+1:]
            x^=1<<rows[sub]
        while x:
            p=x.bit_length()-1
            if p not in pivots:
                pivots[p]=x
                break
            x^=pivots[p]
    return len(pivots)

r5=binary_rank(6) # C_5 -> C_4
r6=binary_rank(7) # C_6 -> C_5
assert (r5,r6)==(4487,2933)
print('independent_edge_state_faces=23624')
print('binary_boundary_rank_C5_to_C4=4487')
print('binary_boundary_rank_C6_to_C5=2933')
print('mod2_top_betti=(4,139)')
print('CROSSCHECK_OK')
