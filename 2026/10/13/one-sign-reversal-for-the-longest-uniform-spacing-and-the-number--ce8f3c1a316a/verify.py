"""Independent exact-arithmetic checks for a Dirichlet-spacing covariance identity.

Run: python3 verify.py
No third-party dependencies are required. Finite calculations are not proofs.
"""
from fractions import Fraction as Q
from math import comb


def h(n):
    return sum((Q(1, j) for j in range(1, n + 1)), Q(0))


def covariance_ie(m, t):
    """Inclusion-exclusion formula obtained by integration over a simplex."""
    z = (1 - t)**(m-1) * (1 + (m-1)*t - h(m))
    for j in range(1, m):
        w = max(Q(0), 1-(j+1)*t)
        z += Q((-1)**(j+1)*comb(m-1,j), j*(j+1))*w**m
    return z


def exceedance_win(m, s):
    """Exact P(B[0]+s exceeds all other components)."""
    return sum((Q((-1)**j*comb(m-1,j), j+1)
                *max(Q(0), 1-j*s)**(m-1)
                for j in range(m)), Q(0))


def win_integral(m, delta):
    z = delta
    for j in range(1, m):
        z += Q((-1)**j*comb(m-1,j), m*j*(j+1)) * (1 - max(Q(0), 1-j*delta)**m)
    return z


def covariance_conditional(m, t):
    d = t/(1-t)
    return m * (1-t)**m * (win_integral(m,d)-h(m)*d/m)


def low_threshold(m, t):
    return Q(1,m) - (1-t)**(m-1)*(Q(1,m)+h(m-1)*t)


def test():
    count = 0
    for m in range(2, 13):
        assert exceedance_win(m, Q(0)) == Q(1,m)
        assert exceedance_win(m, Q(1)) == Q(1)
        for k in range(1, 100):
            t=Q(k,100)
            x=covariance_ie(m,t)
            y=covariance_conditional(m,t)
            assert x==y, (m,k,x,y)
            if t <= Q(1,m):
                assert x==low_threshold(m,t), (m,k,x)
            if m==2:
                assert (x<0 if t<Q(1,2) else x>0 if t>Q(1,2) else x==0)
            elif t <= Q(1,m):
                assert x<0, (m,t,x)
            elif t >= Q(1,2):
                assert x>0, (m,t,x)
            count+=1
    assert covariance_ie(2,Q(1,2))==0
    print(f"PASS: {count} distinct exact rational covariance equalities; small-/large-threshold signs checked.")

if __name__ == '__main__':
    test()
