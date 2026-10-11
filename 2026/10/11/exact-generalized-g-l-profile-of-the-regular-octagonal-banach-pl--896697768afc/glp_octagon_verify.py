from fractions import Fraction as F
from itertools import product, combinations

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
    def __rtruediv__(self,o): return q(o)/self
    def __eq__(self,o): o=q(o); return self.a==o.a and self.b==o.b
    def sign(self):
        a,b=self.a,self.b
        if a==0: return (b>0)-(b<0)
        if b==0: return (a>0)-(a<0)
        if a>0 and b>0: return 1
        if a<0 and b<0: return -1
        # opposite signs; compare |a| with |b|*sqrt(2) by squaring.
        c=a*a-2*b*b
        if c==0: return 0
        if a>0: return 1 if c>0 else -1
        return -1 if c>0 else 1
    def __lt__(self,o): return (self-q(o)).sign()<0
    def __le__(self,o): return (self-q(o)).sign()<=0
    def __hash__(self): return hash((self.a,self.b))
    def __repr__(self): return f'Q2({self.a},{self.b})'
    def fmt(self):
        a,b=self.a,self.b
        if b==0: return str(a)
        if a==0: return f'{b}*sqrt(2)'
        sg='+' if b>0 else '-'
        return f'{a}{sg}{abs(b)}*sqrt(2)'

def q(x): return x if isinstance(x,Q2) else Q2(x,0)
ZERO,ONE,TWO=Q2(0),Q2(1),Q2(2)
R=Q2(0,1)
qv=R-ONE

def vadd(x,y): return (x[0]+y[0],x[1]+y[1])
def vsub(x,y): return (x[0]-y[0],x[1]-y[1])
def vscale(a,x): return (a*x[0],a*x[1])
def dot(h,x): return h[0]*x[0]+h[1]*x[1]

V=[(ONE,qv),(qv,ONE),(-qv,ONE),(-ONE,qv),(-ONE,-qv),(-qv,-ONE),(qv,-ONE),(ONE,-qv)]
D=[vsub(V[(i+1)%8],V[i]) for i in range(8)]
# Eight supporting functionals h with N(w)=max h(w).
H=[(R/TWO,R/TWO),(ZERO,ONE),(-R/TWO,R/TWO),(-ONE,ZERO),(-R/TWO,-R/TWO),(ZERO,-ONE),(R/TWO,-R/TWO),(ONE,ZERO)]

def norm(w):
    vals=[dot(h,w) for h in H]
    m=vals[0]
    for z in vals[1:]:
        if m<z: m=z
    return m

def solve_family(i,j,k):
    # Solve V_i+tD_i - V_j-uD_j = V_k+vD_k.
    cols=[D[i],vscale(-ONE,D[j]),vscale(-ONE,D[k])]
    rhs=vsub(vsub(V[j],V[i]),vscale(-ONE,V[k])) # = -V_i+V_j+V_k
    # choose one free variable, solve the other two by Cramer's rule.
    for free in range(3):
        dep=[z for z in range(3) if z!=free]
        a,b=cols[dep[0]],cols[dep[1]]
        det=a[0]*b[1]-a[1]*b[0]
        if det==ZERO: continue
        c=cols[free]
        # a*p+b*q = rhs-c*s; p=p0+p1*s, q=q0+q1*s
        def solve2(rr):
            p=(rr[0]*b[1]-rr[1]*b[0])/det
            qq=(a[0]*rr[1]-a[1]*rr[0])/det
            return p,qq
        p0,q0=solve2(rhs)
        p1,q1=solve2(vscale(-ONE,c))
        vals=[None,None,None]
        vals[free]=(ZERO,ONE) # intercept, slope
        vals[dep[0]]=(p0,p1)
        vals[dep[1]]=(q0,q1)
        return vals
    return None

def interval_for_affines(vals):
    lo,hi=None,None
    for b,a in vals: # z=b+a*s in [0,1]
        if a==ZERO:
            if b<ZERO or ONE<b: return None
            continue
        r0=(ZERO-b)/a; r1=(ONE-b)/a
        l,h=(r0,r1) if r0<r1 else (r1,r0)
        lo=l if lo is None or lo<l else lo
        hi=h if hi is None or h<hi else hi
    if lo is None: lo=ZERO
    if hi is None: hi=ONE
    if hi<lo: return None
    return lo,hi

def eval_aff(pair,s):
    b,a=pair; return b+a*s

def affine_vec(base,dir,pair):
    b,a=pair
    return (vadd(base,vscale(b,dir)), vscale(a,dir)) # intercept, slope

def sum_aff(A,B): return (vadd(A[0],B[0]),vadd(A[1],B[1]))
def scale_aff(c,A): return (vscale(c,A[0]),vscale(c,A[1]))
def sub_aff(A,B): return (vsub(A[0],B[0]),vsub(A[1],B[1]))
def eval_vec_aff(A,s): return vadd(A[0],vscale(s,A[1]))

target=TWO*R-ONE
maxA=ZERO; maxB=ZERO
families=0; candidate_points=0
observed=set()
for i,j,k in product(range(8),repeat=3):
    vals=solve_family(i,j,k)
    if vals is None: continue
    I=interval_for_affines(vals)
    if I is None: continue
    lo,hi=I; families+=1
    X=affine_vec(V[i],D[i],vals[0])
    Y=affine_vec(V[j],D[j],vals[1])
    W1=sum_aff(X,Y)
    W2=sub_aff(scale_aff(TWO,X),Y)
    cuts={lo,hi}
    for W in (W1,W2):
        forms=[]
        for h in H:
            forms.append((dot(h,W[0]),dot(h,W[1])))
        for f,g in combinations(forms,2):
            db=f[0]-g[0]; da=f[1]-g[1]
            if da!=ZERO:
                root=-db/da
                if lo<=root and root<=hi: cuts.add(root)
    for s in cuts:
        candidate_points+=1
        a=norm(eval_vec_aff(W1,s)); b=norm(eval_vec_aff(W2,s))
        observed.add((a,b))
        if maxA<a: maxA=a
        if maxB<b: maxB=b
        if target<a or target<b:
            raise AssertionError(('bound failure',i,j,k,s,a,b))

# Explicit simultaneous equality pair.
x=(ONE,qv)
y=(Q2(3,-2),ONE) # (3-2sqrt(2),1)
assert norm(x)==ONE and norm(y)==ONE and norm(vsub(x,y))==ONE
A=norm(vadd(x,y)); B=norm(vsub(vscale(TWO,x),y))
assert A==target and B==target
assert maxA==target and maxB==target
expected={(Q2(3,-1),target),(ONE+R/TWO,target),(target,Q2(3,-1)),(target,ONE+R/TWO),(target,target)}
assert observed==expected, observed

print('VERIFY_OK')
print('feasible_edge_families',families)
print('support_breakpoint_checks',candidate_points)
print('distinct_shifted_norm_pairs',len(observed))
print('max_each',target.fmt())
print('attaining_x',x[0].fmt(),x[1].fmt())
print('attaining_y',y[0].fmt(),y[1].fmt())
