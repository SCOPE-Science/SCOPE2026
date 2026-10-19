"""Reproducible finite checks for the stated delayed-polar eigensolver theorem.

The all-dimension and continuous-parameter assertions are proved
analytically in RESULT.md; these finite computations are corroboration only.
Requires Python 3 standard library.
"""
from cmath import sqrt as csqrt
from math import sqrt

EIGS = (9.0, 7.0, 2.0, -1.0)
L = EIGS[0] - EIGS[-1]


def radius(alpha, p):
    a = 1.0 - (1.0 - p) * alpha
    b = p * alpha
    root = csqrt(a*a - 4.0*b)
    return max(abs((a+root)/2.0), abs((a-root)/2.0))


def alpha_ceiling(p):
    flip = 2.0 / (1.0 - 2.0*p) if p < .5 else float('inf')
    product = 1.0 / p if p > 0 else float('inf')
    return min(flip, product)


def grad(w):
    rq = sum(e*x*x for e, x in zip(EIGS, w))
    return tuple(-(e-rq)*x for e,x in zip(EIGS,w))


def polar_step(w, old, eta, p):
    gw, go = grad(w), grad(old)
    z = tuple(x-eta*((1-p)*a+p*b) for x,a,b in zip(w,gw,go))
    norm=sqrt(sum(y*y for y in z))
    return tuple(y/norm for y in z)


def perturbed(mode,h):
    w=[0.0]*len(EIGS)
    w[0]=sqrt(1-h*h)
    w[mode]=h
    return tuple(w)


def run():
    count_roots = 0
    for p in (0.0, .05, .1, .2, .249, .25, .251, .3, .4, .5, .8, 1.0):
        limit = alpha_ceiling(p)
        for factor in (.03, .13, .51, .87, .99, 1.001, 1.04, 1.3):
            alpha=factor*limit
            # The largest gap L always sets the bound; all other modes stable below it.
            all_radii=[radius(alpha*(EIGS[0]-e)/L,p) for e in EIGS[1:]]
            assert (max(all_radii) < 1) == (factor < 1), (p,factor,all_radii)
            count_roots+=len(all_radii)
    # Finite-difference Jacobian of the actual nonlinear normalized sphere update.
    eps = 1e-6
    star=(1.0,0.0,0.0,0.0)
    checks = 0
    for p in (0.0, .1, .25, .4, .8, 1.0):
        for a in (.05, .4, 1.2, 2.8):
            eta=a/L
            for j in (1,2,3):
                fresh=polar_step(perturbed(j,eps),star,eta,p)[j]/eps
                stale=polar_step(star,perturbed(j,eps),eta,p)[j]/eps
                gap=EIGS[0]-EIGS[j]
                assert abs(fresh-(1-eta*(1-p)*gap)) < 2e-8
                assert abs(stale+eta*p*gap) < 2e-8
                checks+=2
    # The extremal p=1/4, alpha=4 mode has a Jordan collision at -1.
    # With N=M+I and N^2=0, M^k=(-1)^k(I-k*N) and ||M^k||=k+sqrt(k^2+1).
    def mm(X,Y):
        return [[sum(X[i][z]*Y[z][j] for z in range(2)) for j in range(2)] for i in range(2)]
    M=[[-2.,-1.],[1.,0.]]
    P=[[1.,0.],[0.,1.]]
    for k in range(1,101):
        P=mm(P,M)
        target=[[(-1)**k * (1+k), (-1)**k*k], [(-1)**k*(-k), (-1)**k*(1-k)]]
        # I - kN = [[1+k,k],[-k,1-k]].
        assert P == target
        frob=sum(t*t for row in P for t in row)
        assert abs(frob - (2+4*k*k)) < 1e-10
        norm=sqrt((frob+sqrt(frob*frob-4))/2)
        assert abs(norm-(k+sqrt(1+k*k)))<1e-10
    print('PASS',count_roots,'mode spectral-root checks,',checks,
          'actual nonlinear Jacobian checks, and 100 exact Jordan powers/norm checks')

if __name__=='__main__':run()
