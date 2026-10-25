#!/usr/bin/env python3
"""Independent finite checks of the K4,4 two-matching homology symmetry character.

Reconstructs admissible faces and acyclic matching; all arithmetic exact.
"""
import itertools
import collections
from math import factorial

N = 4
EDGES = [(a,b) for a in range(N) for b in range(N)]
PERMS = list(itertools.permutations(range(N)))
IDENTITY = tuple(range(N))
ORDER = (7,2,5,10,1,11,13,9,12,15,8,0,4,3,14,6)

def perm_type(p):
    seen=set(); ans=[]
    for i in range(N):
        if i in seen: continue
        j=i; z=0
        while j not in seen:
            seen.add(j);z+=1;j=p[j]
        ans.append(z)
    return tuple(sorted(ans,reverse=True))

def perm_sign(p):
    return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))

def allowed(mask):
    r=[0]*N; c=[0]*N
    for i,(a,b) in enumerate(EDGES):
        if (mask>>i)&1:
            r[a]+=1;c[b]+=1
            if r[a]>2 or c[b]>2:return False
    return True

FACES = tuple(m for m in range(1,1<<16) if allowed(m))
FACESET = set(FACES)
assert len(FACES)==7342

def matching_certificate():
    avail=set(FACES); matched=set();pairs=[]
    for e in ORDER:
        bit=1<<e
        for m in FACES:
            if m not in avail or m&bit:continue
            high=m|bit
            if high in avail:
                avail.remove(m);avail.remove(high)
                matched.add((m,high));pairs.append((m,high))
    dim_counts=collections.Counter(m.bit_count()-1 for m in avail)
    assert len(pairs)==3663,(len(pairs),dim_counts)
    assert dim_counts=={0:1,5:15},dim_counts
    topo_edges=collections.defaultdict(list)
    indegree={m:0 for m in FACES};count=0
    for high in FACES:
        for e in range(16):
            if not(high>>e)&1:continue
            low=high^(1<<e)
            if low not in FACESET:continue
            if (low,high) in matched:
                start,end=high,low
            else:
                start,end=low,high
            topo_edges[start].append(end);indegree[end]+=1;count+=1
    assert count==37728,count
    q=collections.deque(m for m,v in indegree.items() if v==0)
    visited=0
    while q:
        m=q.popleft();visited+=1
        for x in topo_edges[m]:
            indegree[x]-=1
            if indegree[x]==0:q.append(x)
    assert visited==len(FACES),(visited,len(FACES))
    return dim_counts,len(pairs),count

def edge_perm(s,t,flip):
    return tuple((4*s[b]+t[a] if flip else 4*s[a]+t[b]) for a,b in EDGES)

def orbit_character(s,t,flip):
    mapping=edge_perm(s,t,flip);seen=set();cycle_degrees=[]
    for i in range(16):
        if i in seen:continue
        c=[];j=i
        while j not in seen:
            seen.add(j);c.append(EDGES[j]);j=mapping[j]
        r=[0]*4;h=[0]*4
        for a,b in c:r[a]+=1;h[b]+=1
        cycle_degrees.append((r,h))
    def evaluate(i,rs,cs):
        if i==len(cycle_degrees):return 1
        total=evaluate(i+1,rs,cs)
        rr,cc=cycle_degrees[i]
        newr=[x+y for x,y in zip(rs,rr)];newc=[x+y for x,y in zip(cs,cc)]
        if max(newr)<=2 and max(newc)<=2:
            total-=evaluate(i+1,newr,newc)
        return total
    return evaluate(0,[0]*4,[0]*4)

def character_formula(s,t,flip):
    if flip:
        composition=tuple(s[t[i]] for i in range(4))
        return sum(composition[i]==i for i in range(4))-1
    u=sum(s[i]==i for i in range(4))-1
    v=sum(t[i]==i for i in range(4))-1
    return u*v+perm_sign(s)*u+perm_sign(t)*v

def face_lefschetz(s,t,flip):
    p=edge_perm(s,t,flip);result=-1
    for mask in FACES:
        im=[p[i] for i in range(16) if mask&(1<<i)]
        if sum(1<<j for j in im)!=mask:continue
        result+=(-1)**(len(im)-1)*(-1)**sum(im[i]>im[j] for i in range(len(im)) for j in range(i+1,len(im)))
    return -result # only reduced degree five implies reduced Lefschetz = -trace

def verify():
    counts,matched,incidences=matching_certificate()
    reps={}
    for p in PERMS:
        reps.setdefault(perm_type(p),p)
    n=0
    for s in PERMS:
        for t in PERMS:
            for f in (False,True):
                got=orbit_character(s,t,f)
                expected=character_formula(s,t,f)
                assert got==expected,(s,t,f,got,expected)
                n+=1
    independent=0
    for s_type,s in reps.items():
        for t_type,t in reps.items():
            got=face_lefschetz(s,t,False)
            assert got==character_formula(s,t,False),(s_type,t_type,got)
            independent+=1
    for s_type,s in reps.items():
        got=face_lefschetz(s,IDENTITY,True)
        assert got==character_formula(s,IDENTITY,True),(s_type,got)
        independent+=1
    inv=0
    for s in PERMS:
        for t in PERMS:
            for flip in (False,True):
                inv+=character_formula(s,t,flip)
    assert inv==0,inv
    assert character_formula(IDENTITY,IDENTITY,False)==15
    assert character_formula(IDENTITY,IDENTITY,True)==3
    print('K44_TWO_MATCHING_EQUIVARIANT_VERIFIED',
          'faces=',len(FACES),'morse_pairs=',matched,'hasse_incidence=',incidences,
          'symmetries=',n,'independent_fixed_face_checks=',independent,
          'invariants=',inv//1152)

if __name__=='__main__':verify()
