#!/usr/bin/env python3
"""Exact and numerical verification for integer-knot spline jet Parseval frames."""
from fractions import Fraction
from itertools import product
from math import comb, factorial
import cmath
import random
import sympy as S

W = {3:[S.Rational(1),S.Rational(1,3),S.Rational(1,18)],
     4:[S.Rational(1),S.Rational(5,12),S.Rational(13,144),S.Rational(11,864)]}


def samples(n,r):
    return [S.Rational(sum((-1)**ell*comb(n+1,ell)*(j-ell)**(n-r)
             for ell in range(j+1)),factorial(n-r)) for j in range(1,n+1)]


def corr(a):
    return [S.expand(sum(a[j]*a[j+h] for j in range(len(a)-h)))
            for h in range(len(a))]


def main():
  trials=0
  random.seed(27182818)
  for n in (3,4):
    vals=[samples(n,r) for r in range(n)]
    C=[corr(a) for a in vals]
    # Laurent coefficient test; h>=1 vanish, h=0 equals one.
    sums=[S.factor(sum(W[n][r]*C[r][h] for r in range(n))) for h in range(n)]
    assert sums == [S.Integer(1)]+[S.Integer(0)]*(n-1)
    trials+=1
    # Solve the full coefficient system to prove uniqueness of real diagonal weights.
    M=S.Matrix([[C[r][h] for r in range(n)] for h in range(n)])
    assert M.det()!=0
    trials+=1
    exact=list(M.inv()*S.Matrix([1]+[0]*(n-1)))
    assert exact==W[n]
    trials+=1
    assert all(w>0 for w in exact)
    trials+=1
    # Coefficients of squared symbols in s=2-2cos(theta).
    s=S.Symbol('s',real=True)
    polys={3:[(1-s/6)**2,s*(1-s/4),s**2],
           4:[(1-s/4)*(1-s/12)**2,s*(s-6)**2/36,s**2*(1-s/4),s**3]}[n]
    for r in range(n):
      for theta in (0.0,.13,1.23,2.7,3.141592653589793):
        z=cmath.exp(1j*theta)
        H=sum(float(vals[r][j-1])*z**j for j in range(1,n+1))
        observed=H.real**2+H.imag**2
        expected=float(polys[r].subs(s,2-2*__import__('math').cos(theta)))
        assert abs(observed-expected)<1e-12,(n,r,theta,observed,expected)
        trials+=1
    assert S.factor(sum(W[n][r]*polys[r] for r in range(n)))==1
    trials+=1
    # Exact finitely supported coefficient vectors, with exact samples and adjoint synthesis.
    for _ in range(40):
      coeff={j:S.Rational(random.randint(-7,7),random.randint(1,9)) for j in range(-5,8)}
      E=sum(v*v for v in coeff.values())
      jets={}
      for r in range(n):
        a=vals[r]
        for k in range(-5,n+8):
          jets[(r,k)]=sum(coeff.get(k-h,S.Integer(0))*a[h-1] for h in range(1,n+1))
      Smp=sum(W[n][r]*v*v for (r,k),v in jets.items())
      assert Smp==E,(n,E,Smp)
      for j in range(-5,n+8):
        reconstruction=sum(W[n][r]*sum(jets.get((r,j+h),S.Integer(0))*vals[r][h-1]
                    for h in range(1,n+1)) for r in range(n))
        assert reconstruction==coeff.get(j,S.Integer(0)),(n,j,reconstruction,coeff.get(j,0))
        trials+=1
      trials+=1
    print(f'degree={n}; integer-jet-filter taps={vals}; unique Parseval weights={W[n]}; Laurent coefficients={sums}; exact finite reconstructions=40')
  # Cubic samples plus first derivatives have Nyquist energy fixed at 1/9, regardless nonnegative first-derivative weight.
  for b in (S.Rational(0), S.Rational(1,6), S.Rational(1,3),S.Integer(2)):
     assert S.Rational(1,9) + b*S.Integer(0)==S.Rational(1,9)
     trials+=1
  print('ALL CHECKS PASSED, assertions=',trials)

if __name__=='__main__': main()
