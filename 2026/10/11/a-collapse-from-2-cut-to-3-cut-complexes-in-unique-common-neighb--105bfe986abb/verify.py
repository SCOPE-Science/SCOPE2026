#!/usr/bin/env python3
from itertools import combinations
from collections import Counter, defaultdict, deque


def edges_from_mask(n, mask):
    pairs=list(combinations(range(n),2))
    return {pairs[i] for i in range(len(pairs)) if (mask>>i)&1}

def adjsets(n,E):
    A=[set() for _ in range(n)]
    for u,v in E:
        A[u].add(v); A[v].add(u)
    return A

def connected(n,A):
    seen={0}; q=[0]
    while q:
        u=q.pop()
        for v in A[u]-seen:
            seen.add(v); q.append(v)
    return len(seen)==n

def hypotheses(n,E):
    A=adjsets(n,E)
    if not connected(n,A): return False
    # triangle-free
    for a,b,c in combinations(range(n),3):
        if b in A[a] and c in A[a] and c in A[b]: return False
    # no 4-cycle: two distinct vertices never have two common neighbors
    for u,v in combinations(range(n),2):
        if len(A[u]&A[v])>=2: return False
    # diameter at most 2: every nonedge has a common neighbor
    for u,v in combinations(range(n),2):
        if v not in A[u] and not (A[u]&A[v]): return False
    return True

def disconnected_induced(S,A):
    S=set(S)
    if len(S)<=1: return False
    root=next(iter(S)); seen={root}; q=[root]
    while q:
        u=q.pop()
        for v in (A[u]&S)-seen:
            seen.add(v); q.append(v)
    return len(seen)<len(S)

def cut_faces(n,E,k):
    A=adjsets(n,E); V=set(range(n)); facets=[]
    for T in combinations(range(n),k):
        if disconnected_induced(T,A):
            facets.append(frozenset(V-set(T)))
    faces={frozenset()}
    for F in facets:
        xs=list(F)
        for r in range(1,len(xs)+1):
            for s in combinations(xs,r): faces.add(frozenset(s))
    return faces, set(facets)

def collapse_pairs(n,E):
    A=adjsets(n,E); V=set(range(n)); pairs=[]
    for u,v in combinations(range(n),2):
        if v not in A[u]:
            C=A[u]&A[v]
            assert len(C)==1
            w=next(iter(C))
            F=frozenset(V-{u,v})
            s=frozenset(V-{u,v,w})
            pairs.append((s,F))
    return pairs

def verify_collapse(n,E):
    f2,fac2=cut_faces(n,E,2); f3,fac3=cut_faces(n,E,3)
    pairs=collapse_pairs(n,E)
    # Every proposed lower face is free in the original Delta_2.
    for s,F in pairs:
        containers=[H for H in fac2 if s <= H]
        assert containers==[F] or set(containers)=={F}
    assert len({s for s,F in pairs})==len(pairs)
    assert len({F for s,F in pairs})==len(pairs)
    removed={x for p in pairs for x in p}
    assert f2-removed==f3
    return len(f2),len(f3),len(pairs)

# Exhaust all labeled graphs on 5 and 6 vertices satisfying the hypotheses.
class_counts={}
for n in (5,6):
    m=n*(n-1)//2; good=0
    for mask in range(1<<m):
        E=edges_from_mask(n,mask)
        if hypotheses(n,E):
            verify_collapse(n,E); good+=1
    class_counts[n]=good
assert class_counts=={5:17,6:6}, class_counts

# Petersen graph: outer 5-cycle, five spokes, inner star.
n=10
E=set()
def ae(u,v): E.add(tuple(sorted((u,v))))
for i in range(5):
    ae(i,(i+1)%5); ae(i,5+i); ae(5+i,5+((i+2)%5))
assert len(E)==15 and hypotheses(n,E)
nf2,nf3,npairs=verify_collapse(n,E)
F2,fac2=cut_faces(n,E,2); F3,fac3=cut_faces(n,E,3)

def fvec(F):
    c=Counter(len(x)-1 for x in F if x)
    return tuple(c[d] for d in range(max(c)+1))
assert fvec(F2)==(10,45,120,210,252,210,120,30)
assert fvec(F3)==(10,45,120,210,252,210,90)
assert npairs==30

# Independent discrete-Morse check on Delta_3(Petersen): deterministic element matching.
cells=sorted([tuple(sorted(s)) for s in F3 if s], key=lambda x:(len(x),x))
cellset=set(cells)
unmatched=set(cells); matching=[]
for v in range(n):
    used=set()
    for lower in sorted(unmatched, key=lambda x:(len(x),x)):
        if lower in used or v in lower: continue
        upper=tuple(sorted(lower+(v,)))
        if upper in unmatched and upper not in used and len(upper)==len(lower)+1:
            matching.append((lower,upper)); used.add(lower); used.add(upper)
    unmatched.difference_update(used)
crit=sorted(unmatched,key=lambda x:(len(x),x))
assert Counter(len(x)-1 for x in crit)=={0:1,6:6}
# Hasse covers and Forman orientation.
covers=[]
for upper in cells:
    if len(upper)<=1: continue
    for v in upper:
        lower=tuple(x for x in upper if x!=v)
        if lower in cellset: covers.append((lower,upper))
assert len(covers)==4440
matchset=set(matching); adj=defaultdict(list); indeg={c:0 for c in cells}
for lower,upper in covers:
    a,b=(lower,upper) if (lower,upper) in matchset else (upper,lower)
    adj[a].append(b); indeg[b]+=1
q=deque([c for c in cells if indeg[c]==0]); seen=0
while q:
    x=q.popleft(); seen+=1
    for y in adj[x]:
        indeg[y]-=1
        if indeg[y]==0: q.append(y)
assert seen==len(cells)

print('small_graph_hypothesis_counts n5=17 n6=6')
print('petersen_delta2_fvector=10,45,120,210,252,210,120,30')
print('petersen_delta3_fvector=10,45,120,210,252,210,90')
print('collapse_pairs=30 delta3_nonempty_faces=937')
print('petersen_delta3_morse_pairs=%d critical_dims=0,6,6,6,6,6,6 hasse=4440' % len(matching))
print('VERIFY_OK')
