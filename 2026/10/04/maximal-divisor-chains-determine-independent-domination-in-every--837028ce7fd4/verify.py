#!/usr/bin/env python3
from collections import Counter
from itertools import combinations, permutations
import math

def factor(n):
    out=[]
    d=2
    m=n
    while d*d<=m:
        while m%d==0:
            out.append(d); m//=d
        d+=1
    if m>1: out.append(m)
    return out

def phi(n):
    r=n
    for p in set(factor(n)):
        r=r//p*(p-1)
    return r

def divisors(n):
    return [d for d in range(1,n+1) if n%d==0]

def proper_cells(n):
    return [d for d in divisors(n) if d not in (1,n)]

def incomparable(a,b):
    return a%b!=0 and b%a!=0

def is_chain(C):
    return all((a%b==0 or b%a==0) for a,b in combinations(C,2))

def is_maximal_chain(C,P):
    if not is_chain(C): return False
    C=set(C)
    return all(not is_chain(list(C|{e})) for e in P if e not in C)

def cell_union_size(n,C):
    return sum(phi(n//d) for d in C)

def max_chains_by_subset(n):
    P=proper_cells(n)
    out=[]
    for mask in range(1<<len(P)):
        C=[P[i] for i in range(len(P)) if mask>>i & 1]
        if C and is_maximal_chain(C,P):
            out.append(tuple(sorted(C)))
    return out

def distinct_multiset_words(primes):
    return sorted(set(permutations(primes)))

def chain_from_word(word):
    x=1; C=[]
    for p in word[:-1]:
        x*=p; C.append(x)
    return tuple(C)

def word_weight(word):
    # cell d_j = product of first j primes; n/d_j is suffix product
    return sum(phi(math.prod(word[j:])) for j in range(1,len(word)))

def polynomial_from_words(n):
    ps=factor(n)
    return Counter(word_weight(w) for w in distinct_multiset_words(ps))

def polynomial_from_chains(n):
    return Counter(cell_union_size(n,C) for C in max_chains_by_subset(n))

def extreme_formulas(n):
    ps=factor(n)
    counts=Counter(ps)
    distinct=sorted(counts)
    # minimum: largest primes first
    down=[]
    for p in reversed(distinct):
        down += [p]*counts[p]
    up=[]
    for p in distinct:
        up += [p]*counts[p]
    return word_weight(tuple(down)), word_weight(tuple(up))

def direct_vertex_graph(n):
    V=[a for a in range(1,n) if math.gcd(a,n)!=1]
    adj={a:set() for a in V}
    for a,b in combinations(V,2):
        da,db=math.gcd(a,n),math.gcd(b,n)
        if incomparable(da,db):
            adj[a].add(b); adj[b].add(a)
    return V,adj

def actual_independent_dominating_sets(n):
    V,adj=direct_vertex_graph(n)
    sets=[]
    for mask in range(1,1<<len(V)):
        S={V[i] for i in range(len(V)) if mask>>i&1}
        if any(v in adj[u] for u,v in combinations(S,2)):
            continue
        if all(v in S or (adj[v] & S) for v in V):
            sets.append(S)
    return sets

# Structural word-chain identity and extreme values on a broad finite stress suite.
tests=[4,6,8,10,12,14,15,18,20,24,27,28,30,36,40,42,45,48,54,56,60,72,84,90,100,105,120,180]
for n in tests:
    pw=polynomial_from_words(n)
    # Subset enumeration is cheap only for moderate divisor counts.
    if len(proper_cells(n)) <= 14:
        pc=polynomial_from_chains(n)
        assert pw==pc,(n,pw,pc)
    mn,mx=extreme_formulas(n)
    assert min(pw)==mn and max(pw)==mx,(n,pw,mn,mx)
    ps=factor(n)
    expected=math.factorial(len(ps))
    for a in Counter(ps).values():
        expected//=math.factorial(a)
    assert sum(pw.values())==expected,(n,pw,expected)

# Direct graph subset enumeration: no partial gcd-cell independent dominating sets survive.
for n in [4,6,8,10,12,14,15,18,20]:
    ids=actual_independent_dominating_sets(n)
    P=proper_cells(n)
    expected=[]
    for C in max_chains_by_subset(n):
        S={a for a in range(1,n) if math.gcd(a,n) in C}
        expected.append(S)
    assert {frozenset(s) for s in ids}=={frozenset(s) for s in expected}, (n,ids,expected)

assert polynomial_from_words(30)==Counter({3:1,4:1,5:1,8:1,10:1,12:1})
assert polynomial_from_words(48)==Counter({15:4,16:1})

print("VERIFY_OK")
print("direct_graph_checks=n in {4,6,8,10,12,14,15,18,20}")
print("word_chain_checks=28 composite moduli through 180")
print("Z30_polynomial=z^3+z^4+z^5+z^8+z^10+z^12")
print("Z48_polynomial=4z^15+z^16")
