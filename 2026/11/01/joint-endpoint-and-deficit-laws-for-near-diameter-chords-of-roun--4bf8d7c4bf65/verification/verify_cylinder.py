"""Numerical cross-check of near-diameter chord endpoint-type law for cylinders.
Dependencies: numpy, scipy. Run: python verify_cylinder.py
"""
import math
import numpy as np
from scipy.stats import qmc


def kappa(j):
    return math.pi ** (j / 2) / math.gamma(1 + j / 2)


def proposed(d, R, H):
    k = d - 2
    D = math.hypot(2 * R, H)
    pref = 8 * (k + 1) * kappa(k) * 2 ** (k / 2) / (
        (k + 2) * (k + 4) * kappa(k + 1)
        * (2 * R + (k + 1) * H) * D ** (k / 2 + 1)
    )
    weights = {'CC': (H / (2 * R)) ** 2,
               'CS': 2,
               'SS': (2 * R / H) ** 2}
    return {key: pref * weight for key, weight in weights.items()}


def exact_integrals(d, R, H, eps, log2_samples=17):
    k = d - 2
    D = math.hypot(2 * R, H)
    b = R ** 2 / (2 * D)
    phi_max = 1.65 * math.sqrt(eps / b)
    z = qmc.Sobol(d=3, scramble=True, seed=2942).random_base2(log2_samples)
    phi = phi_max * z[:, 0]
    result = {'CC': 0., 'CS': 0., 'SS': 0.}
    surface = kappa(k+1) * R**k * (2*R + (k+1)*H)
    normalization = kappa(k+1) * surface
    angular_factor = (k+1) * kappa(k+1) * k * kappa(k)
    for top in ('C','S'):
        for bottom in ('C','S'):
            ax = 2*R/D if top=='C' else H/D
            ay = 2*R/D if bottom=='C' else H/D
            mx, my = 1.65*eps/ax, 1.65*eps/ay
            sx,sy = mx*z[:,1],my*z[:,2]
            rx = R-sx if top=='C' else R
            ry = R-sy if bottom=='C' else R
            zx = H/2 if top=='C' else H/2-sx
            zy = -H/2 if bottom=='C' else -H/2+sy
            cosine=np.cos(phi)
            length=np.sqrt(rx**2+ry**2+2*rx*ry*cosine+(zx-zy)**2)
            fluxx = (zx-zy)/length if top=='C' else (rx+ry*cosine)/length
            fluxy = (zx-zy)/length if bottom=='C' else (ry+rx*cosine)/length
            weight = fluxx*fluxy*rx**k*ry**k/length**(d-1)
            weight*=np.sin(phi)**(k-1)
            exact = (2*angular_factor/normalization)*mx*my*phi_max * np.mean(weight*(length>D-eps))
            typ = ''.join(sorted([top,bottom]))
            result[typ] += exact
    return result


def test():
    for d,R,H in [(3,1,2),(4,1,2),(5,1,2),(4,1,1)]:
        expected=proposed(d,R,H)
        p=H**2/(H**2+4*R**2)
        assert abs(expected['CC']/sum(expected.values())-p**2)<1e-12
        assert abs(expected['CS']/sum(expected.values())-2*p*(1-p))<1e-12
        for eps in [0.025, 0.008]:
            got=exact_integrals(d,R,H,eps)
            ratios={t:got[t]/eps**((d+2)/2)/expected[t] for t in got}
            print(f'd={d}, R={R}, H={H}, eps={eps}, ratio-to-limit={ratios}')
            assert all(abs(1-v)<0.09 for v in ratios.values()), ratios
    d,R,H=4,1,2
    assert abs(sum(proposed(d,R,H).values())-3/32)<1e-14
    print('PASS: all conditional endpoint types and tail normalizations checked')

if __name__=='__main__':
    test()
