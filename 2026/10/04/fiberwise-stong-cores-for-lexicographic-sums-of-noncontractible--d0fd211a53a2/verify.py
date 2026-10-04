#!/usr/bin/env python3
from itertools import product

def closure(nodes, covers):
    nodes=list(nodes); reach={(x,x) for x in nodes}|set(covers)
    changed=True
    while changed:
        changed=False
        add=set()
        for a,b in reach:
            for c,d in reach:
                if b==c and (a,d) not in reach:
                    add.add((a,d))
        if add:
            reach |= add; changed=True
    return frozenset(nodes), frozenset(reach)

def induced(P, keep):
    nodes, leq=P; keep=frozenset(keep)
    return keep, frozenset((a,b) for a,b in leq if a in keep and b in keep)

def is_leq(P,a,b): return (a,b) in P[1]

def beat_type(P,x):
    nodes,_=P
    up=[y for y in nodes if y!=x and is_leq(P,x,y)]
    if up:
        mins=[m for m in up if all(is_leq(P,m,y) for y in up)]
        if mins: return ('up',mins[0])
    dn=[y for y in nodes if y!=x and is_leq(P,y,x)]
    if dn:
        maxs=[m for m in dn if all(is_leq(P,y,m) for y in dn)]
        if maxs: return ('down',maxs[0])
    return None

def core_with_sequence(P):
    cur=P; seq=[]
    while True:
        beats=[x for x in cur[0] if beat_type(cur,x)]
        if not beats: return cur,seq
        x=min(beats,key=repr)
        seq.append((x,beat_type(cur,x)))
        cur=induced(cur,set(cur[0])-{x})

def lexsum(S, fibers):
    Sn,Sleq=S
    nodes=[]
    for s in Sn:
        for x in fibers[s][0]: nodes.append((s,x))
    leq=set()
    for a in nodes:
        for b in nodes:
            s,x=a; t,y=b
            if s==t:
                if (x,y) in fibers[s][1]: leq.add((a,b))
            elif (s,t) in Sleq:
                leq.add((a,b))
    return frozenset(nodes),frozenset(leq)

def poset(name):
    if name=='chain2': return closure([0,1],[(0,1)])
    if name=='antichain2': return closure([0,1],[])
    if name=='V': return closure([0,1,2],[(0,2),(1,2)])
    if name=='diamond': return closure([0,1,2,3],[(0,1),(0,2),(1,3),(2,3)])
    raise KeyError(name)

def fiber(name):
    if name=='D2': return closure([0,1],[])
    if name=='D3': return closure([0,1,2],[])
    if name=='C4': return closure([0,1,2,3],[(0,2),(0,3),(1,2),(1,3)])
    if name=='C4beat':
        # Add a new point 4 below the minimal point 0; 4 is an up beat point.
        return closure([0,1,2,3,4],[(0,2),(0,3),(1,2),(1,3),(4,0)])
    raise KeyError(name)

fiber_names=['D2','D3','C4','C4beat']
index_names=['chain2','antichain2','V','diamond']
case_count=0; deletion_checks=0
for iname in index_names:
    S=poset(iname); slist=sorted(S[0])
    for choices in product(fiber_names, repeat=len(slist)):
        fibers={s:fiber(nm) for s,nm in zip(slist,choices)}
        local_cores={}; local_seqs={}
        for s in slist:
            c,seq=core_with_sequence(fibers[s])
            assert len(c[0])>=2, (iname,choices,s)
            local_cores[s]=c; local_seqs[s]=seq
        G=lexsum(S,fibers)
        cur=G
        # Replay each local core reduction in the whole lexicographic sum.
        for s in slist:
            for x,_ in local_seqs[s]:
                gx=(s,x)
                assert gx in cur[0]
                assert beat_type(cur,gx) is not None, (iname,choices,s,x)
                deletion_checks += 1
                cur=induced(cur,set(cur[0])-{gx})
        expected=lexsum(S,local_cores)
        assert cur==expected
        assert all(beat_type(cur,x) is None for x in cur[0]), (iname,choices,'nonminimal')
        assert len(cur[0])==sum(len(local_cores[s][0]) for s in slist)
        case_count += 1

# Boundary example: the noncontractibility hypothesis cannot simply be dropped.
# A singleton lexicographically below a two-point antichain is contractible.
S=poset('chain2')
fibers={0:closure([0],[]),1:fiber('D2')}
G=lexsum(S,fibers)
C,seq=core_with_sequence(G)
assert len(G[0])==3 and len(C[0])==1
assert 1+2 != len(C[0])

print('VERIFY_OK')
print('lexicographic_sum_cases',case_count)
print('fiberwise_beat_deletions_replayed',deletion_checks)
print('boundary_example_core_size',len(C[0]))
