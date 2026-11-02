"""Independent symbolic and full-state checks for a bipartite quantum capture law.

Run: python proof_check.py
Requires: sympy, numpy, scipy.
"""
import numpy as np
import sympy as sp
from scipy.linalg import solve
from scipy.optimize import brentq


def symbolic_certificate():
    a,b,g,k,J=sp.symbols('a b g k J',positive=True)
    t=sp.symbols('t',nonnegative=True)
    N=a+b+1
    c=(1-t)/(N-1)
    P=1/k
    Y=-(N-1)*c/(2*J*b)
    Z=c/(2*J*b)
    U=V=-c/g
    X=(N-2)*c/(2*g+k)
    R=P+a*X-(b-1)*V-(g+k/2)*Y/J
    Q=R-(a-1)*U-X+(b-1)*V+g*Z/J
    rhs=[-k*P-2*J*b*Y,
         -2*J*b*Z,
         2*J*(Y+a*Z),
         -J*b*(Y+Z)-(g+k/2)*X,
         J*(P+a*X-R-(b-1)*V)-(g+k/2)*Y,
         J*(Q+(a-1)*U+X-R-(b-1)*V)-g*Z,
         -2*J*b*Z-g*U,
         2*J*(Y+a*Z)-g*V]
    init=[t,c,c]+[0]*5
    for index,(val,initial) in enumerate(zip(rhs,init)):
        assert sp.cancel(val+initial)==0,(index,sp.factor(val+initial))
    A=((N-1)**2+a)/(2*J**2*b)
    B=a*(a-1)+b*(b-1)
    C=a*(N-2)**2
    formula=N/k+c*(k*(N-1)**2/(4*J**2*b)+A*g+B/g+C/(2*g+k))
    assert sp.cancel(P+a*Q+b*R-formula)==0
    assert sp.cancel(sp.diff(formula,g)-c*(A-B/g**2-2*C/(2*g+k)**2))==0
    assert sp.cancel(sp.diff(formula,g,2)-c*(2*B/g**3+8*C/(2*g+k)**3))==0
    print('Symbolic integrated-equation and convexity identities: PASS (11 exact identities).')


def full_state_time(m,n,J,k,g,initial_sink_weight):
    N=m+n
    H=np.zeros((N,N))
    H[:m,m:]=J
    H[m:,:m]=J
    eye=np.eye(N)
    Li=-1j*(np.kron(eye,H)-np.kron(H.T,eye))
    for v in range(N):
        for u in range(N):
            ix=u+N*v
            if u!=v: Li[ix,ix]-=g
            if u==0: Li[ix,ix]-=k/2
            if v==0: Li[ix,ix]-=k/2
    initial_matrix=(1-initial_sink_weight)/(N-1)*(eye-np.diag([1]+[0]*(N-1)))
    initial_matrix[0,0]=initial_sink_weight
    initial=initial_matrix.reshape(N*N,order='F')
    integral=solve(-Li,initial)
    integ=integral.reshape((N,N),order='F')
    return np.trace(integ).real,float(np.linalg.norm(Li@integral+initial,ord=np.inf))


def closed_time(m,n,J,k,g,initial_sink_weight):
    a=m-1;b=n;N=m+n
    A=((N-1)**2+a)/(2*J**2*b*N)
    B=(a*(a-1)+b*(b-1))/N
    C=a*(N-2)**2/N
    return N/k+(1-initial_sink_weight)*N/(N-1)*(k*(N-1)**2/(4*J**2*b*N)+A*g+B/g+C/(2*g+k))


def numerical_tests():
    tests=0;worst=0.0;resmax=0.0
    for m,n in [(2,2),(2,3),(2,5),(3,2),(3,3),(3,4),(4,2),(4,3),(5,2)]:
        for J,k,g in [(1.,1.,1.),(0.7,2.3,0.45),(1.4,0.2,3.1)]:
            for t in (0.,0.35,1./(m+n),1.):
                observed,residual=full_state_time(m,n,J,k,g,t)
                expected=closed_time(m,n,J,k,g,t)
                err=abs(observed-expected)/max(1.,abs(expected))
                worst=max(worst,err);resmax=max(resmax,residual)
                assert err<1e-10,(m,n,J,k,g,t,err)
                assert residual<1e-11,(m,n,J,k,g,t,residual)
                tests+=1
    print(f'Independent full-state Lindblad linear solves: PASS ({tests} cases, max relative error {worst:.3g}, max residual {resmax:.3g}).')


def optimum_tests():
    tests=0
    for m,n in [(2,2),(2,5),(3,3),(4,2),(5,4)]:
        a=m-1;b=n;N=m+n;J=1.
        A=((N-1)**2+a)/(2*J**2*b*N)
        B=(a*(a-1)+b*(b-1))/N
        C=a*(N-2)**2/N
        low=np.sqrt(B/A);high=np.sqrt((B+C/2)/A)
        prev=high
        for k in (0.02,0.1,1.,10.,100.,1000.):
            f=lambda g:A-B/g**2-2*C/(2*g+k)**2
            root=brentq(f,low,high,xtol=1e-13)
            assert low<root<high
            assert root<prev
            assert f(root/1.2)<0<f(root*1.2)
            prev=root;tests+=1
    print(f'Unique-root brackets and strict trap-strength monotonicity: PASS ({tests} cases).')

if __name__=='__main__':
    symbolic_certificate()
    numerical_tests()
    optimum_tests()
