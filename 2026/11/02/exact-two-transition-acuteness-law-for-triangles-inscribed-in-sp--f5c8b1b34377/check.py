#!/usr/bin/env python3
"""Numerical and symbolic-identity diagnostics for spherical geodesic-circle triangles.
Requires Python 3, numpy, scipy, mpmath. All random streams are explicitly seeded.
The analytical proof, not this finite computation, establishes the universal claim.
"""
import math
import numpy as np
import mpmath as mp
from scipy.integrate import quad

mp.mp.dps = 45
PI = mp.pi

def Q(k):
    k=mp.mpf(k)
    w=(1-k)/(1+k)
    return (mp.polylog(2,w)-mp.polylog(2,-w))/PI**2

def B_integral(k):
    k=mp.mpf(k)
    if k >= mp.mpf('0.5'):return mp.mpf('0')
    f=lambda u: mp.log((1-k)/(u*(u+k)))/(1-u*u)
    return mp.quad(f,[k,(mp.mpf('0.5')),1-k])/PI**2

def Phi(u):
    return mp.polylog(2,1-u)+mp.log(u)*mp.log(1+u)+mp.polylog(2,-u)

def H(u,k):
    return (-mp.log(1+k)*mp.log(1-u)+mp.polylog(2,(1-u)/(1+k))
            +mp.log(1+u)**2/2+mp.polylog(2,(1-k)/(1+u)))/2

def B_dilog(k):
    k=mp.mpf(k)
    if k>=mp.mpf('0.5'):return mp.mpf('0')
    F=lambda u:mp.log(1-k)*mp.atanh(u)-Phi(u)/2-H(u,k)
    return (F(1-k)-F(k))/PI**2

def Probability(k):
    k=mp.mpf(k)
    if k<=mp.mpf(1)/3:return mp.mpf('0')
    return mp.mpf('0.25') - 3*Q(k) + 3*B_dilog(k)

# Algebraic identity for three cyclic half gaps; direct random checks at 1000 triples.
rng=np.random.default_rng(281828)
xyz=rng.dirichlet([1,1,1],size=1000)*math.pi
cot=1/np.tan(xyz)
identity=cot[:,0]*cot[:,1]+cot[:,1]*cot[:,2]+cot[:,2]*cot[:,0]
assert np.max(np.abs(identity-1))<1e-9
print('COTANGENT_PAIR_SUM_IDENTITY_PASSED')

# Verify the planar-simplex Jacobian by finite differences away from boundaries.
for u,v in [(.2,.3),(.4,.4),(.7,.2),(.34,.35)]:
    def inverse(U,V):
        W=1-U-V
        return np.array([math.atan(math.sqrt(V/(U*W))),math.atan(math.sqrt(W/(U*V)))])
    h=1e-6
    colu=(inverse(u+h,v)-inverse(u-h,v))/(2*h)
    colv=(inverse(u,v+h)-inverse(u,v-h))/(2*h)
    numeric=abs(np.linalg.det(np.column_stack((colu,colv))))
    expected=1/(2*(1-u)*(1-v)*(u+v))
    assert abs(numeric/expected-1)<3e-8,(u,v,numeric,expected)
print('INDEPENDENT_INVERSE_JACOBIAN_PASSED')

# Check the full logarithmic integral against its independent Li2 antiderivative,
# and the one-tail probability against a separate real quadrature.
for ks in ['0.34','0.37','0.40','0.46','0.49','0.50','0.70','0.90']:
    k=mp.mpf(ks)
    B1=B_integral(k)
    B2=B_dilog(k)
    assert abs(B1-B2)<mp.mpf('2e-35'),(ks,B1,B2)
    q_quad=quad(lambda x:-2*math.log(x)/(math.pi**2*(1-x*x)),float(k),1.0,epsabs=1e-12)[0]
    assert abs(q_quad-float(Q(k)))<2e-12,ks
    assert -1e-14 < float(Probability(k)) < 0.2500000000001
print('INDEPENDENT_TAIL_PAIR_INTEGRALS_AND_DILOGARITHMS_PASSED')

# Independent direct intrinsic-angle evaluation from geodesic tangent vectors.
# Dot products are computed without using the cotangent angular-gap criterion.
for R in [0.20,0.60,math.pi/4,0.90,1.02]:
    n=220000
    theta=rng.uniform(0,2*math.pi,size=(n,3))
    X=np.stack((math.sin(R)*np.cos(theta),math.sin(R)*np.sin(theta),
                np.full_like(theta,math.cos(R))),axis=-1)  # [samples,vertex,xyz]
    all_ac=np.ones(n,dtype=bool)
    for i,j,k in [(0,1,2),(1,0,2),(2,0,1)]:
        xy=np.einsum('ij,ij->i',X[:,i,:],X[:,j,:]); xz=np.einsum('ij,ij->i',X[:,i,:],X[:,k,:]); yz=np.einsum('ij,ij->i',X[:,j,:],X[:,k,:])
        all_ac &= (yz-xy*xz>0)
    observed=float(all_ac.mean())
    predicted=float(Probability(mp.cos(R)**2))
    standard_error=math.sqrt(max(predicted*(1-predicted),1e-6)/n)
    assert abs(observed-predicted)<6.0*standard_error+0.00025,(R,observed,predicted)
    print('DIRECT_INTRINSIC_GEODESIC_ANGLE_MONTE_CARLO_PASSED',f'{R:.8f}',f'{observed:.8f}',f'{predicted:.8f}')

# Boundary expansions and both sharp phase-change coefficients.
rc=mp.acos(1/mp.sqrt(3))
for rstr in ['0.1','0.05','0.025']:
    r=mp.mpf(rstr)
    pred=mp.mpf('0.25')-3*r*r/PI**2-r**4/(2*PI**2)
    assert abs(Probability(mp.cos(r)**2)-pred)<mp.mpf('0.004')*r**6
for dstr in ['0.02','0.01','0.005']:
    d=mp.mpf(dstr)
    actual=Probability(mp.cos(rc-d)**2)
    leading=27*d*d/(2*PI**2)
    assert abs(actual/leading-1)<10*d
    k=mp.mpf('0.5')-d
    correction=3*B_dilog(k)
    assert abs(correction/(24*d*d/PI**2)-1)<10*d
print('SHARP_SMALL_RADIUS_AND_TWO_CRITICAL_PHASE_EXPANSIONS_PASSED')
print('ALL_CHECKS_PASSED')
