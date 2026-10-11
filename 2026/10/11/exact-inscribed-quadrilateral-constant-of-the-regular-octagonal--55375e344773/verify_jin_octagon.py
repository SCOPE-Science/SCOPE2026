from fractions import Fraction as F
from itertools import product, combinations

class Q2:
    __slots__=('a','b')
    def __init__(self,a=0,b=0):
        self.a=F(a); self.b=F(b)
    def __add__(self,o): o=q(o); return Q2(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return Q2(-self.a,-self.b)
    def __sub__(self,o): return self+(-q(o))
    def __rsub__(self,o): return q(o)-self
    def __mul__(self,o):
        o=q(o); return Q2(self.a*o.a+2*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def __truediv__(self,o):
        o=q(o); den=o.a*o.a-2*o.b*o.b
        assert den != 0
        return Q2((self.a*o.a-2*self.b*o.b)/den,(self.b*o.a-self.a*o.b)/den)
    def __rtruediv__(self,o): return q(o)/self
    def __eq__(self,o): o=q(o); return self.a==o.a and self.b==o.b
    def __lt__(self,o): return sign(self-q(o))<0
    def __le__(self,o): return sign(self-q(o))<=0
    def __repr__(self): return f'({self.a})+({self.b})*sqrt2'
def q(x): return x if isinstance(x,Q2) else Q2(x)
def sign(x):
    x=q(x); a,b=x.a,x.b
    if a==0: return (b>0)-(b<0)
    if b==0: return (a>0)-(a<0)
    if a>0 and b>0: return 1
    if a<0 and b<0: return -1
    aa=a*a; bb=2*b*b
    if a>0: return 1 if aa>bb else -1
    return 1 if bb>aa else -1
def qab(x): return -x if sign(x)<0 else x
def qmax(*xs):
    m=xs[0]
    for x in xs[1:]:
        if m < x: m=x
    return m

ZERO=Q2(0); ONE=Q2(1); S=Q2(0,1); A=S-ONE
verts=[(ONE,A),(A,ONE),(-A,ONE),(-ONE,A),(-ONE,-A),(-A,-ONE),(A,-ONE),(ONE,-A)]
edges=[]
for i in range(8):
    p=verts[i]; z=verts[(i+1)%8]
    edges.append((p,(z[0]-p[0],z[1]-p[1])))

def N(p):
    x,y=p; ax,ay=qab(x),qab(y)
    return qmax(ax,ay,(ax+ay)/S)
def sq(x): return x*x
def obj(pts):
    z=ZERO
    for i,j in combinations(range(4),2):
        z += sq(N((pts[i][0]-pts[j][0],pts[i][1]-pts[j][1])))
    return z

def det(c1,c2): return c1[0]*c2[1]-c1[1]*c2[0]
def solve2(c1,c2,rhs):
    d=det(c1,c2); assert d!=ZERO
    return ((rhs[0]*c2[1]-c2[0]*rhs[1])/d,
            (c1[0]*rhs[1]-rhs[0]*c1[1])/d)
def in01(t): return ZERO<=t and t<=ONE

target=Q2(40,-16)
maxv=Q2(-1000); maxpts=None
cand=0; r1cand=0; r2cand=0; feasible_tuples=0
rank_counts={1:0,2:0}
for ids in product(range(8), repeat=4):
    bases=[edges[i][0] for i in ids]; dirs=[edges[i][1] for i in ids]
    rhs=(-sum((p[0] for p in bases),ZERO),-sum((p[1] for p in bases),ZERO))
    rank=1
    for i,j in combinations(range(4),2):
        if det(dirs[i],dirs[j])!=ZERO:
            rank=2; break
    rank_counts[rank]+=1
    local=0
    if rank==2:
        for fixed in combinations(range(4),2):
            free=[i for i in range(4) if i not in fixed]
            if det(dirs[free[0]],dirs[free[1]])==ZERO: continue
            for vals in product([ZERO,ONE], repeat=2):
                rr=[rhs[0],rhs[1]]
                for k,v in zip(fixed,vals):
                    rr[0]-=dirs[k][0]*v; rr[1]-=dirs[k][1]*v
                u,v=solve2(dirs[free[0]],dirs[free[1]],rr)
                if not(in01(u) and in01(v)): continue
                ts=[None]*4
                for k,w in zip(fixed,vals): ts[k]=w
                ts[free[0]]=u; ts[free[1]]=v
                # exact centroid check
                sx=sy=ZERO
                pts=[]
                for b,d,t in zip(bases,dirs,ts):
                    p=(b[0]+d[0]*t,b[1]+d[1]*t); pts.append(p); sx+=p[0]; sy+=p[1]
                assert sx==ZERO and sy==ZERO
                val=obj(pts); cand+=1; r2cand+=1; local+=1
                if maxv<val: maxv=val; maxpts=pts
    else:
        for fixed in combinations(range(4),3):
            free=[i for i in range(4) if i not in fixed][0]
            d=dirs[free]
            for vals in product([ZERO,ONE], repeat=3):
                rr=[rhs[0],rhs[1]]
                for k,v in zip(fixed,vals):
                    rr[0]-=dirs[k][0]*v; rr[1]-=dirs[k][1]*v
                if d[0]!=ZERO: u=rr[0]/d[0]
                elif d[1]!=ZERO: u=rr[1]/d[1]
                else: continue
                if d[0]*u!=rr[0] or d[1]*u!=rr[1] or not in01(u): continue
                ts=[None]*4
                for k,w in zip(fixed,vals): ts[k]=w
                ts[free]=u
                sx=sy=ZERO; pts=[]
                for b,dd,t in zip(bases,dirs,ts):
                    p=(b[0]+dd[0]*t,b[1]+dd[1]*t); pts.append(p); sx+=p[0]; sy+=p[1]
                assert sx==ZERO and sy==ZERO
                val=obj(pts); cand+=1; r1cand+=1; local+=1
                if maxv<val: maxv=val; maxpts=pts
    if local: feasible_tuples+=1

assert rank_counts=={1:64,2:4032}, rank_counts
assert cand==11712, cand
assert r1cand==576 and r2cand==11136, (r1cand,r2cand)
assert maxv==target,(maxv,target,maxpts)

# Explicit witness and independent modified von Neumann--Jordan constant.
w=[verts[0],verts[1],verts[4],verts[5]]
assert all(N(p)==ONE for p in w)
assert sum((p[0] for p in w),ZERO)==ZERO and sum((p[1] for p in w),ZERO)==ZERO
assert obj(w)==target
cnj=ZERO
for x in verts:
    for y in verts:
        v=(sq(N((x[0]+y[0],x[1]+y[1])))+sq(N((x[0]-y[0],x[1]-y[1]))))/Q2(4)
        if cnj<v: cnj=v
assert cnj==Q2(4,-2),cnj
assert target==Q2(8)+Q2(8)*cnj

print('VERIFY_OK')
print('rank1_edge_tuples=64')
print('rank2_edge_tuples=4032')
print(f'candidate_occurrences={cand}')
print(f'rank1_candidates={r1cand}')
print(f'rank2_candidates={r2cand}')
print(f'feasible_edge_tuples={feasible_tuples}')
print('J_in=40-16*sqrt(2)')
print('C_NJ_prime=4-2*sqrt(2)')
print('identity=J_in=8+8*C_NJ_prime')
