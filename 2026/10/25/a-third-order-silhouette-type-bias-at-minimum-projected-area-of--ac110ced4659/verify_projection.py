import numpy as np, math
from scipy.spatial import ConvexHull
from scipy.integrate import quad
from scipy.optimize import brentq
V=np.array([[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]],float)
rng=np.random.default_rng(172919)
maxerr=0; mismatch=0; smallest=100
for i in range(5000):
    u=rng.normal(size=3);u/=np.linalg.norm(u)
    a=np.abs(u); A=max(4*a.max(),2*a.sum())
    # independent 2d orthogonal projection
    b=np.eye(3)[np.argmin(abs(u))]; e=b-b.dot(u)*u;e/=np.linalg.norm(e)
    f=np.cross(u,e)
    proj=V@np.stack([e,f],axis=1)
    h=ConvexHull(proj)
    err=abs(h.volume-A)
    maxerr=max(maxerr,err); smallest=min(smallest,A)
    expected=3 if 2*a.sum()>4*a.max()+1.e-9 else 4
    if len(h.vertices)!=expected:mismatch+=1
assert maxerr<1e-10 and mismatch==0
print('HULL_AREA_AND_VERTEX_COUNT',maxerr,mismatch,'min seen',smallest)
amin=2*math.sqrt(2)
# integral per min neighborhood radial angular for delta small
# slope b(phi)
def b(phi):return max(2*math.sqrt(2)*abs(math.cos(phi)),2*abs(math.sin(phi)))
def R(phi,eps):
    bp=b(phi)
    # exact by root. stable small
    return brentq(lambda r: amin*(math.sqrt(1-r*r)-1)+bp*r-eps, 0, 0.2,xtol=1e-15)
theta=math.atan(math.sqrt(2))
def CDF(eps,typ):
    sectors=[(0,theta)] if typ=='Q' else [(theta,math.pi/2)]
    val=sum(quad(lambda phi:1-math.sqrt(1-R(phi,eps)**2),lo,hi,epsabs=1e-14)[0] for lo,hi in sectors)
    return val*(4*12)/(4*math.pi)
q2=3/(2*math.sqrt(2)*math.pi); t2=q2
q3=5/(8*math.pi);t3=7/(8*math.pi)
print('EXACT_ASYMPTOTIC_CONSTANTS',q2,t2,q3,t3)
for eps in (.2,.1,.05,.02,.01,.005):
    tq=CDF(eps,'T'); qq=CDF(eps,'Q')
    print('EPS',eps,'QT',qq,tq, 'Q_SECOND',(qq-q2*eps**2)/eps**3, 'T_SECOND',(tq-t2*eps**2)/eps**3,'tri_fraction',tq/(tq+qq),'tri_slope',(tq/(tq+qq)-.5)/eps)
    assert abs((qq-q2*eps**2)/eps**3-q3)<1.0*eps
    assert abs((tq-t2*eps**2)/eps**3-t3)<1.0*eps
print('ALL_TETRA_PROJECTION_CHECKS_OK')
