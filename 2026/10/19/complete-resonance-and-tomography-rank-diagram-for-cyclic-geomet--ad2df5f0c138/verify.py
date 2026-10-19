#!/usr/bin/env python3
"""Supplementary checks for geometric cyclic Gabor ambiguity classifications."""
import cmath
import math


def direct_ambiguity(n, gamma, k, b):
    omega = cmath.exp(2j * math.pi / n)
    g = [gamma ** j for j in range(n)]
    return sum(g[j].conjugate() * g[(j - k) % n] * omega ** (b * j)
               for j in range(n))


def formula_ambiguity(n, gamma, k, b):
    omega = cmath.exp(2j * math.pi / n)
    z = abs(gamma)**2 * omega**b
    w = gamma**n
    if abs(z - 1) < 1.e-10:
        assert abs(abs(gamma)-1) < 1.e-10 and b == 0
        return gamma**(-k) * (k*w + n-k)
    return gamma**(-k) * (w - abs(w)**2 + (1-w)*z**k) / (1-z)


def predicted_zero(n, gamma, k, b):
    radius = abs(gamma)
    w = gamma**n
    if abs(radius-1) > 1.e-9:
        return (n % 2 == 0 and k == n//2 and abs(w.imag) < 1.e-8
                and (b % 2 == (1 if w.real > 0 else 0)))
    if abs(w-1) < 1.e-8:
        return b != 0
    return (b != 0 and (b*k) % n == 0) or (
        b == 0 and n % 2 == 0 and k == n//2 and abs(w+1) < 1.e-8)


def rank_formula(n, gamma):
    r = abs(gamma)
    w = gamma**n
    if abs(r-1) > 1.e-9:
        return n*n - (n//2 if n%2==0 and abs(w.imag)<1.e-8 else 0)
    if abs(w-1) < 1.e-8:
        return n
    return (n*n + n - sum(math.gcd(k, n) for k in range(n))
            - int(n%2==0 and abs(w+1)<1.e-8))


def intensity(n, gamma, vec):
    g = [gamma**j for j in range(n)]
    out = []
    for k in range(n):
        for b in range(n):
            v = [cmath.exp(2j*math.pi*b*j/n)*g[(j-k)%n]
                 for j in range(n)]
            out.append(abs(sum(v[j].conjugate()*vec[j] for j in range(n)))**2)
    return out


def main():
    total=0
    for n in range(3,15):
        gammas = [1.17+0j, 1.17*cmath.exp(1j*math.pi/n),
                  1.17*cmath.exp(0.37j), 1+0j,
                  cmath.exp(0.47j), cmath.exp(1j*math.pi/n),
                  cmath.exp(2j*math.pi/n)]
        for gamma in gammas:
            count=0
            for k in range(n):
                for b in range(n):
                    val=direct_ambiguity(n,gamma,k,b)
                    ana=formula_ambiguity(n,gamma,k,b)
                    assert abs(val-ana)<1.e-6*(1+abs(val)), (n,gamma,k,b,val,ana)
                    zero=abs(val)<1.e-7
                    assert zero==predicted_zero(n,gamma,k,b),(n,gamma,k,b,zero)
                    count+=zero
                    total+=1
            assert n*n-count==rank_formula(n,gamma),(n,gamma,count)
    ambiguities=0
    for n in (4,6,8,10):
        for negative in (False,True):
            gamma=1.17*cmath.exp(1j*(math.pi/n if negative else 0))
            m=n//2
            x=[0j]*n; y=[0j]*n
            x[0]=y[0]=1.
            x[m]=(1+0j if negative else 1j)
            y[m]=-x[m]
            lhs=intensity(n,gamma,x)
            rhs=intensity(n,gamma,y)
            assert max(abs(a-b) for a,b in zip(lhs,rhs))<1.e-7
            ambiguities+=1
        gamma=cmath.exp(0.37j)
        x=[0j]*n; y=[0j]*n
        x[0]=1; y[1]=1
        assert max(abs(a-b) for a,b in zip(intensity(n,gamma,x),intensity(n,gamma,y)))<1.e-7
        ambiguities+=1
    print(f'VERIFY_OK {total} direct-vs-formula / zero-pattern comparisons; {ambiguities} independent ambiguity witnesses; N=3..14')

if __name__=='__main__':
    main()
