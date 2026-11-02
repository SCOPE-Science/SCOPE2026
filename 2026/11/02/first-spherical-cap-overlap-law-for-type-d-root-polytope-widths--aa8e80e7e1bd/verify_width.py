"""Independent numerical checks for the random-direction widths of type-D root polytopes.

Requires numpy, scipy, mpmath. This is not a substitute for the analytic proof.
"""
import math
import mpmath as mp
from scipy.integrate import quad

ROOT3 = math.sqrt(3)
D = math.atan(math.sqrt(2))

def q(phi):
    return math.asin(ROOT3/2*math.sin(phi-D))

def F3(w):
    t=w/2
    if t <= 1: return 0.0
    if t >= math.sqrt(2): return 1.0
    if t >= math.sqrt(1.5): return 3*math.sqrt(2)*t-5
    c=t/math.sqrt(2-t*t)
    alpha=math.acos(min(1.0,c/ROOT3))
    a=D-alpha
    if t <= 2/ROOT3:
        return 12/math.pi*(t/math.sqrt(2)*a-q(a)-math.pi/4)
    b=D+alpha
    return 12/math.pi*(t/math.sqrt(2)*(math.pi/2-2*alpha)-q(a)+q(b)-5*math.pi/12)

def independent_F3(w):
    t=w/2
    theta=math.acos(max(-1.0,min(1.0,t/math.sqrt(2))))
    def integrand(phi):
        d=math.cos(phi)+math.sqrt(2)*math.sin(phi)
        rho=math.atan(1/d)
        return max(0.0,math.cos(theta)-math.cos(rho))
    return 12/math.pi*quad(integrand,0,math.pi/2,epsabs=2e-11,points=[math.atan(math.sqrt(2))],limit=300)[0]

if __name__=='__main__':
    samples=[2.0001,2.06,2.12,2.20,2.28,4/math.sqrt(3),2.34,2.40,2.44,math.sqrt(6),2.51,2.65,2.80]
    for w in samples:
        analytic=F3(w)
        independent=independent_F3(w)
        assert abs(analytic-independent) < 2e-8,(w,analytic,independent)
    grid=[2+(2*math.sqrt(2)-2)*i/3000 for i in range(3001)]
    values=[F3(x) for x in grid]
    assert max(v2-v1 for v1,v2 in zip(values[1:],values[:-1]))<1e-8
    assert abs(F3(2)) < 1e-12
    assert abs(F3(2*math.sqrt(2))-1)<1e-12
    for w in [math.sqrt(6),2.50,2.7,2.80]:
        cap_tail=6*(1-w/(2*math.sqrt(2)))
        assert abs((1-F3(w))-cap_tail)<1e-11
    C3=4*math.sqrt(3)*2/math.pi*(2/3)**(3/4)
    # Avoid cancellation for minuscule eps; use 1e-3 or 1e-4.
    for eps,tol in [(0.001,0.002),(0.0001,0.0003)]:
        w=math.sqrt(6)-eps
        D3=F3(w)-(3*w/math.sqrt(2)-5)
        assert abs(D3/eps**1.5-C3)<tol,(eps,D3/eps**1.5,C3)

    mp.mp.dps=65
    n=4
    s=mp.mpf('0.5');c=mp.sqrt(3)/2
    E=4*n*(n-1)*(n-2)
    C4=4*mp.sqrt(3)*(n-1)*(n-2)/mp.pi*(mp.mpf(2)/3)**(mp.mpf(n)/4)
    # For n=4 the joint distribution of two orthogonal sphere coordinates
    # is exactly uniform over the unit disk. Its two-cap lens has an elementary area.
    for delta in ['0.01','0.001','0.0001']:
        delta=mp.mpf(delta)
        threshold=(mp.sqrt(6)-delta)/(2*mp.sqrt(2))
        b=c*mp.sqrt(1-threshold**2)-s*threshold
        lens=2/mp.pi*((b*mp.sqrt(1-b*b)+mp.asin(b))/2-(threshold/c)*b-(s/(2*c))*b*b)
        estimate=E*lens/delta**2
        assert abs(estimate/C4-1)< 0.007,(delta,estimate,C4)
    print('PASS: 13 independent 3D spherical integrals, 3000-point monotonicity grid, cap branch, n=3 and n=4 first-overlap constants')
