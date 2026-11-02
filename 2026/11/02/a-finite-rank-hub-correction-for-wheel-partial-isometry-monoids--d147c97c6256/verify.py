#!/usr/bin/env python3
"""Reproduce the wheel partial-isometry domain-rank theorem using only Python's standard library.

The predicted counts use cyclic run partitions. The independent check tests
all injective partial maps against the entire wheel distance relation.
"""
from collections import Counter
from itertools import combinations, permutations
from math import comb, factorial, prod


def partitions(k, lo=1):
    if k == 0:
        yield ()
    else:
        for part in range(lo, k + 1):
            for tail in partitions(k - part, part):
                yield (part,) + tail


def path_inventory(n):
    """Pairs (k, lambda) -> exact subset multiplicities for a cycle of length n."""
    inv = {}
    for k in range(1, n):
        for p in partitions(k):
            multiplicity = Counter(p)
            t = len(p)
            if t > n-k:
                continue
            b = (n * factorial(t-1) * comb(n-k-1, t-1)
                 // prod(factorial(c) for c in multiplicity.values()))
            inv[(k,p)] = b
    return inv


def cycle_coeff(n):
    out = Counter({0:1, n:2*n})
    for (k,p), b in path_inventory(n).items():
        mm = Counter(p)
        automorphisms = 2**(len(p)-mm.get(1,0))*prod(factorial(v) for v in mm.values())
        out[k] += automorphisms*b*b
    return out


def wheel_coeff(n):
    out = Counter()
    for k,c in cycle_coeff(n).items():
        out[k] += c
        out[k+1] += c
    for k,c in ((1,2*n),(2,5*n*n),(3,2*n*n*(n-1)),(4,2*n*n)):
        out[k] += c
    return out


def adjacency(n, wheel):
    size = n+1 if wheel else n
    adj = [[False]*size for _ in range(size)]
    start = 1 if wheel else 0
    for i in range(n):
        a = start+i
        b = start+(i+1)%n
        adj[a][b]=adj[b][a]=True
        if wheel:
            adj[0][a]=adj[a][0]=True
    return adj


def brute_partial_maps(n, wheel):
    adj=adjacency(n,wheel)
    N=len(adj)
    counts=Counter()
    exceptional=Counter()
    for k in range(N+1):
        for domain in combinations(range(N),k):
            for image_set in combinations(range(N),k):
                for values in permutations(image_set):
                    if all(adj[domain[i]][domain[j]] == adj[values[i]][values[j]]
                           for i in range(k) for j in range(i+1,k)):
                        counts[k] += 1
                        if wheel:
                            center_in_domain = (0 in domain)
                            if center_in_domain:
                                pos = domain.index(0)
                                generic = values[pos] == 0
                            else:
                                generic = (0 not in image_set)
                            if not generic:
                                exceptional[k] += 1
    return counts, exceptional


def run_type(subset, n):
    if not subset or len(subset)==n:
        return None
    components=[]
    seen=set()
    for i in subset:
        if i in seen:
            continue
        stack=[i]; seen.add(i); length=0
        while stack:
            x=stack.pop();length+=1
            for y in ((x-1)%n,(x+1)%n):
                if y in subset and y not in seen:
                    seen.add(y);stack.append(y)
        components.append(length)
    return tuple(sorted(components))


def check_run_inventory():
    for n in range(5,12):
        direct=Counter()
        for mask in range(1,1<<n):
            chosen={i for i in range(n) if (mask>>i)&1}
            if len(chosen)==n:
                continue
            direct[(len(chosen),run_type(chosen,n))]+=1
        formula=path_inventory(n)
        assert direct==formula,(n,direct,formula)
    print('RUN_INVENTORY_OK n=5..11')


def main():
    check_run_inventory()
    for n in range(5,8):
        circ,_ = brute_partial_maps(n,False)
        assert circ==cycle_coeff(n),('cycle',n,circ,cycle_coeff(n))
        brute,exc=brute_partial_maps(n,True)
        predicted=wheel_coeff(n)
        expected_exc=Counter({1:2*n,2:5*n*n,3:2*n*n*(n-1),4:2*n*n})
        assert brute==predicted,('wheel',n,brute,predicted)
        assert exc==expected_exc,('exception',n,exc,expected_exc)
        print('EXHAUSTIVE_OK',n,'rank_counts',','.join(str(brute[k]) for k in range(n+2)),
              'exceptional',','.join(str(exc[k]) for k in range(1,5)))
    for n in range(8,14):
        counts=wheel_coeff(n)
        expected=2*sum(cycle_coeff(n).values())+2*n+5*n*n+2*n**3
        assert sum(counts.values())==expected
        assert counts[n+1]==2*n
    print('POLYNOMIAL_INTERNAL_OK n=8..13')
    print('VERIFY_OK')

if __name__=='__main__':
    main()
