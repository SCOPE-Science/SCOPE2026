"""Complementary exact-cover and local-transformation verification."""
from itertools import combinations
from collections import Counter,deque
from math import comb,factorial

def is_dissociation(n,m):
    edges=[(i//n,i%n) for i in range(n*n) if m>>i&1]
    for x in edges:
        if sum(x!=y and (x[0]==y[0] or x[1]==y[1]) for y in edges)>1:return False
    return True

def brute(n):
    groups=Counter()
    for m in range(1<<(n*n)):
        if is_dissociation(n,m):groups[m.bit_count()]+=1
    ans=max(groups)
    print({'method':'complete_subset_enumeration','n':n,'maximum':ans,'number_maximum':groups[ans]})
    return ans,groups[ans]

def cover_sets(n):
    k=n//3
    # each two-edge star on three ORIGINAL vertices, first n rows and last n cols
    stars=[];by_vertex=[[] for _ in range(2*n)]
    for row in range(n):
        for cols in combinations(range(n),2):
            verts=frozenset((row,n+cols[0],n+cols[1]))
            edge_mask=(1<<(row*n+cols[0])) | (1<<(row*n+cols[1]))
            stars.append((verts,edge_mask,0))
    for col in range(n):
        for rows in combinations(range(n),2):
            verts=frozenset((rows[0],rows[1],n+col))
            edge_mask=(1<<(rows[0]*n+col)) | (1<<(rows[1]*n+col))
            stars.append((verts,edge_mask,1))
    for block in stars:
        for v in block[0]:by_vertex[v].append(block)
    full=frozenset(range(2*n));results=set()
    def rec(unused,mask,counts):
        if not unused:
            if counts==(k,k):results.add(mask)
            return
        v=min(unused)
        for vs,es,typ in by_vertex[v]:
            if counts[typ]>=k or not vs<=unused:continue
            cc=list(counts);cc[typ]+=1
            rec(unused-vs, mask|es,tuple(cc))
    rec(full,0,(0,0))
    return results

def neighbors(n,mask):
    # Reconstruct centers and their unordered two-leaf sets from selected edges.
    r={x:[] for x in range(n)};c={x:[] for x in range(n)}
    for i in range(n*n):
        if mask>>i&1:
            r[i//n].append(i%n);c[i%n].append(i//n)
    assert all(len(x) in (1,2) for x in r.values())
    assert all(len(x) in (1,2) for x in c.values())
    left={a:pair for a,pair in r.items() if len(pair)==2}
    right={b:pair for b,pair in c.items() if len(pair)==2}
    out=set()
    def replace(removed,added):
        q=mask
        for a,b in removed:q^=1<<(a*n+b)
        for a,b in added:q^=1<<(a*n+b)
        assert q!=mask and (q^mask).bit_count()==4
        out.add(q)
    for a,d in combinations(left,2):
        for b in left[a]:
            for e in left[d]:replace([(a,b),(d,e)],[(a,e),(d,b)])
    for b,e in combinations(right,2):
        for a in right[b]:
            for d in right[e]:replace([(a,b),(d,e)],[(a,e),(d,b)])
    for a,leafcols in left.items():
        for b,leafrows in right.items():
            for rleave in leafcols:
                cother=next(c for c in leafcols if c!=rleave)
                for dnew in leafrows:
                    lother=next(d for d in leafrows if d!=dnew)
                    replace([(a,cother),(lother,b)],[(dnew,cother),(lother,rleave)])
    return out

def check(n):
    states=cover_sets(n);assert len(states)==comb(n,n//3)**2*(factorial(2*(n//3))//2**(n//3))**2
    root=next(iter(states));seen={root};queue=deque([root]);degree=Counter()
    while queue:
        x=queue.popleft();nb=neighbors(n,x);degree[len(nb)]+=1
        assert nb<=states
        for y in nb:
            if y not in seen:seen.add(y);queue.append(y)
    assert len(seen)==len(states)
    assert degree==Counter({4*(n//3)**2+8*comb(n//3,2):len(states)})
    print({'method':'exact_cover_plus_explicit_moves','n':n,'maximum':4*(n//3),'number_maximum':len(states),'degree':next(iter(degree)),'components':1})
if __name__=='__main__':
    assert brute(3)==(4,9)
    assert brute(4)[0]==5
    check(3);check(6)
