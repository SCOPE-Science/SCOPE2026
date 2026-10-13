"""Independent numerical checks of the one-dimensional Boolean interval covariance identities.

Only standard-library Python is needed. Numerical tests illustrate, rather than prove,
universality in the grain-length law or intensity.
"""
from math import exp, expm1, factorial
from bisect import bisect_right
import random


def atoms_check(atoms):
    a = sorted((float(x), float(p)) for x, p in atoms)
    assert a and all(x > 0 and p > 0 for x, p in a)
    assert abs(sum(p for _, p in a) - 1.0) < 1e-12
    return a


def mean(atoms):
    return sum(x * p for x, p in atoms)


def h(atoms, t):
    return sum(p * max(x - t, 0.0) for x, p in atoms)


def survival(atoms, t):
    return sum(p for x, p in atoms if x > t)


def integral_exp_h_minus_1(atoms, lam):
    """Exact integration over each interval between consecutive support points."""
    a = atoms_check(atoms)
    ans = 0.0
    left = 0.0
    for j, (right, _) in enumerate(a):
        prob = sum(p for _, p in a[j:])
        h_left, h_right = h(a, left), h(a, right)
        ans += expm1(lam * h_right) * (right - left)
        ans += exp(lam * h_right) * expm1(lam * (h_left - h_right)) / (lam * prob)
        ans -= (right - left) * exp(lam * h_right)
        left = right
    return ans


def H(atoms, lam):
    mu = mean(atoms)
    return expm1(lam * mu) - 2 * lam * integral_exp_h_minus_1(atoms, lam)


def density(atoms, lam):
    mu = mean(atoms)
    return exp(-2 * lam * mu) * H(atoms, lam)


def kernel(atoms, lam, s):
    mu = mean(atoms)
    u = abs(s)
    h_u = h(atoms, u)
    if s >= 0:
        F = 1 - survival(atoms, s)
        return exp(-lam * mu) - F * exp(-lam * (mu - h_u))
    return exp(-lam * mu) - exp(-lam * (mu - h_u))


def simpson(f, a, b, N=1200):
    assert N % 2 == 0
    dx = (b-a)/N
    return dx/3 * (f(a)+f(b)+sum((4 if j%2 else 2)*f(a+j*dx) for j in range(1,N)))


def density_from_independent_palm_kernel(atoms, lam):
    # Integrate the conditional occupation kernels on each region with fixed tail mass.
    a=atoms_check(atoms)
    mu=mean(a)
    total=0.0
    left=0.0
    passed=0.0
    for j,(right,p) in enumerate(a):
        q=1-passed
        delta=right-left
        uncovered=exp(-lam*(mu-h(a,left)))
        pair=2*exp(-lam*mu)*delta-(1+passed)*uncovered*(-expm1(-lam*q*delta))/(lam*q)
        total+=pair
        passed+=p
        left=right
    return lam*exp(-lam*mu)*total


def h_series_coefficient(atoms, k):
    # coefficient of lambda**k in H; integrate h**(k-1) numerically
    m = max(x for x, _ in atoms)
    integral = simpson(lambda t: h(atoms,t)**(k-1),0,m, 8000)
    mu=mean(atoms)
    return mu**k/factorial(k)-2*integral/factorial(k-1)


def critical(atoms):
    a=1e-4 / mean(atoms)
    b=2.5 / mean(atoms)
    assert H(atoms,a)>0 and H(atoms,b)<0
    for _ in range(65):
        m=(a+b)/2
        if H(atoms,m)>0: a=m
        else: b=m
    return (a+b)/2


def main():
    total=0
    uniform=[(1.0,1.0)]
    for lam in [0.02, .09,.2,.5,.9,1.0,1.2,1.5,2,3,4]:
        analytic = exp(-2*lam)*(1+2*lam-exp(lam))
        assert abs(density(uniform,lam)-analytic)<3e-13
        assert abs(density_from_independent_palm_kernel(uniform,lam)-analytic)<2e-8
        total+=2
    rng=random.Random(20261009)
    for j in range(48):
        k=rng.randrange(2,6)
        lengths=sorted(rng.uniform(.12,2.7) for _ in range(k))
        weights=[rng.random()+.1 for _ in lengths]; s=sum(weights)
        atoms=[(x,p/s) for x,p in zip(lengths,weights)]
        lam=rng.uniform(.04,2.3)
        lhs=density(atoms,lam)
        rhs=density_from_independent_palm_kernel(atoms,lam)
        assert abs(lhs-rhs)<2e-7, (atoms,lam,lhs,rhs)
        total+=1
        for m in range(2,7):
            c=h_series_coefficient(atoms,m)
            assert c < -mean(atoms)**m/factorial(m)+1e-9, (m,c)
            total+=1
    laws = [uniform,[(.5,.5),(1.5,.5)],[(.2,.5),(1.8,.5)],[(.05,.5),(1.95,.5)]]
    roots=[critical(a) for a in laws]
    assert all(x>y for x,y in zip(roots,roots[1:])),roots
    total+=3
    for law in laws:
        root=critical(law)
        assert density(law,root*.9)>0 and density(law,root*1.1)<0
        total+=2
    rare=[(.001,1-.0001),( (1-(1-.0001)*.001)/.0001,.0001)]
    assert 0<critical(rare)<.01
    total+=1
    print('PASS',total,'analytical identities and numerical cross-checks')
    print('convex-order threshold example (mean 1):',[(round(x,12)) for x in roots])
    print('rare giant grain threshold:',round(critical(rare),12))

if __name__=='__main__': main()
