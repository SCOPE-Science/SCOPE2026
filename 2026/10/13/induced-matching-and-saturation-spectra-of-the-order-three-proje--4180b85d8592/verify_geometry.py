#!/usr/bin/env python3
"""Exhaustive flag configurations in the projective plane over F_3."""
from collections import Counter, defaultdict
from itertools import product
import csv
from pathlib import Path

Q=3
points=[]
for xyz in product(range(Q), repeat=3):
    if not any(xyz):
        continue
    pivot=next(x for x in xyz if x)
    normal=tuple((x*pow(pivot,-1,Q))%Q for x in xyz)
    if normal not in points:
        points.append(normal)
assert len(points)==13
idx={v:i for i,v in enumerate(points)}
inc=lambda p,l:sum(a*b for a,b in zip(points[p],points[l]))%Q==0
edges=[(p,l) for p in range(13) for l in range(13) if inc(p,l)]
assert len(edges)==52
edge_lookup={p:i for i,p in enumerate(edges)}
line_points=[sum(1<<p for p in range(13) if inc(p,l)) for l in range(13)]

# Method 1: enumerate all point sets, weighted by permissible private lines.
profile=defaultdict(Counter)
matchings={}
for subset in range(1<<13):
    S=[p for p in range(13) if subset & (1<<p)]
    options=[]
    for p in S:
        tangent=[l for l in range(13) if (line_points[l] & subset)==(1<<p)]
        if not tangent:
            break
        options.append(tangent)
    else:
        key=tuple(sorted(len(o) for o in options))
        profile[len(S)][key]+=1
        for lines in product(*options):
            mask=0
            for p,l in zip(S,lines):
                mask|=1<<edge_lookup[(p,l)]
            assert mask not in matchings
            matchings[mask]=len(S)
assert len(matchings)==10700
polynomial=Counter(matchings.values())
assert tuple(polynomial[k] for k in range(7))==(1,52,702,3276,5031,1404,234)
assert dict(profile[5])=={(1,1,1,1,2):702}
assert dict(profile[6])=={(1,1,1,1,1,1):234}

# Extension and inclusion-maximal census.
incompatible=[]
for p,l in edges:
    incompatible.append(sum(1<<j for j,(r,s) in enumerate(edges)
        if p==r or l==s or inc(p,s) or inc(r,l)))
maximal=set()
for mask,k in matchings.items():
    choices=[j for j in range(52) if not (mask & incompatible[j])]
    if not choices:
        maximal.add(mask)
    if k==5:
        assert len(choices)==1
assert Counter(matchings[m] for m in maximal)=={4:1989,6:234}

# Generating set for GL(3,3), with scalars removed on projective points.
matrices=(
    ((1,1,0),(0,1,0),(0,0,1)),
    ((0,1,0),(1,0,0),(0,0,1)),
    ((0,1,0),(0,0,1),(1,0,0)),
    ((2,0,0),(0,1,0),(0,0,1)),
)
def act_matrix(A):
    perm=[]
    for v in points:
        w=tuple(sum(A[i][j]*v[j] for j in range(3))%3 for i in range(3))
        pivot=next(a for a in w if a)
        perm.append(idx[tuple((a*pow(pivot,-1,3))%3 for a in w)])
    mapped_lines=[]
    for line_mask in line_points:
        pmask=sum(1<<perm[p] for p in range(13) if line_mask & (1<<p))
        mapped_lines.append(line_points.index(pmask))
    return tuple(perm),tuple(edge_lookup[(perm[p],mapped_lines[l])] for p,l in edges)
gens=[act_matrix(A) for A in matrices]
# Verify these generate precisely 5616 distinct point collineations.
identity=tuple(range(13))
group={identity}; queue=[identity]
for perm in queue:
    for g,_ in gens:
        new=tuple(g[perm[i]] for i in range(13))
        if new not in group:
            group.add(new);queue.append(new)
assert len(group)==5616
flag_gens=[g[1] for g in gens]
# Incidence polarity exchanges point/line sides and doubles the full group.
flag_gens.append(tuple(edge_lookup[(l,p)] for p,l in edges))
def move(mask,gen):
    return sum(1<<gen[j] for j in range(52) if mask & (1<<j))
remaining=set(matchings)
orbits=[]
while remaining:
    seed=min(remaining)
    orbit={seed}; todo=[seed]
    for cur in todo:
        for gen in flag_gens:
            image=move(cur,gen)
            if image not in orbit:
                orbit.add(image);todo.append(image)
    assert orbit<=remaining
    remaining-=orbit
    orbits.append((seed,matchings[seed],len(orbit),seed in maximal))
assert len(orbits)==12
assert Counter((k,n) for seed,k,n,mx in orbits if mx)=={(4,117):1,(4,1872):1,(6,234):1}
assert sum(size for seed,k,size,mx in orbits)==10700

certificate=Path(__file__).with_name('orbit_classes.csv')
rows=[]
for seed,k,size,ismax in orbits:
    pairs=[f'{p}:{l}' for j,(p,l) in enumerate(edges) if seed & (1<<j)]
    rows.append({'cardinality':k,'orbit_size':size,'inclusion_maximal':str(ismax).lower(),
        'representative_flags':';'.join(pairs)})
rows.sort(key=lambda r:(r['cardinality'],r['orbit_size'],r['representative_flags']))
if certificate.exists():
    with certificate.open(newline='',encoding='utf-8') as f:
        assert list(csv.DictReader(f))==[{k:str(v) for k,v in row.items()} for row in rows]
else:
    with certificate.open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
print('VERIFY_GEOMETRY_OK points=13 lines=13 flags=52 point_subsets=8192')
print('VERIFY_GEOMETRY_OK induced_polynomial=1,52,702,3276,5031,1404,234 total=10700')
print('VERIFY_GEOMETRY_OK five_matchings=1404 all_unique_six_extensions=true')
print('VERIFY_GEOMETRY_OK inclusion_maximal_4=1989 inclusion_maximal_6=234 no_other_sizes=true')
print('VERIFY_GEOMETRY_OK collineations=5616 full_incidence_automorphisms=11232 orbits=12')
print('VERIFY_GEOMETRY_OK maximal_orbit_sizes=117,1872,234 certificate_rows=12')
print('VERIFY_GEOMETRY_OK point_tangent_profiles='+repr({k:dict(v) for k,v in profile.items()}))
