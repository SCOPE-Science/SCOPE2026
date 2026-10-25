"""Reproduce finite checks of a rectangular-pulse Wigner calculation.

Requires Python 3 and NumPy. Finite checks supplement, but do not establish,
the all-parameter asymptotic theorem.
"""
import math
import numpy as np


def wigner_pair_intervals(x, xi, centers, amps, length=1.0):
    """Independent overlap-interval evaluation of the Wigner integral."""
    centers = np.asarray(centers, dtype=float)
    amps = np.asarray(amps, dtype=complex)
    S = float(np.vdot(amps, amps).real)
    total = 0j
    for j, cj in enumerate(centers):
        for k, ck in enumerate(centers):
            lo = max(2*(cj-length/2-x), 2*(x-ck-length/2))
            hi = min(2*(cj+length/2-x), 2*(x-ck+length/2))
            if lo < hi:
                if abs(xi) < 1e-12:
                    integ = hi - lo
                else:
                    integ = (np.exp(-2j*np.pi*xi*lo)-np.exp(-2j*np.pi*xi*hi))/(2j*np.pi*xi)
                total += amps[j]*amps[k].conjugate()*integ
    return (total/(length*S)).real


def wigner_closed(x, xi, centers, amps, length=1.0):
    centers = np.asarray(centers, dtype=float)
    amps = np.asarray(amps, dtype=complex)
    S = float(np.vdot(amps, amps).real)
    tot = 0.0
    for j, cj in enumerate(centers):
        for k in range(j,len(centers)):
            ck=centers[k]
            radius=length-2*abs(x-(cj+ck)/2)
            if radius<=0:
                continue
            sinc = 2*radius if abs(xi)<1e-12 else np.sin(2*np.pi*radius*xi)/(np.pi*xi)
            if j == k:
                tot += abs(amps[j])**2 * sinc
            else:
                tot += 2*(amps[j]*amps[k].conjugate()*np.exp(-2j*np.pi*(cj-ck)*xi)).real*sinc
    return tot/(length*S)


def spatial_abs_closed(xi,centers,amps,length=1.0):
    centers = np.asarray(centers,float)
    amps = np.asarray(amps,complex)
    S = float(np.vdot(amps,amps).real)
    if abs(xi)<1e-12:
        # Continuous limit of J/(pi*length*S*abs(xi)) as xi tends to zero.
        factor=length/S
    else:
        # numerical x-independent exact |sin| integral with full periods
        h=2*np.pi*abs(xi)*length
        q=int(h//np.pi)
        v=h-q*np.pi
        J=(2*q+1-np.cos(v))/(2*np.pi*abs(xi))
        factor=J/(np.pi*length*S*abs(xi))
    rest=S
    for j in range(len(centers)):
        for k in range(j+1,len(centers)):
            rest+=2*abs(amps[j]*amps[k])*abs(np.cos(2*np.pi*(centers[j]-centers[k])*xi-np.angle(amps[j]*amps[k].conjugate())))
    return factor*rest


def coeff(amps):
    amps=np.asarray(amps,complex)
    S=float(np.vdot(amps,amps).real)
    pair=sum(abs(amps[j]*amps[k]) for j in range(len(amps)) for k in range(j+1,len(amps)))
    return 2/np.pi**2+8/np.pi**3*pair/S


def test(centers,amps,label):
    rng=np.random.default_rng(4391)
    err=0.0
    for _ in range(40):
        x=float(rng.uniform(min(centers)-1,max(centers)+1))
        xi=float(rng.uniform(-4,4))
        err=max(err,abs(wigner_closed(x,xi,centers,amps)-wigner_pair_intervals(x,xi,centers,amps)))
    # independently integrate x to test the exact spatial-L1 reduction.
    errL1=0.
    mids=[(centers[j]+centers[k])/2 for j in range(len(centers)) for k in range(j,len(centers))]
    for xi in [0.43, 1.13, 2.71]:
        numeric=0.
        for m in mids:
            xs=np.linspace(m-.5,m+.5,5001)
            ws=np.array([abs(wigner_pair_intervals(x,xi,centers,amps)) for x in xs])
            numeric+=np.trapezoid(ws,xs)
        theoretical=spatial_abs_closed(xi,centers,amps)
        errL1=max(errL1,abs(numeric-theoretical))
    return label,err,errL1,coeff(amps)

if __name__=='__main__':
    samples=[([0],[1+0j],'single'), ([-6,6],[1,0.7*np.exp(.41j)],'complex double'), ([1,10,100],[1,np.exp(.41j),np.exp(-.73j)],'unit three')]
    for cs,az,title in samples:
        print('%s: exact-Wigner residual %.3e; spatial-absolute residual %.3e; predicted log slope %.12f' % test(cs,az,title))
    for n in [1,2,3,7]:
        print('equal %d pulses: predicted slope %.12f' % (n,coeff(np.ones(n))))
    assert all(test(cs,az,title)[1]<2e-12 and test(cs,az,title)[2]<3e-5 for cs,az,title in samples)
    print('All finite numerical cross-checks passed.')
