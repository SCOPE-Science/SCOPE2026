"""Reproduce the weighted-book D-optimal design calculations.

Requires numpy and scipy. Execute: python verify.py
"""
import math
import random
from fractions import Fraction

import numpy as np
from scipy.optimize import minimize


def closed_form(m, P, Q, R, B):
    """Return x, y, z and regime, with m>=3 and all prices/B positive."""
    if P >= Q + R:
        return 0.0, B / ((m + 1) * Q), B / ((m + 1) * R), "first_spoke_absent"
    if Q >= P + R:
        return B / ((m + 1) * P), 0.0, B / ((m + 1) * R), "second_spoke_absent"
    d = Q-P
    rr = (m * d + math.sqrt(m * m * d * d + 4 * P * Q)) / (2 * P)
    # More stable if Q<P and the direct root subtracts near-equal values.
    if d < 0:
        rr = 2 * Q / (math.sqrt(m*m*d*d + 4*P*Q) - m*d)
    Rc = (P * rr + Q) * (rr + 1) / ((m + 1) * rr)
    if R >= Rc:
        y = B / (m * (P * rr + Q))
        return rr * y, y, 0.0, "backbone_absent"
    s = (1 + (Q-P)/R) / 2
    t = B / ((m+1) * (P - R*(1-s)**2))
    z = B / ((m+1)*R) - m*s*(1-s)*t
    assert s > 0 and s < 1 and z > 0, (m,P,Q,R,s,z,Rc)
    return s*t, (1-s)*t, z, "all_positive"


def det_reduced(m, xx, yy, zz):
    # Ground vertex 1 (the second hub). Vertex 0 is the first hub.
    g = np.zeros((m + 1, m + 1))
    def add(i, j, w):
        if i >= 0: g[i, i] += w
        if j >= 0: g[j, j] += w
        if i >= 0 and j >= 0: g[i,j] -= w; g[j,i] -= w
    add(0,-1,zz)
    for i in range(m):
        add(0,i+1,xx[i]);add(-1,i+1,yy[i])
    return float(np.linalg.det(g))


def tau(m,x,y,z):
    return (x+y)**(m-1) * (m*x*y + z*(x+y))


def grad_log_tau(m,x,y,z):
    t=x+y; d=m*x*y+z*t
    return ((m-1)/t+(m*y+z)/d,
            (m-1)/t+(m*x+z)/d,
            t/d)


def check_rational_examples():
    from fractions import Fraction as F
    m=3; B=F(92);P=F(2);Q=F(1);R=F(3,2)
    x,y,z=F(4),F(20),F(16,3)
    assert m*(P*x+Q*y)+R*z==B
    assert (x+y)**(m-1)*(m*x*y+z*(x+y)) == F(211968)
    m=3;B=F(8);P=Q=F(1);R=F(1,2)
    x=y=F(8,7);z=F(16,7)
    assert m*(P*x+Q*y)+R*z==B
    assert (x+y)**(m-1)*(m*x*y+z*(x+y))==F(16384,343)
    for m in range(3,10):
        for a,b,c in [(2,3,1),(3,2,4),(1,3,5),(5,1,6)]:
            x,y,z=F(a),F(b),F(c)
            N=m+1
            mat=[[F(0) for _ in range(N)] for _ in range(N)]
            def edge(i,j,w):
                if i>=0: mat[i][i]+=w
                if j>=0: mat[j][j]+=w
                if i>=0 and j>=0:mat[i][j]-=w;mat[j][i]-=w
            edge(0,-1,z)
            for i in range(m):edge(0,i+1,x);edge(-1,i+1,y)
            # Exact elimination over rational numbers.
            determinant=F(1)
            for k in range(N):
                pivot=mat[k][k]
                assert pivot>0
                determinant*=pivot
                for i in range(k+1,N):
                    f=mat[i][k]/pivot
                    for j in range(k+1,N):mat[i][j]-=f*mat[k][j]
            assert determinant == (x+y)**(m-1)*(m*x*y+z*(x+y))
    return 28


def check_random():
    rng=random.Random(1729)
    regimes=set()
    checks=0; detchecks=0; optimchecks=0; asymmetric_checks=0
    for i in range(320):
        m=rng.randint(3,9)
        P=10**rng.uniform(-1,1); Q=10**rng.uniform(-1,1)
        R=10**rng.uniform(-1.5,1.5);B=10**rng.uniform(-1,1)
        x,y,z,regime=closed_form(m,P,Q,R,B)
        regimes.add(regime)
        assert x>=0 and y>=0 and z>=0
        assert abs(m*(P*x+Q*y)+R*z-B)<B*1e-9
        D=tau(m,x,y,z)
        assert D>0
        g=grad_log_tau(m,x,y,z)
        lam=(m+1)/B
        for weight, marginal, price in [(x,g[0],m*P),(y,g[1],m*Q),(z,g[2],R)]:
            assert marginal<=lam*price+1e-7*(1+lam*price)
            if weight>1e-8:
                assert abs(marginal-lam*price)<=1e-7*(1+lam*price)
        checks+=1
        if i<160:
            val=det_reduced(m,[x]*m,[y]*m,z)
            assert abs(val/D-1)<1e-9
            detchecks+=1
        if i<45:
            n=2*m+1
            edge_prices=np.array([P]*m+[Q]*m+[R])
            optvec=np.array([x]*m+[y]*m+[z])
            def objective(vec):
                val=det_reduced(m,vec[:m],vec[m:2*m],vec[-1]);
                if val<=0:return 1e6
                return -math.log(val)
            # Fully unrestricted all edges; L-BFGS-B on expenditure simplex
            # with scipy SLSQP, random positive feasible initialization.
            init=np.array([0.2+rng.random() for _ in range(n)])
            init=init*B/float(init@edge_prices)
            fit=minimize(objective,init,method='SLSQP',bounds=[(0,None)]*n,
                    constraints=[{'type':'eq','fun':lambda v: v@edge_prices-B}],
                    options={'ftol':1e-10,'maxiter':300})
            if fit.success:
                assert objective(fit.x)>=objective(optvec)-1e-6, (i,fit.fun,objective(optvec))
                optimchecks+=1
        for j in range(8):
            raw=np.array([rng.random()+.01 for _ in range(2*m+1)])
            raw*=B/(np.dot(raw,np.array([P]*m+[Q]*m+[R])))
            val=det_reduced(m,raw[:m],raw[m:2*m],raw[-1])
            assert val/D<=1+2e-9
            asymmetric_checks+=1
    assert regimes=={'first_spoke_absent','second_spoke_absent','backbone_absent','all_positive'}
    return checks,detchecks,optimchecks,asymmetric_checks

if __name__=='__main__':
    ec=check_rational_examples()
    cs=check_random()
    print(f'PASS exact rational determinant cases={ec}; random KKT/budget cases={cs[0]};')
    print(f'PASS spectral determinant cases={cs[1]}; unrestricted optimizer comparisons={cs[2]};')
    print(f'PASS asymmetric feasible allocation comparisons={cs[3]}; all four regimes observed')
