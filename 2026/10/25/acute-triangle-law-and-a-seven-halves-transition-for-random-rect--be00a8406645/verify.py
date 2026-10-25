#!/usr/bin/env python3
"""Independent checks for exact acute-triangle probabilities on rectangle boundaries."""
import math
import numpy as np
from scipy.integrate import quad
import mpmath as mp


def analytic_base(r):
    return 2*r*r + r**3*(17/9+r/6-2*math.log(r)/3)

def analytic_short(r):
    return 2*r+17/9+1/(6*r)+2*math.log(r)/3

def correction(r):
    if r<=2: return 0.
    d=math.sqrt(r*r-4)
    t=math.acosh(r/2)
    return (2*r**3/3-4*r-4)*t+d*(-r**3/6-5*r*r/9+5*r/3+32/9)

def prediction(r):
    return 1-3*(analytic_base(r)+analytic_short(r)+correction(r))/(4*(r+1)**3)

def raw_at_x(x,w,h):
    s=x*(w-x)
    # Contributions from the chosen point's same supporting edge.
    B=2*h*w+6*s
    # Contributions from an adjacent edge and the opposite parallel edge.
    def side_mix(y,z):
        # y is horizontal displacement to vertical edge; z to top edge.
        if y*z <=h*h: return y*z*z/(2*h)
        return h*z-h**3/(2*y)
    L=side_mix(x,w-x)
    R=side_mix(w-x,x)
    # The opposite vertical edges give products yz<s.
    G= h*h if s>=h*h else (s*(1+math.log(h*h/s)) if s>0 else 0.)
    # On the opposite horizontal edge, obtuse iff uv>h^2.
    H= (s-h*h*(1+math.log(s/(h*h)))) if s>h*h else 0.
    return B+2*(L+R+G+H)

def independent_quadrature(r):
    # Integrate unnormalized ordered-pair masses directly, with no symbolic antiderivative.
    J1=quad(lambda x:raw_at_x(x,r,1),0,r,epsabs=1e-10,limit=200,points=([.5*(r-math.sqrt(r*r-4)),.5*(r+math.sqrt(r*r-4))] if r>2 else None))[0]
    J2=quad(lambda x:raw_at_x(x,1,r),0,1,epsabs=1e-10)[0]
    return 1-3*(J1+J2)/(4*(r+1)**3)

def sample_three(r,n=300000,seed=9001):
    rng=np.random.default_rng(seed)
    z=rng.random((n,3))*(2*(r+1))
    x=np.zeros_like(z);y=np.zeros_like(z)
    # Assign a point to one of the four sides of a rectangle of width r, height 1.
    q=z<r;x[q]=z[q]
    q=(z>=r)&(z<r+1);x[q]=r;y[q]=z[q]-r
    q=(z>=r+1)&(z<2*r+1);x[q]=2*r+1-z[q];y[q]=1
    q=z>=2*r+1;y[q]=2*(r+1)-z[q]
    # Test strict acuteness at all three sampled vertices.
    acu=np.ones(n,dtype=bool)
    for k in range(3):
        i=(k+1)%3;j=(k+2)%3
        dots=(x[:,i]-x[:,k])*(x[:,j]-x[:,k])+(y[:,i]-y[:,k])*(y[:,j]-y[:,k])
        acu &= dots>0
    return acu.mean()

for r in (1.,1.4,2.,2.1,3.,6.):
    p=prediction(r);q=independent_quadrature(r)
    assert abs(p-q)<3e-10,(r,p,q)
    est=sample_three(r,180000,int(r*137)+666)
    assert abs(p-est)<0.006,(r,p,est)
    print(f'RECTANGLE r={r:.1f} symbolic={p:.12f} independent_quadrature={q:.12f} raw_xyz_sampling={est:.6f}')
assert abs(prediction(1)-23/96)<1e-13
print('PREVIOUSLY_KNOWN_SQUARE_SPECIALIZATION_23_OVER_96_OK')

mp.mp.dps=75
for eps in ('0.03','0.005','0.0002','0.000001'):
    e=mp.mpf(eps);r=2+e
    d=mp.sqrt(r*r-4);T=mp.acosh(r/2)
    C=((2*r**3)/3-4*r-4)*T+d*(-r**3/6-5*r*r/9+5*r/3+mp.mpf(32)/9)
    ratio= C/e**mp.mpf('3.5')
    assert abs(ratio+mp.mpf(16)/105)<mp.mpf('0.03')
    print(f'PHASE_7_OVER_2_EPS={eps} coefficient={mp.nstr(ratio,18)}')
for rstr in ('100','500','1000'):
    r=mp.mpf(rstr);d=mp.sqrt(r*r-4);T=mp.acosh(r/2)
    B=2*r*r+r**3*(mp.mpf(17)/9+r/6-2*mp.log(r)/3)
    S=2*r+mp.mpf(17)/9+1/(6*r)+2*mp.log(r)/3
    C=((2*r**3)/3-4*r-4)*T+d*(-r**3/6-5*r*r/9+5*r/3+mp.mpf(32)/9)
    p=1-3*(B+S+C)/(4*(r+1)**3)
    target=(3*mp.log(r)-mp.mpf(3)/2)/r**2
    assert abs(p/target-1)<mp.mpf('0.12')
    print(f'THIN_RECTANGLE_R={rstr} exact={mp.nstr(p,14)} leading={mp.nstr(target,14)} ratio={mp.nstr(p/target,13)}')
print('ALL_RECTANGLE_BOUNDARY_ACUTENESS_CHECKS_OK')
