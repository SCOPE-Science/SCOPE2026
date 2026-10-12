"""Finite tests for liar's vertex-edge domination in triangular graphs.
Run with Python 3.10+; standard library only. These tests do not replace the infinite proof.
"""
from itertools import combinations
from math import comb, factorial

def graph(n):
    verts=list(combinations(range(n),2))
    ed=[(i,j) for i in range(len(verts)) for j in range(i) if set(verts[i]) & set(verts[j])]
    neigh=[]
    for i,j in ed:
        inc=set(verts[i]) | set(verts[j])
        neigh.append(sum(1<<k for k,v in enumerate(verts) if set(v)&inc))
    return verts,ed,neigh

def original_liar(mask, neighborhoods):
    hits=[mask&b for b in neighborhoods]
    if any(h.bit_count()<2 for h in hits):return False
    # An edge pair can fail only when both intersections are the same two-element set.
    pairs=[h for h in hits if h.bit_count()==2]
    return len(set(pairs))==len(pairs)

def triple_criterion(mask,verts,n):
    for tri in combinations(range(n),3):
        s=set(tri)
        touching=sum(1<<i for i,(a,b) in enumerate(verts) if a in s or b in s)
        if (mask&touching).bit_count()<3:return False
    return True

def optimal_count_formula(n):
    assert n>=8
    k,r=divmod(n,4)
    weights={j:j**(j-2) for j in range(4,8)}
    # Enumerate integer partitions of deficit r as ordered block sizes, divide by their multiplicities.
    ans=0
    def visit(j,left,counts):
        nonlocal ans
        if j==8:
            if left!=0 or sum(counts.values())!=k:return
            denom=1
            for a,c in counts.items():denom*=factorial(c)*factorial(a)**c
            mult=1
            for a,c in counts.items():mult*=weights[a]**c
            ans+=factorial(n)*mult//denom
            return
        for c in range(k+1):
            if (j-4)*c>left:break
            visit(j+1,left-(j-4)*c,{**counts,j:c})
    visit(4,r,{})
    if r==3:
        ans+=factorial(n)*16**k//(factorial(3)*factorial(4)**k*factorial(k))
    return ans

def direct_minimum_counts():
    for n in range(3,9):
        verts,ed,neigh=graph(n);N=len(verts)
        minimum=(3*n+3)//4
        good=0
        for kk in (minimum-1,minimum):
            total=0
            for ids in combinations(range(N),kk):
                mask=sum(1<<i for i in ids)
                quick=triple_criterion(mask,verts,n)
                if n<=6:
                    assert quick==original_liar(mask,neigh),(n,kk,ids)
                if quick:total+=1
            if kk==minimum-1: assert total==0,(n,kk,total)
            else:good=total
        if n==4:assert good==20
        if n==8:assert good==optimal_count_formula(n)==8960
        print('n',n,'min',minimum,'number_of_minimum_sets',good,'directly_checked',n<=6)
    for n in range(8,25):
        k,r=divmod(n,4)
        assert optimal_count_formula(n)>0
        if r==0:
            expected=factorial(n)*16**k//(factorial(4)**k*factorial(k))
            assert optimal_count_formula(n)==expected
    print('verified_counts_formula_through_n_24')
if __name__=='__main__':
    direct_minimum_counts()
    print('ALL_TESTS_PASS')
