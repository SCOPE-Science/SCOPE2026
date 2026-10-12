#!/usr/bin/env python3
from fractions import Fraction
from itertools import permutations
from math import factorial, comb

def harmonic(n,power=1):
    return sum((Fraction(1,j**power) for j in range(1,n+1)), Fraction(0))

def run():
    permutations_checked=0
    local_cov_checks=aggregate_cov_checks=conditional_checks=0
    total_cov_checks=variance_checks=sign_checks=0

    for n in range(2,10):
        N=factorial(n)
        sumI=[0]*n
        sumR=[0]*n
        sumIR=[[0]*n for _ in range(n)]
        sumF=sumF2=sumRec=sumRec2=sumFRec=0
        sumFRj=[0]*n

        for p in permutations(range(1,n+1)):
            fixed=[int(p[i]==i+1) for i in range(n)]
            records=[]
            mx=0
            for x in p:
                records.append(int(x>mx))
                if x>mx:
                    mx=x
            F=sum(fixed)
            Rec=sum(records)
            sumF+=F; sumF2+=F*F
            sumRec+=Rec; sumRec2+=Rec*Rec
            sumFRec+=F*Rec
            permutations_checked+=1
            for i in range(n):
                sumI[i]+=fixed[i]
            for j in range(n):
                sumR[j]+=records[j]
                sumFRj[j]+=F*records[j]
                for i in range(n):
                    sumIR[i][j]+=fixed[i]*records[j]

        EF=Fraction(sumF,N)
        ERec=Fraction(sumRec,N)
        varF=Fraction(sumF2,N)-EF*EF
        varRec=Fraction(sumRec2,N)-ERec*ERec
        assert EF==1 and varF==1
        assert varRec==harmonic(n)-harmonic(n,2)
        variance_checks+=2

        cov_total=Fraction(sumFRec,N)-EF*ERec
        target_total=sum((Fraction(1,n*comb(n-1,j-1)) for j in range(2,n+1)), Fraction(0))
        assert cov_total==target_total
        total_cov_checks+=1

        for j in range(2,n+1):
            ERj=Fraction(sumR[j-1],N)
            assert ERj==Fraction(1,j)
            covFj=Fraction(sumFRj[j-1],N)-EF*ERj
            targetFj=Fraction(1,n*comb(n-1,j-1))
            assert covFj==targetFj
            aggregate_cov_checks+=1

            cond=Fraction(sumFRj[j-1],sumR[j-1])
            assert cond==1+Fraction(j,n*comb(n-1,j-1))
            conditional_checks+=1

            for i in range(1,n+1):
                cov=Fraction(sumIR[i-1][j-1],N)-Fraction(sumI[i-1],N)*ERj
                if i<j:
                    target=Fraction(1,n*j*(j-1))
                elif i==j:
                    target=Fraction(1,n)*(Fraction(1,comb(n-1,j-1))-Fraction(1,j))
                else:
                    target=Fraction(0)
                assert cov==target
                local_cov_checks+=1

            if n>=4:
                diag=Fraction(sumIR[j-1][j-1],N)-Fraction(sumI[j-1],N)*ERj
                if j<=n-2: assert diag<0
                elif j==n-1: assert diag==0
                else: assert diag>0
                sign_checks+=1

    print(
        "VERIFY_OK "
        f"permutations_checked={permutations_checked} "
        f"local_cov_checks={local_cov_checks} "
        f"aggregate_cov_checks={aggregate_cov_checks} "
        f"conditional_checks={conditional_checks} "
        f"total_cov_checks={total_cov_checks} "
        f"variance_checks={variance_checks} "
        f"sign_checks={sign_checks}"
    )

if __name__=="__main__":
    run()
