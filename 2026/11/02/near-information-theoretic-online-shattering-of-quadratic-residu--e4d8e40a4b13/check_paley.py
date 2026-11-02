#!/usr/bin/env python3
"""Standalone finite checks for quadratic-residue translate incidence classes.
Run with Python 3.10+. This is corroborative; the theorem has an algebraic proof.
"""
from functools import lru_cache
from math import isqrt, log2, sqrt


def primes_to(n):
    return [p for p in range(3, n + 1, 2) if all(p % d for d in range(2, isqrt(p) + 1))]


def system(p):
    residues = {x*x % p for x in range(1,p)}
    chars = [0 if x == 0 else (1 if x in residues else -1) for x in range(p)]
    queries = [sum(1 << c for c in range(p) if (x-c) % p in residues) for x in range(p)]
    return chars, queries


def exact_depth(p, queries):
    allmask = (1 << p) - 1
    @lru_cache(None)
    def can(mask, depth):
        if not depth:
            return bool(mask)
        if mask.bit_count() < (1 << depth):
            return False
        if depth == 1:
            # Distinct concepts: any two columns disagree somewhere.
            return any((mask & q) and (mask & (allmask ^ q)) for q in queries)
        for query in queries:
            positive = mask & query
            negative = mask & (allmask ^ query)
            if min(positive.bit_count(), negative.bit_count()) < (1 << (depth-1)):
                continue
            if can(positive, depth-1) and can(negative, depth-1):
                return True
        return False
    # The additive translation group acts transitively on query locations.
    root_yes = queries[0]
    root_no = allmask ^ root_yes
    dmax = p.bit_length()-1
    for d in range(dmax, 0, -1):
        if min(root_yes.bit_count(), root_no.bit_count()) < 1 << (d-1):
            continue
        if can(root_yes, d-1) and can(root_no, d-1):
            return d, can.cache_info().currsize
    return 0, can.cache_info().currsize


def moment_checks(p, chi):
    if p <= 11:
        samples = range(1 << p)
    else:
        # Deterministic, multiplicatively spaced subsets and boundaries.
        samples = [0, (1<<p)-1]
        for a in range(min(128,p*3)):
            samples.append(sum(1 << c for c in range(p) if ((c*c+5*a*c+7*a*a+3*c+1) % p) < p//2))
    for mask in samples:
        centers = [c for c in range(p) if mask >> c & 1]
        m = len(centers)
        vals = [sum(chi[(x-c)%p] for c in centers) for x in range(p)]
        assert sum(v*v for v in vals) == m*(p-m), (p,mask,'moment')
        assert any(abs(v) <= sqrt(m)+1e-9 for v in vals), (p,mask,'split')
        for x,v in enumerate(vals):
            membership = sum(int(chi[(x-c)%p]==1) for c in centers)
            assert 2*membership == m+v-int(x in centers)
    return len(samples)


def threshold_check():
    assert abs((8-7)-1)<1e-10
    for d in range(1,51):
        t = 8*2**d - 7*2**(d/2)
        prev = 8*2**(d-1)-7*2**((d-1)/2)
        assert t-sqrt(t)-1 >= 2*prev-1e-8*max(1,t), (d,t,prev)
    return True


def main():
    threshold_check()
    print('ANALYTIC_THRESHOLD_INDUCTION_NUMERICAL_CHECK_PASS d=1..50')
    samples=0
    for p in primes_to(131):
        chars, queries = system(p)
        checked=moment_checks(p,chars)
        depth, states = exact_depth(p, queries)
        target=p.bit_length()-1
        assert depth == target, (p,depth,target)
        print('PRIME_CHECK_PASS p={} Ldim={} info_upper={} moment_subsets={} states={}'.format(p,depth,target,checked,states))
        samples+=checked
    print('QUADRATIC_RESIDUE_SECOND_MOMENT_CHECKS_PASS total_subsets={}'.format(samples))
    print('QUADRATIC_RESIDUE_ONLINE_SHATTERING_CHECKS_PASS')

# Extra quadratic-extension-field checks.
def extension_system(p, d):
    assert d not in {x*x%p for x in range(p)}
    def add(x,y):return ((x[0]+y[0])%p,(x[1]+y[1])%p)
    def neg(x):return ((-x[0])%p,(-x[1])%p)
    def mul(x,y):return ((x[0]*y[0]+d*x[1]*y[1])%p,(x[0]*y[1]+x[1]*y[0])%p)
    pts=[(a,b) for a in range(p) for b in range(p)]
    idx={x:i for i,x in enumerate(pts)}
    sq={mul(x,x) for x in pts if x!=(0,0)}
    char={x:(0 if x==(0,0) else (1 if x in sq else -1)) for x in pts}
    rows=[[char[add(x,neg(c))] for c in pts] for x in pts]
    qs=[sum(1<<j for j,c in enumerate(pts) if rows[i][j]==1) for i in range(p*p)]
    for n in (1,2,3,p*p//2,p*p):
        centers=list(range(n))
        vals=[sum(row[i] for i in centers) for row in rows]
        assert sum(v*v for v in vals)==n*(p*p-n)
    return qs

def check_extensions():
    for p,d in [(3,2),(5,2),(7,3)]:
        q=p*p
        queries=extension_system(p,d)
        depth,states=exact_depth(q,queries)
        assert depth==q.bit_length()-1
        print('EXTENSION_FIELD_PASS q={} depth={} states={}'.format(q,depth,states))

if __name__=='__main__':
    main()
    check_extensions()
