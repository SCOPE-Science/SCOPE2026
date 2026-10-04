#!/usr/bin/env python3
from fractions import Fraction as F

class Q2:
    __slots__=('a','b')
    def __init__(self,a=0,b=0): self.a=F(a); self.b=F(b)
    def __add__(self,o): o=q(o); return Q2(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return Q2(-self.a,-self.b)
    def __sub__(self,o): return self+(-q(o))
    def __rsub__(self,o): return q(o)-self
    def __mul__(self,o):
        o=q(o); return Q2(self.a*o.a+2*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def __pow__(self,n):
        if n==2: return self*self
        if n==0: return Q2(1)
        if n==1: return self
        raise ValueError('only powers 0,1,2 supported')
    def inv(self):
        d=self.a*self.a-2*self.b*self.b
        if d==0: raise ZeroDivisionError
        return Q2(self.a/d,-self.b/d)
    def __truediv__(self,o): return self*q(o).inv()
    def __rtruediv__(self,o): return q(o)*self.inv()
    def __eq__(self,o): o=q(o); return self.a==o.a and self.b==o.b
    def sign(self):
        a,b=self.a,self.b
        if a==0:
            return (b>0)-(b<0)
        if b==0:
            return (a>0)-(a<0)
        if a>0 and b>0: return 1
        if a<0 and b<0: return -1
        # opposite signs: compare |a| with |b| sqrt(2)
        aa=a*a; bb=2*b*b
        if aa==bb: return 0
        if a>0: return 1 if aa>bb else -1
        return -1 if aa>bb else 1
    def __lt__(self,o): return (self-q(o)).sign()<0
    def __le__(self,o): return (self-q(o)).sign()<=0
    def __gt__(self,o): return (self-q(o)).sign()>0
    def __ge__(self,o): return (self-q(o)).sign()>=0
    def __hash__(self): return hash((self.a,self.b))
    def __repr__(self):
        if self.b==0:return str(self.a)
        if self.a==0:return f'{self.b}*sqrt2'
        s='+' if self.b>0 else '-'
        return f'{self.a}{s}{abs(self.b)}*sqrt2'
    def fl(self): return float(self.a)+float(self.b)*(2**0.5)

def q(x): return x if isinstance(x,Q2) else Q2(x)
r=Q2(0,1)
h=r/2
SUP=[(q(1),q(0)),(q(-1),q(0)),(q(0),q(1)),(q(0),q(-1)),
     (h,h),(-h,-h),(h,-h),(-h,h)]

class Aff:
    __slots__=('c','m')
    def __init__(self,c=0,m=0): self.c=q(c); self.m=q(m)
    def __add__(self,o): o=aff(o); return Aff(self.c+o.c,self.m+o.m)
    __radd__=__add__
    def __neg__(self): return Aff(-self.c,-self.m)
    def __sub__(self,o): return self+(-aff(o))
    def __rsub__(self,o): return aff(o)-self
    def __mul__(self,o):
        if isinstance(o,Aff): raise TypeError('affine*affine not affine')
        o=q(o); return Aff(self.c*o,self.m*o)
    __rmul__=__mul__
    def at(self,t): return self.c+self.m*q(t)
    def __repr__(self): return f'({self.c})+({self.m})t'
def aff(x): return x if isinstance(x,Aff) else Aff(x,0)

def sf(i,u,v):
    a,b=SUP[i]
    return u*a+v*b

def solve2(b,c):
    # f_b(y)=1 ; f_c(x-y)=1, x=(1,t)
    a,bv=SUP[b]; cc,d=SUP[c]
    det=a*d-bv*cc
    if det==0:return None
    # cc*y1+d*y2 = cc + d*t - 1
    R1=Aff(1,0); R2=Aff(cc-1,d)
    y1=(R1*d-R2*bv)*(q(1)/det)
    y2=(R2*a-R1*cc)*(q(1)/det)
    return y1,y2

def intersect(ineqs):
    # affine <=0
    lo=Q2(1-r.a, -1) # placeholder overwritten; no infinities necessary
    hi=Q2(-1+r.a, 1)
    # Actually start x-facet interval [1-sqrt2,sqrt2-1]
    lo=Q2(1,-1); hi=Q2(-1,1)
    for g in ineqs:
        if g.m==0:
            if g.c>0:return None
        elif g.m>0:
            bd=-g.c/g.m
            if bd<hi: hi=bd
        else:
            bd=-g.c/g.m
            if bd>lo: lo=bd
    if lo>hi:return None
    return lo,hi

def crossings(U,lo,hi):
    vals=[sf(i,*U) for i in range(8)]
    out=[]
    for i in range(8):
        for j in range(i+1,8):
            d=vals[i]-vals[j]
            if d.m!=0:
                z=-d.c/d.m
                if lo<=z<=hi: out.append(z)
    return out

def norm_at(U,z): return max((sf(i,*U).at(z) for i in range(8)))

def quad_for_support(U,i):
    L=sf(i,*U)
    # square affine: c^2 + 2cm t + m^2 t^2
    return (L.c*L.c, 2*L.c*L.m, L.m*L.m)

def addq(A,B):return tuple(A[i]+B[i] for i in range(3))
def qeval(Q,z):return Q[0]+Q[1]*z+Q[2]*z*z

# Exhaustive nonparallel active-facet decomposition.
segments=[]
for ib in range(8):
  for ic in range(8):
    sol=solve2(ib,ic)
    if sol is None: continue
    y1,y2=sol
    x1,x2=Aff(1),Aff(0,1)
    d1,d2=x1-y1,x2-y2
    ineq=[]
    for j in range(8):
        ineq += [sf(j,x1,x2)-1, sf(j,y1,y2)-1, sf(j,d1,d2)-1]
    I=intersect(ineq)
    if I is not None:
        segments.append((ib,ic,I[0],I[1],y1,y2))

# Degenerate/parallel active lines: same direction would require f_b(x)=2, impossible.
# Opposite directions require f_b(x)=0. For horizontal support this is impossible;
# for diagonal supports it forces t=+/-1 outside the x-facet interval; for vertical
# supports it forces t=0, but then y=(u,+/-1) gives u<=sqrt(2)-1 from N(y)<=1
# while N(x-y)<=1 forces u>=2-sqrt(2), contradiction.
for ib in range(8):
  for ic in range(8):
    a,b=SUP[ib]; c,d=SUP[ic]
    if a*d-b*c!=0: continue
    if (a,b)==(c,d):
        continue
    if (a,b)==(-c,-d):
        if ib in (0,1):
            continue
        if ib in (4,5,6,7):
            # f_b(1,t)=0 gives |t|=1, outside |t|<=sqrt2-1.
            assert Q2(-1,1) < q(1)
            continue
        if ib in (2,3):
            assert Q2(-1,1) < Q2(2,-1)  # sqrt2-1 < 2-sqrt2
            continue
    raise AssertionError('unexpected parallel supports')

# Deduplicate identical affine feasible branches.
uniq=[]
for s in segments:
    key=(s[2],s[3],s[4].c,s[4].m,s[5].c,s[5].m)
    if key not in [u[0] for u in uniq]: uniq.append((key,s))
segments=[s for _,s in uniq]
assert len(segments)==6, len(segments)

expected=set([
 (Q2(3,-2),Q2(-1,1), Q2(2,-1),q(-1), q(1),q(0)), # y1=2-r-t, y2=1
 (Q2(1,-1),Q2(-3,2), Q2(2,-1),q(1), q(-1),q(0)), # y1=2-r+t, y2=-1
 (Q2(1,-1),Q2(-3,2), Q2(-1,1),q(-1), q(1),q(1)), # y1=r-1-t,y2=1+t
 (Q2(-3,2),Q2(3,-2), Q2(F(1,2)),q(F(-1,2)), Q2(F(-1,2),1),q(F(1,2))),
 (Q2(3,-2),Q2(-1,1), Q2(-1,1),q(1), q(-1),q(1)),
 (Q2(-3,2),Q2(3,-2), Q2(F(1,2)),q(F(1,2)), Q2(F(1,2),-1),q(F(1,2))),
])
got={(lo,hi,y1.c,y1.m,y2.c,y2.m) for _,_,lo,hi,y1,y2 in segments}
assert got==expected, (got,expected)

best=None; checked_cells=0
for ib,ic,lo,hi,y1,y2 in segments:
    U=(Aff(1)+y1,Aff(0,1)+y2)       # x+y
    V=(Aff(2)-y1,Aff(0,2)-y2)       # 2x-y
    pts=set([lo,hi]+crossings(U,lo,hi)+crossings(V,lo,hi))
    pts=sorted(pts)
    # Adjacent switch intervals: identify active supports at midpoint and prove convexity.
    for a,b in zip(pts,pts[1:]):
        mid=(a+b)/2
        ui=max(range(8),key=lambda i:sf(i,*U).at(mid))
        vi=max(range(8),key=lambda i:sf(i,*V).at(mid))
        Q=addq(quad_for_support(U,ui),quad_for_support(V,vi))
        assert Q[2]>=0
        # Check exact endpoint values using true max-norm, enough for convex quadratic.
        for z in (a,b):
            val=norm_at(U,z)**2+norm_at(V,z)**2
            if best is None or val>best[0]: best=(val,z,ib,ic,y1.at(z),y2.at(z))
        checked_cells+=1
    if len(pts)==1:
        z=pts[0]; val=norm_at(U,z)**2+norm_at(V,z)**2
        if best is None or val>best[0]: best=(val,z,ib,ic,y1.at(z),y2.at(z))

TARGET=Q2(18,-8)
assert best[0]==TARGET, best
# Explicit witness.
x=(q(1),Q2(-1,1))
y=(Q2(3,-2),q(1))
def nrm(P): return max(sf(i,q(P[0]),q(P[1])) for i in range(8))
def sub(A,B): return (A[0]-B[0],A[1]-B[1])
def add(A,B): return (A[0]+B[0],A[1]+B[1])
def smul(c,A): return (q(c)*A[0],q(c)*A[1])
assert nrm(x)==1 and nrm(y)==1 and nrm(sub(x,y))==1
M=Q2(-1,2) # 2sqrt2-1
assert nrm(add(x,y))==M
assert nrm(sub(smul(2,x),y))==M
assert 2*M*M==TARGET
print('segments=6')
print('piecewise_cells=',checked_cells)
print('maximum=',TARGET,'approx=',TARGET.fl())
print('witness=',x,y)
print('VERIFY_OK')
