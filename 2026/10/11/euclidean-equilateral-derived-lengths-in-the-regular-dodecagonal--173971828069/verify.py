from fractions import Fraction as F

class Q3:
    __slots__=('a','b')
    def __init__(self,a=0,b=0): self.a=F(a); self.b=F(b)
    def __add__(self,o): o=q(o); return Q3(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return Q3(-self.a,-self.b)
    def __sub__(self,o): return self+(-q(o))
    def __rsub__(self,o): return q(o)-self
    def __mul__(self,o): o=q(o); return Q3(self.a*o.a+3*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def __truediv__(self,o):
        o=q(o); d=o.a*o.a-3*o.b*o.b
        if d==0: raise ZeroDivisionError
        return Q3((self.a*o.a-3*self.b*o.b)/d,(self.b*o.a-self.a*o.b)/d)
    def __eq__(self,o): o=q(o); return self.a==o.a and self.b==o.b
    def __hash__(self): return hash((self.a,self.b))
    def sign(self):
        a,b=self.a,self.b
        if a==0: return (b>0)-(b<0)
        if b==0: return (a>0)-(a<0)
        if a>0 and b>0: return 1
        if a<0 and b<0: return -1
        if a>0 and b<0: return 1 if a*a>3*b*b else -1
        return 1 if 3*b*b>a*a else -1
    def __le__(self,o): return (self-q(o)).sign()<=0
    def __lt__(self,o): return (self-q(o)).sign()<0
    def __repr__(self): return f'Q3({self.a},{self.b})'
def q(x): return x if isinstance(x,Q3) else Q3(x)
Z=Q3(); O=Q3(1); R=Q3(0,1); H=F(1,2)
funcs=[(O,Z),(R*H,Q3(H)),(Q3(H),R*H),(Z,O),(Q3(-H),R*H),(-R*H,Q3(H))]
sfuncs=[]
for f in funcs:sfuncs += [f,(-f[0],-f[1])]
rows=[]
for kind in range(3):
  for a,b in sfuncs:
    rows.append((a,b,Z,Z) if kind==0 else ((Z,Z,a,b) if kind==1 else (a,b,-a,-b)))

def dot(a,b):
  s=Z
  for x,y in zip(a,b): s=s+x*y
  return s

def rref_line(idxs):
  A=[[rows[i][j] for j in range(4)]+[O] for i in idxs]
  piv=[]; r=0
  for c in range(4):
    k=next((k for k in range(r,3) if A[k][c]!=Z),None)
    if k is None: continue
    A[r],A[k]=A[k],A[r]
    d=A[r][c]; A[r]=[x/d for x in A[r]]
    for k2 in range(3):
      if k2==r: continue
      z=A[k2][c]
      if z!=Z: A[k2]=[A[k2][j]-z*A[r][j] for j in range(5)]
    piv.append(c);r+=1
    if r==3: break
  for row in A:
    if all(row[c]==Z for c in range(4)) and row[4]!=Z: return None
  if r!=3: raise AssertionError(('unexpected consistent rank',r,idxs))
  free=next(c for c in range(4) if c not in piv)
  p=[Z,Z,Z,Z]; d=[Z,Z,Z,Z]; d[free]=O
  for rr,c in enumerate(piv):
    p[c]=A[rr][4]
    d[c]=-A[rr][free]
  return tuple(p),tuple(d)

def interval(p,d):
  lo=None; hi=None
  for row in rows:
    c=dot(row,p); e=dot(row,d); rhs=O-c
    if e==Z:
      if not c<=O: return None
    else:
      t=rhs/e
      if e.sign()>0:
        if hi is None or t<hi: hi=t
      else:
        if lo is None or lo<t: lo=t
  if lo is None or hi is None: raise AssertionError('P should be bounded')
  if hi<lo:return None
  return lo,hi

def point(p,d,t): return tuple(p[i]+d[i]*t for i in range(4))
def ef(f,z):return f[0]*z[0]+f[1]*z[1]
def norm(z):
  vals=[ef(f,z) for f in sfuncs]; m=vals[0]
  for a in vals[1:]:
    if m<a:m=a
  return m
def out(v):
  x=(v[0],v[1]);y=(v[2],v[3])
  return (x,y,(x[0]-y[0],x[1]-y[1]),(x[0]+y[0],x[1]+y[1]),(2*x[0]-y[0],2*x[1]-y[1]))

nonempty=points=segments=0
endpoint_set=set()
for ix in range(12):
  for iy in range(12,24):
    for iz in range(24,36):
      ld=rref_line((ix,iy,iz))
      if ld is None: continue
      p,d=ld; I=interval(p,d)
      if I is None: continue
      nonempty+=1;lo,hi=I
      a=point(p,d,lo); b=point(p,d,hi)
      endpoint_set.add(a);endpoint_set.add(b)
      for v in {a,b}:
        x,y,z,u,w=out(v)
        assert norm(x)==norm(y)==norm(z)==O
        assert norm(u)==R and norm(w)==R
      if lo==hi:
        points+=1
      else:
        segments+=1
        _,_,_,ua,wa=out(a);_,_,_,ub,wb=out(b)
        cu={j for j,f in enumerate(sfuncs) if ef(f,ua)==R and ef(f,ub)==R}
        cw={j for j,f in enumerate(sfuncs) if ef(f,wa)==R and ef(f,wb)==R}
        assert cu and cw
assert nonempty==168,(nonempty,points,segments)
assert points==144 and segments==24,(points,segments)
assert len(endpoint_set)==24,len(endpoint_set)
# explicit pair
x=(R-O,R-O);y=(O,R-Q3(2));v=(x[0],x[1],y[0],y[1])
x,y,z,u,w=out(v)
assert norm(x)==norm(y)==norm(z)==O
assert norm(u)==norm(w)==R
print('VERIFY_OK nonempty_triples=168 point_triples=144 segment_triples=24 unique_equilateral_vertices=24 GL=6')
