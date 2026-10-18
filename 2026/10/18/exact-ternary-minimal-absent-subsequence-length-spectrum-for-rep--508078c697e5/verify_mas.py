#!/usr/bin/env python3
"""Direct brute-force check of ternary repeated-block MAS distribution.
All tests independently use subsequence embedding rather than the weak-descent theorem.
"""
from itertools import product
from collections import Counter
from math import comb

def sub(u,w):
    i=0
    for letter in w:
        if i<len(u) and u[i]==letter:
            i+=1
    return i==len(u)

def minimal_absent(u,w):
    return not sub(u,w) and all(sub(u[:i]+u[i+1:],w) for i in range(len(u)))

def local(u,k):
    h=sum(u[i]>=u[i+1] for i in range(len(u)-1))
    if h!=k or len(u)<2 or u[0]<u[1] or u[-2]<u[-1]:return False
    return all(int(u[i-1]>=u[i])+int(u[i]>=u[i+1])-int(u[i-1]>=u[i+1]) == 1 for i in range(1,len(u)-1))

# independent polynomial transfer-counting
S=[(a,b) for a in range(3) for b in range(3)]
def matrix_counts(kmax):
    d=Counter()
    for a,b in S:
        if a>=b:d[(1,2,a,b)]=1
    output=Counter()
    for _ in range(3*kmax+3):
        nd=Counter()
        for (k,m,a,b),n in d.items():
            if k<=kmax and a>=b:output[(k,m)]+=n
            for c in range(3):
                newk=k+(b>=c)
                if newk<=kmax and int(a>=b)+int(b>=c)-int(a>=c)==1:
                    nd[(newk,m+1,b,c)]+=n
        d=nd
        if not d: break
    return output

M=matrix_counts(8)
expected_total=[6,16,46,127,349,960,2640,7264]
for k in range(1,9):
    computed=sum(v for (kk,m),v in M.items() if kk==k)
    assert computed==expected_total[k-1],(k,computed)
    assert M[(k,k+1)]==comb(k+3,2)
print('TRANSFER_OK',expected_total)
for k in range(1,7):
    w=tuple(i%3 for i in range(3*k))
    histogram=Counter()
    for m in range(2,1+max(m for (kk,m),n in M.items() if kk==k and n)):
        for u in product(range(3),repeat=m):
            mas=minimal_absent(u,w)
            loc=local(u,k)
            assert mas==loc,(k,m,u,mas,loc)
            if mas: histogram[m]+=1
    expected={m:n for (kk,m),n in M.items() if kk==k and n}
    assert dict(histogram)==expected,(k,histogram,expected)
    print('DIRECT_OK',k,dict(sorted(histogram.items())))
print('VERIFY_OK')
