#!/usr/bin/env python3
from fractions import Fraction as F

def pieces(u, t, a):
    N = u*u + 4*t*a*u + 2*t*t*(a*a + 1)
    Q = t*t*u*u + 2*t*a*(t*t + 1)*u + t**4 + 2*t*t*a*a + 1
    P = 2*t**3*a**3 + 2*t*t*a*a*u + t*a*u*u + 2*t*a + t*t*u + u
    dN = 2*u + 4*t*a
    dQ = 2*t*t*u + 2*t*a*(t*t + 1)
    R = (
        t*t*u**4 + 4*t**3*a*u**3 + 4*t*a*u**3
        + 6*t**4*a*a*u*u + t**4*u*u + 14*t*t*a*a*u*u + 3*u*u
        + 8*t**5*a*u + 16*t**3*a**3*u + 8*t*a*u
        + 2*t**6*a*a + 2*t**6 + 4*t**4*a**4
        + 4*t**4*a*a + 2*t*t*a*a + 2*t*t
    )
    return N, Q, P, dN, dQ, R

def main():
    vals = [F(1,7), F(1,3), F(2,3), F(1), F(3,2), F(5), F(17,3)]
    checks = 0
    for u in vals:
        for t in vals:
            for a in vals:
                N,Q,P,dN,dQ,R = pieces(u,t,a)
                assert dN*Q - N*dQ == -2*(t*t-1)*P
                assert N*Q - 2*u*(t*t-1)*P == R
                assert N > 0 and Q > 0 and P > 0 and R > 0
                if t > 1:
                    num = 2*u*(t*t-1)*P
                    assert 0 < num < N*Q
                if t < 1:
                    assert dN*Q - N*dQ > 0
                if t == 1:
                    assert N == Q
                checks += 1
    print(f"VERIFY_OK exact_rational_cases={checks}")

if __name__ == "__main__":
    main()
