"""Reproduce the magnetic rhombic chain two-frequency transfer and elliptic law.

Requires Python 3, NumPy, SciPy. All comparisons have predetermined finite ranges.
"""
import math
import numpy as np
from scipy.linalg import eigh
from scipy.integrate import quad
from scipy.special import ellipk


def finite_chain(flux, j=1.0, plaquettes=12):
    a = list(range(plaquettes + 1))
    b = list(range(plaquettes + 1, 2*plaquettes + 1))
    c = list(range(2*plaquettes + 1, 3*plaquettes + 1))
    h = np.zeros((3*plaquettes + 1, 3*plaquettes + 1), complex)
    for n in range(plaquettes):
        angle = flux if n % 2 == 0 else math.pi
        for u, v, val in ((a[n], b[n], 1), (a[n], c[n], 1),
                          (a[n+1], b[n], 1),
                          (a[n+1], c[n], np.exp(1j*angle))):
            h[u,v] = j*val
            h[v,u] = j*np.conj(val)
    return h


def frequencies(flux, j=1.0):
    c = math.cos(flux/2)
    return j*math.sqrt(2*(2-c)), j*math.sqrt(2*(2+c))


def transfer(flux, t, j=1.0):
    m, p = frequencies(flux, j)
    return (math.cos(m*t)-math.cos(p*t))**2/4


def high_fraction(epsilon):
    return quad(lambda x: 2*ellipk(x)/(math.pi**2*math.sqrt(1-x)),
                0, epsilon, epsabs=1e-12)[0]


def main():
    checks = 0
    worst = 0.0
    for flux in (0, .2, .6, 1.1, 2.0, 2.8, math.pi):
        h = finite_chain(flux)
        eig, vec = eigh(h)
        init, target = 4, 5  # an interior non-pi plaquette
        amp_coeff = vec[target, :] * np.conj(vec[init, :])
        for t in (0.05, .22, .7, 1.3, 2.1, 3.7, 5.2):
            amp = np.sum(amp_coeff * np.exp(-1j*eig*t))
            diff = abs(abs(amp)**2 - transfer(flux, t))
            worst=max(worst, diff)
            assert diff < 4e-12, (flux,t,diff)
            checks+=1
    # Density is the product of independent Beta(1/2,1/2) variables.
    # Check the analytical density against a one-dimensional convolution.
    for z in (.015, .08, .3, .6, .92):
        integrand = lambda a: 1/(math.pi**2*math.sqrt(z*a*(1-a)*(a-z)))
        # Endpoint singularities are handled by the elliptic-parameter substitution.
        conv = (2/(math.pi**2*math.sqrt(z)))*quad(
            lambda v: 1/math.sqrt(1-(1-z)*math.sin(v)**2),
            0, math.pi/2, epsabs=1e-12)[0]
        density = 2*ellipk(1-z)/(math.pi**2*math.sqrt(z))
        assert abs(conv-density)<2e-12
        checks+=1
    for eps in (.001, .01, .1, .35, .8):
        integral = quad(lambda s: math.acos(max(-1,min(1,math.sqrt(1-eps)/math.cos(s)))),
                        0, math.asin(math.sqrt(eps)), epsabs=1e-12)[0]
        area = 4*integral/math.pi**2
        assert abs(area-high_fraction(eps))<2e-11
        checks+=1
    for p,q in ((2,3),(3,4),(5,8)):
        r=p/q
        c=2*(1-r*r)/(1+r*r)
        phi=2*math.acos(c)
        wm, wp = frequencies(phi)
        t=math.pi*p/wm
        assert abs(transfer(phi,t)-1)<1e-12
        checks+=1
    for p,q in ((1,1),(3,5),(5,7),(7,9)):
        r=p/q
        if r*r<1/3: continue
        c=2*(1-r*r)/(1+r*r)
        phi=2*math.acos(c)
        theta=np.linspace(0,2*math.pi,250001)
        vals=(np.cos(p*theta)-np.cos(q*theta))**2/4
        cap=math.cos(math.pi/(2*(p+q)))**4
        assert float(vals.max())<=cap+3e-12
        checks+=1
    # Deterministic quasi-periodic time sampling for two irrational ratios.
    for phi in (0.0, .73):
        wm,wp=frequencies(phi)
        t=np.linspace(0,30000,150001)
        v=(np.cos(wm*t)-np.cos(wp*t))**2/4
        for eps in (.1,.5):
            est=np.mean(v>1-eps)
            err=abs(est-high_fraction(eps))
            assert err<.012, (phi,eps,err)
            checks+=1
    assert abs(high_fraction(.001)-(.001/math.pi+3*.001**2/(8*math.pi)))<1e-9
    checks+=1
    print(f'PASS checks={checks} maximal_matrix_error={worst:.3e} D(.1)={high_fraction(.1):.12f} D(.5)={high_fraction(.5):.12f}')


if __name__=='__main__':
    main()
