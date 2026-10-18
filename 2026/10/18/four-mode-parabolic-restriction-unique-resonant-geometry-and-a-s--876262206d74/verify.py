#!/usr/bin/env python3
"""Standalone reproducibility checks of exact four-mode parabolic moment identities.

All enumerations and arithmetic use only the Python standard library. The
finite checks corroborate, but do not replace, the analytical theorem.
"""
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import combinations, combinations_with_replacement
from math import comb, factorial, sqrt


def triple_fibers(support):
    """Map integer quadratic momentum-energy to multinomial triple weights."""
    bins = defaultdict(list)
    for triple in combinations_with_replacement(support, 3):
        ct = Counter(triple)
        mult = factorial(3)
        for c in ct.values():
            mult //= factorial(c)  # fine here: denominators 1,2,6
        bins[(sum(triple), sum(z*z for z in triple))].append((triple, mult))
    return bins


def three_energy(support):
    return sum(sum(mult for _, mult in fib)**2 for fib in triple_fibers(support).values())


def special(s):
    a,b,c,d = s
    h = b-a
    return c == a+3*h and d == a+4*h


cases=0
exceptional=0
for n in range(4,27):
    hits=0
    for s in combinations(range(n+1), 4):
        fibers=triple_fibers(s)
        dup=[f for f in fibers.values() if len(f)>1]
        if special(s):
            assert len(dup)==1 and len(dup[0])==2
            assert three_energy(s)==274
            hits+=1
        else:
            assert not dup
            assert three_energy(s)==256
        cases+=1
    m=n//4
    assert hits==m*(n+1)-2*m*(m+1)
    exceptional+=hits

# Every composition on several uniform rational grids satisfies the sharp
# nonresonant normalized moment stability inequality.
checks=0
for den in (4,7,10):
    for a in range(den+1):
      for b in range(den-a+1):
       for c in range(den-a-b+1):
        d=den-a-b-c
        w=[F(k,den) for k in (a,b,c,d)]
        h=F(6)-9*sum(x*x for x in w)+4*sum(x*x*x for x in w)
        dist=sum((x-F(1,4))**2 for x in w)
        assert F(4)-h>=4*dist
        checks+=1

# Check the radical identities for the unique pair-balanced extremum by
# performing arithmetic in Q(sqrt(97)) (no floating point).
class R:
    def __init__(self,a=0,b=0):
        self.a,self.b=F(a),F(b)
    def __add__(self,o):
        o=o if isinstance(o,R) else R(o)
        return R(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self):return R(-self.a,-self.b)
    def __sub__(self,o):return self+-o if isinstance(o,R) else self+R(-o)
    def __rsub__(self,o):return (o if isinstance(o,R) else R(o))+(-self)
    def __mul__(self,o):
        o=o if isinstance(o,R) else R(o)
        return R(self.a*o.a+97*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def __pow__(self,n):
        v=R(1)
        for i in range(n):v=v*self
        return v
    def __truediv__(self,o):return self*F(1,o)
    def __eq__(self,o):
        o=o if isinstance(o,R) else R(o)
        return (self.a,self.b)==(o.a,o.b)
    def approx(self):return float(self.a)+float(self.b)*sqrt(97)

rr=R(0,1)
p=(14-rr)/18
q=R(F(1,2))-p
assert 36*p*p-56*p+11 == 0
assert p+q==R(F(1,2))
Fpoly=lambda x: 18*x**3-42*x*x+R(F(33,2))*x+R(F(5,2))
assert Fpoly(p)==(97*rr-260)/162
assert F(0)<p.approx()<F(1,2)
assert Fpoly(p).approx()>4
print('VERIFY_OK', cases, 'quadratic 3-fold support energies;', exceptional,
      'resonant supports across bands;', checks,
      'rational stability checks; exact radical optimum')
