#!/usr/bin/env python3
"""Finite stress tests for the theorem on computable constants in randomizations.
All infinite computability assertions require the mathematical proof in RESULT.md.
"""
from itertools import permutations, combinations, product
from fractions import Fraction

def group_automorphisms(n, relation):
    # Relation is an explicitly labelled binary relation.
    out=[]
    for p in permutations(range(n)):
        if all(((a,b) in relation)==((p[a],p[b]) in relation)
               for a in range(n) for b in range(n)):
            out.append(p)
    return out

def fixed(g, n):
    return frozenset(a for a in range(n) if all(p[a]==a for p in g))

def closure(g, S, n):
    stab=[p for p in g if all(p[a]==a for a in S)]
    assert stab
    return fixed(stab, n)

def analyze(g,n):
    full=frozenset(range(n))
    closed=[]
    for mask in range(1<<n):
        S=frozenset(a for a in range(n) if mask>>a&1)
        C=closure(g,S,n)
        assert S <= C
        assert closure(g,C,n)==C
        if C==S: closed.append(S)
    # Every fixed set of a family of automorphisms must be closed.
    # For small groups check all families; otherwise check generators and pairs.
    subsets=[]
    if len(g)<=12:
        for mask in range(1<<len(g)):
            subsets.append([g[i] for i in range(len(g)) if mask>>i&1])
    else:
        subsets=[[p] for p in g]
        subsets += [[g[i],g[j]] for i in range(min(len(g),20))
                    for j in range(i+1,min(len(g),20))]
        subsets += [g]
    for h in subsets:
        T=fixed(h,n)
        assert closure(g,T,n)==T
        assert T in closed
    assert full in closed
    return set(map(frozenset,closed))

def tests():
    tested=0
    for n in range(1,7):
        group=[tuple(p) for p in permutations(range(n))]
        closed=analyze(group,n)
        sizes={len(s) for s in closed}
        expected=({n} if n==1 else (set(range(n-1))|{n}))
        assert sizes==expected, (n,sizes,expected)
        assert len(closed)==(1 if n==1 else 2**n-n)
        tested+=1
    # All directed binary relations on at most three labels.
    directed=0
    for n in range(1,4):
        all_pairs=list(product(range(n), repeat=2))
        for mask in range(1<<len(all_pairs)):
            R={ab for i,ab in enumerate(all_pairs) if mask>>i&1}
            analyze(group_automorphisms(n,R),n)
            directed+=1
    # All undirected loop-free simple graphs on four vertices.
    undirected=0
    n=4
    pairs=list(combinations(range(n),2))
    for mask in range(1<<len(pairs)):
        E={e for i,e in enumerate(pairs) if mask>>i&1}
        R=E|{(b,a) for a,b in E}
        analyze(group_automorphisms(n,R),n)
        undirected+=1
    # In a finite-valued random variable, knowing all but one value
    # makes the event of being the remaining value the complement of
    # those known alternatives, exactly (not just approximately).
    metric=0
    for q in range(2,5):
        for length in range(1,5):
            for vals in product(range(q),repeat=length):
                missing=q-1
                actual=sum(v!=missing for v in vals)
                recovered=sum(sum(v==b for v in vals) for b in range(q-1))
                assert Fraction(actual,length)==Fraction(recovered,length)
                metric+=1
    print('ALL_CHECKS_OK pure_sizes=1..6 directed_binary_models=%d undirected_4_models=%d finite_event_instances=%d'%(directed,undirected,metric))

if __name__=='__main__':
    tests()
