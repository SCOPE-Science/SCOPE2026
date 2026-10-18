"""Exact finite consistency checks for the one-parallel-pair matroid toric charts.

The all-parameter proof uses semigroup arguments, separately recorded in RESULT.md.
"""
from itertools import combinations
from math import comb
from fractions import Fraction


def rank(rows):
    if not rows:return 0
    a=[[Fraction(x) for x in row] for row in rows]
    piv=0
    for col in range(len(a[0])):
        q=next((i for i in range(piv,len(a)) if a[i][col]),None)
        if q is None:continue
        a[piv],a[q]=a[q],a[piv]
        x=a[piv][col]
        a[piv]=[y/x for y in a[piv]]
        for i in range(len(a)):
            if i==piv:continue
            x=a[i][col]
            if x:a[i]=[y-x*z for y,z in zip(a[i],a[piv])]
        piv+=1
        if piv==len(a):break
    return piv


def vec(n,S):return tuple(int(i in S) for i in range(n))
def diff(u,v):return tuple(a-b for a,b in zip(u,v))
def add(u,v):return tuple(a+b for a,b in zip(u,v))


def test(n):
    E=set(range(n)); pair={0,1}
    bases=[frozenset(S) for S in combinations(range(n),2) if set(S)!=pair]
    assert len(bases)==comb(n,2)-1
    zero=(0,)*n
    special=isolated=0
    for B in bases:
        base=vec(n,B)
        # Each monomial in the vertex chart is a product of edge swaps.
        neighbors=[diff(vec(n,C),base) for C in bases if len(B-C)==1]
        assert len(set(neighbors))==len(neighbors)
        expected=(2*(n-3)+1) if B&pair else 2*(n-2)
        assert len(neighbors)==expected
        assert rank([x[:-1] for x in neighbors])==n-1
        low={zero,*neighbors}
        two={add(u,v) for u in low for v in low}
        assert all(diff(vec(n,C),base) in two for C in bases)
        if B&pair:
            special+=1
            # The unused parallel element belongs to precisely one edge
            # direction not appearing in any 2-by-(n-3) matrix generator.
            j=next(iter(B-pair))
            other=next(iter(pair-B))
            solo=diff(vec(n,{other,j}),base)
            mat=[x for x in neighbors if x!=solo]
            assert len(mat)==2*(n-3)
            # The two groups of edge moves satisfy all rank-one minors.
            other_free=sorted(E-(pair|{j}))
            s=next(iter(B&pair))
            aa=[diff(vec(n,{j,t}),base) for t in other_free]
            bb=[diff(vec(n,{s,t}),base) for t in other_free]
            assert set(mat)==set(aa+bb)
            for i in range(len(aa)):
                for h in range(i+1,len(aa)):
                    assert add(aa[i],bb[h])==add(aa[h],bb[i])
        else:
            isolated+=1
            B0=sorted(B)
            L=sorted(E-B)
            aa=[diff(vec(n,{B0[0],t}),base) for t in L]
            bb=[diff(vec(n,{B0[1],t}),base) for t in L]
            assert set(neighbors)==set(aa+bb)
            for i in range(len(L)):
                for h in range(i+1,len(L)):
                    assert add(aa[i],bb[h])==add(aa[h],bb[i])
    assert special==2*(n-2)
    assert isolated==comb(n-2,2)
    # The facet containing each special edge is supported by a
    # functional that maximizes at exactly its two endpoints.
    for j in range(2,n):
        weights=[1,1]+[0]*(n-2)
        weights[j]=10
        mx=max(sum(weights[i] for i in B) for B in bases)
        f={B for B in bases if sum(weights[i] for i in B)==mx}
        assert f=={frozenset({0,j}),frozenset({1,j})}
    return special,isolated,n-2,comb(n-2,2)

if __name__=='__main__':
    for n in range(4,10):
        print('n=%d (special_fixed,other_fixed,curve_components,isolated_components)=%s'% (n,test(n)))
    print('VERIFY_OK')
