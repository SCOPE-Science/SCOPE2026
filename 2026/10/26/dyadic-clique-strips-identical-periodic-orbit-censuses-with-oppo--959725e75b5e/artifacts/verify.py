#!/usr/bin/env python3
"""Direct exact finite-field checks for dyadic open clique strips.

No third-party modules required. The proof does not depend on these tests.
"""
from collections import Counter


def adjacency_masks(n, q):
    # Vertices (path coordinate, clique coordinate), indexed by i*q+a.
    masks=[]
    for i in range(n):
        for a in range(q):
            neigh=0
            for b in range(q):
                if b!=a:
                    neigh ^= 1 << (i*q+b)
            if i>0: neigh ^= 1 << ((i-1)*q+a)
            if i+1<n: neigh ^= 1 << ((i+1)*q+a)
            masks.append(neigh)
    return masks


def apply(rows, x):
    out=0
    for i, mask in enumerate(rows):
        if (mask & x).bit_count() & 1:
            out |= 1<<i
    return out


def multiply(left, right):
    # Matrix row representation; compute left @ right over F2.
    out=[]
    for r in left:
        total=0
        while r:
            bit=r & -r
            total ^= right[bit.bit_length()-1]
            r^=bit
        out.append(total)
    return out


def rank(rows):
    piv={}
    for row in rows:
        while row:
            i=row.bit_length()-1
            if i in piv: row ^= piv[i]
            else:
                piv[i]=row
                break
    return len(piv)


def expected_fix_dimension(n, q, j):
    t=1<<j
    if q&1:
        return (q-1)*min(t,n)
    return (q-2)*min(t,n)+min(t,n-1)+min(t,n+1)


def exact_rank_checks(s, q):
    n=(1<<s)-1
    dim=n*q
    A=adjacency_masks(n,q)
    I=[1<<k for k in range(dim)]
    powers=[I]
    for t in range(1,n+2):
        powers.append(multiply(A,powers[-1]))
    if q&1:
        for t,p in enumerate(powers):
            expected=(q-1)*n+max(0,n-t)
            assert rank(p)==expected,(n,q,t,rank(p),expected)
        assert powers[n+1]==powers[n] or rank(powers[n+1])==(q-1)*n
    else:
        for t,p in enumerate(powers):
            assert rank(p)==dim,(n,q,t)
    for j in range(s+1):
        t=1<<j
        P=I
        for _ in range(t):
            P=multiply(A,P)
        diff=[P[k]^I[k] for k in range(dim)]
        obs=dim-rank(diff)
        want=expected_fix_dimension(n,q,j)
        assert obs==want,(n,q,j,obs,want)
    return dim,len(powers),s+1


def enumerate_configs(s,q):
    n=(1<<s)-1
    N=n*q
    rows=adjacency_masks(n,q)
    expected_transient=Counter()
    observed_transient=Counter()
    observed_periodic=Counter()
    for start in range(1<<N):
        seen={}
        x=start
        t=0
        while x not in seen:
            seen[x]=t
            x=apply(rows,x)
            t+=1
        depth=seen[x]
        period=t-depth
        assert (period&(period-1))==0,(n,q,start,period)
        observed_transient[depth]+=1
        if depth==0: observed_periodic[period]+=1
    if q&1:
        for t in range(n+1):
            want=(1<<((q-1)*n))*(1 if t==0 else (1<<(t-1)))
            expected_transient[t]=want
    else:
        expected_transient[0]=(1<<N)
    assert observed_transient==expected_transient,(n,q,observed_transient,expected_transient)
    for j in range(s+1):
        t=1<<j
        a=1<<expected_fix_dimension(n,q,j)
        b=0 if j==0 else 1<<expected_fix_dimension(n,q,j-1)
        assert observed_periodic[t]==a-b,(n,q,t,observed_periodic[t],a-b)
    assert sum(observed_periodic.values())==(1<<(N if q%2==0 else (q-1)*n))
    return 1<<N, dict(observed_transient),dict(observed_periodic)


def reversible_neighbour(n,q):
    rows=adjacency_masks(n,q)
    return rank(rows)==n*q


def main():
    matrix_cases=0; rank_ids=0; brute=0
    for s in (2,3,4):
        for q in (2,3,4,5,6):
            if s==4 and q>4: continue
            N,_,z=exact_rank_checks(s,q)
            matrix_cases+=1
            rank_ids+=z
            print('RANK',s,q,N,'PASS')
    for s,q in ((2,2),(2,3),(2,4),(3,2)):
        samples,counts,cycles=enumerate_configs(s,q)
        brute+=samples
        print('EXHAUSTIVE',s,q,samples,sorted(counts.items()),sorted(cycles.items()),'PASS')
    for n in (4,16):
        for q in (2,3,4,5):
            assert reversible_neighbour(n,q),(n,q)
            print('NEIGHBOUR_REVERSIBLE',n,q,'PASS')
    print('DYADIC_CLIQUE_STRIP_VERIFY_OK',
          'matrix_cases='+str(matrix_cases),
          'rank_profiles='+str(rank_ids),
          'full_states='+str(brute))


if __name__=='__main__':main()
