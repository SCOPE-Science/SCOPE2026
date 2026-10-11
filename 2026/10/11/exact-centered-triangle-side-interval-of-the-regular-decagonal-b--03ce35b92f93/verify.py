from fractions import Fraction
import itertools

class Q5:
    __slots__=("a","b")
    def __init__(self,a=0,b=0):
        if isinstance(a,Q5) and b==0:
            self.a,self.b=a.a,a.b
        else:
            self.a=Fraction(a); self.b=Fraction(b)
    def __add__(self,o):
        o=q(o); return Q5(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return Q5(-self.a,-self.b)
    def __sub__(self,o): return self+(-q(o))
    def __rsub__(self,o): return q(o)-self
    def __mul__(self,o):
        o=q(o); return Q5(self.a*o.a+5*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def inv(self):
        d=self.a*self.a-5*self.b*self.b
        assert d
        return Q5(self.a/d,-self.b/d)
    def __truediv__(self,o): return self*q(o).inv()
    def __rtruediv__(self,o): return q(o)/self
    def __eq__(self,o):
        try:o=q(o)
        except Exception:return False
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
    def __repr__(self): return f"Q5({self.a},{self.b})"

def q(x): return x if isinstance(x,Q5) else Q5(x)

rt5=Q5(0,1)
r=(rt5-1)/2

facets=[
    (Q5(1),Q5(1)),
    (r,Q5(1)),
    (Q5(0),r),
    (-r,Q5(0)),
    (Q5(-1),-r),
    (Q5(-1),Q5(-1)),
    (-r,Q5(-1)),
    (Q5(0),-r),
    (r,Q5(0)),
    (Q5(1),r),
]

def row_for(f,block):
    a,b=f
    if block==0:return [a,b,Q5(),Q5()]
    if block==1:return [Q5(),Q5(),a,b]
    return [a,b,-a,-b]

constraints=[]
for block in range(3):
    constraints += [row_for(f,block) for f in facets]

def dot4(row,z):
    return sum((row[i]*z[i] for i in range(4)),Q5())

def solve_line(rows):
    M=[list(rw)+[Q5(1)] for rw in rows]
    piv=[]
    for col in range(4):
        pr=next((i for i in range(len(piv),3) if M[i][col]!=0),None)
        if pr is None: continue
        k=len(piv)
        M[k],M[pr]=M[pr],M[k]
        inv=M[k][col].inv()
        M[k]=[u*inv for u in M[k]]
        for i in range(3):
            if i!=k and M[i][col]!=0:
                c=M[i][col]
                M[i]=[M[i][j]-c*M[k][j] for j in range(5)]
        piv.append(col)
        if len(piv)==3: break
    for rw in M:
        if all(rw[j]==0 for j in range(4)) and rw[4]!=0:
            return "inconsistent",None,None
    if len(piv)<3:
        return "lowrank",None,None
    free=next(j for j in range(4) if j not in piv)
    z0=[Q5() for _ in range(4)]
    d=[Q5() for _ in range(4)]
    d[free]=Q5(1)
    for i,pc in enumerate(piv):
        z0[pc]=M[i][4]
        d[pc]=-M[i][free]
    return "line",z0,d

def interval(z0,d):
    lo=None; hi=None
    for rw in constraints:
        coef=dot4(rw,d)
        rhs=1-dot4(rw,z0)
        sg=coef.sign()
        if sg==0:
            if rhs<0:return None
        else:
            t=rhs/coef
            if sg>0:
                if hi is None or t<hi:hi=t
            else:
                if lo is None or t>lo:lo=t
    assert lo is not None and hi is not None
    if hi<lo:return None
    return lo,hi

def at(z0,d,t):
    return [z0[i]+d[i]*t for i in range(4)]

def fsum(m,z):
    return facets[m][0]*(z[0]+z[2])+facets[m][1]*(z[1]+z[3])

def norm2(v):
    vals=[f[0]*v[0]+f[1]*v[1] for f in facets]
    return max(vals)

def normsum(z):
    return max(fsum(m,z) for m in range(10))

global_min=None
global_max=None
nonempty=0
segments=0
lowrank=0
inconsistent=0

for i,j,k in itertools.product(range(10),repeat=3):
    status,z0,d=solve_line([constraints[i],constraints[10+j],constraints[20+k]])
    if status=="inconsistent":
        inconsistent+=1
        continue
    if status=="lowrank":
        lowrank+=1
        continue
    iv=interval(z0,d)
    if iv is None:
        continue
    lo,hi=iv
    nonempty+=1
    if lo<hi:segments+=1

    # Endpoint values suffice for the convex function's maximum.
    e0=normsum(at(z0,d,lo))
    e1=normsum(at(z0,d,hi))
    local_max=max(e0,e1)

    # Its minimum is at an endpoint or an intersection of affine pieces.
    ts=[lo,hi]
    c0=[fsum(m,z0) for m in range(10)]
    dz=[d[0]+d[2],d[1]+d[3]]
    cd=[facets[m][0]*dz[0]+facets[m][1]*dz[1] for m in range(10)]
    for a in range(10):
        for b in range(a+1,10):
            den=cd[a]-cd[b]
            if den!=0:
                t=(c0[b]-c0[a])/den
                if lo<=t<=hi:
                    ts.append(t)
    local_min=min(normsum(at(z0,d,t)) for t in ts)

    if global_min is None or local_min<global_min:global_min=local_min
    if global_max is None or global_max<local_max:global_max=local_max

expected_min=(Q5(9)-rt5)/4
expected_max=Q5(4)-rt5
assert lowrank==0
assert nonempty==60
assert segments==60
assert global_min==expected_min
assert global_max==expected_max

xmin=[(Q5(1)+rt5)/4,(Q5(3)-rt5)/4]
ymin=[-(Q5(1)+rt5)/4,Q5(3)/2]
xmax=[Q5(1),Q5(0)]
ymax=[(Q5(1)-rt5)/2,(Q5(5)-rt5)/2]

for x,y,target in ((xmin,ymin,expected_min),(xmax,ymax,expected_max)):
    diff=[x[0]-y[0],x[1]-y[1]]
    summ=[x[0]+y[0],x[1]+y[1]]
    assert norm2(x)==1
    assert norm2(y)==1
    assert norm2(diff)==1
    assert norm2(summ)==target

print("VERIFY_OK triples=1000 nonempty_faces=60 segments=60 min=(9-sqrt5)/4 max=4-sqrt5")
