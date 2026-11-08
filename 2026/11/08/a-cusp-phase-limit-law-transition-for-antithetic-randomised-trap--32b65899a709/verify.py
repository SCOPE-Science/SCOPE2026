"""Reproducible finite checks for cusp-phase antithetic quadrature.

Run: python verify.py
All numerical assertions use deterministic test nodes; no simulation is used as proof.
Only the Python standard library is required.
"""
import math
from fractions import Fraction


def direct_error(gamma, n, us):
    h = 1.0 / n
    total = 0.0
    for j, u in enumerate(us):
        total += 0.5 * h * (abs((j + u) * h - 0.5)**gamma +
                            abs((j + 1 - u) * h - 0.5)**gamma)
    return total - 2.0**(-gamma) / (gamma + 1.0)


def local_error(gamma, offset, u):
    if offset == 0.0:
        true_integral = 1.0 / (gamma + 1.0)
    else:
        true_integral = ((offset + 1.0)**(gamma + 1.0) -
                         offset**(gamma + 1.0)) / (gamma + 1.0)
    return (0.5 * ((offset + u)**gamma +
                   (offset + 1.0 - u)**gamma) - true_integral)


def decomposed_error(gamma, n, us):
    m = n // 2
    if n % 2 == 0:
        s = sum(local_error(gamma, j, us[m-1-j]) +
                local_error(gamma, j, us[m+j]) for j in range(m))
    else:
        s = abs(us[m] - 0.5)**gamma - 2.0**(-gamma)/(gamma + 1.0)
        s += sum(local_error(gamma, j+0.5, us[m-1-j]) +
                 local_error(gamma, j+0.5, us[m+1+j]) for j in range(m))
    return s * n**(-gamma-1.0)


def variance_local(gamma, offset, count=96):
    # Composite midpoint integration on U in (0,1), centering independently.
    vals = [0.5*((offset + (i+0.5)/count)**gamma +
                 (offset + 1.0 - (i+0.5)/count)**gamma)
            for i in range(count)]
    mean = math.fsum(vals)/count
    return math.fsum((x-mean)**2 for x in vals)/count


def check():
    num = 0
    for gamma in (0.4, 0.75, 1., 1.25, 1.5, 1.75, 2.):
        for n in range(2, 20):
            us = [(((7*j+3) % 29)+0.31)/30.0 for j in range(n)]
            a = direct_error(gamma,n,us)
            b = decomposed_error(gamma,n,us)
            assert abs(a-b)<5e-12, (gamma,n,a,b)
            num += 1
    for n in range(2,70):
        for uf in (Fraction(1,11),Fraction(2,5),Fraction(1,2)):
            u=float(uf)
            got=n*n*direct_error(1,n,[u]*n)
            target=0.0 if n%2==0 else abs(u-0.5)-0.25
            assert abs(got-target)<1e-11, (n,u,got,target)
            num += 1
    for gamma in (0.8,1.25,1.5,1.75,2.):
        for offset in (40.,100.,250.,1000.):
            var=variance_local(gamma,offset)
            leading=(gamma*(gamma-1.))**2/720. * offset**(2*gamma-4)
            assert abs(var/leading-1.)<0.051, (gamma,offset,var/leading)
            num += 1
    for gamma,n in ((1.5,512),(1.5,4096),(1.75,4096),(2.,300)):
        assert n%2==0
        sm=2*math.fsum(variance_local(gamma,float(j)) for j in range(n//2))
        var=sm*n**(-2*gamma-2)
        observed=n**5*var
        if gamma==1.5:
            observed/=math.log(n)
            target=1.0/640.
            assert 0.5*target<observed<2.5*target
        else:
            target=2.0**(4-2*gamma)*(gamma*(gamma-1.))**2/(720*(2*gamma-3))
            assert abs(observed/target-1.)<0.26, (gamma,n,observed,target)
        print('gamma',gamma,'n',n,'scaled variance',format(observed,'.12g'),
              'asymptotic target',format(target,'.12g'))
        num += 1
    assert Fraction(1,80)-Fraction(1,12)**2 == Fraction(1,180)
    assert Fraction(2,1)*Fraction(3,4)**2/Fraction(720) == Fraction(1,640)
    print('PASS:',num+2,'deterministic checks')

if __name__ == '__main__':
    check()
