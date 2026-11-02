#!/usr/bin/env python3
"""Exact arithmetic checks of the eight quasipolynomial Turan factorizations."""
from fractions import Fraction
from math import comb, factorial, prod

# m: (r, integer normalizing denominator, W_even numerator & denominator,
#     W_odd numerator & denominator, low-to-high coefficients P_even, P_odd)
DATA = {
    4: (5, 907200, ((), ()), ((6,), (1,)),
        (63, 24, 4), (21, 28, 4)),
    5: (7, 457228800, ((), (7,)), ((), (1,)),
        (126, 75, 22, 2), (90, 107, 26, 2)),
    6: (8, 36212520960000, ((), ()), ((9,), (1,)),
        (22275, 18000, 7184, 1152, 64),
        (22275, 27360, 9136, 1280, 64)),
    7: (10, 93211028951040000, ((), (10,)), ((), (1,)),
        (70785, 73128, 36308, 8104, 832, 32),
        (99099, 129096, 53012, 10216, 928, 32)),
}

def choose_polynomial_upper(u, d):
    """Polynomial binomial(u,d), valid also for u<d."""
    return Fraction(prod(u-i for i in range(d)), factorial(d))

def quasi_coeff(m, t, e):
    """Quasipolynomial evaluation at n=2t+e, e=0 or 1."""
    return sum((comb(m,j)*choose_polynomial_upper(t-(j-e)//2+2*m-1,2*m-1)
                for j in range(e,m+1,2)), Fraction(0))

def independent_count(m, n):
    """Direct two-colour-level partition count: j twos and n-2j ones."""
    if n<0: return 0
    return sum(comb(j+m-1,m-1)*comb(n-2*j+m-1,m-1)
               for j in range(n//2+1))

def factor_rhs(m, t, e):
    r, den, we, wo, pe, po = DATA[m]
    fn,fd = we if e==0 else wo
    poly = pe if e==0 else po
    val = Fraction(prod((t+j)**2 for j in range(1,r+1)),den)
    val *= Fraction(prod(t+j for j in fn),prod(t+j for j in fd))
    val *= sum(c*t**i for i,c in enumerate(poly))
    return val

def run():
    identities = counts = 0
    for m in range(4,8):
        # Each coefficient quasipolynomial has degree at most 2m-1.
        # The difference of three products has degree <=4m-2;
        # 4m-1 evaluations therefore rigorously determine the identity.
        for e in (0,1):
            for t in range(4*m-1):
                a = quasi_coeff(m,t,e)
                if e==0:
                    lo = quasi_coeff(m,t-1,1)
                    hi = quasi_coeff(m,t,1)
                else:
                    lo = quasi_coeff(m,t,0)
                    hi = quasi_coeff(m,t+1,0)
                delta = a*a-lo*hi
                rhs = factor_rhs(m,t,e)
                assert delta == rhs, (m,t,e,delta,rhs)
                assert rhs > 0
                identities += 1
        assert quasi_coeff(m,-1,1)==0  # Correct boundary at n=0.
        for n in range(129):
            assert quasi_coeff(m,n//2,n%2) == independent_count(m,n)
            if n>=1:
                a0 = independent_count(m,n-1)
                a1 = independent_count(m,n)
                a2 = independent_count(m,n+1)
                assert a1*a1 > a0*a2
            counts += 1
    for m in range(1,4):
        assert m*m - m*(m+3)//2 <= 0
    print(f'PASS: {identities} polynomial-identity evaluations (degree bounds prove identities), '
          f'{counts} independent coefficient comparisons and strict checks, exact boundary and sharpness.')

if __name__ == '__main__':
    run()
