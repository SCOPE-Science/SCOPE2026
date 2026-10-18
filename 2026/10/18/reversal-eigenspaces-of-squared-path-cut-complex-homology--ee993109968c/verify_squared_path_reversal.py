#!/usr/bin/env python3
"""Exact combinatorial checks for squared-path cut-complex reversal characters.

All calculations use built-in Python integers and rational-group character
identities. Finite checks support, but do not replace, the general proof.
"""
from itertools import combinations
from math import comb


def choose(n, k):
    return comb(n, k) if n >= 0 and 0 <= k <= n else 0


def beta(n, k):
    r = n-k
    z = sum(choose(k-1, j)*(r-j+1) for j in range(min(k-1, r)+1))
    return choose(n-1, k-1)-z+r


def short_gap_count(j, A):
    if j < 1 or A < j:
        return 0
    return sum(choose(j-1, ell) for ell in range(min(j-1, A-j)+1))


def centered_connected_formula(n, k):
    a = n//2
    if n % 2 == 0 and k % 2:
        return 0
    if n % 2 and k % 2:
        j = (k-1)//2
        return short_gap_count(j,a)+short_gap_count(j,a-1)
    return short_gap_count(k//2,a)


def skeleton_trace(n, r):
    a = n//2
    f = n % 2
    return sum((-1)**i * choose(a,i) * choose(a+f-1,r-i) for i in range(r+1))


def proposed_trace(n, k):
    r = n-k
    c = centered_connected_formula(n,k)
    return (skeleton_trace(n,r) - (1 if (r//2)%2 == 0 else -1)*c
            + ((1 if ((r-1)//2)%2 == 0 else -1) if r%2 else 0))


def disconnected_facets(n, k):
    full = (1<<n)-1
    for sites in combinations(range(n),k):
        if any(sites[j+1]-sites[j] >= 3 for j in range(k-1)):
            mask = sum(1<<p for p in sites)
            yield full ^ mask


def cut_faces(n, k):
    facets = tuple(disconnected_facets(n,k))
    return [mask for mask in range(1<<n)
            if any(mask & ~facet == 0 for facet in facets)]


def face_trace(n, faces):
    # Actual trace of the simplicial automorphism in the *augmented* chain groups.
    trace = 0
    for mask in faces:
        reflected = sum(1<<(n-1-i) for i in range(n) if mask>>i & 1)
        if reflected == mask:
            p = mask.bit_count()
            trace += (-1)**(p-1 + p*(p-1)//2)
    return trace


def count_invariant_connected_brute(n,k):
    return sum(1 for s in combinations(range(n),k)
               if all(s[i+1]-s[i] <= 2 for i in range(k-1))
               and set(n-1-i for i in s)==set(s))


def reduced_betti_mod2(n, faces):
    # Exact GF(2) boundary ranks, using sparse bitset Gaussian elimination.
    by_dim = {}
    for f in faces:
        if f:
            by_dim.setdefault(f.bit_count()-1, []).append(f)
    max_dim=max(by_dim)
    ranks={}
    for d in range(1,max_dim+1):
        sources=by_dim.get(d,[])
        row={face:i for i,face in enumerate(by_dim.get(d-1,[]))}
        pivots={}
        for face in sources:
            v=0
            for i in range(n):
                if face>>i&1:
                    v ^= 1<<row[face ^ (1<<i)]
            while v:
                p=v.bit_length()-1
                if p in pivots:
                    v ^= pivots[p]
                else:
                    pivots[p]=v
                    break
        ranks[d]=len(pivots)
    out={}
    for d in range(max_dim+1):
        x = len(by_dim.get(d,[]))-ranks.get(d,0)-ranks.get(d+1,0)
        if d==0:
            x-=1
        if x:
            out[d]=x
    return out


def main():
    total=0
    count_rank=0
    for n in range(5,14):
        for k in range(2,n-2):
            faces=cut_faces(n,k)
            r=n-k
            observed=(-1)**(r-1)*face_trace(n,faces)
            predicted=proposed_trace(n,k)
            assert observed==predicted,(n,k,observed,predicted)
            assert count_invariant_connected_brute(n,k)==centered_connected_formula(n,k),(n,k)
            b=beta(n,k)
            assert abs(predicted)<=b and (b+predicted)%2==0,(n,k,b,predicted)
            assert all(f.bit_count()<=r for f in faces)
            if n<=10:
                groups=reduced_betti_mod2(n,faces)
                expect={r-1:b} if b else {}
                assert groups==expect,(n,k,groups,expect)
                count_rank+=1
            total+=1
    print('ALL PASS')
    print('Parameter pairs checked by independent face enumeration and signed reversal traces:',total)
    print('Parameter pairs checked by full GF(2) homology:',count_rank)
    for n,k in [(8,4),(9,4),(10,5),(12,6),(13,6)]:
        b=beta(n,k);chi=proposed_trace(n,k)
        print(f'n={n}, k={k}, Betti={b}, reversal_trace={chi}, plus={(b+chi)//2}, minus={(b-chi)//2}')
    print('Finite verification does not certify the infinite family or originality.')

if __name__ == '__main__':
    main()
