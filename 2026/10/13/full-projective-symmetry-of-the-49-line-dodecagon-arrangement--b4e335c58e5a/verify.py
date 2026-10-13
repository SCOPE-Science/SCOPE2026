from itertools import combinations, permutations
from collections import Counter
from math import gcd
import sympy as sp

K = sp.QQ.algebraic_field(sp.sqrt(3))
Z = K.zero

def cv(a): return K.from_sympy(sp.simplify(a))
def cross(a,b):
    return [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]]
def pkey(v):
    for q in v:
        if q != Z:
            return tuple(x/q for x in v)
    raise AssertionError('zero vector')
def dot(l,p): return l[0]*p[0]+l[1]*p[1]+l[2]*p[2]
def cols(cs): return [[cs[j][i] for j in range(3)] for i in range(3)]
def det(A):
    return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
           -A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
           +A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))
def inv(A):
    d=det(A)
    if d==Z: return None
    B=[
      [ A[1][1]*A[2][2]-A[1][2]*A[2][1], -(A[0][1]*A[2][2]-A[0][2]*A[2][1]), A[0][1]*A[1][2]-A[0][2]*A[1][1]],
      [-(A[1][0]*A[2][2]-A[1][2]*A[2][0]), A[0][0]*A[2][2]-A[0][2]*A[2][0], -(A[0][0]*A[1][2]-A[0][2]*A[1][0])],
      [ A[1][0]*A[2][1]-A[1][1]*A[2][0], -(A[0][0]*A[2][1]-A[0][1]*A[2][0]), A[0][0]*A[1][1]-A[0][1]*A[1][0]]]
    return [[B[i][j]/d for j in range(3)] for i in range(3)]
def mm(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(3)),Z) for j in range(3)] for i in range(3)]
def mv(A,v):
    return [sum((A[i][k]*v[k] for k in range(3)),Z) for i in range(3)]
def tr(A): return [[A[j][i] for j in range(3)] for i in range(3)]
def H4(src,tgt):
    Bs,Bt=cols(src[:3]),cols(tgt[:3])
    Bsi,Bti=inv(Bs),inv(Bt)
    if Bsi is None or Bti is None: return None
    cs,ct=mv(Bsi,src[3]),mv(Bti,tgt[3])
    if any(c==Z for c in cs) or any(c==Z for c in ct): return None
    Ps=[[Bs[i][j]*cs[j] for j in range(3)] for i in range(3)]
    Pt=[[Bt[i][j]*ct[j] for j in range(3)] for i in range(3)]
    Psi=inv(Ps)
    return None if Psi is None else mm(Pt,Psi)
def peqM(A,B):
    # projective equality of nonzero 3x3 matrices
    aa=sum(A,[]); bb=sum(B,[])
    for a,b in zip(aa,bb):
        if a!=Z and b!=Z:
            lam=a/b
            return all(x==lam*y for x,y in zip(aa,bb))
        if (a==Z)!=(b==Z): return False
    return False
def matpow(A,n):
    I=[[K.one if i==j else Z for j in range(3)] for i in range(3)]
    R=I
    while n:
        if n&1: R=mm(R,A)
        A=mm(A,A); n//=2
    return R
def perm_order(p):
    seen=[False]*len(p); o=1
    for i in range(len(p)):
        if not seen[i]:
            j=i;c=0
            while not seen[j]: seen[j]=True;c+=1;j=p[j]
            o=sp.ilcm(o,c)
    return int(o)
def orbits(perms,n):
    unseen=set(range(n)); out=[]
    while unseen:
        a=min(unseen); orb={p[a] for p in perms}; unseen-=orb; out.append(sorted(orb))
    return sorted(out,key=lambda q:(len(q),q))

# Regular dodecagon and its twelve side lines.
V=[]
for j in range(12):
    a=sp.pi*j/6
    V.append([cv(sp.cos(a)),cv(sp.sin(a)),K.one])
C12=[list(pkey(cross(V[j],V[(j+1)%12]))) for j in range(12)]
assert len({pkey(l) for l in C12})==12

# The 66 ordinary intersections of the side arrangement.
Pdict={}
for i,j in combinations(range(12),2):
    Pdict.setdefault(pkey(cross(C12[i],C12[j])),[]).append((i,j))
assert len(Pdict)==66 and all(len(v)==1 for v in Pdict.values())
P=[list(k) for k in Pdict]

# Lambda_{ {2},4}: all lines through at least four of those 66 points.
candidates={}
for i,j in combinations(range(66),2): candidates[pkey(cross(P[i],P[j]))]=None
rich=[]
for lk in candidates:
    l=list(lk); inds=tuple(i for i,p in enumerate(P) if dot(l,p)==Z)
    if len(inds)>=4: rich.append((lk,inds))
O=[list(l) for l,_ in rich]
Okeys={pkey(l) for l in O}
assert len(O)==49
assert Counter(len(v) for _,v in rich)==Counter({4:24,11:12,6:7,5:6})

# Singular-point census.
sing={}
for i,j in combinations(range(49),2):
    pk=pkey(cross(O[i],O[j])); sing.setdefault(pk,set()).update((i,j))
assert Counter(len(v) for v in sing.values())==Counter({2:204,3:96,4:6,5:24,6:6,7:12,12:1})
P12=list([k for k,v in sing.items() if len(v)==12][0])
S7=[list(k) for k,v in sing.items() if len(v)==7]
assert len(S7)==12

# Choose P12 and three sevenfold points forming a projective frame.
src=None
for a,b,c in combinations(range(12),3):
    ss=[P12,S7[a],S7[b],S7[c]]
    if H4(ss,ss) is not None:
        src=ss; break
assert src is not None

# Exhaustive stabilizer enumeration.  Any projective automorphism fixes the unique
# 12-fold point and permutes the 12 sevenfold points.  Its action on this frame
# determines it uniquely, so these 12P3 possibilities are exhaustive.
stabs=[]
for a,b,c in permutations(range(12),3):
    M=H4(src,[P12,S7[a],S7[b],S7[c]])
    if M is None: continue
    N=tr(inv(M))
    if all(pkey(mv(N,l)) in Okeys for l in O): stabs.append(M)
assert len(stabs)==24

idx={pkey(l):i for i,l in enumerate(O)}
perms=[]
for M in stabs:
    N=tr(inv(M)); perms.append(tuple(idx[pkey(mv(N,l))] for l in O))
profile=Counter(perm_order(p) for p in perms)
assert profile==Counter({1:1,2:13,3:2,4:2,6:2,12:4})
orb_sizes=sorted(len(q) for q in orbits(perms,49))
assert orb_sizes==[1,6,6,12,12,12]
fixed=[q for q in orbits(perms,49) if len(q)==1][0][0]
assert pkey(O[fixed])==pkey([Z,Z,K.one])

# Visible dihedral generators inherited from the regular dodecagon.
s=cv(sp.sqrt(3))
R=[[s,-K.one,Z],[K.one,s,Z],[Z,Z,cv(2)]]
S=[[K.one,Z,Z],[Z,-K.one,Z],[Z,Z,K.one]]
I=[[K.one if i==j else Z for j in range(3)] for i in range(3)]
assert peqM(matpow(R,12),I) and not peqM(matpow(R,6),I)
assert peqM(matpow(S,2),I)
assert peqM(mm(mm(S,R),S),inv(R))
for M in (R,S):
    N=tr(inv(M)); assert all(pkey(mv(N,l)) in Okeys for l in O)

print('VERIFY_OK lines=49 singular=204,96,6,24,6,12,1 stabilizer=24:D12 order_profile=1:1,2:13,3:2,4:2,6:2,12:4 line_orbits=1+6+6+12+12+12 fixed=z=0')
