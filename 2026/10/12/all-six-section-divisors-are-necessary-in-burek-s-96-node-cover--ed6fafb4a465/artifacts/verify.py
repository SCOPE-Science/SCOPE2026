from fractions import Fraction as F
from itertools import combinations
from collections import Counter

class G:
    __slots__=("a","b")
    def __init__(self,a=0,b=0): self.a=F(a); self.b=F(b)
    def __add__(self,o): o=gg(o); return G(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return G(-self.a,-self.b)
    def __sub__(self,o): return self+(-gg(o))
    def __rsub__(self,o): return gg(o)-self
    def __mul__(self,o): o=gg(o); return G(self.a*o.a-self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def inv(self):
        d=self.a*self.a+self.b*self.b
        if d==0: raise ZeroDivisionError
        return G(self.a/d,-self.b/d)
    def __truediv__(self,o): return self*gg(o).inv()
    def __rtruediv__(self,o): return gg(o)/self
    def __pow__(self,n):
        if n<0: return (self.inv())**(-n)
        r=G(1); x=self
        while n:
            if n&1:r=r*x
            x=x*x;n//=2
        return r
    def __eq__(self,o): o=gg(o); return self.a==o.a and self.b==o.b
    def __hash__(self): return hash((self.a,self.b))
    def __repr__(self):
        if self.b==0:return str(self.a)
        return f"({self.a}{'+' if self.b>=0 else ''}{self.b}i)"
def gg(x): return x if isinstance(x,G) else G(x)
I=G(0,1)

def A(z): return z**8+14*z**4+1
def B(z): return z*(z**4-1)
def C(z): return z**12-33*z**8-33*z**4+1
A2=G(481); C2=G(-4879)

def section(j,u,v,t):
    gam=B(u); delt=B(v); m=gam*delt; z=gam*t+delt/t
    if j==1:
        aa=-18*(1+I)*(u*v+I)
        bb=-3*(5*u**4*v**4-u**4-v**4+24*I*u**3*v**3-24*u**2*v**2-24*I*u*v+5)
    elif j==2:
        aa=18*(1+I)*(u*v+I)
        bb=-3*(5*u**4*v**4-u**4-v**4+24*I*u**3*v**3-24*u**2*v**2-24*I*u*v+5)
    elif j==6:
        aa=G(0)
        bb=3*(u**4*v**4+u**4+v**4+6*u**4*v**2+6*u**2*v**4-12*u**2*v**2+6*u**2+6*v**2+1)
    else: raise ValueError
    cc=aa**3/108
    dd=(3*aa**2*bb-11664*m-cc**2)/108
    return (t**2*(aa*z+bb), t**3*(54*z**2+cc*z+dd))

def node_x(v,t): return 3*A2**2*C(v)/(C2*A(v))*t**2

labels=[("P1",1,G(2)),("P2",2,G(2)),("P6",6,G(2)),
        ("P1'",1,2*I),("P2'",2,2*I),("P6'",6,2*I)]

def q(a,b=0,d=1): return G(F(a,d),F(b,d))
roots_tau=[
(q(-3),q(-2,-2)),(q(-2),q(-1)),(q(-4,-3,5),q(-26,18,125)),(q(-4,3,5),q(-26,-18,125)),
(q(-3,-4,5),q(-26,-18,125)),(q(-3,4,5),q(-26,18,125)),(q(-1,0,2),q(-1,0,8)),(q(-1,0,3),q(-2,-2,27)),
(-3*I,q(-2,-2)),(-2*I,q(-1)),(-I/2,q(-1,0,8)),(-I/3,q(-2,-2,27)),
(I/3,q(-2,-2,27)),(I/2,q(-1,0,8)),(2*I,q(-1)),(3*I,q(-2,-2)),
(q(1,0,3),q(-2,-2,27)),(q(1,0,2),q(-1,0,8)),(q(3,-4,5),q(-26,18,125)),(q(3,4,5),q(-26,-18,125)),
(q(4,-3,5),q(-26,-18,125)),(q(4,3,5),q(-26,18,125)),(q(2),q(-1)),(q(3),q(-2,-2))]

# Verify the 24 listed v-values are distinct roots of J and each tau is a fourth root of C(v)/C(2).
assert len({v for v,_ in roots_tau})==24
for v,tau in roots_tau:
    J=A2**3*B(v)**4-G(30)**4*A(v)**3
    assert J==0
    assert tau**4==C(v)/C2

nodes=[]
for v,tau in roots_tau:
    for k in range(4):
        t=(I**k)*tau
        target=(node_x(v,t),G(0))
        passing=[]
        for name,j,u in labels:
            if section(j,u,v,t)==target:
                passing.append(name)
        assert passing
        nodes.append((v,t,tuple(passing)))
assert len(nodes)==96
assert len({(v,t) for v,t,_ in nodes})==96

multiplicity=Counter(len(p) for _,_,p in nodes)
assert multiplicity==Counter({1:44,2:24,3:16,4:8,5:4})
section_counts=Counter()
unique_counts=Counter()
for _,_,ps in nodes:
    for s in ps: section_counts[s]+=1
    if len(ps)==1: unique_counts[ps[0]]+=1
assert section_counts==Counter({s:32 for s,_,_ in labels})
assert unique_counts==Counter({"P1":6,"P2":6,"P6":10,"P1'":6,"P2'":6,"P6'":10})

covers={s:set() for s,_,_ in labels}
for idx,(_,_,ps) in enumerate(nodes):
    for s in ps:covers[s].add(idx)
names=[s for s,_,_ in labels]
for r in range(1,6):
    assert all(len(set().union(*(covers[s] for s in sub)))<96 for sub in combinations(names,r))
assert len(set().union(*(covers[s] for s in names)))==96

union_profiles={}
for r in range(1,7):
    c=Counter()
    for sub in combinations(names,r):
        c[len(set().union(*(covers[s] for s in sub)))] += 1
    union_profiles[r]=dict(sorted(c.items()))

print("nodes=96")
print("incidence_multiplicity="+repr(dict(sorted(multiplicity.items()))))
print("section_counts="+repr(dict(section_counts)))
print("unique_counts="+repr(dict(unique_counts)))
print("union_profiles="+repr(union_profiles))
print("minimum_cover_size=6")
print("VERIFY_OK")
