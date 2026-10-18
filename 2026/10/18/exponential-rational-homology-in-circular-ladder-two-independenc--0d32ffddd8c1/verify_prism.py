#!/usr/bin/env python3
"""Independent exact checks for a circular-ladder higher-independence theorem.
Requires Python >=3.9 and sympy. All computations are integral/rational.
"""
from collections import Counter
from fractions import Fraction
import sympy as S

def transfer(z):
    m = S.zeros(16,16)
    for a in range(4):
      for b in range(4):
        for c in range(4):
          valid = True
          for r in (0,1):
            if b & (1<<r):
              deg = int(bool(a&(1<<r))) + int(bool(c&(1<<r))) + int(bool(b&(1<<(1-r))))
              if deg > 1: valid=False
          if valid: m[4*a+b,4*b+c] = z**(c.bit_count())
    return m

def brute_poly(n):
    # Deliberately separate from the triple-state automaton:
    # inspect each selected vertex's actual neighbors in the graph.
    neighbors = [0]*(2*n)
    for i in range(n):
      for row in (0,1):
        v=2*i+row
        for w in (2*((i-1)%n)+row, 2*((i+1)%n)+row,2*i+(1-row)):
          neighbors[v]|=1<<w
    coeff=[0]*(2*n+1)
    for mask in range(1<<(2*n)):
      subset=mask
      good=True
      while subset:
        lsb=subset & -subset
        v=lsb.bit_length()-1
        if (neighbors[v]&mask).bit_count()>1:
          good=False
          break
        subset-=lsb
      if good:coeff[mask.bit_count()]+=1
    return coeff

def check():
    z,t=S.symbols('z t')
    M=transfer(z)
    A=S.factor(M.charpoly(t).as_expr())
    expected=t**10*(t**2+z*t+z*z)*(t**4-(z+1)*t**3-(2*z*z+z)*t*t+(z**3-z*z)*t+z**4)
    assert S.expand(A-expected)==0, (A,expected)
    # Directly check the full polynomial for n=3..8. Such finite checks alone do not establish the theorem.
    Mk=S.eye(16)
    for n in range(1,9):
      Mk=Mk*M
      if n>=3:
        tr=S.Poly(S.trace(Mk),z)
        f=brute_poly(n)
        assert [int(tr.nth(j)) for j in range(2*n+1)]==f,(n,tr,f)
    signed=transfer(S.Integer(-1))
    signed_char=S.factor(signed.charpoly(t).as_expr())
    assert signed_char==t**10*(t*t-t+1)*(t**4-t*t-2*t+1)
    expected_values=[1,1,4,-3,11,10,1,29,4,21,67,6,105,113,44,317,171,298,761]
    W=S.eye(16)
    for n in range(1,20):
      W=W*signed
      assert S.trace(W)==expected_values[n-1],(n,S.trace(W))
    assert all(x>0 for x in expected_values[4:])
    assert expected_values[2]>0 and expected_values[3]<0
    q=lambda x:x**4-x**2-2*x+1
    a=Fraction(1386,1000); b=Fraction(1387,1000)
    c=Fraction(425,1000); d=Fraction(430,1000)
    assert q(c)>0 and q(d)<0 and q(a)<0 and q(b)>0
    # |complex roots|^2 = 1/(alpha*delta). Upper bound 1.31 exact.
    rho=Fraction(131,100)
    assert 1/(a*c)<rho*rho
    # For n >= 20 the worst ratio occurs n=20; the terms strictly decrease.
    assert 2*(rho/a)**20+(d/a)**20+2/(a**20)<S.Rational(2,3)
    print('VERIFIED_CIRCULAR_LADDER_SIGNED_HIGHER_INDEPENDENCE',
          'symbolic_charpoly=exact','independent_bruteforce=3..8',
          'signed_initial_terms=1..19','rational_root_certificates=exact')
if __name__=='__main__':check()
