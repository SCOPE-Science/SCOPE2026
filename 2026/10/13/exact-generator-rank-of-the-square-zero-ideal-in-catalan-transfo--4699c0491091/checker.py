#!/usr/bin/env python3
"""Direct finite checks for rank of the square-zero Catalan ideal."""
from itertools import product, combinations_with_replacement
from math import comb

def compose(v,u):
    return tuple(v[x-1] for x in u)

def square_zero(f):
    return all(f[f[i]-1] == 1 for i in range(len(f)))

def all_catalan(n):
    for f in product(*(range(1,i+1) for i in range(1,n+1))):
        if all(f[i]<=f[i+1] for i in range(n-1)):
            yield f

def specialized(n):
    for m in range(2,n+1):
        for t in combinations_with_replacement(range(2,m+1),n-m):
            yield (1,)*m+t

def criterion(f):
    if len(set(f))==1:return True
    m=next(i for i,y in enumerate(f) if y>1)
    return m>=f[-1]+len(set(f))-1

def theoretical(n):
    if n==1:return 1
    x=1
    for m in range(2,n):
        for s in range(1,min(n-m,(m-1)//2)+1):
            x+=comb(m-s-1,s)*comb(n-m-1,s-1)
    return x

def main():
    B=[0,1,1,1]
    for n in range(4,31):
        B.append(2*B[-1]-B[-2]+B[-3])
    for n in range(3,9):
        full=set(f for f in all_catalan(n) if square_zero(f))
        ref=set(specialized(n))
        assert full==ref,(n,'set')
        assert len(full)==2**(n-2)
        sq={compose(v,u) for u in full for v in full}
        by_criterion={f for f in full if criterion(f)}
        assert sq==by_criterion,(n, sq^by_criterion)
        assert len(sq)==theoretical(n)==B[n]
    for n in range(9,12):
        S=list(specialized(n))
        sq={compose(v,u) for u in S for v in S}
        by_criterion={f for f in S if criterion(f)}
        assert sq==by_criterion
        assert len(sq)==theoretical(n)==B[n]
    assert 2**(6-2)-B[6]==9 and 2**(6-3)==8
    print('VERIFY_OK')

if __name__=='__main__':main()
