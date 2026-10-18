"""Exact algebra and independent finite-temperature response checks for confined run-and-tumble calorimetry."""
import sympy as sp
import numpy as np
from scipy.integrate import quad
from scipy.linalg import expm

q,a=sp.symbols('q a', positive=True)
A=q*(q*q-1)**2*(q**4+6*q*q+1)
B=3*q**10+14*q**8+19*q**6+19*q**4+14*q*q+3
C=2*q*(q**8+5*q**6+6*q**4+5*q*q+1)
P=3*q*(q*q+1); Q=q**4+q*q+1
E2=q*(q*q+1)*(a*(q*q+1)+2*q)/(2*a*q+q*q+1)**3
E3=q*(A*a*a+B*a+C)/(P*a+Q)**3

def rate_model(m):
    ss=[(j,z) for j in range(m) for z in (-1,1)]
    G=sp.zeros(len(ss))
    h=[]
    for i,(j,z) in enumerate(ss):
        heat=0
        for d in (-1,1):
            if 0 <= j+d < m:
                v=q**(z*d)
                G[i,ss.index((j+d,z))]+=v
                G[i,i]-=v
                heat+=v*z*d
        k=ss.index((j,-z))
        G[i,k]+=a;G[i,i]-=a
        h.append(heat)
    return G,sp.Matrix(h)

for m,expected in [(2,E2),(3,E3)]:
    G,h=rate_model(m)
    dim=G.rows
    W=G.T.copy();W[-1,:]=sp.ones(1,dim)
    pi=W.inv()*sp.Matrix([0]*(dim-1)+[1])
    hav=(pi.T*h)[0]
    L=G.copy();L[-1,:]=pi.T
    rhs=sp.Matrix([hav-h[i] for i in range(dim-1)]+[0])
    w=L.inv()*rhs
    extracted=sp.factor(-q*(sp.diff(pi,q).T*w)[0])
    assert sp.cancel(extracted-expected)==0, ('response identity',m)
    assert sp.simplify(pi.T*G)==sp.zeros(1,dim)
    assert sp.simplify(G*w+h-sp.ones(dim,1)*hav)==sp.zeros(dim,1)
    print('Exact stationary, Poisson, response identities verified:',m)

assert sp.factor(A*Q-P*B)==-2*q*(4*q**12+23*q**10+52*q**8+58*q**6+52*q**4+23*q**2+4)
assert sp.expand((B*Q-3*P*C)-(q*q+1)*(q**4+q*q+1)*(3*q**8-7*q**6-64*q**4-7*q*q+3))==0
assert sp.cancel(sp.diff(E2,a)-q*(q*q+1)*(q**4-10*q*q+1-4*a*q*(q*q+1))/(2*a*q+q*q+1)**4)==0
H=-A*P*a*a+2*(A*Q-P*B)*a+(B*Q-3*P*C)
assert sp.cancel(sp.diff(E3,a)-q*H/(P*a+Q)**4)==0
print('Derivative factorization verified')

# Independent semigroup finite-response check: old stationary state evolves with new-temperature generator.
def arrays(m,T,af,f=1.):
    qq=np.exp(f/(2*T)); ss=[(j,z) for j in range(m) for z in (-1,1)]
    G=np.zeros((len(ss),len(ss))); h=np.zeros(len(ss))
    for i,(j,z) in enumerate(ss):
        for d in (-1,1):
            if 0<=j+d<m:
                rate=qq**(z*d);G[i,ss.index((j+d,z))]+=rate;G[i,i]-=rate;h[i]+=f*rate*z*d
        k=ss.index((j,-z));G[i,k]+=af;G[i,i]-=af
    M=G.T.copy();M[-1,:]=1
    rhs=np.zeros(len(ss));rhs[-1]=1
    pi=np.linalg.solve(M,rhs)
    return G,h,pi

for m in (2,3):
    for qq,aa in [(1.2,.05),(2.,.4),(2.5,.1),(3.3,.2),(5.,1.)]:
        T=1/(2*np.log(qq));eps=1.e-4
        Gold,_,pold=arrays(m,T,aa)
        Gnew,hnew,pnew=arrays(m,T+eps,aa)
        mu=np.dot(pnew,hnew)
        Mat=Gnew.copy();Mat[-1,:]=pnew
        rhs=mu-hnew;rhs[-1]=0
        w=np.linalg.solve(Mat,rhs)
        response=-np.dot(pold-pnew,w)/eps
        exact=(1/(2*T*T))*float((E2 if m==2 else E3).subs({q:qq,a:aa}))
        assert abs(response-exact)<2e-3*max(1,abs(exact)),(m,qq,aa,response,exact)
        # Time-domain quadrature of the transient heat flux, no stationary Poisson equation.
        xs=np.linspace(0,25,501)
        flux=np.array([float((pold@expm(Gnew*t)-pnew)@hnew) for t in xs])
        transient=np.trapezoid(flux,xs)
        assert abs(transient/eps + exact)<4e-2*max(1,abs(exact)),(m,qq,aa,transient/eps,exact)
print('Ten finite-temperature perturbations and semigroup quadratures verified')

# Show phase separation in a range where only the three-site channel has an interior optimum.
q3=float(sp.sqrt(((7+sp.sqrt(889))/6+sp.sqrt(((7+sp.sqrt(889))/6)**2-4))/2))
q2=float(sp.sqrt(5+2*sp.sqrt(6)))
assert 2.44<q3<2.45 and 3.14<q2<3.15
for qq in [1.25,2.,2.44,2.5,3.,3.3,4.,6.]:
    initial2=float(sp.diff(E2,a).subs({q:qq,a:0}))
    initial3=float(sp.diff(E3,a).subs({q:qq,a:0}))
    assert (initial2>0)==(qq>q2)
    assert (initial3>0)==(qq>q3)
print('Critical q3, q2:',q3,q2)
