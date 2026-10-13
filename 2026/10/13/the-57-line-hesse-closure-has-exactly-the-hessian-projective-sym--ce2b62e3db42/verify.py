from fractions import Fraction
from dataclasses import dataclass
from collections import defaultdict, Counter

@dataclass(frozen=True)
class K:
    a: Fraction
    b: Fraction
    def __add__(self, o):
        o = toK(o); return K(self.a+o.a, self.b+o.b)
    __radd__ = __add__
    def __neg__(self): return K(-self.a, -self.b)
    def __sub__(self, o): return self + (-toK(o))
    def __rsub__(self, o): return toK(o) - self
    def __mul__(self, o):
        o = toK(o)
        return K(self.a*o.a-self.b*o.b,
                 self.a*o.b+self.b*o.a-self.b*o.b)
    __rmul__ = __mul__
    def inv(self):
        n = self.a*self.a-self.a*self.b+self.b*self.b
        if n == 0: raise ZeroDivisionError
        return K((self.a-self.b)/n, -self.b/n)
    def __truediv__(self, o): return self*toK(o).inv()
    def __rtruediv__(self, o): return toK(o)*self.inv()

def toK(x):
    if isinstance(x, K): return x
    return K(Fraction(x), Fraction(0))

E = K(Fraction(0), Fraction(1)) # E^2+E+1=0
Z, O = toK(0), toK(1)
half = Fraction(1,2)
em1, ep1, twoep2 = -E-O, E+O, 2*E+2

# The 57 linear forms printed for H_57 in Pokora--Roulleau,
# Construction of free arrangements using point-line operators,
# arXiv:2403.20024v1, proof of Theorem A. Each tuple is (a,b,c)
# for ax+by+cz=0, with E a primitive cube root of unity.
lines = [
(1,em1,E),(0,1,1),(1,-2*E,E),(1,E,-2*E),(1,E,twoep2),(1,0,em1),
(1,E,-2),(1,-half*E,-half*E),(1,1,-2),(1,-half,-half),(0,1,E),(1,ep1,0),
(1,half*ep1,-half*E),(1,twoep2,E),(1,twoep2,em1),(1,E,0),(1,-half,half*ep1),(0,0,1),
(1,1,1),(1,1,E),(1,0,-E),(1,E,E),(1,-1,0),(1,E,1),(1,em1,-2*E),(1,E,em1),
(1,em1,1),(1,-2,E),(1,em1,em1),(1,1,em1),(1,-E,0),(0,1,0),(0,1,ep1),(1,0,ep1),
(1,1,twoep2),(1,half*ep1,-half),(1,-half*E,half*ep1),(0,1,-E),(1,-2,1),(1,0,0),
(0,1,-1),(1,0,-1),(1,1,0),(1,-2*E,1),(1,-2,em1),(1,-2*E,em1),(0,1,em1),(1,0,E),
(1,twoep2,1),(1,em1,-2),(1,em1,0),(1,1,-2*E),(1,0,1),(1,-half,-half*E),
(1,em1,twoep2),(1,half*ep1,half*ep1),(1,-half*E,-half)
]
lines = [tuple(toK(c) for c in L) for L in lines]

def cross(u,v):
    return (u[1]*v[2]-u[2]*v[1],
            u[2]*v[0]-u[0]*v[2],
            u[0]*v[1]-u[1]*v[0])

def dot(u,v): return sum((a*b for a,b in zip(u,v)), Z)

def pnorm(v):
    v = tuple(toK(x) for x in v)
    for c in v:
        if c != Z:
            ci = c.inv(); return tuple(x*ci for x in v)
    raise ValueError('zero projective vector')

nlines = {pnorm(L) for L in lines}
assert len(lines) == 57 and len(nlines) == 57

point_lines = defaultdict(set)
for i in range(57):
    for j in range(i+1,57):
        p = pnorm(cross(lines[i], lines[j]))
        point_lines[p].update((i,j))
mult = Counter(len(S) for S in point_lines.values())
assert mult == Counter({2:252, 3:108, 4:72, 8:21}), mult
assert sum(m*(m-1)//2 * n for m,n in mult.items()) == 57*56//2

P8 = [p for p,S in point_lines.items() if len(S)==8]
profile = Counter(sum(dot(L,p)==Z for p in P8) for L in lines)
assert profile == Counter({2:36, 4:9, 5:12}), profile

five = {pnorm(L) for L in lines if sum(dot(L,p)==Z for p in P8)==5}
# Classical Hesse arrangement: the three coordinate axes and the nine
# lines x + E^i y + E^j z = 0 (i,j in Z/3).
powers = [O,E,em1]
hesse = {pnorm((1,0,0)), pnorm((0,1,0)), pnorm((0,0,1))}
for a in powers:
    for b in powers:
        hesse.add(pnorm((1,a,b)))
assert len(hesse)==12
assert five == hesse

idx = [i+1 for i,L in enumerate(lines) if pnorm(L) in five]
assert idx == [1,18,19,20,22,24,26,27,29,30,32,40], idx

print('VERIFY_OK lines=57 singularities=n2:252,n3:108,n4:72,n8:21 maxpoint_profile=12x5+9x4+36x2 recovered_hesse=exact')
