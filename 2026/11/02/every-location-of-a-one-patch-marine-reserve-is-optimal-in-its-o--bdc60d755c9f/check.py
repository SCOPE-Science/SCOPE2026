"""Exact checks for the three-site reserve-placement classification.
Requires only the Python standard library. Run: python check.py
"""
from fractions import Fraction as F
from itertools import product

class Poly:
    def __init__(self, terms=None):
        self.t = {k: F(v) for k, v in (terms or {}).items() if v}
    def __add__(self, other):
        other = other if isinstance(other, Poly) else Poly({(0,0,0):other})
        d = self.t.copy()
        for k,v in other.t.items(): d[k] = d.get(k,F(0))+v
        return Poly(d)
    __radd__ = __add__
    def __neg__(self): return Poly({k:-v for k,v in self.t.items()})
    def __sub__(self, other): return self+(-aspoly(other))
    def __rsub__(self, other): return aspoly(other)+(-self)
    def __mul__(self, other):
        other=aspoly(other); d={}
        for k,v in self.t.items():
            for l,w in other.t.items():
                t=tuple(k[i]+l[i] for i in range(3));d[t]=d.get(t,F(0))+v*w
        return Poly(d)
    __rmul__=__mul__
    def __pow__(self, n):
        assert isinstance(n,int) and n>=0
        p=aspoly(1)
        for i in range(n): p=p*self
        return p
    def __eq__(self, other):return self.t==aspoly(other).t
    def __repr__(self):return repr(self.t)

def aspoly(x): return x if isinstance(x,Poly) else Poly({(0,0,0):x})
# Monomials indexed by (power of h, power of m, power of natural mortality mu).
h=Poly({(1,0,0):1}); m=Poly({(0,1,0):1}); mu=Poly({(0,0,1):1})
A=mu+h+2*m;B=mu+2*m
D=A*A*B-(A+B)*m*m
X=A*B-2*m*m
P=A*A*B-(2*A+B)*m*m-m**3
S=A*B+B*m-m*m
N01=A*A*B*B-A*A*B*m-2*A*B*m*m+2*A*m**3-B*B*m*m+2*m**4
N12=A*B*B-2*A*B*m+B*B*m-2*B*m*m+2*m**3
# Exact cross-multiplied differences from the three equilibrium inverses.
assert A*(A+m)*X-(B+m)*D == h*P
assert (B+m)*D-B*(A+m)*X == h*m*S
assert B*D-m*(A+m)*X == N01
assert (B*(A+m)-m*m)*X-B*D == m*N12
assert N01*S-N12*P == m*X*D
# Positivity for all h,m,mu>0 follows from positive-coefficient expansions.
for tag,poly in [('D',D),('X',X),('P',P),('S',S),('N01',N01),('N12',N12)]:
    assert poly.t and all(v>0 for v in poly.t.values()), (tag,poly)
print('Symbolic identities: 5 exact polynomial checks; all six positivity expansions certified.')


def solve3(b,matrix):
    a=[[F(q) for q in row]+[F(b[i])] for i,row in enumerate(matrix)]
    for i in range(3):
        j=next(k for k in range(i,3) if a[k][i])
        a[i],a[j]=a[j],a[i];d=a[i][i]
        a[i]=[x/d for x in a[i]]
        for k in range(3):
            if k!=i:
                d=a[k][i];a[k]=[a[k][v]-d*a[i][v] for v in range(4)]
    return [a[i][3] for i in range(3)]

N=0
for mortality,movement,fish in product([F(1,5),F(1),F(3)], [F(1,7),F(1),F(5)], [F(1,4),F(1),F(4)]):
    A0=mortality+fish+2*movement;B0=mortality+2*movement
    D0=A0*A0*B0-(A0+B0)*movement**2
    X0=A0*B0-2*movement**2
    Tformula=[A0*(A0+movement)/D0,(B0+movement)/X0,B0*(A0+movement)/D0]
    Yformula=[fish*movement*(A0+movement)/D0,fish*B0/X0,fish*(B0*(A0+movement)-movement**2)/D0]
    for j in range(3):
        H=[fish,fish,fish];H[j]=F(0)
        mat=[[mortality+H[i]+2*movement if i==k else (-movement if abs(i-k)==1 else F(0)) for k in range(3)] for i in range(3)]
        u=solve3([1,0,0],mat)
        assert all(x>0 for x in u)
        assert sum(u)==Tformula[j] and sum(H[i]*u[i] for i in range(3))==Yformula[j]
        N+=1
    T,Y=Tformula,Yformula
    assert T[0]>T[1]>T[2]>0 and 0<Y[0]<Y[1]<Y[2]
    lo=(Y[2]-Y[1])/(T[1]-T[2]);hi=(Y[1]-Y[0])/(T[0]-T[1])
    assert 0<lo<hi
    test_weights=[F(0),lo,(lo+hi)/2,hi,hi+1]
    expected=[(2,),(1,2),(1,),(0,1),(0,)]
    for q,winners in zip(test_weights,expected):
        welfare=[Y[i]+q*T[i] for i in range(3)]
        best=max(welfare)
        assert tuple(i for i in range(3) if welfare[i]==best)==winners
        N+=1
assert N==27*8
# Model with equal natural mortality, migration and fishing; closed-form table.
a,b,c=F(1),F(1),F(1)
T=[F(20,41),F(2,5),F(15,41)]
Y=[F(5,41),F(3,10),F(14,41)]
assert (Y[2]-Y[1])/(T[1]-T[2])==F(17,14)
assert (Y[1]-Y[0])/(T[0]-T[1])==F(73,36)
print(f'Exact rational checks: {N} equilibrium/ordering/optimality tests; example thresholds 17/14 and 73/36.')
