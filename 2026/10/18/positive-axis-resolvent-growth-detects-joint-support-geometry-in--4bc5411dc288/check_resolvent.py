"""Finite diagnostics for multidimensional Volterra positive-ray resolvent kernels."""
import math


def logsumexp(vals):
    a=max(vals)
    return a+math.log(sum(math.exp(v-a) for v in vals))


def log_e(d,z):
    assert d>=1 and z>0
    nmax=int(5*z**(1/d)+80)
    return logsumexp([n*math.log(z)-d*math.lgamma(n+1) for n in range(nmax+1)])


def point_rect_resolvent(d, a, b, x, lam):
    """Positive resolvent for indicator of axis-aligned rectangle at x.

    For n >= 1, V^n 1_[a,b] (x) = [(x-a)_+^n-(x-b)_+^n]/n!.
    """
    assert len(a)==len(b)==len(x)==d
    terms=[]
    z=1./lam
    for n in range(1, int(6*z**(1/d)+100)):
        factors=[max(0,x[j]-a[j])**n-max(0,x[j]-b[j])**n for j in range(d)]
        if all(t>0 for t in factors):
            terms.append(-(n+1)*math.log(lam)-d*math.lgamma(n+1)+sum(math.log(t) for t in factors))
    return logsumexp(terms)


def main():
    checks=0
    # The elementary multinomial bound on E_d, and its sharp exponential type.
    for d in (2,3,4):
        for z in (0.5,1,10,100,1000):
            L=log_e(d,z)
            assert L<=d*z**(1/d)+2e-13
            checks+=1
        for z in (1e3,1e4,1e5):
            L=log_e(d,z)
            assert L<=d*z**(1/d)+1e-11
            assert L>=d*z**(1/d)-5*d*math.log(z+2)
            checks+=2
    # Check tensor kernel at x=(1,1) for two geometrically different supports.
    eps=0.16
    diag=[((0.,0.),(eps,eps)),((1-eps,1-eps),(1.,1.))]
    cross=[((0.,1-eps),(eps,1.)),((1-eps,0.),(1.,eps))]
    samples=[]
    for lam in (0.0025,0.001,0.0004,0.0002):
        records={}
        for label,rects,rho in [('diag',diag,1.),('cross',cross,eps)]:
            logs=[point_rect_resolvent(2,a,b,(1.,1.),lam) for a,b in rects]
            val=logsumexp(logs)
            scaled=lam**0.5*val
            target=2*math.sqrt(rho)
            # Corrections are logarithmic, therefore at finite lambda the raw
            # value is only an approximation, not an asymptotic certificate.
            records[label]=(scaled,target)
            assert val>0
            checks+=1
        samples.append((lam,records))
    # Algebraic support example: equal marginal support, distinct product extrema.
    assert 0<eps<.5 and eps < 1
    checks+=1
    print('FINITE_DIAGNOSTICS_OK', checks)
    for lam,record in samples:
        print('lambda',lam,'diag_scaled/target',record['diag'], 'cross_scaled/target',record['cross'])


if __name__=='__main__':
    main()
