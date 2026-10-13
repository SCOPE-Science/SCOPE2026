from fractions import Fraction as Q

# Polynomials are coefficient lists, low degree first.
def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]==0: a.pop()
    return a

def add(a,b):
    n=max(len(a),len(b)); c=[Q(0) for _ in range(n)]
    for i,x in enumerate(a): c[i]+=x
    for i,x in enumerate(b): c[i]+=x
    return trim(c)

def neg(a): return [-x for x in a]
def sub(a,b): return add(a,neg(b))
def mul(a,b):
    c=[Q(0) for _ in range(len(a)+len(b)-1)]
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return trim(c)
def scale(a,s): return trim([Q(s)*x for x in a])
def pw(a,n):
    r=[Q(1)]; b=a
    while n:
        if n&1: r=mul(r,b)
        b=mul(b,b); n//=2
    return r

def divmodp(a,b):
    a=trim(a); b=trim(b)
    q=[Q(0)]*max(1,(len(a)-len(b)+1))
    while len(a)>=len(b) and a!=[0]:
        d=len(a)-len(b); t=a[-1]/b[-1]
        q[d]+=t
        a=sub(a, [Q(0)]*d + scale(b,t))
    return trim(q),trim(a)

def compose_shift(a,shift):
    # a(x+shift)
    xps=[Q(shift),Q(1)]
    r=[Q(0)]
    for i,c in enumerate(a): r=add(r,scale(pw(xps,i),c))
    return trim(r)

class RF:
    def __init__(self,n,d=(1,)):
        self.n=trim([Q(x) for x in n]); self.d=trim([Q(x) for x in d])
    def __add__(self,o):
        o=o if isinstance(o,RF) else RF([o])
        return RF(add(mul(self.n,o.d),mul(o.n,self.d)),mul(self.d,o.d))
    def __neg__(self): return RF(neg(self.n),self.d)
    def __sub__(self,o): return self+(-o)
    def __mul__(self,o):
        o=o if isinstance(o,RF) else RF([o])
        return RF(mul(self.n,o.n),mul(self.d,o.d))
    def inv(self): return RF(self.d,self.n)
    def __truediv__(self,o):
        o=o if isinstance(o,RF) else RF([o])
        return self*o.inv()
    def __pow__(self,n): return RF(pw(self.n,n),pw(self.d,n))

x=[Q(0),Q(1)]
G=[Q(16),Q(-64),Q(55),Q(16)]
N=[Q(-16),Q(28)]; D=[Q(-36),Q(67)]
# D^3 G(N/D)=512 G(x)
lhs=add(add(scale(pw(N,3),16),scale(mul(pw(N,2),D),55)),add(scale(mul(N,pw(D,2)),-64),scale(pw(D,3),16)))
assert trim(lhs)==trim(scale(G,512))

# Projective matrix of tau cubed.
def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
M=[[28,-16],[67,-36]]
M2=mm(M,M); M3=mm(M2,M)
assert M2==[[-288,128],[-536,224]]
assert M3==[[512,0],[0,512]]

X=RF(x)
tau=RF(N,D)
tau2=RF([Q(-16),Q(36)],[Q(-28),Q(67)])
p=RF([Q(-4),Q(5),Q(8)],[Q(-8),Q(16)])
q=RF([Q(4),Q(-11),Q(8)],[Q(-8),Q(16)])
# Entry-renormalization identities, checked exactly modulo G.
for name,e in [
    ('c_to_tau', tau.inv()**2 - (q**2)/(X**2) + q*2),
    ('b_to_tau2', tau2.inv()**2 - (p**2)/(X**2) + p*2),
]:
    _,rem=divmodp(e.n,G)
    assert rem==[0], (name,rem)

# Fixed points of tau: 67 x^2 - 64 x + 16, discriminant -192.
assert (-64)**2-4*67*16==-192

# Integral model y=16k.
F=[Q(4096),Q(-1024),Q(55),Q(1)]
b,c,d=55,-1024,4096
disc=b*b*c*c - 4*c*c*c - 4*b*b*b*d - 27*d*d + 18*b*c*d
assert disc==(128*91)**2

# z=(y^2+119y+64)/128 is integral: z^3+10z^2-361z+1702=0 modulo F.
yRF=RF(x)
z=(yRF**2 + yRF*119 + 64)/128
Pz=z**3 + z**2*10 - z*361 + 1702
_,rem=divmodp(Pz.n,F)
assert rem==[0], rem
assert disc//(128**2)==91**2

# Eisenstein shifts proving total ramification at 7 and 13.
F7=compose_shift(F,-2)   # F(X-2), for y+2
F13=compose_shift(F,-1)  # F(X-1), for y+1
assert [int(v) for v in F7]==[6356,-1232,49,1]
assert [int(v) for v in F13]==[5174,-1131,52,1]
for p0,H in [(7,F7),(13,F13)]:
    ints=[int(v) for v in H]
    assert all(v%p0==0 for v in ints[:-1])
    assert ints[0]%(p0*p0)!=0
    assert ints[-1]%p0!=0

print('VERIFY_OK mobius_order=3 root_cycle=exact entry_cycle=a->c->b field_discriminant=8281 eisenstein=7,13')
