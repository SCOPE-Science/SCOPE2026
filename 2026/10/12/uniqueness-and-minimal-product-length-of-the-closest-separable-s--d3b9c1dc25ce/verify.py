from fractions import Fraction
import math, cmath


def binom(n,k):
    return math.comb(n,k)


def exact_checks():
    for n in range(2, 11):
        for s in (Fraction(1,5), Fraction(1,3), Fraction(2,3), Fraction(4,5)):
            p=(1-s)/n
            q=(n-1+s)/n
            t=p/q
            assert p+q == 1
            assert s/q**n == (1-(n-1)*t)*(1+t)**(n-1)
            assert 1/q**(n-1) == (1+t)**(n-1)
            weights=[Fraction(binom(n,k))*p**k*q**(n-k) for k in range(n+1)]
            assert all(w>0 for w in weights)
            assert sum(weights)==1
            assert weights[0]==q**n
            assert weights[1]==(1-s)*q**(n-1)
            # Exact tangent inequality on a rational grid; universal proof is convexity.
            for j in range(0, 21):
                Q=Fraction(j,7)
                lhs=(1+Q)**n
                rhs=(1+t)**(n-1)*(1-(n-1)*t+n*Q)
                assert lhs >= rhs
                if Q==t:
                    assert lhs==rhs


def root_checks():
    for n in range(2, 21):
        N=n+1
        for m in range(1,n+1):
            z=sum(cmath.exp(2j*math.pi*j*m/N) for j in range(N))/N
            assert abs(z) < 2e-13


def main():
    exact_checks()
    root_checks()
    print('VERIFY_OK')
    print('exact_dimensions = 2..10')
    print('root_dimensions = 2..20')
    print('note = finite checks supplement the analytic proof')

if __name__=='__main__':
    main()
