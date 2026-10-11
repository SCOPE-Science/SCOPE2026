from fractions import Fraction

class Q2:
    # a + b*sqrt(2)
    __slots__=("a","b")
    def __init__(self,a=0,b=0):
        self.a=Fraction(a); self.b=Fraction(b)
    def __add__(self,o):
        o=o if isinstance(o,Q2) else Q2(o)
        return Q2(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return Q2(-self.a,-self.b)
    def __sub__(self,o): return self+(-o)
    def __rsub__(self,o): return Q2(o)-self
    def __mul__(self,o):
        o=o if isinstance(o,Q2) else Q2(o)
        return Q2(self.a*o.a+2*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def __truediv__(self,o):
        o=o if isinstance(o,Q2) else Q2(o)
        den=o.a*o.a-2*o.b*o.b
        return Q2((self.a*o.a-2*self.b*o.b)/den,(self.b*o.a-self.a*o.b)/den)
    def __eq__(self,o):
        o=o if isinstance(o,Q2) else Q2(o)
        return self.a==o.a and self.b==o.b
    def sign(self):
        if self.a==0: return (self.b>0)-(self.b<0)
        if self.b==0: return (self.a>0)-(self.a<0)
        if (self.a>0 and self.b>0): return 1
        if (self.a<0 and self.b<0): return -1
        aa=self.a*self.a; bb=2*self.b*self.b
        if aa==bb: return 0
        if self.a>0: return 1 if aa>bb else -1
        return 1 if bb>aa else -1
    def __lt__(self,o):
        o=o if isinstance(o,Q2) else Q2(o)
        return (self-o).sign()<0
    def __abs__(self): return self if self.sign()>=0 else -self
    def __repr__(self): return f"{self.a}+{self.b}*sqrt2"

S=Q2(0,1)
ONE=Q2(1)
A=S-ONE
ZERO=Q2(0)
TWO=Q2(2)

def norm(v):
    x,y=v
    return max([abs(x),abs(y),(abs(x)+abs(y))/S])

def add(u,v): return (u[0]+v[0],u[1]+v[1])
def sub(u,v): return (u[0]-v[0],u[1]-v[1])

verts=[(ONE,A),(A,ONE),(-A,ONE),(-ONE,A),(-ONE,-A),(-A,-ONE),(A,-ONE),(ONE,-A)]
assert A*A == Q2(3,-2)
assert ONE+A == S
for v in verts:
    assert norm(v)==ONE

patterns=set()
for u in verts:
    for v in verts:
        r=norm(add(u,v)); s=norm(sub(u,v))
        pair=tuple(sorted([(r.a,r.b),(s.a,s.b)]))
        patterns.add(pair)
expected={
    tuple(sorted([(TWO.a,TWO.b),(ZERO.a,ZERO.b)])),
    tuple(sorted([(TWO.a,TWO.b),((TWO*A).a,(TWO*A).b)])),
    tuple(sorted([(S.a,S.b),(S.a,S.b)])),
}
assert patterns==expected, patterns
assert ONE + A*A == Q2(4,-2)
print("VERIFY_OK")
print("vertices_checked=8")
print("ordered_vertex_pairs_checked=64")
print("shifted_norm_patterns=3")
print("endpoint_p2=4-2*sqrt(2)")
