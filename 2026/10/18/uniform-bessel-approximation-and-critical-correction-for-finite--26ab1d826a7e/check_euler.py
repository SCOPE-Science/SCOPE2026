"""Independent finite-dimensional checks for Euler-matrix Hilbert--Schmidt energy.

Requires only the Python standard library. Finite tests complement, and do not
replace, the integral and inequality arguments in RESULT.md.
"""
import math
from fractions import Fraction


def i0_i1(z):
    a0, a1 = 1.0, z / 2.0
    b0, b1 = a0, a1
    for k in range(1, 1000):
        a0 *= z*z/(4*k*k)
        a1 *= z*z/(4*k*(k+1))
        b0 += a0
        b1 += a1
        if max(abs(a0),abs(a1)) < 1e-16*max(1.0,abs(b0),abs(b1)):
            return b0, b1
    raise RuntimeError("Bessel series did not converge")


def energy(N, r):
    total = 0.0
    for n in range(N):
        p = (1-r)**n
        for k in range(n+1):
            total += p*p
            if k < n:
                p = p*(n-k)/(k+1)*r/(1-r)
    return total


def heat(N, beta):
    z = 2*N*beta
    i0, i1 = i0_i1(z)
    return N*math.exp(-z)*(i0+i1)


def correction(lam):
    z=2*lam
    i0,i1 = i0_i1(z)
    return lam*math.exp(-z)*(i0-i1)


def rational_middle(N):
    total = Fraction(0)
    for n in range(N):
        total += Fraction(math.comb(2*n,n),4**n)
    predicted = Fraction((2*N-1)*math.comb(2*N-2,N-1),4**(N-1))
    return total == predicted


def main():
    count=0
    for N in [1,2,3,4,8,13,25,40]:
        assert rational_middle(N)
        count+=1
        for r in [.01,.03,.1,.25,.5,.75,.9,.97,.99]:
            actual=energy(N,r)
            proxy=heat(N,r*(1-r))
            assert -3e-10 < actual-proxy < .5+3e-10, (N,r,actual,proxy)
            assert abs(actual-energy(N,1-r)) < 1e-8
            count+=1
    for lam in [.05,.1,.3,1,2,3]:
        L=3
        for N in [32,64,128]:
            beta=lam/N
            r=(1-math.sqrt(1-4*beta))/2
            rem=abs(energy(N,r)-heat(N,beta)-correction(lam))
            bound=(32*L*L/3+200*L**3/9)/N
            assert rem <=bound + 1e-8, (lam,N,rem,bound)
            count+=1
    print('CHECK_OK',count,'finite tests; no claim of exhaustive proof')


if __name__=='__main__':
    main()
