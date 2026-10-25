"""Independent finite-temperature checks for the fixed-field-norm XX dimer."""
import numpy as np
from scipy.linalg import expm
from scipy.optimize import minimize_scalar

X=np.array([[0,1],[1,0.]],dtype=complex)
Y=np.array([[0,-1j],[1j,0]],dtype=complex)
Z=np.diag([1.,-1.]); I=np.eye(2)
S=np.kron(Y,Y)

def direct(J,R,beta,B):
    b=np.sqrt(max(0.,R*R-B*B)); h1=B+b;h2=B-b
    H=J/2*(np.kron(X,X)+np.kron(Y,Y))+0.5*(h1*np.kron(Z,I)+h2*np.kron(I,Z))
    rho=expm(-beta*H);rho/=np.trace(rho)
    vals=np.linalg.eigvals(rho@S@rho.conj()@S)
    roots=np.sqrt(np.maximum(0,np.real(vals))); roots.sort()
    return max(0.,roots[-1]-sum(roots[:-1]))

def formula(J,R,beta,B):
    E=np.sqrt(J*J+R*R-B*B)
    a=np.exp(-beta*E)
    n=(J/E)*(1-a*a)-2*a
    d=1+a*a+np.exp(-beta*(E-B))+np.exp(-beta*(E+B))
    return max(0.,n/d)

def opt(J,R,beta):
    f=lambda B:-formula(J,R,beta,B)
    x=minimize_scalar(f,bounds=(0,R),method='bounded',options={'xatol':1e-13})
    pts=[(x.x,-x.fun),(0,formula(J,R,beta,0)),(R,formula(J,R,beta,R))]
    return max(pts,key=lambda z:z[1])

rng=np.random.default_rng(481903)
n=0
for _ in range(240):
    J=float(np.exp(rng.uniform(-1,1))); R=float(np.exp(rng.uniform(-1,1)))
    beta=float(np.exp(rng.uniform(-1,1)))
    B=float(rng.uniform(0,R))
    x=direct(J,R,beta,B); y=formula(J,R,beta,B)
    assert abs(x-y)<5e-8,(J,R,beta,B,x,y)
    n+=1
print('direct 4x4 Gibbs/concurrence comparisons:',n)
for J,R in [(1.,.65),(.5,.2),(2.,1.)]:
    for beta in [20.,50.,100.]:
        B,c=opt(J,R,beta)
        assert abs(B-R)<2e-7,(J,R,beta,B)
        n+=1
print('subcritical endpoint tests:',9)
for J,R in [(1.,1.),(1.,1.4),(.7,2.),(2.,2.1)]:
    tc=np.sqrt((J*J+R*R)/2)
    for beta in [100.,250.,500.]:
        B,c=opt(J,R,beta)
        epsilon=tc-B
        pred=np.log(2*beta*tc)/(2*beta)
        assert epsilon>0 and abs(epsilon/pred-1)<0.05,(J,R,beta,B,epsilon,pred)
        approx=J/tc*(1-(np.log(2*beta*tc)+1)/(2*beta*tc))
        assert abs(c-approx)<.006,(J,R,beta,c,approx)
        n+=2
print('critical/supercritical asymptotic tests:',24)
print('TOTAL assertions:',n)
