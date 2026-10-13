"""Exact finite-horizon checks for scalar Gaussian-Hessian sketch reuse.

All calculations use rational arithmetic; infinite-moment conclusions follow
from integrability exponents in the associated proof, not from simulation.
"""
from fractions import Fraction as F
from math import comb


def inverse_moment(ell, power):
    """Return E(W^{-power}) for W=chi-square(ell)/ell, or None if infinite."""
    if power == 0:
        return F(1)
    if ell <= 2*power:
        return None
    out = F(1)
    for j in range(1,power+1):
        out *= F(ell, ell-2*j)
    return out


def one_block_even_moment(ell, eta, length):
    """E (1-eta/W)^(2 length), finite iff ell > 4 length."""
    if ell <= 4*length:
        return None
    q = 2*length
    total = F(0)
    for j in range(q+1):
        total += (-eta)**j * comb(q,j) * inverse_moment(ell,j)
    assert total > 0
    return total


def schedule_second_moment(ell, eta, segments):
    val = F(1)
    for r in segments:
        a = one_block_even_moment(ell, eta, r)
        if a is None:
            return None
        val *= a
    return val


def check():
    checks=0
    for ell in range(5,29):
        eta=F(ell-4,ell)
        assert one_block_even_moment(ell,eta,1)==F(2,ell-2)
        checks+=1
        for k in range(1,9):
            moment=one_block_even_moment(ell,eta,k)
            assert (moment is not None)==(ell>4*k)
            checks+=1
            assert schedule_second_moment(ell,eta,[1]*k)==F(2,ell-2)**k
            checks+=1
            for bound in range(1,k+1):
                pieces=[bound]+[1]*(k-bound)
                m=schedule_second_moment(ell,eta,pieces)
                assert (m is not None)==(ell>4*bound)
                checks+=1
    assert one_block_even_moment(6,F(1,3),1)==F(1,2)
    assert one_block_even_moment(6,F(1,3),2) is None
    assert schedule_second_moment(6,F(1,3),[1,1])==F(1,4)
    checks+=3
    print(f'PASS: {checks} exact-rational algebra and integrability boundary checks')
    print('ell=6, eta=1/3: fresh MSE at k=1,2 is 1/2,1/4; a repeated sketch has infinite MSE at k=2.')

if __name__=='__main__':
    check()
