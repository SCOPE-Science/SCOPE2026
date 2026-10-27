"""Numerical and exact-rational checks for stationary-barycenter Lipschitz theorem.

Requires numpy and scipy for the numerical heat-semigroup section.
Run: python check_stationary_barycentric.py
"""
from fractions import Fraction as F
from random import Random
import numpy as np
from scipy.linalg import expm


def barrier(pi, x):
    return [
        (sum(pi[j]*x[j] for j in range(k+1,len(pi)))/sum(pi[k+1:])
         -sum(pi[j]*x[j] for j in range(k+1))/sum(pi[:k+1]))
         /(x[k+1]-x[k])
        for k in range(len(pi)-1)
    ]


def block_kernel(pi, k):
    n=len(pi)
    Q=[[F(0) for j in range(n)] for i in range(n)]
    for i in range(n):
        indices=range(0,k+1) if i<=k else range(k+1,n)
        total=sum(pi[j] for j in indices)
        for j in indices:
            Q[i][j]=pi[j]/total
    return Q


def row_metric(P,x):
    n=len(P)
    vals=[]
    for i in range(n-1):
        d=[P[i][j]-P[i+1][j] for j in range(n)]
        cum=0
        s=0
        for j in range(n-1):
            cum+=d[j]
            s+=(x[j+1]-x[j])*abs(cum)
        vals.append(s/(x[i+1]-x[i]))
    return vals


def means_metric(P,x):
    v=[sum(P[i][j]*x[j] for j in range(len(x))) for i in range(len(x))]
    return [(v[i+1]-v[i])/(x[i+1]-x[i]) for i in range(len(x)-1)]


def check_exact():
    r=Random(247)
    tests=0
    for n in range(3,13):
        for trial in range(17):
            raw=[r.randrange(1,20) for i in range(n)]
            pi=[F(v,sum(raw)) for v in raw]
            x=[F(0)]
            for i in range(n-1):
                x.append(x[-1]+F(r.randrange(1,13),r.randrange(1,9)))
            B=barrier(pi,x)
            for k in range(n-1):
                K=block_kernel(pi,k)
                assert all(sum(K[i])==1 for i in range(n))
                assert all(sum(pi[i]*K[i][j] for i in range(n))==pi[j] for j in range(n))
                row=row_metric(K,x)
                mean=means_metric(K,x)
                assert row==mean
                assert row[k]==B[k]
                assert max(row)<=max(B)
                tests+=1
    for n in range(3,30):
        pi=[F(1,n)]*n
        x=[F(i) for i in range(n)]
        assert all(b==F(n,2) for b in barrier(pi,x))
    # Stationarity without order preservation cannot be substituted for monotonicity.
    perm=(0,3,1,2)
    K=[[F(int(perm[i]==j)) for j in range(4)] for i in range(4)]
    assert max(row_metric(K,[F(i) for i in range(4)]))==3
    assert max(barrier([F(1,4)]*4,[F(i) for i in range(4)]))==2
    print('exact block and equilibrium checks:',tests,'; boundary permutation: OK')


def make_Q(pi,c):
    n=len(pi)
    Q=np.zeros((n,n))
    for i in range(n-1):
        Q[i,i+1]=c[i]/pi[i]
        Q[i+1,i]=c[i]/pi[i+1]
    for i in range(n): Q[i,i]=-Q[i].sum()
    return Q


def check_semigroup():
    r=np.random.default_rng(24017)
    tests=0
    for n in range(3,12):
        for trial in range(80):
            pi=r.dirichlet(np.ones(n)*1.5)
            x=np.r_[0.,np.cumsum(np.exp(r.uniform(-0.8,0.8,n-1)))]
            c=np.exp(r.uniform(-2.,2.,n-1))
            t=np.exp(r.uniform(-5.,2.))
            Q=make_Q(pi,c)
            H=expm(t*Q)
            assert np.max(abs(Q@np.ones(n)))<1e-10
            assert np.max(abs(pi@Q))<1e-9
            assert np.max(abs(H@np.ones(n)-1))<2e-10
            assert np.max(abs(pi@H-pi))<2e-10
            # The full transport formula is independent of the monotone-potential shortcut.
            W=np.asarray(row_metric(H,x))
            E=np.asarray(means_metric(H,x))
            assert np.max(abs(W-E))<3e-9
            assert max(W)<max(barrier(pi,x))+3e-9
            tests+=1
    print('semigroup/transport/bound checks:',tests)


def check_singular_limits():
    r=np.random.default_rng(24042)
    trials=0
    for n in range(3,10):
        for attempt in range(6):
            pi=r.dirichlet(np.ones(n)*2.)
            x=np.r_[0.,np.cumsum(np.exp(r.uniform(-0.6,0.6,n-1)))]
            k=r.integers(0,n-1)
            B=barrier(pi,x)[k]
            vals=[]
            for eps in [1e-2,1e-5,1e-8]:
                c=np.ones(n-1);c[k]=eps
                t=eps**(-0.5)
                H=expm(t*make_Q(pi,c))
                vals.append(float(means_metric(H,x)[k]))
            assert abs(vals[-1]-B)<0.035+0.003*B,(n,k,vals,B)
            assert abs(vals[-1]-B)<=abs(vals[0]-B)+0.005
            trials+=1
    print('two-block singular limit checks:',trials)

if __name__=='__main__':
    check_exact()
    check_semigroup()
    check_singular_limits()
    print('ALL CHECKS PASSED')
