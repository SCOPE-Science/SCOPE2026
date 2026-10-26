"""Quadrature checks for the finite-aperture bandpass concentration crossing law."""
import math
import numpy as np
from scipy.special import roots_legendre
from scipy.optimize import brentq


def pair_spectrum(a, width, bandwidth, nodes=72):
    """Nonzero Nyström spectra for the two parity blocks on one short interval."""
    t, wt = roots_legendre(nodes)
    x = width * t[:, None]
    y = width * t[None, :]
    def kernel(u):
        return bandwidth / math.pi * np.sinc(bandwidth * u / math.pi)
    same = kernel(x-y)
    cross = kernel(2*a+x+y)
    scale = width * np.sqrt(wt[:, None]*wt[None, :])
    eig_plus = np.linalg.eigvalsh(scale * (same+cross))
    eig_minus = np.linalg.eigvalsh(scale * (same-cross))
    return eig_plus, eig_minus


def crossing(a, width, n, nodes=72):
    base = n * math.pi / (2*a)
    def gap(w):
        ep, em = pair_spectrum(a, width, w, nodes)
        return ep[-1] - em[-1]
    return brentq(gap, base-0.15, base+0.15, xtol=1e-13)


def main():
    a=1.0
    checks=0
    for n in (1,2,3):
        previous=None
        for eps in (0.2,0.1,0.05,0.025):
            w0=n*math.pi/(2*a)
            w=crossing(a,eps,n)
            w_alt=crossing(a,eps,n,nodes=48)
            target=w0*(1+eps*eps/(6*a*a))
            error=abs(w-target)
            assert abs(w-w_alt)<2e-10, (n,eps,w,w_alt)
            assert error<1.0*eps**4, (n,eps,error)
            assert w>w0
            ep, em=pair_spectrum(a,eps,w)
            assert abs(ep[-1]-em[-1]) < 3e-12
            assert min(ep[-1],em[-1]) > 9*max(ep[-2],em[-2])
            trace=float(ep.sum()+em.sum())
            trace_theory=4*eps*w/math.pi
            assert abs(trace-trace_theory)<3e-12, (n,eps,trace,trace_theory)
            step=1e-3
            lo=pair_spectrum(a,eps,w-step)
            hi=pair_spectrum(a,eps,w+step)
            gap_lo=lo[0][-1]-lo[1][-1]
            gap_hi=hi[0][-1]-hi[1][-1]
            assert gap_hi * gap_lo < 0
            slope=(gap_hi-gap_lo)/(2*step)
            assert abs(slope - 4*eps*(-1)**n/math.pi) < 12.0*eps**3, (n,eps,slope,4*eps*(-1)**n/math.pi)
            if previous is not None:
                # The remainder is fourth-order, as required by the even analytic expansion.
                assert error < previous/8
            previous=error
            checks+=1
            print(f"n={n} eps={eps:.3f} crossing={w:.12f} prediction={target:.12f} "
                  f"error={error:.3e} slope={slope:.8f} trace_err={abs(trace-trace_theory):.1e}")
    print(f"PASS {checks} parameter cases; two independent Nyström orders, gap reversals, trace and spectral separation")

if __name__=='__main__':
    main()
