"""Reproduce the reset-count mixture calculation for a stochastically gated target.
Requires numpy, scipy and sympy. These finite checks supplement, not replace, the proof.
"""
import math
import numpy as np
import sympy as sp
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve


def kernel(alpha,beta,r,D,x):
    p=beta/(alpha+beta); q=1-p; t=r/(r+alpha+beta)
    k=math.sqrt(r/D); h=math.sqrt((r+alpha+beta)/r)
    f0=alpha*(h*math.exp(-k*x)-math.exp(-k*h*x))/(beta+alpha*h)
    f1=(alpha*h*math.exp(-k*x)+beta*math.exp(-k*h*x))/(beta+alpha*h)
    P=np.array([[p+t*q,q*(1-t)],[p*(1-t),q+t*p]])
    K=(np.eye(2)-np.outer([f0,f1],[0.,1.]))@P
    return K,P,p,t,f0,f1


def finite_difference_kernel(alpha,beta,r,D,x0,L=12.,points=401):
    # Solve (r I-Q)U-D U''=r I, open state Dirichlet and closed state Neumann at 0,
    # approximate bounded half-line by Neumann at the far boundary.
    h=L/(points-1); rows=2*points
    Q=np.array([[-alpha,alpha],[beta,-beta]])
    A=lil_matrix((rows,rows),dtype=float);B=np.zeros((rows,2))
    idx=lambda i,s:2*i+s
    for i in range(points):
        for state in (0,1):
            j=idx(i,state)
            if i==0 and state==1:
                A[j,j]=1.
                continue
            if i==0 or i==points-1:
                near=1 if i==0 else points-2
                A[j,j]=1.
                A[j,idx(near,state)]=-1.
                continue
            A[j,j]=r-Q[state,state]+2*D/h**2
            A[j,idx(i-1,state)]=-D/h**2
            A[j,idx(i+1,state)]=-D/h**2
            A[j,idx(i,1-state)]=-Q[state,1-state]
            B[j,state]=r
    U=np.column_stack([spsolve(A.tocsr(),B[:,j]) for j in (0,1)])
    nearest=int(round(x0/h))
    return U[[idx(nearest,0),idx(nearest,1)],:]


def run():
    p,t,f0,f1=sp.symbols('p t f0 f1',positive=True)
    q=1-p
    P=sp.Matrix([[p+t*q,q*(1-t)],[p*(1-t),q+t*p]])
    K=(sp.eye(2)-sp.Matrix([f0,f1])*sp.Matrix([[0,1]]))*P
    pi=sp.Matrix([[p,q]])
    fbar=p*f0+q*f1
    s=(pi*K*sp.ones(2,1))[0]
    assert sp.factor(s-(1-fbar))==0
    assert sp.factor(K.det()-t*(1-f1))==0
    assert sp.factor((sp.eye(2)-K).det()-(1-t)*fbar)==0
    assert sp.factor((s*sp.eye(2)-K).det()+p*t*(f1-f0)*fbar)==0
    m=(pi*(sp.eye(2)-K).inv()*K*sp.ones(2,1))[0]
    assert sp.factor(m-(1-t+t*f1-fbar)/((1-t)*fbar))==0
    R=(sp.eye(2)-K).inv()
    second_fact=2*(pi*R*K*R*K*sp.ones(2,1))[0]
    discrepancy=sp.factor((m+second_fact-m*m)-m*(1+m))
    assert sp.factor(discrepancy-2*p*t*(f1-f0)/((1-t)**2*fbar))==0
    ntests=6
    rng=np.random.default_rng(551)
    for _ in range(1500):
        alpha,beta,r,D=np.exp(rng.uniform(-1.4,1.4,4))
        dimensionless_x=rng.uniform(.2,1.5)
        x=dimensionless_x*math.sqrt(D/r)
        K,P,p,t,f0,f1=kernel(alpha,beta,r,D,x)
        pi=np.array([p,1-p]); fbar=p*f0+(1-p)*f1
        assert 0<f0<f1<1
        assert np.all(K>0) and np.all(K.sum(axis=1)<1)
        assert np.allclose(K.sum(axis=1),[1-f0,1-f1],rtol=2e-13,atol=1e-13)
        ev=np.linalg.eigvals(K)
        l1,l2=sorted(ev,reverse=True)
        s=float(pi@K@np.ones(2))
        assert 0<l2<s<l1<1
        w1=(s-l2)/(l1-l2);w2=1-w1
        assert min(w1,w2)>0
        assert np.isclose(w1+w2,1)
        for n in (0,1,2,5,9):
            survival=float(pi@np.linalg.matrix_power(K,n)@np.ones(2))
            mixture=w1*l1**n+w2*l2**n
            assert math.isclose(survival,mixture,rel_tol=3e-11,abs_tol=3e-11)
            ntests+=1
        means=np.array([l1/(1-l1),l2/(1-l2)])
        mean_mix=w1*means[0]+w2*means[1]
        m=(1-t+t*f1-fbar)/((1-t)*fbar)
        assert math.isclose(mean_mix,m,rel_tol=3e-10,abs_tol=3e-10)
        delta=2*p*t*(f1-f0)/((1-t)**2*fbar)
        delta_mix=2*w1*w2*(means[0]-means[1])**2
        assert delta>0 and math.isclose(delta,delta_mix,rel_tol=2e-9,abs_tol=2e-9)
        ntests+=11
    samples=[(.5,2.,1.,1.,1.),(2.,.3,1.4,.8,1.1),(.25,.8,.6,1.1,1.6)]
    for alpha,beta,r,D,x in samples:
        K=kernel(alpha,beta,r,D,x)[0]
        val=finite_difference_kernel(alpha,beta,r,D,x,L=20.,points=801)
        # x approximated to nearest grid point (<=.0125 absolute positional error).
        assert np.allclose(K,val,rtol=.035,atol=.006),(K,val)
        ntests+=4
    print('PASS: symbolic equalities, 1500 parameter suites, finite-difference resolvent comparisons')
    print('assertion groups:',ntests)

if __name__=='__main__':run()
