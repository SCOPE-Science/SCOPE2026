"""Exact discrete-Morse and cyclic Lefschetz verifier for the
Möbius–Kantor dominance complex. Standard-library Python 3 only.
"""
from collections import Counter
import heapq

n=8
m=2*n
neighbors=[set() for _ in range(m)]
def edge(a,b):neighbors[a].add(b);neighbors[b].add(a)
for i in range(n):
    edge(i,(i+1)%n)
    edge(i,8+i)
    edge(8+i,8+(i+3)%n)
assert all(len(a)==3 for a in neighbors)
closed=[sum(1<<j for j in ({i}|neighbors[i])) for i in range(m)]
faces={s for s in range(1<<m) if all(s&c!=c for c in closed)}
assert len(faces)==32391
assert all((s ^ (1<<j)) in faces for s in faces for j in range(m) if s & (1<<j))
fvec=Counter(s.bit_count()-1 for s in faces if s)
assert [fvec[i] for i in range(12)] == [16,120,560,1804,4176,6976,8208,6462,3136,832,96,4]

# A fully specified greedy vertex-toggle matching.
unmatched=set(faces)
pairs=[]
for vertex in range(m):
    bit=1<<vertex
    for low in sorted(unmatched):
        hi=low|bit
        if not (low&bit) and low in unmatched and hi in unmatched:
            unmatched.remove(low);unmatched.remove(hi);pairs.append((low,hi))
assert len(pairs)==16192
assert len(unmatched)==7
assert all(x.bit_count()==8 for x in unmatched)
assert (0,1) in pairs
pairs.remove((0,1))
critical=unmatched|{1}
assert Counter(s.bit_count()-1 for s in critical)=={0:1,7:7}
match=set(pairs)

# Exhaustive directed Hasse graph: downward edges except upward matches.
nonempty=faces-{0}
indegree={s:0 for s in nonempty}
out={s:[] for s in nonempty}
arrows=0
for upper in nonempty:
    for j in range(m):
        if not (upper>>j&1):continue
        lower=upper^(1<<j)
        if lower==0:continue
        a,b=(lower,upper) if (lower,upper) in match else (upper,lower)
        out[a].append(b);indegree[b]+=1;arrows+=1
queue=[s for s in nonempty if indegree[s]==0]
heapq.heapify(queue)
removed=0
while queue:
    s=heapq.heappop(queue);removed+=1
    for t in out[s]:
        indegree[t]-=1
        if indegree[t]==0:heapq.heappush(queue,t)
assert removed==len(nonempty)==32390

# Exact signed trace of each rotation on every oriented simplicial face.
def permutation_sign(moved):
    return -1 if (sum(moved[i]>moved[j] for i in range(len(moved))
                      for j in range(i+1,len(moved)))&1) else 1
traces=[]
for t in range(8):
    perm=[(i+t)%8 if i<8 else 8+(i-8+t)%8 for i in range(m)]
    reduced_lefschetz=-1
    for s in nonempty:
        chosen=[i for i in range(m) if s>>i&1]
        images=[perm[i] for i in chosen]
        if sum(1<<j for j in images)!=s:continue
        reduced_lefschetz+=(-1)**(len(chosen)-1)*permutation_sign(images)
    # The Morse model has reduced homology in degree seven only.
    traces.append(-reduced_lefschetz)
assert traces==[7,-1,3,-1,7,-1,3,-1]
print('Morse and cyclic character verification: PASS')
print('nonempty faces:',len(nonempty),'fvector:',[fvec[i] for i in range(12)])
print('acyclic gradient:',removed,'vertices;',arrows,'cover arrows')
print('matched pairs:',len(pairs),'critical:',[(d,Counter(s.bit_count()-1 for s in critical)[d]) for d in (0,7)])
print('critical seven-face masks:',sorted(unmatched))
print('rotation traces:',traces)
print('representation: Q^2 plus sign^3 plus Q(i), inflated from C4')
