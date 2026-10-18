#!/usr/bin/env python3
"""Independent small-instance verification of the disjointness concept-lattice classification."""
from itertools import combinations
from math import comb, factorial
import random

def case(n,k):
    attrs=[frozenset(s) for s in combinations(range(n),k)]
    universe=set(attrs)
    def closure(B):
        bset=[attrs[i] for i in B]
        common=[A for A in attrs if all(not (A & X) for X in bset)]
        return frozenset(i for i,A in enumerate(attrs) if all(not (A & Y) for Y in common))
    def explicit(B):
        U=set().union(*(attrs[i] for i in B)) if B else set()
        if len(U)>n-k: return frozenset(range(len(attrs)))
        return frozenset(i for i,A in enumerate(attrs) if A<=U)
    q=len(attrs)
    if q<=13:
        trials=(tuple(i for i in range(q) if b>>i&1) for b in range(1<<q))
    else:
        rng=random.Random(100*n+k)
        trials=[tuple(i for i in range(q) if rng.randrange(2)) for _ in range(500)]
        trials.extend([tuple(),tuple(range(q))]);trials.extend([(i,) for i in range(q)])
    ct=0
    for B in trials:
        assert closure(B)==explicit(B),(n,k,B)
        ct+=1
    CLOSED={closure([i for i,A in enumerate(attrs) if A<=set(U)]) for s in range(n+1) for U in combinations(range(n),s)}
    expected=2+sum(comb(n,t) for t in range(k,n-k+1))
    assert len(CLOSED)==expected,(n,k,len(CLOSED),expected)
    def level(U):
        if not U: return 0
        if len(U)==q:return n-2*k+2
        return min(s for s in range(k,n-k+1) if comb(s,k)==len(U))-k+1
    mu={}
    for U in sorted(CLOSED,key=lambda x:(level(x),len(x))):
        if not U: mu[U]=1
        else: mu[U]=-sum(mu[V] for V in mu if V < U)
        if U and len(U)!=q:
            s=next(s for s in range(k,n-k+1) if comb(s,k)==len(U))
            assert mu[U]==(-1)**(s-k+1)*comb(s-1,k-1)
    if n>2*k and k>=2:
        A=set(range(k));B=set(range(k,2*k));Z=A|{k}
        al=explicit([i for i,a in enumerate(attrs) if a==frozenset(A)])
        bl=explicit([i for i,a in enumerate(attrs) if a==frozenset(B)])
        zl=explicit([i for i,a in enumerate(attrs) if a==frozenset(A) or a==frozenset((A-{0})|{k})])
        def meet(X,Y):return X&Y
        def join(X,Y):return closure(X|Y)
        assert al<=zl
        assert join(al,meet(bl,zl))!=meet(join(al,bl),zl)
    if q <= 10:
        # Exhaustively calculate minimal Horn witness size for every nontrivial inference.
        best=0
        for m in range(1<<q):
            B=frozenset(i for i in range(q) if m>>i&1)
            full=closure(B)
            minimal=[q+1]*q
            for sub in range(1<<q):
                if sub & ~m:continue
                cl=closure(i for i in range(q) if sub>>i&1)
                r=sub.bit_count()
                for i in cl:
                    if r<minimal[i]:minimal[i]=r
            for i in full: best=max(best,minimal[i])
        target=1 if k==1 else n-2*k+2
        assert best==target,(n,k,best,target)
    return n,k,q,expected,ct,mu[frozenset(range(q))]

if __name__=='__main__':
    cases=[(n,k) for n in range(2,9) for k in range(1,n//2+1) if comb(n,k)<=24]
    results=[]
    for n,k in cases: results.append(case(n,k))
    print('CLOSURE_MOBIUS_MODULARITY_OK',len(results),'cases',results)
    def count_automorphisms(n,k):
        vs=[frozenset(c) for c in combinations(range(n),k)]
        q=len(vs)
        adj=[{j for j in range(q) if j!=i and len(vs[i]&vs[j])==k-1} for i in range(q)]
        order=[0]; seen={0}; pos=0
        while pos<len(order):
            u=order[pos];pos+=1
            for v in sorted(adj[u]):
                if v not in seen:seen.add(v);order.append(v)
        order.extend(v for v in range(q) if v not in seen)
        count=0
        def rec(pos,used,images):
            nonlocal count
            if pos==q:
                count+=1;return
            u=order[pos]
            for v in range(q):
                if used>>v&1:continue
                if any(((w in adj[u]) != (images[w] in adj[v])) for w in images):continue
                images[u]=v
                rec(pos+1,used|1<<v,images)
                del images[u]
        rec(0,0,{})
        return count
    for n,k in [(3,1),(4,2),(5,2),(6,2)]:
        order=count_automorphisms(n,k) if n>2*k else factorial(comb(n,k))
        expected=factorial(comb(n,k)) if n==2*k else factorial(n)
        assert order==expected,(n,k,order,expected)
        print('AUTOMORPHISM_OK',n,k,order)
    print('VERIFY_OK')
