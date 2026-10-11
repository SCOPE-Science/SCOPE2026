from fractions import Fraction
from itertools import product

# Exact arithmetic in Q(sqrt(3)) represented as a+b*s.
class Q3:
    __slots__=('a','b')
    def __init__(self,a=0,b=0): self.a=Fraction(a); self.b=Fraction(b)
    def __add__(self,o): o=o if isinstance(o,Q3) else Q3(o); return Q3(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return Q3(-self.a,-self.b)
    def __sub__(self,o): return self+(- (o if isinstance(o,Q3) else Q3(o)))
    def __rsub__(self,o): return Q3(o)-self
    def __mul__(self,o):
        o=o if isinstance(o,Q3) else Q3(o)
        return Q3(self.a*o.a+3*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def __truediv__(self,o):
        o=o if isinstance(o,Q3) else Q3(o)
        den=o.a*o.a-3*o.b*o.b
        return Q3((self.a*o.a-3*self.b*o.b)/den,(self.b*o.a-self.a*o.b)/den)
    def __eq__(self,o):
        o=o if isinstance(o,Q3) else Q3(o)
        return self.a==o.a and self.b==o.b
    def __repr__(self): return f'Q3({self.a},{self.b})'

s=Q3(0,1)
r=s-1
C=(Q3(3)+s)/2
# Verify the sharp one-variable factorization:
# C - (x^2+2x+4)/(x^2+2) = ((1+s)/2)*(x-(s-1))^2/(x^2+2).
# Coefficients of numerator difference match the square expansion.
A=(Q3(1)+s)/2
assert A*r*r == s-1
assert -2*A*r == -2
# Witness value for unequal radii r,1,1.
S=r+2
M=S-2*r
R=(3*S*S+M*M)/(4*(r*r+2))
assert R==C

# Projective sign classes for the four sign sums (first sign normalized to +1).
P=[(1,1,1),(1,1,-1),(1,-1,1),(1,-1,-1)]

def dot(p,q): return sum(a*b for a,b in zip(p,q))
# Every row covers exactly one projective sign class with squared value 9; all others give 1.
for p in P:
    vals=sorted(dot(p,q)**2 for q in P)
    assert vals==[1,1,1,9]

# Enumerate all 3-row vertex configurations for the modified constant.
max_num=0
arg=None
for rows in product(P, repeat=3):
    num=sum(max(dot(sig,row)**2 for row in rows) for sig in P)
    if num>max_num: max_num,arg=num,rows
assert max_num==28
assert Fraction(max_num,12)==Fraction(7,3)
assert len(set(arg))==3

# Two-pattern configurations never exceed 2 in the unmodified ratio by the analytic inequality
# S^2+(S-2a)^2 <= 4(a^2+b^2+c^2), using (b+c)^2<=2(b^2+c^2).
# One-pattern configurations have ratio exactly 1 by expansion.
print('VERIFY_OK')
print('modified_upper_third_linf3 = 7/3')
print('upper_third_linf3 = (3+sqrt(3))/2')
print('unequal_radius_ratio = sqrt(3)-1 : 1 : 1')
