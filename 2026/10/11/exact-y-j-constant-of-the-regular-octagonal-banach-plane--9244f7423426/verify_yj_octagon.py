"""Exact active-facet proof certificate for Y_J of the regular octagonal plane.

Only coefficients in Q(sqrt(2)); all comparisons, including the norm maximum,
are exact. The witness is in the original N(x+y)=1 convention.
"""
from fractions import Fraction as F
from itertools import product

class Q2:
    __slots__ = ('a','b')
    def __init__(self,a=0,b=0): self.a=F(a); self.b=F(b)
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
    def __eq__(self,o): o=q(o); return self.a==o.a and self.b==o.b
    def sign(self):
        a,b=self.a,self.b
        if a==0: return (b>0)-(b<0)
        if b==0: return (a>0)-(a<0)
        if (a>0 and b>0): return 1
        if (a<0 and b<0): return -1
        aa=a*a; bb=2*b*b
        if a>0 and b<0: return 1 if aa>bb else -1
        if a<0 and b>0: return 1 if bb>aa else -1
        raise AssertionError
    def __le__(self,o): return (self-q(o)).sign()<=0
    def __lt__(self,o): return (self-q(o)).sign()<0
    def __repr__(self): return f'({self.a})+({self.b})*sqrt2'

def q(x): return x if isinstance(x,Q2) else Q2(x,0)
ZERO,ONE=Q2(0),Q2(1)
r=Q2(0,F(1,2))  # 1/sqrt(2)
H=[(Q2(1),ZERO),(Q2(-1),ZERO),(ZERO,Q2(1)),(ZERO,Q2(-1)),
   (r,r),(-r,r),(r,-r),(-r,-r)]
def dot(h,v): return h[0]*v[0]+h[1]*v[1]
def solve4(rows,rhs):
    A=[list(row)+[b] for row,b in zip(rows,rhs)]
    for c in range(4):
        p=next((i for i in range(c,4) if A[i][c]!=ZERO),None)
        if p is None: return None
        A[c],A[p]=A[p],A[c]
        z=A[c][c]; A[c]=[x/z for x in A[c]]
        for i in range(4):
            if i==c: continue
            z=A[i][c]
            if z!=ZERO:
                A[i]=[A[i][j]-z*A[c][j] for j in range(5)]
    return [A[i][4] for i in range(4)]
def blockrow(which,h):
    hx,hy=h
    if which==0: return (hx,hy,ZERO,ZERO)
    if which==1: return (ZERO,ZERO,hx,hy)
    if which==2: return (hx,hy,hx,hy)
    raise ValueError
def norm(v): return max(dot(h,v) for h in H)
def feasible(v):
    x=v[:2]; y=v[2:]; s=[x[i]+y[i] for i in range(2)]
    return all(dot(h,w)<=ONE for w in (x,y,s) for h in H)

target=Q2(-1,2)
maxval=ZERO; witness=None; feasible_systems=0; unique=set()
for i,j,k in product(range(8),repeat=3):
    base=[blockrow(0,H[i]),blockrow(1,H[j]),blockrow(2,H[k])]
    for w in range(3):
        for ell in range(8):
            sol=solve4(base+[blockrow(w,H[ell])],[ONE]*4)
            if sol is None or not feasible(sol): continue
            feasible_systems+=1
            unique.add(tuple((z.a,z.b) for z in sol))
            x=sol[:2]; y=sol[2:]
            d=[x[i]-y[i] for i in range(2)]
            val=norm(d)
            if maxval<val: maxval=val; witness=(x,y,d)
if maxval!=target:
    raise SystemExit(f'FAIL max={maxval}, target={target}')
x=[Q2(1),Q2(1,-1)]
y=[Q2(2,-2),Q2(-2,1)]
s=[x[i]+y[i] for i in range(2)]
d=[x[i]-y[i] for i in range(2)]
if [norm(x),norm(y),norm(s),norm(d)]!=[ONE,ONE,ONE,target]:
    raise SystemExit('FAIL explicit witness')
assert len(unique)==48,(len(unique),feasible_systems)
assert feasible_systems==96,(len(unique),feasible_systems)
print('VERIFY_OK')
print('feasible_active_systems',feasible_systems)
print('unique_vertices',len(unique))
print('maximum','2*sqrt(2)-1')
print('explicit_witness_x','(1,1-sqrt(2))')
print('explicit_witness_y','(2-2sqrt(2),sqrt(2)-2)')
