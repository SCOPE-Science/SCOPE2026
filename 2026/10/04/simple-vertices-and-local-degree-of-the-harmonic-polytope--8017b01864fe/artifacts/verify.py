from itertools import permutations
from fractions import Fraction
from math import factorial

def rtl_max_indices(q):
    m=-1; out=[]
    for i in range(len(q)-1,-1,-1):
        if q[i]>m:
            out.append(i); m=q[i]
    return out[::-1]

def harmonic_singleton(q,k):
    n=len(q); pk=q[k]
    return all(not(i>k and q[i]>pk) for i in range(n) if i!=k)

def count_direct_codim1(q,k):
    n=len(q); valid_merge=0
    # pi1 normalized identity. Merge adjacent positions a,a+1. Only membership relation to k can change.
    for a in range(n-1):
        # if pair does not involve k, harmonicity unchanged
        if k not in (a,a+1):
            valid_merge += 1
        else:
            j=a if a+1==k else a+1
            # after merge j is same block as k; harmonicity requires j earlier than k in pi2
            if q[j] < q[k]:
                valid_merge += 1
    # pi2 merges: work with labels ordered by q position
    inv=[None]*n
    for label,pos in enumerate(q): inv[pos-1]=label
    for a in range(n-1):
        pair=(inv[a],inv[a+1])
        if k not in pair:
            valid_merge += 1
        else:
            j=pair[0] if pair[1]==k else pair[1]
            # after merge j same block as k in pi2; requires j earlier than k in pi1
            if j < k:
                valid_merge += 1
    # K expansion: {k,l} harmonic iff k,l are both product maxima.
    M=set(rtl_max_indices(q))
    valid_expand=sum(1 for l in range(n) if l!=k and l in M)
    return valid_merge+valid_expand

def formula_degree(q,k):
    M=rtl_max_indices(q); j=M.index(k); s=len(M)
    em=int(j>0 and k==M[j-1]+1)
    ep=int(j+1<s and q[k]==q[M[j+1]]+1)
    return 2*len(q)+s-3-em-ep, (s,em,ep,j)

def harmonic_number(m):
    return sum(Fraction(1,i) for i in range(1,m+1))

for n in range(2,9):
    simple=0; vertices=0; deg_hist={}
    for q in permutations(range(1,n+1)):
        M=rtl_max_indices(q)
        for k in M:
            assert harmonic_singleton(q,k)
            d1=count_direct_codim1(q,k)
            d2,info=formula_degree(q,k)
            assert d1==d2,(n,q,k,d1,d2,info)
            vertices+=1
            deg_hist[d1]=deg_hist.get(d1,0)+1
            if d1==2*n-2:
                simple+=1
                s,em,ep,j=info
                assert s-1==em+ep
    expect_vertices=factorial(n)*harmonic_number(n)
    expect_simple=3*factorial(n-1)+factorial(n-2)*harmonic_number(n-2)
    assert vertices==expect_vertices,(n,vertices,expect_vertices)
    assert simple==expect_simple,(n,simple,expect_simple)
    print(f'n={n} marked_vertices={vertices} simple_marked={simple} degree_hist={dict(sorted(deg_hist.items()))}')
print('VERIFY_OK harmonic-polytope simple-vertex classification n=2..8')
