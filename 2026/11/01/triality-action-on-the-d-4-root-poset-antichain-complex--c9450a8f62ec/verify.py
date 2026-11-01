#!/usr/bin/env python3
"""Exact finite-chain and orbit-simplex verification for type-D4 root-poset topology."""
from itertools import combinations, permutations
from fractions import Fraction
from collections import Counter, defaultdict

def positive_roots():
    es = [tuple(int(i == j) for i in range(4)) for j in range(4)]
    result = set()
    for i, j in combinations(range(4), 2):
        for sign in (-1, 1):
            v = [es[i][k] + sign*es[j][k] for k in range(4)]
            a, b = v[0], v[0]+v[1]
            c, d = Fraction(b+v[2]-v[3], 2), Fraction(b+v[2]+v[3], 2)
            assert c.denominator == d.denominator == 1
            root = a, b, int(c), int(d)
            assert all(z >= 0 for z in root)
            result.add(root)
    assert len(result) == 12
    return tuple(sorted(result, key=lambda x: (sum(x), x)))

ROOTS=positive_roots()

def incomparable(a,b):
    return not (all(x<=y for x,y in zip(a,b)) or all(y<=x for x,y in zip(a,b)))

def all_faces(orbits):
    good = lambda sub: all(incomparable(a,b) for i,j in combinations(sub,2)
                             for a in orbits[i] for b in orbits[j])
    good_orbits = [i for i,O in enumerate(orbits)
                   if all(incomparable(a,b) for a,b in combinations(O,2))]
    return {tuple(sub) for n in range(1,len(good_orbits)+1)
            for sub in combinations(good_orbits,n) if good(sub)}

def rank_exact(matrix):
    if not matrix:return 0
    M = [list(map(Fraction,row)) for row in matrix]
    n, k = len(M), len(M[0]); rank=0
    for j in range(k):
        pivot = next((i for i in range(rank,n) if M[i][j]), None)
        if pivot is None:continue
        M[rank],M[pivot] = M[pivot],M[rank]
        v=M[rank][j]; M[rank] = [a/v for a in M[rank]]
        for i in range(rank+1,n):
            if M[i][j]:
                v=M[i][j]; M[i] = [a-v*b for a,b in zip(M[i], M[rank])]
        rank += 1
        if rank == n:break
    return rank

def betti(faces):
    counts=Counter(map(len,faces)); ranks={}
    for d in range(1,max(counts)+1):
        top=sorted(f for f in faces if len(f)==d)
        bottom=sorted(f for f in faces if len(f)==d-1) if d>1 else [()]
        index={f:i for i,f in enumerate(bottom)}
        mat=[[0]*len(top) for _ in bottom]
        for j,f in enumerate(top):
            for i in range(len(f)):
                mat[index[f[:i]+f[i+1:]]][j] = (-1)**i
        ranks[d]=rank_exact(mat)
    return counts,ranks,{d-1:counts[d]-ranks[d]-ranks.get(d+1,0) for d in counts}

outer=(0,2,3)
ident=outer
trans=(2,0,3)
rot=(2,3,0)

def action(x,p):
    y=list(x)
    for j,k in zip(outer,p):y[j]=x[k]
    return tuple(y)

def orbits(group):
    seen=set(); orbit_list=[]
    for r in ROOTS:
        if r in seen:continue
        orbit=tuple(sorted({action(r,g) for g in group}))
        seen.update(orbit);orbit_list.append(orbit)
    assert seen==set(ROOTS)
    return orbit_list

full=all_faces([(r,) for r in ROOTS]); count,ranks,b=betti(full)
assert [count[i] for i in range(1,5)] == [12,24,12,1],count
assert [ranks[i] for i in range(1,5)] == [1,9,10,1],ranks
assert [b.get(i,0) for i in range(4)]==[2,5,1,0],b

C2=orbits([ident,trans]);C3=orbits([ident,rot,(3,0,2)]);S3=orbits(list(permutations(outer)))
assert C3==S3
fixed={}
for key,O in [('C2',C2),('C3',C3),('S3',S3)]:
    fs=all_faces(O)
    fcount,branks,bet=betti(fs)
    fixed[key]=(O,fs,fcount,branks,bet)
assert (len(C2), len(fixed['C2'][1])) == (9,19)
assert dict(fixed['C2'][2])=={1:9,2:9,3:1}
assert fixed['C2'][4]=={0:2,1:2,2:0}
assert len(C3)==6 and fixed['C3'][2] == {1:6,2:1}
assert fixed['C3'][4]=={0:4,1:0}

# Only two isolated fixed vertices for C2; its main component is a triangle and
# six extra graph edges. The triangle has a free edge, so collapses to a graph.
fs=fixed['C2'][1]
triangles=[f for f in fs if len(f)==3]; assert len(triangles)==1
edges={f for f in fs if len(f)==2}
free_edges=[e for e in combinations(triangles[0],2)
            if sum(set(e).issubset(f) for f in triangles)==1]
assert free_edges
collapsed_edges=edges-{free_edges[0]}
vertices={i for f in fs for i in f}
adj={i:set() for i in vertices}
for i,j in collapsed_edges:adj[i].add(j);adj[j].add(i)
seen=set(); comps=[]
for v in adj:
    if v in seen:continue
    stack=[v]; seen.add(v); comp=set()
    while stack:
        u=stack.pop();comp.add(u)
        for w in adj[u]-seen:seen.add(w);stack.append(w)
    comps.append(comp)
assert sorted(map(len,comps))==[1,1,7]
assert len(collapsed_edges)==8
assert len(collapsed_edges)-7+1==2

# In the complete complex, the highest two roots are globally isolated,
# hence the reduced H0 permutation character is twice the trivial character.
iso=[i for i in range(12) if not any(i in f for f in full if len(f)==2)]
assert len(iso)==2
assert all(action(ROOTS[i],p)==ROOTS[i] for i in iso for p in permutations(outer))
# The trace of each symmetry on reduced homology is the reduced Euler char of
# its geometric fixed complex (Hopf-Lefschetz).
# id trace = -2; transposition trace=0; three-cycle trace=4.
# Write top 1d character for transposition as s=±1 and three-cycle as +1.
# Then H1 traces are (5,2+s,-1). Nonnegative S3 multiplicities exclude s=+1.
for s in (-1,1):
    h1=(5,2+s,-1)
    standard=(h1[0]-h1[2])/3  # solving chars at e and three-cycle
    aplusb=h1[2]+standard
    a=(aplusb+h1[1])/2; bb=(aplusb-h1[1])/2
    if s==-1:assert (a,bb,standard)==(1,0,2)
    else:assert bb<0
print('VERIFY_OK roots=12 full_faces=(12,24,12,1) exact_boundary_ranks=(1,9,10,1)')
print('fixed_C2=(S1_vee_S1)+2_points; fixed_C3=fixed_S3=interval+4_points')
print('H1_Q=trivial+2_standard, H2_Q=sign, H0_tilde_Q=2_trivial')
