"""Exact, standalone enumeration for the C20 nearest/next-nearest Ising cluster.

Run with Python 3: python verify_dodecahedron.py
There is no sampling: all 2**20 spin assignments are enumerated.
"""
from collections import Counter
from itertools import combinations

N = 20
# The dodecahedral graph is the generalized Petersen graph GP(10,2).
# Vertices 0,...,9 are outer, 10,...,19 inner; all indices modulo 10.
edges = set()
def edge(a,b):
    edges.add(tuple(sorted((a,b))))
for i in range(10):
    edge(i,(i+1)%10)
    edge(i,10+i)
    edge(10+i,10+(i+2)%10)
assert len(edges) == 30
neighbors = [set() for _ in range(N)]
for u,v in edges:
    neighbors[u].add(v); neighbors[v].add(u)
assert all(len(v)==3 for v in neighbors)

# All graph-distance-two pairs and all induced cycles of length five.
pairs2 = sorted({tuple(sorted((u,w))) for v in range(N)
                 for u,w in combinations(neighbors[v],2)})
assert len(pairs2)==60
faces=[]
for vs in combinations(range(N),5):
    if all(sum((w in neighbors[v]) for w in vs)==2 for v in vs):
        faces.append(vs)
assert len(faces)==12
Fmask=[sum(1<<j for j in face) for face in faces]
edge_in_faces=Counter(e for face in faces for e in combinations(face,2) if e in edges)
next_in_faces=Counter(e for face in faces for e in combinations(face,2) if e in pairs2)
assert all(edge_in_faces[e]==2 for e in edges)
assert all(next_in_faces[e]==1 for e in pairs2)

# Method A: face constraints count the critical manifold directly.
critical=Counter()
left=Counter()
right=Counter()
for mask in range(1<<N):
    if any((mask & f).bit_count() not in (2,3) for f in Fmask):
        continue
    m=2*mask.bit_count()-N
    critical[m]+=1
    # At the NN lower bound -18, every pentagon has exactly one aligned edge.
    s1=30-2*sum(((mask>>u)^(mask>>v))&1 for u,v in edges)
    if s1==-18: left[m]+=1
    # At the NNN lower bound -20, no vertex has three equal-spin neighbors.
    if all(0<sum((mask>>u)&1 for u in neighbors[v])<3 for v in range(N)):
        right[m]+=1
assert dict(critical)=={-4:25,-2:1800,0:5600,2:1800,4:25},critical
assert dict(left)=={-4:5,0:240,4:5},left
assert dict(right)=={0:720},right
assert sum(critical.values())==9250
assert sum(left.values())==250
assert sum(right.values())==720

# Method B: independently evaluate all 2**20 energies (integer arithmetic).
# Ground states for ratios 1/4, 1/2 and 1; scale energy by 4, 2 and 1.
count=Counter(); minenergy={1:10**9,2:10**9,4:10**9}; mag={1:Counter(),2:Counter(),4:Counter()}
for mask in range(1<<N):
    m=2*mask.bit_count()-N
    cut1=sum(((mask>>u)^(mask>>v))&1 for u,v in edges)
    cut2=sum(((mask>>u)^(mask>>v))&1 for u,v in pairs2)
    s1=30-2*cut1; s2=60-2*cut2
    for q in (1,2,4):
        # J1=1 and J2/J1=q/4: 4E=4s1+q s2.
        energy=4*s1+q*s2
        if energy<minenergy[q]:
            minenergy[q]=energy;mag[q]=Counter({m:1})
        elif energy==minenergy[q]:
            mag[q][m]+=1
assert minenergy=={1:-60,2:-48,4:-88},minenergy
assert mag[1]==left,mag[1]
assert mag[2]==critical,mag[2]
assert mag[4]==right,mag[4]
print('PASS: all 1,048,576 spin assignments checked twice using distinct criteria')
print('Faces:',len(faces),'NN edges:',len(edges),'NNN edges:',len(pairs2))
for q in (1,2,4):
 print('J2/J1=',q/4,'energy x4=',minenergy[q], 'magnetizations:',dict(sorted(mag[q].items())))
print('Critical zero-field degeneracy:',sum(critical.values()))
print('Critical zero-field Curie coefficient:',304,'/',185)
