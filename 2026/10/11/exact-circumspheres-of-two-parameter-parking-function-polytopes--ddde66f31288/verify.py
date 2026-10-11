#!/usr/bin/env python3
from fractions import Fraction
from math import ceil, sqrt

def q(layer,s):
    return sum((Fraction(x)-s)*(Fraction(x)-s) for x in layer)

checks=0
for n in range(2,26):
    for a in range(1,9):
        for b in range(1,7):
            d=a-1
            lam=[d+j*b for j in range(n)]
            layers=[[0]*k+lam[k:] for k in range(n+1)]
            S=[sum(lam[k:]) for k in range(n+1)]
            T=[sum(x*x for x in lam[k:]) for k in range(n+1)]
            D=[None]+[2*S[k]-n*lam[k-1] for k in range(1,n+1)]
            assert all(D[k+1] < D[k] for k in range(1,n))
            K=min(k for k in range(1,n+1) if D[k] <= n*b)
            s=Fraction(S[K],n) if D[K]>=0 else Fraction(lam[K-1],2)
            R2=Fraction(n)*s*s-2*S[K]*s+T[K]
            direct=[q(v,s) for v in layers]
            assert max(direct)==R2
            # Verify the convex piecewise-quadratic optimality conditions directly.
            if D[K]>=0:
                assert 0 <= D[K] <= n*b
            else:
                assert K>1 and D[K-1] > n*b and D[K] < 0
            active=[k for k,val in enumerate(direct) if val==R2]
            if a==1 and 0 in active and 1 in active:
                active=[k for k in active if k!=0]
            if 0 < D[K] < n*b:
                expected=[K]
            elif D[K] == n*b:
                expected=[K,K+1]
            else:
                expected=[K-1,K]
            if a==1 and 0 in expected and 1 in expected:
                expected=[k for k in expected if k!=0]
            assert active==expected, (n,a,b,K,D[K],active,expected)
            if a==1 and b==1:
                Kn=ceil((sqrt((n-1)*(5*n-1))-(n-1))/2 - 1e-12)
                assert K==Kn
            checks+=1
print(f"VERIFY_OK parking-circumspheres cases={checks} exact_layer_minimax=yes")
