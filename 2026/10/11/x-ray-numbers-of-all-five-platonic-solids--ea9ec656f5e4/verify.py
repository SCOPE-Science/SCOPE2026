from fractions import Fraction as F

class Q5:
    __slots__=('a','b')
    def __init__(self,a=0,b=0): self.a=F(a); self.b=F(b)
    def __add__(self,o): o=q(o); return Q5(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return Q5(-self.a,-self.b)
    def __sub__(self,o): return self+(-q(o))
    def __rsub__(self,o): return q(o)-self
    def __mul__(self,o):
        o=q(o); return Q5(self.a*o.a+5*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def __eq__(self,o): o=q(o); return self.a==o.a and self.b==o.b
    def sign(self):
        a,b=self.a,self.b
        if b==0: return (a>0)-(a<0)
        if a==0: return (b>0)-(b<0)
        if a>0 and b>0: return 1
        if a<0 and b<0: return -1
        aa=a*a; bb=5*b*b
        if aa==bb: return 0
        if a>0 and b<0: return 1 if aa>bb else -1
        if a<0 and b>0: return -1 if aa>bb else 1
        raise AssertionError
    def __lt__(self,o): return (self-q(o)).sign()<0
    def __le__(self,o): return (self-q(o)).sign()<=0
    def __gt__(self,o): return (self-q(o)).sign()>0
    def __ge__(self,o): return (self-q(o)).sign()>=0
    def __hash__(self): return hash((self.a,self.b))
    def __repr__(self): return f'Q5({self.a},{self.b})'
def q(x): return x if isinstance(x,Q5) else Q5(x)
SQ5=Q5(0,1); PHI=Q5(F(1,2),F(1,2)); INV=Q5(F(-1,2),F(1,2))

def dot(a,b):
    s=Q5()
    for x,y in zip(a,b): s += q(x)*q(y)
    return s

def max_exact(vals):
    m=vals[0]
    for v in vals[1:]:
        if m<v: m=v
    return m

def signs(vals): return [q(v).sign() for v in vals]
def same_strict(vals):
    s=signs(vals); return all(x>0 for x in s) or all(x<0 for x in s)

def uniq(seq):
    out=[]
    for v in seq:
        t=tuple(q(x) for x in v)
        if t not in out: out.append(t)
    return out

# Tetrahedron.
T=[(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]
for i in range(4):
    for j in range(4):
        assert dot(T[i],T[j]) == (3 if i==j else -1)
for i in range(4):
    inc=[tuple(-q(x) for x in T[j]) for j in range(4) if j!=i]
    assert same_strict([dot(n,T[i]) for n in inc])
# Pairwise antipodality witness vi-vj.
for i in range(4):
    for j in range(i+1,4):
        d=tuple(q(T[i][k])-q(T[j][k]) for k in range(3))
        vals=[dot(d,v) for v in T]
        assert vals[i] == 4 and vals[j] == -4
        assert all(vals[i]>=x for x in vals) and all(vals[j]<=x for x in vals)

# Cube.
C=[(sx,sy,sz) for sx in (-1,1) for sy in (-1,1) for sz in (-1,1)]
body_diags=[(1,1,1),(1,1,-1),(1,-1,1),(-1,1,1)]
covered=set()
for d in body_diags:
    for i,v in enumerate(C):
        inc=[(v[0],0,0),(0,v[1],0),(0,0,v[2])]
        if same_strict([dot(n,d) for n in inc]): covered.add(i)
assert len(covered)==8
# Exhaustive sign-cell fact: a line direction with all nonzero coordinate signs covers one antipodal pair.
for s in C:
    d=s
    cv=[]
    for i,v in enumerate(C):
        inc=[(v[0],0,0),(0,v[1],0),(0,0,v[2])]
        if same_strict([dot(n,d) for n in inc]): cv.append(i)
    assert len(cv)==2 and tuple(-x for x in C[cv[0]])==C[cv[1]]

# Octahedron.
O=[]
for i in range(3):
    for s in (-1,1):
        v=[0,0,0]; v[i]=s; O.append(tuple(v))
ON=[(sx,sy,sz) for sx in (-1,1) for sy in (-1,1) for sz in (-1,1)]
for v in O:
    inc=[n for n in ON if dot(n,v)==1]
    assert len(inc)==4
    axis=tuple(abs(v[k]) for k in range(3))
    assert same_strict([dot(n,axis) for n in inc])

# Dodecahedron vertices and facet normals.
D=[]
for sx in (-1,1):
  for sy in (-1,1):
    for sz in (-1,1): D.append((sx,sy,sz))
for sy in (-1,1):
  for sz in (-1,1): D.append((0,sy*INV,sz*PHI))
for sx in (-1,1):
  for sy in (-1,1): D.append((sx*INV,sy*PHI,0))
for sx in (-1,1):
  for sz in (-1,1): D.append((sx*PHI,0,sz*INV))
D=uniq(D); assert len(D)==20
ND=[]
for sy in (-1,1):
  for sz in (-1,1): ND.append((0,sy*PHI,sz))
for sx in (-1,1):
  for sy in (-1,1): ND.append((sx*PHI,sy,0))
for sx in (-1,1):
  for sz in (-1,1): ND.append((sx,0,sz*PHI))
ND=uniq(ND); assert len(ND)==12
SUP=PHI*PHI
facetsD=[]
for n in ND:
    vals=[dot(v,n) for v in D]; m=max_exact(vals)
    assert m==SUP
    face=[i for i,x in enumerate(vals) if x==m]
    assert len(face)==5
    facetsD.append(face)
incD=[]
for i,v in enumerate(D):
    inc=[j for j,Fc in enumerate(facetsD) if i in Fc]
    assert len(inc)==3
    incD.append(inc)
# Edges share exactly two facets; count and common squared length.
edgesD=[]
for i in range(20):
  for j in range(i+1,20):
    if len(set(incD[i])&set(incD[j]))==2: edgesD.append((i,j))
assert len(edgesD)==30
ed2={dot(tuple(D[i][k]-D[j][k] for k in range(3)), tuple(D[i][k]-D[j][k] for k in range(3))) for i,j in edgesD}
assert len(ed2)==1
DL=[(1,1,0),(1,-1,0),(0,0,1)]
for i,v in enumerate(D):
    assert any(same_strict([dot(ND[j],d) for j in incD[i]]) for d in DL)

# Icosahedron vertices and triangular facet normals.
I=[]
for sy in (-1,1):
  for sz in (-1,1): I.append((0,sy,sz*PHI))
for sx in (-1,1):
  for sy in (-1,1): I.append((sx,sy*PHI,0))
for sx in (-1,1):
  for sz in (-1,1): I.append((sx*PHI,0,sz))
I=uniq(I); assert len(I)==12
NI=[]
for sx in (-1,1):
  for sy in (-1,1):
    for sz in (-1,1): NI.append((sx,sy,sz))
for sy in (-1,1):
  for sz in (-1,1): NI.append((0,sy*PHI,sz*INV))
for sx in (-1,1):
  for sz in (-1,1): NI.append((sx*INV,0,sz*PHI))
for sx in (-1,1):
  for sy in (-1,1): NI.append((sx*PHI,sy*INV,0))
NI=uniq(NI); assert len(NI)==20
SUPI=PHI*PHI
facetsI=[]
for n in NI:
    vals=[dot(v,n) for v in I]; m=max_exact(vals)
    assert m==SUPI
    face=[i for i,x in enumerate(vals) if x==m]
    assert len(face)==3
    facetsI.append(face)
incI=[]
for i,v in enumerate(I):
    inc=[j for j,Fc in enumerate(facetsI) if i in Fc]
    assert len(inc)==5
    incI.append(inc)
edgesI=[]
for i in range(12):
  for j in range(i+1,12):
    if len(set(incI[i])&set(incI[j]))==2: edgesI.append((i,j))
assert len(edgesI)==30
ed2i={dot(tuple(I[i][k]-I[j][k] for k in range(3)), tuple(I[i][k]-I[j][k] for k in range(3))) for i,j in edgesI}
assert len(ed2i)==1
IL=[(1,0,0),(0,1,0),(0,0,1)]
for i,v in enumerate(I):
    assert any(same_strict([dot(NI[j],d) for j in incI[i]]) for d in IL)

print('VERIFY_OK')
print('tetrahedron: upper=4, weak-neighbourly antipodal lower certificate=4')
print('cube: four body diagonals cover; every sign cell covers exactly one antipodal vertex pair')
print('octahedron: three coordinate axes cover all six vertices')
print('dodecahedron: V=20 F=12 E=30, three exact line directions cover all vertices')
print('icosahedron: V=12 F=20 E=30, three coordinate axes cover all vertices')
print('dodeca_edge_sq=', next(iter(ed2)))
print('icosa_edge_sq=', next(iter(ed2i)))
