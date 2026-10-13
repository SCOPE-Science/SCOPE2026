#!/usr/bin/env python3
"""Independent finite checks for morphisms of globally quantified Heyting-chain powers."""
from itertools import product
from math import comb, factorial
from collections import Counter

def implication(a,b,top):
    return top if a<=b else b

def chain_homs(k,l):
    ans=[]
    for values in product(range(l),repeat=k-2):
        f=(0,)+values+(l-1,)
        if all(f[min(i,j)]==min(f[i],f[j]) and f[max(i,j)]==max(f[i],f[j])
               and f[implication(i,j,k-1)]==implication(f[i],f[j],l-1)
               for i in range(k) for j in range(k)):
            ans.append(f)
    return ans

def surjs(n,m):
    return [p for p in product(range(m),repeat=n) if len(set(p))==m]

def source_operations(k,m):
    vecs=list(product(range(k),repeat=m))
    ind={x:i for i,x in enumerate(vecs)}
    return vecs,ind

def coordinate_homs(k,m,l):
    vecs,ind=source_operations(k,m)
    N=len(vecs)
    # Fixed named bottom and top. Independently test preservation of all binary operations.
    zero=ind[(0,)*m]; one=ind[(k-1,)*m]
    candidates=[]
    others=[i for i in range(N) if i!=zero and i!=one]
    for middle in product(range(l),repeat=len(others)):
        f=[None]*N; f[zero]=0; f[one]=l-1
        for i,y in zip(others,middle):f[i]=y
        valid=True
        for i,x in enumerate(vecs):
            if not valid:break
            for j,y in enumerate(vecs):
                mt=ind[tuple(min(a,b) for a,b in zip(x,y))]
                jt=ind[tuple(max(a,b) for a,b in zip(x,y))]
                it=ind[tuple(implication(a,b,k-1) for a,b in zip(x,y))]
                if f[mt]!=min(f[i],f[j]) or f[jt]!=max(f[i],f[j]) or f[it]!=implication(f[i],f[j],l-1):
                    valid=False;break
        if valid:candidates.append(tuple(f))
    return vecs,ind,candidates

def test():
    chain_cases=0; pair_cases=0; vector_morphs=0; composition_cases=0
    for k in range(2,7):
        for l in range(2,7):
            hh=chain_homs(k,l)
            expected=sum(comb(l-2,t) for t in range(min(k-2,l-2)+1))
            assert len(hh)==expected,(k,l,len(hh),expected)
            chain_cases+=1
    for k in range(2,6):
        hh=chain_homs(k,k)
        idem=[f for f in hh if tuple(f[y] for y in f)==f]
        assert len(idem)==k-1,(k,idem)
    for k,m,l,nn in [(2,2,2,1),(2,2,2,2),(2,2,2,3),(2,3,2,2),
                      (2,3,2,3),(3,2,3,1),(3,2,3,2),(3,2,3,3),
                      (3,1,3,1),(3,1,3,2),(2,2,3,3)]:
        vecs,idx,candidates=coordinate_homs(k,m,l)
        canonical=set()
        for i in range(m):
            for phi in chain_homs(k,l):
                canonical.add(tuple(phi[x[i]] for x in vecs))
        assert set(candidates)==canonical,(k,m,l,'coordinate homs',len(candidates),len(canonical))
        pair_cases+=1
        actual=[]
        for fs in product(candidates,repeat=nn):
            good=True
            for ix,x in enumerate(vecs):
                source_min=idx[(min(x),)*m]
                source_max=idx[(max(x),)*m]
                ys=tuple(f[ix] for f in fs)
                if any(f[source_min]!=min(ys) or f[source_max]!=max(ys) for f in fs):
                    good=False;break
            if good:actual.append(fs)
        wanted=len(surjs(nn,m))*len(chain_homs(k,l))
        assert len(actual)==wanted,(k,m,l,nn,len(actual),wanted)
        sizes=Counter()
        inj=0; onto=0
        for fs in actual:
            outputs={tuple(f[ix] for f in fs) for ix in range(len(vecs))}
            sizes[len(outputs)]+=1
            inj+=len(outputs)==len(vecs)
            onto+=len(outputs)==l**nn
        predicted=Counter()
        for t in range(min(k-2,l-2)+1):
            predicted[(t+2)**m]+=len(surjs(nn,m))*comb(l-2,t)
        assert sizes==predicted,(k,m,l,nn,sizes,predicted)
        assert inj==len(surjs(nn,m))*(comb(l-2,k-2) if l>=k else 0)
        assert onto==(factorial(m) if m==nn and k>=l else 0)
        vector_morphs+=len(actual)
    for k in range(2,6):
        for n in range(1,5):
            perms=surjs(n,n)[:2]
            for phi in chain_homs(k,k):
                for psi in chain_homs(k,k):
                    for sig in perms:
                        for tau in perms:
                            for x in product(range(k),repeat=n):
                                mid=tuple(phi[x[sig[j]]] for j in range(n))
                                out=tuple(psi[mid[tau[j]]] for j in range(n))
                                pred=tuple(psi[phi[x[sig[tau[j]]]]] for j in range(n))
                                assert out==pred
                                composition_cases+=1
    print('VERIFY_OK chain_parameter_pairs',chain_cases,'coordinate_hom_cases',pair_cases,'enumerated_full_homomorphisms',vector_morphs,'composition_checks',composition_cases)

if __name__=='__main__':test()
