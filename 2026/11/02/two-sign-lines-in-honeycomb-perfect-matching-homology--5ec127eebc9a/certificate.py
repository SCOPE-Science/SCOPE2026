#!/usr/bin/env python3
"""Exact finite verification for a symmetric honeycomb perfect-matching complex.
Pure Python 3.10+; no external dependencies or network. """
import collections
from itertools import combinations

RADIUS = 2
P = frozenset((i,j) for i in range(-RADIUS,RADIUS+1)
                 for j in range(-RADIUS,RADIUS+1) if abs(i+j) <= RADIUS)
triangles = set()
for i in range(-RADIUS-1,RADIUS+2):
    for j in range(-RADIUS-1,RADIUS+2):
        t1=frozenset(((i,j),(i+1,j),(i,j+1)))
        t2=frozenset(((i+1,j+1),(i+1,j),(i,j+1)))
        if t1 <= P: triangles.add(t1)
        if t2 <= P: triangles.add(t2)
V=tuple(sorted(triangles,key=lambda t:tuple(sorted(t))))
E=tuple((i,j) for i in range(len(V)) for j in range(i+1,len(V)) if len(V[i]&V[j])==2)
assert len(V)==24 and len(E)==30
nbr=[[] for _ in V]
for idx,(u,v) in enumerate(E):
    nbr[u].append((v,idx));nbr[v].append((u,idx))
assert sorted(map(len,nbr))==[2]*12+[3]*12

def enumerate_matchings(remaining, mask=0):
    if not remaining:
        yield mask
        return
    u=min(remaining)
    for v,e in nbr[u]:
        if v in remaining:
            yield from enumerate_matchings(remaining-{u,v},mask | (1<<e))
M=set(enumerate_matchings(frozenset(range(len(V)))))
assert len(M)==20 and all(m.bit_count()==12 for m in M)
# Exhaustive down-closure. Here zero denotes the augmented empty face.
F={0}
for m in M:
    sub=m
    while sub:
        F.add(sub)
        sub=(sub-1)&m
assert len(F)==66370
assert [sum(v.bit_count()==k for v in F) for k in range(1,13)] == [
    30,357,1966,6069,11892,15807,14688,9612,4368,1320,240,20]
assert sum((-1)**(v.bit_count()-1) for v in F if v)==-1

# Greedy ordered element-toggle Morse matching on the ordinary (nonaugmented)
# face poset. No empty-face matching is used.
remaining=F-{0}
paired=set()
for e in range(len(E)):
    bit=1<<e
    for lower in tuple(remaining):
        if not (lower&bit) and (lower|bit) in remaining:
            remaining.remove(lower)
            remaining.remove(lower|bit)
            paired.add((lower,lower|bit))
assert len(paired)==33183, len(remaining)==3
assert sorted(v.bit_count()-1 for v in remaining)==[0,3,3]

# Complete exact acyclicity test of the directed Hasse graph: matched edges up,
# all other cover edges down. No finite/truncated search is involved.
F_nonempty=F-{0}
indegree={v:0 for v in F_nonempty}
arcs=collections.defaultdict(list)
cover_count=0
for upper in F_nonempty:
    t=upper
    while t:
        bit=t&-t
        t-=bit
        lower=upper^bit
        if lower==0: continue
        if (lower,upper) in paired:
            src,dst=lower,upper
        else:
            src,dst=upper,lower
        indegree[dst]+=1
        arcs[src].append(dst)
        cover_count+=1
queue=collections.deque([x for x,d in indegree.items() if d==0])
visited=0
while queue:
    u=queue.popleft();visited+=1
    for v in arcs[u]:
        indegree[v]-=1
        if indegree[v]==0:queue.append(v)
assert visited==len(F_nonempty), (visited,len(F_nonempty))
assert cover_count==sum(v.bit_count() if v.bit_count()>1 else 0 for v in F_nonempty)
# Forman's theorem gives the wedge S^3 v S^3, independently of the paper.

vindex={v:i for i,v in enumerate(V)}
eindex={e:i for i,e in enumerate(E)}
def image_point(p,op):
    i,j=p
    if op=='r':return (-j,i+j)
    if op=='s':return (j,i)
    raise ValueError(op)
def on_edges(op):
    vperm=[vindex[frozenset(image_point(p,op) for p in t)] for t in V]
    return tuple(eindex[tuple(sorted((vperm[u],vperm[v])))] for u,v in E)
def compose(a,b):
    return tuple(a[b[i]] for i in range(len(E)))
r=on_edges('r');s=on_edges('s');iden=tuple(range(len(E)))
rot=[iden]
for i in range(1,6):rot.append(compose(r,rot[-1]))
assert compose(r,rot[-1])==iden
assert compose(s,s)==iden
assert compose(s,compose(r,s))==rot[-1]
group=[('r',i,p) for i,p in enumerate(rot)] + [('s',i,compose(s,p)) for i,p in enumerate(rot)]
assert len({p for _,_,p in group})==12
assert all({sum(1<<p[e] for e in range(30) if (m>>e)&1) for m in M}==M for _,_,p in group)

def sign_orbit_perm(targets):
    # targets are distinct edge indices of an invariant face, ordered by its
    # original vertices: number of inversions is the cellular orientation.
    return -1 if sum(targets[i]>targets[j]
                     for i in range(len(targets)) for j in range(i+1,len(targets))) % 2 else 1

def direct_lefschetz(p):
    # Every face, every dimension, and the orientation sign are checked.
    total=-1  # reduced chain has one empty face with sign -1
    fixed_by_dim=collections.Counter()
    for mask in F_nonempty:
        t=mask
        images=[]
        im_mask=0
        while t:
            bit=t&-t
            t-=bit
            e=bit.bit_length()-1
            j=p[e];images.append(j);im_mask |= 1<<j
        if im_mask==mask:
            d=mask.bit_count()-1
            contribution=(-1)**d*sign_orbit_perm(images)
            total+=contribution
            fixed_by_dim[d]+=contribution
    return total,dict(sorted(fixed_by_dim.items()))

def orbit_lefschetz(p):
    # Independent orbitwise enumeration: invariant faces are unions of cycles
    # of p on the 30 edge-vertices. Test them by containment in maximal faces.
    unvisited=set(range(30));cycles=[]
    while unvisited:
        x=min(unvisited);cyc=[];y=x
        while y not in cyc:
            cyc.append(y);unvisited.remove(y);y=p[y]
        assert y==x
        cycles.append(tuple(cyc))
    cycle_masks=[sum(1<<v for v in c) for c in cycles]
    total=-1
    # Only subsets of each perfect matching can contribute; constructing their
    # union produces every invariant face exactly once.
    inv_faces=set()
    for m in M:
        allowed=[b for b in cycle_masks if m&b==b]
        for bits in range(1,1<<len(allowed)):
            mask=0
            for j,b in enumerate(allowed):
                if (bits>>j)&1:mask|=b
            inv_faces.add(mask)
    for mask in inv_faces:
        images=[p[e] for e in range(30) if (mask>>e)&1]
        total+=(-1)**(mask.bit_count()-1)*sign_orbit_perm(images)
    return total,len(inv_faces)

characters=[]
for kind,k,p in group:
    L,by_dim=direct_lefschetz(p)
    L2,nfixed=orbit_lefschetz(p)
    assert L==L2, (kind,k,L,L2)
    trace=-L # all reduced rational homology is in degree 3
    # Proposed two dihedral linear characters alpha(r)=+1,alpha(s)=-1
    # and beta(r)=-1,beta(s)=+1.
    expected=((1 if kind=='r' else -1) + ((-1)**k if kind=='r' else (-1)**k))
    assert trace==expected,(kind,k,trace,expected)
    characters.append((kind,k,trace,L,nfixed,by_dim))
assert [x[2] for x in characters[:6]]==[2,0,2,0,2,0]
assert [x[2] for x in characters[6:]]==[0,-2,0,-2,0,-2]
assert sum(t for kind,k,t,*_ in characters)==0
assert sum(t for kind,k,t,*_ in characters[:6])//6==1
assert sum(t for kind,k,t,*_ in characters[::2][:3])//3==2
print('HONEYCOMB_222_DIHEDRAL_EXACT_OK')
print('vertices=24 edges=30 perfect_matchings=20 ordinary_nonempty_faces=66369')
print('morse_pairs=33183 critical_cell_dimensions=[0,3,3] hasse_covers=',cover_count)
print('rotation_H3_traces=',[x[2] for x in characters[:6]])
print('reflection_H3_traces=',[x[2] for x in characters[6:]])
print('signed_fixed_face_counts=',[x[4] for x in characters])
print('quotient_H3: D6=0, C6=1, C3=2, <s>=1, <sr>=0')
