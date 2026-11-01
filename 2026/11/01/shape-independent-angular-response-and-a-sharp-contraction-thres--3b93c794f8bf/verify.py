"""Finite cross-checks for a triangular chord-recentering moment identity.

Requires only Python 3 standard library. Finite checks are not a proof of the
analytic all-triangles theorem or of the infinite angular integral.
"""
from fractions import Fraction
from math import pi, sqrt, cos, sin, isclose


def signed_area2(p, q, r):
    return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])


def shoelace(poly):
    return sum(poly[i][0] * poly[(i+1) % len(poly)][1]
               - poly[i][1] * poly[(i+1) % len(poly)][0]
               for i in range(len(poly))) / 2


def area_and_inertia(T):
    A = abs(signed_area2(*T)) / 2
    edges2 = sum((T[i][0]-T[(i+1)%3][0])**2 +
                 (T[i][1]-T[(i+1)%3][1])**2 for i in range(3))
    return A, A*edges2/36


def one_direction_moment(T, theta, lam):
    u = (cos(theta), sin(theta)); v = (-sin(theta), cos(theta))
    values = [(p[0]*v[0]+p[1]*v[1], p[0]*u[0]+p[1]*u[1]) for p in T]
    cuts = sorted(z[0] for z in values)
    A, _ = area_and_inertia(T)
    qnodes = (-sqrt(3/5), 0., sqrt(3/5))
    qweights = (5/9, 8/9, 5/9)
    s1 = s2 = s3 = st = st2 = 0.0
    for left,right in zip(cuts[:-1],cuts[1:]):
        if right-left<1e-12: continue
        mid=(left+right)/2; half=(right-left)/2
        for z,wt in zip(qnodes,qweights):
            t=mid+half*z
            hits=[]
            for i in range(3):
                ti, xi = values[i]; tj, xj = values[(i+1)%3]
                if abs(ti-tj)<1e-13: continue
                r=(t-ti)/(tj-ti)
                if -1e-10<=r<=1+1e-10:
                    hits.append(xi+r*(xj-xi))
            if len(hits)!=2:
                raise AssertionError(('unexpected slice',T,theta,t,hits))
            ell=max(hits)-min(hits)
            wt*=half
            s1+=wt*ell; s2+=wt*ell**2; s3+=wt*ell**3
            st+=wt*t*ell; st2+=wt*t*t*ell
    assert isclose(s1,float(A),rel_tol=2e-11,abs_tol=1e-11)
    c=.5-lam
    raw=st2+(lam**3+(1-lam)**3)*s3/3
    return raw-(st**2+c*c*s2*s2)/float(A)


def main():
    R=Fraction
    P=[(R(-1),R(-1)), (R(0),R(-1)), (R(1),R(0)),
       (R(1),R(1)), (R(0),R(1)), (R(-1),R(0))]
    assert shoelace(P)==3
    tests=[[(0.,0.),(1.,0.),(0.,1.)],
           [(0.,0.),(3.,1.),(.1,2.)],
           [(-2.,.5),(.4,3.),(5.,-1.)],
           [(0.,0.),(2.,0.),(1.,sqrt(3))]]
    ns=4800
    checks=1
    for T in tests:
        A,I=area_and_inertia(T)
        for lam in (0., .1, .25, .5):
            means=sum(one_direction_moment(T,2*pi*(k+.337)/ns,lam)
                      for k in range(ns))/ns
            exact=I/2+A*A/(4*pi)+A*A*(lam-.5)**2/(3*pi)
            assert abs(means-exact)<3e-6*max(1.,exact), (T,lam,means,exact)
            checks+=1
        # Every edge orientation can cause a breakpoint. Check a shifted grid.
        for lam in (0., .5):
            means=sum(one_direction_moment(T,2*pi*(k+.119)/ns,lam)
                      for k in range(ns))/ns
            exact=I/2+A*A/(4*pi)+A*A*(lam-.5)**2/(3*pi)
            assert abs(means-exact)<3e-6*max(1.,exact)
            checks+=1
    threshold=.5-sqrt(pi*sqrt(3)/6-.75)
    assert .10<threshold<.11
    equi=tests[-1]; A,I=area_and_inertia(equi)
    for lam,sign in [(0.,1),(.1,1),(threshold,0),(.25,-1),(.5,-1)]:
        diff=I/2+A*A/(4*pi)+A*A*(lam-.5)**2/(3*pi)-I
        if sign: assert sign*diff>0
        else: assert abs(diff)<1e-11
        checks+=1
    # Exact rational Heron/Weitzenbock identity, checked with many triples.
    for a,b,c in [(3,4,5),(5,5,6),(8,9,13),(1,1,1),(2,3,4)]:
        x,y,z=(R(a*a),R(b*b),R(c*c))
        A2=(2*x*y+2*y*z+2*z*x-x*x-y*y-z*z)/16
        assert (x+y+z)**2-48*A2==2*((x-y)**2+(y-z)**2+(z-x)**2)
        checks+=1
    print(f'TRIANGLE_RECENTERING_CHECK_OK: {checks} exact/algebraic or independent quadrature comparisons; '
          f'{4*6*ns} direction-level evaluations; threshold={threshold:.15f}')

if __name__=='__main__': main()
