#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import combinations_with_replacement
from collections import defaultdict

D = 97

class Q:
    # a + b*sqrt(D)
    __slots__ = ("a", "b")
    def __init__(self, a=0, b=0):
        self.a, self.b = F(a), F(b)
    def __add__(self, o):
        o = o if isinstance(o,Q) else Q(o)
        return Q(self.a+o.a, self.b+o.b)
    __radd__ = __add__
    def __neg__(self): return Q(-self.a,-self.b)
    def __sub__(self,o): return self + (- (o if isinstance(o,Q) else Q(o)))
    def __rsub__(self,o): return Q(o)-self
    def __mul__(self,o):
        o = o if isinstance(o,Q) else Q(o)
        return Q(self.a*o.a + D*self.b*o.b, self.a*o.b + self.b*o.a)
    __rmul__ = __mul__
    def __truediv__(self,o):
        if isinstance(o,Q):
            den=o.a*o.a-D*o.b*o.b
            return Q((self.a*o.a-D*self.b*o.b)/den,(self.b*o.a-self.a*o.b)/den)
        return Q(self.a/F(o),self.b/F(o))
    def __pow__(self,n):
        r=Q(1)
        for _ in range(n): r=r*self
        return r
    def __eq__(self,o):
        o=o if isinstance(o,Q) else Q(o)
        return self.a==o.a and self.b==o.b


def collisions():
    A=(0,1,4,9)
    by=defaultdict(list)
    for t in combinations_with_replacement(A,3):
        by[sum(t)].append(t)
    c={s:v for s,v in by.items() if len(v)>1}
    assert c=={9:[(0,0,9),(1,4,4)]}
    return c


def direct_l6(coeffs):
    A=(0,1,4,9)
    conv=defaultdict(int)
    for i,a in enumerate(A):
        for j,b in enumerate(A):
            for k,c in enumerate(A):
                conv[a+b+c]+=coeffs[i]*coeffs[j]*coeffs[k]
    return sum(v*v for v in conv.values())


def closed_l6(coeffs):
    # Real coefficients; the unique resonance has aligned or opposite real phase automatically.
    x=[F(c*c) for c in coeffs]
    S=sum(x,F(0))
    base=6*S**3-9*S*sum((t*t for t in x),F(0))+4*sum((t**3 for t in x),F(0))
    cross=18*F(coeffs[0]**2*coeffs[3]*coeffs[1]*coeffs[2]**2)
    return base+cross


def algebra():
    s=Q(0,1)
    p=(s-5)/9
    assert 9*p*p+10*p-8 == 0
    phi=Q(F(5,2))+6*p-F(15,4)*p*p-F(9,4)*p*p*p
    target=Q(F(-260,162),F(97,162))
    assert phi==target
    q=1-p
    assert p+q==1


def main():
    c=collisions()
    cases=[(1,1,1,1),(1,2,3,4),(2,1,4,3),(3,2,1,5),(5,1,2,2)]
    for v in cases:
        assert F(direct_l6(v))==closed_l6(v)
    algebra()
    print(f"VERIFY_OK collisions={len(c)} algebra=exact convolution_cases={len(cases)}")

if __name__ == '__main__':
    main()
