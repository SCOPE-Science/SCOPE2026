from fractions import Fraction as F

# Complex rational scalar.
class C:
    __slots__=("r","i")
    def __init__(self,r=0,i=0): self.r=F(r); self.i=F(i)
    def __add__(self,o): o=asC(o); return C(self.r+o.r,self.i+o.i)
    __radd__=__add__
    def __neg__(self): return C(-self.r,-self.i)
    def __sub__(self,o): return self+(-asC(o))
    def __rsub__(self,o): return asC(o)-self
    def __mul__(self,o): o=asC(o); return C(self.r*o.r-self.i*o.i,self.r*o.i+self.i*o.r)
    __rmul__=__mul__
    def __truediv__(self,o):
        o=asC(o); d=o.r*o.r+o.i*o.i
        return C((self.r*o.r+self.i*o.i)/d,(self.i*o.r-self.r*o.i)/d)
    def conj(self): return C(self.r,-self.i)
    def __eq__(self,o): o=asC(o); return self.r==o.r and self.i==o.i
    def __repr__(self): return f"C({self.r},{self.i})"
def asC(x): return x if isinstance(x,C) else C(x)
I=C(0,1)
ZERO=C(0)
ONE=C(1)

def vadd(a,b): return [x+y for x,y in zip(a,b)]
def vscale(c,a): return [c*x for x in a]
def matvec(A,x): return [sum((A[r][c]*x[c] for c in range(len(x))),ZERO) for r in range(len(A))]
def conjdot(p,q): return sum((p[k].conj()*q[k] for k in range(len(q))),ZERO)

def solve(A,b):
    M=[row[:] + [b[i]] for i,row in enumerate(A)]
    n=len(A)
    for j in range(n):
        piv=next(i for i in range(j,n) if M[i][j]!=ZERO)
        M[j],M[piv]=M[piv],M[j]
        s=M[j][j]
        M[j]=[z/s for z in M[j]]
        for i in range(n):
            if i==j: continue
            s=M[i][j]
            if s!=ZERO: M[i]=[M[i][k]-s*M[j][k] for k in range(n+1)]
    return [M[i][n] for i in range(n)]

A=[[C(0),C(1),C(0)],[C(0),C(0),C(1)],[C(-1),C(-1),C(-1)]]
AT=[[A[j][i] for j in range(3)] for i in range(3)]
q=[C(-1),-I,C(1)]
p=[C(F(-1,4),F(-1,4)),C(0,F(-1,2)),C(F(1,4),F(-1,4))]
assert matvec(A,q)==vscale(I,q)
assert matvec(AT,p)==vscale(-I,p)
assert conjdot(p,q)==ONE

# Polynomial in alpha and gamma with exact complex-rational coefficients.
class P:
    def __init__(self,d=None):
        self.d={k:asC(v) for k,v in (d or {}).items() if asC(v)!=ZERO}
    @staticmethod
    def const(c): return P({(0,0):asC(c)})
    def __add__(self,o):
        o=asP(o); d=dict(self.d)
        for k,v in o.d.items(): d[k]=d.get(k,ZERO)+v
        return P(d)
    __radd__=__add__
    def __neg__(self): return P({k:-v for k,v in self.d.items()})
    def __sub__(self,o): return self+(-asP(o))
    def __rsub__(self,o): return asP(o)-self
    def __mul__(self,o):
        o=asP(o); d={}
        for (i,j),a in self.d.items():
            for (k,l),b in o.d.items():
                key=(i+k,j+l); d[key]=d.get(key,ZERO)+a*b
        return P(d)
    __rmul__=__mul__
    def __truediv__(self,o):
        o=asP(o)
        assert list(o.d.keys()) in ([],[(0,0)]) and o.d
        c=o.d[(0,0)]
        return P({k:v/c for k,v in self.d.items()})
    def conj(self): return P({k:v.conj() for k,v in self.d.items()})
    def __eq__(self,o): return self.d==asP(o).d
    def coeff(self,i,j): return self.d.get((i,j),ZERO)
    def __repr__(self): return repr(self.d)
def asP(x): return x if isinstance(x,P) else P.const(x)
AL=P({(1,0):ONE}); GA=P({(0,1):ONE})

def pvec_scale(c,a): return [asP(c)*x for x in a]
def pconjdot(pc,qc): return sum((pc[k].conj()*qc[k] for k in range(len(qc))),P())
def lift(v): return [P.const(x) for x in v]

def B(x,y):
    return [P(),P(), -2*AL*x[2]*y[2]+x[0]*y[1]+x[1]*y[0]]
def C3(x,y,z):
    return [P(),P(), 6*GA*x[2]*y[2]*z[2]]

def solve_const_matrix(A,b):
    # A has C entries, b has P entries; Gaussian elimination scales rows by C.
    M=[[P.const(A[i][j]) for j in range(3)]+[b[i]] for i in range(3)]
    for j in range(3):
        piv=next(i for i in range(j,3) if M[i][j]!=P())
        M[j],M[piv]=M[piv],M[j]
        c=M[j][j].coeff(0,0)
        M[j]=[z/P.const(c) for z in M[j]]
        for i in range(3):
            if i==j: continue
            c=M[i][j].coeff(0,0)
            if c!=ZERO: M[i]=[M[i][k]-P.const(c)*M[j][k] for k in range(4)]
    return [M[i][3] for i in range(3)]

qp=lift(q); qbar=[z.conj() for z in qp]; pp=lift(p)
h11=solve_const_matrix(A,B(qp,qbar))
M20=[[((2*I if r==c else ZERO)-A[r][c]) for c in range(3)] for r in range(3)]
h20=solve_const_matrix(M20,B(qp,qp))
assert h11==[2*AL,P(),P()]
term=[C3(qp,qp,qbar)[k]-2*B(qp,h11)[k]+B(qbar,h20)[k] for k in range(3)]
G=pconjdot(pp,term)
# l1 = Re(G)/2. Check every symbolic coefficient.
L={k:v.r/F(2) for k,v in G.d.items()}
expected={(2,0):F(2,5),(1,0):F(-13,20),(0,1):F(3,4),(0,0):F(-1,20)}
assert {k:v for k,v in L.items() if v}==expected

def formula(a,g): return (8*a*a-13*a+15*g-1)/20
assert formula(F(23,10),F(1,20))==F(1217,2000)
assert formula(F(23,10),F(1,100))==F(1157,2000)
# Crossing derivative at lambda=i: -i/(-2+2i).
lamprime=(-I)/C(-2,2)
assert lamprime==C(F(-1,4),F(1,4))
print('VERIFY_OK')
