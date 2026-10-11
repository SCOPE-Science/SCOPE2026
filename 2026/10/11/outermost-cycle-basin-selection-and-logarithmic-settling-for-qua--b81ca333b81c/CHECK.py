"""Finite exact-arithmetic checks for the basin partition of quantized affine contractions.

Run: python CHECK.py
These tests are finite consistency tests; the included mathematical proof is general.
"""
from fractions import Fraction
from math import floor, log


def check(r, mu):
    assert 0 < r < 1
    def f(n):
        return floor(mu-r*n)
    def g(n):
        return f(f(n))
    q=mu/(1+r)
    M = floor(abs(q)+2/(1-r))+12
    fixed=[n for n in range(-M,M+1) if g(n)==n]
    assert fixed
    L,U=fixed[0],fixed[-1]
    assert fixed==list(range(L,U+1))
    for n in fixed:
        assert f(n)==L+U-n
    for n in range(-M-100, M+101):
        z=n
        for _ in range(2*M+200):
            if L<=z<=U:
                break
            z=g(z)
        else:
            raise AssertionError(('non-termination',r,mu,n))
        assert z==(L if n<L else U if n>U else n)
    for k in range(-300,301):
        x=Fraction(k,4)
        n=f(x)
        interior=(L<n<U)
        external=(x<=((mu-U)/r) or x>((mu-L-1)/r))
        if L<U:
            assert (not interior)==external
        for m in range(L+1,U):
            in_cell= ((mu-m-1)/r)<x<=((mu-m)/r)
            assert (n==m)==in_cell
    for n in [10**k for k in range(1,8)]:
        z=n;t=0
        while not(L<=z<=U):
            z=g(z);t+=1
            assert t<4000
        # Displays residuals but does not assert any universal finite-N bound.
        residual=t-log(n)/(-2*log(float(r)))
        assert abs(residual)<150
    return len(fixed),L,U


if __name__=='__main__':
    count=0
    for r in [Fraction(1,10),Fraction(1,3),Fraction(3,5),Fraction(7,10),Fraction(9,10),Fraction(49,50)]:
        for mu in [Fraction(-3,2),Fraction(0),Fraction(1,4),Fraction(1,2),Fraction(7,10),Fraction(11,5)]:
            result=check(r,mu)
            count+=1
            if (r,mu)==(Fraction(9,10),Fraction(1,2)):
                assert result==(9,-4,4)
                print('example: r=9/10, mu=1/2, [L,U]=[-4,4]')
    print('CHECK_OK:',count,'exact parameter cases and orbit/basin samples')
