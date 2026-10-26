#!/usr/bin/env python3
"""Finite checks for the characteristic-two elementary-symmetric cubic.
This is supporting finite evidence; the all-dimensional proof is in RESULT.md.
"""
from itertools import product
from math import comb

# F4 = F2[a]/(a*a+a+1), bit encodings 0,1,a,a+1.
def mul(a,b):
    x=0
    for j in range(2):
        if (b>>j)&1: x ^= a<<j
    if x&8: x ^= 0b1110
    if x&4: x ^= 0b111
    return x

def gradients(point):
    n=len(point)
    out=[]
    for i in range(n):
        inds=[k for k in range(n) if k!=i]
        z=0
        for a in range(len(inds)):
            for b in range(a+1,len(inds)):
                z ^= mul(point[inds[a]],point[inds[b]])
        out.append(z)
    return out

def normalized_vectors(n, field_size):
    for first in range(n):
        for suffix in product(range(field_size),repeat=n-first-1):
            yield (0,)*first+(1,)+suffix

def rank2(matrix):
    a=list(matrix)
    basis={}
    for row in a:
        x=row
        while x:
            j=x.bit_length()-1
            if j in basis: x ^= basis[j]
            else:
                basis[j]=x
                break
    return len(basis)

def parity_hessian_rank(point):
    n=len(point)
    pivot=next(i for i,t in enumerate(point) if t)
    free=[i for i in range(n) if i!=pivot]
    rows=[]
    for i in free:
        r=0
        for pos,j in enumerate(free):
            if j!=i and (sum(point[k] for k in range(n) if k!=i and k!=j)%2):
                r|=1<<pos
        rows.append(r)
    return rank2(rows)

def run():
    for n in range(3,13):
        crit=[]
        for a in normalized_vectors(n,2):
            if not any(gradients(a)):
                crit.append(a)
        actual={tuple(a) for a in crit}
        expected={tuple(int((mask>>j)&1) for j in range(n))
                  for mask in range(1,1<<n) if mask.bit_count()%4==1}
        if n%4==2:
            assert actual!=expected  # these cases have positive-dimensional critical loci
            print('n=',n, 'excluded (positive-dimensional critical locus)', 'F2-points=',len(actual))
            continue
        assert actual==expected,(n,len(actual),len(expected),actual^expected)
        for a in crit:
            r=parity_hessian_rank(a)
            assert r==(n-1 if n%2 else n-2),(n,a,r)
            if n%4==0:
                m=sum(a)
                t=n-m
                assert m%4==1 and t%4==3
                assert (m*comb(t,2))%2==1
        distinct=len(expected)
        length=distinct*(2 if n%4==0 else 1)
        if n%4==0: assert length==2**(n-1)
        print('n=',n,'F2-singular-points=',distinct,'projective-Jacobian-length=',length)
    for n in range(3,9):
        if n%4==2: continue
        count=0
        for pt in normalized_vectors(n,4):
            if not any(gradients(pt)):
                count+=1
                assert all(c in (0,1) for c in pt) and sum(pt)%4==1,(n,pt)
        predicted=sum(comb(n,j) for j in range(1,n+1,4))
        assert count==predicted,(n,count,predicted)
        print('F4-complete n=',n,'singular=',count)
    print('VERIFY_OK')

if __name__=='__main__':run()
