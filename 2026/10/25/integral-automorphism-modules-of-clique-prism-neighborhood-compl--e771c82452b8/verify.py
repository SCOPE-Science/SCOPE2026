#!/usr/bin/env python3
"""Exact finite checks for the integral symmetry theorem on clique-prism neighborhood complexes.

No external dependencies. Run: python3 verify.py
"""
from itertools import permutations, combinations
from math import comb


def sign_perm(seq):
    return -1 if sum(seq[i] > seq[j] for i in range(len(seq)) for j in range(i+1,len(seq))) % 2 else 1


def faces(n):
    # Indices 0..n-1 denote first layer, n..2n-1 denote second.
    facets = []
    for i in range(n):
        facets.append(tuple(sorted([j for j in range(n) if j != i] + [n+i])))
        facets.append(tuple(sorted([n+j for j in range(n) if j != i] + [i])))
    F=set()
    for facet in facets:
        for k in range(1,len(facet)+1):
            F.update(combinations(facet,k))
    return facets, tuple(sorted(F, key=lambda t:(len(t),t)))


def check_cover(n,facets,F):
    X=set();Y=set()
    for idx,fac in enumerate(facets):
        T= X if idx%2==0 else Y
        for k in range(1,len(fac)+1):T.update(combinations(fac,k))
    assert X|Y==set(F)
    inter=X&Y
    cross={(i,n+j) for i in range(n) for j in range(n) if i!=j}
    assert {s for s in inter if len(s)==2}==cross
    assert len(inter)==2*n+n*(n-1)
    assert len(X & Y & set(combinations(range(n),2)))==0
    assert len(X & Y & set(combinations(range(n,2*n),2)))==0


def gf2_rank(cols):
    piv={}
    for v in cols:
        while v:
            p=v.bit_length()-1
            if p not in piv:
                piv[p]=v;break
            v^=piv[p]
    return len(piv)


def bettis(n,F):
    bydim={}
    for f in F:bydim.setdefault(len(f)-1,[]).append(f)
    dimmax=max(bydim)
    ranks={}
    for k in range(1,dimmax+1):
        prev={face:i for i,face in enumerate(bydim[k-1])}
        cols=[]
        for simplex in bydim[k]:
            v=0
            for i in range(k+1):v^=1 << prev[simplex[:i]+simplex[i+1:]]
            cols.append(v)
        ranks[k]=gf2_rank(cols)
    answer={}
    for k in range(dimmax+1):
        b=len(bydim[k])-ranks.get(k,0)-ranks.get(k+1,0)
        if k==0:b-=1
        if b:answer[k]=b
    return answer


def check_char(n,F,perm,swap):
    def image(v):
        if v<n: return (n if swap else 0)+perm[v]
        return (0 if swap else n)+perm[v-n]
    tr={}
    for simplex in F:
        images=tuple(image(v) for v in simplex)
        if set(images)!=set(simplex):continue
        sign=sign_perm(images)
        k=len(simplex)-1
        tr[k]=tr.get(k,0)+sign
    lefs=sum((-1)**k * s for k,s in tr.items())-1
    f=sum(i==perm[i] for i in range(n))
    two=sum(i<perm[i] and perm[perm[i]]==i for i in range(n))
    sign=sign_perm(perm)
    low=(2*two-1 if swap else f*f-3*f+1)
    high=(0 if swap else 2*sign)
    expected=low+(-1)**(n-2)*high
    assert lefs==expected,(n,perm,swap,lefs,expected)
    return True


def main():
    total=0
    for n in (5,6,7):
        facets,F=faces(n)
        check_cover(n,facets,F)
        if n<=6:
            B=bettis(n,F)
            expected={2:n*n-3*n+1,n-2:2}
            assert B==expected,(n,B,expected)
        testperms=permutations(range(n)) if n<=6 else (
            tuple(range(n)),(1,0,*range(2,n)),tuple((i+1)%n for i in range(n)),
            (1,2,0,*range(3,n)),tuple(reversed(range(n)))
        )
        tests=0
        for p in testperms:
            for flip in (False,True):
                check_char(n,F,p,flip);tests+=1
        print(f'n={n}: {len(F)} nonempty faces, {tests} exact augmented Lefschetz tests; cover/intersection checks OK')
        total+=tests
    print(f'VERIFY_OK: {total} signed fixed-face Lefschetz calculations; integral module proof is not replaced by finite checks')

if __name__=='__main__':main()
