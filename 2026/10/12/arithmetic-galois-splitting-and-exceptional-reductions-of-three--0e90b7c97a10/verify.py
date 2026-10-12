#!/usr/bin/env python3
"""Exact ring arithmetic and prime-field checks for the three-conic node theorem.

Requires Python 3 standard library only. No computer algebra package is needed.
"""
from collections import Counter


class E:
    """Element a+b*w+c*r+d*w*r, w*w+w+1=0 and r*r=13."""
    __slots__ = ('a', 'b', 'c', 'd')

    def __init__(self, a=0, b=0, c=0, d=0):
        self.a, self.b, self.c, self.d = map(int, (a, b, c, d))

    @staticmethod
    def _cast(v):
        return v if isinstance(v, E) else E(v)

    def __add__(self, other):
        other = self._cast(other)
        return E(self.a+other.a, self.b+other.b,
                 self.c+other.c, self.d+other.d)

    __radd__ = __add__

    def __neg__(self):
        return E(-self.a, -self.b, -self.c, -self.d)

    def __sub__(self, other):
        return self + -self._cast(other)

    def __rsub__(self, other):
        return self._cast(other) + -self

    @staticmethod
    def _mul2(a, b, c, d):
        return (a*c-b*d, a*d+b*c-b*d)

    def __mul__(self, other):
        other = self._cast(other)
        u, v = self._mul2(self.a, self.b, other.a, other.b)
        r, s = self._mul2(self.c, self.d, other.c, other.d)
        t, h = self._mul2(self.a, self.b, other.c, other.d)
        j, k = self._mul2(self.c, self.d, other.a, other.b)
        return E(u+13*r, v+13*s, t+j, h+k)

    __rmul__ = __mul__

    def __eq__(self, other):
        other = self._cast(other)
        return (self.a, self.b, self.c, self.d) == (other.a, other.b, other.c, other.d)

    def __repr__(self):
        return f'E({self.a},{self.b},{self.c},{self.d})'


W, R = E(0, 1), E(0, 0, 1)
W2 = W*W
assert W*W+W+1 == 0 and R*R == 13


def q(which, pt):
    x,y,z = pt
    if which == 1:
        return 21*(x*x+y*y)-22*x*y-6*(x+y)*z+z*z
    if which == 2:
        return 21*(W*x*x+W2*y*y)-22*x*y-6*(W2*x+W*y)*z+z*z
    if which == 3:
        return 21*(W2*x*x+W*y*y)-22*x*y-6*(W*x+W2*y)*z+z*z
    raise ValueError(which)


def T(pt):
    x,y,z = pt
    return (W*x, W2*y, z)


def sigma(t):
    # Galois conjugation w -> w^2=-1-w, r -> r.
    return E(t.a-t.b, -t.b, t.c-t.d, -t.d)


def tau(t):
    # Conjugation r -> -r.
    return E(t.a, t.b, -t.c, -t.d)


def proj_equal(P, Q):
    return all(P[i]*Q[j] == P[j]*Q[i]
               for i in range(3) for j in range(i+1, 3))


def unique_projective(points):
    result=[]
    for P in points:
        if not any(proj_equal(P,Q) for Q in result):
            result.append(P)
    return result


bases=[(E(-7),E(5),E(7)), (E(5),E(-7),E(7)),
       (E(1),E(1),E(-3)+2*R), (E(1),E(1),E(-3)-2*R)]
points=[]
for base in bases:
    P=base
    for _ in range(3):
        points.append(P)
        P=T(P)
    assert proj_equal(P, base)
assert len(unique_projective(points))==12
for P in points:
    assert sum(q(i,P)==0 for i in (1,2,3)) == 2, (P,[q(i,P) for i in (1,2,3)])
assert all(q(2,P)==0 and q(3,P)==0 for P in bases)
assert [q(1,P) for P in bases[:2]] == [E(2457), E(2457)]
assert q(1,bases[2])*q(1,bases[3]) == E(-3**5*13)
assert all(q(1,bases[k])!=0 for k in range(4))


def galois(P, sigma_on, tau_on):
    result=[]
    for coordinate in P:
        if sigma_on:
            coordinate=sigma(coordinate)
        if tau_on:
            coordinate=tau(coordinate)
        result.append(coordinate)
    return tuple(result)


fixed_counts={}
for a in (0,1):
    for b in (0,1):
        fixed_counts[(a,b)] = sum(proj_equal(P,galois(P,a,b)) for P in points)
assert fixed_counts == {(0,0):12,(0,1):6,(1,0):4,(1,1):2}, fixed_counts
orbits=[]
remaining=list(points)
while remaining:
    P=remaining[0]
    orbit=unique_projective([galois(P,a,b) for a in (0,1) for b in (0,1)])
    orbits.append(orbit)
    remaining=[Q for Q in remaining if not any(proj_equal(Q,U) for U in orbit)]
assert sorted(map(len,orbits)) == [1,1,2,2,2,4]


def legendre(a,p):
    r=pow(a%p,(p-1)//2,p)
    assert r in (1,p-1)
    return 1 if r==1 else -1


def rational_node_count_by_jacobian(p):
    # The rational sextic is proportional to Q1*Q2*Q3:
    # Q2*Q3=(R0^2+3*S0^2)/4, with R0 and S0 integral quadrics.
    def singular(x,y,z):
        q1=21*(x*x+y*y)-22*x*y-6*(x+y)*z+z*z
        a=-21*(x*x+y*y)-44*x*y+6*(x+y)*z+2*z*z
        b=21*(x*x-y*y)+6*(x-y)*z
        g=a*a+3*b*b
        qd=(42*x-22*y-6*z,42*y-22*x-6*z,-6*(x+y)+2*z)
        ad=(-42*x-44*y+6*z,-42*y-44*x+6*z,6*(x+y)+4*z)
        bd=(42*x+6*z,-42*y-6*z,6*(x-y))
        return q1*g%p==0 and all((qd[i]*g+q1*(2*a*ad[i]+6*b*bd[i]))%p==0 for i in range(3))
    n=0
    for x in range(p):
        for y in range(p):
            n+=singular(x,y,1)
    for x in range(p):
        n+=singular(x,1,0)
    n+=singular(1,0,0)
    return n


primes=(5,11,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89)
for p in primes:
    a,b=legendre(-3,p),legendre(13,p)
    target=2+2*(b==1)+4*(a==1)+4*(a==1 and b==1)
    count=rational_node_count_by_jacobian(p)
    assert count==target, (p,a,b,target,count)

print('VERIFY_OK: 12 projective nodes, Q(w,sqrt13) Galois orbits, exact fixed counts, 20 finite-field Jacobian censuses')
