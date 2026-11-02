#!/usr/bin/env python3
"""Direct finite-field enumeration of associative pairing ranks on monomial axis algebras.

Run: python verify_multibranch_forms.py
Only Python's standard library is required.
"""
import itertools
from collections import Counter


def field(q):
    if q in (2, 3, 5):
        return (lambda a, b: (a+b) % q), (lambda a, b: (a*b) % q), (lambda a: (-a) % q)
    if q == 4:
        def mul(a, b):
            x = 0
            for i in range(2):
                if (b >> i) & 1:
                    x ^= a << i
            if x & 8:
                x ^= 0b1110  # reduce t^3 using t^2+t+1=0
            if x & 4:
                x ^= 0b111  # reduce t^2 using t+1
            return x
        return lambda a,b: a^b, mul, lambda a:a
    raise ValueError(q)


def matrix_rank(M, q):
    add, mul, neg = field(q)
    A = [list(row) for row in M]
    inv = {a: next(b for b in range(1,q) if mul(a,b)==1) for a in range(1,q)}
    rank = 0
    for col in range(len(A[0])):
        pivot = next((j for j in range(rank,len(A)) if A[j][col]), None)
        if pivot is None: continue
        A[rank], A[pivot] = A[pivot], A[rank]
        A[rank] = [mul(inv[A[rank][col]],a) for a in A[rank]]
        for j in range(len(A)):
            if j == rank: continue
            factor=A[j][col]
            if factor:
                A[j] = [add(v,mul(neg(factor),w)) for v,w in zip(A[j],A[rank])]
        rank += 1
        if rank == len(A): break
    return rank


def algebra_basis(lengths):
    basis = [(-1,0)] + [(i,h) for i,r in enumerate(lengths) for h in range(1,r)]
    index={v:j for j,v in enumerate(basis)}
    products=[]
    for i,a in enumerate(basis):
        row=[]
        for j,b in enumerate(basis):
            if i==0: row.append(j)
            elif j==0:row.append(i)
            elif a[0]==b[0] and a[1]+b[1]<lengths[a[0]]:
                row.append(index[(a[0],a[1]+b[1])])
            else: row.append(-1)
        products.append(row)
    return basis,products


def formula_counts(lengths,q):
    result=Counter({0:1,1:q-1})
    for hs in itertools.product(*[range(r) for r in lengths]):
        if not any(hs):continue
        active=[h for h in hs if h>0]
        r=2+sum(h-1 for h in active)
        N=q
        for h in active:N*=(q-1)*q**(h-1)
        result[r]+=N
    return result


def check(lengths, q):
    basis,products=algebra_basis(lengths)
    counts=Counter()
    maxrank=2+sum(r-2 for r in lengths)
    bounds={R:[tuple(1+a for a in av) for av in itertools.product(*[range(r-1) for r in lengths]) if sum(av)==R-2] for R in range(2,maxrank+1)}
    positions={i:[(h, basis.index((i,h))) for h in range(1,L)] for i,L in enumerate(lengths)}
    for f in itertools.product(range(q), repeat=len(basis)):
        matrix=[[f[k] if k>=0 else 0 for k in row] for row in products]
        rank=matrix_rank(matrix,q)
        counts[rank]+=1
        for R,bv in bounds.items():
            predicted=any(all(all(h<=bound or f[j]==0 for h,j in positions[i]) for i,bound in enumerate(b)) for b in bv)
            if predicted != (rank<=R):
                raise AssertionError(('locus',q,lengths,R,f,rank,bv))
        for R,bv in bounds.items():
            assert len(bv)==sum(1 for a in itertools.product(*[range(r-1) for r in lengths]) if sum(a)==R-2)
    expected=formula_counts(lengths,q)
    if counts!=expected:
        raise AssertionError((q,lengths,sorted(counts.items()),sorted(expected.items())))
    maxrank=2+sum(r-2 for r in lengths)
    assert max(counts)==maxrank
    assert sum(counts.values())==q**len(basis)
    print('PASS',q,','.join(map(str,lengths)),len(basis),sorted(counts.items()))


def main():
    cases=[(2,(2,2)),(3,(2,2)),(4,(2,2)),
           (2,(2,3)),(3,(2,3)),(4,(2,3)),
           (2,(3,3)),(3,(3,3)),(4,(3,3)),
           (2,(2,2,2)),(3,(2,2,2)),(4,(2,2,2)),
           (2,(2,2,3)),(3,(2,2,3)),(4,(2,2,3)),
           (2,(2,3,3)),(3,(2,3,3)),
           (2,(2,2,2,2))]
    for q,lengths in cases:check(lengths,q)
    print('MULTIBRANCH_ASSOCIATIVE_PAIRING_RANKS_OK',len(cases))

if __name__=='__main__':main()
