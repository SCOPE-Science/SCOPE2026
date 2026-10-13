#!/usr/bin/env python3
"""Finite deterministic-frame color-generation theorem: independent exhaustive tests.
Uses only the Python standard library.  Run: python verify.py
"""
import itertools, math, random
from collections import Counter


def mobius(n):
    ps = 0
    d = 2
    while d * d <= n:
        if n % d == 0:
            n //= d
            if n % d == 0:
                return 0
            ps += 1
        d += 1
    if n > 1:
        ps += 1
    return -1 if ps % 2 else 1


def primitive(q, m):
    return sum(mobius(d)*q**(m//d) for d in range(1,m+1) if m % d == 0)


def falling(a, b):
    p=1
    for j in range(b): p *= a-j
    return p


def cycle_data(f):
    n=len(f)
    cyc=set()
    lens=[]
    seen=set()
    for s in range(n):
        if s in seen: continue
        loc={}
        chain=[]
        x=s
        while x not in seen and x not in loc:
            loc[x]=len(chain); chain.append(x); x=f[x]
        if x in loc:
            cycle=chain[loc[x]:]
            cyc.update(cycle)
            lens.append(len(cycle))
        seen.update(chain)
    return cyc,Counter(lens)


def formula(f,q):
    cyc,lens=cycle_data(f)
    total=1
    for m,c in lens.items():
        P=primitive(q,m)
        for j in range(c): total *= P-j*m
    for v in range(len(f)):
        incoming=sum(1 for x in range(len(f)) if f[x]==v)
        if v in cyc:
            total *= falling(q-1,incoming-1)
        else:
            total *= falling(q,incoming)
    return total


def primitive_cycle_condition(f,letters):
    n=len(f)
    cyc=set()
    words_by_len={}
    seen=set()
    for s in range(n):
        if s in seen: continue
        loc={}; chain=[]; x=s
        while x not in seen and x not in loc:
            loc[x]=len(chain); chain.append(x); x=f[x]
        if x in loc:
            cycle=chain[loc[x]:]
            word=tuple(letters[x] for x in cycle)
            k=len(word)
            if any(word==word[j:]+word[:j] for j in range(1,k)): return False
            canonical=min(word[j:]+word[:j] for j in range(k))
            if canonical in words_by_len.setdefault(k,set()):return False
            words_by_len[k].add(canonical)
        seen.update(chain)
    # All children with a common successor must have distinct colors.
    for v in range(n):
        colors=[letters[x] for x in range(n) if f[x]==v]
        if len(colors)!=len(set(colors)):return False
    return True


def trace_partition_full(f,letters):
    # Independent Moore partition refinement, exact for finite deterministic systems.
    n=len(f)
    codes=list(letters)
    for iteration in range(n+1):
        index={}; refined=[]
        for u in range(n):
            key=(letters[u],codes[f[u]])
            if key not in index:index[key]=len(index)
            refined.append(index[key])
        if len(set(refined))==n:return True
        if all((codes[i]==codes[j]) == (refined[i]==refined[j]) for i in range(n) for j in range(n)):
            return False
        codes=refined
    raise AssertionError('refinement did not stabilize')


def direct_boolean_modal_closure_full(f,letters,q):
    # Independent algebra closure under unions, complements and inverse image.
    n=len(f); universe=(1<<n)-1
    sets={0,universe}
    for c in range(q):
        sets.add(sum(1<<v for v in range(n) if letters[v]==c))
    while True:
        new=set(sets)
        for s in sets:
            new.add(universe^s)
            new.add(sum(1<<v for v in range(n) if (s>>f[v])&1))
        vals=list(sets)
        for a in vals:
            for b in vals:new.add(a|b)
        if len(new)==len(sets):break
        sets=new
    return len(sets)==(1<<n)


def main():
    exhaustive=0; count_cases=0; direct=0; random_tests=0; rank=0
    for n,q in [(1,1),(2,1),(3,1),(4,1),(5,1),(1,2),(2,2),(3,2),(4,2),(5,2),
                (1,3),(2,3),(3,3),(4,3),
                (1,4),(2,4),(3,4),(4,4)]:
        for f in itertools.product(range(n),repeat=n):
            observed=0
            for a in itertools.product(range(q),repeat=n):
                truth=trace_partition_full(f,a)
                criterion=primitive_cycle_condition(f,a)
                assert truth==criterion,(f,a,truth,criterion)
                observed+=truth
                exhaustive+=1
                if n<=4 and q<=3:
                    closure=direct_boolean_modal_closure_full(f,a,q)
                    assert truth==closure,(f,a,truth,closure)
                    direct+=1
            assert observed==formula(f,q),(n,q,f,observed,formula(f,q))
            count_cases+=1
    rng=random.Random(20261009)
    for n in range(1,26):
        for _ in range(120):
            f=tuple(rng.randrange(n) for _ in range(n))
            for q in (2,3,4,6):
                a=tuple(rng.randrange(q) for _ in range(n))
                assert primitive_cycle_condition(f,a)==trace_partition_full(f,a)
                random_tests+=1
            if n<=10:
                c=[q for q in range(1,n+3) if formula(f,q)>0]
                assert c and min(c)<=n
                lo=min(c)
                assert all(formula(f,q)==0 for q in range(1,lo))
                cyc,lens=cycle_data(f)
                delta=max(sum(1 for x in f if x==v) for v in range(n))
                for q in range(1,n+3):
                    existence=(q>=delta and all(primitive(q,m)>=m*ct for m,ct in lens.items()))
                    assert (formula(f,q)>0)==existence
                    rank+=1
    # Nontrivial explicit examples.
    assert formula((0,0,0),4)==24
    assert formula((0,0,0),2)==0
    assert formula((1,2,0),2)==6
    assert formula((1,2,0,4,5,3),2)==18
    print('VERIFY_OK exhaustive_colorings',exhaustive,'full_census_graphs',count_cases,
          'direct_boolean_modal_closures',direct,'random_colorings',random_tests,
          'rank_boundaries',rank,
          'examples',(formula((0,0,0),4),formula((1,2,0,4,5,3),2)))

if __name__=='__main__':main()
