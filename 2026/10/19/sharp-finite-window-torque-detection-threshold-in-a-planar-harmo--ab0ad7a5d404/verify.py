"""Deterministic independent numerical checks for planar OU drift-torque formulas.
Run with Python 3, NumPy and SciPy (versions are not essential for the identities).
"""
import numpy as np
from scipy.linalg import solve_continuous_lyapunov, expm
from scipy.integrate import quad
from scipy.special import k0e

checks=0

def close(a,b,rtol=2e-10,atol=1e-11):
    global checks
    if not np.allclose(a,b,rtol=rtol,atol=atol):
        raise AssertionError((a,b))
    checks+=1

def require(cond):
    global checks
    if not cond: raise AssertionError('condition failed')
    checks+=1

# Use the Cartesian drift and solve its Lyapunov equation; no normal-mode
# stationary covariance is assumed in these comparison calculations.
for theta in [0.1,0.37,0.82,1.24,2.1]:
    co,si=np.cos(theta),np.sin(theta)
    U=np.array([[co,-si],[si,co]])
    for l1,l2 in [(0.25,1.6),(1.0,3.0),(0.8,0.95)]:
        for d1,d2,rhoD in [(2.,0.3,0.2),(0.4,2.,-0.5),(1.8,1.1,0.85)]:
            A=U@np.diag([l1,l2])@U.T
            R=np.array([[d1,rhoD*np.sqrt(d1*d2)],[rhoD*np.sqrt(d1*d2),d2]])
            S=solve_continuous_lyapunov(A,2*R)
            St=U.T@S@U
            B=np.array([[0,1],[1,0]])
            # Quadratic-form matrix: x_1(-Ax)_2-x_2(-Ax)_1=x^T K x
            K=np.array([[-A[1,0],(A[0,0]-A[1,1])/2],
                        [(A[0,0]-A[1,1])/2,A[0,1]]])
            delta=l1-l2
            v1,v2,c=St[0,0],St[1,1],St[0,1]
            mean_matrix=np.trace(K@S)
            variance_matrix=2*np.trace(K@S@K@S)
            mean_eigen=delta*c
            variance_eigen=delta**2*(v1*v2+c*c)
            close(mean_matrix,mean_eigen)
            close(variance_matrix,variance_eigen)
            alpha=2*np.sqrt(l1*l2)/(l1+l2)
            require(c*c/(v1*v2)<alpha*alpha+1e-12)
            require(mean_matrix**2/variance_matrix<alpha**2/(1+alpha**2)+1e-12)
            for t in [0.,0.2,1.,3.]:
                # Wick's theorem for two different time blocks:
                # Cov(x_0^TKx_0,x_t^TKx_t)=2 Tr(K C_{0t} K C_{t0})
                C0t=S@expm(-A*t)
                Ct0=expm(-A*t)@S
                cv=2*np.trace(K@C0t@K@Ct0)
                close(cv,variance_eigen*np.exp(-(l1+l2)*t))
            # Independent 2D integral of centered covariance to verify
            # finite-time averaging formula, without using its elementary antiderivative.
            T=1.7
            num=2/T**2*quad(lambda t:(T-t)*2*np.trace(
                K@(S@expm(-A*t))@K@(expm(-A*t)@S)),0,T,epsabs=2e-10)[0]
            x=(l1+l2)*T
            ana=variance_eigen*2*(x-1+np.exp(-x))/x**2
            close(num,ana,rtol=2e-9)

# For the Brownian gyrator in the cited model: Xdot=-X+uY+noise,
# Ydot=-Y+uX+noise, and torque u(X^2-Y^2).
for u in [0.12,0.5,0.93]:
    for Tx,Ty in [(1.,3.),(0.4,5.),(100.,0.01)]:
        A=np.array([[1.,-u],[-u,1.]])
        S=solve_continuous_lyapunov(A,2*np.diag([Tx,Ty]))
        qmean=u*(S[0,0]-S[1,1])
        qvar=2*u*u*(S[0,0]**2+S[1,1]**2-2*S[0,1]**2)
        predicted=u*u*((Tx+Ty)**2/(1-u*u)+(Tx-Ty)**2)
        close(qmean,u*(Tx-Ty))
        close(qvar,predicted)
        require(abs(qmean)/np.sqrt(qvar)<np.sqrt((1-u*u)/(2-u*u)))

# Exactly normalized product-normal density. Integral and first two moments
# are compared against an independent characteristic-function computation.
v1,v2,c,delta=2.1,0.6,-0.34,-1.7
H=v1*v2-c*c

def pdf(y):
    if y==0.: return np.inf
    arg=np.sqrt(v1*v2)*abs(y)/(abs(delta)*H)
    return np.exp(c*y/(delta*H)-arg)*k0e(arg)/(np.pi*abs(delta)*np.sqrt(H))

for power,expect in [(0,1.),(1,delta*c),(2,delta**2*(v1*v2+2*c*c))]:
    # scipy special k0 has integrable logarithmic singularity at zero
    f=lambda s:(s**power)*pdf(s)
    num=quad(f,-np.inf,0,epsabs=5e-10,limit=200)[0]+quad(f,0,np.inf,epsabs=5e-10,limit=200)[0]
    close(num,expect,rtol=2e-9)

# Sharpness of the bound as independent temperatures tend to a cold bath.
for u in [0.23,0.6,0.9]:
    ratios=[]
    for cold in [1e-2,1e-5,1e-9]:
        x=(1-cold)/(1+cold)
        ratios.append(x*x/(1/(1-u*u)+x*x))
    bound=(1-u*u)/(2-u*u)
    require(ratios[0]<ratios[1]<ratios[2]<bound)
    close(ratios[-1],bound,atol=2e-9,rtol=2e-9)

# Sharp time-to-unit-SNR threshold: the variance attenuation factor decreases
# monotonically and the threshold diverges as the spectral condition degenerates.
from scipy.optimize import brentq
from math import exp
for a2 in [0.0001,0.001,0.01,0.1,0.5,0.99]:
    b=a2/(1+a2)
    f=lambda z: b*z*z/(2*(z-1+exp(-z)))-1
    root=brentq(f,0.00001,1000000)
    close(f(root),0.,atol=1e-9)
    require(f(root*0.8)<0<f(root*1.2))
for a2 in [0.0001,0.001]:
    b=a2/(1+a2)
    f=lambda z: b*z*z/(2*(z-1+exp(-z)))-1
    root=brentq(f,0.00001,1000000)
    close(root*a2/2,1.,rtol=0.001)

print('PASS',checks,'independent numerical and analytic-identity assertions')
