#!/usr/bin/env python3
"""Exact finite-field checks for a family of quartic surfaces in characteristic two.

No external libraries are required. The universal scheme and monodromy claims
are proved symbolically in RESULT.md; finite checks are corroborating evidence.
"""
from itertools import product
from collections import Counter
from math import comb

EDGES = tuple((i,j) for i in range(4) for j in range(i+1,4))
IRREDUCIBLE = {1: 0b11, 2: 0b111, 3: 0b1011, 4: 0b10011}


def mul(a,b,m):
    mod = IRREDUCIBLE[m]
    ans = 0
    while b:
        if b & 1:
            ans ^= a
        b >>= 1
        a <<= 1
        if a & (1 << m):
            a ^= mod
    return ans


def powq(a,n,m):
    result=1
    while n:
        if n & 1:
            result=mul(result,a,m)
        a=mul(a,a,m)
        n>>=1
    return result


def trace(a,m):
    z=a
    out=0
    for _ in range(m):
        out ^= z
        z=mul(z,z,m)
    assert out in (0,1)
    return out


def Q(point,b,a,m):
    ans=0
    for i in range(4):
        ans ^= mul(b[i],mul(point[i],point[i],m),m)
    for e,c in zip(EDGES,a):
        i,j=e
        ans ^= mul(c,mul(point[i],point[j],m),m)
    return ans


def F(point,b,a,m):
    pr=1
    for x in point:
        pr=mul(pr,x,m)
    v=Q(point,b,a,m)
    return pr ^ mul(v,v,m)


def gradient(point,m):
    grad=[]
    for i in range(4):
        pr=1
        for j in range(4):
            if i!=j:
                pr=mul(pr,point[j],m)
        grad.append(pr)
    return tuple(grad)


def projective_points(m):
    elems=range(1 << m)
    seen=set()
    for p in product(elems,repeat=4):
        if p == (0,0,0,0):
            continue
        pivot=next(x for x in p if x)
        inv=powq(pivot,(1<<m)-2,m)
        normalized=tuple(mul(x,inv,m) for x in p)
        seen.add(normalized)
    return seen


def edge_support(b,a,m):
    elems=range(1<<m)
    out=set()
    for (i,j),aa in zip(EDGES,a):
        for t in elems:
            # x_i = 1, x_j = t on the coordinate edge.
            p=[0]*4
            p[i],p[j]=1,t
            if Q(p,b,a,m)==0:
                out.add(tuple(p))
    return out


def exhaustive_binary_coefficients():
    field=2
    m=2
    pts=projective_points(m)
    assert len(pts)==85
    counts=Counter()
    for mask in range(64):
        aa=tuple((mask>>k)&1 for k in range(6))
        bb=(1,1,1,1)
        actual={p for p in pts if F(p,bb,aa,m)==0 and gradient(p,m)==(0,0,0,0)}
        expected=edge_support(bb,aa,m)
        assert actual==expected, (mask, actual.symmetric_difference(expected))
        missing=sum(1 for z in aa if z==0)
        assert len(actual)==12-missing
        counts[missing]+=1
    assert all(counts[k]==comb(6,k) for k in range(7))
    return counts


def all_edge_trace_cases():
    count=0
    for m in (2,3,4):
        n=1<<m
        for bi,bj,a in product(range(1,n),range(1,n),range(n)):
            roots=[]
            for t in range(n):
                t2=mul(t,t,m)
                if mul(bi,t2,m) ^ mul(a,t,m) ^ bj == 0:
                    roots.append(t)
            if a==0:
                assert len(roots)==1
            else:
                inva=powq(a,n-2,m)
                arg=mul(mul(bi,bj,m),mul(inva,inva,m),m)
                assert len(roots)==(2 if trace(arg,m)==0 else 0)
            count+=1
    return count


def main():
    mask_counts=exhaustive_binary_coefficients()
    edge_cases=all_edge_trace_cases()
    assert edge_cases==4028
    print('SIX_EDGE_STRATIFICATION_MASK_COUNTS', dict(sorted(mask_counts.items())))
    print('EXACT_TRACE_EDGE_INSTANCES',edge_cases)
    print('TETRAHEDRAL_CHAR2_64_SURFACES_4028_TRACE_CASES_PASS')

if __name__=='__main__':
    main()
