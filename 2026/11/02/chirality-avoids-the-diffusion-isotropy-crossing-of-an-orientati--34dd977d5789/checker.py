"""Reproduce the chiral orientational-resetting dispersion identities.
Requires Python 3 with sympy, numpy, and scipy.
"""
import sympy as sp
import numpy as np
from scipy.integrate import quad
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve

r,d,w,v=sp.symbols('r d w v', real=True, positive=True)
I=sp.I
beta=r+d
m1=r/(beta-I*w)
m2=r/(r+4*d-2*I*w)
delta=m2-m1**2
Z=v**2*delta/(beta-I*w)
identity=v**2*r*(d**2-2*d*r-w**2-2*I*d*w)/((r+4*d-2*I*w)*(beta-I*w)**3)
assert sp.simplify(Z-identity)==0
assert sp.simplify(sp.diff(Z,r).subs({r:d/2,w:0})+16*v**2/(243*d**2))==0
assert sp.simplify(sp.diff(Z,w).subs({r:d/2,w:0})+16*I*v**2/(243*d**2))==0
assert sp.simplify(Z.subs(w,0).subs(r,d/2))==0


def exact_K(reset,rot,spin,speed=1.,Dt=0.):
    mu1=reset/(reset+rot-1j*spin)
    mu2=reset/(reset+4*rot-2j*spin)
    u=np.array([mu1.real,mu1.imag])
    C=np.array([[(1+mu2.real)/2,mu2.imag/2],
                [mu2.imag/2,(1-mu2.real)/2]])-np.outer(u,u)
    b=reset+rot
    J=np.array([[0.,-1.],[1.,0.]])
    A=(b*np.eye(2)+spin*J)/(b*b+spin*spin)
    K=Dt*np.eye(2)+speed**2*(A@C+C@A.T)/2
    z=(K[0,0]-K[1,1])+2j*K[0,1]
    target=speed**2*(mu2-mu1**2)/(b-1j*spin)
    assert abs(z-target)<1e-12
    return K,C,z

# Independent time-domain Green--Kubo integration.
for reset,rot,spin in [(0.25,1.,0.),(0.5,1.,0.),(0.5,1.,0.2),(1.2,0.7,-0.55),(4.0,1.6,1.1)]:
    K,C,z=exact_K(reset,rot,spin,1.5,0.07)
    J=np.array([[0.,-1.],[1.,0.]])
    def cov(t):
        angle=spin*t
        R=np.array([[np.cos(angle),-np.sin(angle)],[np.sin(angle),np.cos(angle)]])
        return np.exp(-(reset+rot)*t)*R@C
    integ=np.array([[quad(lambda t,i=i,j=j: (cov(t)[i,j]+cov(t)[j,i])/2,0,np.inf,epsabs=1e-11)[0]
                     for j in range(2)] for i in range(2)])
    assert np.max(np.abs(K-0.07*np.eye(2)-1.5**2*integ)) <2e-10
    if spin: assert abs(z)>1e-8
    print('Green-Kubo',reset,rot,spin,'gap',abs(z))

# Recover the previously established achiral longitudinal and transverse diffusivities.
for R in [sp.Rational(1,5),sp.Rational(1,2),sp.Integer(2),sp.Integer(7)]:
    m1r=R/(R+1)
    m2r=R/(R+4)
    Sxx=(1+m2r)/2-m1r**2
    Syy=(1-m2r)/2
    Kxx=Sxx/(R+1)
    Kyy=Syy/(R+1)
    assert sp.simplify(2*Kxx-(4+10*R)/((1+R)**3*(4+R)))==0
    assert sp.simplify(2*Kyy-4/((1+R)*(4+R)))==0

# A separately discretized circular Markov generator gives the same diffusion tensor
# in the fine-grid limit; no continuum Fourier formulas are used for this check.
def discrete_K(n,reset,rot,spin,speed=1.,Dt=0.):
    h=2*np.pi/n
    Q=lil_matrix((n,n),dtype=float)
    ahead=rot/h**2+max(spin,0)/h
    behind=rot/h**2+max(-spin,0)/h
    for j in range(n):
        Q[j,(j+1)%n]+=ahead
        Q[j,(j-1)%n]+=behind
        Q[j,0]+=reset
        Q[j,j]-=ahead+behind+reset
    Q=Q.tocsr()
    stat=Q.T.tolil();stat[0,:]=np.ones(n)
    b=np.zeros(n);b[0]=1
    pi=spsolve(stat.tocsc(),b)
    assert abs(pi.sum()-1)<1e-9 and pi.min()>-1e-9
    theta=np.arange(n)*h
    U=np.column_stack([np.cos(theta),np.sin(theta)])
    F=U-pi@U
    H=(-Q).tolil();H[0,:]=pi
    G=np.column_stack([spsolve(H.tocsc(),np.r_[0.,F[1:,j]]) for j in range(2)])
    W=F.T@(pi[:,None]*G)
    return Dt*np.eye(2)+speed**2*(W+W.T)/2

for reset,rot,spin in [(0.5,1.,0.2),(1.2,0.7,-0.55),(0.5,1.,0.)]:
    exact,_,_=exact_K(reset,rot,spin)
    e128=np.max(np.abs(discrete_K(128,reset,rot,spin)-exact))
    e256=np.max(np.abs(discrete_K(256,reset,rot,spin)-exact))
    print('discrete',reset,rot,spin,'errors',e128,e256)
    assert e256<0.012 and e256<e128
print('ALL CHECKS PASSED')
