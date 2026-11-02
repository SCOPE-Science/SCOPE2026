"""Self-contained checks for the explicit enclosing ellipsoid of a Euclidean ball cap.

Requires SymPy, mpmath and Python 3. No sample-based test is used as a proof.
"""
from fractions import Fraction
import math
import sympy as S
import mpmath as mp


def parameters(d, a):
    if a <= -S.Rational(1, d):
        return S.Integer(0), S.Integer(1), S.Integer(1)
    return ((1 + d*a) / (d+1), d*(1-a)/(d+1),
            d*S.sqrt(1-a*a)/S.sqrt(d*d-1))


def verify_exact():
    x = S.symbols('x', real=True)
    for d in range(2, 11):
        for a in [S.Rational(-9, 10), S.Rational(-1, 3), S.Rational(0),
                  S.Rational(1, 5), S.Rational(4, 5)]:
            if not -1 < a < 1:
                continue
            t,u,v = parameters(d,a)
            if a > -S.Rational(1,d):
                f = (x-t)**2/u**2 + (1-x*x)/v**2
                coefficient = S.factor(1/u**2-1/v**2)
                target = S.factor(coefficient * (x-a)*(1-x))
                assert S.simplify(1-f-target) == 0
                assert coefficient > 0
                assert S.simplify((a-t)/u + S.Rational(1,d)) == 0
                assert S.simplify((1-t)/u - 1) == 0
                assert S.simplify((1-a*a)/v**2 - (1-S.Rational(1,d*d))) == 0
            else:
                assert (t,u,v)==(0,1,1)
            # In any phase, the affine images of a regular-simplex frame
            # are in the truncated ball and on the candidate ellipsoid.
            latitude = -S.Rational(1,d)
            if a > latitude:
                actual_latitude = S.simplify(t+u*latitude)
                actual_rad_sq = S.simplify(v*v*(1-latitude**2))
                assert S.simplify(actual_latitude-a)==0
                assert S.simplify(actual_rad_sq-(1-a*a))==0
            else:
                assert latitude >= a
            # The frame is centered, with scalar covariance I/d.
            assert 1+d*latitude==0
            assert 1+d*latitude**2 == S.Rational(d+1,d)
            assert S.simplify(d*(1-latitude**2)/(d-1) - S.Rational(d+1,d))==0
    print('EXACT_CONTAINMENT_AND_SIMPLEX_FRAME_PASSED')


def kapp(n):
    return mp.pi**(mp.mpf(n)/2)/mp.gamma(mp.mpf(n)/2+1)


def volume_ratio(d, a):
    d=int(d); a=mp.mpf(a)
    q=mp.mpf(d-1)/2
    cap=mp.quad(lambda x:(1-x*x)**q,[a,(a+1)/2,1])*kapp(d-1)
    if a<=-mp.mpf(1)/d:
        u=v=mp.mpf(1)
    else:
        u=d*(1-a)/(d+1)
        v=d*mp.sqrt((1-a*a)/(d*d-1))
    return kapp(d)*u*v**(d-1)/cap


def verify_ratios():
    mp.mp.dps=50
    for d in range(2,12):
        offsets=[mp.mpf('-0.99'), -mp.mpf(1)/d,
                 mp.mpf('-0.1'),mp.mpf('0'),mp.mpf('.2'),mp.mpf('.6'),mp.mpf('.9'),mp.mpf('.99')]
        offsets=sorted(set(float(x) for x in offsets))
        vals=[volume_ratio(d,a) for a in offsets]
        assert all(y>x for x,y in zip(vals,vals[1:])),(d,vals)
        limit=kapp(d)/kapp(d-1)*mp.mpf(d)**d/(2*(d*d-1)**(mp.mpf(d-1)/2))
        near=volume_ratio(d,'0.99999')
        assert abs(near/limit-1) < mp.mpf('3e-4'),(d,near,limit)
    print('SHARP_RATIO_MONOTONICITY_AND_THIN_CAP_LIMIT_PASSED')
    # Independent low-dimensional integral checks, including the 2025
    # hemispherical benchmark in three dimensions.
    assert abs(volume_ratio(3,0)-mp.mpf(27)/16)<mp.mpf('1e-30')
    assert abs(volume_ratio(2,0)-(mp.pi*mp.mpf(4)/(3*mp.sqrt(3)))/
               (mp.pi/2))<mp.mpf('1e-30')
    print('HEMISPHERE_BENCHMARKS_PASSED')


def verify_boundary_layer():
    mp.mp.dps=50
    d=10000
    for tau in [-2,-1,0,1,2]:
        a=mp.mpf(tau)/mp.sqrt(d)
        # beta-integral evaluation is stabler than raw quadrature for d=10000
        volume_fraction=(1-mp.betainc(mp.mpf('0.5'),mp.mpf(d+1)/2,
                                       0,a*a,regularized=True))/2 if a>=0 else \
                        (1+mp.betainc(mp.mpf('0.5'),mp.mpf(d+1)/2,
                                       0,a*a,regularized=True))/2
        if a <=-mp.mpf(1)/d:
            axes_prod=mp.mpf(1)
        else:
            axes_prod=d*(1-a)/(d+1)*(d*mp.sqrt((1-a*a)/(d*d-1)))**(d-1)
        got=axes_prod/volume_fraction
        normal_tail=mp.erfc(mp.mpf(tau)/mp.sqrt(2))/2
        target=mp.exp(-max(0,tau)**2/2)/normal_tail
        assert abs(got/target-1)<mp.mpf('.045'),(tau,got,target)
    print('GAUSSIAN_BOUNDARY_LAYER_PASSED')

if __name__ == '__main__':
    verify_exact()
    verify_ratios()
    verify_boundary_layer()
    print('ALL_CHECKS_PASSED')
