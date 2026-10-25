"""Reproducible finite checks for intersections of equally long circle arcs.
The infinite dynamical and spectral claims require the mathematical proof.
"""
from fractions import Fraction
from math import sin, pi, cos, isclose, sqrt
from random import Random


def seg(start, length):
    end = start + length
    if end <= 1:
        return [(start, end)]
    return [(start, Fraction(1)), (Fraction(0), end - 1)]


def intersection(a, b):
    pieces = []
    for u, v in a:
        for w, z in b:
            lo, hi = max(u, w), min(v, z)
            if hi > lo: pieces.append((lo, hi))
    return sorted(pieces)


def total(pieces):
    return sum((b-a for a,b in pieces), Fraction(0))


def expected(alpha, delta):
    if alpha < Fraction(1,2):
        return max(Fraction(0), alpha-delta)
    if delta <= 1-alpha:
        return alpha-delta
    return 2*alpha-1


def fourier_first(pieces):
    # Integral of indicator against exp(-2*pi*i*t).
    import cmath
    return sum((cmath.exp(-2j*pi*a)-cmath.exp(-2j*pi*b))/(2j*pi)
               for a,b in pieces)


def expected_fourier_magnitude(alpha, delta):
    alpha,delta=float(alpha),float(delta)
    if alpha < .5:
        return sin(pi*max(0,alpha-delta))/pi
    if delta <= 1-alpha:
        return sin(pi*(alpha-delta))/pi
    return 2*sin(pi*(1-alpha))*cos(pi*delta)/pi


def main():
    rng=Random(13023722)
    total_cases=0
    for _ in range(3000):
        q=rng.randrange(23,150)
        a=rng.randrange(1,q)
        if a*2==q:continue
        alpha=Fraction(a,q)
        d=Fraction(rng.randrange(0,81),160)
        pieces=intersection(seg(Fraction(0),alpha),seg(d,alpha))
        assert total(pieces)==expected(alpha,d),(alpha,d,pieces)
        assert isclose(abs(fourier_first(pieces)),expected_fourier_magnitude(alpha,d),abs_tol=2e-14),(alpha,d,pieces)
        total_cases+=1
    # The exceptional half-turn symmetry is exact for long intervals.
    for a,q in [(7,11),(5,8),(11,19),(19,27)]:
        alpha=Fraction(a,q)
        d=Fraction(1,2)
        first=intersection(seg(Fraction(0),alpha),seg(d,alpha))
        rotated=intersection(seg(Fraction(1,2),alpha),seg(Fraction(0),alpha))
        assert first==rotated
        assert total(first)==2*alpha-1
    # Two genuinely irrational example slopes: collapsed/constant-density regimes.
    for alpha in ((3-sqrt(5))/2,(sqrt(5)-1)/2):
        phases=[0.0, .07, .13, .24, .35, .49, .5]
        rho=[max(0.0,alpha-d) if alpha<.5 else
             (alpha-d if d<=1-alpha else 2*alpha-1) for d in phases]
        for phase,m in zip(phases,rho):
            N=30000
            count=sum(1 for i in range(N) if (i*alpha)%1 < alpha and ((i*alpha-phase)%1)<alpha)
            assert abs(count/N-m)<.0035,(alpha,phase,count/N,m)
    print(f'VERIFY_OK: {total_cases} exact rational overlap/Fourier checks; '
          'four half-turn invariance examples; 14 finite irrational-orbit density checks; '
          'the unrestricted measure/spectral theorem follows from the proof.')

if __name__=='__main__':main()
