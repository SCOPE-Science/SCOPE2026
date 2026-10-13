from fractions import Fraction as F
from collections import deque, Counter
from math import lcm

# Exact arithmetic in K = Q[z]/(1+z+...+z^6), with z a primitive seventh root.
class K:
    __slots__=('c',)
    def __init__(self,c=0):
        if isinstance(c,K): self.c=c.c; return
        if isinstance(c,(int,F)): self.c=(F(c),)+(F(0),)*5; return
        a=[F(x) for x in c]+[F(0)]*6; self.c=tuple(a[:6])
    def __add__(self,o):
        o=K(o); return K([a+b for a,b in zip(self.c,o.c)])
    __radd__=__add__
    def __neg__(self): return K([-a for a in self.c])
    def __sub__(self,o): return self+(-K(o))
    def __rsub__(self,o): return K(o)-self
    def __mul__(self,o):
        o=K(o); tmp=[F(0)]*11
        for i,a in enumerate(self.c):
            for j,b in enumerate(o.c): tmp[i+j]+=a*b
        for d in range(10,5,-1):
            a=tmp[d]
            if a:
                tmp[d]=0
                for k in range(6): tmp[d-6+k]-=a
        return K(tmp[:6])
    __rmul__=__mul__
    def __eq__(self,o): return self.c==K(o).c
    def __bool__(self): return any(self.c)
    def __pow__(self,n):
        if n<0: return self.inv()**(-n)
        r=K(1); a=self
        while n:
            if n&1: r=r*a
            a=a*a; n//=2
        return r
    def inv(self):
        A=[[F(0)]*7 for _ in range(6)]
        for j in range(6):
            v=self*(z**j)
            for i in range(6): A[i][j]=v.c[i]
        for i in range(6): A[i][6]=F(i==0)
        row=0
        for col in range(6):
            piv=next(i for i in range(row,6) if A[i][col])
            A[row],A[piv]=A[piv],A[row]
            q=A[row][col]; A[row]=[x/q for x in A[row]]
            for i in range(6):
                if i!=row and A[i][col]:
                    q=A[i][col]; A[i]=[A[i][j]-q*A[row][j] for j in range(7)]
            row+=1
        return K([A[i][6] for i in range(6)])
    def __truediv__(self,o): return self*K(o).inv()
    def __rtruediv__(self,o): return K(o)*self.inv()

z=K([0,1,0,0,0,0])
assert sum((z**i for i in range(7)),K(0))==K(0)

def mm(A,B): return [[sum((A[i][k]*B[k][j] for k in range(3)),K(0)) for j in range(3)] for i in range(3)]
def det(A):
    return A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])-A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])+A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0])
def inv(A):
    d=det(A); assert d
    C=[[K(0)]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            rs=[r for r in range(3) if r!=i]; cs=[c for c in range(3) if c!=j]
            C[i][j]=K((-1)**(i+j))*(A[rs[0]][cs[0]]*A[rs[1]][cs[1]]-A[rs[0]][cs[1]]*A[rs[1]][cs[0]])
    return [[C[j][i]/d for j in range(3)] for i in range(3)]
def normM(A):
    for row in A:
        for x in row:
            if x:
                y=x.inv(); return tuple(tuple((v*y).c for v in r) for r in A)
    raise ValueError
def unnorm(key): return [[K(key[i][j]) for j in range(3)] for i in range(3)]
def normv(v):
    for x in v:
        if x:
            y=x.inv(); return tuple((a*y).c for a in v)
    raise ValueError

# Sparse homogeneous polynomial arithmetic in T,X,Z.
def padd(p,q):
    r=dict(p)
    for m,c in q.items():
        r[m]=r.get(m,K(0))+c
        if not r[m]: del r[m]
    return r
def pmul(p,q):
    r={}
    for a,ca in p.items():
        for b,cb in q.items():
            m=(a[0]+b[0],a[1]+b[1],a[2]+b[2])
            r[m]=r.get(m,K(0))+ca*cb
            if not r[m]: del r[m]
    return r
def ppow(p,n):
    r={(0,0,0):K(1)}
    for _ in range(n): r=pmul(r,p)
    return r
def pscale(p,c): return {m:c*v for m,v in p.items() if c*v}
def lin(row): return {(1,0,0):row[0],(0,1,0):row[1],(0,0,1):row[2]}
def quartic_sub(A):
    T,X,Z=map(lin,A)
    return padd(padd(pmul(ppow(T,3),X),pmul(ppow(X,3),Z)),pmul(ppow(Z,3),T))
Q={(3,1,0):K(1),(0,3,1):K(1),(1,0,3):K(1)}

def proportional(p,q):
    mons=set(p)|set(q)
    first=next((m for m in mons if q.get(m,K(0))),None)
    assert first is not None
    lam=p.get(first,K(0))/q[first]
    return all(p.get(m,K(0))==lam*q.get(m,K(0)) for m in mons),lam

# Three standard projective automorphisms of the Klein quartic.
S=[[z,K(0),K(0)],[K(0),z**4,K(0)],[K(0),K(0),z**2]]
T=[[K(0),K(0),K(1)],[K(1),K(0),K(0)],[K(0),K(1),K(0)]]
a=z-z**6; b=z**2-z**5; c=z**4-z**3
U=[[a,b,c],[b,c,a],[c,a,b]]
for G in [S,T,U]:
    ok,_=proportional(quartic_sub(G),Q)
    assert ok

I=[[K(1),K(0),K(0)],[K(0),K(1),K(0)],[K(0),K(0),K(1)]]
gens=[S,T,U]
seen={normM(I)}; dq=deque([I])
while dq:
    A=dq.popleft()
    for G in gens:
        B=mm(A,G); key=normM(B)
        if key not in seen:
            seen.add(key); dq.append(unnorm(key))
assert len(seen)==168

# The 28 bitangent equations used by Bannai--Tokunaga--Yamamoto.
e1=z+z**-1; e2=z**2+z**-2; e3=z**4+z**-4
def line(k,j):
    if k==0:
        A=-(z**j); B=-(z**(3*j))
    elif k==1:
        A=-(z**j)*(e1**2); B=-(z**(3*j))*(e3**-2)
    elif k==2:
        A=-(z**j)*(e2**2); B=-(z**(3*j))*(e1**-2)
    else:
        A=-(z**j)*(e3**2); B=-(z**(3*j))*(e2**-2)
    return [-A,K(1),-B]
labels=[]; lines=[]
for k in range(4):
    for j in range(7): labels.append((k,j)); lines.append(line(k,j))
line_map={normv(v):i for i,v in enumerate(lines)}
assert len(line_map)==28

# Exact induced action on all 28 bitangents.
perms=[]
for key in seen:
    A=unnorm(key); Ai=inv(A); p=[]
    for ell in lines:
        image=[sum((ell[k]*Ai[k][j] for k in range(3)),K(0)) for j in range(3)]
        assert normv(image) in line_map
        p.append(line_map[normv(image)])
    perms.append(tuple(p))
assert len(set(perms))==168

# L1=L_{0,0}, L2=L_{1,0}, L3=L_{1,1}, L4=L_{3,3}, L5=L_{1,6}, L6=L_{3,4}, L7=L_{2,5}.
src=[(0,0),(1,0),(1,1),(3,3),(1,6),(3,4),(2,5)]
idx={lab:i for i,lab in enumerate(labels)}; selected=[idx[x] for x in src]
Isets=[{selected[i-1] for i in [1,2,3,5]},
       {selected[i-1] for i in [1,2,3,6]},
       {selected[i-1] for i in [1,2,4,7]}]

def perm_order(p):
    used=[False]*len(p); o=1
    for i in range(len(p)):
        if not used[i]:
            j=i; n=0
            while not used[j]: used[j]=True; n+=1; j=p[j]
            o=lcm(o,n)
    return o

stabs=[]
for Sset in Isets:
    stab=[p for p in perms if {p[i] for i in Sset}==Sset]
    stabs.append(stab)
assert [len(s) for s in stabs]==[6,1,1]
assert Counter(perm_order(p) for p in stabs[0])==Counter({1:1,2:3,3:2})
# For the first arrangement the six elements fix L2 and permute L1,L3,L5 as all six permutations.
L1,L2,L3,L4,L5,L6,L7=selected
assert all(p[L2]==L2 for p in stabs[0])
trip=(L1,L3,L5); observed={tuple(trip.index(p[x]) for x in trip) for p in stabs[0]}
assert len(observed)==6
# Orbit-stabilizer in the 168-element group.
assert [168//len(s) for s in stabs]==[28,168,168]

print('GROUP_SIZE=168')
print('STABILIZER_SIZES=6,1,1')
print('FIRST_STABILIZER_ORDER_PROFILE=1:1,2:3,3:2')
print('ORBIT_SIZES=28,168,168')
print('VERIFY_OK')
