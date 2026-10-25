"""Independent numerical checks for angularly conditioned areas of inscribed quadrilaterals.
This checker samples Cartesian vertices and computes shoelace area and chord direction angles.
"""
import math
import numpy as np
from scipy.integrate import quad
PI=math.pi

def mean_area(t):
    return PI*np.sin(t)**2/(t*(PI-t))

def variance_area(t):
    s=np.sin(t)
    return s*s*(1+np.sin(2*t)*(1/t-1/(PI-t))/4-s*s*(1/t**2+1/(PI-t)**2))

def cv(v,t):
    if v <= -1: return 0.
    if v >= math.cos(t):return 1.
    return (PI-math.acos(v))/(PI-t)

def cdf_area(k,t):
    if k<=0:return 0.
    if k>=2*math.sin(t):return 1.
    z=k/math.sin(t)
    return 1-quad(lambda a:cv(math.cos(a)-z,t),0,t,epsabs=5e-12,epsrel=5e-12,limit=100)[0]/t

rng=np.random.default_rng(20261021)
n=450000
angles=np.sort(rng.uniform(0,2*PI,(n,4)),axis=1)
xx=np.cos(angles); yy=np.sin(angles)
area=0.5*np.abs(np.sum(xx*np.roll(yy,-1,axis=1)-yy*np.roll(xx,-1,axis=1),axis=1))
dx1=xx[:,2]-xx[:,0];dy1=yy[:,2]-yy[:,0]
dx2=xx[:,3]-xx[:,1];dy2=yy[:,3]-yy[:,1]
angle=np.arctan2(np.abs(dx1*dy2-dy1*dx2),np.abs(dx1*dx2+dy1*dy2))
assert np.min(angle)>0 and np.max(angle)<=PI/2
pred_mean=3/PI
pred_second=1/2+105/(16*PI**2)
assert abs(np.mean(area)-pred_mean)<0.003, (np.mean(area),pred_mean)
assert abs(np.mean(area*area)-pred_second)<0.004
print('CARTESIAN_AREA_AND_TWO_GLOBAL_MOMENTS', np.mean(area),np.mean(area*area),pred_mean,pred_second)
for lo,hi in [(.20,.30),(.42,.52),(.72,.82),(1.04,1.14),(1.40,1.50)]:
    mask=(angle>=lo)&(angle<hi)
    t=angle[mask]
    expected=mean_area(t)
    centered=area[mask]-expected
    ev=np.mean(variance_area(t))
    assert mask.sum()>4000
    assert abs(np.mean(centered))<0.022, (lo,hi,np.mean(centered))
    assert abs(np.mean(centered**2)-ev)<0.03,(lo,hi,np.mean(centered**2),ev)
    print('CARTESIAN_CONDITIONAL_MEAN_VAR_OK',lo,hi,int(mask.sum()),round(float(np.mean(centered)),5),round(float(np.mean(centered**2)),5),round(float(ev),5))
for t in (.35,.8,1.25,PI/2):
    # Test the CDF from the independent cosine-rectangle representation at several quantiles.
    u=rng.uniform(0,t,350000)
    v=rng.uniform(t,2*PI-t,350000)
    y=math.sin(t)*(np.cos(u)-np.cos(v))
    assert abs(y.mean()-mean_area(t))<0.008
    assert abs(y.var()-variance_area(t))<0.009
    for frac in (.15,.4,.7,.9):
        k=2*math.sin(t)*frac
        assert abs(np.mean(y<=k)-cdf_area(k,t))<0.0045,(t,frac)
    print('CONDITIONAL_CDF_1D_QUADRATURE_OK',t,mean_area(t),variance_area(t))
# Diagonal angle density has already been established in earlier literature/records.
for x in (.3,.8,1.2):
    F=6*(x/PI)**2-4*(x/PI)**3
    assert abs(np.mean(angle<=x)-F)<0.004
print('KNOWN_CROSSING_ANGLE_MARGINAL_RECONSTRUCTED_OK')
print('ALL_QUADRILATERAL_CONDITIONAL_AREA_CHECKS_OK')
