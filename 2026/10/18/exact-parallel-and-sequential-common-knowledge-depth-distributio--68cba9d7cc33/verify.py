#!/usr/bin/env python3
"""Exhaustive checks of common-knowledge approximation depth, standard-library only."""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import factorial

def partitions(n):
    if n == 0:
        yield ()
        return
    def rec(a, m):
        if len(a) == n:
            yield tuple(a)
            return
        for j in range(m+2):
            yield from rec(a+[j], max(m,j))
    yield from rec([0],0)

def involutions(n):
    if n == 0:
        yield ()
        return
    def rec(items):
        if not items:
            yield ()
            return
        a=items[0]
        for rest in rec(items[1:]):
            yield ((a,),)+rest
        for b in items[1:]:
            for rest in rec([v for v in items[1:] if v!=b]):
                yield ((a,b),)+rest
    for blocks in rec(list(range(n))):
        p=[None]*n
        for i,block in enumerate(blocks):
            for v in block:p[v]=i
        yield tuple(p)

def adjacency(a,b):
    n=len(a)
    A=[{v for v in range(n) if a[u]==a[v]} for u in range(n)]
    B=[{v for v in range(n) if b[u]==b[v]} for u in range(n)]
    return A,B

def reach_row(A,B, mode):
    n=len(A)
    rows=[]
    for u in range(n):
        if mode=='parallel':rows.append(A[u]|B[u])
        else:rows.append(set().union(*(B[v] for v in A[u])))
    return rows

def depth_by_relation(A,B,mode):
    rows=reach_row(A,B,mode)
    n=len(A)
    target=[]
    for u in range(n):
        seen={u}; front=[u]
        for x in front:
            for v in A[x]|B[x]:
                if v not in seen: seen.add(v);front.append(v)
        target.append(seen)
    current=[{u} for u in range(n)]
    for k in range(n+1):
        if all(current[u]==target[u] for u in range(n)):
            return k
        current=[set().union(*(rows[v] for v in current[u])) for u in range(n)]
    raise AssertionError('no stabilization')

def cutoff(n,d,mode):
    # Paths of size r have r! labeled structures, r>=2; cycles 2j have (2j-1)!.
    maxpath=(d+1 if mode=='parallel' else 2*d)
    maxcycle=(d if mode=='parallel' else 2*d)
    # For d=0, isolated vertices only.
    coeff=[Fraction(0) for _ in range(n+1)]
    coeff[0]=Fraction(1)
    terms=[(1,Fraction(1))]
    terms += [(r,Fraction(1)) for r in range(2,min(maxpath,n)+1)]
    terms += [(2*j,Fraction(1,2*j)) for j in range(1,min(maxcycle,n//2)+1)]
    for degree,coefficient in terms:
        new=[Fraction(0) for _ in range(n+1)]
        for k,c in enumerate(coeff):
            t=0
            while k+degree*t<=n:
                new[k+degree*t]+=c*coefficient**t/factorial(t)
                t+=1
        coeff=new
    result=coeff[n]*factorial(n)
    assert result.denominator==1
    return int(result)

def perfect(p):
    return all(sum(1 for q in p if q==c)==2 for c in set(p))

def test():
    for n in range(1,8):
        inv=list(involutions(n)); t=len(inv)**2
        hist={mode:Counter() for mode in ('parallel','sequential')}
        for a,b in product(inv,repeat=2):
            A,B=adjacency(a,b)
            for mode in hist:hist[mode][depth_by_relation(A,B,mode)]+=1
        for mode in hist:
            for d in range(0,n+1):
                direct=sum(c for k,c in hist[mode].items() if k<=d)
                formal=cutoff(n,d,mode)
                assert direct==formal,(n,mode,d,direct,formal)
        print('binary-at-most-2',n,'total',t,'parallel',sorted(hist['parallel'].items()),'sequential',sorted(hist['sequential'].items()))
    for n in range(3,7):
        ps=list(partitions(n));mx=Counter()
        for a,b in product(ps,repeat=2):
            A,B=adjacency(a,b)
            mx[depth_by_relation(A,B,'parallel')]+=1
        assert mx[n-1]==factorial(n),(n,mx)
        print('all-S5',n,'maxdepth-count',mx[n-1])
    for n in (2,4,6,8):
        ms=[a for a in involutions(n) if perfect(a)]
        total=len(ms)**2
        histP=Counter();histS=Counter()
        for a,b in product(ms,repeat=2):
            A,B=adjacency(a,b)
            histP[depth_by_relation(A,B,'parallel')]+=1
            histS[depth_by_relation(A,B,'sequential')]+=1
        assert histP[n//2]==factorial(n-1)
        print('binary-exactly-2',n,'total',total,'parallel',sorted(histP.items()),'sequential',sorted(histS.items()))
    # Truly independent truth-set semantics check (no relation powers).
    for n in range(1,5):
        for a,b in product(involutions(n),repeat=2):
            A,B=adjacency(a,b)
            components=[]
            for u in range(n):
                seen={u}; queue=[u]
                for x in queue:
                    for v in A[x]|B[x]:
                        if v not in seen:seen.add(v);queue.append(v)
                components.append(seen)
            for mask in range(1<<n):
                P={u for u in range(n) if mask&(1<<u)}
                C={u for u in range(n) if components[u]<=P}
                for mode in ('parallel','sequential'):
                    X=set(P)
                    iterations=None
                    for k in range(n+1):
                        if X==C:
                            iterations=k;break
                        if mode=='parallel':
                            X={u for u in range(n) if A[u]<=X and B[u]<=X}
                        else:
                            Y={u for u in range(n) if B[u]<=X}
                            X={u for u in range(n) if A[u]<=Y}
                    assert iterations is not None
                    assert iterations<=depth_by_relation(A,B,mode)
        print('truth-set semantics',n,'PASS')
    print('VERIFY_OK')
if __name__=='__main__': test()
