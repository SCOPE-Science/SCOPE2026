"""Supplementary checks for a Cauchy Gabor single-erasure edge criterion.
This numerical script is not a proof of the asymptotic statements.
Python 3.9+; standard library only. Run: python verify_erasure.py
"""
import math
import cmath

TWO_PI = 2 * math.pi

def quantities(q, a, theta):
    r = math.exp(-TWO_PI * a)
    d1 = 1 + r*r - 2*r*math.cos(theta)
    dq = 1 + r**(2*q) - 2*r**q * math.cos(q*theta)
    k = q * (1-r**(2*q)) / (1-r*r)
    w = dq / (k*d1)
    h = dq / ((1+r**q)**2)
    return w, h, r, k, d1, dq

def edge_integral(q, a, N=65536):
    """Midpoint quadrature; the integrable singularities are never sampled exactly."""
    total=0.0
    total_w=0.0
    for j in range(N):
        theta=TWO_PI*(j+.5)/N
        w,h,r,k,d1,dq=quantities(q,a,theta)
        t=4*math.pi*a
        one_minus_h=2*r**q*(1+math.cos(q*theta))/(1+r**q)**2
        # Away from machine-roundoff, expression below is algebraically 1-h.
        if one_minus_h <= 0.0:
            one_minus_h=max(1-h,1e-280)
        add=math.log((1-r*r*h)/one_minus_h)/t
        total+=w*(1+add)
        total_w+=w
    return total/N, total_w/N

def check_direct_zak(q,a,x,omega):
    e=cmath.exp(2j*math.pi*x)
    za=lambda y: -2j*math.pi*cmath.exp(2j*math.pi*y*omega)*math.exp(2*math.pi*a*omega)/(1-cmath.exp(2j*math.pi*y)*math.exp(2*math.pi*a))
    lhs=sum(abs(za(x-k/q))**2 for k in range(q))
    w,h,r,K,d1,D=quantities(q,a,TWO_PI*x)
    rhs=4*math.pi**2*r**(2*(1-omega))*K/D
    assert abs(lhs-rhs) < 1e-9 * max(1,abs(rhs)), (q,a,x,omega,lhs,rhs)

for q in (2,3,4,5):
    for a in (.03,.15,.4):
        for x,omega in ((.113,.29),(.277,.81),(.717,.11)):
            check_direct_zak(q,a,x,omega)

for q,a,upper in ((3,.02,False),(3,.1,True),(4,.01,False),(4,.1,True)):
    val,mass=edge_integral(q,a)
    assert abs(mass-1/q)<2e-7,(q,a,mass)
    assert (val<1) if upper else (val>1), (q,a,val)
    print(f'q={q}, a={a:.4g}, edge_test={val:.9f}, leverage={mass:.9f}')

for q in (2,3,4):
    a=.0005
    val,_=edge_integral(q,a,131072)
    asym=q*math.sqrt(math.pi*a)*val
    assert abs(asym-1) < .003,(q,asym)
    print(f'q={q}, small-pole asymptotic ratio={asym:.7f}')
for q in (3,4,5):
    val,_=edge_integral(q,.5,65536)
    assert abs(val-(.5+1/q))<.002,(q,val)
    print(f'q={q}, large-pole edge={val:.9f}, limit={.5+1/q:.9f}')
print('All supplementary numerical checks passed.')
