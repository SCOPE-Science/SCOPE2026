#!/usr/bin/env python3
"""Independent arithmetic and quadrature checks for finite chord-moment inversion.
Standard-library Python 3.10+; run: python verify.py
"""
from fractions import Fraction
from math import gamma, sqrt, pi, cos, sin


def elementary(b):
    coeff = [Fraction(1)]
    for bi in b:
        nb = [Fraction(0) for _ in range(len(coeff)+1)]
        for j, c in enumerate(coeff):
            nb[j] += c
            nb[j+1] -= c*bi
        coeff = nb
    return coeff  # prod (1 - b_i*t)


def poch(a, n):
    result = Fraction(1)
    for i in range(n):
        result *= a+i
    return result


def half_inverse_coeff(p, max_k):
    """Coefficients of prod (1-b_i*t)^(-1/2), exact rational arithmetic."""
    h = [Fraction(1)]
    for k in range(1, max_k+1):
        convolution = sum(h[j]*h[k-j] for j in range(1,k))
        for j in range(1,k+1):
            ckj = sum(h[r]*h[k-j-r] for r in range(k-j+1))
            convolution += p[j]*ckj
        h.append(-convolution/2)
    return h


def invert_square(h):
    """Recover prod (1-b_i*t) from its inverse square root's coefficients."""
    inv=[Fraction(1)]
    for k in range(1,len(h)):
        inv.append(-sum(h[j]*inv[k-j] for j in range(1,k+1)))
    return [sum(inv[j]*inv[k-j] for j in range(k+1)) for k in range(len(h))]


def simpson(f, n):
    assert n%2 == 0
    step = 1./n
    ans = f(0.) + f(1.)
    for j in range(1,n):
        ans += (4. if j%2 else 2.)*f(j*step)
    return ans*step/3


def J_integral(es, x, n=20000):
    """Exact monotone parameter integral, evaluated by transformed Simpson rule.
    es=[e1,...,e_(d-1)]; P0(y)=y^d+e1*y^(d-1)+...+e_(d-1)*y.
    """
    d=len(es)+1
    coeff=[1.]+list(map(float,es))
    def fn(t):
        if t >= 1.: return 0.
        if t == 0.: return 2.*coeff[-1]/x**1.5
        y=(t/(1-t))**2
        # Horner for P0(y)=y*(y^(d-1)+e1*y^(d-2)+...+e_(d-1)).
        acc=coeff[0]
        for c in coeff[1:]: acc=acc*y+c
        P0=y*acc
        derivative=d*coeff[0]
        for i,c in enumerate(coeff[1:],start=1):
            derivative=derivative*y+(d-i)*c
        return 2.*derivative/((1-t)**2*(x+P0)**1.5)
    return simpson(fn,n)


def k0_from_integral(d, es, x):
    return 2.*sqrt(pi)*gamma((d+1)/2)/gamma(d/2)/J_integral(es,x)


def gauss_legendre_nodes(n):
    nodes=[]
    for i in range(1,n+1):
        z=cos(pi*(i-.25)/(n+.5))
        for iteration in range(25):
            pm, pn=1.,z
            for k in range(2,n+1):
                pm,pn=pn,((2*k-1)*z*pn-(k-1)*pm)/k
            deriv=n*(z*pn-pm)/(z*z-1)
            step=pn/deriv
            z-=step
            if abs(step)<1e-15:break
        nodes.append((z,2./((1-z*z)*deriv**2)))
    return nodes


def recover_constant_term(d, es, k0, lower, upper):
    factor=2.*sqrt(pi)*gamma((d+1)/2)/gamma(d/2)
    for _ in range(37):
        mid=(lower+upper)/2
        value=factor/J_integral(es,mid,n=6000)
        if value < k0: lower=mid
        else: upper=mid
    return (lower+upper)/2


def sphere_integral_direction_ratios(b):
    """Independent spherical Gauss-Legendre/periodic-trapezoid quadrature."""
    assert len(b)==3
    nphi=192
    es=[0.,0.,0.,0.]
    for z,w in gauss_legendre_nodes(64):
        h=sqrt(max(0.,1-z*z))
        for ip in range(nphi):
            phi=2*pi*(ip+.5)/nphi
            u=(h*cos(phi),h*sin(phi),z)
            A=sum(u[i]*u[i]/float(b[i]) for i in range(3))
            es[0] += w*sqrt(A)
            for k in range(3): es[k+1] += w*A**(-1.5-k)
    es=[v/(2*nphi) for v in es]
    return [es[k+1]/es[0] for k in range(3)]


def run():
    for b in ([1,1],[1,4,9],[1,4,9,16],[4,4,4,4]):
        b=list(map(Fraction,b));d=len(b)
        poly=elementary(b)
        h=half_inverse_coeff(poly,d-1)
        recovered=invert_square(h)
        assert recovered==poly[:d],(recovered,poly)
        # Exact ratios predicted by the measured normalized chord moments.
        ratios=[Fraction(1)]
        for k in range(1,d):
            ratios.append(Fraction(1,1)*__import__('math').factorial(k)/poch(Fraction(d,2),k)*h[k])
        h_from_ratios=[poch(Fraction(d,2),k)*ratios[k]/__import__('math').factorial(k) for k in range(d)]
        assert invert_square(h_from_ratios)==poly[:d]
        es=[(-1)**k*poly[k] for k in range(1,d)]
        x=float(__import__('math').prod(b))
        k0=k0_from_integral(d,es,x)
        exact_ball = (sqrt(x)/sqrt(sum(1./float(v) for v in b)/d) if len(set(b))==1 else None)
        if exact_ball is not None: assert abs(k0/exact_ball-1)<2e-7
        recovered_x=recover_constant_term(d,es,k0,x/20,20*x)
        assert abs(recovered_x/x-1.)<1e-6,(recovered_x,x)
        j1=J_integral(es,x*.9)
        j2=J_integral(es,x)
        j3=J_integral(es,x*1.1)
        assert j1>j2>j3
        print('dimension',d,'squared axes',list(map(str,b)),
              'recovered coefficients',list(map(str,recovered)),
              'K0',round(k0,9),'strict-J-decrease',True)
        if d==3 and len(set(b))==3:
            numerical=sphere_integral_direction_ratios(b)
            analytic=[k0*float(z) for z in ratios]
            errs=[abs(a-c)/abs(c) for a,c in zip(numerical,analytic)]
            print('  independent angular moments ratios vs exact',numerical,analytic,
                  'relative errors',errs)
            assert max(errs)<2.0e-5
    print('PASS: polynomial inversion, strict monotonicity, and angular checks')

if __name__=='__main__': run()
