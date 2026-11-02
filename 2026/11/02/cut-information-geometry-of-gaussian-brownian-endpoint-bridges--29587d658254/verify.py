"""Exact-rational checks for the conditional path information formula.

Run: python verify.py
Only Python's standard library is required.
The checks are finite diagnostics; the proof establishes the theorem.
"""
from fractions import Fraction as F
import itertools
import math
import random


def k(a, b, c, s, t):
    return min(s, t)-s*t+a*(1-s)*(1-t)+c*((1-s)*t+s*(1-t))+b*s*t


def determinant(mat):
    n=len(mat)
    A=[list(map(F, row)) for row in mat]
    v=F(1)
    for i in range(n):
        j=next((j for j in range(i,n) if A[j][i]), None)
        if j is None:
            return F(0)
        if j != i:
            A[i],A[j]=A[j],A[i]
            v=-v
        pivot=A[i][i]
        v *= pivot
        for j in range(i+1,n):
            if A[j][i]:
                q=A[j][i]/pivot
                for h in range(i+1,n):
                    A[j][h]-=q*A[i][h]
                A[j][i]=F(0)
    return v


def conditional_covariance(a,b,c,ts,cut):
    v=k(a,b,c,cut,cut)
    return [[k(a,b,c,s,t)-k(a,b,c,s,cut)*k(a,b,c,cut,t)/v for t in ts] for s in ts]


def squared_rho_from_three(a,b,c,t):
    A=k(a,b,c,F(0),F(0))
    B=k(a,b,c,F(1),F(1))
    C=k(a,b,c,F(0),F(1))
    V=k(a,b,c,t,t)
    L=k(a,b,c,F(0),t)
    R=k(a,b,c,t,F(1))
    return (C*V-L*R)**2/((A*V-L*L)*(B*V-R*R))


def squared_rho_formula(a,b,c,t):
    delta=a*b-c*c
    ratio=(F(1)-t)/t
    return (delta-c)**2/((b+delta*ratio)*(a+delta/ratio))


def path_information_ratio(a,b,c,s,t,u):
    # conditional mutual information of (X_0,X_s) and (X_u,X_1) given X_t
    ts=[F(0),s,u,F(1)]
    S=conditional_covariance(a,b,c,ts,t)
    A=[row[:2] for row in S[:2]]
    B=[row[2:] for row in S[2:]]
    return determinant(A)*determinant(B)/determinant(S)


def evaluate():
    rng=random.Random(20261029)
    checks=0
    for _ in range(650):
        a=F(rng.randint(1,14),rng.randint(1,9))
        b=F(rng.randint(1,14),rng.randint(1,9))
        # Ensure positive definiteness by using c^2 < ab.
        c=F(rng.randint(-8,8),20)*min(a,b)
        if a*b <= c*c:
            c=F(0)
        s=F(rng.randint(1,20),100)
        t=F(rng.randint(31,60),100)
        u=F(rng.randint(71,95),100)
        rho2=squared_rho_from_three(a,b,c,t)
        assert rho2 == squared_rho_formula(a,b,c,t)
        checks+=1
        assert 0 <= rho2 < 1
        checks+=1
        ratio=path_information_ratio(a,b,c,s,t,u)
        assert ratio == 1/(1-rho2)
        checks+=1
        # Geometric bridge precision expression, checked separately.
        delta=a*b-c*c
        j00=b/delta+(1-t)/t
        j11=a/delta+t/(1-t)
        j01=F(1)-c/delta
        assert rho2 == j01*j01/(j00*j11)
        checks+=1
    for aa,bb in itertools.product(range(1,10),repeat=2):
        a=F(aa**2)
        b=F(bb**2)
        # all such c give the same optimal cut time.
        tstar=F(aa,aa+bb)
        for ratio_c in [F(-3,4),F(-1,2),F(0),F(1,3),F(2,3)]:
            c=F(aa*bb)*ratio_c
            delta=a*b-c*c
            # For detC=c, rho2=0 and all times tie; inequality still holds.
            rsqstar=squared_rho_formula(a,b,c,tstar)
            rsqmax=(delta-c)**2/(delta+F(aa*bb))**2
            assert rsqstar==rsqmax
            checks+=1
            for q in [F(i,20) for i in range(1,20)]:
                assert squared_rho_formula(a,b,c,q) <= rsqmax
                checks+=1
    # Explicit singular covariance: Y_0=2Z, Y_1=3Z, Z~N(0,1).
    # After conditioning on the noisy interior measurement, Z remains diffuse.
    for t in (F(1,10),F(1,3),F(1,2),F(4,5)):
        v=t*(1-t)
        f=2*(1-t)+3*t
        assert v/(v+f*f)>0
        checks+=1
    print('PASS',checks,'exact-rational assertions')
    print('Example C=I, maximal conditional path information (nats):',format(-0.5*math.log(F(3,4)),'.12f'))
    print('Unique maximizing cut for (a,b)=(1,4):',F(1,3))


if __name__=='__main__':
    evaluate()
