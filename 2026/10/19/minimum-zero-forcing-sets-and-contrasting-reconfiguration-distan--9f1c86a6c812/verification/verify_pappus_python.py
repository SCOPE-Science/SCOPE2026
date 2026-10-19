"""Independent finite-incidence and symmetry-based verification of minimum zero forcing on Biaff(3)."""
from itertools import combinations,product
from collections import Counter,deque
from hashlib import sha256

def P(x,y):return 3*y+x
def L(m,b):return 9+3*b+m
N=18
EDGE=set()
for x,y,m,b in product(range(3),repeat=4):
    if (y-m*x-b)%3==0:
        EDGE.add(frozenset((P(x,y),L(m,b))))
assert len(EDGE)==27
nb=[set() for _ in range(N)]
for e in EDGE:
    u,v=tuple(e);nb[u].add(v);nb[v].add(u)
assert all(len(s)==3 for s in nb)

def zf(seed):
    blue=set(seed)
    while True:
        nxt=blue|{next(iter(nb[u]-blue)) for u in blue if len(nb[u]-blue)==1}
        if len(nxt)==len(blue):return len(blue)==N
        blue=nxt

sizes={};states=[]
for k in range(1,8):
    m=[frozenset(t) for t in combinations(range(N),k) if zf(t)]
    sizes[k]=len(m)
    if m:states=m;break
assert len(states)==6912 and k==7 and all(sizes.get(j)==0 for j in range(1,7))
S={s:i for i,s in enumerate(states)}
print('min_size',k,'count',len(states),'size_counts',sizes,flush=True)
print('bipartition',dict(sorted(Counter(sum(v<9 for v in s) for s in states).items())),flush=True)

def affine(a,d,c,e,f):
    out={}
    for x,y in product(range(3),repeat=2):out[P(x,y)]=P((a*x+c)%3,(d*y+e*x+f)%3)
    for m,b in product(range(3),repeat=2):
        mm=(d*m+e)*a%3
        bb=(d*b+f-mm*c)%3
        out[L(m,b)]=L(mm,bb)
    return out

def polarity():
    out={}
    for x,y in product(range(3),repeat=2):out[P(x,y)]=L(-x%3,y)
    for m,b in product(range(3),repeat=2):out[L(m,b)]=P(m,b)
    return out

def compose(A,B):return {x:A[B[x]] for x in range(N)}
D=polarity()
T=[];fingerprints=set()
for a,d in product([1,2],repeat=2):
    for c,e,f in product(range(3),repeat=3):
        g=affine(a,d,c,e,f)
        for h in (g,compose(D,g)):
            assert len(set(h.values()))==N
            assert {frozenset((h[u],h[v])) for u,v in (tuple(t) for t in EDGE)}==EDGE
            key=tuple(h[x] for x in range(N))
            if key not in fingerprints:fingerprints.add(key);T.append(h)
assert len(T)==216
print('checked_automorphisms',len(T),flush=True)

for sl in (False,True):
    links=[]
    for s in states:
        moves=set()
        for u in s:
            for v in (nb[u] if sl else range(N)):
                if v not in s:
                    t=frozenset((s-{u})|{v})
                    if t in S:moves.add(S[t])
        links.append(moves)
    assert all(i in links[j] for j,Ls in enumerate(links) for i in Ls)
    compseen=set();components=[]
    for i in range(len(states)):
        if i not in compseen:
            comp={i};q=[i]
            for t in q:
                for j in links[t]-comp:comp.add(j);q.append(j)
            compseen|=comp;components.append(len(comp))
    assert components==[6912]
    # Representative orbits of verified graph automorphisms.
    unseen=set(range(len(states)));reps=[]
    while unseen:
        r=min(unseen)
        orbit={S[frozenset(g[v] for v in states[r])] for g in T}
        assert orbit <= unseen
        reps.append((r,len(orbit)))
        unseen-=orbit
    eccs=Counter()
    witness=[]
    for r,mult in reps:
        distance={r:0}; q=deque([r])
        while q:
            u=q.popleft()
            for v in links[u]:
                if v not in distance:
                    distance[v]=distance[u]+1;q.append(v)
        assert len(distance)==len(states)
        e=max(distance.values());eccs[e]+=mult
        if e==max(eccs):witness.append((r,max(distance,key=distance.get),e))
    deg=Counter(map(len,links))
    print(('SLIDE' if sl else 'JUMP'), 'edges',sum(map(len,links))//2,'components',components,'group_orbits',len(reps),'ecc',dict(sorted(eccs.items())),'degrees',dict(sorted(deg.items())),flush=True)
    print('witness',witness[:3],flush=True)
    if sl:
        assert sum(map(len,links))//2==10962 and eccs==Counter({16:648,17:4968,18:1296})
    else:
        assert sum(map(len,links))//2==97524 and eccs==Counter({7:6912})
print('PYTHON_VERIFIED',flush=True)
