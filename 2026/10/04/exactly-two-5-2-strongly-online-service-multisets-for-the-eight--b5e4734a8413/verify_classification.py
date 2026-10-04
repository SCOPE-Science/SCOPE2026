#!/usr/bin/env python3
from itertools import combinations, product

G = [
    [1,0,1,0,1,0,1,1],
    [0,1,1,0,0,1,1,1],
    [0,0,0,1,1,1,1,1],
]
COLS = [tuple(G[r][c] for r in range(3)) for c in range(8)]

def xor_vec(a,b): return tuple(x^y for x,y in zip(a,b))
def spans_e(indices, req):
    target = tuple(1 if r==req else 0 for r in range(3))
    vals={(0,0,0)}
    for idx in indices:
        v=COLS[idx]
        vals |= {xor_vec(x,v) for x in tuple(vals)}
    return target in vals

def minimal_recovery_sets(req):
    out=[]
    for size in range(1,9):
        for C in combinations(range(8),size):
            if not spans_e(C,req): continue
            if any(spans_e(D,req) for t in range(size) for D in combinations(C,t)):
                continue
            out.append(frozenset(i+1 for i in C))
    return out

R=[minimal_recovery_sets(i) for i in range(3)]
assert [len(x) for x in R] == [11,11,11]
expected1={frozenset(x) for x in [(1,),(2,3),(4,5),(6,7),(6,8),(2,4,7),(2,4,8),(2,5,6),(3,4,6),(3,5,7),(3,5,8)]}
assert set(R[0]) == expected1

# In an L=2 service multiset, any selected recovery set has multiplicity at most 2,
# because it intersects every copy of itself. Enumerate all 3^11 multiplicity vectors
# for each request, retaining those with at least m=5 services and satisfying all
# same-request exclusion bounds.
def exclusions(service, recs, mult):
    return sum(mult[j] for j,T in enumerate(recs) if service & T)

valid=[]
for req in range(3):
    vr=[]
    for mult in product(range(3), repeat=len(R[req])):
        if sum(mult) < 5: continue
        if all(not mult[i] or exclusions(R[req][i],R[req],mult) <= 2
               for i in range(len(R[req]))):
            vr.append(mult)
    valid.append(vr)
assert [len(v) for v in valid] == [141,141,141]
assert [{s:sum(sum(x)==s for x in v) for s in range(5,9)} for v in valid] == [
    {5:82,6:45,7:11,8:3},
    {5:82,6:45,7:11,8:3},
    {5:82,6:45,7:11,8:3},
]

def cross_ok(req_a, ma, req_b, mb):
    # Every selected service for req_a excludes at most two services for req_b,
    # and conversely.
    for i,a in enumerate(R[req_a]):
        if ma[i] and exclusions(a,R[req_b],mb)>2: return False
    for j,b in enumerate(R[req_b]):
        if mb[j] and exclusions(b,R[req_a],ma)>2: return False
    return True

pairs={}
for a,b in [(0,1),(0,2),(1,2)]:
    P=set()
    for ia,ma in enumerate(valid[a]):
        for ib,mb in enumerate(valid[b]):
            if cross_ok(a,ma,b,mb): P.add((ia,ib))
    pairs[a,b]=P
    assert len(P)==306

solutions=[]
for i,m0 in enumerate(valid[0]):
    for j,m1 in enumerate(valid[1]):
        if (i,j) not in pairs[0,1]: continue
        for k,m2 in enumerate(valid[2]):
            if (i,k) in pairs[0,2] and (j,k) in pairs[1,2]:
                solutions.append((m0,m1,m2))
assert len(solutions)==2
assert all(tuple(sum(x) for x in sol)==(5,5,5) for sol in solutions)

def canon(sol):
    return tuple(tuple(sorted((tuple(sorted(R[r][i])),m) for i,m in enumerate(sol[r]) if m)) for r in range(3))
C=sorted(canon(sol) for sol in solutions)
EXPECTED=sorted([
(
 (((1,),2),((4,5),1),((6,7),1),((6,8),1)),
 (((1,3),1),((2,),2),((5,7),1),((5,8),1)),
 (((2,6),1),((3,7),1),((3,8),1),((4,),2)),
),
(
 (((1,),2),((2,3),1),((6,7),1),((6,8),1)),
 (((2,),2),((4,6),1),((5,7),1),((5,8),1)),
 (((1,5),1),((3,7),1),((3,8),1),((4,),2)),
),
])
assert C==EXPECTED
print('minimal_recovery_counts', [len(x) for x in R])
print('same_request_candidates', [len(x) for x in valid])
print('pair_compatible_counts', [len(pairs[p]) for p in [(0,1),(0,2),(1,2)]])
print('global_structures', len(solutions))
for s in C: print(s)
print('VERIFY_OK')
