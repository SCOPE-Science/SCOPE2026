"""Independent finite checks of the one-long-edge even-cycle theorem.
Uses only Python's standard library; no external research infrastructure.
"""
from fractions import Fraction as F
from itertools import product
from math import sqrt


def all_vertex_shells(m, t):
    # Take every cube vertex and every intersection of a cube edge with
    # each of the two nontrivial strip boundary hyperplanes.
    shells = set()
    for signs in product((-1, 1), repeat=m):
        s = sum(signs)
        if abs(s) <= t:
            shells.add((F(m), F(s*s)))
    for signs in product((-1, 1), repeat=m-1):
        s0 = sum(signs)
        for target in (t, -t):
            x = target-s0
            if -1 <= x <= 1:
                shells.add((F(m-1)+x*x, target*target))
    return shells


def outer_shells(m,t,r):
    return max(float(h)+(r-1)*float(s2)/m for h,s2 in all_vertex_shells(m,t))


def given_outer(m,t,r):
    t=float(t)
    return max(m+(r-1)/m,
               m-1+(2-t)**2+(r-1)*t*t/m)


def distortion_squared(m,t,r,independent=False):
    t=float(t)
    outer=outer_shells(m,F(str(t)),r) if independent else given_outer(m,t,r)
    return outer * max((m-1+1/r)/m, m/(t*t*r))


def predicted(m,t):
    t=float(t)
    t_star=m/sqrt(1+(m-1)*sqrt(m+1))
    if t<=t_star:
        r=(m*m/(t*t)-1)/(m-1)
        d2=1/(t*t)+(m-1)*(m*m-1)/(m*m-t*t)
    else:
        r=sqrt(m+1)
        d2=((m-1)*sqrt(m+1)+1)**2/m**2
    return r,d2,t_star


def golden_min(m,t):
    a,b=0.02, max(100.,10.*m)
    golden=(sqrt(5)-1)/2
    c=b-golden*(b-a);d=a+golden*(b-a)
    fc=distortion_squared(m,t,c);fd=distortion_squared(m,t,d)
    for _ in range(180):
        if fc<fd:
            b=d;d=c;fd=fc;c=b-golden*(b-a);fc=distortion_squared(m,t,c)
        else:
            a=c;c=d;fc=fd;d=a+golden*(b-a);fd=distortion_squared(m,t,d)
    r=(a+b)/2
    return r, distortion_squared(m,t,r)


def run():
    total=0
    for m in (5,7,9):
        for t in (F(1),F(6,5),F(3,2),F(7,4),F(2)):
            shells=all_vertex_shells(m,t)
            assert shells
            for r in (F(1,2),F(1),F(2),F(3),F(m),F(2*m)):
                direct=max(h+(r-1)*s2/m for h,s2 in shells)
                predicted_F=max(F(m)+(r-1)/m, F(m-1)+(2-t)**2+(r-1)*t*t/m)
                assert direct==predicted_F,(m,t,r,direct,predicted_F)
                total+=1
            rp,dp,tc=predicted(m,t)
            rn,dn=golden_min(m,float(t))
            assert abs(dp-dn)<1e-8,(m,t,dp,dn)
            assert abs(rp-rn)<1e-5,(m,t,rp,rn)
    for m in (11,13,15,17,19,21):
        tc=predicted(m,1.5)[2]
        assert (tc<2)==(m<=15)
        for t in (1,1.25,1.5,1.75,2):
            rp,dp,_=predicted(m,t)
            rn,dn=golden_min(m,t)
            assert abs(dp-dn)<1e-8,(m,t,dp,dn)
    # Known boundary cases: m=3 yields the four-cycle 5/3 plateau.
    m=3
    tc=3/sqrt(5)
    assert abs(predicted(m,2)[0]-2)<1e-12
    assert abs(predicted(m,2)[1]-25/9)<1e-12
    assert abs(predicted(m,1)[1]-3)<1e-12
    print('PASS: %d exact rational vertex-shell/ellipsoid comparisons' % total)
    print('PASS: 45 independent golden-section minimizations')
    print('PASS: dimension cutoff m<=15 and known four-cycle boundary')

if __name__=='__main__':
    run()
