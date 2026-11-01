#!/usr/bin/env python3
"""Direct adjacency-matrix power ranks over F_2; no polynomial factorization used."""
from itertools import combinations_with_replacement

def matrix(lengths):
    n = sum(lengths)
    forbidden = [set() for _ in range(n)]
    offset = 0
    for length in lengths:
        for j in range(length):
            forbidden[offset+j].update((offset+(j-1)%length, offset+(j+1)%length))
        offset += length
    return [sum(1<<j for j in range(n) if j != i and j not in forbidden[i]) for i in range(n)]

def product(A, B):
    C=[]
    for row in A:
        value = 0
        while row:
            bit = row & -row
            value ^= B[bit.bit_length()-1]
            row -= bit
        C.append(value)
    return C

def binary_rank(A):
    pivots={}
    for row in A:
        while row:
            col = row.bit_length()-1
            if col in pivots:
                row ^= pivots[col]
            else:
                pivots[col] = row
                break
    return len(pivots)

def predicted_nullity(lengths, t):
    n=sum(lengths)
    return (int(n%2==1 and t>0)
       + 2*sum(min(t,(m & -m)) for m in lengths if m%3==0))

def verify(lengths):
    n=sum(lengths)
    adjacency=matrix(lengths)
    power=[1<<i for i in range(n)]
    e=max([1 if n%2 else 0]+[(m & -m) for m in lengths if m%3==0]+[0])
    for t in range(e+3):
        nullity=n-binary_rank(power)
        prediction=predicted_nullity(lengths,t)
        assert nullity==prediction,(lengths,t,nullity,prediction)
        power=product(power,adjacency)

if __name__=='__main__':
    tested=0
    for number in (1,2,3,4):
        for lengths in combinations_with_replacement(range(3,17),number):
            if sum(lengths)>40:continue
            verify(lengths);tested+=1
    print('PASS: exact GF(2) matrix-power nullity identity on',tested,
          'cycle multisets, each length 3..16, at most four components, N<=40.')
    for example in ((3,3),(3,6),(3,12),(6,6),(6,12),(12,12),(3,4,5)):
        n=sum(example)
        nulls=[predicted_nullity(example,t) for t in range(6)]
        print('lengths',example,'N',n,'nullities t=0..5',nulls)
