"""Exact arithmetic checks for a two-state finite-randomness rounding law.

Tests are finite corroboration, not a substitute for the general proof.
"""
from fractions import Fraction as F


def stationary(K, eta, b):
    assert K >= 1 and K & (K-1) == 0
    assert F(0) < eta < F(1) and F(0) < b < F(1)
    v = K*eta
    pcount = (v*b).__floor__()
    qcount = -(v*(1-b)).__neg__().__floor__()  # ceil(v*(1-b))
    assert 0 <= pcount < K and 1 <= qcount <= K and pcount+qcount <= K
    p, q = F(pcount, K), F(qcount, K)
    pi = p/(p+q)
    assert pi*(1-q)+(1-pi)*p == pi
    assert 0 <= pi <= b
    return pi, p, q


def run():
    tested = 0
    # Many rational step sizes and rational targets, including exact ties.
    for K in (1, 2, 4, 8, 16, 32, 64):
        for den_eta in (3, 5, 7, 9, 16, 19):
            for num_eta in range(1,den_eta):
                eta = F(num_eta,den_eta)
                v = K*eta
                bound = min(F(1), F(1,1)/v)
                for den_b in (3, 4, 7, 11, 16, 19, 23, 37):
                    for num_b in range(1,den_b):
                        b = F(num_b,den_b)
                        pi,p,q = stationary(K,eta,b)
                        assert b-pi <= bound
                        lam = 1-p-q
                        assert 0 <= lam < 1
                        for init in (F(0),F(1)):
                            x0=init
                            # Two-step recurrence and spectral formula.
                            x1=(1-x0)*p+x0*(1-q)
                            x2=(1-x1)*p+x1*(1-q)
                            assert x1 == pi+(init-pi)*lam
                            assert x2 == pi+(init-pi)*lam**2
                        tested+=1
    # A rational witness within epsilon of the sharp supremum for v>1.
    for K in (2,4,8,16,32,64,128):
        for den_eta in (3,5,7,9,13):
            for num_eta in range(1,den_eta):
                eta = F(num_eta,den_eta)
                v = K*eta
                if v > 1:
                    # Approaches the critical target from below.
                    b = F(1,1)/v * (1-F(1,10**6))
                    pi,_,_=stationary(K,eta,b)
                    assert pi == 0
                    assert 0 < F(1,1)/v - (b-pi) < F(1,10**6)
                    tested+=1
                else:
                    pi,_,_=stationary(K,eta,F(999999,1000000))
                    assert pi == 0
                    tested+=1
    print(f"PASS: {tested} exact Markov and distortion evaluations; two-step identities for both initial states verified")


if __name__ == '__main__':
    run()
