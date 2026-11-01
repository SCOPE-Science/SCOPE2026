"""Deterministic reproducibility checks for isosceles-trapezoid width-law formulas.

Run: python3 check.py  (Python 3 standard library only)
This checks analytical identities and representative parameter configurations;
the proof of the all-parameter theorem is in RESULT.md.
"""
from math import pi, sin, cos, tan, atan, atan2, sqrt, acos, asin, isclose


def geometry(A,B,H):
    c=A-B; s=A+B; ell=sqrt(c*c+H*H)
    alpha=atan(c/H); beta=atan(H/s)
    Q=sqrt(s*s+H*H); z=2*A*H/ell
    return c,s,ell,alpha,beta,Q,z

def projection(A,B,H,theta):
    ux,uy=cos(theta),sin(theta)
    verts=[(-A,0),(A,0),(-B,H),(B,H)]
    ps=[x*ux+y*uy for x,y in verts]
    return max(ps)-min(ps)

def branch(A,B,H,theta):
    c,s,ell,alpha,beta,Q,z=geometry(A,B,H)
    return 2*A*cos(theta) if theta<=alpha else s*cos(theta)+H*sin(theta)

def density(A,B,H,w):
    c,s,ell,alpha,beta,Q,z=geometry(A,B,H)
    q=0.
    if z<w<2*A: q+=1/sqrt(4*A*A-w*w)
    if beta<=alpha+1e-12:
        if H<w<z: q+=1/sqrt(Q*Q-w*w)
    else:
        if z<w<Q: q+=1/sqrt(Q*Q-w*w)
        if H<w<Q: q+=1/sqrt(Q*Q-w*w)
    return 2*q/pi

def cdf(A,B,H,w):
    """Independent angular preimage-length calculation, not density integration."""
    c,s,ell,alpha,beta,Q,z=geometry(A,B,H)
    if w<0: return 0.
    # theta in [0,alpha] where 2A cos(theta) <= w
    first=max(0.,alpha-max(0.,acos(max(-1.,min(1.,w/(2*A)))))) if w<2*A else alpha
    # theta in [alpha,pi/2] where Q cos(theta-beta) <= w
    if w>=Q: second=pi/2-alpha
    else:
        delta=acos(max(-1.,min(1.,w/Q)))
        second=max(0.,min(pi/2,beta-delta)-alpha)+max(0.,pi/2-max(alpha,beta+delta))
    return 2*(first+second)/pi

def density_from_arc(A,B,H,w):
    h=1e-6*max(1.,w)
    return (cdf(A,B,H,w+h)-cdf(A,B,H,w-h))/(2*h)

def close(a,b,tol=1e-7):
    if abs(a-b)>tol*max(1.,abs(a),abs(b)):
        raise AssertionError((a,b,a-b))

cases=[(1.,.5,.3),(1.,.5,sqrt(.75)),(1.,.5,1.),
       (1.,.5,sqrt(1.75)),(1.,.5,1.5),
       (1.,.5,sqrt(3.75)),(1.,.5,1.95),
       (1.,.5,2.),(1.,.5,2.5),
       (3.,.8,4.),(3.,2.99,2.), (2.,2.,3.), (1.,1.,2.)]
for A,B,H in cases:
    c,s,ell,alpha,beta,Q,z=geometry(A,B,H)
    for j in range(1001):
        theta=(pi/2)*j/1000
        close(projection(A,B,H,theta),branch(A,B,H,theta),tol=3e-14)
    specials=[H,z,2*A,Q]
    for i in range(1,401):
        w=max(2*A,H,Q)*i/401.
        if min(abs(w-x) for x in specials) < .003*max(1.,w): continue
        close(density(A,B,H,w),density_from_arc(A,B,H,w),tol=3e-5)
    close(cdf(A,B,H,0),0)
    close(cdf(A,B,H,max(2*A,Q)+1),1)
    # exact primitive of the density integrates to angular interval lengths.
    integral_first=asin(1.)-asin(z/(2*A))
    close(integral_first,alpha)
    if beta>alpha+1e-12:
        integral_rise=acos(max(-1.,min(1.,z/Q)))
        integral_fall=acos(H/Q)
        close(integral_rise,beta-alpha)
        close(integral_fall,pi/2-beta)
        close((2/pi)*(integral_first+integral_rise+integral_fall),1)
    else:
        integral_second=asin(max(-1.,min(1.,z/Q)))-asin(H/Q)
        close(integral_second,pi/2-alpha)
        close((2/pi)*(integral_first+integral_second),1)
    # perimeter/mean identity, independent numerical midpoint integration.
    N=250000
    numerical_mean=(pi/2/N)*sum(branch(A,B,H,(j+.5)*pi/(2*N)) for j in range(N))*2/pi
    close(numerical_mean,2*(s+ell)/pi,3e-7)
    # when no interior maximum, recover B from A, H and mean.
    if beta<=alpha+1e-12:
        P=s+ell
        reconstructed_B=(P*P-2*A*P-H*H)/(2*(P-2*A))
        close(reconstructed_B,B)
    else:
        # With H known, the axial diagonal Q reconstructs the upper halfbase.
        reconstructed_B=sqrt(Q*Q-H*H)-A
        close(reconstructed_B,B)
    # For the interior-max class with Q>2A, the three lower endpoint
    # coefficient tests distinguish H<z, H=z and z<H.
    if A>B and beta>alpha+1e-12 and Q>2*A:
        m=min(H,z)
        baseline=1/sqrt(Q*Q-m*m)
        if H < z-1e-11: predicted=baseline
        elif H > z+1e-11: predicted=baseline+1/sqrt(4*A*A-m*m)
        else: predicted=2*baseline+1/sqrt(4*A*A-m*m)
        eps=1e-8*min(1.,abs(H-z) if abs(H-z)>1e-11 else 1.)
        measured=(pi/2)*density(A,B,H,m+eps)
        close(measured,predicted,tol=1e-5)
        if z+1e-11 < H:
            for w in [(z+H)/2., (H+Q)/2.]:
                residue=(pi/2)*density(A,B,H,w)
                if z<w<2*A: residue-=1/sqrt(4*A*A-w*w)
                if z<w<Q: residue-=1/sqrt(Q*Q-w*w)
                expected=(1/sqrt(Q*Q-w*w)) if H<w<Q else 0.
                close(residue,expected)
print('DIRECT_VERTEX_VS_TWO_BRANCH_WIDTH_PASSED')
print('PIECEWISE_DENSITY_VS_INDEPENDENT_CDF_DERIVATIVE_PASSED')
print('NORMALIZATION_ALL_PHASES_AND_ENDPOINTS_PASSED')
print('INVERSE_PARAMETER_FORMULAS_AND_LOWER_ENDPOINT_CLASSIFICATION_PASSED')
print('ALL_CHECKS_PASSED')
