from fractions import Fraction as F
from itertools import product

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
r=Q2(0,F(1,2))  # 1/sqrt(2)=sqrt(2)/2
# support functionals h with N(v)=max h(v)
H=[(Q2(1),Q2(0)),(Q2(-1),Q2(0)),(Q2(0),Q2(1)),(Q2(0),Q2(-1)),
   (r,r),(-r,r),(r,-r),(-r,-r)]

def dot(h,v): return h[0]*v[0]+h[1]*v[1]

def solve4(rows, rhs):
    A=[list(row)+[b] for row,b in zip(rows,rhs)]
    n=4
    for c in range(n):
        p=next((i for i in range(c,n) if A[i][c]!=ZERO),None)
        if p is None: return None
        A[c],A[p]=A[p],A[c]
        z=A[c][c]
        A[c]=[x/z for x in A[c]]
        for i in range(n):
            if i==c: continue
            z=A[i][c]
            if z!=ZERO:
                A[i]=[A[i][j]-z*A[c][j] for j in range(n+1)]
    return [A[i][n] for i in range(n)]

def blockrow(which,h):
    hx,hy=h
    if which==0: return (hx,hy,ZERO,ZERO) # x
    if which==1: return (ZERO,ZERO,hx,hy) # y
    if which==2: return (hx,hy,-hx,-hy)   # x-y
    raise ValueError

def feasible(v):
    x=(v[0],v[1]); y=(v[2],v[3]); d=(v[0]-v[2],v[1]-v[3])
    return all(dot(h,w)<=ONE for w in (x,y,d) for h in H)

def norm(v): return max((dot(h,v) for h in H), key=lambda z: float(z.a)+float(z.b)*2**0.5)

target=Q2(-1,2) # 2 sqrt2 - 1
maxval=ZERO; witness=None; feasible_systems=0; unique=set()
for i,j,k in product(range(8), repeat=3):
    base=[blockrow(0,H[i]),blockrow(1,H[j]),blockrow(2,H[k])]
    for w in range(3):
        for ell in range(8):
            sol=solve4(base+[blockrow(w,H[ell])],[ONE]*4)
            if sol is None or not feasible(sol): continue
            feasible_systems += 1
            key=tuple((z.a,z.b) for z in sol)
            unique.add(key)
            x=(sol[0],sol[1]); y=(sol[2],sol[3])
            s=(x[0]+y[0],x[1]+y[1])
            val=norm(s)
            if maxval<val:
                maxval=val; witness=(x,y,(x[0]-y[0],x[1]-y[1]),s)
if maxval!=target:
    raise SystemExit(f'FAIL max={maxval}, target={target}')
# explicit witness a=(1,sqrt2-1), b=(2sqrt2-2,2-sqrt2) after sign normalization.
x=(Q2(1),Q2(1,-1))
y=(Q2(-2,2),Q2(2,-1))
d=(x[0]-y[0],x[1]-y[1]); s=(x[0]+y[0],x[1]+y[1])
if norm(x)!=ONE or norm(y)!=ONE or norm(d)!=ONE or norm(s)!=target:
    raise SystemExit('FAIL explicit witness')
print('VERIFY_OK')
print('feasible_active_systems',feasible_systems)
print('unique_vertices',len(unique))
print('maximum','2*sqrt(2)-1')
print('explicit_witness_x','(1,1-sqrt(2))')
print('explicit_witness_y','(2*sqrt(2)-2,2-sqrt(2))')
