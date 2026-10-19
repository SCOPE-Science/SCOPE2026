"""Exact rational verification for a three-regime noisy-voter process.
Uses only the Python standard library. Run: python check.py
"""
from fractions import Fraction as F
from itertools import product

def solve(A,b):
    n=len(b); a=[list(A[i])+[b[i]] for i in range(n)]
    for col in range(n):
        pivot=next(k for k in range(col,n) if a[k][col]); a[col],a[pivot]=a[pivot],a[col]
        q=a[col][col]; a[col]=[v/q for v in a[col]]
        for row in range(n):
            if row!=col and a[row][col]:
                v=a[row][col]; a[row]=[a[row][j]-v*a[col][j] for j in range(n+1)]
    return [a[i][-1] for i in range(n)]

def case(N,a,alpha,delta,lam):
    states=list(product(range(N+1), range(3))); sz=len(states)
    index={s:j for j,s in enumerate(states)}
    q=1/(1+alpha); beta=alpha/(1+alpha); c=2*a+beta
    z=[F(0),delta,F(1)]
    G=[[F(0) for _ in states] for __ in states]
    for row,(i,s) in enumerate(states):
        up=(N-i)*(a+q*i/N+beta*z[s]); dn=i*(a+q*(N-i)/N+beta*(1-z[s]))
        for state,rate in [((i+1,s),up) if i<N else ((i,s),F(0)),((i-1,s),dn) if i>0 else ((i,s),F(0))]:
            if rate: G[row][index[state]]+=rate; G[row][row]-=rate
        for s2,rate in ({0:{1:lam},1:{0:lam/2,2:lam/2},2:{1:lam}}[s]).items():
            G[row][index[(i,s2)]]+=rate; G[row][row]-=rate
    A=[[G[j][i] for j in range(sz)] for i in range(sz)]; b=[F(0)]*sz
    A[-1]=[F(1)]*sz; b[-1]=F(1)
    pi=solve(A,b)
    def ex(f):return sum(pi[i]*f[i] for i in range(sz))
    bar=(1+2*delta)/4
    mu=(a+beta*bar)/c
    f=[F(i,N)-mu for i,s in states]
    var=ex([v*v for v in f]); cov=ex([f[k]*(z[s]-bar) for k,(i,s) in enumerate(states)])
    V1=F(1,8); V2=(1-2*delta)**2/16
    covexpected=beta*(V1/(c+lam)+V2/(c+2*lam))
    E1=beta**2*V1/(c*(c+lam)); E2=beta**2*V2/(c*(c+2*lam))
    env=E1+E2
    H0=a+2*q*mu*(1-mu)+beta*(mu+bar-2*mu*bar)
    kappa=H0/2-(c+q)*env
    vexp=env+kappa/(N*c+q)
    assert cov==covexpected,(N,cov,covexpected)
    assert var==vexp,(N,var,vexp)
    assert kappa>0
    cur=f
    def gder(k,eta):
        if c==eta:
            return (-c)**k*(1-k)
        return (c*(-eta)**k-eta*(-c)**k)/(c-eta)
    for k in range(7):
        actual=ex([f[j]*cur[j] for j in range(sz)])
        expected=E1*gder(k,lam)+E2*gder(k,2*lam)+(var-env)*(-c)**k
        assert actual==expected,(N,k,actual,expected)
        cur=[sum(G[i][j]*cur[j] for j in range(sz)) for i in range(sz)]
    return sz,kappa,var

if __name__=='__main__':
    examples=[(F(1,10),F(1,2),F(4,5),F(7,10)),
              (F(0),F(2,3),F(1,2),F(1,3)),
              (F(1,4),F(1),F(1,3),F(5,7)),
              (F(1,3),F(1,2),F(3,5),F(7,15)),
              (F(1,12),F(1,2),F(1,2),F(1,2)),
              (F(1,4),F(1),F(3,5),F(1,2))]
    tests=0
    for a,alpha,delta,lam in examples:
        for N in (1,2,3,4,5):
            sz,kappa,var=case(N,a,alpha,delta,lam)
            tests+=7
            print(f'N={N}, states={sz}, variance={var}, intrinsic coefficient={kappa}')
    print(f'PASS: {len(examples)*5} exact rational generators, {tests} covariance-derivative identities (orders 0..6), all positive coefficients')
