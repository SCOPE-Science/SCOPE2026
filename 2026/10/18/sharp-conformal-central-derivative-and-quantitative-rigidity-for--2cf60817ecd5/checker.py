"""Reproducible numerical checks of sharp ellipse harmonic derivative formulas.

Pure Python 3, standard library only. These finite quadratures supplement,
but do not replace, the mathematical arguments.
"""
from math import cos, sin, sqrt, pi, isclose

SAMPLES=16384
PHASES=[(i+0.5)*pi/(2*SAMPLES) for i in range(SAMPLES)]

def integral(a,b,u):
    return 2.0/SAMPLES*sum(sqrt((a*u*cos(t))**2+(b*(1-u)*sin(t))**2) for t in PHASES)

def derivative(a,b,u):
    acc=0.0
    for t in PHASES:
        c,s=cos(t),sin(t)
        denom=sqrt((a*u*c)**2+(b*(1-u)*s)**2)
        acc+=(a*a*u*c*c-b*b*(1-u)*s*s)/denom
    return 2.0/SAMPLES*acc

def find_min(a,b):
    lo,hi=0.0,1.0
    for _ in range(57):
        m=(lo+hi)/2
        if derivative(a,b,m)>0: hi=m
        else: lo=m
    u=(lo+hi)/2
    return u,integral(a,b,u)

def moments(a,b,u):
    accx=accy=0.0
    for t in PHASES:
        c,s=cos(t),sin(t)
        den=sqrt((a*u*c)**2+(b*(1-u)*s)**2)
        x,y=a*a*u*c/den,b*b*(1-u)*s/den
        assert abs(x*x/(a*a)+y*y/(b*b)-1)<4e-15
        accx+=x*c
        accy+=y*s
    # first derivative of harmonic Poisson extension, even symmetries
    return 2*accx/SAMPLES,2*accy/SAMPLES

def main():
    assert abs(find_min(1,1)[1]-1)<3e-9
    assert abs(find_min(4,4)[1]-4)<2e-8
    for a,b in [(2,1),(5,1),(20,1),(1.5,1),(4,3),(1,1)]:
        u,L=find_min(a,b)
        dx,dy=moments(a,b,u)
        assert 0<u<1
        assert abs(dx-dy)<2e-8
        assert abs(dx-L)<2e-8
        assert abs(dy-L)<2e-8
        assert b-1e-8<L<4*b/pi+1e-8
    for eps in [0.1,0.05,0.02,0.01]:
        u,L=find_min(1+eps,1-eps)
        assert abs((L-1)/(eps*eps)+2)<0.04
        assert abs((u-0.5)/eps+1.5)<0.05
    # Support-function stability inequality at finitely many boundary/interior points.
    for a,b in [(2,1),(3,2),(1,1)]:
        u,L=find_min(a,b)
        dmin=min(a*u,b*(1-u))
        for j in range(50):
            t=(j+0.5)*pi/100
            c,s=cos(t),sin(t)
            den=sqrt((a*u*c)**2+(b*(1-u)*s)**2)
            qx,qy=(a*u*c,b*(1-u)*s)
            ex,ey=(qx/den,qy/den)
            for radius in [0,0.3,0.8,1]:
                for ang in [0,1.2,2.5,4]:
                    vx,vy=radius*cos(ang),radius*sin(ang)
                    deficit=den-qx*vx-qy*vy
                    lower=den*((vx-ex)**2+(vy-ey)**2)/2
                    assert deficit>=lower-1e-12
                    assert deficit>=dmin*((vx-ex)**2+(vy-ey)**2)/2-1e-12
    L20=find_min(20,1)[1]
    assert abs(L20-4/pi)<0.002
    print('VERIFY_OK 6 ellipse configurations, 4 near-round tests, support stability, boundary parametrization and Fourier moments')
if __name__=='__main__':main()
