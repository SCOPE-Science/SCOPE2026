#!/usr/bin/env python3
from fractions import Fraction
from itertools import product
import math

def falling(x,r):
    out=1
    for j in range(r):
        out*=x-j
    return out

def run():
    words_checked=0
    leaf_mean_checks=0
    first_cov_checks=0
    factorial_cov_checks=0
    conditional_checks=0
    pgf_checks=0
    sign_checks=0

    for n in range(3,9):
        m=n-2
        rows=[]
        byk={k:[] for k in range(m+1)}
        for w in product(range(n), repeat=m):
            cnt=[0]*n
            for x in w:
                cnt[x]+=1
            N=cnt[0]
            L=sum(c==0 for c in cnt)
            rows.append((N,L))
            byk[N].append(L)
            words_checked+=1

        total=n**m
        a=Fraction(n-1,n)
        b=Fraction(n-2,n-1)

        EL=Fraction(sum(L for N,L in rows),total)
        assert EL==n*(a**m)
        leaf_mean_checks+=1

        EN=Fraction(sum(N for N,L in rows),total)
        ENL=Fraction(sum(N*L for N,L in rows),total)
        assert ENL-EN*EL==0
        first_cov_checks+=1

        for k, vals in byk.items():
            if not vals:
                continue
            got=Fraction(sum(vals),len(vals))
            if k==0:
                target=1+(n-1)*(b**m)
            else:
                target=(n-1)*(b**(m-k))
            assert got==target
            conditional_checks+=1

        for r in range(1,m+1):
            ef=Fraction(sum(falling(N,r) for N,L in rows),total)
            efl=Fraction(sum(falling(N,r)*L for N,L in rows),total)
            cov=efl-ef*EL
            target=Fraction(falling(m,r),n**r)*(a**(m-r))*((n-1)-n*(a**r))
            assert cov==target
            if r==1:
                assert cov==0
            else:
                assert cov>0
                sign_checks+=1
            factorial_cov_checks+=1

        for z in (Fraction(0),Fraction(1,2),Fraction(3,2),Fraction(2)):
            lhs=Fraction(sum(L*(z**N) for N,L in rows),total)
            rhs=(a**m)+(n-1)*(Fraction(n-2, n)+Fraction(1,n)*z)**m
            assert lhs==rhs
            pgf_checks+=1

    print(
        "VERIFY_OK "
        f"words_checked={words_checked} "
        f"leaf_mean_checks={leaf_mean_checks} "
        f"first_cov_checks={first_cov_checks} "
        f"factorial_cov_checks={factorial_cov_checks} "
        f"conditional_checks={conditional_checks} "
        f"pgf_checks={pgf_checks} "
        f"sign_checks={sign_checks}"
    )

if __name__=="__main__":
    run()
