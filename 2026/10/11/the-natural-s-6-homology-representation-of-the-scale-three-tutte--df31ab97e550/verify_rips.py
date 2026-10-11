"""Independent small-instance checks for graph-metric Rips complexes of GQ(2,2).
Uses only Python standard library. All tests are finite; the uniform proof is textual.
"""
from itertools import combinations
from collections import deque, Counter
from math import comb

letters = tuple(range(6))
points = tuple(combinations(letters, 2))

def perfect_matchings(v):
    if not v:
        yield ()
    else:
        a, *rest = v
        for b in rest:
            remaining = [x for x in rest if x != b]
            for M in perfect_matchings(remaining):
                yield tuple(sorted(((a,b),)+M))

lines = tuple(sorted(set(perfect_matchings(list(letters)))))
assert len(points) == len(lines) == 15
P, L = len(points), len(lines)
N = P+L
inc = {(i,P+j) for i,p in enumerate(points) for j,l in enumerate(lines) if p in l}
assert len(inc) == 45
adj = [set() for _ in range(N)]
for a,b in inc:
    adj[a].add(b); adj[b].add(a)
assert set(map(len,adj)) == {3}

def bfs(source):
    d=[-1]*N;d[source]=0;Q=deque([source])
    while Q:
        x=Q.popleft()
        for y in adj[x]:
            if d[y]<0:
                d[y]=d[x]+1;Q.append(y)
    return d
D=[bfs(i) for i in range(N)]
assert set(d for row in D for d in row)=={0,1,2,3,4}
assert all(D[i][j] in (1,3) for i in range(P) for j in range(P,N))
assert all(D[i][j] in (2,4) for i in range(P) for j in range(P) if i!=j)
assert all(D[i][j] in (2,4) for i in range(P,N) for j in range(P,N) if i!=j)

def cliques(vertices, k, distmax):
    # Enumerate all nonempty cliques using extension without duplicates.
    answer=[]
    def go(face, choices):
        for idx,x in enumerate(choices):
            f=face+(x,);answer.append(f)
            go(f,[y for y in choices[idx+1:] if D[x][y]<=distmax])
    go((),list(vertices))
    return answer

# Girth eight: enumerate nonbacktracking cycles of length up to six.
for root in range(N):
    def rec(path):
        if len(path)>=3 and path[-1] in adj[root]:
            assert len(path)>=8, 'incidence graph has a forbidden short cycle'
        if len(path)==7:return
        for v in adj[path[-1]]:
            if v!=root and v not in path:rec(path+[v])
    rec([root])

# Rips2: all nonempty simplices and a concrete acyclic matching
r2=cliques(range(N),0,2)
f2=Counter(map(len,r2))
assert [f2[k] for k in range(1,5)] == [30,135,120,30]
assert max(f2)==4
faces=set(r2)
paired={}
for f in r2:
    if len(f)<2:continue
    if all(x<P for x in f):
        cand=[j for j in range(P,N) if all(D[x][j]==1 for x in f)]
        assert len(cand)==1
        h=tuple(sorted(f+(cand[0],)))
        assert h in faces and f not in paired and h not in paired
        paired[f]=h;paired[h]=f
    elif all(x>=P for x in f):
        cand=[j for j in range(P) if all(D[x][j]==1 for x in f)]
        assert len(cand)==1
        h=tuple(sorted(f+(cand[0],)))
        assert h in faces and f not in paired and h not in paired
        paired[f]=h;paired[h]=f
assert len(paired)==240
unmatched=faces-set(paired)
assert len(unmatched)==75
assert unmatched=={(i,) for i in range(N)}|{tuple(sorted(e)) for e in inc}
# Check acyclic oriented Hasse graph: unmatched lower->higher; matched upper->lower.
out={f:[] for f in r2};indeg={f:0 for f in r2};hasse=0
for high in r2:
    for j in range(len(high)):
        low=high[:j]+high[j+1:]
        if not low:continue
        a,b=(high,low) if paired.get(low)==high else (low,high)
        out[a].append(b);indeg[b]+=1;hasse+=1
Q=deque(f for f in r2 if indeg[f]==0);vis=0
while Q:
    x=Q.popleft();vis+=1
    for y in out[x]:
        indeg[y]-=1
        if indeg[y]==0:Q.append(y)
assert vis==len(r2), '2-Rips collapse matching cyclic'

# At threshold three: the point and line sections must independently have
# clique complexes formed by their incidence blocks, and all mixed edges exist.
A=cliques(range(P),0,3)
B=cliques(range(P,N),0,3)
for side,cs in [('point',A),('line',B)]:
    fv=Counter(map(len,cs))
    assert [fv[k] for k in range(1,4)] == [15,45,15],(side,fv)
    assert max(fv)==3
    for f in cs:
        if len(f)>=2:
            cross=range(P,N) if side=='point' else range(P)
            centers=[v for v in cross if all(D[x][v]==1 for x in f)]
            assert len(centers)==1
assert all(D[i][j]<=3 for i in range(P) for j in range(P,N))

def rank_binary(cols):
    piv={}
    for x in cols:
        while x:
            p=x.bit_length()-1
            if p not in piv:
                piv[p]=x;break
            x ^= piv[p]
    return len(piv)

def boundary_ranks(cs):
    f_by_k={k:sorted(f for f in cs if len(f)==k) for k in range(1,4)}
    ranks=[]
    for k in (2,3):
        index={f:i for i,f in enumerate(f_by_k[k-1])}
        cols=[]
        for f in f_by_k[k]:
            col=0
            for j in range(k):col ^= 1<<index[f[:j]+f[j+1:]]
            cols.append(col)
        ranks.append(rank_binary(cols))
    return ranks
assert boundary_ranks(A)==[14,15]
assert boundary_ranks(B)==[14,15]
b=45-14-15
assert b==16
# The scale-three complex is literally A*B, and its complete f-vector is
# the convolution of the two face polynomials (empty face included).
F=[1,15,45,15]
join_f=[sum(F[i]*F[k-i] for i in range(len(F)) if 0<=k-i<len(F)) for k in range(7)]
assert join_f==[1,30,315,1380,2475,1350,225],join_f
# (Unreduced) Euler characteristic: 1 minus number of three-spheres.
chi=sum((-1)**(k-1)*join_f[k] for k in range(1,7))
assert chi == 1-b*b == -255
# All 30 vertices are connected at scale one. A collapse rel G preserves H1
# up to scale two; at scale three the joins give H3 rank 256; scale four
# is full simplex since the diameter is four.
print('DOILY_15_POINTS_15_LINES_45_FLAGS')
print('INCIDENCE_DIAMETER', max(max(row) for row in D))
print('RIPS_2_FACE_VECTOR', [f2[k] for k in range(1,5)])
print('RIPS_2_RELATIVE_COLLAPSE',len(paired)//2,'MATCHED_PAIRS',len(unmatched),'REMAINING_FACES','HASSE',hasse)
print('SCALE_3_SIDE_FACE_VECTOR',[15,45,15])
print('SCALE_3_SIDE_BOUNDARY_RANKS',[14,15])
print('RIPS_3_JOIN_F_VECTOR',[join_f[k] for k in range(1,7)])
print('REDUCED_HOMOLOGY_RANKS_SCALE_1_2_3',b,b,b*b)
print('RIPS_3_EULER',chi)
print('EXPECTED_INTERVALS_H1',[1,3,b], 'H3',[3,4,b*b])
print('VERIFY_OK')
