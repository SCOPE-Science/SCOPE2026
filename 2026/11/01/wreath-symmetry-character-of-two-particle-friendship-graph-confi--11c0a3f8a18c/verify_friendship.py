"""Finite signed-cell and unimodular-minor checks for friendship graph configuration spaces.

Run: python3 verify_friendship.py
Requires only Python standard library. This does not replace the all-n proof.
"""
from itertools import permutations, product, combinations
from math import factorial
from collections import deque

def graph(n):
    v = list(range(2*n+1)); h=2*n
    edges=[]
    for i in range(n):
        edges.extend([(h,2*i),(h,2*i+1),(2*i,2*i+1)])
    return v,edges

def automorphisms(n):
    h=2*n
    for sig in permutations(range(n)):
        for flip in product(range(2),repeat=n):
            p=list(range(2*n+1))
            for i in range(n):
                for a in range(2):p[2*i+a]=2*sig[i]+(a^flip[i])
            p[h]=h
            yield sig,flip,tuple(p)

def checks(n):
    verts,edges=graph(n)
    ev={frozenset(e):i for i,e in enumerate(edges)}
    c0=list(combinations(verts,2))
    c1=[(i,v) for i,e in enumerate(edges) for v in verts if v not in e]
    c2=[(i,j) for i,j in combinations(range(len(edges)),2) if not set(edges[i])&set(edges[j])]
    ix0={x:i for i,x in enumerate(c0)}
    ix1={x:i for i,x in enumerate(c1)}
    assert len(c2)==5*n*(n-1)//2
    # Build integral cellular boundaries, and check d1*d2=0 exactly.
    d1=[]
    for e,v in c1:
        a,b=edges[e]
        d1.append({tuple(sorted((b,v))):1,tuple(sorted((a,v))):-1})
    d2=[]
    for e,f in c2:
        a,b=edges[e];c,d=edges[f]
        d2.append({(f,b):1,(f,a):-1,(e,d):-1,(e,c):1})
    for col in d2:
        total={}
        for row,k in col.items():
            for v,w in d1[ix1[row]].items():total[v]=total.get(v,0)+k*w
        assert all(x==0 for x in total.values())
    # The full-rank primitive integer minor: spoke-by-other-petal,
    # then petal-by-petal. Its diagonal blocks are signed identity matrices.
    S=[(3*i+a,3*j+2) for i in range(n) for a in range(2) for j in range(n) if i!=j]
    P=[(3*i+2,3*j+2) for i,j in combinations(range(n),2)]
    S=[tuple(sorted(x)) for x in S]; P=[tuple(sorted(x)) for x in P]
    assert set(S+P)==set(c2)
    sr=[(3*i+a,2*j) for i in range(n) for a in range(2) for j in range(n) if i!=j]
    pr=[(3*i+2,2*j) for i,j in combinations(range(n),2)]
    assert len(set(sr+pr))==len(c2)
    cols={s:d2[k] for k,s in enumerate(c2)}
    for i,s in enumerate(S):
        assert abs(cols[s].get(sr[i],0))==1
        assert all(cols[x].get(sr[i],0)==0 for x in S if x!=s)
    for i,s in enumerate(P):
        assert abs(cols[s].get(pr[i],0))==1
        assert all(cols[x].get(pr[i],0)==0 for x in P if x!=s)
        assert all(cols[x].get(r,0)==0 for x in P for r in sr)
    # Connectedness of unordered two-token graph on the original vertices.
    ad={x:set() for x in c0}
    for e,v in c1:
        a,b=edges[e];x=tuple(sorted((a,v)));y=tuple(sorted((b,v)))
        ad[x].add(y);ad[y].add(x)
    seen={c0[0]};que=deque([c0[0]])
    while que:
        for y in ad[que.popleft()]:
            if y not in seen:seen.add(y);que.append(y)
    assert len(seen)==len(c0)
    # Full signed chain Lefschetz calculation for every wreath-group element.
    for sig,flip,p in automorphisms(n):
        mapped=[]
        for e in edges:
            a,b=p[e[0]],p[e[1]]
            k=ev[frozenset((a,b))]
            mapped.append((k,1 if (a,b)==edges[k] else -1))
        tr0=sum(frozenset((p[a],p[b]))==frozenset((a,b)) for a,b in c0)
        tr1=sum(mapped[i][1] if mapped[i][0]==i and p[v]==v else 0 for i,v in c1)
        tr2=0
        for i,j in c2:
            a,sa=mapped[i];b,sb=mapped[j]
            if {a,b}=={i,j}:tr2+=sa*sb*(1 if a<b else -1)
        observed=1-tr0+tr1-tr2
        f=sum(sig[i]==i for i in range(n))
        t=sum(1 if flip[i]==0 else -1 for i in range(n) if sig[i]==i)
        f2=sum(sig[sig[i]]==i for i in range(n))
        predicted=((f-1)**2-(f2-1))//2 + f*t
        assert observed==predicted,(n,sig,flip,observed,predicted)
    rank=1-len(c0)+len(c1)-len(c2)
    assert rank==n*n+(n-1)*(n-2)//2
    print(f'n={n} cells={tuple(map(len,(c0,c1,c2)))} primitive_pivots={len(c2)} automorphisms={2**n*factorial(n)} H1_rank={rank} PASS')

if __name__=='__main__':
    for n in range(2,6):checks(n)
    print('FRIENDSHIP_WREATH_CHARACTER_AND_UNIMODULAR_MINOR_OK')
