"""Independent direct enumeration of paired dominating sets of variable-leaf coronas.
Run with Python 3 standard library: python paired_heterogeneous_verifier.py
"""
from functools import lru_cache
from itertools import combinations, product
from collections import Counter
from math import comb


def perfect_match(adj, selected):
    if selected.bit_count() % 2:
        return False
    @lru_cache(None)
    def search(mask):
        if not mask:
            return True
        lowest = mask & -mask
        v = lowest.bit_length()-1
        options = adj[v] & (mask ^ lowest)
        while options:
            b = options & -options
            if search(mask ^ lowest ^ b):
                return True
            options ^= b
        return False
    return search(selected)


def base_edges(n, edge_code):
    adj = [0]*n
    for bit,(u,v) in enumerate(combinations(range(n), 2)):
        if edge_code & (1 << bit):
            adj[u] |= 1 << v
            adj[v] |= 1 << u
    return adj


def decorate(base, multiplicities):
    n = len(base)
    result = [a for a in base] + [0]*sum(multiplicities)
    leaf = n
    for v,r in enumerate(multiplicities):
        for _ in range(r):
            result[v] |= 1 << leaf
            result[leaf] = 1 << v
            leaf += 1
    return result


def direct_counts(adj):
    counts=Counter()
    n=len(adj)
    for selected in range(1 << n):
        if selected.bit_count() & 1:
            continue
        if not all(selected >> v & 1 or adj[v] & selected for v in range(n)):
            continue
        if perfect_match(adj,selected):
            counts[selected.bit_count()] += 1
    return counts


def formula_counts(base, multiplicities):
    n=len(base)
    total=Counter()
    for subset in range(1 << n):
        if perfect_match(base,subset):
            coefficient=1
            for v,r in enumerate(multiplicities):
                if not (subset >> v) & 1:
                    coefficient *= r
            total[2*n-subset.bit_count()] += coefficient
    return total


def matching_counts(base):
    n=len(base)
    edges=[(i,j) for i in range(n) for j in range(i+1,n) if base[i] >> j & 1]
    total=Counter()
    for subset in range(1 << len(edges)):
        vertices=0
        allowed=True
        for bit,(u,v) in enumerate(edges):
            if subset >> bit & 1:
                endpoints=(1<<u)|(1<<v)
                if vertices & endpoints:
                    allowed=False
                    break
                vertices |= endpoints
        if allowed:
            total[subset.bit_count()] += 1
    return total


def even_cycle(base):
    n=len(base)
    from itertools import permutations
    for k in range(4,n+1,2):
        for nodes in combinations(range(n),k):
            for ordering in permutations(nodes[1:]):
                cyc=(nodes[0],)+ordering
                if all(base[cyc[i]] >> cyc[(i+1)%k] & 1 for i in range(k)):
                    return True
    return False


def main():
    tested=0
    candidates=0
    no_even=0
    # Every labeled graph and all (1,2)-leaf vectors through four base vertices.
    for n in range(1,5):
        for edge_code in range(1 << (n*(n-1)//2)):
            base=base_edges(n,edge_code)
            for rs in product((1,2),repeat=n):
                d=decorate(base,rs)
                got=direct_counts(d)
                expected=formula_counts(base,rs)
                assert got == expected, (n,edge_code,rs,got,expected)
                tested += 1
                candidates += 1 << len(d)
                if not even_cycle(base):
                    if rs == (1,)*n:
                        ordinary=matching_counts(base)
                        for k,count in ordinary.items():
                            assert expected[2*n-2*k]==count
                        no_even += 1
    # All labeled graphs through five vertices in the one-leaf specialization.
    for edge_code in range(1 << 10):
        base=base_edges(5,edge_code)
        rs=(1,)*5
        got=direct_counts(decorate(base,rs))
        expected=formula_counts(base,rs)
        assert got==expected, (5,edge_code)
        tested+=1
        candidates+=1<<10
        if not even_cycle(base):
            ordinary=matching_counts(base)
            for k,count in ordinary.items():
                assert expected[10-2*k]==count
            no_even+=1
    # Representative 5/6-vertex heterogeneous graphs.
    for n in (5,6):
        masks=[0,(1<<(n*(n-1)//2))-1]
        masks.extend((i*7919+127)%(1<<(n*(n-1)//2)) for i in range(24))
        for edge_code in masks:
            base=base_edges(n,edge_code)
            rs=tuple((v+edge_code)%2 + 1 for v in range(n))
            got=direct_counts(decorate(base,rs))
            expected=formula_counts(base,rs)
            assert got==expected,(n,edge_code,rs)
            tested+=1
            candidates+=1<<(n+sum(rs))
    # Even-cycle boundary: perfect matching multiplicity is not the support count.
    four_cycle=base_edges(4, (1<<1)|(1<<2)|(1<<3)|(1<<4))
    assert formula_counts(four_cycle,(1,1,1,1))[4]==1
    assert matching_counts(four_cycle)[2]==2
    # A path on n vertices has binom(n-k,k) k-matchings.
    for n in range(1,10):
        adj=[0]*n
        for v in range(n-1):
            adj[v]|=1<<(v+1)
            adj[v+1]|=1<<v
        a=formula_counts(adj,(1,)*n)
        assert all(a[2*n-2*k]==comb(n-k,k) for k in range(n//2+1))
    print('PASS: exact heterogeneous pendant-corona paired domination polynomials')
    print(f'Graph-and-leaf instances checked: {tested}')
    print(f'Direct candidate vertex-subsets checked: {candidates}')
    print(f'No-even-cycle unweighted matching comparisons: {no_even}')
    print('Full labeled graphs n<=4 with every leaf count 1 or 2; all labeled graphs n=5 with one leaf.')
    print('Additional representative heterogeneous n=5,6 cases (not exhaustive).')
    print('Checked cycle C4 support vs matching multiplicity 1 vs 2 and paths n<=9.')

if __name__=='__main__': main()
