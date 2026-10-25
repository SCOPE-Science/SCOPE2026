"""Standalone numerical checks for maximum-area triangle tails on a threefold radial oval.
All claims require the analytical proof; this script tests finite-dimensional identities.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.stats import qmc
SQ3=math.sqrt(3.0)
A0=3*SQ3/4

def radius(th,eta): return 1+eta*np.cos(3*th)
def speed(th,eta):
    rr=radius(th,eta)
    return np.sqrt(rr**2+9*eta*eta*np.sin(3*th)**2)

def area(th,eta):
    r=radius(th,eta)
    xp=r*np.cos(th)
    yp=r*np.sin(th)
    return np.abs((xp[...,1]-xp[...,0])*(yp[...,2]-yp[...,0]) - (yp[...,1]-yp[...,0])*(xp[...,2]-xp[...,0]))/2

def constants(eta):
    R=1+eta
    L=quad(lambda x:speed(x,eta),0,2*math.pi,epsabs=1e-11)[0]
    a=3*SQ3*R*(1+7*eta)/8
    b=9*SQ3*eta*R/4
    coeff=8*math.pi*(R/L)**3/(a*math.sqrt(b)) if eta>0 else float("inf")
    return A0*R*R,L,a,b,coeff

def crossover(s):
    if s<=0.5: return 1-s
    theta=math.acos(1-1/s)
    return ((1-s)*theta+s*math.sin(theta))/math.pi

def independent_hessian(eta,h=3e-5):
    center=np.array([0,2*math.pi/3,4*math.pi/3]); f=lambda z:area(z[None,:],eta)[0]
    base=f(center); H=np.zeros((3,3))
    for i in range(3):
        dz=np.zeros(3); dz[i]=h
        H[i,i]=(f(center+dz)-2*base+f(center-dz))/(h*h)
        for j in range(i):
            ez=np.zeros(3);ez[j]=h
            H[i,j]=H[j,i]=(f(center+dz+ez)-f(center+dz-ez)-f(center-dz+ez)+f(center-dz-ez))/(4*h*h)
    return np.sort(-np.linalg.eigvalsh(H)/2)

def local_sample_fixed(eta,eps,N=131072):
    Amax,L,a,b,C=constants(eta)
    sob=qmc.Sobol(d=3,scramble=False).random_base2(int(round(math.log2(N))))
    # Ellipsoid scaled by eps, enlarge by factor 1.1 to integrate entire support robustly.
    z=sob*2-1
    z=z[np.sum(z*z,axis=1)<=1]
    # transform uniform points in unit ball; eigenbasis of 3x3 circulant Hessian
    e0=np.ones(3)/SQ3
    e1=np.array([1.,-1.,0.])/math.sqrt(2)
    e2=np.array([1.,1.,-2.])/math.sqrt(6)
    y=np.stack((e1,e2,e0),axis=1)
    d=np.array([math.sqrt(eps/a),math.sqrt(eps/a),math.sqrt(eps/b)])
    # sampling uniform Euclidean ball all supported ellipsoid plus factor 1.1
    th0=np.array([0,2*math.pi/3,4*math.pi/3])
    theta=th0+z@np.diag(d)@y.T*1.10
    deficit=Amax-area(theta,eta)
    point_weight=np.prod(speed(theta,eta),axis=-1)/(L**3)
    vol=(4*math.pi/3)*np.prod(d)*1.1**3
    prob=6*vol*np.mean(point_weight*(deficit<eps))
    return prob/(C*eps**1.5),len(z)

def crossover_sample(s,eps,N=131072):
    eta=s*eps/(2*A0)
    L=constants(eta)[1]
    sob=qmc.Sobol(d=3,scramble=False).random_base2(int(round(math.log2(N))))
    phi=2*math.pi*sob[:,0]
    # disk around ideal equilateral of circle with radius sqrt(eps/a0), expanded x1.10
    rad=1.10*np.sqrt(eps/(3*SQ3/8))
    t=np.sqrt(sob[:,1]); ang=2*math.pi*sob[:,2]
    u=rad*t*np.cos(ang); v=rad*t*np.sin(ang)
    v0=np.ones((len(u),3))*phi[:,None]
    v0[:,1]+=2*math.pi/3
    v0[:,2]+=4*math.pi/3
    v0[:,0]+=(u/math.sqrt(2)+v/math.sqrt(6))
    v0[:,1]+=(-u/math.sqrt(2)+v/math.sqrt(6))
    v0[:,2]+=(-2*v/math.sqrt(6))
    weight=np.prod(speed(v0,eta),axis=1)/L**3
    deficit=constants(eta)[0]-area(v0,eta)
    # theta triple integral: 2 orientation branches, orthonormal Jacobian sqrt 3
    probability=2*SQ3*(2*math.pi)*(math.pi*rad*rad)*np.mean(weight*(deficit<eps))
    expected=4/(3*math.pi)*eps*crossover(s)
    return probability/expected,probability,expected

if __name__=='__main__':
  for eta in [0,.01,.05,.09]:
    if eta==0: continue
    vals=independent_hessian(eta)
    A,L,a,b,C=constants(eta)
    expected=np.array([b,a,a])
    assert np.allclose(vals,expected,rtol=1e-5,atol=3e-6), (eta,vals,expected)
    print('HESSIAN_SPECTRAL_IDENTITY_OK',eta,vals)
    for eps in [1e-3,2e-4]:
        ratio,n=local_sample_fixed(eta,eps)
        assert .88<ratio<1.12, (eta,eps,ratio)
        print('FIXED_LOBE_TAIL_IMPORTANCE_SAMPLING_OK',eta,eps,round(ratio,5),n)
  for s in [0,0.25,0.5,0.75,2.0,5.0]:
    ratio,approx,expect=crossover_sample(s,0.0005)
    assert .85<ratio<1.15,(s,ratio)
    print('JOINT_SMALL_SHAPE_CROSSOVER_OK',s,round(ratio,5),round(expect,8))
  # check analytic cutoff, large s normalization and near-zero matching
  assert abs(crossover(.25)-.75)<1e-13
  assert abs(math.sqrt(10000)*crossover(10000) -2*math.sqrt(2)/(3*math.pi))<1e-4
  t=0.0001
  cusp=(crossover(0.5+t)-(0.5-t))/t**1.5
  assert abs(cusp-8*math.sqrt(2)/(3*math.pi))<0.001
  print('CUSP_PROFILE_COEFFICIENT_OK')
  print('CRITICAL_PROFILE_AND_MATCHED_COEFFICIENT_OK')
  print('ALL_TRILOBE_GEOMETRY_CHECKS_OK')
