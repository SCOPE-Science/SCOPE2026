"""Reproduce the exact stationary wall-occupation covariance identities.

No numerical approximation is used to prove the continuum identities.
The upwind finite-chain calculations are independent consistency tests.
"""
import sympy as sp
import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve

u, w, tau, alpha, x = sp.symbols('u w tau alpha x', positive=True)
H = tau + u + w
p = [u/H, w/H]

# Time and distance scaled to velocity one, and L=tau.
def potential(j):
    q = p[j]
    C = (q-int(j==0))*u
    J = q*x + C
    S = alpha*q*x*x + 2*alpha*C*x
    plus, minus = S+J, S-J
    wall0 = minus.subs(x,0)
    wall1 = plus.subs(x,tau)
    assert sp.simplify(sp.diff(plus,x)+alpha*(minus-plus)-q)==0
    assert sp.simplify(-sp.diff(minus,x)+alpha*(plus-minus)-q)==0
    assert sp.simplify((plus.subs(x,0)-wall0)/(2*u)-(q-int(j==0)))==0
    assert sp.simplify((minus.subs(x,tau)-wall1)/(2*w)-(q-int(j==1)))==0
    return plus, minus, wall0, wall1

h=[potential(0),potential(1)]
def stationary_integral(f):
    plus,minus,left,right=f
    return sp.simplify(sp.integrate(plus+minus,(x,0,tau))/(2*H)+p[0]*left+p[1]*right)
def green(i,j):
    return sp.simplify(p[i]*(h[j][2+i]-stationary_integral(h[j])))
S=[[sp.factor(green(i,j)+green(j,i)) for j in range(2)] for i in range(2)]
S00=2*u**2*(2*alpha*tau**3+6*alpha*tau**2*w+6*alpha*tau*w*w+3*tau*tau+6*tau*w+6*w*w)/(3*H**3)
S11=2*w**2*(2*alpha*tau**3+6*alpha*tau**2*u+6*alpha*tau*u*u+3*tau*tau+6*tau*u+6*u*u)/(3*H**3)
S01=-2*u*w*(alpha*(tau**3+3*tau*tau*(u+w)+6*tau*u*w)+3*tau*(u+w)+6*u*w)/(3*H**3)
assert sp.simplify(S[0][0]-S00)==0
assert sp.simplify(S[1][1]-S11)==0
assert sp.simplify(S[0][1]-S01)==0
assert sp.simplify(S[1][0]-S01)==0
assert sp.simplify(sp.diff(S01,alpha) + 2*u*w*tau*(tau*tau+3*tau*(u+w)+6*u*w)/(3*H**3))==0
print('PASS: exact generator, boundary, invariant-integral, and all covariance identities')
print('PASS: cross-covariance strictly negative and strictly decreases with alpha')

# Upwind finite-volume CTMC: directed flight jumps and stochastic releases.
def discrete_sigma(n, speed, length, tumble, left_rate, right_rate):
    flight=speed*n/length
    N=2*n+2
    Q=lil_matrix((N,N))
    def edge(i,j,r):
        Q[i,j]+=r; Q[i,i]-=r
    for i in range(n):
        edge(i,i+1 if i<n-1 else 2*n+1,flight)
        edge(n+i,n+i-1 if i>0 else 2*n,flight)
        edge(i,n+i,tumble)
        edge(n+i,i,tumble)
    edge(2*n,0,left_rate)
    edge(2*n+1,2*n-1,right_rate)
    un=speed/(2*left_rate); wn=speed/(2*right_rate)
    Hn=length+un+wn
    left_mass=un/Hn; right_mass=wn/Hn
    pi=np.full(N,length/(2*n*Hn)); pi[-2:]=[left_mass,right_mass]
    assert np.max(np.abs(pi @ Q.toarray())) < 1e-10
    M=(-Q).tolil(); M[-1,:]=0; M[-1,-1]=1
    M=M.tocsc()
    fs=[]
    for idx in range(2):
        f=np.zeros(N); f[-2+idx]=1
        g=f-pi[-2+idx]
        g[-1]=0
        h=spsolve(M,g)
        fs.append((f,h))
    res=np.empty((2,2))
    for i in range(2):
        for j in range(2):
            fi,hi=fs[i]; fj,hj=fs[j]
            res[i,j] = sum(pi*(fi-pi[-2+i])*hj)+sum(pi*(fj-pi[-2+j])*hi)
    return res

numeric_cases=[(2.0,3.0,2.0,1.0,3.0),(1.7,3.2,2.4,0.8,1.4),(4.0,1.0,0.75,3.0,0.6)]
for speed,length,tumble,left_rate,right_rate in numeric_cases:
    params={u:1/(2*left_rate), w:1/(2*right_rate),tau:length/speed,alpha:tumble}
    ref=np.array([[float(val.subs(params)) for val in row] for row in S])
    errors=[]
    for n in (40,80,160,320):
        approx=discrete_sigma(n,speed,length,tumble,left_rate,right_rate)
        err=np.max(np.abs(ref-approx))
        errors.append(err)
    assert all(errors[j+1]<errors[j] for j in range(3)),errors
    assert errors[-1]<0.02,errors
    assert ref[0,1]<0 and np.min(np.linalg.eigvalsh(ref))>0
    print('PASS: finite-chain convergence',tuple(round(float(y),7) for y in errors),
          'exact cross=',round(float(ref[0,1]),9))
print('PASS: all independent tests')
