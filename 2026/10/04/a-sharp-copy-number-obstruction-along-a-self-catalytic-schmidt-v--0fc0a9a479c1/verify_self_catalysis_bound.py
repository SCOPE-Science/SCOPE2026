#!/usr/bin/env python3
from fractions import Fraction
from itertools import product

BETA=(Fraction(19,20),Fraction(3,100),Fraction(1,50),Fraction(0,1))
ROWS=[
    (Fraction(900,1000),2,Fraction(18,11)),
    (Fraction(908,1000),3,Fraction(227,105)),
    (Fraction(918,1000),4,Fraction(459,140)),
    (Fraction(925,1000),5,Fraction(296,63)),
    (Fraction(928,1000),6,Fraction(928,165)),
]

def alpha(a):
    return (a,Fraction(247,250)-a,Fraction(3,500),Fraction(3,500))

def tensor(v,w):
    return tuple(x*y for x in v for y in w)

def power(v,n):
    out=(Fraction(1,1),)
    for _ in range(n):
        out=tensor(out,v)
    return out

def majorized(src,tgt):
    s=sorted(src,reverse=True)
    t=sorted(tgt,reverse=True)
    assert sum(s)==sum(t)==1
    cs=ct=Fraction(0,1)
    for k in range(len(s)-1):
        cs+=s[k]; ct+=t[k]
        if cs>ct:
            return False,k+1,cs-ct
    return True,None,Fraction(0,1)

def R(a):
    return 40*a/((19-20*a)*(247-250*a))

def prefix_diff(a,N):
    b=Fraction(247,250)-a
    S=a**N*(a+(N+1)*b)
    T=a**(N-1)*(Fraction(49,50)*a+Fraction(19,20)*N*b)
    return S-T

def main():
    success_checks=0
    failure_checks=0
    for a,N,r in ROWS:
        assert R(a)==r
        aa=alpha(a)
        src=power(aa,N+1)
        tgt=tensor(BETA,power(aa,N))
        ok,_,_=majorized(src,tgt)
        assert ok
        success_checks+=1

        for m in range(1,N):
            srcm=power(aa,m+1)
            tgtm=tensor(BETA,power(aa,m))
            ok,k,diff=majorized(srcm,tgtm)
            assert not ok
            # The analytic obstruction must itself fail at prefix m+2.
            assert prefix_diff(a,m)>0
            ss=sorted(srcm,reverse=True)
            tt=sorted(tgtm,reverse=True)
            assert sum(ss[:m+2])-sum(tt[:m+2])==prefix_diff(a,m)
            failure_checks+=1

    print("VERIFY_OK")
    print("successful_table_rows =",success_checks)
    print("smaller_copy_failures =",failure_checks)
    print("exact_bounds =",",".join(str(R(a)) for a,_,_ in ROWS))

if __name__=="__main__":
    main()
