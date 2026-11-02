"""Independent finite-degree checks for an explicit varying Sobolev OPUC family.

Python 3 standard library only. Finite tests supplement the analytic proof.
"""
from fractions import Fraction as F
from math import sqrt

def solve(A, b):
    """Dense exact Gaussian elimination for independent Gram-matrix test."""
    n=len(b)
    x=[[F(v) for v in A[i]]+[F(b[i])] for i in range(n)]
    for i in range(n):
        j=next(k for k in range(i,n) if x[k][i])
        x[i],x[j]=x[j],x[i]
        fac=x[i][i]
        x[i]=[v/fac for v in x[i]]
        for k in range(n):
            if k!=i:
                fac=x[k][i]
                x[k]=[x[k][h]-fac*x[i][h] for h in range(n+1)]
    return [x[i][-1] for i in range(n)]

def gram(n, lam, c):
    return [[(F(i==j)+(lam*F(i*j,n*n)*(F(i==j)+c*F(abs(i-j)==1))))
             for j in range(n+1)] for i in range(n+1)]

def coefficients(n, lam, c):
    G=gram(n,lam,c)
    y=solve([row[:n] for row in G[:n]],[-G[j][n] for j in range(n)])
    return y+[F(1)]

def test_exact():
    for lam,c,rho in [(F(1),F(5,13),F(1,5)), (F(2),F(6,17),F(1,4))]:
        assert 0<c<F(1,2)
        delta=lam*c*(1/rho-rho)
        assert (1+lam)*rho==lam*c*(1+rho*rho)
        a=-1/delta
        b=1-(1+lam)/(delta*delta)
        for n in range(2,13):
            co=coefficients(n,lam,c)
            assert co[0]==0 and co[n]==1
            u=[(-1)**k*co[n-k] for k in range(n)]
            assert u[0]==1
            for k in range(1,n):
                x=F(n-k,n)
                left=(1+lam*x*x)*u[k]
                left-=lam*c*x*F(n-k+1,n)*u[k-1]
                if k<n-1:
                    left-=lam*c*x*F(n-k-1,n)*u[k+1]
                assert left==0,(lam,c,n,k)
            # First-order analytic ansatz: exact residual must have no 0th/1st powers in 1/n.
            for k in range(1,n):
                v=lambda l:rho**l*(1+(a*l*l+b*l)/n)
                x=F(n-k,n)
                residual=(1+lam*x*x)*v(k)-lam*c*x*F(n-k+1,n)*v(k-1)
                if k<n-1:
                    residual-=lam*c*x*F(n-k-1,n)*v(k+1)
                # The computed residual is O(n^-2) uniformly; tested here to a fixed coarse envelope.
                assert abs(residual)<F(50,n*n)
        # convergence at n=300 tested independently by Thomas solver.
        n=300
        dia=[1+float(lam)*(j/n)**2 for j in range(1,n)]
        off=[-float(lam*c)*(j*(j+1)/n**2) for j in range(1,n-1)]
        rhs=[0.0]*(n-1)
        rhs[-1]=-float(lam*c)*(n-1)/n  # equation at j=n-1 coupled to known p_n=1
        for j in range(1,n-1):
            fac=off[j-1]/dia[j-1]
            dia[j]-=fac*off[j-1]
            rhs[j]-=fac*rhs[j-1]
        v=[0.0]*(n-1)
        v[-1]=rhs[-1]/dia[-1]
        for j in range(n-3,-1,-1):
            v[j]=(rhs[j]-off[j]*v[j+1])/dia[j]
        u1=-v[-1]
        expected=float(rho)*(1+float(a+b)/n)
        assert abs(u1-expected)<1.0/n**2,(u1,expected)
        assert abs(-v[-1]-float(rho))<1.0/n
        print('EXACT_OK', str(lam), str(c), 'n=2..12', 'rho',rho,'delta',delta)
    print('FINITE_CHECKS_OK')

if __name__=='__main__':
    test_exact()
