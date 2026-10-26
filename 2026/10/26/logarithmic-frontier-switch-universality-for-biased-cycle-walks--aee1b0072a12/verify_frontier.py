"""Independent finite-state checks for frontier-switch claims.

This code is a mathematical verification aid, not a proof of asymptotic results.
Run: python verify_frontier.py
"""
from collections import defaultdict
from fractions import Fraction as F
from math import prod, isclose, log, sqrt


def gambler_boundary(m, p):
    """Solve the finite tridiagonal Dirichlet problem by rational elimination.

    States 1,...,m are the visited interval with absorbing sites 0,m+1.
    Return P(exit right | start at 1), P(exit left | start at m).
    """
    q=1-p
    # A * h = b, with h_i = p*h_(i+1)+q*h_(i-1)
    a=[[F(int(i==j)) - (p if j==i+1 else F(0)) - (q if j==i-1 else F(0)) for j in range(m)] for i in range(m)]
    b=[F(0)]*(m-1)+[p]
    # Gauss-Jordan elimination
    for i in range(m):
        pivot=a[i][i]
        assert pivot
        for j in range(i,m):a[i][j]/=pivot
        b[i]/=pivot
        for k in range(m):
            if k==i: continue
            mult=a[k][i]
            if mult:
                for j in range(i,m):a[k][j]-=mult*a[i][j]
                b[k]-=mult*b[i]
    return b[0],1-b[-1]


def frontier_dp(n,p,independent_linear=False):
    # state: last side R=1 L=-1, switch count
    d={(1,0):p,(-1,0):1-p}
    for m in range(2,n):
        if independent_linear:
            b,a=gambler_boundary(m,p)
        else:
            r=(1-p)/p
            if r==1:a=b=F(1,m+1)
            else:
                s=sum(r**j for j in range(m+1))
                b=1/s;a=r**m/s
        nd=defaultdict(F)
        for (side,k),mass in d.items():
            if side==1:
                nd[(1,k)]+=mass*(1-a)
                nd[(-1,k+1)]+=mass*a
            else:
                nd[(-1,k)]+=mass*(1-b)
                nd[(1,k+1)]+=mass*b
        d=nd
    ans=defaultdict(F)
    for (_,k),pr in d.items():ans[k]+=pr
    assert sum(ans.values())==1
    return dict(ans)


def raw_path_dp(n,p,horizon):
    # Raw random-walk steps, no gambler's ruin or frontier transition formulas.
    d={(1,0,0,0):F(1)}  # visited length, position from leftmost, last side (0 undefined), switches
    terminal=defaultdict(F)
    for t in range(horizon):
        nd=defaultdict(F)
        for (m,x,side,k),v in d.items():
            for direction,pr in ((1,p),(-1,1-p)):
                nx=x+direction
                nm=m; ns=side;nk=k
                if nx==-1:
                    nm=m+1;nx=0;ns=-1
                    if side!=0 and side!=-1:nk+=1
                elif nx==m:
                    nm=m+1;ns=1
                    if side!=0 and side!=1:nk+=1
                if nm==n:terminal[nk]+=v*pr
                else:nd[(nm,nx,ns,nk)]+=v*pr
        d=nd
    rem=sum(d.values())
    return dict(terminal),rem


def symmetric_pg(n):
    p=[F(1)]
    for j in range(3,n+1):
        q=[F(0)]*(len(p)+1)
        for i,v in enumerate(p):
            q[i]+=v*F(j-1,j)
            q[i+1]+=v*F(1,j)
        p=q
    return dict(enumerate(p))


def checks():
    checks=0
    for n in range(3,10):
        for p in [F(1,3),F(1,2),F(2,3),F(3,4)]:
            left=frontier_dp(n,p)
            right=frontier_dp(n,p,True)
            assert left==right,(n,p,left,right)
            checks+=len(left)
            if p==F(1,2):
                assert left==symmetric_pg(n)
                checks+=len(left)
    # Independent raw path enumeration via exact rational transition propagation,
    # with explicit residual probability bound, rather than pretending a truncation is exact.
    for n in range(3,7):
        for p in [F(1,3),F(1,2),F(2,3)]:
            exact=frontier_dp(n,p)
            seen,rem=raw_path_dp(n,p,400)
            assert rem<F(1,10**12),(n,p,rem)
            assert all(F(0)<=exact.get(k,0)-seen.get(k,0)<=rem for k in exact)
            checks+=len(exact)
    # The analytic geometric estimates on each step's switch probabilities.
    for theta in [0.001,0.01,0.1,0.35,0.5,1.0,1.5,3.0]:
        from math import exp
        r=exp(-theta)
        M=int(1/theta)
        for m in range(2,min(20000,M)+1):
            S=sum(r**j for j in range(m+1)) if m<2000 else (1-r**(m+1))/(1-r)
            a=r**m/S;b=1/S;w=1/(m+1)
            assert abs(a-w)<=2.718282*theta*(1+1e-10)
            assert abs(b-w)<=1.359142*theta*(1+1e-10)
            checks+=2
    print('PASS exact and analytic-bound checks:',checks)
    print('Symmetric n=6 probability distribution:',symmetric_pg(6))
    for n,theta in [(100,0),(1000,.001),(10000,.001),(10000,.00001)]:
        M=min(n-1, int(1/theta) if theta else n-1)
        print('n,theta,benchmark mean, log effective size:',n,theta,round(sum(1/(m+1) for m in range(2,M+1)),7),round(log(min(n,1/theta) if theta else n),7))
if __name__=='__main__':checks()
