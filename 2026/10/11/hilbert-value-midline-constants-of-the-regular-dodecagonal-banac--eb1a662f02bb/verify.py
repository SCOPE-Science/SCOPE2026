from fractions import Fraction
import itertools

class Q3:
    __slots__=("a","b")
    def __init__(self,a=0,b=0):
        if isinstance(a,Q3) and b==0:
            self.a,self.b=a.a,a.b
        else:
            self.a=Fraction(a); self.b=Fraction(b)
    def __add__(self,o):
        o=q(o); return Q3(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return Q3(-self.a,-self.b)
    def __sub__(self,o): return self+(-q(o))
    def __rsub__(self,o): return q(o)-self
    def __mul__(self,o):
        o=q(o); return Q3(self.a*o.a+3*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def inv(self):
        d=self.a*self.a-3*self.b*self.b
        assert d
        return Q3(self.a/d,-self.b/d)
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
        c=a*a-3*b*b
        if a>0 and b<0:return 1 if c>0 else -1
        if a<0 and b>0:return -1 if c>0 else 1
        raise AssertionError
    def __lt__(self,o): return (self-q(o)).sign()<0
    def __le__(self,o): return (self-q(o)).sign()<=0
    def __gt__(self,o): return (self-q(o)).sign()>0
    def __ge__(self,o): return (self-q(o)).sign()>=0
    def __repr__(self): return f"Q3({self.a},{self.b})"

def q(x): return x if isinstance(x,Q3) else Q3(x)

rt3=Q3(0,1)
half=Fraction(1,2)
facets=[
    (Q3(1),Q3(0)),
    (Q3(0,Fraction(1,2)),Q3(Fraction(1,2))),
    (Q3(Fraction(1,2)),Q3(0,Fraction(1,2))),
    (Q3(0),Q3(1)),
    (Q3(-Fraction(1,2)),Q3(0,Fraction(1,2))),
    (Q3(0,-Fraction(1,2)),Q3(Fraction(1,2))),
]
facets += [(-a,-b) for a,b in facets]

def row_for(f,block):
    a,b=f
    if block==0:return [a,b,Q3(),Q3()]
    if block==1:return [Q3(),Q3(),a,b]
    return [a,b,-a,-b]

constraints=[]
for block in range(3):
    constraints += [row_for(f,block) for f in facets]

def dot4(row,z):
    return sum((row[i]*z[i] for i in range(4)),Q3())

def solve_line(rows):
    M=[list(rw)+[Q3(1)] for rw in rows]
    piv=[]
    prow=0
    for col in range(4):
        pr=next((i for i in range(prow,3) if M[i][col]!=0),None)
        if pr is None: continue
        M[prow],M[pr]=M[pr],M[prow]
        inv=M[prow][col].inv()
        M[prow]=[u*inv for u in M[prow]]
        for i in range(3):
            if i!=prow and M[i][col]!=0:
                c=M[i][col]
                M[i]=[M[i][j]-c*M[prow][j] for j in range(5)]
        piv.append(col)
        prow+=1
        if prow==3:break
    for rw in M:
        if all(rw[j]==0 for j in range(4)) and rw[4]!=0:
            return "inconsistent",None,None
    if len(piv)<3:return "lowrank",None,None
    free=next(j for j in range(4) if j not in piv)
    z0=[Q3() for _ in range(4)]
    d=[Q3() for _ in range(4)]
    d[free]=Q3(1)
    for i,pc in enumerate(piv):
        z0[pc]=M[i][4]
        d[pc]=-M[i][free]
    return "line",z0,d

def interval(z0,d):
    lo=None; hi=None
    for rw in constraints:
        coef=dot4(rw,d)
        rhs=Q3(1)-dot4(rw,z0)
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

def point(z0,d,t):
    return [z0[i]+d[i]*t for i in range(4)]

def evalf(f,v):
    return f[0]*v[0]+f[1]*v[1]

def norm(v):
    return max(evalf(f,v) for f in facets)

def objectives(z):
    x=(z[0],z[1]); y=(z[2],z[3])
    A=norm((x[0]+y[0],x[1]+y[1]))
    B=norm((Q3(2)*x[0]-y[0],Q3(2)*x[1]-y[1]))
    return (A+B)/2,(A*A+B*B)/2,A,B

max1=None
max2=None
arg1=None
arg2=None
nonempty=0
segments=0
lowrank=0

for i,j,k in itertools.product(range(12),repeat=3):
    status,z0,d=solve_line([constraints[i],constraints[12+j],constraints[24+k]])
    if status=="inconsistent":
        continue
    if status=="lowrank":
        lowrank+=1
        continue
    iv=interval(z0,d)
    if iv is None:
        continue
    lo,hi=iv
    nonempty+=1
    ts=[lo] if lo==hi else [lo,hi]
    if lo<hi:segments+=1
    for t in ts:
        z=point(z0,d,t)
        o1,o2,A,B=objectives(z)
        if max1 is None or max1<o1:
            max1=o1; arg1=(z,A,B)
        if max2 is None or max2<o2:
            max2=o2; arg2=(z,A,B)

assert lowrank==0
assert nonempty==168,nonempty
assert segments==24,segments
assert max1==rt3,max1
assert max2==Q3(3),max2

x=(Q3(1),rt3-2)
y=(rt3-1,rt3-1)
assert norm(x)==Q3(1)
assert norm(y)==Q3(1)
assert norm((x[0]-y[0],x[1]-y[1]))==Q3(1)
assert norm((x[0]+y[0],x[1]+y[1]))==rt3
assert norm((Q3(2)*x[0]-y[0],Q3(2)*x[1]-y[1]))==rt3

print("VERIFY_OK triples=1728 nonempty_faces=168 segments=24 M1=sqrt3 M2=3 M3=3^(1/4)")
