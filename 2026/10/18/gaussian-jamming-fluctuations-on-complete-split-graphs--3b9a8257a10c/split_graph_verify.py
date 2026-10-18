#!/usr/bin/env python3
"""Standalone checks for random-priority dimer deposition on complete split graphs.

No external packages are needed. Finite verification supports, but does not prove,
the asymptotic limit theorem and the central limit theorem.
"""
from fractions import Fraction
from itertools import permutations
from math import exp, isclose
from collections import Counter


def exact_moments(A, B):
    """Compute terminal A-population moments by the independent count-chain recurrence."""
    mean = [[Fraction(0) for _ in range(B+1)] for _ in range(A+1)]
    second = [[Fraction(0) for _ in range(B+1)] for _ in range(A+1)]
    for a in range(A+1):
        mean[a][0] = Fraction(a)
        second[a][0] = Fraction(a*a)
    for b in range(1,B+1):
        for a in range(A+1):
            ab = a*b
            bb = b*(b-1)//2
            if not ab+bb:
                continue
            p = Fraction(ab, ab+bb)
            q = 1-p
            mean[a][b] = (p*mean[a-1][b-1] if ab else 0) + (q*mean[a][b-2] if bb else 0)
            second[a][b] = (p*second[a-1][b-1] if ab else 0) + (q*second[a][b-2] if bb else 0)
    return mean[A][B], second[A][B]


def numerical_moments(A, B):
    """An independent floating point dynamic-programming implementation."""
    m = [[0.0]*(B+1) for _ in range(A+1)]
    s = [[0.0]*(B+1) for _ in range(A+1)]
    for a in range(A+1):
        m[a][0] = float(a)
        s[a][0] = float(a*a)
    for b in range(1, B+1):
        for a in range(A+1):
            w1 = a*b
            w2 = b*(b-1)/2
            if w1+w2 == 0: continue
            p = w1/(w1+w2)
            m[a][b] = p*m[a-1][b-1] + (1-p)*m[a][b-2]
            s[a][b] = p*s[a-1][b-1] + (1-p)*s[a][b-2]
    return m[A][B], max(0, s[A][B]-m[A][B]**2)


def brute_priority(A, B):
    N = A+B
    edges = [(i,j) for i in range(N) for j in range(i+1,N)
             if i >= A or j >= A]
    counts = Counter()
    for ordering in permutations(edges):
        unoccupied = (1<<N)-1
        for i,j in ordering:
            mask = (1<<i)|(1<<j)
            if (unoccupied&mask) == mask:
                unoccupied ^= mask
        counts[(unoccupied & ((1<<A)-1)).bit_count()] += 1
    total = sum(counts.values())
    mean = Fraction(sum(k*v for k,v in counts.items()), total)
    second = Fraction(sum(k*k*v for k,v in counts.items()), total)
    return mean,second,counts,total


def asymptotics(alpha):
    L = (1-alpha)/alpha
    r = alpha*exp(-L)
    v = r*(4-(L+2)**2 * exp(-L))
    return r,v


def main():
    print('Physical random-edge enumeration vs an independent count Markov chain:')
    for A,B in ((1,3),(2,2),(2,3)):
        physical_m,physical_s,c,t = brute_priority(A,B)
        chain_m,chain_s = exact_moments(A,B)
        assert (physical_m,physical_s)==(chain_m,chain_s)
        print('A,B=',A,B,'orders=',t,'counts=',dict(c),
              'E=',str(chain_m),'E2=',str(chain_s))
    print('Exact rational dynamic-programming moments for small populations:')
    for A in range(1,6):
        for B in range(0,7):
            x,y=exact_moments(A,B)
            xm,vs=numerical_moments(A,B)
            assert isclose(xm,float(x),abs_tol=1e-10)
            assert isclose(vs,float(y-x*x),abs_tol=1e-10)
    print('35 exact rational comparisons passed.')
    print('Limit constants and independent finite-count moments:')
    for alpha in (0.2,0.35,0.5,0.7):
        r,v=asymptotics(alpha)
        assert 0<r<alpha and v>0
        for N in (300,600,1200):
            A=round(alpha*N)
            mean,variance=numerical_moments(A,N-A)
            print(f'alpha={alpha:.2f} N={N} E[Afinal]/N={mean/N:.9f} '
                  f'N*Var[Afinal/N]={variance/N:.9f} '
                  f'target_mean={r:.9f} target_variance={v:.9f}')
            assert abs(mean/N-r)<max(.006,5/N)
            assert abs(variance/N-v)<.012
    # The quadratic-variation integral can be evaluated explicitly.
    # This quadrature uses midpoint Riemann sums, independently of the formula.
    for alpha in (0.15,0.3,0.5,0.8):
        r,v=asymptotics(alpha)
        L=(1-alpha)/alpha
        steps=50000
        du=L/steps
        integral=r*du*sum(exp(-(k+0.5)*du)*(((k+0.5)*du)**2+2*(k+0.5)*du)
                          for k in range(steps))
        assert abs(integral-v)<1e-7
        print('variance-integral alpha=',alpha,'quadrature=',integral,'formula=',v)
    print('All verification checks passed; finite checks are not CLT proofs.')


if __name__=='__main__':
    main()
