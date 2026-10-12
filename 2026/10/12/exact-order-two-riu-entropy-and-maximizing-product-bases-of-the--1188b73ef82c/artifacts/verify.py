from fractions import Fraction as F
from itertools import product, combinations

# Exact field Q(i,sqrt(3)): a + b*r + i(c + d*r), r^2=3.
class K:
    __slots__=('a','b','c','d')
    def __init__(self,a=0,b=0,c=0,d=0): self.a,self.b,self.c,self.d=map(F,(a,b,c,d))
    def __add__(self,o):
        o=toK(o); return K(self.a+o.a,self.b+o.b,self.c+o.c,self.d+o.d)
    __radd__=__add__
    def __neg__(self): return K(-self.a,-self.b,-self.c,-self.d)
    def __sub__(self,o): return self+(-toK(o))
    def __rsub__(self,o): return toK(o)-self
    def __mul__(self,o):
        o=toK(o)
        # (x+iy)(u+iv), each x,y in Q(r)
        xr=(self.a*o.a+3*self.b*o.b, self.a*o.b+self.b*o.a)
        yi=(self.c*o.c+3*self.d*o.d, self.c*o.d+self.d*o.c)
        xv=(self.a*o.c+3*self.b*o.d, self.a*o.d+self.b*o.c)
        yu=(self.c*o.a+3*self.d*o.b, self.c*o.b+self.d*o.a)
        return K(xr[0]-yi[0],xr[1]-yi[1],xv[0]+yu[0],xv[1]+yu[1])
    __rmul__=__mul__
    def __truediv__(self,o):
        if isinstance(o,(int,F)): return K(self.a/F(o),self.b/F(o),self.c/F(o),self.d/F(o))
        raise TypeError
    def conj(self): return K(self.a,self.b,-self.c,-self.d)
    def __eq__(self,o):
        o=toK(o); return (self.a,self.b,self.c,self.d)==(o.a,o.b,o.c,o.d)
    def __repr__(self): return f'K{self.a,self.b,self.c,self.d}'
def toK(x): return x if isinstance(x,K) else K(x)

one=K(1); ii=K(0,0,1,0); rt3=K(0,1,0,0)
omega=K(F(-1,2),0,0,F(1,2))
omega2=K(F(-1,2),0,0,F(-1,2))
amps={0b0011:one,0b1100:one,0b0101:omega,0b1010:omega,0b0110:omega2,0b1001:omega2}
assert sum((v.conj()*v for v in amps.values()),K()) == 6

# Pauli action on one bit: returns (newbit, phase).
def act1(label,bit):
    if label=='I': return bit,one
    if label=='X': return 1-bit,one
    if label=='Z': return bit, one if bit==0 else -one
    if label=='Y': return 1-bit, ii if bit==0 else -ii
    raise ValueError(label)
def expect(labels):
    total=K()
    for x,cx in amps.items():
        y=0; phase=one
        for pos,label in enumerate(labels):
            bit=(x>>(3-pos))&1
            nb,ph=act1(label,bit)
            y=(y<<1)|nb; phase=phase*ph
        cy=amps.get(y,K())
        total=total+cy.conj()*phase*cx
    return total/6

axes='XYZ'
# one-body tensors
for i in range(4):
    for a in axes:
        labs=['I']*4; labs[i]=a
        assert expect(labs)==0
# two-body tensors
for i,j in combinations(range(4),2):
    for a,b in product(axes,repeat=2):
        labs=['I']*4; labs[i]=a; labs[j]=b
        target=F(-1,3) if a==b else 0
        assert expect(labs)==target
# Levi-Civita
def eps(a,b,c):
    if len({a,b,c})<3:return 0
    p=[axes.index(a),axes.index(b),axes.index(c)]
    inv=sum(p[u]>p[v] for u in range(3) for v in range(u+1,3))
    return -1 if inv%2 else 1
triple_sign={(0,1,2):-1,(0,1,3):1,(0,2,3):-1,(1,2,3):1}
for tri in combinations(range(4),3):
    for abc in product(axes,repeat=3):
        labs=['I']*4
        for i,a in zip(tri,abc): labs[i]=a
        target=triple_sign[tri]*eps(*abc)*rt3/3
        assert expect(labs)==target
# four-body isotropic pairing tensor
for abcd in product(axes,repeat=4):
    labs=list(abcd)
    a,b,c,d=abcd
    target=F((a==b)*(c==d)+(a==c)*(b==d)+(a==d)*(b==c),3)
    assert expect(labs)==target

# Minimal polynomial engine to verify the four-vector Gram identity.
# Variables are a=g12,b=g13,c=g14,d=g23,e=g24,f=g34.
N=6
def poly_const(q): return {(0,)*N:F(q)} if q else {}
def poly_var(k):
    e=[0]*N;e[k]=1;return {tuple(e):F(1)}
def padd(P,Q):
    R=P.copy()
    for m,v in Q.items():
        R[m]=R.get(m,F(0))+v
        if not R[m]: del R[m]
    return R
def pneg(P):return {m:-v for m,v in P.items()}
def psub(P,Q):return padd(P,pneg(Q))
def pmul(P,Q):
    R={}
    for m,u in P.items():
        for n,v in Q.items():
            k=tuple(m[i]+n[i] for i in range(N));R[k]=R.get(k,F(0))+u*v
    return {m:v for m,v in R.items() if v}
def ppow(P,n):
    R=poly_const(1)
    for _ in range(n): R=pmul(R,P)
    return R
def det(M):
    if len(M)==1:return M[0][0]
    R={}
    for j in range(len(M)):
        sub=[row[:j]+row[j+1:] for row in M[1:]]
        term=pmul(M[0][j],det(sub))
        R=padd(R,term if j%2==0 else pneg(term))
    return R
v=[poly_var(i) for i in range(6)]
a,b,c,d,e,f=v
onep=poly_const(1)
G=[[onep,a,b,c],[a,onep,d,e],[b,d,onep,f],[c,e,f,onep]]
S={}
for x in v:S=padd(S,ppow(x,2))
# Triple determinant squares for unit-vector Gram triples.
def triple(x,y,z):
    # det [[1,x,y],[x,1,z],[y,z,1]] = 1+2xyz-x^2-y^2-z^2
    R=poly_const(1);R=padd(R,{m:2*q for m,q in pmul(pmul(x,y),z).items()})
    for t in (x,y,z):R=psub(R,ppow(t,2))
    return R
T={}
for x,y,z in [(a,b,d),(a,c,e),(b,c,f),(d,e,f)]:T=padd(T,triple(x,y,z))
P={}
for x,y in [(a,f),(b,e),(c,d)]:P=padd(P,ppow(pmul(x,y),2))
Q=padd(padd(pmul(a,f),pmul(b,e)),pmul(c,d))
rhs=psub(padd(padd(T,S),{m:2*q for m,q in P.items()}),poly_const(3))
gram_residual=psub(ppow(Q,2),rhs)
assert padd(det(G),gram_residual)=={}
print('VERIFY_OK')
