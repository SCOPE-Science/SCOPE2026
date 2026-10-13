#!/usr/bin/env python3
"""Exact enumeration of proper distinguishing 4-colour partitions of the Fano Levi graph.
The method enumerates restricted-growth colour-class partitions and constructs the
336 graph automorphisms from GL(3,2) and an incidence-reversing polarity.
No third-party dependencies.
"""
import itertools, collections, csv, sys
from pathlib import Path

POINTS = tuple(range(1, 8))
LINES = tuple(sorted({tuple(sorted((a,b,a^b))) for a in POINTS for b in POINTS if a<b}))
assert len(LINES)==7
LID={line:i for i,line in enumerate(LINES)}
EDGE={(p-1,7+j) for j,L in enumerate(LINES) for p in L}
assert len(EDGE)==21
N=[set() for _ in range(14)]
for u,v in EDGE:N[u].add(v);N[v].add(u)

def images_of_basis():
    for a in POINTS:
        for b in POINTS:
            if b==a: continue
            for c in POINTS:
                if c in (a,b,a^b):continue
                yield a,b,c

def linear_perm(basis):
    def f(p):
        a,b,c=basis
        return ((a if p&1 else 0)^(b if p&2 else 0)^(c if p&4 else 0))
    result=[f(p)-1 for p in POINTS]
    for L in LINES:result.append(7+LID[tuple(sorted(f(p) for p in L))])
    return tuple(result)

GL=tuple(linear_perm(b) for b in images_of_basis())
assert len(GL)==168 and len(set(GL))==168
orth={p:tuple(q for q in POINTS if ((p&q).bit_count()%2)==0) for p in POINTS}
assert set(orth.values())==set(LINES)
dual=[0]*14
for p in POINTS:dual[p-1]=7+LID[orth[p]]
for j,L in enumerate(LINES):dual[7+j]=next(p-1 for p in POINTS if orth[p]==L)
assert all(dual[dual[i]]==i for i in range(14))
AUT=tuple(sorted(set(GL)|{tuple(dual[g[i]] for i in range(14)) for g in GL}))
IDENTITY=tuple(range(14))
assert len(AUT)==336 and AUT[0]==IDENTITY
assert all({tuple(sorted((g[u],g[v]))) for u,v in EDGE} == EDGE for g in AUT)


def canon(colors):
    relabel={};out=[]
    for x in colors:
        if x not in relabel:relabel[x]=len(relabel)
        out.append(relabel[x])
    return tuple(out)

# Independent from the labelled-colour search: every set partition is generated
# exactly once in restricted-growth representation, and each class is independent.
proper=collections.Counter();dist=collections.Counter(); all_four=set(); all_three=set()
color=[0]*14

def dfs(v,used):
    if v==14:
        proper[used]+=1
        if used==3:all_three.add(tuple(color))
        if used==4 and not any(all(color[i]==color[g[i]] for i in range(14)) for g in AUT[1:]):
            dist[4]+=1;all_four.add(tuple(color))
        return
    for d in range(min(4,used+1)):
        if any(color[w]==d for w in N[v] if w<v): continue
        color[v]=d
        dfs(v+1,max(used,d+1))

dfs(0,0)
assert dict(proper)=={2:1,3:350,4:29610},proper
assert dist[4]==13692,dist
# Each 4-class partition has 4! labelled colourings.
assert sum(proper[r]*__import__('math').perm(4,r) for r in proper)==719052
assert dist[4]*24==328608

unseen=set(all_four); reps=[]; orbitsizes=collections.Counter(); by_profile=collections.Counter()
while unseen:
    seed=min(unseen)
    orb={canon(tuple(seed[g[i]] for i in range(14))) for g in AUT}
    assert len(orb & unseen)==len(orb)
    unseen-=orb
    rep=min(orb)
    sizes=tuple(sorted((rep.count(c) for c in range(4)),reverse=True))
    stab=[]
    for g in AUT:
        cc=tuple(rep[g[i]] for i in range(14))
        if canon(cc)==rep:
            remap=tuple(cc[rep.index(c)] for c in range(4))
            assert sorted(remap)==list(range(4))
            stab.append(remap)
    staborder=336//len(orb)
    assert len(stab)==staborder
    # Distinguishes a cyclic four-group from the Klein four-group.
    element_orders=[]
    for s in stab:
        vv=tuple(range(4));ord=0
        while True:
            vv=tuple(s[i] for i in vv);ord+=1
            if vv==tuple(range(4)):break
        element_orders.append(ord)
    etypes=','.join(f'{order}:{element_orders.count(order)}' for order in sorted(set(element_orders)))
    reps.append((rep,len(orb),staborder,sizes,etypes))
    orbitsizes[len(orb)]+=1
    by_profile[sizes]+=len(orb)

assert len(reps)==51
assert dict(orbitsizes)=={56:1,84:1,112:1,168:16,336:32},orbitsizes
assert sum(len_orb for _,len_orb,_,_,_ in reps)==13692
assert sum(by_profile.values())==13692

print('VERIFY_OK graph=Heawood vertices=14 edges=21 automorphisms=336 GL3=168 polarity=1')
print('VERIFY_OK unlabeled_proper_partitions',dict(proper),'proper_4_colorings=719052')
print('VERIFY_OK unlabeled_proper_distinguishing_4_partitions=13692 labelled=328608')
print('VERIFY_OK symmetry_orbits=51 sizes',dict(sorted(orbitsizes.items())))
print('VERIFY_OK orbit_class_profiles',dict(sorted(by_profile.items())))
for k in sorted(orbitsizes):
 rr=[r for r in reps if r[1]==k]
 print(' orbit_size',k,'stabilizer_types',collections.Counter(r[4] for r in rr))

if len(sys.argv)>1 and sys.argv[1]=='--csv':
    out=Path(sys.argv[2] if len(sys.argv)>2 else 'orbit_representatives.csv')
    with out.open('w',newline='',encoding='utf-8') as f:
        w=csv.writer(f);w.writerow(['orbit_id','canonical_four_color_word','unlabeled_orbit_size','labelled_four_colorings','class_sizes_descending','partition_stabilizer_order','partition_stabilizer_element_orders'])
        for j,(rep,s,st,sz,etypes) in enumerate(sorted(reps),1):
            w.writerow([f'O{j:02d}',''.join(map(str,rep)),s,24*s,'-'.join(map(str,sz)),st,etypes])
    print('CSV_WRITTEN',out)

# Compact lower-bound certificate: all 350 canonical proper three-class partitions.
three_remaining=set(all_three); three_reps=[]
while three_remaining:
    x=min(three_remaining)
    orbit={canon(tuple(x[g[i]] for i in range(14))) for g in AUT}
    assert orbit<=three_remaining
    three_remaining-=orbit
    rep=min(orbit)
    witness=next((g for g in AUT[1:] if all(rep[i]==rep[g[i]] for i in range(14))),None)
    assert witness is not None
    three_reps.append((rep,len(orbit),tuple(witness)))
print('VERIFY_OK three_color_partition_orbits',len(three_reps),dict(collections.Counter(n for _,n,_ in three_reps)))
for row in three_reps:print('LOWER', ''.join(map(str,row[0])),row[1], ''.join(chr(65+x) for x in row[2]))
if len(sys.argv)>1 and sys.argv[1]=='--csv':
 out=Path(sys.argv[3] if len(sys.argv)>3 else 'three_color_obstructions.csv')
 with out.open('w',newline='',encoding='utf-8') as f:
  w=csv.writer(f);w.writerow(['canonical_three_color_word','partition_orbit_size','nonidentity_color_preserving_automorphism_image_0_to_13'])
  for rep,n,witness in sorted(three_reps):w.writerow([''.join(map(str,rep)),n,'-'.join(map(str,witness))])
 print('CSV_WRITTEN',out)
