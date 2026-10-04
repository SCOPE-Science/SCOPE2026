from itertools import product, combinations
from collections import deque
from math import prod


def build(qs):
    n=len(qs)
    vertices=[]
    classes={}
    for mask in range(1,(1<<n)-1):
        size=1
        for i,q in enumerate(qs):
            if (mask>>i)&1:
                size*=q-1
        cls=[]
        for j in range(size):
            v=(mask,j)
            vertices.append(v)
            cls.append(v)
        classes[mask]=cls
    adj={v:set() for v in vertices}
    for a,b in combinations(vertices,2):
        if a[0]&b[0]==0:
            adj[a].add(b); adj[b].add(a)
    return vertices,classes,adj


def distances(vertices,adj):
    D={}
    for s in vertices:
        d={s:0}; q=deque([s])
        while q:
            x=q.popleft()
            for y in adj[x]:
                if y not in d:
                    d[y]=d[x]+1; q.append(y)
        D[s]=d
    return D


def is_rd(W,vertices,adj,D):
    W=set(W)
    for v in vertices:
        if v not in W and not (adj[v]&W):
            return False
    seen={}
    order=sorted(W)
    for v in vertices:
        sig=tuple(D[v][w] for w in order)
        if sig in seen:
            return False
        seen[sig]=v
    return True


def formula(qs):
    n=len(qs)
    N=prod(qs)-prod(q-1 for q in qs)-1
    t=sum(q==2 for q in qs)
    return N-((1<<n)-2)+t


def canonical(qs,classes):
    n=len(qs)
    W=[]
    for mask,cls in classes.items():
        W.extend(cls[:-1])
    for i,q in enumerate(qs):
        if q==2:
            W.append(classes[1<<i][0])
    return list(dict.fromkeys(W))


def check_lower_accounting(qs,classes):
    n=len(qs)
    base=sum(len(cls)-1 for cls in classes.values())
    N=sum(len(cls) for cls in classes.values())
    assert base==N-((1<<n)-2)
    binary=[i for i,q in enumerate(qs) if q==2]
    pairs=[]
    for i in binary:
        a=1<<i
        b=((1<<n)-1)^a
        pairs.append((a,b))
        assert len(classes[a])==1
    flat=[x for p in pairs for x in p]
    assert len(flat)==len(set(flat))  # uses n>=3
    assert base+len(binary)==formula(qs)


def brute_opt(qs,vertices,adj,D):
    target=formula(qs)
    for k in range(target+1):
        for W in combinations(vertices,k):
            if is_rd(W,vertices,adj,D):
                return k
    raise AssertionError('no resolving dominating set found')

patterns=[]
for n in range(3,6):
    for qs in product((2,3,4), repeat=n):
        patterns.append(qs)

for qs in patterns:
    vertices,classes,adj=build(qs)
    D=distances(vertices,adj)
    W=canonical(qs,classes)
    assert len(W)==formula(qs)
    assert is_rd(W,vertices,adj,D)
    check_lower_accounting(qs,classes)
    if len(vertices)<=12:
        assert brute_opt(qs,vertices,adj,D)==formula(qs)

# Explicit mixed instances, including several twin-class multiplicities.
for qs in [(2,2,3),(2,3,3),(2,2,4),(2,3,4),(2,2,2,3),(2,3,3,3)]:
    vertices,classes,adj=build(qs)
    D=distances(vertices,adj)
    W=canonical(qs,classes)
    assert len(W)==formula(qs)
    assert is_rd(W,vertices,adj,D)

print('VERIFY_OK')
