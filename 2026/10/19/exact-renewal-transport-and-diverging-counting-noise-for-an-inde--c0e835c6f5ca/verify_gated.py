#!/usr/bin/env python3
"""Exact rational validation of a stochastic gated-bond vacancy ring.

Requires SymPy. Run: python verify_gated.py
Checks the independent full Markov generator against renewal formulas.
"""
import sympy as S

def formula(n,r,a,b,s):
    k=a+b
    p=b/k
    m=n-1
    return S.factor(r*((b+p*s)/(1+s)**m+(1-p)*s/(1+s+k)**m)/(s*s+(r+k)*s+r*b))

def moments(n,r,a,b):
    k=a+b; p=b/k; m=n-1; u=(1+k)**(-m)
    mean=S.factor(m+1/(r*p)+(1-p)*(1-u)/(p*k))
    nprime=r*(p-b*m+(1-p)*u)
    nsecond=r*(b*m*(m+1)-2*p*m-2*(1-p)*m*u/(1+k))
    second=S.factor((nsecond-2+2*mean*(r+k))/(r*b))
    return mean, second

def matrix(n,r,a,b):
    N=2*n
    Q=S.zeros(N)
    for i in range(n):
        for g in range(2):
            src=2*i+g
            dest=2*i+(1-g)
            rate=a if g==1 else b
            Q[src,dest]+=rate;Q[src,src]-=rate
            if i!=0 or g==1:
                rate=r if i==0 else S.Integer(1)
                dest=2*((i-1)%n)+g
                Q[src,dest]+=rate;Q[src,src]-=rate
    return Q

def check(n,r,a,b):
    Q=matrix(n,r,a,b)
    N=2*n
    assert all(sum(Q[i,j] for j in range(N))==0 for i in range(N))
    M=Q.T.copy()
    for j in range(N): M[N-1,j]=1
    rhs=S.zeros(N,1);rhs[N-1]=1
    pi=M.inv()*rhs
    assert all(x>0 for x in pi)
    J=S.factor(r*pi[1])
    mean,second=moments(n,r,a,b)
    assert S.simplify(J-1/mean)==0,(n,r,a,b,'current')
    K=Q.copy();K[1,2*(n-1)+1]-=r
    # The diagonal remains minus all original exit rates; this is killing.
    rhs=S.zeros(N,1);rhs[1]=r
    start=2*(n-1)+1
    E= -K.inv()*S.ones(N,1)
    E2= -K.inv()*(2*E)
    assert S.simplify(E[start]-mean)==0,(n,r,a,b,'first')
    assert S.simplify(E2[start]-second)==0,(n,r,a,b,'second')
    for s in [S.Rational(1,5),S.Rational(3,4)]:
        L=((s*S.eye(N)-K).inv()*rhs)[start]
        assert S.simplify(L-formula(n,r,a,b,s))==0,(n,r,a,b,'Laplace',s)
    return 4

if __name__=='__main__':
    count=0
    for n in range(3,9):
        for r,a,b in [
            (S.Rational(1,2), S.Rational(2,3), S.Rational(1,5)),
            (S.Rational(2), S.Rational(1,3), S.Rational(4,3)),
            (S.Rational(3,2), S.Rational(5,2), S.Rational(3)),
            (S.Rational(1,3), S.Rational(1,4), S.Rational(1,4)),
        ]:
            count+=check(n,r,a,b)
    print('PASS:',count,'independent rational generator/current/moment/Laplace identities,',6*4,'parameter instances')
