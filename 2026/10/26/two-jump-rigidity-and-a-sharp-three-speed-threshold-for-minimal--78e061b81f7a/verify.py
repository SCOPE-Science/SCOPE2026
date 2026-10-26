#!/usr/bin/env python3
"""Finite combinatorial checks for binary jump classification and minimal positive triple."""
import itertools

def verify():
    cases=0
    for n in range(3,11):
        for a in range(1,5):
            for d in range(1,7):
                b=a+d
                for bits in itertools.product((False,True),repeat=n):
                    p=[b if bits[i] else a for i in range(n)]
                    f=[(i+p[i])%n for i in range(n)]
                    bij=len(set(f))==n
                    inv=all(bits[i]==bits[(i+d)%n] for i in range(n))
                    if bij != inv:
                        raise AssertionError((n,a,d,bits,bij,inv))
                    cases+=1
    constructs=0
    for n in (11,13,17,19,23,29):
        def R(z):
            z%=n
            return 1 if z==0 else (0 if z==1 else z)
        S=[R((R(i)+2)%n) for i in range(n)]
        p=[]
        for i,j in enumerate(S):
            opts=[k for k in (1,2,3) if (i+k)%n==j]
            assert len(opts)==1
            p.append(opts[0])
        assert set(p)=={1,2,3} and len(set(S))==n
        constructs+=1
    print('VERIFY_OK', cases, 'exhaustive finite-cycle two-valued assignments;', constructs, 'positive-triple conjugation proxies')

if __name__=='__main__':verify()
