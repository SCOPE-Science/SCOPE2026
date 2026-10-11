from fractions import Fraction
import itertools

class Q5:
    __slots__ = ("a","b")
    def __init__(self,a=0,b=0):
        self.a = a if isinstance(a,Fraction) else Fraction(a)
        self.b = b if isinstance(b,Fraction) else Fraction(b)
    def __add__(self,o):
        o=toQ(o); return Q5(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return Q5(-self.a,-self.b)
    def __sub__(self,o): return self+(-toQ(o))
    def __rsub__(self,o): return toQ(o)-self
    def __mul__(self,o):
        o=toQ(o); return Q5(self.a*o.a+5*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def inv(self):
        d=self.a*self.a-5*self.b*self.b
        if d==0: raise ZeroDivisionError
        return Q5(self.a/d,-self.b/d)
    def __truediv__(self,o): return self*toQ(o).inv()
    def __rtruediv__(self,o): return toQ(o)/self
    def __eq__(self,o):
        o=toQ(o); return self.a==o.a and self.b==o.b
    def sign(self):
        a,b=self.a,self.b
        if b==0: return (a>0)-(a<0)
        if a==0: return (b>0)-(b<0)
        if a>0 and b>0: return 1
        if a<0 and b<0: return -1
        aa=a*a; bb=5*b*b
        if a>0 and b<0:
            return 1 if aa>bb else (-1 if aa<bb else 0)
        return 1 if bb>aa else (-1 if bb<aa else 0)
    def __lt__(self,o): return (self-toQ(o)).sign()<0
    def __le__(self,o): return (self-toQ(o)).sign()<=0
    def __gt__(self,o): return (self-toQ(o)).sign()>0
    def __ge__(self,o): return (self-toQ(o)).sign()>=0
    def __repr__(self): return f"Q5({self.a},{self.b})"

def toQ(x): return x if isinstance(x,Q5) else Q5(x)
Z=Q5(0); O=Q5(1); S=Q5(0,1)
R=(S-1)/2
PH=(S+1)/2
A=R/2
B=PH/2

class Aff:
    __slots__=("c","u","t","w")
    def __init__(self,c=0,u=0,t=0,w=0):
        self.c,self.u,self.t,self.w=map(toQ,(c,u,t,w))
    def __add__(self,o):
        o=toAff(o); return Aff(self.c+o.c,self.u+o.u,self.t+o.t,self.w+o.w)
    __radd__=__add__
    def __neg__(self): return Aff(-self.c,-self.u,-self.t,-self.w)
    def __sub__(self,o): return self+(-toAff(o))
    def __mul__(self,o):
        o=toQ(o); return Aff(self.c*o,self.u*o,self.t*o,self.w*o)
    __rmul__=__mul__
    def eval(self,p):
        uu,tt,ww=p
        return self.c+self.u*uu+self.t*tt+self.w*ww

def toAff(x): return x if isinstance(x,Aff) else Aff(x)
def fdot(f,v): return v[0]*f[0]+v[1]*f[1]
def minq(a,b): return a if a<=b else b

supports=[
    (O,O),(-O,-O),(R,O),(-R,-O),(Z,R),(Z,-R),
    (R,Z),(-R,Z),(O,R),(-O,-R)
]
verts=[
    (-O,Z),(Z,-O),(O,-PH),(PH,-PH),(PH,-O),
    (O,Z),(Z,O),(-O,PH),(-PH,PH),(-PH,O)
]
x=(Aff(-1,1,0,0),Aff(0,-1,0,0))

def solve3(rows,rhs):
    M=[list(row)+[toQ(b)] for row,b in zip(rows,rhs)]
    for col in range(3):
        pivot=next((i for i in range(col,3) if M[i][col]!=Z),None)
        if pivot is None: return None
        M[col],M[pivot]=M[pivot],M[col]
        inv=M[col][col].inv()
        M[col]=[q*inv for q in M[col]]
        for i in range(3):
            if i==col: continue
            f=M[i][col]
            if f!=Z:
                M[i]=[M[i][j]-f*M[col][j] for j in range(4)]
    return tuple(M[i][3] for i in range(3))

def feasible(P,lo,hi):
    u,t,w=P
    return Z<=u<=Q5(Fraction(1,2)) and lo<=t<=hi and Z<=w<=t

def facets(lo,hi):
    return [
        Aff(0,1,0,0),
        Aff(Fraction(-1,2),1,0,0),
        Aff(0,0,0,1),
        Aff(0,0,-1,1),
        Aff(-lo,0,1,0),
        Aff(-hi,0,1,0),
    ]

def domain_vertices(lo,hi):
    return [
        (u,t,w)
        for u in (Z,Q5(Fraction(1,2)))
        for t in (lo,hi)
        for w in (Z,t)
    ]

def pair_best(j,k,l,lo,hi,L):
    p=verts[j]; q=verts[(j+1)%10]
    d=(q[0]-p[0],q[1]-p[1])
    ty=(Aff(0,0,p[0],d[0]),Aff(0,0,p[1],d[1]))
    plus=(x[0]+ty[0],x[1]+ty[1])
    minus=(x[0]-ty[0],x[1]-ty[1])
    e1=fdot(supports[k],plus)-L
    e2=fdot(supports[l],minus)-L

    candidates=[]
    for P in domain_vertices(lo,hi):
        candidates.append(minq(e1.eval(P),e2.eval(P)))

    eq=e1-e2
    F=facets(lo,hi)
    for f1,f2 in itertools.combinations(F,2):
        rows=[
            (eq.u,eq.t,eq.w),
            (f1.u,f1.t,f1.w),
            (f2.u,f2.t,f2.w),
        ]
        rhs=[-eq.c,-f1.c,-f2.c]
        P=solve3(rows,rhs)
        if P is not None and feasible(P,lo,hi):
            candidates.append(e1.eval(P))

    best=candidates[0]
    for z in candidates[1:]:
        if z>best: best=z
    return best

branches=[
    (Z,R,Aff(1,0,A,0)),
    (R,O,Aff(B,0,R,0)),
]
table=[]
support_cases=0
for lo,hi,L in branches:
    row=[]
    for j in range(5):
        worst=None
        for k in range(10):
            for l in range(10):
                z=pair_best(j,k,l,lo,hi,L)
                support_cases+=1
                if worst is None or z>worst: worst=z
                assert z<=Z
        row.append(worst)
    table.append(row)

expected0=[Z,Z,Z,Z,Z]
expected1=[
    Q5(Fraction(-9,4),Fraction(3,4)),
    Q5(Fraction(-3,4),Fraction(1,4)),
    Z,
    Z,
    Q5(Fraction(-3,2),Fraction(1,2)),
]
assert table[0]==expected0
assert table[1]==expected1
assert support_cases==1000

def N(v):
    u,vv=v
    vals=[
        u+vv,-u-vv,
        R*u+vv,-R*u-vv,
        R*vv,-R*vv,
        R*u,-R*u,
        u+R*vv,-u-R*vv,
    ]
    m=vals[0]
    for z in vals[1:]:
        if z>m: m=z
    return m

# First sharp branch.
x1=(-O,Z)
y1=(Q5(Fraction(3,4),Fraction(1,4)),-PH)
assert N(x1)==O and N(y1)==O
# The exact endpoint identities plus affine support structure establish the branch.
for tt in (Z,R):
    target=O+A*tt
    assert N((x1[0]+tt*y1[0],x1[1]+tt*y1[1]))==target
    assert N((x1[0]-tt*y1[0],x1[1]-tt*y1[1]))==target

# Second sharp branch.
x2=(Q5(Fraction(-1,2)),Q5(Fraction(-1,2)))
y2=(PH,-PH)
assert N(x2)==O and N(y2)==O
for tt in (R,O):
    target=B+R*tt
    assert N((x2[0]+tt*y2[0],x2[1]+tt*y2[1]))==target
    assert N((x2[0]-tt*y2[0],x2[1]-tt*y2[1]))==target

# Weighted-profile algebra and midpoint.
D=Q5(Fraction(3,4),Fraction(-1,4))
assert B-R==D
assert O/(O+R)==R
mid=R+D/2
assert mid==Q5(Fraction(-1,8),Fraction(3,8))
assert 2*mid==Q5(Fraction(-1,4),Fraction(3,4))

print(
    "VERIFY_OK "
    f"support_cases={support_cases} "
    "field=Q(sqrt5) "
    "branches=2 edge_classes=5 "
    "midpoint_J=(-1+3sqrt5)/8"
)
