"""Independent integer-coefficient checks for the slope-two Hartogs numerator identity.

Run with Python 3: python verify_slope_two.py
The universal unit-circle inequality is proved analytically in RESULT.md;
finite tests here check the derived coefficient formulas only.
"""
from math import gcd


def direct_numerator(n):
    """Compute diagonal Q from the five terms in Edholm--Mathew (1.4)."""
    m = 2*n+1
    k = m-n
    out = [0]*(2*k+1)
    out[k] += m*m
    for j in range(m-1):
        L = (1+n*(j+1)+m-1)//m
        kap = m+n-1+n*j-m*L
        terms = (
            (j-L+1, (j+1)*(kap+1)),
            (j-L+2, (j+1)*(m-kap-1)),
            (j-L+k+1, (m-j-1)*(kap+1)),
            (j-L+k+2, (m-j-1)*(m-kap-1)),
        )
        for degree, coefficient in terms:
            assert 0 <= degree <= 2*k
            out[degree] += coefficient
    return out


def claimed_numerator(n):
    k=n+1
    out=[0]*(2*k+1)
    out[0]=out[-1]=n
    for j in range(1,n+1):
        out[j]=out[-j-1]=(8*n-4)*j+2
    out[k]=8*n*n+4*n+1
    return out


def main():
    for n in range(1,501):
        assert gcd(2*n+1,n)==1
        direct=direct_numerator(n)
        predicted=claimed_numerator(n)
        assert direct==predicted, (n,direct,predicted)
        assert direct==direct[::-1]
        assert direct[0]==n and direct[n+1]==8*n*n+4*n+1
    print('PASS: full five-part formula and closed coefficients match for 1 <= n <= 500.')
    print('The infinite statement is proved by pairwise parity algebra and trigonometric estimates.')

if __name__ == '__main__':
    main()
