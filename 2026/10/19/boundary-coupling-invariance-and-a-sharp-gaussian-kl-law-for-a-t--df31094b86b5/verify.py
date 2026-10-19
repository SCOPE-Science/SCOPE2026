"""Reproduce finite-dimensional covariance-compression identities.

Requires Python 3 and NumPy; optional SymPy verifies the symbolic determinant and trace identities.
All inputs are synthetic deterministic data. No external files or network calls.
"""
from math import log, sqrt
import numpy as np

def experiment(alpha,beta,a,b,c):
    A=np.array([[alpha,beta,0.0],[beta,a,c],[0.,c,b]])
    assert np.linalg.eigvalsh(A)[0]>0
    C=np.linalg.inv(A)
    R=b*b+c*c
    u=np.array([b,-c])/sqrt(R)
    v=np.array([c,b])/sqrt(R)
    Q=np.eye(3)
    Q[1:,1:]=np.stack((u,v),axis=1)
    C=Q.T@C@Q
    Chat=C.copy()
    Chat[1,2]=Chat[2,1]=0.0
    assert np.linalg.eigvalsh(Chat)[0]>0
    f=.5*(np.trace(np.linalg.solve(Chat,C))-3+np.linalg.slogdet(Chat)[1]-np.linalg.slogdet(C)[1])
    r=.5*(np.trace(np.linalg.solve(C,Chat))-3+np.linalg.slogdet(C)[1]-np.linalg.slogdet(Chat)[1])
    delta=c*c*(a*b-c*c)/R**2
    return C,Chat,delta,f,r

def main():
    rng=np.random.default_rng(20261014)
    n=0
    for _ in range(4500):
        lam1=float(np.exp(rng.uniform(-2,2)))
        kappa=float(np.exp(rng.uniform(0,4)))
        phi=float(rng.uniform(-1.56,1.56))
        co,si=np.cos(phi),np.sin(phi)
        U=np.array([[co,-si],[si,co]])
        T=U@np.diag([lam1,lam1*kappa])@U.T
        a,c,b=T[0,0],T[0,1],T[1,1]
        alpha=float(np.exp(rng.uniform(-1,1)))
        threshold=alpha*(a-c*c/b)
        beta=float(np.sqrt(threshold)*rng.uniform(.001,.999))
        C,Chat,delta,f,r=experiment(alpha,beta,a,b,c)
        assert abs(f-.5*log(1+delta))<2e-8
        assert abs(r-(delta-.5*log(1+delta)))<2e-8
        dmax=(kappa-1)**2/(4*kappa)
        assert delta <= dmax+1e-10
        n+=1
    for kappa in [1.1,2.,3.,10.,100.,1000.]:
        p=1/(kappa*kappa+1)
        a=1+(kappa-1)*(1-p)
        b=1+(kappa-1)*p
        c=(kappa-1)*sqrt(p*(1-p))
        delta=c*c*(a*b-c*c)/(b*b+c*c)**2
        assert abs(delta-(kappa-1)**2/(4*kappa))<1e-10
        n+=1
    for eps in [0.1,0.01,0.0001,1e-6]:
        C,Chat,d,f,r=experiment(1.,sqrt(.75-eps),1.,1.,.5)
        assert abs(d-.12)<1e-12
        assert abs(f-.5*log(1.12))<1e-7
        assert abs(r-(.12-.5*log(1.12)))<1e-7
        n+=1
    try:
        import sympy as sp
        alpha,a,b,c,h=sp.symbols('alpha a b c h',positive=True)
        A=sp.Matrix([[alpha,h,0],[h,a,c],[0,c,b]])
        Q=sp.Matrix([[1,0,0],[0,b,c],[0,-c,b]])
        X=Q.T*A.inv()*Q
        Xhat=sp.Matrix(X);Xhat[1,2]=Xhat[2,1]=0
        D=sp.factor(c*c*(a*b-c*c)/(b*b+c*c)**2)
        assert sp.simplify(Xhat.det()/X.det()-(1+D))==0
        assert sp.simplify((X.inv()*Xhat).trace()-(3+2*D))==0
        assert sp.simplify(X[0,2])==0
        n+=3
    except ImportError:
        print('Optional SymPy unavailable: symbolic checks skipped.')
    print('PASS:',n,'finite algebraic, spectral, KL and extremizer checks')
    print('Sharp kappa=3 bound: forward=',log(2/sqrt(3)),
          'reverse=',1/3-log(2/sqrt(3)))
    print('Fixed compressed T example: forward=',.5*log(1.12),
          'reverse=',.12-.5*log(1.12))

if __name__=='__main__':
    main()
