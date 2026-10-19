"""Standalone exact verification for a pair of graphical Lie algebras.

No external dependencies. Run: python verify.py
"""
from collections import Counter
from itertools import combinations, permutations, product
from pathlib import Path

EDGES_G = ((0,1),(0,2),(0,3),(0,4),(1,4),(2,3),(3,5))
EDGES_H = ((0,4),(0,5),(1,3),(1,4),(2,3),(2,4),(3,4))
N=6

def graph_edges(n, bits):
    pairs=list(combinations(range(n),2))
    return tuple(p for i,p in enumerate(pairs) if bits>>i & 1)

def adj(n, edges):
    a=[0]*n
    for u,v in edges:
        a[u]|=1<<v
        a[v]|=1<<u
    return a

def components(n, a, mask):
    unvisited=mask
    out=[]
    while unvisited:
        start=unvisited & -unvisited
        unvisited^=start
        comp=start; queue=start
        while queue:
            x=queue & -queue;queue^=x
            v=x.bit_length()-1
            fresh=a[v]&unvisited
            queue|=fresh
            comp|=fresh
            unvisited^=fresh
        out.append(comp)
    return out

def profile(n,edges):
    a=adj(n,edges)
    hist=Counter()
    for S in range(1<<n):
        closed=S
        for u in range(n):
            if S>>u&1:closed|=a[u]
        sizes=tuple(sorted(c.bit_count() for c in components(n,a,S)))
        hist[(closed.bit_count(),sizes)]+=1
    assert sum(hist.values())==1<<n
    return hist

def rank_one_signature(n,edges):
    a=adj(n,edges)
    hist=Counter()
    for S in range(1<<n):
        closed=S
        for u in range(n):
            if S>>u&1:closed|=a[u]
        c=len(components(n,a,S))
        hist[(S.bit_count(),closed.bit_count()-c)]+=1
    return tuple(sorted(hist.items()))

def connected(n,edges):
    return len(components(n,adj(n,edges),(1<<n)-1))==1

def canonical(n,edges):
    # Exhaustive vertex relabelling (not a hash or graph atlas lookup).
    a=set(tuple(sorted(pair)) for pair in edges)
    pos={pair:i for i,pair in enumerate(combinations(range(n),2))}
    best=None
    for pi in permutations(range(n)):
        bits=0
        for u,v in a:
            pair=tuple(sorted((pi[u],pi[v])))
            bits|=1<<pos[pair]
        if best is None or bits<best:best=bits
    return best

def smallest_order_check():
    expected={1:1,2:1,3:2,4:6,5:21}
    for n in range(1,6):
        signatures={}
        canon_seen=set()
        total=0
        for bits in range(1<<(n*(n-1)//2)):
            e=graph_edges(n,bits)
            if not connected(n,e):continue
            total+=1
            c=canonical(n,e)
            if c in canon_seen:continue
            canon_seen.add(c)
            sig=rank_one_signature(n,e)
            if sig in signatures and signatures[sig]!=c:
                raise AssertionError(('pre-six collision',n,bits,signatures[sig],c))
            signatures[sig]=c
        assert len(canon_seen)==len(signatures)==expected[n],(n,len(canon_seen),len(signatures))
        print('ORDER',n,'connected classes',len(canon_seen),'distinct one-element rank signatures',len(signatures),'labeled connected',total)

def sixth_order_smaller_edge_check():
    n=6
    allpairs=tuple(combinations(range(n),2))
    for m,expected in ((5,6),(6,13)):
        signature_class={}
        unique_classes=set()
        labeled=0
        for edges in combinations(allpairs,m):
            if not connected(n,edges):
                continue
            labeled+=1
            signature=rank_one_signature(n,edges)
            previous=signature_class.get(signature)
            if previous is None:
                previous=canonical(n,edges)
                signature_class[signature]=previous
            else:
                assert canonical(n,edges)==previous,(m,edges)
            unique_classes.add(previous)
        assert len(unique_classes)==len(signature_class)==expected
        print('ORDER_6_EDGES',m,'classes',len(unique_classes),'labeled connected',labeled)

def triangle_profile(n,edges):
    e=set(edges)
    tri=Counter({v:0 for v in range(n)})
    for u,v,w in combinations(range(n),3):
        if (u,v) in e and (u,w) in e and (v,w) in e:
            for x in (u,v,w):tri[x]+=1
    return tuple(sorted(tri.values()))

def rank_mod(A,q):
    A=[list(row) for row in A]
    if not A:return 0
    m=len(A);n=len(A[0]);i=0
    for j in range(n):
        pivot=next((k for k in range(i,m) if A[k][j]%q),None)
        if pivot is None:continue
        A[i],A[pivot]=A[pivot],A[i]
        inv=pow(A[i][j],-1,q)
        A[i]=[(v*inv)%q for v in A[i]]
        for k in range(m):
            if k!=i:
                h=A[k][j]%q
                if h:A[k]=[(x-h*y)%q for x,y in zip(A[k],A[i])]
        i+=1
        if i==m:break
    return i

def brute_tuples(n,edges,q,t):
    hist=Counter()
    for flat in product(range(q),repeat=n*t):
        vectors=[flat[t*i:t*(i+1)] for i in range(n)]
        rows=[]
        for u,v in edges:
            for j in range(t):
                r=[0]*n
                r[u]=-vectors[v][j]%q
                r[v]=vectors[u][j]%q
                rows.append(r)
        hist[rank_mod(rows,q)]+=1
    return hist

def predicted(n,edges,q,t):
    a=adj(n,edges)
    hist=Counter()
    P=(q**t-1)//(q-1)
    for mask in range(1<<n):
        closed=mask
        for u in range(n):
            if mask>>u&1:closed|=a[u]
        h=Counter({0:1})
        for C in components(n,a,mask):
            c=C.bit_count()
            yes=P*(q-1)**c
            no=(q**t-1)**c-yes
            hh=Counter()
            for mono,count in h.items():
                hh[mono]+=count*no
                hh[mono+1]+=count*yes
            h=hh
        for mono,count in h.items():
            hist[closed.bit_count()-mono]+=count
    assert sum(hist.values())==q**(n*t)
    return hist

def main():
    assert len(EDGES_G)==len(EDGES_H)==7
    assert connected(N,EDGES_G) and connected(N,EDGES_H)
    assert triangle_profile(N,EDGES_G)!=(triangle_profile(N,EDGES_H))
    print('TRIANGLES',triangle_profile(N,EDGES_G),triangle_profile(N,EDGES_H))
    P=profile(N,EDGES_G)
    assert P==profile(N,EDGES_H)
    tab=Path(__file__).with_name('profile.tsv').read_text(encoding='utf-8')
    exp=Counter()
    for line in tab.splitlines():
        if not line or line.startswith('#'):continue
        closed,parts,amount=line.split('\t')
        part=tuple(int(x) for x in parts.split(',') if x)
        exp[(int(closed),part)]=int(amount)
    assert exp==P and sum(exp.values())==64
    print('PROFILE_ROWS',len(P),'ALL_SUBSETS',sum(P.values()))
    assert rank_one_signature(N,EDGES_G)==rank_one_signature(N,EDGES_H)
    for q,t in [(2,1),(3,1),(2,2),(3,2),(2,3),(5,2)]:
        p1=predicted(N,EDGES_G,q,t)
        p2=predicted(N,EDGES_H,q,t)
        assert p1==p2,(q,t,p1,p2)
        print('PREDICTED',q,t,sorted(p1.items()))
    for q,t in [(2,1),(3,1),(2,2)]:
        a=brute_tuples(N,EDGES_G,q,t)
        b=brute_tuples(N,EDGES_H,q,t)
        assert a==b==predicted(N,EDGES_G,q,t)
        print('DIRECT_MATRIX',q,t,'OK')
    smallest_order_check()
    sixth_order_smaller_edge_check()
    print('VERIFY_OK')

if __name__=='__main__':main()
