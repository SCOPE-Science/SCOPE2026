"""Brute-force check conditional squarefree polynomial counts in binary fields.

Usage: python VERIFY.py. No external dependencies.
"""
from itertools import product
from math import gcd

MODS = {1: 0b11, 2: 0b111, 3: 0b1011, 4: 0b10011}

def mult(a,b,rank):
    mod=MODS[rank]
    ans=0
    while b:
        if b&1: ans ^= a
        b>>=1
        a<<=1
        if a&(1<<rank): a^=mod
    return ans

def inverse(x,rank):
    if not x: raise ZeroDivisionError
    q=1<<rank
    for y in range(1,q):
        if mult(x,y,rank)==1:return y
    raise ArithmeticError('nonunit')

def trim(p):
    while p and p[-1]==0:p.pop()
    return p

def rem(a,b,rank):
    a=trim(list(a)); b=trim(list(b))
    if not b:raise ZeroDivisionError
    c=inverse(b[-1],rank)
    while len(a)>=len(b):
        d=len(a)-len(b)
        scale=mult(a[-1],c,rank)
        if scale:
            for j in range(len(b)):
                a[j+d]^=mult(scale,b[j],rank)
        a=trim(a)
    return a

def is_squarefree(coefs,rank):
    derivative=trim([coefs[j] if j%2 else 0 for j in range(1,len(coefs))])
    a=list(coefs); b=derivative
    while b:
        a,b=b,rem(a,b,rank)
    return len(a)==1

def predicted(q,n,t):
    sn=(-1)**n
    numerator=(q**(n-1)-q*sn) if t==0 else (q**(n-1)+sn)
    assert numerator%(q+1)==0
    return numerator//(q+1)

def verify():
    total_cases=0
    total_polys=0
    count_fibers=0
    nonzero_constant=0
    for rank,top in ((1,10),(2,7),(3,5),(4,4)):
        q=1<<rank
        for n in range(2,top+1):
            obs={(t,c):0 for t in range(q) for c in range(1,q)}
            for middle in product(range(q),repeat=n-2):
                for t in range(q):
                    for c in range(1,q):
                        f=(c,)+middle+(t,1)
                        total_polys+=1
                        if is_squarefree(f,rank):
                            obs[(t,c)]+=1
            for (t,c),v in obs.items():
                assert v==predicted(q,n,t),(rank,n,t,c,v,predicted(q,n,t))
            total_cases+=1
            count_fibers+=len(obs)
            nonzero_constant+=sum(obs.values())
    print('VERIFY_OK cases=',total_cases,'fibers=',count_fibers,'polynomials=',total_polys,'squarefree=',nonzero_constant)

if __name__=='__main__':verify()
