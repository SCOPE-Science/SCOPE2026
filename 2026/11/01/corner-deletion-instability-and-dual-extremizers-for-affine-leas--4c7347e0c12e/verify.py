#!/usr/bin/env python3
"""Exact rational checks for affine least-squares projection on a punctured Boolean cube."""
from fractions import Fraction
from itertools import product
from math import comb

def theoretical(d):
    assert d>=2
    M=1<<d
    C=comb(d,d//2)
    base=Fraction((d+1)*C,M)
    correction=Fraction((d-1)*( (d-1 if d%2==0 else d+1)*C-M),M*(M-d-1))
    return base+correction,base

def numerator(d,x,y):
    M=1<<d
    m=d+1
    return (M-m)*(1+sum(a*b for a,b in zip(x,y)))+(1+sum(x))*(1+sum(y))

def computed_row_by_orbit(d,k):
    M=1<<d;den=M-d-1
    raw=0
    for h in range(k+1):
        for l in range(d-k+1):
            if h+l==0:continue # deleted all-plus design point
            yminus=h+l
            mismatch=k-h+l
            p=d+1-2*mismatch
            tx=d+1-2*k
            ty=d+1-2*yminus
            raw+=comb(k,h)*comb(d-k,l)*abs((M-d-1)*p+tx*ty)
    return Fraction(raw,M*den)

def run():
    cnt={'matrix_kernel_entries':0,'orbit_rows':0,'sign_checks':0,'extremizer_rows':0,'fullrank_checks':0}
    for d in range(2,11):
        M=1<<d;den=M-d-1
        full=[x for x in product((-1,1),repeat=d) if any(v==-1 for v in x)]
        theory,base=theoretical(d)
        assert (M>d+1)
        cnt['fullrank_checks']+=1
        by_k={k:computed_row_by_orbit(d,k) for k in range(1,d+1)}
        cnt['orbit_rows']+=d
        assert max(by_k.values())==theory,(d,max(by_k.values()),theory)
        assert [k for k,v in by_k.items() if v==theory]==([1,2] if d==2 else [1,d])
        for x in full:
            k=sum(t==-1 for t in x)
            raw=0; signed=0
            for y in full:
                p=1+sum(a*b for a,b in zip(x,y))
                v=numerator(d,x,y)
                assert p*v>=0,(d,x,y,p,v)
                cnt['sign_checks']+=1
                raw+=abs(v)
                signed+=v
                cnt['matrix_kernel_entries']+=1
            assert Fraction(raw,M*den)==by_k[k],(d,k,raw,by_k[k])
            assert Fraction(signed,M*den)==1
            if k in (1,d):
                # sign(x-row) is the exact norm-attaining data function
                val=Fraction(raw,M*den)
                assert val==theory
                cnt['extremizer_rows']+=1
    for d in range(11,101):
        theory,base=theoretical(d)
        by_k=[computed_row_by_orbit(d,k) for k in range(1,d+1)]
        assert max(by_k)==theory
        assert [k+1 for k,v in enumerate(by_k) if v==theory]==[1,d]
        cnt['orbit_rows']+=d
        assert theory>base
    # Exact elementary cases and growth checks
    assert theoretical(2)==(Fraction(1),Fraction(3,2))
    assert theoretical(3)==(Fraction(7,4),Fraction(3,2))
    assert theoretical(4)==(Fraction(21,11),Fraction(15,8))
    print('ALL PASS:',cnt)
    print('d=3..9:',[(d,str(theoretical(d)[0])) for d in range(3,10)])
if __name__=='__main__': run()
