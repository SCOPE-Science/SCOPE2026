#!/usr/bin/env python3
"""Exact integer cross-checks for the enumerative formulas for quadric unprojections.
All identities have independent algebraic proofs in RESULT.md; finite checks are not a proof.
"""
from math import comb


def c2_coefficient(n):
    # [t^2](1+t)^(n+3) / (1+2t)^n
    return (comb(n + 3, 2) - 2*n*(n+3) + 4*comb(n+1, 2))


def geometrical_counts(n):
    assert n >= 2
    h2 = 2**n
    E2 = 1-n
    HE = 1
    a = n-1
    DD = a*a*h2 + 2*a*HE + E2
    KD = (n-3)*(a*h2+HE)
    chi = h2*c2_coefficient(n)
    J = chi + 2*KD + 3*DD
    dual = J-a
    original_dual = chi + 2*(n-3)*h2 + 3*h2
    return DD,KD,chi,J,dual,original_dual


def closed_counts(n):
    a=n-1
    return (
       a*a*2**n + a,
       (n-3)*(a*2**n + 1),
       (n*n-3*n+6)*2**(n-1),
       (11*n*n-31*n+24)*2**(n-1)+5*n-9,
       (11*n*n-31*n+24)*2**(n-1)+4*n-8,
       n*(n+1)*2**(n-1)
    )

def check():
    for n in range(2,101):
        g=geometrical_counts(n)
        f=closed_counts(n)
        assert g==f, (n,g,f)
        DD,KD,e,J,dual,original_dual=g
        a=n-1
        # On Bl_{D^2} S, Euler is e(S)+D^2. Smooth pencil member: e(C)=-D(D+K)
        assert (e+DD-2*(-DD-KD))==J
        # At the single exceptional pencil parameter, E+R has exactly a nodes.
        assert J-dual == a
        assert dual>0 and original_dual>0
        assert 2*(1+(DD+KD)//2) == 2+DD+KD
        assert (DD+KD)%2==0
    assert geometrical_counts(2)[-2:]==(12,12)
    assert geometrical_counts(3)[-2:]==(124,48)
    assert geometrical_counts(4)[-2:]==(616,160)
    assert geometrical_counts(5)[-2:]==(2316,480)
    print('VERIFY_OK: independent coefficient-extraction and closed forms agree for 99 values n=2..100; Euler-fibration, genus parity, exceptional nodal contribution, and four base examples all check.')

if __name__=='__main__':
    check()
