"""Finite, independently enumerated checks of maximal-subgroup intersections.
This script checks examples only; the general result uses a separate proof.
"""
from itertools import combinations, product
from math import prod


def hyperplanes(p, d):
    """Enumerate every codimension-one subspace as an actual tuple set."""
    vecs = list(product(range(p), repeat=d))
    seen = set()
    result = []
    for a in vecs[1:]:
        h = frozenset(x for x in vecs if sum(u*v for u,v in zip(a,x)) % p == 0)
        if h not in seen:
            seen.add(h)
            result.append(h)
    return vecs, result


def exhaustive_ui(prime_ranks):
    """Every maximal subgroup and every subset thereof, no formula for ui used."""
    primes = [p for p,_ in prime_ranks]
    assert len(set(primes)) == len(primes)
    f = [hyperplanes(p,d) for p,d in prime_ranks]
    coordinates = [v for v,_ in f]
    universe = set(product(*coordinates))
    maxima=[]
    for i, (_, hs) in enumerate(f):
        for h in hs:
            maxima.append(frozenset(x for x in universe if x[i] in h))
    core = frozenset.intersection(*maxima)
    m=len(maxima)
    noncore_max=-1
    witness=None
    for mask in range(1<<m):
        if mask==0:
            intersection=universe
        else:
            indices=[i for i in range(m) if mask&(1<<i)]
            intersection=set(maxima[indices[0]])
            for i in indices[1:]:
                intersection.intersection_update(maxima[i])
        if intersection != core and mask.bit_count()>noncore_max:
            noncore_max=mask.bit_count()
            witness=[i for i in range(m) if mask&(1<<i)]
    return m,noncore_max+1,len(core),witness


def predicted_ui(prime_ranks):
    M=sum((p**d-1)//(p-1) for p,d in prime_ranks)
    return M - min(p**(d-1) for p,d in prime_ranks) + 1


def test():
    profiles = [((2,1),),((2,2),),((2,3),),((2,4),),
                ((3,1),),((3,2),),((3,3),),((5,1),),((5,2),),
                ((2,2),(3,1)),((2,2),(3,2)),((2,3),(3,1)),
                ((2,3),(3,2)),((2,1),(3,2)),((2,2),(5,1)),
                ((3,1),(5,1))]
    for profile in profiles:
        M,ui,core,witness=exhaustive_ui(profile)
        expected=predicted_ui(profile)
        assert ui==expected, (profile,ui,expected)
        print('PASS', profile, 'maximals',M, 'ui',ui,'Frattini size',core,'bad witness size',len(witness))
    mA,uA,_,_=exhaustive_ui(((2,2),))
    mB,uB,_,_=exhaustive_ui(((3,1),))
    mG,uG,_,_=exhaustive_ui(((2,2),(3,1)))
    assert (mA,uA,mB,uB,mG,uG)==(3,2,1,1,4,4)
    assert uG>uA+uB
    print('COUNTEREXAMPLE_OK: ui(C2^2)=2, ui(C3)=1, ui(C2^2 x C3)=4')

if __name__=='__main__':
    test()

# Independent nonabelian stress test for the general coprime-product clause.
# Enumerate the full subgroup lattice from the multiplication table.
def subgroup_lattice(elements, op, identity):
    elems=tuple(elements)
    def generated(H, a):
        curr=set(H)|{a}
        while True:
            updated=set(curr)
            for x in curr:
                for y in curr:
                    updated.add(op(x,y))
            if updated==curr:
                return frozenset(curr)
            curr=updated
    subs={frozenset({identity})}
    queue=list(subs)
    for H in queue:
        for g in elems:
            if g not in H:
                K=generated(H,g)
                if K not in subs:
                    subs.add(K)
                    queue.append(K)
    return subs


def ui_from_lattice(elements, op, identity):
    allset=frozenset(elements)
    subs=subgroup_lattice(elements,op,identity)
    maxs=[H for H in subs if H != allset and not any(H<K<allset for K in subs)]
    core=set.intersection(*(set(M) for M in maxs))
    m=len(maxs)
    worst=0
    for mask in range(1<<m):
        h=set(allset)
        for j in range(m):
            if mask & (1<<j):
                h.intersection_update(maxs[j])
        if h!=core:
            worst=max(worst,mask.bit_count())
    return m,worst+1,len(subs)


def test_s3_c5():
    from itertools import permutations
    S3=list(permutations(range(3)))
    e=(0,1,2)
    opS=lambda a,b:tuple(a[b[i]] for i in range(3))
    C5=list(range(5))
    opC=lambda a,b:(a+b)%5
    pair=list(product(S3,C5))
    opPair=lambda a,b:(opS(a[0],b[0]),opC(a[1],b[1]))
    mA,tA,sA=ui_from_lattice(S3,opS,e)
    mB,tB,sB=ui_from_lattice(C5,opC,0)
    mG,tG,sG=ui_from_lattice(pair,opPair,(e,0))
    assert (mA,tA,mB,tB,mG,tG)==(4,2,1,1,5,5),(mA,tA,mB,tB,mG,tG)
    assert tG==mA+mB-min(mA-tA,mB-tB)
    print('NONABELIAN_COPRIME_OK', (mA,tA,sA),(mB,tB,sB),(mG,tG,sG))

if __name__=='__main__':
    test_s3_c5()
    print('VERIFY_OK')
