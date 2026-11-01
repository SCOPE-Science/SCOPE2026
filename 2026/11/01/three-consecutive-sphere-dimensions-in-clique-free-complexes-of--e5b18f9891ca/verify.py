#!/usr/bin/env python3
"""Finite checks for clique-path clique-free complexes (purely mathematical)."""
from collections import defaultdict
from itertools import product
from math import comb


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def betti_formula(p, q, r, t):
    a = lambda j: choose(p - 1, j)
    b = lambda j: choose(q - 1, j)
    c = lambda j: choose(r - 1, j)
    return {
        3*t-4: a(t-1)*b(t-1)*c(t-1),
        3*t-5: a(t-2)*b(t-2)*c(t-1) + a(t-1)*b(t-2)*c(t-2),
        3*t-6: a(t-2)*b(t-3)*c(t-2),
    }


def data(p, q, r, t):
    n = p + q + r + 2
    x, y = n-2, n-1
    blocks = (
        sum(1 << i for i in range(p)) | (1 << x),
        sum(1 << i for i in range(p, p+q)) | (1 << x) | (1 << y),
        sum(1 << i for i in range(p+q, p+q+r)) | (1 << y),
    )
    faces = [[] for _ in range(n+1)]
    for mask in range(1 << n):
        if all((mask & block).bit_count() <= t-1 for block in blocks):
            faces[mask.bit_count()].append(mask)
    return faces


def rank_gf2(columns):
    pivots = {}
    for val in columns:
        while val:
            pivot = val.bit_length()-1
            if pivot not in pivots:
                pivots[pivot] = val
                break
            val ^= pivots[pivot]
    return len(pivots)


def homology_gf2(faces, n):
    b_rank = {}
    for cardinality in range(1, n+1):
        if not faces[cardinality]:
            continue
        rows = {m: i for i,m in enumerate(faces[cardinality-1])}
        cols = []
        for m in faces[cardinality]:
            c = 0
            for i in range(n):
                if m & (1 << i):
                    c ^= 1 << rows[m ^ (1 << i)]
            cols.append(c)
        b_rank[cardinality] = rank_gf2(cols)
    out = {}
    for degree in range(-1, n):
        beta = len(faces[degree+1]) - b_rank.get(degree+1,0) - b_rank.get(degree+2,0)
        if beta:
            out[degree] = beta
    return out


def cycle_representatives(n):
    # One representative of every integer partition / conjugacy class of S_n.
    def partitions(left, cap):
        if left == 0:
            yield []
        else:
            for k in range(min(cap,left), 0, -1):
                for tail in partitions(left-k, k):
                    yield [k]+tail
    for lengths in partitions(n,n):
        perm = list(range(n))
        offset = 0
        for length in lengths:
            for j in range(length):
                perm[offset+j] = offset+(j+1)%length
            offset += length
        yield lengths, perm


def trace_exterior_augmentation(lengths, k):
    # det(1+z sigma | U_n) = (prod_{ell}(1-(-z)^ell))/(1+z).
    n = sum(lengths)
    polynomial = [1] + [0]*n
    for length in lengths:
        for j in range(n-length,-1,-1):
            polynomial[j+length] -= (-1)**length * polynomial[j]
    coefficients = [0]*n
    for j in range(n):
        coefficients[j] = polynomial[j] - (coefficients[j-1] if j else 0)
    return coefficients[k] if 0 <= k < n else 0


def predicted_lefschetz(types, t):
    a,b,c=types
    e=lambda lengths,j:trace_exterior_augmentation(lengths,j)
    d=3*t-4
    top=e(a,t-1)*e(b,t-1)*e(c,t-1)
    middle=(e(a,t-2)*e(b,t-2)*e(c,t-1)
            +e(a,t-1)*e(b,t-2)*e(c,t-2))
    bottom=e(a,t-2)*e(b,t-3)*e(c,t-2)
    return (-1)**d * (top-middle+bottom)


def observed_lefschetz(faces, permutation):
    total=-1 # empty face, reduced augmentation degree -1
    n=len(permutation)
    for size in range(1,len(faces)):
        sign_dim=(-1)**(size-1)
        for mask in faces[size]:
            image=0
            points=[]
            for i in range(n):
                if mask & (1<<i):
                    image|=1<<permutation[i]
                    points.append(permutation[i])
            if image != mask:
                continue
            inversions=sum(points[i]>points[j] for i in range(len(points)) for j in range(i+1,len(points)))
            total+=sign_dim*(-1)**inversions
    return total


def main():
    tests=[(3,2,2,2),(3,3,2,3),(3,2,3,2),(3,3,3,3),
           (3,4,3,2),(3,4,4,4),(4,4,4,4),(4,4,5,4)]
    for t,p,q,r in tests:
        faces=data(p,q,r,t)
        computed=homology_gf2(faces,p+q+r+2)
        target={j:v for j,v in betti_formula(p,q,r,t).items() if v}
        assert computed==target,(t,p,q,r,computed,target)
        print('HOMOLOGY OK',t,p,q,r,sorted(computed.items()),'faces',sum(map(len,faces)))
    for t,p,q,r in [(3,3,3,3),(3,4,3,2),(4,4,4,4)]:
        faces=data(p,q,r,t)
        count=0
        for (ca,pa),(cb,pb),(cc,pc) in product(cycle_representatives(p),cycle_representatives(q),cycle_representatives(r)):
            perm=pa+[p+i for i in pb]+[p+q+i for i in pc]+[p+q+r,p+q+r+1]
            observed=observed_lefschetz(faces,perm)
            target=predicted_lefschetz((ca,cb,cc),t)
            assert observed==target,(t,p,q,r,ca,cb,cc,observed,target)
            count+=1
        print('SYMMETRY OK',t,p,q,r,count,'conjugacy classes')

if __name__=='__main__':
    main()
