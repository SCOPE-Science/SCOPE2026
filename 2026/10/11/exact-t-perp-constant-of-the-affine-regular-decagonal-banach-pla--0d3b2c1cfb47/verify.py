from fractions import Fraction
from itertools import combinations

class Q5:
    __slots__=('a','b')
    def __init__(self,a=0,b=0):
        if isinstance(a,Q5) and b==0:
            self.a,self.b=a.a,a.b
        else:
            self.a=Fraction(a); self.b=Fraction(b)
    def __add__(self,o): o=q(o); return Q5(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return Q5(-self.a,-self.b)
    def __sub__(self,o): return self+(-q(o))
    def __rsub__(self,o): return q(o)-self
    def __mul__(self,o): o=q(o); return Q5(self.a*o.a+5*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def inv(self):
        d=self.a*self.a-5*self.b*self.b
        assert d
        return Q5(self.a/d,-self.b/d)
    def __truediv__(self,o): return self*q(o).inv()
    def __rtruediv__(self,o): return q(o)/self
    def __eq__(self,o):
        try:o=q(o)
        except:return False
        return self.a==o.a and self.b==o.b
    def sign(self):
        a,b=self.a,self.b
        if a==0 and b==0:return 0
        if b==0:return 1 if a>0 else -1
        if a==0:return 1 if b>0 else -1
        if a>0 and b>0:return 1
        if a<0 and b<0:return -1
        c=a*a-5*b*b
        if a>0 and b<0:return 1 if c>0 else -1
        if a<0 and b>0:return -1 if c>0 else 1
        raise AssertionError
    def __lt__(self,o): return (self-q(o)).sign()<0
    def __le__(self,o): return (self-q(o)).sign()<=0
    def __gt__(self,o): return (self-q(o)).sign()>0
    def __ge__(self,o): return (self-q(o)).sign()>=0
    def __abs__(self): return self if self.sign()>=0 else -self
    def __repr__(self): return f'({self.a})+({self.b})sqrt5'

def q(x): return x if isinstance(x,Q5) else Q5(x)
Z=Q5(); O=Q5(1); rt5=Q5(0,1); r=(rt5-1)/2; phi=(1+rt5)/2
fac=[
    (O,O),(r,O),(Z,r),(-r,Z),(-O,-r),
    (-O,-O),(-r,-O),(Z,-r),(r,Z),(O,r)
]

def dot(f,v): return f[0]*v[0]+f[1]*v[1]
def add(u,v): return (u[0]+v[0],u[1]+v[1])
def sub(u,v): return (u[0]-v[0],u[1]-v[1])
def scale(c,v): c=q(c); return (c*v[0],c*v[1])
def norm(v): return max(dot(f,v) for f in fac)

def solve2(f,g):
    det=f[0]*g[1]-f[1]*g[0]
    assert det!=0
    return ((g[1]-f[1])/det,(f[0]-g[0])/det)

# v_i is intersection of facet i and i+1.
verts=[solve2(fac[i],fac[(i+1)%10]) for i in range(10)]
assert all(norm(v)==1 for v in verts)
# facet i edge endpoints v_{i-1}, v_i
edges=[(verts[(i-1)%10],verts[i]) for i in range(10)]
for i,e in enumerate(edges):
    assert dot(fac[i],e[0])==dot(fac[i],e[1])==1

# Affine line segment helper: z(t)=a+t(b-a), t in [lo,hi].
def segpoint(a,b,t): return add(a,scale(t,sub(b,a)))

# Find exact interval t in [0,1] where two affine conditions have sign product <=0.
def linear_val_at(f,a,b,t): return dot(f,segpoint(a,b,t))

def roots_in_unit(f,a,b):
    va=dot(f,a); dv=dot(f,sub(b,a))
    if dv==0:return []
    t=-va/dv
    return [t] if 0<t<1 else []

def allowed_intervals_vertex(i,a,b):
    f=fac[i]; g=fac[(i+1)%10]
    cuts=[Q5(0),Q5(1)] + roots_in_unit(f,a,b)+roots_in_unit(g,a,b)
    # unique sort
    cuts=sorted(Q5(a,b) for a,b in set((c.a,c.b) for c in cuts))
    out=[]
    for u,v in zip(cuts,cuts[1:]):
        m=(u+v)/2
        if (linear_val_at(f,a,b,m)*linear_val_at(g,a,b,m))<=0:
            out.append((u,v))
    # include isolated zeros? If product <=0 only at a cut, it does not matter for sup but verify endpoints can be folded.
    return out

# For affine y(t), compute max over t interval of N(x+y)*N(2x-y).
# Both norms are maxima of ten affine functions. Partition at every pairwise crossing for both envelopes.
def affine_coeff(f,base,dir): return dot(f,base),dot(f,dir)

def envelope_product_max(x,a,b,lo=Q5(0),hi=Q5(1)):
    d=sub(b,a)
    baseA=add(x,a); dirA=d
    baseB=sub(scale(2,x),a); dirB=scale(-1,d)
    AA=[affine_coeff(f,baseA,dirA) for f in fac]
    BB=[affine_coeff(f,baseB,dirB) for f in fac]
    cuts=[lo,hi]
    for arr in (AA,BB):
        for (c1,m1),(c2,m2) in combinations(arr,2):
            den=m1-m2
            if den!=0:
                t=(c2-c1)/den
                if lo<t<hi: cuts.append(t)
    # exact unique sort
    uniq={(t.a,t.b):t for t in cuts}
    cuts=sorted(uniq.values())
    best=None; best_t=None
    def val(t):
        y=segpoint(a,b,t)
        return norm(add(x,y))*norm(sub(scale(2,x),y))
    # Endpoints
    for t in cuts:
        z=val(t)
        if best is None or best<z: best,best_t=z,t
    # Each open cell has fixed active affine forms, hence a quadratic product.
    for u,v in zip(cuts,cuts[1:]):
        m=(u+v)/2
        def active(arr):
            vals=[c+s*m for c,s in arr]
            return max(range(10),key=lambda k: vals[k])
        ia=active(AA); ib=active(BB)
        ca,ma=AA[ia]; cb,mb=BB[ib]
        # product derivative = ma*(cb+mb t)+mb*(ca+ma t)
        den=2*ma*mb
        num=ma*cb+mb*ca
        if den!=0:
            t=-num/den
            if u<t<v:
                z=val(t)
                if best<z: best,best_t=z,t
    return best,best_t

# Smooth-edge Birkhoff cases are handled by the direct routine below.
# Direct routine variable x on edge, fixed y.
def edge_x_product_max(a,b,y):
    d=sub(b,a)
    # A=N(x+y), B=N(2x-y)
    AA=[affine_coeff(f,add(a,y),d) for f in fac]
    BB=[affine_coeff(f,sub(scale(2,a),y),scale(2,d)) for f in fac]
    cuts=[Q5(0),Q5(1)]
    for arr in (AA,BB):
        for (c1,m1),(c2,m2) in combinations(arr,2):
            den=m1-m2
            if den!=0:
                t=(c2-c1)/den
                if 0<t<1: cuts.append(t)
    uniq={(t.a,t.b):t for t in cuts}; cuts=sorted(uniq.values())
    def val(t):
        x=segpoint(a,b,t)
        return norm(add(x,y))*norm(sub(scale(2,x),y))
    best=max(((val(t),t) for t in cuts),key=lambda z:z[0])
    for u,v in zip(cuts,cuts[1:]):
        m=(u+v)/2
        ia=max(range(10),key=lambda k:AA[k][0]+AA[k][1]*m)
        ib=max(range(10),key=lambda k:BB[k][0]+BB[k][1]*m)
        ca,ma=AA[ia]; cb,mb=BB[ib]
        den=2*ma*mb; num=ma*cb+mb*ca
        if den!=0:
            t=-num/den
            if u<t<v:
                z=val(t)
                if best[0]<z:best=(z,t)
    return best

edge_global=None; edge_record=None
for i,(a,b) in enumerate(edges):
    f=fac[i]; k=(f[1],-f[0]); nk=norm(k); y=(k[0]/nk,k[1]/nk)
    for sgn in (1,-1):
        yy=scale(sgn,y)
        assert norm(yy)==1 and dot(f,yy)==0
        z,t=edge_x_product_max(a,b,yy)
        if edge_global is None or edge_global<z:
            edge_global=z; edge_record=(i,sgn,t,segpoint(a,b,t),yy)

# Vertex cases: x=v_i, active facets i and i+1. Enumerate y edge subsegments where the two values straddle zero.
vertex_global=None; vertex_record=None; allowed=0
for i,x in enumerate(verts):
    for j,(a,b) in enumerate(edges):
        for lo,hi in allowed_intervals_vertex(i,a,b):
            allowed+=1
            z,t=envelope_product_max(x,a,b,lo,hi)
            if vertex_global is None or vertex_global<z:
                vertex_global=z; vertex_record=(i,j,lo,hi,t,x,segpoint(a,b,t))

expected_edge=(Q5(63)-5*rt5)/16
expected_vertex=(Q5(2)+5*rt5)/4
assert edge_global==expected_edge,(edge_global,expected_edge,edge_record)
assert vertex_global==expected_vertex,(vertex_global,expected_vertex,vertex_record)
assert allowed==20,allowed
assert edge_global<vertex_global

# Explicit maximizing pair x=(0,1), y=(-phi,(1+phi)/2)
x=(Q5(0),Q5(1)); y=(-phi,(Q5(1)+phi)/2)
assert norm(x)==norm(y)==1
assert dot(fac[0],y)<0<dot(fac[1],y)
A=norm(add(x,y)); B=norm(sub(scale(2,x),y))
assert A==(Q5(-1)+3*rt5)/4,(A,)
assert B==(Q5(7)+rt5)/4,(B,)
assert A*B==expected_vertex

print('VERIFY_OK edges=10 vertex_allowed_segments=20 edge_max=(63-5sqrt5)/16 global=(2+5sqrt5)/4')
