#!/usr/bin/env python3
"""Reproduce finite-order partial graph automorphism rank polynomials for complete multipartite graphs.

No external libraries are required. Formula evaluation uses cycle recurrences;
verification independently constructs maps on each induced subgraph.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations, permutations, product
from math import comb, factorial, lcm

@lru_cache(None)
def sigma_torsion(s, d):
    """Number of permutations of s labels whose d-th power is the identity."""
    if s == 0:
        return 1
    return sum(comb(s-1, j-1)*factorial(j-1)*sigma_torsion(s-j,d)
               for j in range(1,s+1) if d % j == 0)

@lru_cache(None)
def block_torsion(s, m, d):
    """Number of d-torsion elements in Sym(s) wr Sym(m)."""
    if m == 0:
        return 1
    return sum(comb(m-1,ell-1)*factorial(ell-1)*
               factorial(s)**(ell-1)*sigma_torsion(s,d//ell)*
               block_torsion(s,m-ell,d)
               for ell in range(1,m+1) if d % ell == 0)

def rank_polynomial(part_sizes, d):
    if not part_sizes or any(n < 1 for n in part_sizes) or d < 1:
        raise ValueError('Positive part sizes and positive power required')
    ans = Counter()
    for profile in product(*(range(n+1) for n in part_sizes)):
        ways = 1
        for n,s in zip(part_sizes,profile):
            ways *= comb(n,s)
        class_count = Counter(s for s in profile if s)
        for s,m in class_count.items():
            ways *= block_torsion(s,m,d)
        ans[sum(profile)] += ways
    return dict(sorted(ans.items()))

def direct_enumeration(part_sizes,d):
    """Independent exhaustive graph-adjacency and permutation-power tests."""
    groups = sum(([i]*n for i,n in enumerate(part_sizes)),[])
    size = len(groups)
    ans = Counter()
    for k in range(size+1):
        for subset in combinations(range(size),k):
            for arrangement in permutations(subset):
                f = dict(zip(subset,arrangement))
                power_ok = True
                for x in subset:
                    y=x
                    for _ in range(d):
                        y=f[y]
                    if y!=x:
                        power_ok=False
                        break
                if not power_ok:
                    continue
                adjacency_ok = all((groups[u]!=groups[v]) ==
                                   (groups[f[u]]!=groups[f[v]])
                                   for u in subset for v in subset)
                if adjacency_ok:
                    ans[k]+=1
    return dict(sorted(ans.items()))

def independent_sigma_torsion(s,d):
    count=0
    for arrangement in permutations(range(s)):
        p={i:x for i,x in enumerate(arrangement)}
        if all((lambda i: step_power(p,i,d))(i)==i for i in range(s)):
            count+=1
    return count

def step_power(perm,i,d):
    for _ in range(d):
        i=perm[i]
    return i

def run_checks():
    tests=[(2,2),(3,1),(2,1,1),(2,2,1),(3,2),(2,2,2),
           (4,1),(1,1,1,1),(3,1,1)]
    count=0
    for parts in tests:
        for d in [1,2,3,4,6]:
            predicted=rank_polynomial(parts,d)
            actual=direct_enumeration(parts,d)
            assert predicted == actual, (parts,d,predicted,actual)
            assert predicted[0]==1
            if d==1:
                assert all(predicted.get(k,0)==comb(sum(parts),k)
                           for k in range(sum(parts)+1))
            count += 1
    for s in range(7):
        for d in range(1,9):
            assert sigma_torsion(s,d)==independent_sigma_torsion(s,d)
    assert rank_polynomial((3,2),2)=={0:1,1:5,2:20,3:22,4:26,5:8}
    assert rank_polynomial((2,2,2),2)=={0:1,1:6,2:30,3:56,4:66,5:36,6:20}
    print('ALL_EXACT_CHECKS_PASSED',count,'full-graph cases',7*8,'symmetric-group cases')
    for parts in [(3,2),(2,2,2),(3,2,1)]:
        print(parts,'d=2',rank_polynomial(parts,2))
        print(parts,'d=6',rank_polynomial(parts,6))

if __name__=='__main__':
    run_checks()

# Power-preserving ambient extension refinement.
def extendible_rank_polynomial(part_sizes,d):
    ans=Counter()
    for profile in product(*(range(n+1) for n in part_sizes)):
        ways=1
        for n,s in zip(part_sizes,profile):
            ways*=comb(n,s)
        strata=Counter((s,n) for s,n in zip(profile,part_sizes) if s)
        for (s,n),m in strata.items():
            ways*=block_torsion(s,m,d)
        ans[sum(profile)]+=ways
    return dict(sorted(ans.items()))

def brute_extendible(part_sizes,d):
    """Enumerate global automorphisms of order dividing d, then all restrictions."""
    groups=sum(([i]*n for i,n in enumerate(part_sizes)),[])
    size=len(groups)
    admissible=set()
    for arr in permutations(range(size)):
        p=dict(enumerate(arr))
        if not all(step_power(p,i,d)==i for i in range(size)):
            continue
        if not all((groups[u]!=groups[v])==(groups[p[u]]!=groups[p[v]])
                   for u in range(size) for v in range(size)):
            continue
        for k in range(size+1):
            for subset in combinations(range(size),k):
                if set(p[i] for i in subset)!=set(subset):
                    continue
                admissible.add((subset,tuple(p[i] for i in subset)))
    out=Counter(len(x[0]) for x in admissible)
    return dict(sorted(out.items()))

def run_extension_checks():
    cases=[(2,2),(3,1),(2,1,1),(2,2,1),(3,2),(2,2,2),
           (4,1),(1,1,1,1),(3,1,1)]
    count=0
    for parts in cases:
        for d in [1,2,3,4,6]:
            e=extendible_rank_polynomial(parts,d)
            b=brute_extendible(parts,d)
            assert e==b, (parts,d,e,b)
            if d==2:
                gap=sum(x*y for i,x in enumerate(parts)
                        for y in parts[i+1:] if x!=y)
                p=rank_polynomial(parts,d)
                assert p[2]-e[2]==gap,(parts,gap,p[2],e[2])
                if len(set(parts))==1:
                    assert p==e
                else:
                    assert gap>0
            count+=1
    print('POWER_PRESERVING_EXTENSION_CHECKS_PASSED', count)

if __name__=='__main__':
    run_extension_checks()
