"""Independent finite comparisons for the population exceptional-point theorem.

Dependencies: numpy and scipy. Analytic proof, not these finite experiments,
controls the universal parameter classification.
"""
import numpy as np
from scipy.linalg import expm
from math import sqrt

count=0

def check(c):
    global count
    assert c, f'failed check {count+1}'
    count+=1

A=np.array([[0,1,0],[0,0,sqrt(2)],[0,0,0]],complex)
C=A.conj().T
X=(A+C)/sqrt(2)
J=X@A
H=np.diag([0,1,2]);I3=np.eye(3)

def dissipator(L):
    K=L.conj().T@L
    return np.kron(L.conj(),L)-.5*(np.kron(I3,K)+np.kron(K.T,I3))

def population(a,b):
    return np.array([[-a,0,b],[a,-2*a,0],[0,2*a,-b]],float)

def full_liouvillian(a,b):
    return -1j*(np.kron(I3,H)-np.kron(H.T,I3))+a*dissipator(C)+b*dissipator(J)

def get_pop(vec):
    return np.real(vec[[0,4,8]])

def formula(a,b,t):
    K=population(a,b)
    pi=np.array([2*b,b,2*a])/(2*a+3*b)
    Pi=np.outer(pi,np.ones(3));Q=np.eye(3)-Pi
    m=(3*a+b)/2
    delta=a*a-6*a*b+b*b
    B=K+m*Q
    if delta>1e-10:
        omega=sqrt(delta)/2
        return Pi+np.exp(-m*t)*(np.cosh(omega*t)*Q+np.sinh(omega*t)/omega*B)
    if delta< -1e-10:
        omega=sqrt(-delta)/2
        return Pi+np.exp(-m*t)*(np.cos(omega*t)*Q+np.sin(omega*t)/omega*B)
    return Pi+np.exp(-m*t)*(Q+t*B)

for b in (.05,.5,1,2.3,8.):
    ratios=[.02,.1, 3-2*sqrt(2), .5,1,3,3+2*sqrt(2),7.,10.,50.]
    for ratio in ratios:
        a=b*ratio; K=population(a,b);G=full_liouvillian(a,b)
        pi=np.array([2*b,b,2*a])/(2*a+3*b)
        check(np.linalg.norm(K@pi)<1e-10)
        # Projection to populations intertwines the exact Lindbladian.
        for u in range(9):
            v=np.eye(9,dtype=complex)[:,u]
            check(np.max(np.abs(get_pop(G@v)-K@get_pop(v)))<3e-13)
        ev=np.linalg.eigvals(K)
        m=(3*a+b)/2;delta=a*a-6*a*b+b*b
        target=np.array([0, -m+np.sqrt(complex(delta))/2,-m-np.sqrt(complex(delta))/2])
        check(all(min(abs(v-w) for w in target)<max(2e-6,1e-8*abs(v)) for v in ev))
        for t in (0,.01,.1,.4,1,3):
            check(np.max(np.abs(expm(K*t)-formula(a,b,t)))<2e-10)
            R=expm(G*t)
            for p in range(3):
                rho=np.zeros((3,3),complex);rho[p,p]=1
                exact=get_pop(R@rho.reshape(9,order='F'))
                check(np.max(np.abs(exact-expm(K*t)[:,p]))<4e-11)
        if abs(delta)<1e-10:
            Q=np.eye(3)-np.outer(pi,np.ones(3)); N=K+m*Q
            check(np.linalg.norm(N)>1e-5)
            check(np.linalg.norm(N@N)<2e-10)
            # geometric multiplicity one at the repeated eigenvalue
            check(np.linalg.matrix_rank(K+m*np.eye(3),tol=1e-8)==2)
        else:
            check((delta<0)==(3-2*sqrt(2)<ratio<3+2*sqrt(2)))
print(f'PASS {count} finite checks')
