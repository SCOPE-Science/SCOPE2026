#!/usr/bin/env python3
"""Exact rational checks for a two-class Lipschitz ellipsoid formula.
Inputs p,q >=2 and T=t^2/2 >=1/2, at most 2. This is reproducibility only;
the all-parameter theorem is proved separately by strict concavity and KKT.
"""
from fractions import Fraction as F
from itertools import combinations

def shape(p,q,T):
    p,q=int(p),int(q)
    assert 2<=p<=q and F(1,2)<=T<=2
    N=p+q; d=N-1
    if T<=F(q,2*q-1):
        a=b=T
        c=(1-F(p-1,p)*a-F(q-1,q)*b)/(F(N,p*q))
        phase=1
    elif T<=F(q,d):
        a=1-F(q-1,q)*T
        b=T
        c=F(q,N)*a
        phase=2
    else:
        a=F(p,d); b=F(q,d); c=F(p*q,N*d)
        phase=3
    return a,b,c,phase

def matrix(p,q,a,b,c):
    N=p+q
    X=[[F(0) for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            # within-class projector P_A (i,j < p), P_B (i,j >= p)
            if i<p and j<p: X[i][j]+=a*(int(i==j)-F(1,p))
            if i>=p and j>=p: X[i][j]+=b*(int(i==j)-F(1,q))
            # P_C entries: +q/(pN) on AxA, +p/(qN) on BxB, -1/N across
            pc=(F(q,p*N) if i<p else F(p,q*N)) if (i<p)==(j<p) else -F(1,N)
            X[i][j]+=c*pc
    return X

def check(p,q,T):
    a,b,c,phase=shape(p,q,T)
    N=p+q;d=N-1
    alpha=F(p-1,p);beta=F(q-1,q);gamma=F(N,p*q)
    assert a>0 and b>0 and c>0
    assert 2*a<=2*T and 2*b<=2*T
    assert alpha*a+beta*b+gamma*c==1
    # At optimum, all positive scalars. KKT multipliers for constraints
    # Lagrangian log determinant - lambda_cross*(alpha*a+beta*b+gamma*c-1)
    # - lambda_A*(a-T) - lambda_B*(b-T).
    lc=1/(gamma*c)
    la=F(p-1,1)/a-lc*alpha
    lb=F(q-1,1)/b-lc*beta
    assert la>=0 and lb>=0, (p,q,T,la,lb)
    assert la*(T-a)==0 and lb*(T-b)==0
    S=matrix(p,q,a,b,c)
    assert all(sum(row)==0 for row in S)
    for i,j in combinations(range(N),2):
        val=S[i][i]+S[j][j]-2*S[i][j]
        assert val>0
        assert val<=2*T if (i<p)==(j<p) else val==1, (p,q,T,i,j,val)
        if (i<p)==(j<p):
            assert val==2*(a if i<p else b)
    # The rational KKT certificate plus strict log-det concavity proves uniqueness.
    return phase

if __name__=='__main__':
    counts={1:0,2:0,3:0}; tests=0
    for p in range(2,12):
        for q in range(p,14):
            t1=F(q,2*q-1); t2=F(q,p+q-1)
            samples=[F(1,2),t1,(t1+t2)/2,t2,(t2+2)/2,F(2)]
            # Additional exact values throughout each interval.
            samples += [F(1,2)+(t1-F(1,2))*F(h,11) for h in range(1,11)]
            if t1<t2: samples += [t1+(t2-t1)*F(h,11) for h in range(1,11)]
            samples += [t2+(2-t2)*F(h,11) for h in range(1,11)]
            for T in set(samples):
                ph=check(p,q,T);counts[ph]+=1;tests+=1
    # Boundary equality / symmetry and contact transitions.
    assert shape(2,2,F(1,2))[:3] == (F(1,2),F(1,2),F(1,2))
    assert shape(2,5,F(5,9))[0]==F(5,9)
    print(f'PASS {tests} full rational matrix, support, and KKT checks; phases {counts}')
