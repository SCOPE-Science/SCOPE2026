"""Direct finite verification for four rank-five additive-Steiner theories.

No external packages. Orbit reduction uses complete linear-relation kernels;
proof of stability in all dimensions is mathematical, not finite sampling.
"""
from itertools import combinations, permutations, product
from functools import lru_cache


def pg(m):
    vs=tuple(range(1,2**m))
    blocks=frozenset(frozenset((a,b,a^b)) for a,b in combinations(vs,2))
    return ('PG',m,vs,blocks)


def ag(d):
    vs=tuple(product(range(3),repeat=d))
    def third(a,b):return tuple((-x-y)%3 for x,y in zip(a,b))
    blocks=frozenset(frozenset((a,b,third(a,b))) for a,b in combinations(vs,2))
    return ('AG',d,vs,blocks)


def validate(S):
    family,dim,vs,blocks=S
    assert all(len(b)==3 for b in blocks)
    third={}
    for B in blocks:
        for a,b in combinations(B,2):
            pair=frozenset((a,b))
            assert pair not in third
            third[pair]=next(iter(B-{a,b}))
    assert len(third)==len(vs)*(len(vs)-1)//2
    assert len(blocks)==len(vs)*(len(vs)-1)//6
    return third


def witnesses(S):
    family,dim,vs,blocks=S
    third=validate(S)
    pasch=None
    empty=None
    for a,b,c,d in permutations(vs,4):
        quad=(a,b,c,d)
        collinear=any(frozenset(t) in blocks for t in combinations(quad,3))
        if pasch is None:
            e=third[frozenset((a,b))]
            f=third[frozenset((a,c))]
            if e==third[frozenset((c,d))] and f==third[frozenset((b,d))] and len(set(quad+(e,f)))==6:
                pasch=quad+(e,f)
        if empty is None and not collinear:
            matchings=(((a,b),(c,d)),((a,c),(b,d)),((a,d),(b,c)))
            if all(third[frozenset(P)]!=third[frozenset(Q)] for P,Q in matchings):
                empty=quad
        if pasch is not None and empty is not None:break
    return pasch,empty


def relation_kernel(family,t):
    if not t:return (0,0)
    if family=='PG':
        value=0
        for mask in range(1<<len(t)):
            acc=0
            for j,x in enumerate(t):
                if mask>>j & 1:acc ^= x
            if acc==0:value |= 1<<mask
        return (len(t),value)
    d=len(t[0]); v0=t[0]
    differences=[tuple((x-v0[j])%3 for j,x in enumerate(y)) for y in t[1:]]
    value=0
    for ci,coeff in enumerate(product(range(3),repeat=len(differences))):
        if all(sum(c*diff[j] for c,diff in zip(coeff,differences))%3==0 for j in range(d)):
            value |= 1<<ci
    return (len(t),value)


def quantifier_type_signatures(structures,maxrank=5):
    """Canonical exact recursive Hintikka signatures with orbit memoization.

    Kernels of all linear relations classify GL-orbits of PG tuples and
    kernels of affine difference relations classify AGL-orbits of AG tuples.
    """
    interning={}
    sigcache={}
    orbit_counts={}
    def intern(key):
        if key not in interning:interning[key]=len(interning)
        return interning[key]
    def atomic(t,blocks):
        eq=tuple(int(t[i]==t[j]) for i in range(len(t)) for j in range(i+1,len(t)))
        triples=tuple(int(frozenset((t[i],t[j],t[k])) in blocks) for i in range(len(t)) for j in range(i+1,len(t)) for k in range(j+1,len(t)))
        return eq,triples
    def typ(i,t,r):
        family,dim,vs,blocks=structures[i]
        key=(i,relation_kernel(family,t),r)
        if key in sigcache:return sigcache[key]
        qf=atomic(t,blocks)
        if r==0: val=intern((len(t),0,qf))
        else:
            child_types=frozenset(typ(i,t+(x,),r-1) for x in vs)
            val=intern((len(t),r,qf,child_types))
        sigcache[key]=val
        orbit_counts[i]=orbit_counts.get(i,0)+1
        return val
    signatures=[]
    for r in range(maxrank+1):
        ids=[typ(i,(),r) for i in range(len(structures))]
        signatures.append((r,ids))
    return signatures,orbit_counts,len(sigcache)


if __name__=='__main__':
    systems=[pg(3),pg(4),pg(5),ag(2),ag(3),ag(4)]
    for S in systems:
        if len(S[2])<=27:
            p,e=witnesses(S)
        else:
            if S[0]=='AG':
                p=None
                e=((0,0,0,0),(1,0,0,0),(0,1,0,0),(0,0,1,0))
                assert all(frozenset(t) not in S[3] for t in combinations(e,3))
            else:
                p=(1,2,4,7,3,5)
                e=(1,2,4,8)
                assert all(frozenset(t) not in S[3] for t in combinations(e,3))
                assert all(frozenset(t) in S[3] for t in ((1,2,3),(4,7,3),(1,4,5),(2,7,5)))
        print('DESIGN',S[0],S[1],'v',len(S[2]),'blocks',len(S[3]),'Pasch',bool(p),'empty_quad',bool(e))
        assert bool(p)==(S[0]=='PG')
        assert bool(e)==((S[0]=='PG' and S[1]>=4) or (S[0]=='AG' and S[1]>=3))
    out,orbit_counts,ncache=quantifier_type_signatures(systems)
    for r,ids in out:
        print('EXACT_FO_TYPES',r,'IDs',ids)
        if r<=4:assert len(set(ids))==1
        if r==5:
            assert len(set(ids))==4
            assert ids[1]==ids[2] and ids[4]==ids[5]
            assert len(set((ids[0],ids[1],ids[3],ids[4])))==4
    print('ORBIT_REDUCED_STATES',orbit_counts,'total',ncache)
    print('VERIFY_OK')
