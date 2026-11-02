"""Construct and verify minimum circular/linear covers for fixed-point-free complementary 4-palindromes.
No external dependencies. Run: python rc_cover_verify.py
"""
from collections import Counter
from itertools import product


def complement(x):
    return x ^ 1


def target(a, b):
    return (a, b, complement(b), complement(a))


def overlap_cost(x, y):
    for k in (3, 2, 1):
        if x[-k:] == y[:k]:
            return 4-k
    return 4


def modules(q):
    # Each module is (source vertex, destination vertex, first target (a,b), second target).
    m = q // 2
    edges = []
    def add(a, b):
        if b == complement(a):
            second = (complement(a), a)
            edges.append((a,a,(a,b),second))
        else:
            second = (complement(b), complement(a))
            edges.append((a,b,(a,b),second))
    for i in range(m):
        a = 2*i
        add(a,a)
        add(a,a^1)
        for j in range(i+1,m):
            b = 2*j
            add(a,b)
            add(b,a)
            add(a,b^1)
            add(b^1,a)
    assert len(edges) == q*q//2
    allpairs = [x for u,v,p,r in edges for x in (p,r)]
    assert len(set(allpairs)) == q*q
    assert set(allpairs) == set(product(range(q),repeat=2))
    return edges


def euler_modules(q):
    e = modules(q)
    adj = [[] for _ in range(q)]
    for k,(u,v,_,_) in enumerate(e): adj[u].append(k)
    pos = [0]*q
    stack=[(0,None)]
    out=[]
    while stack:
        u,_ =stack[-1]
        if pos[u]<len(adj[u]):
            k=adj[u][pos[u]];pos[u]+=1
            stack.append((e[k][1],k))
        else:
            _,k=stack.pop()
            if k is not None:out.append(k)
    out=out[::-1]
    assert len(out)==len(e) and len(set(out))==len(e)
    for k in range(len(out)):
        assert e[out[k]][1]==e[out[(k+1)%len(out)]][0]
    pairs=[]
    for k in out:
        u,v,p,r=e[k]
        pairs.extend([p,r])
    return pairs


def construct(q):
    assert q>=2 and q%2==0
    pairs=euler_modules(q)
    W=[target(*p) for p in pairs]
    costs=[overlap_cost(W[k],W[(k+1)%len(W)]) for k in range(len(W))]
    assert costs.count(3)==q*q//2
    assert costs.count(2)==q*(q-1)//2
    assert costs.count(1)==q//2
    L=sum(costs)
    assert L==(5*q*q-q)//2
    # For a cyclic cover concatenate the suffix of each target that begins after the preceding target overlap.
    cword=[]
    for k in range(len(W)):
        # Segment from start of kth target through beginning of next target has length costs[k].
        # This is the first costs[k] letters of current target, with continuation from future target for boundary.
        cword.extend(W[k][:costs[k]])
    assert len(cword)==L
    for k in range(len(W)):
        start=sum(costs[:k]); assert tuple(cword[(start+j)%L] for j in range(4))==W[k], (q,k,start, W[k])
    profiles={tuple(cword[(i+j)%L] for j in range(4)) for i in range(L)}
    assert set(W)<=profiles
    # Cut across one cost-three transition, which only has a one-symbol overlap.
    j=costs.index(3)
    offset=sum(costs[:j+1])%L
    rotated=cword[offset:]+cword[:offset]
    linear=rotated + rotated[:1]
    assert len(linear)==L+1
    assert set(W)<={tuple(linear[i:i+4]) for i in range(len(linear)-3)}
    return cword,linear,costs


def exact_tsp(q):
    """Independent Held-Karp exact TSP and path; invoked only for q=2,4."""
    targets=[target(a,b) for a,b in product(range(q),repeat=2)]
    n=len(targets)
    D=[[overlap_cost(x,y) for y in targets] for x in targets]
    states={(1,0):0}
    for z in range(1,n):
        nxt={}
        for (mask,j),cost in states.items():
            for h in range(1,n):
                if mask>>h&1: continue
                key=(mask | 1<<h,h)
                val=cost+D[j][h]
                if val<nxt.get(key,10**10):nxt[key]=val
        states=nxt
    tour=min(v+D[j][0] for (mask,j),v in states.items())
    states={(1<<j,j):0 for j in range(n)}
    for z in range(1,n):
        nxt={}
        for (mask,j),cost in states.items():
            for h in range(n):
                if mask>>h&1: continue
                key=(mask | 1<<h,h)
                val=cost+D[j][h]
                if val<nxt.get(key,10**10):nxt[key]=val
        states=nxt
    path=4+min(states.values())
    return tour,path


def verify():
    for q in range(2,32,2):
        c,l,co=construct(q)
        if q in (2,4):
            opt=exact_tsp(q)
            assert opt==(len(c),len(l)), (q,opt,len(c),len(l))
        print('q=',q, 'targets=',q*q,'cyclic=',len(c),'linear=',len(l))
        if q in (2,4):print('cyclic witness', ''.join(map(str,c)),'linear witness',''.join(map(str,l)))
    print('VERIFY_OK')

if __name__=='__main__':verify()
