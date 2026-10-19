"""Reproduce algebra and finite ODE illustrations for FOAF constant responsiveness.
The mathematical classification is proved separately; finite tests are not its proof.
Requires Python 3 and numpy/scipy for optional integration.
"""
from fractions import Fraction as F
import random


def f_edge(W, i, j, c):
    n=len(W)
    prod=sum(W[i][k]*W[k][j] for k in range(n))
    z=W[i][j]
    return c*(z+prod/F(n))*(1-z)-(1-c)*z


def checks():
    random.seed(1816)
    exact=0
    for n in range(2,9):
        A=F(n+2,n); B=F(n-2,n)
        cc=F(n,2*(n+1))
        for ccandidate in [cc/F(2),cc,(cc+1)/F(2)]:
            r=ccandidate*F(2*n+2,n)-1
            for _ in range(40):
                W=[[F(1) if i==j else F(0) for j in range(n)] for i in range(n)]
                for i in range(n):
                    for j in range(i+1,n):
                        W[i][j]=W[j][i]=F(random.randint(0,15),16)
                m=max(W[i][j] for i in range(n) for j in range(i+1,n))
                top=r*m-F(4,n)*ccandidate*m*m-ccandidate*B*m*m*m
                for i in range(n):
                    for j in range(i+1,n):
                        z=W[i][j]
                        deriv=f_edge(W,i,j,ccandidate)
                        lower=r*z-ccandidate*A*z*z
                        assert deriv>=lower
                        if z==m: assert deriv<=top
                        exact+=1
                assert r==0 if ccandidate==cc else (r<0 if ccandidate<cc else r>0)
        # Complete-graph critical reduction, including the first quadratic correction
        assert A-B==F(4,n)
        assert cc*F(2*n+2,n)==1
    print('Exact algebraic comparisons:',exact)
    try:
        import numpy as np
        from scipy.integrate import solve_ivp
    except ImportError:
        print('Optional scipy unavailable; exact checks complete.')
        return
    illustrations=0
    for n in [2,3,5]:
        cc=n/(2*(n+1))
        for ratio in [0.7,1.0,1.2]:
            c=cc*ratio
            W=np.eye(n)
            for i in range(n-1):W[i,i+1]=W[i+1,i]=0.65
            x=np.linspace(-0.7,0.7,n)
            initial=np.r_[x,W[np.triu_indices(n,1)]]
            iu=np.triu_indices(n,1)
            def rhs(t,y):
                X=y[:n]; M=np.eye(n);M[iu]=y[n:];M[(iu[1],iu[0])]=y[n:]
                deg=M.sum(axis=1)
                dX=c*(M@(X)-deg*X)/deg
                MM=M@M
                dM=c*(M+MM/n)*(1-M)-(1-c)*M
                return np.r_[dX,dM[iu]]
            end=1200 if ratio==1 else 150
            ans=solve_ivp(rhs,(0,end),initial,rtol=2e-9,atol=2e-11)
            assert ans.success
            endw=ans.y[n:,-1]; d0=max(x)-min(x);df=max(ans.y[:n,-1])-min(ans.y[:n,-1])
            if ratio<1:
                assert max(endw)<1e-6
                assert df>0.01*d0
            elif ratio>1:
                assert df<1e-5
                assert max(endw)>0.01
            else:
                assert max(endw)<0.05
                assert df<0.1*d0
            if n==2 and ratio==1:
                w0=.65; a=2*c*w0/(1+w0)
                assert abs(endw[0]-w0/(1+2*c*w0*end))<2e-7
                assert abs(df-d0/(1+a*end))<2e-7
            illustrations+=1
    print('Independent full-ODE integrations:',illustrations)


if __name__=='__main__':checks()
