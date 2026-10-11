"""Exact finite rational replay of an explicit neutral-interval construction.

Not a proof by enumeration: the all-word proof appears in RESULT.md.
Python standard library only.
"""
from itertools import product
from fractions import Fraction


def construct(base_prefix, center_prefix, M):
    r, k = len(base_prefix), len(center_prefix)
    assert M >= 2 and k >= 1
    c = sum(d < M for d in base_prefix)
    p = r-c
    h = max(k,p)
    H = c-p+h
    assert H >= c
    center_word = tuple(center_prefix) + (0,)*(h-k)
    base_word = tuple(base_prefix) + (M,)*H + tuple(reversed(center_word))
    N = len(base_word)
    assert N == 2*(c+h) <= 2*(r+k)
    return base_word, center_word, h


def base_fixed(word, M, a):
    scale = Fraction(1)
    offset = Fraction(0)
    for d in word:
        if d < M:
            t, b = a, a*d
        else:
            t, b = 1-M*a, M*a
        offset += scale*b
        scale *= t
    assert 0 < scale < 1
    return offset/(1-scale)


def forward(word, M, a, x, z):
    for d in word:
        if x < M*a:
            actual = x//a
            assert actual == d, (word,d,actual,x)
            x = (x-a*d)/a
            z = (z+d)/M
        else:
            assert d == M
            x=(x-M*a)/(1-M*a)
            z=M*z-(M*z//1)
    return x,z

for M in (2,3,4):
 for a in (Fraction(1,M+1),Fraction(1,2*M+1), Fraction(2,2*M+1)):
  for r in range(0,4):
   for k in range(1,4):
    for u in product(range(M+1),repeat=r):
     for v in product(range(M),repeat=k):
      w,b,h=construct(u,v,M)
      x=base_fixed(w,M,a)
      j=sum(t*M**(h-i-1) for i,t in enumerate(b))
      low=Fraction(j,M**h)
      target=Fraction(sum(t*M**(k-i-1) for i,t in enumerate(v)),M**k)
      assert target<=low and low+Fraction(1,M**h)<=target+Fraction(1,M**k)
      for t in (Fraction(1,3),Fraction(2,3)):
       z=low+t/M**h
       assert forward(w,M,a,x,z)==(x,z),(M,a,u,v,w,x,z)
print('PARAMETER_UNIFORM_NEUTRAL_LOCALIZATION_CHECK_OK')
