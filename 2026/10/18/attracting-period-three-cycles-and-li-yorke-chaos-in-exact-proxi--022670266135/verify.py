"""Exact rational transcription checks for a ProxSPS period-three theorem.

Requires only Python 3 standard library. Finite tests supplement, not replace,
the analytic proof of the all-parameter conclusions.
"""
from fractions import Fraction as Q


def model(y, x, alpha, lam):
    f = (x-Q(1))**2 / Q(2)
    linear = f + (x-Q(1))*(y-x)
    return max(linear, Q(0)) + lam*y*y/Q(2) + (y-x)**2/(Q(2)*alpha)


def prox_direct(x, alpha, lam):
    # The convex model is quadratic on two half-lines, with a single kink.
    # Its exact minimizer lies among their two unconstrained vertex points
    # and the kink; evaluation selects the global minimizer, not a formula.
    candidates = [x/(1+alpha*lam), (x-alpha*(x-1))/(1+alpha*lam)]
    if x != 1:
        candidates.append((x+1)/2)
    return min(candidates, key=lambda y: model(y, x, alpha, lam))


def kink(alpha, lam):
    return (alpha*(2-lam)-1)/(alpha*(2+lam)-1)


def piece(x, alpha, lam):
    c=kink(alpha,lam)
    return (x+1)/2 if x<=c else (alpha+(1-alpha)*x)/(1+alpha*lam)


def orbit(alpha, lam):
    den=alpha+3+4*alpha*lam
    return ((alpha+3)/den,(alpha+3+2*alpha*lam)/den,(alpha+3+3*alpha*lam)/den)


def test():
    count=0
    examples=0
    for denlam in (20, 15, 10, 8, 6, 5, 4):
        lam=Q(1,denlam)
        for ai in (5,6,7,8,10,12,15,20,30,40,60,100):
            alpha=Q(ai)
            if not (0<lam<Q(1,3) and alpha*(1-3*lam)>4):
                continue
            c=kink(alpha,lam)
            p=orbit(alpha,lam)
            assert 0<p[0]<p[1]<c<p[2]<1
            assert piece(p[0],alpha,lam)==p[1]
            assert piece(p[1],alpha,lam)==p[2]
            assert piece(p[2],alpha,lam)==p[0]
            mu=(1-alpha)/(4*(1+alpha*lam))
            assert (abs(mu)<1) == (alpha*(1-4*lam)<5)
            for x in list(p)+[c, Q(0), Q(1)]+[Q(i,151) for i in range(152)]:
                q=prox_direct(x,alpha,lam)
                assert q==piece(x,alpha,lam),(x,alpha,lam,q,piece(x,alpha,lam))
                assert 0<=q<=1
                count+=1
            examples+=1
    alpha=Q(5);lam=Q(1,20)
    assert kink(alpha,lam)==Q(35,37)
    assert orbit(alpha,lam)==(Q(8,9),Q(17,18),Q(35,36))
    assert (1-alpha)/(4*(1+alpha*lam))==Q(-4,5)
    assert prox_direct(Q(8,9),alpha,lam)==Q(17,18)
    assert prox_direct(Q(17,18),alpha,lam)==Q(35,36)
    assert prox_direct(Q(35,36),alpha,lam)==Q(8,9)
    print(f'PASS: {examples} admissible rational parameter pairs, {count} exact proximal minimizations; full period-three algebra and stability classification verified at test points.')
    print('Witness: alpha=5, lambda=1/20; cycle 8/9 -> 17/18 -> 35/36 -> 8/9; kink 35/37; period-three multiplier -4/5.')

if __name__=='__main__':
    test()
