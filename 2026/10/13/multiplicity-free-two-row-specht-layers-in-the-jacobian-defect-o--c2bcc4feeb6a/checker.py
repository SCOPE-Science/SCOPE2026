#!/usr/bin/env python3
"""Exact finite-field Macaulay checks for the elementary-cubic Jacobian formula.
The accompanying mathematical argument establishes the all-size theorem over C.
These finite tests are independent diagnostics, not an infinite proof.
"""
from itertools import combinations
from math import comb

P = 1000003

def rank_sparse(columns):
    pivots = {}
    for vec in columns:
        v = {k: (a % P) for k, a in vec.items() if a % P}
        while v:
            pivot = max(v)
            if pivot not in pivots:
                inv = pow(v[pivot], -1, P)
                pivots[pivot] = {k: a*inv % P for k,a in v.items() if a*inv % P}
                break
            c = v[pivot]
            row = pivots[pivot]
            for k, a in row.items():
                val = (v.get(k,0)-c*a) % P
                if val:
                    v[k] = val
                else:
                    v.pop(k,None)
    return len(pivots)

def subsets(n,d):
    return [sum(1<<i for i in z) for j in range(min(n,d)+1)
            for z in combinations(range(n),j)]

def boole_kernel_dimension(n,d):
    old = subsets(n,d)
    new = {z:i for i,z in enumerate(subsets(n,d+1))}
    cols = []
    for mask in old:
        k = mask.bit_count()
        v = {}
        if k!=1:
            v[new[mask]]=k-1
        for i in range(n):
            if not mask>>i&1:
                v[new[mask|(1<<i)]]=1
        cols.append(v)
    return len(old)-rank_sparse(cols)

def exponents(n,d):
    if n==1:
        yield (d,)
        return
    for i in range(d+1):
        for rest in exponents(n-1,d-i):
            yield (i,)+rest

def direct_jacobian_dim(n,d):
    if d<2:return comb(n+d-1,d)
    mons = list(exponents(n,d))
    row = {v:i for i,v in enumerate(mons)}
    cols = []
    for alpha in exponents(n,d-2):
        for i in range(n):
            v = {}
            for j in range(n):
                if j==i:continue
                beta = list(alpha)
                beta[i]+=1
                beta[j]+=1
                v[row[tuple(beta)]]=-1
            cols.append(v)
    return len(mons)-rank_sparse(cols)

def expected(n,d):
    if d<=n-1:return comb(n,d)
    return n



def integer_partitions(n, ceiling=None):
    if n==0:
        yield ()
        return
    if ceiling is None:
        ceiling=n
    for k in range(min(ceiling,n),0,-1):
        for rest in integer_partitions(n-k,k):
            yield (k,)+rest


def fixed_subsets(cycles,d):
    counts=[0]*(d+1)
    counts[0]=1
    for length in cycles:
        for q in range(d,length-1,-1):
            counts[q]+=counts[q-length]
    return counts[d]


def check_characters(n):
    types=list(integer_partitions(n))
    for d in range(2,n-1):
        r=min(d,n-d)
        for typ in types:
            defect_char=fixed_subsets(typ,d)-fixed_subsets(typ,1)
            specht_char=sum(fixed_subsets(typ,j)-fixed_subsets(typ,j-1)
                            for j in range(2,r+1))
            assert defect_char==specht_char,(n,d,typ,defect_char,specht_char)
    return len(types)

def main():
    for n in range(3,9):
        for d in range(n+2):
            observed=boole_kernel_dimension(n,d)
            predicted=0 if d<n-1 else (n-1 if d==n-1 else n)
            assert observed==predicted,(n,d,observed,predicted)
        print('boolean_n=%d: kernel dimensions confirmed in degrees 0..%d'%(n,n+1))
    for n in range(3,6):
        vals=[]
        for d in range(n+2):
            got=direct_jacobian_dim(n,d)
            want=expected(n,d)
            assert got==want,(n,d,got,want)
            vals.append(got)
        print('direct_jacobian_n=%d: Hilbert values %s'%(n,','.join(map(str,vals))))
    for n in range(3,9):
        length=(1<<n)-n*n+n-2
        assert length==sum(comb(n,d)-n for d in range(2,n-1))
        print('defect_length_n=%d: %d'%(n,length))
    for n in range(4,10):
        nt=check_characters(n)
        print('character_n=%d: all %d cycle types and eligible degrees verified'%(n,nt))
    print('All character and finite-field checks passed (modulo %d).'%P)

if __name__=='__main__':
    main()
