"""Standalone reproducibility checks for the tangent-chord product theorem.

Requires Python 3 with scipy. This verifies finite instances and density
normalization; the general theorem is proved analytically in RESULT.md.
"""
import math
from scipy.integrate import quad


def product_from_roots(A, B, r, theta):
    ca, sa = math.cos(theta), math.sin(theta)
    # n=(cos,sin), v=(-sin,cos); A,B are squared semiaxes
    alpha, beta = 1/A, 1/B
    q2 = alpha*sa*sa + beta*ca*ca
    q1 = 2*r*(beta-alpha)*ca*sa
    q0 = r*r*(alpha*ca*ca + beta*sa*sa)-1
    disc = q1*q1-4*q2*q0
    u1=(-q1-math.sqrt(disc))/(2*q2)
    u2=(-q1+math.sqrt(disc))/(2*q2)
    assert u1 < 0 < u2
    return -u1*u2


def product_closed(A,B,r,theta):
    a,b = 1/A,1/B
    ca,sa = math.cos(theta), math.sin(theta)
    z=a*sa*sa+b*ca*ca
    return r*r+(1-r*r*(a+b))/z


def invert_endpoints(lo,hi,r):
    rr=r*r
    if abs(hi-lo)<1e-12:
        assert abs(lo-rr)>1e-12
        return lo+rr,lo+rr
    assert (lo-rr)*(hi-rr)>0
    vals=sorted([lo,hi],key=lambda x:abs(x-rr))
    near,far=vals
    ratio=(far-rr)/(near-rr)
    small=near+rr/ratio
    return ratio*small,small


def endpoints(A,B,r):
    qa=B-r*r*B/A
    qb=A-r*r*A/B
    return min(qa,qb),max(qa,qb)


for A,B,rr in [(9,4,1),(9,4,3.8),(5,3,1),(5,3,2.8),(4,4,1.1)]:
    r=math.sqrt(rr)
    for j in range(96):
        t=2*math.pi*j/96
        assert math.isclose(product_from_roots(A,B,r,t), product_closed(A,B,r,t),rel_tol=1e-12,abs_tol=1e-12)
    lo,hi=endpoints(A,B,r)
    recovered=invert_endpoints(lo,hi,r)
    assert math.isclose(recovered[0],A,rel_tol=2e-12)
    assert math.isclose(recovered[1],B,rel_tol=2e-12)
print('EXACT_QUADRATIC_AND_ENDPOINT_INVERSION_PASSED')

r=1.7
T=1/(r*r)
for frac in [0.08,0.2,0.33,0.5]:
    alpha=frac*T
    beta=(1-frac)*T
    A,B=1/alpha,1/beta
    assert min(A,B)>r*r
    for j in range(60):
        q=product_closed(A,B,r,2*math.pi*j/60)
        assert math.isclose(q,r*r,rel_tol=1e-12)
    s=0.7*r
    los,his=endpoints(max(A,B),min(A,B),s)
    assert his-los>0 if frac!=0.5 else abs(his-los)<1e-12
print('RESONANT_FIBER_AND_TWO_RADIUS_SEPARATION_PASSED')

for A,B,rr in [(9,4,1),(9,4,3.8),(5,3,1),(5,3,2.8)]:
    r=math.sqrt(rr)
    lo,hi=endpoints(A,B,r)
    def density_at_psi(psi):
        q=lo+(hi-lo)*math.sin(psi)**2
        jac=2*(hi-lo)*math.sin(psi)*math.cos(psi)
        if psi==0 or psi==math.pi/2:return 0
        den=(math.pi*abs(q-rr)*math.sqrt((q-lo)*(hi-q)))
        num=math.sqrt((lo-rr)*(hi-rr))
        return num/den*jac
    prob,_=quad(density_at_psi,1e-7,math.pi/2-1e-7,epsabs=1e-9,epsrel=1e-9)
    assert abs(prob-1)<2e-6,(A,B,r,prob)
    assert math.isclose(hi-lo,(A-B)*abs(1-rr*(1/A+1/B)),rel_tol=1e-12,abs_tol=1e-12)
print('DENSITY_NORMALIZATION_AND_EXACT_SENSITIVITY_PASSED')
print('ALL_CHECKS_PASSED')
