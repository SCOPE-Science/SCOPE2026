#!/usr/bin/env python3
"""Standalone numerical checks for exact area-deficit covariance formulas.

Requires Python 3 and NumPy. Trapezoidal quadrature integrates each finite
trigonometric polynomial exactly when its grid resolves all frequencies.
"""
import math
import numpy as np

MODES = {2: (0.019, -0.008), 3: (0.004, 0.011), 5: (-0.003, 0.002)}

def weights(modes):
    return {m: math.pi * (m*m - 1) * (a*a + b*b) / 2
            for m, (a, b) in modes.items()}

def support_coeff(modes, axes):
    z = {m: complex(a, -b) for m, (a, b) in modes.items()}
    for axis in axes:
        z = {m: (u + u.conjugate()*np.exp(-2j*m*axis))/2
             for m, u in z.items()}
    return z

def deficit_coeff(coeff):
    return sum(math.pi*(m*m - 1)*abs(z)**2/2
               for m, z in coeff.items())

def area_integral(coeff, r=1.0, N=4096):
    theta = 2*math.pi*np.arange(N)/N
    h = np.full(N, r)
    dh = np.zeros(N)
    for m, z in coeff.items():
        harmonic = z*np.exp(1j*m*theta)
        h += harmonic.real
        dh += (1j*m*harmonic).real
    return math.pi*(h*h-dh*dh).mean()

def check_close(label, a, b, tol=3e-11):
    if abs(float(a)-float(b)) > tol*max(1.0,abs(float(b))):
        raise AssertionError((label,a,b,abs(float(a)-float(b))))


def main():
    ws = weights(MODES)
    D0 = sum(ws.values()); S2 = sum(w*w for w in ws.values())
    assert sum((m*m-1)*math.hypot(a,b) for m,(a,b) in MODES.items()) < 1
    for t in range(1, 7):
        mean = D0/2**t
        var = ((3/8)**t-(1/4)**t)*S2
        assert var > 0 and mean > 0

    angles = math.pi*(np.arange(128)+.37)/128
    d1 = np.array([deficit_coeff(support_coeff(MODES,[u])) for u in angles])
    check_close('one-step mean', d1.mean(), D0/2)
    check_close('one-step variance', d1.var(), (3/8-1/4)*S2)
    assert np.all(d1 <= D0*(1+1e-14))

    # Resolve all frequency combinations of two successive symmetrizations:
    # 128 x 128 is far above the maximum 4*(2+3+5) frequency.
    d2 = np.empty((128,128))
    for i,u in enumerate(angles):
        for j,v in enumerate(angles):
            coeff = support_coeff(MODES,[u,v])
            d2[i,j] = deficit_coeff(coeff)
            if i==7 and j==39:
                area = area_integral(coeff)
                check_close('support-integrated area',math.pi-area,d2[i,j])
    check_close('two-step mean',d2.mean(),D0/4)
    check_close('two-step variance',d2.var(),((3/8)**2-(1/4)**2)*S2)
    check_close('one-two covariance',((d1[:,None]-d1.mean())*(d2-d2.mean())).mean(),
                .5*(3/8-1/4)*S2)
    assert np.all(d2 <= d1[:,None]*(1+1e-14))
    assert D0*D0>S2
    one_mode={5:(.014,.007)}
    w=next(iter(weights(one_mode).values()))
    d=np.array([deficit_coeff(support_coeff(one_mode,[u])) for u in angles])
    check_close('sharp case variance',d.var(),(3/8-1/4)*w*w)
    check_close('sharp case mean',d.mean(),w/2)
    print('VERIFY_OK: deterministic quadrature, two-step moment/covariance, ' 
          'support-integral area, convexity, and equality cases.')

if __name__=='__main__':
    main()
