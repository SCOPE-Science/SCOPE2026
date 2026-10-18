"""Exact finite checks for the cycle-record position covariance theorem."""
from itertools import permutations
from fractions import Fraction
from math import comb, factorial

def check(n):
    totals=[0]*(n+1)
    joint=[0]*(n+1)
    cyc_total=0
    r_total=0
    cr_total=0
    for perm in permutations(range(1,n+1)):
        cycle_count=0
        seen=[False]*(n+1)
        for p in range(1,n+1):
            if not seen[p]:
                cycle_count+=1
                q=p
                while not seen[q]:
                    seen[q]=True
                    q=perm[q-1]
        record_count=0
        current_max=0
        for k,v in enumerate(perm,1):
            if v>current_max:
                current_max=v
                record_count+=1
                totals[k]+=1
                joint[k]+=cycle_count
        cyc_total+=cycle_count
        r_total+=record_count
        cr_total+=cycle_count*record_count
    fact=factorial(n)
    H=sum((Fraction(1,k) for k in range(1,n+1)),Fraction(0))
    assert Fraction(cyc_total,fact)==H
    assert Fraction(r_total,fact)==H
    cov_sum=Fraction(0)
    for k in range(1,n+1):
        assert Fraction(totals[k],fact)==Fraction(1,k)
        observed=Fraction(joint[k],fact)-H*Fraction(1,k)
        expected=Fraction(k-1,k*k*comb(n,k))
        assert observed==expected,(n,k,observed,expected)
        cov_sum+=expected
    assert Fraction(cr_total,fact)-H*H==cov_sum
    return n, cov_sum

if __name__=='__main__':
    for n in range(1,10):
        print(*check(n))
    for n in range(1,201):
        H_n=sum((Fraction(1,j) for j in range(1,n+1)),Fraction(0))
        for k in range(1,n+1):
            lhs=sum((Fraction(comb(k,r),r*comb(n,r)) for r in range(1,k+1)),Fraction(0))
            rhs=sum((Fraction(1,j) for j in range(n-k+1,n+1)),Fraction(0))
            assert lhs==rhs
    print('PASS exact enumeration n<=9, all n<=200 binomial-harmonic identities')
