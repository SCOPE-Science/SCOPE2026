"""Independent numerical and algebraic checks for fixed-axis dephasing metrology."""
from itertools import product
from math import sqrt
import numpy as np


def closed_qfi(n, p):
    z = (1.0-p)**2
    if z == 0:
        return 0.
    return (n-2)**2*z**(n-2)*((n-1)*(1+z)-(n-2)*z*z)/(1+(n-1)*z)


def direct_qfi(n, p):
    states = [1 << i for i in range(n)] + [(1 << n)-1-(1 << i) for i in range(n)]
    assert len(set(states)) == 2*n
    bits = [int(s).bit_count() for s in states]
    rho = np.empty((2*n,2*n), dtype=float)
    for i in range(2*n):
        for j in range(2*n):
            rho[i,j] = (1-p)**(int(states[i]^states[j]).bit_count())/(2*n)
    G = np.diag([(n-2*b)/2 for b in bits])
    ev, V = np.linalg.eigh(rho)
    ev[np.abs(ev)<1e-12] = 0
    H = V.T @ G @ V
    qfi=0.
    for a in range(2*n):
        for b in range(2*n):
            denominator=ev[a]+ev[b]
            if denominator>1e-10:
                qfi += 2*(ev[a]-ev[b])**2/denominator*H[a,b]**2
    return qfi


def difference_polynomial(n,z):
    P=(n-1)*(1+z)-(n-2)*z*z
    return (n-2)**2*P - n*n*z*z*(1+(n-1)*z)


def bisection_root(n):
    lo,hi=0.,1.
    assert difference_polynomial(n,lo)>0 and difference_polynomial(n,hi)<0
    for _ in range(90):
        mid=(lo+hi)/2
        if difference_polynomial(n,mid)>0: lo=mid
        else: hi=mid
    return (lo+hi)/2


def main():
    checks=0
    for n in range(3,13):
        for p in (0., .0001, .01, .03, .12, .25, .49, .8, .99, 1.):
            observed=direct_qfi(n,p)
            expected=closed_qfi(n,p)
            assert np.isclose(observed,expected,atol=2e-8,rtol=2e-9), (n,p,observed,expected)
            checks += 1
        root=bisection_root(n)
        assert 0<root<1
        assert difference_polynomial(n,root*.999)>0
        assert difference_polynomial(n,(root+1)/2)<0
        checks += 3
    for n in (20,40,100,1000,5000):
        z=bisection_root(n)
        assert z>0
        # independently test asymptotic coefficient without treating it as a proof
        assert abs(n*(1-sqrt(z))-.5)<4/n
        checks+=1
    for n in range(3,15):
        for z in (.001,.03,.1,.4,.7, .99):
            q=(n-2)**2*((n-1)*(1+z)-(n-2)*z*z)/(n*n*z*z*(1+(n-1)*z))
            h=1e-6
            q2=(n-2)**2*((n-1)*(1+z+h)-(n-2)*(z+h)**2)/(n*n*(z+h)**2*(1+(n-1)*(z+h)))
            assert q2<q
            checks+=1
    print('VERIFY_OK',checks)

if __name__=='__main__': main()
