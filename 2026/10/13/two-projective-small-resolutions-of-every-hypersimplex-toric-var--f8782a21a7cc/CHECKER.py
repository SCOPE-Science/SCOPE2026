"""Exact enumeration of bounded cube slices and their two smooth refinements."""
from fractions import Fraction
from itertools import product, combinations
from math import comb
from collections import Counter


def bounded_slice_vertices(n,k,low,high):
    vertices=set()
    for f in range(n):
        for b in product((low,high),repeat=n-1):
            z=list(b)
            missing=Fraction(k)-sum(b)
            if low <= missing <= high:
                z.insert(f,missing)
                vertices.add(tuple(z))
    return vertices


def audit(n,k,orientation):
    eps=Fraction(1,3*n)
    low,high=(Fraction(0),Fraction(1)+eps) if orientation=='upper' else (Fraction(0)-eps,Fraction(1))
    actual=bounded_slice_vertices(n,k,low,high)
    expected=set()
    fiber=Counter()
    for f in range(n):
        if orientation=='upper':
            for uppers in combinations((i for i in range(n) if i!=f),k-1):
                z=[Fraction(0)]*n
                for i in uppers: z[i]=high
                z[f]=Fraction(1)-(k-1)*eps
                expected.add(tuple(z));fiber[tuple(sorted((*uppers,f)))]+=1
        else:
            for uppers in combinations((i for i in range(n) if i!=f),k):
                z=[low]*n
                for i in uppers: z[i]=high
                z[f]=(n-k-1)*eps
                expected.add(tuple(z));fiber[tuple(uppers)]+=1
    assert actual==expected,(n,k,orientation,len(actual),len(expected))
    assert len(actual)==(k if orientation=='upper' else n-k)*comb(n,k)
    assert len(fiber)==comb(n,k)
    assert all(v==(k if orientation=='upper' else n-k) for v in fiber.values())
    assert all(sum(sum(1 for t in z if t in (low,high)) for z in [v])==n-1 for v in actual)
    return len(actual)


def main():
    instances=0;verts=0
    for n in range(4,10):
        for k in range(2,n-1):
            for side in ('upper','lower'):
                verts+=audit(n,k,side);instances+=1
        print(f'n={n}: complete exact bounded-slice vertex enumeration passed')
    assert comb(4,2)==6 and comb(4+2-2,2-1)==4
    print(f'PASS tested_instances={instances} enumerated_vertices={verts}')

if __name__=='__main__':
    main()
