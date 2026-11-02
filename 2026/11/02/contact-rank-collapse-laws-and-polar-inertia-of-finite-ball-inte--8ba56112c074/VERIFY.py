"""Independent numerical and combinatorial checks of equal-ball collapse laws."""
import math
import numpy as np
from scipy.linalg import null_space
from scipy.special import gamma
from scipy.integrate import simpson
from scipy.stats import qmc

def reg_vertices(d):
    n=d+1
    q=null_space(np.ones((1,n)))
    return np.sqrt(n/d)*q

def polarvol_reg(k):
    return k**(k/2)*(k+1)**((k+1)/2)/math.factorial(k)

def kappa(m):
    return math.pi**(m/2)/gamma(m/2+1)

def leading(d,k,R=1):
    m=d-k
    return polarvol_reg(k)*kappa(m)*(2*R)**(m/2)*gamma(m/2+1)*gamma(k+1)/gamma(k+m/2+1)

def radial_vol2(eps, N=2**16):
    v=reg_vertices(2)
    theta=(np.arange(N)+0.37)*2*math.pi/N
    q=np.stack((np.cos(theta),np.sin(theta)),axis=-1)
    a=-(q @ v.T).min(axis=1)
    delta=2*eps+eps**2
    rad=delta/(np.sqrt(a*a+delta)+a)
    return math.pi*np.mean(rad*rad)

for eps in [0.02,0.01,0.005,0.0025]:
    val=radial_vol2(eps)
    norm=val/(leading(2,2)*eps**2)
    print('triangle d2',eps,'ratio',format(norm,'.12f'),'slope',(norm-1)/eps)
assert abs((radial_vol2(0.0025)/(leading(2,2)*0.0025**2)-1)/0.0025 + 1) < .012

# Explicit 3D two-sphere lens exact volume; exponent=(3+1)/2=2.
for eps in [0.02,0.01,0.001]:
    actual=2*math.pi*(eps**2+2*eps**3/3)
    target=leading(3,1)*eps**2
    print('lens d3',eps,'ratio', actual/target)
assert abs(leading(3,1)-2*math.pi)<1e-12

# Quasi-Monte Carlo for a 2-simplex lying in 3-space; exponent=5/2.
verts=reg_vertices(2)
p=18
s=qmc.Sobol(d=3,scramble=True,seed=713).random_base2(p)
z=np.empty_like(s)
z[:,0:2]=6*s[:,0:2]-3
z[:,2]=3.1*s[:,2]-1.55
for eps in [0.02, 0.01, 0.005]:
    xpar=eps*z[:,:2]
    xper=np.sqrt(eps)*z[:,2]
    ok=((np.sum(xpar*xpar,axis=1)+xper**2)[:,None]-2*xpar@verts.T <=2*eps+eps**2).all(axis=1)
    measured=(6*6*3.1)*ok.mean()/eps**0 * eps**2.5
    ratio=measured/(leading(3,2)*eps**2.5)
    print('triangle d3',eps,'ratio',ratio)
    assert abs(ratio-1)<.07
print('ALL_CHECKS_PASSED')
# Nonregular fully active triangle: exact polar inertia predicts first curvature correction.
from numpy.linalg import solve, det
angs=np.deg2rad([0.,127.,250.]); normals=np.stack((np.cos(angs),np.sin(angs)),axis=1)
verts=np.array([solve(normals[[i,(i+1)%3],:],-np.ones(2)) for i in range(3)])
area=0.; moment=0.
for i in range(3):
 a=verts[i]; b=verts[(i+1)%3]
 A=abs(det(np.stack((a,b))))/2
 area+=A
 moment+=A*(np.dot(a,a)+np.dot(b,b)+np.dot(a,b))/6
coef=(2*area-4*moment)/(2*area)
theta=(np.arange(2**16)+0.15)*2*math.pi/2**16
vec=np.stack((np.cos(theta),np.sin(theta)),axis=1)
radA=-(vec@normals.T).min(axis=1)
for eps in [0.01,0.005,0.0025]:
 D=2*eps+eps**2
 rad=D/(np.sqrt(radA**2+D)+radA)
 v=math.pi*np.mean(rad**2)
 observed=(v/(area*eps**2)-1)/eps
 print('nonregular triangle',eps,'slope',observed,'theory',coef)
 assert abs(observed-coef)<.075
print('NONREGULAR_SECOND_ORDER_PASSED')
