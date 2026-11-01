#!/usr/bin/env python3
"""Independent finite checks for dihedral non-generating Frattini-core nerve.

Usage: python verify.py
Standard-library only; no external data or service required.
"""
from math import gcd, prod


def primes(n):
    return tuple(p for p in range(2, n + 1) if n % p == 0 and all(p % d for d in range(2, int(p**.5)+1)))


def maximal_subgroups(n):
    # Elements (u, epsilon) denote r^u s^epsilon in D_{2n}.
    P=primes(n)
    V=[('R',0)]+[(p,i) for p in P for i in range(p)]
    S={('R',0):frozenset((u,0) for u in range(n))}
    for p in P:
        for i in range(p):
            S[(p,i)]=frozenset([(u,0) for u in range(0,n,p)] + [(u,1) for u in range(i,n,p)])
    return P,V,S


def predicted(mask, V, P):
    if mask==0:return True
    chosen=[V[j] for j in range(len(V)) if mask>>j&1]
    blocks={p:[i for q,i in chosen if q==p] for p in P}
    if any(not x for x in blocks.values()):return True
    return ('R',0) not in chosen and all(len(x)==1 for x in blocks.values())



def mul(x,y,n):
    return ((x[0]+((-1)**x[1])*y[0])%n,(x[1]+y[1])%2)


def subgroup_generated_by(gens,n):
    S={(0,0)} | set(gens)
    while True:
        T=S|{mul(x,y,n) for x in S for y in S}
        if len(T)==len(S): return frozenset(S)
        S=T


def independently_maximal(n):
    universe=frozenset((i,e) for i in range(n) for e in (0,1))
    found={frozenset([(0,0)])}
    q=list(found)
    for H in q:
        for g in universe-H:
            K=subgroup_generated_by(H|{g},n)
            if K not in found:
                found.add(K);q.append(K)
    proper=[H for H in found if H!=universe]
    result=frozenset(H for H in proper if not any(H<Q for Q in proper))
    return result


def verify(n):
    P,V,S=maximal_subgroups(n)
    m=prod(P)
    phi=frozenset((u,0) for u in range(0,n,m))
    real_phi=frozenset.intersection(*list(S.values()))
    assert phi==real_phi,(n,'Frattini',phi,real_phi)
    universe=frozenset((u,e) for u in range(n) for e in (0,1))
    assert all(len(S[v])<len(universe) for v in V)
    if n<=12:
        actual_max=independently_maximal(n)
        assert actual_max==frozenset(S.values()),(n,'maximal subgroup classification')
    K_count=[0]*(len(V)+1)
    transversals=[]
    basefaces=0
    for mask in range(1<<len(V)):
        chosen=[V[i] for i in range(len(V)) if mask>>i&1]
        intersection=universe
        for v in chosen:intersection=intersection.intersection(S[v])
        actual=bool(intersection-phi) if chosen else True
        expected=predicted(mask,V,P)
        assert actual==expected,(n,chosen,'actual',actual,'expected',expected)
        if actual:
            K_count[len(chosen)]+=1
            if ('R',0) not in chosen and len(chosen)==len(P) and len({p for p,i in chosen})==len(P):
                transversals.append(tuple(sorted(chosen)))
            if ('R',0) not in chosen and any(not any(v[0]==p for v in chosen) for p in P):basefaces+=1
    assert len(transversals)==m,(n,m,len(transversals))
    # The remainder of K is the cone from the rotation maximal subgroup
    # on faces avoiding at least one prime block.
    assert sum(K_count)==2*basefaces + m,(n,K_count,basefaces,m)
    # Tally relative-cell Euler characteristic: m top-dimensional cells.
    chi_reduced=sum((-1)**(i-1)*x for i,x in enumerate(K_count))
    assert chi_reduced==(-1)**(len(P)-1)*m,(n,chi_reduced)
    units=[a for a in range(n) if gcd(a,n)==1]
    for a in units:
        for b in range(n):
            def act(u,e):return ((a*u+b*e)%n,e)
            for v in V:
                if v[0]=='R': vimage=v
                else:vimage=(v[0],(a*v[1]+b)%v[0])
                assert frozenset(act(u,e) for u,e in S[v]) == S[vimage]
            # Its action on relative top cells is j -> a*j+b (mod m).
            hits=sum((a*j+b-j)%m==0 for j in range(m))
            d=gcd(a-1,m)
            expected=d if b%d==0 else 0
            assert hits==expected
    print('CHECK_OK n=%s squarefree_radical=%s distinct_primes=%s nerve_faces=%s top_rank=%s aff_maps=%s' %
          (n,m,len(P),sum(K_count),m,len(units)*n))

if __name__=='__main__':
    for n in (3,4,5,6,8,9,10,12,15,18,21,30,36,42,60):verify(n)
    print('ALL_VERIFY_OK direct_subgroup_intersections_nerve_affine_action_and_euler')
