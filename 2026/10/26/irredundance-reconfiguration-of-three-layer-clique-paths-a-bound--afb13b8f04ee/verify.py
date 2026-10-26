"""Direct brute-force checks for maximal irredundance and slide reconfiguration.

Run with standard Python 3: python verify.py
Exhaustive domain: every vertex subset for n = 4, 5, 6, 7.
The infinite-family theorem is justified by the separate proof, not this checker.
"""
from collections import Counter, deque
from math import comb


def neighbours(n):
    """Closed neighborhoods of K_n Cartesian P_3, indexed layer*n+column."""
    out=[]
    for a in range(3):
        for i in range(n):
            mask=((1<<n)-1) << (a*n)
            if a>0: mask |= 1<<((a-1)*n+i)
            if a<2: mask |= 1<<((a+1)*n+i)
            out.append(mask)
    return out


def irredundant(mask, closed):
    """Raw definition: each chosen vertex has a unique closed-neighborhood witness."""
    chosen=[v for v in range(len(closed)) if mask & (1<<v)]
    for v in chosen:
        other_coverage=0
        for u in chosen:
            if u!=v: other_coverage |= closed[u]
        if not (closed[v] & ~other_coverage): return False
    return True


def predicted_irredundant(n, mask):
    q=(1<<n)-1
    A=mask&q
    B=(mask>>n)&q
    C=(mask>>(2*n))&q
    if not B:
        return (A&C)==0 or (A==C and A.bit_count()==1)
    if not A and not C: return True
    if A.bit_count()>1 or C.bit_count()>1: return False
    if A and C: return B.bit_count()==1
    return B!=q


def predicted_maximal(n, mask):
    q=(1<<n)-1
    A=mask&q
    B=(mask>>n)&q
    C=(mask>>(2*n))&q
    if B==0:
        return (A==q and C==0) or (C==q and A==0) or (bool(A) and bool(C) and (A&C)==0 and (A|C)==q)
    if not A and not C: return B==q
    if A and C: return A.bit_count()==B.bit_count()==C.bit_count()==1
    return (A.bit_count()+C.bit_count()==1) and B.bit_count()==n-1


def possible_edge(n, i, j):
    la,ca=divmod(i,n)
    lb,cb=divmod(j,n)
    return (la==lb and ca!=cb) or (ca==cb and abs(la-lb)==1)


def predicted_edges(n):
    """Set of unordered pairs of maximal n-vertex sets in the predicted IR graph."""
    q=(1<<n)-1
    middle=q<<n
    pairs=set()
    def add(x,y):
        if x!=y: pairs.add((min(x,y), max(x,y)))
    for outer in (0,2):
        X={}
        for i in range(n):
            for k in range(n):
                X[(i,k)]=(1<<(outer*n+i)) | ((q ^ (1<<k))<<n)
        for i in range(n):
            for k in range(n):
                x=X[(i,k)]
                for i2 in range(n): add(x,X[(i2,k)])
                for k2 in range(n): add(x,X[(i,k2)])
                if i==k: add(x,middle)
    return pairs


def main():
    subsets=0
    for n in (4,5,6,7):
        N=3*n
        closed=neighbours(n)
        good=set()
        predicted=set()
        for S in range(1<<N):
            expected=predicted_irredundant(n,S)
            actual=irredundant(S,closed)
            assert actual==expected, (n,'irredundance',S,expected,actual)
            subsets+=1
            if actual:good.add(S)
            if predicted_maximal(n,S):predicted.add(S)
        observed=Counter(S.bit_count() for S in good)
        formula={}
        for k in range(n+1):
            count=comb(n,k)*2**k
            if k>=1: count+=comb(n,k)
            if k==2: count+=n
            if 2<=k<=n: count+=2*n*comb(n,k-1)
            if k==3: count+=n**3
            formula[k]=count
        assert dict(observed)=={k:v for k,v in formula.items() if v}, (n,'all-set polynomial',observed,formula)
        maximal=set()
        for S in good:
            if all((S | (1<<v)) not in good for v in range(N) if not S&(1<<v)):
                maximal.add(S)
        assert maximal==predicted, (n,'maximal classification',maximal^predicted)
        size_counts=Counter(S.bit_count() for S in maximal)
        assert size_counts=={3:n**3,n:2*n*n+2**n+1},(n,size_counts)
        irsets=[S for S in maximal if S.bit_count()==n]
        raw_edges=set()
        for S in irsets:
            for u in range(N):
                if not S & (1<<u):continue
                for v in range(N):
                    if S&(1<<v) or not possible_edge(n,u,v):continue
                    T=S^(1<<u)^(1<<v)
                    if T in predicted: raw_edges.add((min(S,T),max(S,T)))
        expected_edges=predicted_edges(n)
        assert raw_edges==expected_edges,(n,'edges differ',len(raw_edges^expected_edges))
        adj={S:set() for S in irsets}
        for S,T in raw_edges: adj[S].add(T); adj[T].add(S)
        components=[]
        unseen=set(irsets)
        while unseen:
            root=unseen.pop(); component={root}; frontier=[root]
            while frontier:
                v=frontier.pop()
                for u in adj[v]:
                    if u not in component:
                        assert u in unseen
                        unseen.remove(u);component.add(u);frontier.append(u)
            components.append(component)
        assert Counter(len(C) for C in components)=={1:2**n, 2*n*n+1:1}
        core=next(C for C in components if len(C)>1)
        diam=0
        for root in core:
            dist={root:0}; queue=deque([root])
            while queue:
                v=queue.popleft()
                for u in adj[v]:
                    if u not in dist:dist[u]=dist[v]+1;queue.append(u)
            assert len(dist)==len(core)
            diam=max(diam,max(dist.values()))
        assert diam==4
        edge_count=2*n*n*(n-1)+2*n
        assert len(raw_edges)==edge_count
        print(f'n={n}: {1<<N} subsets; maximal={len(maximal)}; max-cardinality={len(irsets)}; IR edges={len(raw_edges)}; isolated={2**n}; core diameter={diam}')
    print(f'VERIFIED: {subsets} exhaustive subsets and all predicted IR-graph edges; n=4,5,6,7')

if __name__=='__main__': main()
