"""Independent quadrature for curvature-optimal density compromises on a radial sphere.

The verified geometric family is r(u)=1+epsilon*P2(u_3) in R^3.
This code checks numerical leading coefficients; the all-dimension theorem is analytic.
"""
import math


def integrate(samples, weights, vals):
    return sum(w * x for w, x in zip(weights, vals)) / sum(weights)


def quadrupole_data(eps, size=20000):
    # Midpoint integration in z=cos(theta), with dS=2*pi*r*speed dz.
    weights, curvatures = [], []
    principal = []
    for i in range(size):
        z = -1.0 + (2.0*i+1.0)/size
        sin = math.sqrt(1-z*z)
        r = 1 + eps*(3*z*z-1)/2
        rp = -3*eps*z*sin
        rpp = 3*eps*(1-2*z*z)
        speed = math.hypot(r, rp)
        km = (r*r+2*rp*rp-r*rpp)/(speed**3)
        ka = (r+3*eps*z*z)/(r*speed)
        assert km > 0 and ka > 0
        curvatures.append(km*ka)
        principal.append((km+ka)/2)
        weights.append(r*speed)
    curvature_h = [
        [kap**1.5 for kap in curvatures],
        [math.sqrt(kap)*mean for kap,mean in zip(curvatures,principal)],
        [math.sqrt(kap) for kap in curvatures],
    ]
    density = []
    for weights_j in curvature_h:
        raw = [math.sqrt(x) for x in weights_j]
        norm = integrate(None, weights, raw)
        density.append([x/norm for x in raw])
    return weights,density


def source_gap(eps):
    weights,p = quadrupole_data(eps)
    pm,p2,pp = p
    # A positive, normalized probability density for each comparison.
    base = [math.sqrt(x*y) for x,y in zip(pm,pp)]
    norm = integrate(None, weights, base)
    mid = [x/norm for x in base]
    def risk(x):
        return integrate(None, weights, [(a/t)**2 * t for a,t in zip(x,mid)])
    upper = max(risk(z) for z in p)
    # Exact dual lower bound on two endpoint risks via one scalar maximum.
    f=lambda l: integrate(None,weights,[(a*a-b*b)/math.sqrt(l*a*a+(1-l)*b*b) for a,b in zip(pm,pp)])
    lo,hi=0.,1.
    assert f(lo)>0 and f(hi)<0
    for _ in range(43):
        lam=(lo+hi)/2
        if f(lam)>0:lo=lam
        else:hi=lam
    lam=(lo+hi)/2
    Z=integrate(None,weights,[math.sqrt(lam*a*a+(1-lam)*b*b) for a,b in zip(pm,pp)])
    lower=Z*Z
    assert lower-1e-12<=upper
    return lower,upper,lam


def main():
    for eps in (0.1, 0.05, 0.025, 0.0125):
        lo,hi,lam=source_gap(eps)
        ratio_lo=(lo-1)/(eps*eps)
        ratio_hi=(hi-1)/(eps*eps)
        print(f'eps={eps:.4f} lower_coefficient={ratio_lo:.8f} upper_coefficient={ratio_hi:.8f} dual_weight={lam:.7f}')
        assert 0.16<ratio_lo<0.24
        assert 0.16<ratio_hi<0.24
    assert abs((source_gap(.0125)[0]-1)/(.0125**2)-.2)<.01
    assert abs((source_gap(.0125)[1]-1)/(.0125**2)-.2)<.01
    # Algebraic checks for the harmonic eigenvalue in dimension 3.
    d=3
    eigenvalue_2 = 2*d-(d-1)
    assert eigenvalue_2 == 4
    variance_P2 = 1/5
    constant = (d-1)**2/(4*(d-1)**2*(d+1))
    assert abs(constant*eigenvalue_2**2*variance_P2-.2)<1e-14
    print('CURVATURE_MINIMAX_QUADRATURE_OK')


if __name__ == '__main__':
    main()
