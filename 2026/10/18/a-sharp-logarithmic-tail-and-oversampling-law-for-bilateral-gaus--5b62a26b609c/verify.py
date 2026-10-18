"""Reproducibility checks for the Gaussian bilateral singular-gap law.

Finite checks supplement, but do not replace, the analytical proof.
"""
import math
import random


def dot(a,b):
    return sum(x*y for x,y in zip(a,b))


def gram_stats(a,b):
    aa,bb,ab=dot(a,a),dot(b,b),dot(a,b)
    return aa,bb,ab,max(0.,aa*bb-ab*ab)


def gap_ratio_direct(g1,g2,h1,h2,eps):
    a,b,c,ga=gram_stats(g1,g2)
    d,e,f,ha=gram_stats(h1,h2)
    f2=a*d+2*eps*c*f+eps*eps*b*e
    area=math.sqrt(ga*ha)
    det2=eps*eps*ga*ha
    disc=max(0.,f2*f2-4*det2)
    top=(f2+math.sqrt(disc))/2
    return area/top


def gap_limit(g1,g2,h1,h2):
    ag,bg,cg,gg=gram_stats(g1,g2)
    ah,bh,ch,gh=gram_stats(h1,h2)
    return math.sqrt(gg*gh)/(ag*ah)


def c(n):
    return (2/n)*math.gamma((2*n-1)/2)/(math.gamma((n-1)/2)*math.gamma(n/2))


def mom(n,p):
    if p >= n: return math.inf
    return (math.gamma((n-1+p)/2)*math.gamma((n-p)/2)
            /(math.gamma((n-1)/2)*math.gamma(n/2)))


def midpoint(func,a,b,steps):
    h=(b-a)/steps
    return h*sum(func(a+(i+.5)*h) for i in range(steps))


def tail_22(z):
    # Substitution u=tan(theta) in T_2's probability density.
    def integrand(theta):
        u=math.tan(theta)
        v=math.hypot(z,u)
        return math.cos(theta)*u*u/(v*(v+z))
    return midpoint(integrand,0.,math.pi/2,120000)


def main():
    rng=random.Random(314159)
    checks=0
    for m,n in [(2,2),(2,3),(3,2),(3,3),(4,5),(6,7)]:
        for _ in range(125):
            g1=[rng.gauss(0,1) for _ in range(m)]
            g2=[rng.gauss(0,1) for _ in range(m)]
            h1=[rng.gauss(0,1) for _ in range(n)]
            h2=[rng.gauss(0,1) for _ in range(n)]
            z=gap_limit(g1,g2,h1,h2)
            scale=(math.sqrt(dot(g2,g2)*dot(h2,h2)) /
                   math.sqrt(dot(g1,g1)*dot(h1,h1)))
            for trial_eps in [1e-6,1e-8]:
                eps=min(trial_eps,.1/max(scale,1e-300))
                a=gap_ratio_direct(g1,g2,h1,h2,eps)
                q=eps*scale
                assert z/(1+q)**2-1e-9 <= a <= z/(1-q)**2+1e-9, (m,n,eps,a,z,q)
                checks+=1
    for n in range(2,10):
        assert abs(c(n)-((2/n)*math.exp(math.lgamma(n-.5)-math.lgamma((n-1)/2)-math.lgamma(n/2))))<1e-9
        checks+=1
    for n in range(3,9):
        assert abs(mom(n,2)-(n-1)/(n-2))<1e-10
        checks+=1
    for z in [30.,100.,500.,1000.]:
        p=tail_22(z)
        leading=math.log(z)/(2*z*z)
        assert .9 < p/leading < 1.03,(z,p,leading)
        checks+=1
    # Exact hand-computable orthogonal columns, where both projections have length 1.
    assert abs(gap_ratio_direct([1,0],[0,1],[1,0],[0,1],.3)-1)<1e-12
    assert abs(gap_limit([1,0],[0,1],[1,0],[0,1])-1)<1e-12
    checks+=2
    print('PASS:',checks,'checks of finite rank-two identities, moments and tails')


if __name__=='__main__': main()
