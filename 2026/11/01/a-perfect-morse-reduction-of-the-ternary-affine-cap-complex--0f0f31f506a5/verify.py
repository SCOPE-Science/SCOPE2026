"""Exact finite certificate for the affine ternary cap complex.

Run with Python 3: python verify.py . No external packages are required.
All simplices use nine-bit masks; vertex i represents (i//3,i%3) over F_3.
"""
from collections import Counter, deque
from fractions import Fraction
from itertools import combinations

V = [(a,b) for a in range(3) for b in range(3)]
lines = []
for triple in combinations(range(9),3):
    a,b,c = (V[i] for i in triple)
    if ((b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])) % 3 == 0:
        lines.append(sum(1<<i for i in triple))
assert len(lines)==12
faces = [m for m in range(1,1<<9) if not any((m&ell)==ell for ell in lines)]
face_set = set(faces)
assert len(faces)==171
assert Counter(m.bit_count()-1 for m in faces)=={0:9,1:36,2:72,3:54}
assert all(m.bit_count()<=4 for m in faces)

# Lexicographic vertex toggles on the still-unmatched face poset.
unmatched = set(faces)
matching = []
for v in range(9):
    for lo in faces:
        hi = lo | (1<<v)
        if hi != lo and lo in unmatched and hi in unmatched:
            unmatched.remove(lo)
            unmatched.remove(hi)
            matching.append((lo,hi))
assert len(matching)==79
assert Counter(m.bit_count()-1 for m in unmatched)=={0:1,2:1,3:11}
assert len(unmatched)==13
assert sorted(unmatched)==[1,54,70,216,232,240,344,360,368,390,408,424,432]

# Hasse arrows downwards except matched arrows upwards. Exhaustive DAG test.
matched=set(matching)
out={f:[] for f in faces}
indegree={f:0 for f in faces}
edge_count=0
for big in faces:
    for v in range(9):
        if big & (1<<v):
            small=big^(1<<v)
            if not small: continue
            if small not in face_set: raise AssertionError('not downward closed')
            source,target=(small,big) if (small,big) in matched else (big,small)
            out[source].append(target)
            indegree[target]+=1
            edge_count+=1
assert edge_count==504
queue=deque(f for f,d in indegree.items() if d==0)
seen=0
while queue:
    f=queue.popleft(); seen+=1
    for t in out[f]:
        indegree[t]-=1
        if indegree[t]==0: queue.append(t)
assert seen==len(faces), 'matching contains a closed alternating gradient path'

# Exact rational elimination of the boundary C_3 -> C_2.
triangles=[f for f in faces if f.bit_count()==3]
tetrahedra=[f for f in faces if f.bit_count()==4]
tri_index={f:i for i,f in enumerate(triangles)}
columns=[]
for t in tetrahedra:
    col={}
    for i,v in enumerate(v for v in range(9) if t&(1<<v)):
        col[tri_index[t^(1<<v)]]=Fraction((-1)**i)
    columns.append(col)

# Sparse Gaussian elimination over Q, in column form.
pivots={}
for col in columns:
    while col:
        r=min(col)
        if r not in pivots:
            factor=col[r]
            pivots[r]={s:x/factor for s,x in col.items()}
            break
        factor=col[r]
        for s,x in pivots[r].items():
            value=col.get(s,Fraction(0))-factor*x
            if value: col[s]=value
            elif s in col: del col[s]
assert len(pivots)==43
print('12 affine lines; f-vector (9,36,72,54)')
print('79 matched pairs; critical cells (1,0,1,11) in degrees 0,1,2,3')
print('Directed Hasse graph: 171 vertices, 504 arrows, acyclic')
print('Exact rational rank of 72x54 boundary C3->C2: 43')
print('Morse degree-three boundary is zero; homotopy type S2 wedge 11 S3')
print('VERIFY_OK')
