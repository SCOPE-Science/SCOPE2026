#!/usr/bin/env python3
from fractions import Fraction
from itertools import product

def runs(bits):
    out=[]
    i=0
    while i<len(bits):
        j=i+1
        while j<len(bits) and bits[j]==bits[i]:
            j+=1
        out.append(j-i)
        i=j
    return out

def f_direct(bits):
    n=len(bits)
    total=0
    for a in range(1,n):
        for i in range(1,a+1):
            I=bits[i-1:a]
            for j in range(a+1,n+1):
                J=bits[a:j]
                if 1 in I and 0 in J:
                    total+=1
                if 0 in I and 1 in J:
                    total+=1
    return total

def phi(n,t):
    return t*(t+1)*(3*n-t-2)//6

checks=0
for n in range(3,15):
    T=n*(n*n-1)//6
    contacts=[]
    for bits in product((0,1),repeat=n):
        k=sum(bits)
        if k==0 or k==n:
            continue
        f=f_direct(bits)
        ls=runs(bits)
        f_run=2*T-sum(phi(n,t) for t in ls)+sum(ls[i]*ls[i+1] for i in range(len(ls)-1))
        assert f==f_run

        baseline=Fraction(n*k*(n-k),2)
        assert f>=baseline
        is_prefix_suffix=(len(ls)==2)
        assert (f==baseline)==is_prefix_suffix

        # Compare squared intrinsic facet distance with the claimed radius.
        dist2=Fraction(f*f*n,k*(n-k))
        r2=Fraction(n**3*(n-1),4)
        assert dist2>=r2
        if dist2==r2:
            X=tuple(i+1 for i,b in enumerate(bits) if b)
            contacts.append(X)
        checks+=1

    expected={
        (1,),
        (n,),
        tuple(range(1,n)),
        tuple(range(2,n+1)),
    }
    assert set(contacts)==expected,(n,contacts)

print(f"VERIFY_OK strong-rectangulotope-inradius subsets={checks} n=3..14 exact=yes")
