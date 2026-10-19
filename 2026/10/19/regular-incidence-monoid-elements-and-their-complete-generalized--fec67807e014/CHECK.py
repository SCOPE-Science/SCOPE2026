#!/usr/bin/env python3
"""Exhaustive incidence-monoid generalized-inverse checks; standard-library only."""
from itertools import product
from collections import Counter


def field(q):
    if q in (2, 3, 5):
        return lambda a,b:(a+b)%q, lambda a,b:(a*b)%q
    if q == 4:  # F2[t]/(t^2+t+1): 2 denotes t.
        def mul(a,b):
            v=0
            if b&1: v^=a
            if b&2: v^=a<<1
            if v&8: v^=0b1100
            if v&4: v^=0b0111
            return v
        return lambda a,b:a^b,mul
    raise ValueError(q)


def closure(n, covers):
    E=set((i,i) for i in range(n))|set(covers)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if (i,k) in E and (k,j) in E:E.add((i,j))
    assert all(i<=j for i,j in E), 'Input numbering must be a linear extension'
    return sorted(E)


def formula(n,E,q,T):
    T=set(T);Z=set(range(n))-T
    m=sum(i!=j for i,j in E)
    mT=sum(i!=j and i in T and j in T for i,j in E)
    mZ=sum(i!=j and i in Z and j in Z for i,j in E)
    cross=m-mT-mZ
    return ((q-1)**len(T)*q**(m-mZ),
            q**(n+m-len(T)-mT),q**cross,
            q**cross*(q-1)**len(Z)*q**mZ)


def check(n,covers,q):
    E=closure(n,covers);pos={ij:k for k,ij in enumerate(E)}
    add,mul=field(q)
    terms=[[(pos[(i,k)],pos[(k,j)]) for k in range(n) if (i,k) in pos and (k,j) in pos]
           for i,j in E]
    elems=list(product(range(q), repeat=len(E)))
    def mult(a,b):
        ans=[]
        for pairs in terms:
            w=0
            for x,y in pairs:w=add(w,mul(a[x],b[y]))
            ans.append(w)
        return tuple(ans)
    predicted_total=0; observed_total=0; observed_reflexive_pairs=0;observed_inner_pairs=0;observed_unit_inner_pairs=0
    for a in elems:
        T=tuple(i for i in range(n) if a[pos[i,i]]!=0)
        support_count,inner,reflexive,unit_inner=formula(n,E,q,T)
        nin=nr=nui=ng=0
        for b in elems:
            ab=mult(a,b)
            if mult(ab,a)==a:
                nin+=1
                if all(b[pos[i,i]]!=0 for i in range(n)):nui+=1
                if mult(b,ab)==b:
                    nr+=1
                    if ab==mult(b,a):ng+=1
        if nin:
            assert (nin,nr,nui,ng)==(inner,reflexive,unit_inner,1),(n,covers,q,a,T,nin,nr,nui,ng,inner,reflexive,unit_inner)
            observed_total+=1
            observed_inner_pairs+=nin;observed_reflexive_pairs+=nr;observed_unit_inner_pairs+=nui
        else:
            assert nr==0 and nui==0 and ng==0
    predicted_total=sum(formula(n,E,q,T)[0] for k in range(n+1) for T in __import__('itertools').combinations(range(n),k))
    assert observed_total==predicted_total,(n,covers,q,observed_total,predicted_total)
    print('OK',n,'covers',covers,'q',q,'size',len(elems),'regular',observed_total,'inner_pairs',observed_inner_pairs,'reflexive_pairs',observed_reflexive_pairs,'unit_inner_pairs',observed_unit_inner_pairs)
    return observed_total,observed_reflexive_pairs


def main():
    s=check(4,[(0,1),(0,2),(0,3)],2)
    p=check(4,[(0,2),(1,2),(1,3)],2)
    assert s==(91,341) and p==(89,337)
    check(3,[(0,1),(1,2)],2)
    check(3,[(0,1),(1,2)],3)
    check(3,[(0,1),(0,2)],2)
    check(2,[(0,1)],4)
    check(2,[],5)
    print('ALL_INCIDENCE_INVERSE_SPECTRA_PASSED')
if __name__=='__main__':main()
