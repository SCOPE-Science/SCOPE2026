from fractions import Fraction as F
from itertools import combinations

class Q2:
    __slots__=('a','b')
    def __init__(self,a=0,b=0):
        self.a=a if isinstance(a,F) else F(a)
        self.b=b if isinstance(b,F) else F(b)
    def __add__(self,o):
        o=q(o); return Q2(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return Q2(-self.a,-self.b)
    def __sub__(self,o): return self+(-q(o))
    def __rsub__(self,o): return q(o)-self
    def __mul__(self,o):
        o=q(o); return Q2(self.a*o.a+2*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def inv(self):
        d=self.a*self.a-2*self.b*self.b
        if d==0: raise ZeroDivisionError
        return Q2(self.a/d,-self.b/d)
    def __truediv__(self,o): return self*q(o).inv()
    def __rtruediv__(self,o): return q(o)/self
    def __eq__(self,o):
        o=q(o); return self.a==o.a and self.b==o.b
    def __hash__(self): return hash((self.a,self.b))
    def sign(self):
        a,b=self.a,self.b
        if a==0 and b==0:return 0
        if b==0:return 1 if a>0 else -1
        if b>0:
            if a>=0:return 1
            # b*sqrt2 ? -a
            c=2*b*b-a*a
            return 1 if c>0 else (0 if c==0 else -1)
        # b<0
        if a<=0:return -1
        c=a*a-2*b*b
        return 1 if c>0 else (0 if c==0 else -1)
    def __lt__(self,o): return (self-q(o)).sign()<0
    def __le__(self,o): return (self-q(o)).sign()<=0
    def __repr__(self): return f'({self.a})+({self.b})*r2'

def q(x): return x if isinstance(x,Q2) else Q2(x)
R2=Q2(0,1)
R=R2-1
HALF=Q2(F(1,2))
INV_R2=R2/2

# Octagon vertices for N(s,t)=max(|s|,|t|,(|s|+|t|)/sqrt(2)).
V=[(q(1),R),(R,q(1)),(-R,q(1)),(q(-1),R),(q(-1),-R),(-R,q(-1)),(R,q(-1)),(q(1),-R)]
# Eight support functionals l(z)=ax+by whose maximum is N(z).
S=[(q(1),q(0)),(q(-1),q(0)),(q(0),q(1)),(q(0),q(-1)),
   (INV_R2,INV_R2),(INV_R2,-INV_R2),(-INV_R2,INV_R2),(-INV_R2,-INV_R2)]

def vec_add(x,y): return (x[0]+y[0],x[1]+y[1])
def vec_sub(x,y): return (x[0]-y[0],x[1]-y[1])
def vec_scale(c,x): return (c*x[0],c*x[1])
def dot(l,z): return l[0]*z[0]+l[1]*z[1]

def affine_point(i,which):
    # returns vector affine coefficients z=z0+s*zs (if which 0) or z0+t*zt
    a=V[i]; b=V[(i+1)%8]; d=vec_sub(b,a)
    if which==0:return (a,d,(q(0),q(0)))
    return (a,(q(0),q(0)),d)

def aff_vec_sum(A,B,sgn=1):
    # triples of vectors constant,s,t
    return tuple(vec_add(A[k],vec_scale(q(sgn),B[k])) for k in range(3))

def aff_dot(l,Z): return tuple(dot(l,Z[k]) for k in range(3))

def aff_sub(A,B): return tuple(A[k]-B[k] for k in range(3))

def aff_eval(A,s,t): return A[0]+A[1]*s+A[2]*t

def intersect(H1,H2):
    # h=c+as+bt=0
    c1,a1,b1=H1; c2,a2,b2=H2
    det=a1*b2-a2*b1
    if det.sign()==0:return None
    s=(b1*c2-b2*c1)/det
    t=(a2*c1-a1*c2)/det
    return s,t

def feasible(H,s,t):
    return all(aff_eval(h,s,t).sign()>=0 for h in H)

def Qval(a,b):
    # Target inequality Q=a^2+b^2-(sqrt2-1)ab-4 <= 0,
    # equivalent to P-angle cosine <= (sqrt2-1)/2 when a,b>0.
    return a*a+b*b-R*a*b-4

def N_exact(z):
    vals=[dot(l,z) for l in S]
    m=vals[0]
    for v in vals[1:]:
        if m<v:m=v
    return m

maxQ=None; maxdata=None; cells=0; vertices=0
for i in [0]:
  X=affine_point(i,0)
  for j in range(8):
    Y=affine_point(j,1)
    U=aff_vec_sum(X,Y,1)
    W=aff_vec_sum(X,Y,-1)
    Uforms=[aff_dot(l,U) for l in S]
    Wforms=[aff_dot(l,W) for l in S]
    for ku in range(8):
      a=Uforms[ku]
      for kw in range(8):
        b=Wforms[kw]
        H=[(q(0),q(1),q(0)),(q(1),q(-1),q(0)),(q(0),q(0),q(1)),(q(1),q(0),q(-1))]
        H += [aff_sub(a,f) for f in Uforms]
        H += [aff_sub(b,f) for f in Wforms]
        pts=set()
        for h1,h2 in combinations(H,2):
            p=intersect(h1,h2)
            if p is not None and feasible(H,*p): pts.add(p)
        if not pts: continue
        cells+=1
        # Q is a convex quadratic in (a,b), since [[1,-R/2],[-R/2,1]] is positive definite;
        # a,b are affine on this cell, so maximum over polygon occurs at vertices.
        for s,t in pts:
            vertices+=1
            aa=aff_eval(a,s,t); bb=aff_eval(b,s,t)
            qq=Qval(aa,bb)
            if maxQ is None or maxQ<qq:
                maxQ=qq; maxdata=(i,j,ku,kw,s,t,aa,bb)
            if qq.sign()>0:
                raise SystemExit(f'FAIL positive Q {qq} at {maxdata}')

# Exact witness: adjacent vertices x=(1,R), y=(R,1).
x=V[0]; y=V[1]
aa=N_exact(vec_add(x,y)); bb=N_exact(vec_sub(x,y))
assert aa==q(2)
assert bb==2*R
assert Qval(aa,bb)==q(0)
# resulting cosine is R/2
num=aa*aa+bb*bb-4
den=2*aa*bb
assert num/den==R/2
assert maxQ==q(0)
print('VERIFY_OK')
print('feasible_cells',cells)
print('checked_cell_vertices',vertices)
print('max_Q',maxQ)
print('witness_a',aa,'witness_b',bb,'cosine',R/2)
