"""Independent finite checks for the sharp random-contraction reset tail theorem.

Uses only Python's standard library. This is a finite checker, not a proof of
stationary existence, asymptotic tail equivalence, or infinite-product bounds.
"""
from math import prod, exp, isclose
from itertools import product

ASSERTIONS = 0


def check(condition, message):
    global ASSERTIONS
    assert condition, message
    ASSERTIONS += 1


def qproduct(base, count=250):
    z = 1.0
    for j in range(1, count + 1):
        z /= (1.0 - base(j))
    return z


def exact_upper_sum(rho, p, count=250):
    q = rho * rho
    h = 1.0
    total = (1.0 - p)
    weight = 1.0
    for n in range(1, count + 1):
        weight *= p
        h /= (1.0 - q**n)
        total += (1.0 - p) * weight * h
    return total


def finite_binary_contraction_average(a, b, prob_b, depth):
    """Exact finite-tree expectation (up to floating arithmetic)."""
    leaves = [(1.0, 1.0, 1.0)]  # cumulative factor, denominator product, weight
    for _ in range(depth):
        nxt = []
        for cumulative, inverse_product, weight in leaves:
            aa = cumulative * a
            bb = cumulative * b
            nxt.append((aa, inverse_product / (1.0 - aa*aa), weight * (1.0-prob_b)))
            nxt.append((bb, inverse_product / (1.0 - bb*bb), weight * prob_b))
        leaves = nxt
    return sum(z*weight for _, z, weight in leaves)


def check_parameters(rho,c):
    p=c/rho
    lo=qproduct(lambda j: c**(2*j))
    hi=qproduct(lambda j: p*rho**(2*j))
    alternate=exact_upper_sum(rho,p)
    check(lo >= 1.0, 'lower prefactor >= 1')
    check(lo < hi, 'sharp envelopes separate')
    check(isclose(hi,alternate,rel_tol=2e-12,abs_tol=2e-12), 'geometric and Euler q products agree')
    return lo,hi


if __name__=='__main__':
    for rho,c in [(0.7,0.35),(0.6,0.2),(0.9,0.55),(0.4,0.1),(0.75,0.2),(0.65,0.4)]:
        check_parameters(rho,c)

    rho,c=0.7,0.35
    lower,upper=check_parameters(rho,c)
    for a,b in [(0.2,0.5),(0.1,0.55),(0.30,0.40)]:
        p=(c-a)/(b-a)
        for depth in [8,10,12]:
            partial=finite_binary_contraction_average(a,b,p,depth)
            check(lower < partial < upper, 'nondegenerate interior mean-preserving spread is strictly internal')
            # Omitted tail factor is nonnegative; globally bounded by rho^j.
            remainder=qproduct(lambda j: rho**(2*j), 250) / qproduct(lambda j: rho**(2*j), depth)
            check(partial <= partial*remainder < upper,'finite-product remainder sandwich')

    for rho,c in [(0.5,0.1),(0.65,0.15),(0.8,0.4),(0.9,0.45)]:
        p=c/rho
        lower,upper=check_parameters(rho,c)
        for n in range(1,30):
            q=rho*rho
            h=prod(1/(1-q**j) for j in range(1,n+1))
            check(h >= 1.0, 'nonnegative coefficients in Bernoulli expansion')
            check(h <= qproduct(lambda j:q**j)+1e-10, 'finite-product upper bound')
        # Compare a truncated geometric tail mixture with the infinite exact upper.
        for depth in [5,10,25,50]:
            partial=exact_upper_sum(rho,p,depth)
            check(partial <= upper*(1+1e-12),'finite geometric mixture below infinite value')
            # The missing weight is p**(depth+1).
            bound=qproduct(lambda j:q**j)*p**(depth+1)
            check(-1e-10 <= upper-partial <= bound+1e-10,'rigorous geometric-tail remainder (floating tolerance)')

    # Compare exact Laplace-sum upper tails with the q-product coefficient.
    # The signed exponential coefficients follow from partial fractions.
    for rho,p in [(0.6,0.4),(0.5,0.65)]:
        upper=qproduct(lambda j:p*rho**(2*j))
        def tail_finite_sum(n,x):
            total=0.0
            for j in range(n+1):
                coeff=prod(1.0/(1.0-rho**(2*(k-j))) for k in range(n+1) if k != j)
                total+=coeff*exp(-x/rho**j)
            return 0.5*total
        for x in (12.0,18.0):
            tail=0.0
            for n in range(21):
                tail+=(1-p)*p**n*tail_finite_sum(n,x)
            ratio=2.0*exp(x)*tail
            check(abs(ratio-upper)<0.005,'exact finite mixture tail approaches sharp prefactor')

    print('PASS: '+str(ASSERTIONS)+' independent finite assertions')
    print('example rho=0.7 c=0.35: lower=%.12f upper=%.12f'%check_parameters(0.7,0.35))
