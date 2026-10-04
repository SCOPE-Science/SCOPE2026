from fractions import Fraction
from itertools import product

class Q2:
    __slots__=('a','b')
    def __init__(self,a=0,b=0): self.a=Fraction(a); self.b=Fraction(b)
    def __add__(self,o): o=q(o); return Q2(self.a+o.a,self.b+o.b)
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
    def __eq__(self,o): o=q(o); return self.a==o.a and self.b==o.b
    def sign(self):
        a,b=self.a,self.b
        if a==0: return (b>0)-(b<0)
        if b==0: return (a>0)-(a<0)
        if (a>0 and b>0): return 1
        if (a<0 and b<0): return -1
        # compare |a| with |b| sqrt(2)
        cmp=(a*a > 2*b*b)-(a*a < 2*b*b)
        if a>0 and b<0: return cmp
        # a<0,b>0: sign = sign(|b|sqrt2-|a|) = -cmp
        return -cmp
    def __lt__(self,o): return (self-q(o)).sign()<0
    def __le__(self,o): return (self-q(o)).sign()<=0
    def __gt__(self,o): return (self-q(o)).sign()>0
    def __ge__(self,o): return (self-q(o)).sign()>=0
    def __repr__(self): return f'Q2({self.a},{self.b})'

def q(x): return x if isinstance(x,Q2) else Q2(x)
R=Q2(0,1)
HALFR=R/2
ONE=Q2(1)
ZERO=Q2(0)
TWO=Q2(2)

# N(s,t)=max |s|,|t|,(|s|+|t|)/sqrt(2)
# equivalently max over these 8 linear forms.
F=[
    (ONE,ZERO),(-ONE,ZERO),(ZERO,ONE),(ZERO,-ONE),
    (HALFR,HALFR),(-HALFR,-HALFR),(HALFR,-HALFR),(-HALFR,HALFR)
]

def dot(row,z):
    s=ZERO
    for a,b in zip(row,z): s=s+a*b
    return s

def eq_row(which,facet):
    a,b=F[facet]
    if which==0: return [a,b,ZERO,ZERO]            # x
    if which==1: return [ZERO,ZERO,a,b]            # y
    return [a,b,-a,-b]                              # x-y

def out_row(kind,facet):
    a,b=F[facet]
    if kind==0: return [a,b,a,b]                    # x+y
    return [TWO*a,TWO*b,-a,-b]                      # 2x-y

def affine(row,z0,d): return dot(row,z0),dot(row,d)

def solve3(rows):
    # RREF of 3 x (4+rhs) over Q(sqrt2); return z0,d for one-dimensional solution or None.
    M=[r[:] + [ONE] for r in rows]
    pivot_cols=[]; pr=0
    for c in range(4):
        piv=None
        for rr in range(pr,3):
            if M[rr][c].sign()!=0: piv=rr; break
        if piv is None: continue
        M[pr],M[piv]=M[piv],M[pr]
        inv=M[pr][c].inv()
        M[pr]=[v*inv for v in M[pr]]
        for rr in range(3):
            if rr==pr: continue
            f=M[rr][c]
            if f.sign()!=0: M[rr]=[M[rr][j]-f*M[pr][j] for j in range(5)]
        pivot_cols.append(c); pr+=1
        if pr==3: break
    if pr<3: return None
    free=[c for c in range(4) if c not in pivot_cols]
    if len(free)!=1: return None
    f=free[0]
    z0=[ZERO for _ in range(4)]; d=[ZERO for _ in range(4)]
    d[f]=ONE
    for r,c in enumerate(pivot_cols):
        z0[c]=M[r][4]
        d[c]=-M[r][f]
    return z0,d

def tighten(lo,hi,c0,c1,rhs):
    # c0+c1*t <= rhs
    beta=rhs-c0
    s=c1.sign()
    if s==0:
        return None if beta.sign()<0 else (lo,hi)
    bd=beta/c1
    if s>0:
        hi=bd if hi is None or bd<hi else hi
    else:
        lo=bd if lo is None or bd>lo else lo
    if lo is not None and hi is not None and lo>hi: return None
    return lo,hi

def base_interval(z0,d):
    lo=hi=None
    for which in range(3):
        for h in range(8):
            c0,c1=affine(eq_row(which,h),z0,d)
            got=tighten(lo,hi,c0,c1,ONE)
            if got is None: return None
            lo,hi=got
    return lo,hi

def dom_interval(z0,d,lo,hi,kind,a):
    ar=out_row(kind,a)
    for h in range(8):
        # L_h(output)-L_a(output) <= 0
        hr=out_row(kind,h)
        row=[hr[j]-ar[j] for j in range(4)]
        c0,c1=affine(row,z0,d)
        got=tighten(lo,hi,c0,c1,ZERO)
        if got is None: return None
        lo,hi=got
    return lo,hi

def eval_quad(c0,c1,c2,t): return c0+c1*t+c2*t*t

def prod_coeff(A0,A1,B0,B1): return A0*B0, A0*B1+A1*B0, A1*B1

def within(t,lo,hi): return (lo is None or t>=lo) and (hi is None or t<=hi)

M=Q2(9,-4) # (2 sqrt(2)-1)^2
maxq=None
cells=0
for i,j,k in product(range(8), repeat=3):
    sol=solve3([eq_row(0,i),eq_row(1,j),eq_row(2,k)])
    if sol is None: continue
    z0,d=sol
    base=base_interval(z0,d)
    if base is None: continue
    blo,bhi=base
    if blo is None or bhi is None:
        raise AssertionError('unit-sphere cell unexpectedly unbounded')
    for a,b in product(range(8),repeat=2):
        I=dom_interval(z0,d,blo,bhi,0,a)
        if I is None: continue
        I=dom_interval(z0,d,*I,1,b)
        if I is None: continue
        lo,hi=I
        if lo is None or hi is None: raise AssertionError('dominance cell unbounded')
        A0,A1=affine(out_row(0,a),z0,d)
        B0,B1=affine(out_row(1,b),z0,d)
        c0,c1,c2=prod_coeff(A0,A1,B0,B1)
        cand=[lo,hi]
        if c2.sign()<0:
            tv=-c1/(TWO*c2)
            if within(tv,lo,hi): cand.append(tv)
        for t in cand:
            val=eval_quad(c0,c1,c2,t)
            if val>M:
                raise AssertionError(f'upper bound failed: {val} > {M}')
            if maxq is None or val>maxq: maxq=val
        cells+=1

# Exact equality witness.
x=[ONE,R-ONE]
y=[Q2(3,-2),ONE]
def N(z):
    return max(dot(f,z) for f in F)
def vecadd(u,v): return [u[0]+v[0],u[1]+v[1]]
def vecsub(u,v): return [u[0]-v[0],u[1]-v[1]]
def scale(a,u): return [a*u[0],a*u[1]]
assert N(x)==ONE and N(y)==ONE and N(vecsub(x,y))==ONE
A=N(vecadd(x,y)); B=N(vecsub(scale(TWO,x),y))
TARGET=Q2(-1,2) # 2 sqrt(2)-1
assert A==TARGET and B==TARGET and A*B==M
assert maxq==M
print('VERIFY_OK')
print('cells',cells)
print('max_product',maxq)
print('witness_factor',TARGET)
