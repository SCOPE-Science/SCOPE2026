#!/usr/bin/env python3
"""Independent quadratic-character count in explicit extension fields of F3.
Pure Python and no dependency on COUNT.py.
"""
from itertools import product


def field_check(modulus):
    n=len(modulus)-1
    assert modulus[-1]==1
    q=3**n
    def mul(a,b):
        raw=[0]*(2*n-1)
        for i,x in enumerate(a):
            if x:
                for j,y in enumerate(b):raw[i+j]=(raw[i+j]+x*y)%3
        for k in range(2*n-2,n-1,-1):
            t=raw[k]
            if t:
                for j in range(n):raw[k-n+j]=(raw[k-n+j]-t*modulus[j])%3
        return tuple(raw[:n])
    zero=(0,)*n;one=(1,)+(0,)*(n-1)
    def integer(a):
        return sum(z*3**i for i,z in enumerate(a))
    def power(a,e):
        b=one
        while e:
            if e&1:b=mul(b,a)
            a=mul(a,a);e//=2
        return b
    squares=set()
    vals=list(product(range(3),repeat=n))
    for x in vals[1:]:
        if x!=zero:squares.add(integer(mul(x,x)))
    assert len(squares)==(q-1)//2, ('modulus reducible?',n,len(squares))
    good=[]
    for x in vals:
        if x==zero or all(x[i]==0 for i in range(1,n)):
            continue
        chars=[]
        for a in range(3):
            y=((x[0]-a)%3,)+x[1:]
            chars.append(integer(y) in squares)
        if all(chars):good.append(x)
    # An element has exact degree n iff it lies in no proper subfield.
    prime=[];k=n
    for p in range(2,n+1):
        if k%p==0:
            prime.append(p)
            while k%p==0:k//=p
    exact=[x for x in good if all(power(x,3**(n//p))!=x for p in prime)]
    print('degree',n,'all_triples',len(good),'exact_degree',len(exact),'polynomials',len(exact)//n)
    expected={6:(96,72,12),8:(798,720,90)}
    assert (len(good),len(exact),len(exact)//n)==expected[n]

if __name__=='__main__':
    field_check((1,0,0,0,2,0,1))
    field_check((1,0,0,0,0,1,2,2,1))
    print('independent finite-field character checks passed')
