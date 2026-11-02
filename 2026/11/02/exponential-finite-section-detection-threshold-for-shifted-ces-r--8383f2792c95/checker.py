"""Finite exact-rational checks for a shifted Cesaro self-commutator calculation.

Run with Python 3.10 or newer: python checker.py
The analytic proof is required for the infinite-dimensional statements.
"""
from fractions import Fraction as F


def data(a, i):
    u = F(i+1) + a
    return 1/u, 1/(u*(u+1)), 1/(u*u*(u+1))


def dot(x, y):
    return sum((p*q for p,q in zip(x,y)), F(0))


def direct_difference_gram(a, i, j):
    # b_i=e_i-e_(i+1).  C b_i and C* b_i have finite support.
    m=max(i,j)+3
    u=[F(0)]*m; v=[F(0)]*m
    u[i]=1;u[i+1]=-1;v[j]=1;v[j+1]=-1
    def C(x):
        t=F(0);res=[]
        for k in range(m):
            t+=x[k];res.append(t*data(a,k)[0])
        return res
    def CT(x):
        return [sum((x[n]*data(a,n)[0] for n in range(j0,m)), F(0)) for j0 in range(m)]
    # Cx has zero tail; C*x is also finitely supported.
    return dot(C(u),C(v))-dot(CT(u),CT(v))


def rational_tail_bounds(a, N, M=250):
    # Infinite D_tail = sum_{i=N-1}^inf [u_i^2(u_i+1)]^-1.
    # f(u)<u^-3 and decreases.  The omitted tail is bounded by
    # the first omitted u^-3 plus integral of u^-3 beyond it.
    p=sum((data(a,k)[2] for k in range(N-1,N-1+M)),F(0))
    u=F(N)+a+M
    return p,p+1/u**3+1/(2*u*u)


def scalar_threshold_bounds(a, N):
    z=F(N)+a
    pre=sum((1/(F(i)+a+2) for i in range(N-1)),F(0))
    lo,hi=rational_tail_bounds(a,N)
    return pre+1/(z*z*hi),pre+1/(z*z*lo)


def check():
    count=0
    for a in [F(-3,4),F(-1,2),F(-1,4),F(-1,10),F(0),F(1,2)]:
        for i in range(7):
            for j in range(7):
                ai,gi,di=data(a,i)
                aj,gj,dj=data(a,j)
                target=(di if i==j else 0)+a*gi*gj
                assert direct_difference_gram(a,i,j)==target
                count+=1
        # Check rational identities for partial-sum form and exact
        # factorization on zero-total-support vectors.
        for N in range(2,8):
            for h in range(4):
                x=[F((i*i+3*h*i+1)%7-3) for i in range(N)]
                x.append(-sum(x))
                t=[];cum=F(0)
                for xi in x:
                    cum+=xi;t.append(cum)
                lhs=F(0)
                for i,xi in enumerate(x):
                    for j,xj in enumerate(x):
                        lhs+=xi*xj*direct_K_diff(a,i,j,len(x))
                rhs=sum((data(a,i)[2]*t[i]*t[i] for i in range(len(t))),F(0))
                rhs+=a*sum((data(a,i)[1]*t[i] for i in range(len(t))),F(0))**2
                assert lhs==rhs
                count+=1
    for a,N_before,N_after in [(F(-3,4),1,2),(F(-1,2),1,2),
                                (F(-1,4),9,10)]:
        _lo,up=scalar_threshold_bounds(a,N_before)
        low,_hi=scalar_threshold_bounds(a,N_after)
        assert (-a)*up<1 and (-a)*low>1
        count+=2
    print('PASS:',count,'finite exact-rational assertions')


def direct_K_diff(a,i,j,L):
    # K on zero-sum test vectors: the common infinite tail of C*C
    # cancels in the second differences, so use Gram identities.
    # b-difference coefficient basis: x=sum t_i b_i.
    # K_{ij} contains a common tail, but the combination against
    # the zero-sum x is well defined by any finite trailing tail.
    # A finite cutoff T>=L suffices for zero-sum x: each Cx has
    # finite support and C*x has finite support.
    T=L+1
    aa=[data(a,k)[0] for k in range(T)]
    return sum((aa[k]**2 for k in range(max(i,j),T)),F(0)) - (min(i,j)+1)*aa[i]*aa[j]


if __name__ == '__main__':
    check()
