from itertools import product

# Reduction modulo 2 of Markushevich--Moreau's three H-generators on the
# two factors of O/2O = F_2 x F_2, in the source's O-basis e1,e2,e3.
A0 = [
 ((1,1,0),(0,1,0),(0,0,1)),
 ((1,0,0),(0,1,1),(0,0,1)),
 ((1,0,0),(0,1,0),(1,0,1)),
]
A1 = [
 ((1,0,1),(0,1,0),(0,0,1)),
 ((1,0,0),(1,1,0),(0,0,1)),
 ((1,0,0),(0,1,0),(0,1,1)),
]
P = ((0,0,1),(1,0,0),(0,1,0))

I3=((1,0,0),(0,1,0),(0,0,1))

def mm(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(len(B)))&1 for j in range(len(B[0]))) for i in range(len(A)))

def mt(A): return tuple(zip(*A))
def mv(A,v): return tuple(sum(A[i][j]*v[j] for j in range(len(v)))&1 for i in range(len(A)))
def add(u,v): return tuple(a^b for a,b in zip(u,v))
def rank(A):
    a=[list(r) for r in A]; m=len(a); n=len(a[0]); r=0
    for c in range(n):
        p=next((i for i in range(r,m) if a[i][c]),None)
        if p is None: continue
        a[r],a[p]=a[p],a[r]
        for i in range(m):
            if i!=r and a[i][c]: a[i]=[x^y for x,y in zip(a[i],a[r])]
        r+=1
    return r

def tupmat(bits,n=3): return tuple(tuple(bits[n*i+j] for j in range(n)) for i in range(n))

def group_pair():
    ident=(I3,I3)
    S={ident}; front=[ident]
    gens=list(zip(A0,A1))
    while front:
        g=front.pop()
        for h in gens:
            z=(mm(g[0],h[0]),mm(g[1],h[1]))
            if z not in S: S.add(z); front.append(z)
    return S
G=group_pair()
assert len(G)==168

# Unique perfect intertwining pairing A0^T P A1=P.
inter=[]
for bits in product((0,1),repeat=9):
    Q=tupmat(bits)
    if all(mm(mm(mt(X),Q),Y)==Q for X,Y in zip(A0,A1)):
        inter.append(Q)
assert len(inter)==2 and P in inter
assert P in inter and rank(P)==3
assert sum(rank(Q)==3 for Q in inter)==1

# 6x6 action and cross symplectic form.
def blockdiag(X,Y):
    Z=[]
    for i in range(3): Z.append(tuple(X[i])+ (0,0,0))
    for i in range(3): Z.append((0,0,0)+tuple(Y[i]))
    return tuple(Z)
G6=[blockdiag(X,Y) for X,Y in zip(A0,A1)]
B=tuple(tuple((P[i][j-3] if i<3 and j>=3 else P[j][i-3] if i>=3 and j<3 else 0) for j in range(6)) for i in range(6))
assert rank(B)==6 and all(mm(mm(mt(g),B),g)==B for g in G6)

# Dimension of invariant alternating forms by solving homogeneous equations over F2.
pairs=[(i,j) for i in range(6) for j in range(i+1,6)]
def alt_from_bits(bits):
    M=[[0]*6 for _ in range(6)]
    for b,(i,j) in zip(bits,pairs): M[i][j]=M[j][i]=b
    return tuple(tuple(r) for r in M)
inv_alt=[]
for bits in product((0,1),repeat=15):
    M=alt_from_bits(bits)
    if all(mm(mm(mt(g),M),g)==M for g in G6): inv_alt.append(M)
assert len(inv_alt)==2 and B in inv_alt  # dimension one

vec3=list(product((0,1),repeat=3)); vec6=list(product((0,1),repeat=6))
def dotP(x,y):
    return sum(x[i]*P[i][j]*y[j] for i in range(3) for j in range(3))&1
def q(z): return dotP(z[:3],z[3:])
# q polarization is B.
for z in vec6:
    for w in vec6:
        lhs=q(add(z,w))^q(z)^q(w)
        rhs=sum(z[i]*B[i][j]*w[j] for i in range(6) for j in range(6))&1
        assert lhs==rhs
assert sum(q(z)==0 for z in vec6)==36 and sum(q(z)==1 for z in vec6)==28
# q invariant under generators.
assert all(q(mv(g,z))==q(z) for g in G6 for z in vec6)

# No nonzero invariant linear functional, hence unique invariant quadratic refinement of B.
# A difference of two refinements is linear.
def fixed_covectors():
    ans=[]
    for ell in vec6:
        ok=True
        for g in G6:
            for z in vec6:
                if (sum(ell[i]*mv(g,z)[i] for i in range(6))&1)!=(sum(ell[i]*z[i] for i in range(6))&1):
                    ok=False; break
            if not ok: break
        if ok: ans.append(ell)
    return ans
assert fixed_covectors()==[(0,0,0,0,0,0)]

def label(z):
    x=z[:3]; y=z[3:]
    zx=not any(x); zy=not any(y)
    if zx and zy: return '0'
    if not zx and zy: return 'A'
    if zx and not zy: return 'B'
    return 'C' if q(z)==0 else 'D'

# Enumerate full H-orbits.
def act_pair(g,z): return mv(g[0],z[:3])+mv(g[1],z[3:])
orbits=[]; unseen=set(vec6)
while unseen:
    z=next(iter(unseen)); O={act_pair(g,z) for g in G}; orbits.append(O); unseen-=O
prof=sorted((len(O),label(next(iter(O)))) for O in orbits)
assert prof==[(1,'0'),(7,'A'),(7,'B'),(21,'C'),(28,'D')]

classes={L:[z for z in vec6 if label(z)==L] for L in ['0','A','B','C','D']}
expected={
('A','A'):{'0':1,'A':6},
('A','B'):{'C':3,'D':4},
('A','C'):{'B':3,'C':6,'D':12},
('A','D'):{'B':4,'C':12,'D':12},
('B','A'):{'C':3,'D':4},
('B','B'):{'0':1,'B':6},
('B','C'):{'A':3,'C':6,'D':12},
('B','D'):{'A':4,'C':12,'D':12},
('C','A'):{'B':1,'C':2,'D':4},
('C','B'):{'A':1,'C':2,'D':4},
('C','C'):{'0':1,'A':2,'B':2,'C':8,'D':8},
('C','D'):{'A':4,'B':4,'C':8,'D':12},
('D','A'):{'B':1,'C':3,'D':3},
('D','B'):{'A':1,'C':3,'D':3},
('D','C'):{'A':3,'B':3,'C':6,'D':9},
('D','D'):{'0':1,'A':3,'B':3,'C':9,'D':12},
}
for X in 'ABCD':
  x=classes[X][0]
  for Y in 'ABCD':
    got={}
    for y in classes[Y]:
        L=label(add(x,y)); got[L]=got.get(L,0)+1
    assert got==expected[(X,Y)], (X,Y,got)

print('VERIFY_OK group=168 module=V+Vdual pairing_space_dim=1 invariant_alt_dim=1 q_zero=36 q_one=28 orbits=1+7+7+21+28 fusion=verified')
