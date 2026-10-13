from itertools import combinations
from collections import Counter
import sympy as s

# Explicit deck matrix in the standard Picard basis e0,e1,...,e6.
M=s.Matrix([
[ 4, 2, 1, 1, 2, 2, 1],
[-1,-1, 0, 0, 0,-1, 0],
[-2,-1,-1, 0,-1,-1,-1],
[-2,-1,-1,-1,-1,-1, 0],
[-1,-1, 0, 0,-1, 0, 0],
[-1, 0, 0, 0,-1,-1, 0],
[-2,-1, 0,-1,-1,-1,-1],
])
J=s.diag(1,-1,-1,-1,-1,-1,-1)
assert M.T*J*M==J

def vec(a):
    return s.Matrix(a)

lines={}
for i in range(1,7):
    a=[0]*7; a[i]=1; lines[f'E{i}']=vec(a)
for i,j in combinations(range(1,7),2):
    a=[0]*7; a[0]=1; a[i]=-1; a[j]=-1; lines[f'F{i}{j}']=vec(a)
for i in range(1,7):
    a=[2]+[-1]*6; a[i]=0; lines[f'G{i}']=vec(a)
assert len(lines)==27
rev={tuple(map(int,c)):name for name,c in lines.items()}
perm={name:rev[tuple(map(int,M*c))] for name,c in lines.items()}

seen=set(); cycles=[]
for name in sorted(lines):
    if name in seen: continue
    cyc=[]; x=name
    while x not in seen:
        seen.add(x); cyc.append(x); x=perm[x]
    cycles.append(tuple(cyc))
assert Counter(map(len,cycles))==Counter({3:9})

def intersection(a,b):
    return int((lines[a].T*J*lines[b])[0])

meeting=[(a,b) for a,b in combinations(lines,2) if intersection(a,b)==1]
assert len(meeting)==135
tritangents=[]
for tri in combinations(lines,3):
    if all(intersection(a,b)==1 for a,b in combinations(tri,2)):
        tritangents.append(tri)
assert len(tritangents)==45

fiber={name:i for i,cyc in enumerate(cycles) for name in cyc}
projection=Counter(tuple(sorted({fiber[x] for x in tri})) for tri in tritangents)
singletons=[b for b in projection if len(b)==1]
blocks=[b for b in projection if len(b)==3]
assert len(singletons)==9 and all(projection[b]==1 for b in singletons)
assert len(blocks)==12 and all(projection[b]==3 for b in blocks)
pairs=Counter()
for block in blocks:
    for pair in combinations(block,2): pairs[pair]+=1
assert len(pairs)==36 and set(pairs.values())=={1}

tri_index={frozenset(t):i for i,t in enumerate(tritangents)}
tperm={i:tri_index[frozenset(perm[x] for x in tri)] for i,tri in enumerate(tritangents)}
seen=set(); orbits=[]
for i in range(45):
    if i in seen: continue
    orb=[]; x=i
    while x not in seen:
        seen.add(x); orb.append(x); x=tperm[x]
    orbits.append(orb)
assert Counter(map(len,orbits))==Counter({1:9,3:12})

print('VERIFY_OK lines=27 line_orbits=9x3 tritangents=45 deck_orbits=9x1+12x3 projected_blocks=STS(9)=AG(2,3) monodromy_orbits=9+36 stabilizers=72,18')
