"""Exact binomial-series checks for inner-function Hardy objective sensitivity.
Uses only Python's standard library. No finite check is used as an infinite proof.
"""
from fractions import Fraction
from math import comb


def bcoeff(alpha, j):
    v = Fraction(1)
    for k in range(j):
        v *= (alpha - k) / (k + 1)
    return (-1)**j * v


def fjet(m, a, cutoff, shift=False):
    stride = m + (1 if shift else 0)
    f = [Fraction(0)] * (cutoff+1)
    f[0] = a
    for t in range(1, cutoff // stride+1):
        f[t*stride] = -(1-a*a) * a**(t-1)
    return f


def product(a,b,cutoff):
    c = [Fraction(0)]*(cutoff+1)
    for i,x in enumerate(a):
        if not x or i > cutoff: continue
        for j,y in enumerate(b):
            if i+j>cutoff: break
            c[i+j] += x*y
    return c


def moment_coeff(f, alpha, T):
    v = Fraction(0)
    for j in range(T+1):
        k = T-j
        if j<k: continue
        bj = bcoeff(alpha,j); bk=bcoeff(alpha,k)
        if j==k:
            v += bj*bk*comb(2*j,j)
            continue
        pow_f = [Fraction(0)]*(k+1); pow_f[0]=1
        ft=f[:k+1]
        for _ in range(j-k):
            pow_f=product(pow_f,ft,k)
        # coefficient of z^t in (1+z)^j f^(j-k), matched to z^-t of (1+z^-1)^k
        integral = Fraction(0)
        for t in range(k+1):
            coeff=sum(comb(j,h)*pow_f[t-h] for h in range(min(j,t)+1))
            integral += comb(k,t)*coeff
        v += 2*bj*bk*integral
    return v


def test():
    cases = 0
    for alpha in [Fraction(1,2),Fraction(3,2),Fraction(5,2),Fraction(7,4)]:
        for a in [Fraction(1,2), Fraction(1,3)]:
            for m in range(1,10):
                F=fjet(m,a,m)
                G=fjet(m,a,m,True)
                diff=[moment_coeff(F,alpha,t)-moment_coeff(G,alpha,t) for t in range(2*m+2)]
                assert not any(diff[:2*m+1]),(alpha,a,m,diff)
                expected=-2*(1-a*a)*bcoeff(alpha,m)*bcoeff(alpha,m+1)
                assert diff[2*m+1]==expected!=0,(alpha,a,m,diff[-1],expected)
                cases+=1
    print(f'PASS: exact rational coefficient test for {cases} parameter triples; each onset is order 2m+1')
    alpha=Fraction(3,2); a=Fraction(1,2); m=3
    expected=-2*(1-a*a)*bcoeff(alpha,m)*bcoeff(alpha,m+1)
    print(f'Example p=3, a=1/2, m=3: Taylor coefficient [lambda^7] difference = {expected}')

if __name__=='__main__':test()
