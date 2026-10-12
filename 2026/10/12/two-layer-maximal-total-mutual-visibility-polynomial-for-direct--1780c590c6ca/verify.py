"""Direct finite check for maximal total-visibility configurations."""
from itertools import combinations
from math import comb,factorial
from random import Random

def expected(m,n):
    p=24*comb(m,4)*comb(n,4) if min(m,n)>=4 else 0
    f=lambda q:comb(q,2)*(comb(q,2)-1)*(comb(q,2)-2)
    s=comb(m,3)*f(n)+comb(n,3)*f(m)-6*comb(m,3)*comb(n,3)
    return p,s

def checks(m,n,mode='full'):
    N=m*n
    adj=[]
    for a in range(N):
        i,j=divmod(a,n)
        adj.append(sum(1<<b for b in range(N) if (lambda k,l: k!=i and l!=j)(*divmod(b,n))))
    covers=[]
    for a in range(N):
        for b in range(a+1,N):
            if not adj[a]>>b&1:
                q=adj[a]&adj[b]
                assert q
                covers.append(q)
    def valid(mask): return all(mask & q for q in covers)
    def classify(mask):
        rowsets=[set() for _ in range(m)]
        colsets=[set() for _ in range(n)]
        for a in range(N):
            if mask>>a&1:
                i,j=divmod(a,n);rowsets[i].add(j);colsets[j].add(i)
        usedrows=[r for r in rowsets if r];usedcols=[c for c in colsets if c]
        if mask.bit_count()==4:
            return len(usedrows)==4 and len(usedcols)==4
        if mask.bit_count()!=6:return False
        return ((len(usedrows)==3 and all(len(s)==2 for s in usedrows) and len({frozenset(s) for s in usedrows})==3)
                or (len(usedcols)==3 and all(len(s)==2 for s in usedcols) and len({frozenset(s) for s in usedcols})==3))
    c4=c6=0;tested=0
    masks=range(1<<N) if mode=='full' else [(1<<N)-1 if i==0 else Random(20261010+i).getrandbits(N) for i in range(10000)]
    for mask in masks:
        tested+=1
        if not valid(mask):
            if classify(mask): raise AssertionError(('predicted invalid',m,n,mask))
            continue
        minimal=all(not valid(mask^(1<<a)) for a in range(N) if mask>>a&1)
        pred=classify(mask)
        if minimal!=pred:raise AssertionError(('mismatch',m,n,mask, minimal,pred))
        if minimal:
            if mask.bit_count()==4:c4+=1
            else:c6+=1
    if mode=='full':
        assert (c4,c6)==expected(m,n),((m,n),(c4,c6),expected(m,n))
    return (m,n,mode,tested,c4,c6,expected(m,n))

if __name__=='__main__':
    for m,n,mode in [(3,3,'full'),(3,4,'full'),(3,5,'full'),(4,4,'full'),(4,5,'sample'),(5,5,'sample')]:
        print(checks(m,n,mode),flush=True)
    print('DIRECT_VISIBILITY_REPLAY_OK')
