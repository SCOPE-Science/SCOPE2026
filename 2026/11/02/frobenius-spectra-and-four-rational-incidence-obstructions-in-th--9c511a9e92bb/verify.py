"""Exact 16_6 Kummer incidence and 96-flag Frobenius verifier (Python standard library)."""
from itertools import permutations, combinations
from collections import Counter
from math import lcm

N=6; MASK=(1<<N)-1
canon=lambda a:min(a,a^MASK)
EVEN=tuple(sorted({canon(x) for x in range(1<<N) if x.bit_count()%2==0}))
ODD=tuple(sorted({canon(x) for x in range(1<<N) if x.bit_count()%2==1}))
SINGLE={canon(1<<i) for i in range(N)}
FLAGS=tuple((a,b) for a in EVEN for b in ODD if canon(a^b) in SINGLE)
assert (len(EVEN),len(ODD),len(FLAGS))==(16,16,96)
assert set(sum(1 for a,b in FLAGS if a==u) for u in EVEN)=={6}
assert set(sum(1 for a,b in FLAGS if b==v) for v in ODD)=={6}
assert set(sum(1 for a,b in FLAGS if a in (x,y)) for x,y in [])==set()
# Independent historic labels: p_0, p_ij and T_i, T_{ABC}; ensure the complete incidence rule.
for a,b in FLAGS:
    aa = a if a.bit_count()<=2 else a^MASK
    bb = b if b.bit_count()<=3 else b^MASK
    av=aa.bit_count(); bv=bb.bit_count()
    if av==0: assert bv==1
    elif bv==1: assert av==2 and bool(aa & bb)
    else: assert av==2 and bv==3 and ((aa & bb).bit_count() in (0,2))

def image(p,a):
    return canon(sum(1<<p[i] for i in range(N) if a>>i & 1))

def partition(p):
    done=set(); ans=[]
    for i in range(N):
        if i in done:continue
        j=i; m=0
        while j not in done:
            done.add(j);m+=1;j=p[j]
        ans.append(m)
    return tuple(sorted(ans,reverse=True))

def spectrum(p,stuff):
    todo=set(stuff); ans=Counter()
    while todo:
        x=next(iter(todo)); y=x; d=0
        while y in todo:
            todo.remove(y);d+=1
            y=tuple(image(p,z) for z in y) if isinstance(y,tuple) else image(p,y)
        assert y==x
        ans[d]+=1
    assert sum(d*c for d,c in ans.items())==len(stuff)
    return tuple(sorted(ans.items()))

all_types={}; counts=Counter()
for p in permutations(range(N)):
    lam=partition(p);counts[lam]+=1
    sn,st,sf=[spectrum(p,x) for x in (EVEN,ODD,FLAGS)]
    assert sn==st  # matching number of closed points in each degree
    for d in range(1,7):
        pp=tuple(p[i] for i in range(N))
        for _ in range(d-1): pp=tuple(p[pp[i]] for i in range(N))
        actual=sum(1 for a,b in FLAGS if image(pp,a)==a and image(pp,b)==b)
        formula=sum(m*c for m,c in sf if d%m==0)
        assert actual==formula
    assert lcm(*[d for d,c in sf])==lcm(*lam)
    tup=(sn,st,sf)
    if lam in all_types: assert all_types[lam]==tup
    else:all_types[lam]=tup
assert len(all_types)==11 and sum(counts.values())==720
expected_obstructions={(6,),(4,2),(3,3),(2,2,2)}
actual_obstructions={lam for lam,(sn,st,sf) in all_types.items() if dict(sn).get(1,0)>0 and dict(st).get(1,0)>0 and dict(sf).get(1,0)==0}
assert actual_obstructions==expected_obstructions
print('OBJECTS nodes=16 tropes=16 incident_flags=96 each_node_degree=6 each_trope_degree=6')
print('GROUP permutations_checked=720 conjugacy_types=11')
for lam in sorted(all_types,reverse=True):
    sn,st,sf=all_types[lam]
    print('type={} permutations={} nodes_and_tropes={} flags={} rational_nodes={} rational_tropes={} rational_flags={}'.format(lam,counts[lam],sn,sf,dict(sn).get(1,0),dict(st).get(1,0),dict(sf).get(1,0)))
print('RATIONAL_INCIDENCE_OBSTRUCTIONS (6) (4,2) (3,3) (2,2,2)')
print('VERIFY_OK')
