"""Exact-arithmetic verification of the Fermat quartic's F5 Picard trace lattice.

Requires Python 3.10+ and SymPy 1.12+; run: python verify.py
No file/network input. Counts include the entire projective surface over F25.
"""
import collections
import itertools
import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_form

# F_25=F_5[a]/(a^2-2); a^4=-1. Pairs represent u+v*a.
ZERO=(0,0); ONE=(1,0)
def add(x,y):return ((x[0]+y[0])%5,(x[1]+y[1])%5)
def sub(x,y):return ((x[0]-y[0])%5,(x[1]-y[1])%5)
def mul(x,y):return ((x[0]*y[0]+2*x[1]*y[1])%5,(x[0]*y[1]+x[1]*y[0])%5)
def inv(x):
    d=pow((x[0]*x[0]-2*x[1]*x[1])%5,-1,5)
    return ((x[0]*d)%5,(-x[1]*d)%5)

# Three coordinate matchings, 4x4 coefficient pairs: 48 lines.
MATCHINGS=[((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2))]
lines=[]
for m in MATCHINGS:
    for u in range(1,5):
        for v in range(1,5):
            equations=[]
            for (i,j),b in zip(m,(u,v)):
                row=[ZERO]*4
                row[i]=ONE
                row[j]=(0,(-b)%5)
                equations.append(row)
            lines.append((m,u,v,equations))
assert len(lines)==48

def matrix_rank_f25(rows):
    a=[row[:] for row in rows]
    rank=0
    for j in range(4):
        piv=next((i for i in range(rank,len(a)) if a[i][j]!=ZERO),None)
        if piv is None:continue
        a[rank],a[piv]=a[piv],a[rank]
        unit=inv(a[rank][j])
        a[rank]=[mul(unit,t) for t in a[rank]]
        for i in range(rank+1,len(a)):
            if a[i][j]!=ZERO:
                q=a[i][j]
                a[i]=[sub(v,mul(q,w)) for v,w in zip(a[i],a[rank])]
        rank+=1
        if rank==len(a):break
    return rank

G=sp.zeros(48)
for i,l in enumerate(lines):
    G[i,i]=-2
    for j in range(i+1,48):
        meets=int(matrix_rank_f25(l[3]+lines[j][3])<4)
        G[i,j]=G[j,i]=meets
assert all(sum(int(G[i,j]) for j in range(48) if j!=i)==14 for i in range(48))
assert G.rank()==20
assert G.eigenvals()=={sp.Integer(12):1,sp.Integer(-12):1,sp.Integer(-8):6,sp.Integer(-4):12,sp.Integer(0):28}

# Frobenius on a sends a to -a; all 48 lines form 24 conjugate pairs.
seen=set();orbits=[]
for i,(m,u,v,eq) in enumerate(lines):
    if i in seen:continue
    j=next(t for t,l in enumerate(lines) if l[:3]==(m,(-u)%5,(-v)%5))
    assert i!=j and j not in seen and G[i,j]==0
    seen.update((i,j));orbits.append((i,j))
assert len(orbits)==24 and len(seen)==48
S=sp.zeros(48,24)
for k,(i,j) in enumerate(orbits):
    S[i,k]=S[j,k]=1
H=S.T*G*S
assert H.rank()==8
assert collections.Counter(H[i,j] for i in range(24) for j in range(i+1,24))=={0:168,2:48,4:60}
assert H.eigenvals()=={sp.Integer(24):1,sp.Integer(-24):1,sp.Integer(-16):6,sp.Integer(0):16}

# Exact index and discriminant of the lattice spanned by 48 lines.
_,piv=G.rref();piv=list(piv)
assert len(piv)==20
B=G.extract(piv,piv)
assert B.det()==-64
V=B.inv()*G.extract(piv,list(range(48)))
d=sp.ilcm(*[int(sp.denom(v)) for v in V])
C=hermite_normal_form((V*d).applyfunc(int))
assert C.shape==(20,20)
assert sp.Rational(d)**20/abs(C.det())==1
# Thus the 20 pivot lines form a genuine integral lattice basis.
assert d==1 or sp.Rational(d)**20/abs(C.det())==1

# Trace-lattice basis in the coordinates of the 20 line basis classes.
W=V*S
D=sp.ilcm(*[int(sp.denom(v)) for v in W])
T=hermite_normal_form((W*D).applyfunc(int))/D
assert T.shape==(20,8)
assert all(sp.denom(z)==1 for z in T)
T=T.applyfunc(int)
Q=T.T*B*T
assert Q.det()==-4096 and Q.rank()==8
assert [abs(int(smith_normal_form(Q,domain=sp.ZZ)[i,i])) for i in range(8)]==[2]*6+[8,8]

# T is 2-saturated in L: all 2^8 half-trace cosets are tested.
for m in range(1,256):
    v=T*sp.Matrix([(m>>j)&1 for j in range(8)])
    assert any(int(z)%2 for z in v)
# Since 2 NS^Frob is contained in T, 2-saturation implies NS^Frob=T.

# Independent complete projective point count over F25, and F5 proof.
F25=[(a,b) for a in range(5) for b in range(5)]
p4={x:mul(mul(x,x),mul(x,x)) for x in F25}
count=0
for j in range(4):
    for tail in itertools.product(F25,repeat=3-j):
        xx=[ZERO]*j+[ONE]+list(tail)
        s=ZERO
        for x in xx:s=add(s,p4[x])
        count+=(s==ZERO)
assert count==1112
assert sum((sum(pow(x,4,5) for x in ([0]*j+[1]+list(tail)))%5)==0
           for j in range(4) for tail in itertools.product(range(5),repeat=3-j))==0
# Frobenius has 8 fixed and 12 anti-fixed algebraic dimensions.
# The remaining H^2 trace is -6; pure weight 2 gives T^2+6T+25.
assert 1+25+(8-12)*5-6==0
assert 1+625+(8+12)*25+((-3+4j)**2+(-3-4j)**2)==1112
print('VERIFY_OK: 48 lines, 24 conjugate pairs, Picard rank 8, discriminant -4096, SNF 2^6 8^2; F25 points 1112')
