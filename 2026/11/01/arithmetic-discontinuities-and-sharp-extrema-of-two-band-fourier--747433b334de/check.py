"""Reproducible supplementary checks for the two-band Fourier projection law.

All inputs and outputs are mathematical quantities.  Only Python's standard library
is required; the proof of the infinite-dimensional limit is in RESULT.md.
"""
import math
from fractions import Fraction


def constant_series(p, q, terms=1200):
    assert p > q >= 1 and math.gcd(p, q) == 1
    correction = math.fsum(
        (1 if (q * ell) % 2 == 0 else -1)
        / ((4*p*p*ell*ell-1)*(4*q*q*ell*ell-1))
        for ell in range(1, terms+1)
    )
    return (16 / math.pi**3)*(1+2*correction)


def periodic_mean(p, q, pieces=90000):
    """Composite midpoint rule on one exact period of |sin(qv)cos(pv)|."""
    h=math.pi/pieces
    return 4 / math.pi**2 * h * math.fsum(
        abs(math.sin(q*(j+0.5)*h)*math.cos(p*(j+0.5)*h))
        for j in range(pieces)
    )


def lebesgue_norm(N, alpha, pieces=None):
    """Positive-half-period midpoint quadrature; no geometric-series cancellation."""
    m=math.floor(alpha*N)
    pieces = pieces or 50*N
    h=math.pi/pieces
    vals=[]
    for j in range(pieces):
        t=(j+0.5)*h
        val=2*abs(math.sin(N*t/2)*math.cos(m*t/2))/math.sin(t/2)
        vals.append(val)
    return h/math.pi * math.fsum(vals)


def main():
    generic=16/math.pi**3
    c_min=8*(2*math.sqrt(2)-1)/(3*math.pi**2)
    c_max=8*(3*math.sqrt(3)-2)/(5*math.pi**2)
    checks=0
    for p,q in [(2,1),(3,2),(3,1),(5,2),(5,3),(7,4),(7,5),(11,6)]:
        s=constant_series(p,q)
        integral=periodic_mean(p,q)
        assert abs(s-integral)<2e-8, (p,q,s,integral)
        checks+=1
        if q%2==0: assert s>generic
        else: assert s<generic
        checks+=1
        assert c_min-1e-10<=s<=c_max+1e-10
        checks+=1
    assert abs(constant_series(2,1)-c_min)<2e-11
    assert abs(constant_series(3,2)-c_max)<2e-11
    checks+=2
    for alpha,pred in [(2,c_min),(1.5,c_max),(math.sqrt(2),generic), (5/3,constant_series(5,3))]:
        n1,n2=320,1280
        l1,l2=lebesgue_norm(n1,alpha),lebesgue_norm(n2,alpha)
        slope=(l2-l1)/math.log(n2/n1)
        assert abs(slope-pred)<0.002, (alpha,slope,pred)
        checks+=1
    print('PASS',checks,'supplementary periodic-integral, series, parity, global-bound, and finite-N slope checks')
    print('minimum',f'{c_min:.12f}', 'generic',f'{generic:.12f}', 'maximum',f'{c_max:.12f}')


if __name__=='__main__':
    main()
