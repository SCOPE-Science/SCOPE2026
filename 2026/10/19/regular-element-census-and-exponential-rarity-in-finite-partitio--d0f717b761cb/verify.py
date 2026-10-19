"""Exact-arithmetic checks of regular transformation counts for finite block partitions.
Run: python verify.py. Uses only the Python standard library.
"""
from itertools import product
from math import comb


def onto(n, s):
    """Number of surjections [n] -> a specified s-set (zero if s>n)."""
    if s > n: return 0
    return sum((-1) ** j * comb(s, j) * (s-j)**n for j in range(s+1))


def local_count(sizes, target_size):
    """Count tuples of maps into a target_size-set whose union is one image."""
    return sum(comb(target_size, s) *
               (s**sum(sizes) - __import__('math').prod(s**n-onto(n,s) for n in sizes))
               for s in range(1, target_size+1))


def general_formula(ns):
    m=len(ns)
    ans=0
    for top in product(range(m),repeat=m):
        t=1
        for j in set(top):
            t*=local_count(tuple(ns[i] for i in range(m) if top[i]==j),ns[j])
        ans+=t
    return ans


def uniform_egf_formula(n,m):
    # m! [z^m] A_n(z)^m without rational coefficients
    from functools import lru_cache
    @lru_cache(None)
    def F(positions,boxes):
        if boxes==0: return int(positions==0)
        return sum(comb(positions,k)*(local_count((n,)*k,n) if k else 1)
                   *F(positions-k,boxes-1) for k in range(positions+1))
    return F(m,m)


def elements(ns):
    """Pairs (local map tuple, block character) in block-intrinsic coordinates."""
    m=len(ns)
    for top in product(range(m),repeat=m):
        choices=[list(product(range(ns[top[i]]), repeat=ns[i])) for i in range(m)]
        for fs in product(*choices): yield (fs,top)


def compose(a,b):
    # Right transformation composition: first a then b.
    fs, top=a
    gs, ntop=b
    return (tuple(tuple(gs[top[i]][fs[i][x]] for x in range(len(fs[i])))
                  for i in range(len(fs))),
            tuple(ntop[top[i]] for i in range(len(top))))


def is_regular_by_images(a):
    fs,top=a
    for j in set(top):
        pre=[i for i in range(len(top)) if top[i]==j]
        union=set().union(*(set(fs[i]) for i in pre))
        if not any(set(fs[i])==union for i in pre): return False
    return True


def has_inner_inverse(a, universe):
    for b in universe:
        if compose(compose(a,b),a)==a: return True
    return False


def run():
    for ns in [(1,), (2,), (3,), (1,2), (2,2), (2,3),
               (1,1,2), (1,2,2), (2,2,2), (3,2,1)]:
        universe=list(elements(ns))
        predicted=general_formula(ns)
        byimages=sum(is_regular_by_images(a) for a in universe)
        assert predicted==byimages,(ns,predicted,byimages)
        if len(set(ns))==1:
            assert predicted==uniform_egf_formula(ns[0],len(ns))
        print('blocks',ns,'regular',predicted,'of',len(universe))
        if len(universe)<=500:
            byinverse=sum(has_inner_inverse(a,universe) for a in universe)
            assert byinverse==predicted,(ns,byinverse,predicted)
            print('  exhaustive inner inverses:',byinverse)
        elif ns in [(1,2,2),(2,2,2),(3,2,1)]:
            import random
            rng=random.Random(sum(ns)*113+len(ns))
            yes=[a for a in universe if is_regular_by_images(a)]
            no=[a for a in universe if not is_regular_by_images(a)]
            sample=rng.sample(yes,min(20,len(yes)))+rng.sample(no,min(20,len(no)))
            assert all(has_inner_inverse(a,universe)==is_regular_by_images(a) for a in sample)
            print('  direct inverse spotchecks:',len(sample))
    for n in (2,3):
        for k in (2,3):
            maps=list(product(range(n),repeat=n))
            observed=sum(any(all(set(fs[i])<=set(fs[j]) for i in range(k)) for j in range(k))
                         for fs in product(maps,repeat=k))
            assert observed==local_count((n,)*k,n)
            print('local n,k',n,k,observed)
    print('ALL CHECKS PASSED')

if __name__=='__main__':run()
