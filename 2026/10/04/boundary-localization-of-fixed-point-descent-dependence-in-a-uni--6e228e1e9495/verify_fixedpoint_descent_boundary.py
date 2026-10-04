#!/usr/bin/env python3
from fractions import Fraction
from itertools import permutations
import math

def run():
    permutations_checked=0
    local_cov_checks=0
    row_sum_checks=0
    column_sum_checks=0
    cyclic_checks=0
    global_checks=0
    variance_checks=0

    for n in range(2,10):
        N=math.factorial(n)
        sumI=[0]*n
        sumJ=[0]*(n-1)
        sumK=0
        sumIJ=[[0]*(n-1) for _ in range(n)]
        sumIK=[0]*n
        sumF=sumD=sumC=sumFD=sumFC=sumF2=sumD2=0

        for p in permutations(range(1,n+1)):
            I=[int(p[i]==i+1) for i in range(n)]
            J=[int(p[j]>p[j+1]) for j in range(n-1)]
            K=int(p[n-1]>p[0])
            F=sum(I)
            D=sum(J)
            C=D+K

            for i,a in enumerate(I):
                sumI[i]+=a
                if a:
                    for j,b in enumerate(J):
                        sumIJ[i][j]+=b
                    sumIK[i]+=K
            for j,b in enumerate(J):
                sumJ[j]+=b
            sumK+=K

            sumF+=F
            sumD+=D
            sumC+=C
            sumFD+=F*D
            sumFC+=F*C
            sumF2+=F*F
            sumD2+=D*D
            permutations_checked+=1

        EF=Fraction(sumF,N)
        ED=Fraction(sumD,N)
        EC=Fraction(sumC,N)
        assert EF==1
        assert ED==Fraction(n-1,2)
        assert EC==Fraction(n,2)

        for i0 in range(n):
            i=i0+1
            EI=Fraction(sumI[i0],N)
            assert EI==Fraction(1,n)

            for j0 in range(n-1):
                j=j0+1
                EJ=Fraction(sumJ[j0],N)
                assert EJ==Fraction(1,2)
                cov=Fraction(sumIJ[i0][j0],N)-EI*EJ

                if i==j:
                    target=Fraction(2*j-n-1,2*n*(n-1))
                elif i==j+1:
                    target=Fraction(n-2*j-1,2*n*(n-1))
                else:
                    target=Fraction(0)

                assert cov==target
                local_cov_checks+=1

            row=sum(
                Fraction(sumIJ[i0][j0],N)
                - EI*Fraction(sumJ[j0],N)
                for j0 in range(n-1)
            )
            target_row=Fraction(-1,2*n) if i in (1,n) else Fraction(0)
            assert row==target_row
            row_sum_checks+=1

            wrap_cov=Fraction(sumIK[i0],N)-EI*Fraction(sumK,N)
            assert row+wrap_cov==0
            cyclic_checks+=1

        for j0 in range(n-1):
            col=sum(
                Fraction(sumIJ[i0][j0],N)
                - Fraction(sumI[i0],N)*Fraction(sumJ[j0],N)
                for i0 in range(n)
            )
            assert col==Fraction(-1,n*(n-1))
            column_sum_checks+=1

        covFD=Fraction(sumFD,N)-EF*ED
        covFC=Fraction(sumFC,N)-EF*EC
        assert covFD==Fraction(-1,n)
        assert covFC==0
        global_checks+=2

        varF=Fraction(sumF2,N)-EF*EF
        varD=Fraction(sumD2,N)-ED*ED
        assert varF==1
        assert varD==Fraction(n+1,12)
        variance_checks+=2

    print(
        "VERIFY_OK "
        f"permutations_checked={permutations_checked} "
        f"local_cov_checks={local_cov_checks} "
        f"row_sum_checks={row_sum_checks} "
        f"column_sum_checks={column_sum_checks} "
        f"cyclic_checks={cyclic_checks} "
        f"global_checks={global_checks} "
        f"variance_checks={variance_checks}"
    )

if __name__=="__main__":
    run()
