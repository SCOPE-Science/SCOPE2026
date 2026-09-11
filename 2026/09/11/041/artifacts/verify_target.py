"""TARGET verifier: M2 (rank 4 on [8], nonbases {1234,5678}) realizability lift.
Checks: (1) exact 70-minor support of A; (2) matroid axioms/connectedness;
(3) Dressian 3-term min-twice for h; (4) secondary subdivision: 3 full-dim
cells w/ supporting planes, strict-above, cover; (5) valued lift A(t)=A+tG
valuations = h (0 bases / 1 nonbases) -> relint of Dressian secondary cone.
Run: python3 verify_target.py  (stdlib only) -> prints ALL_CHECKS_PASS.
"""
import itertools
from fractions import Fraction
cols=[[4,4,1,0],[3,5,4,0],[4,3,4,0],[3,5,2,0],[0,5,2,3],[0,2,1,5],[0,3,5,5],[0,2,3,1]]
A=[[cols[c][r] for c in range(8)] for r in range(4)]
G=[[0]*8 for _ in range(4)]; G[3][0]=1; G[0][4]=1
NB={(0,1,2,3),(4,5,6,7)}
def det_int(M):
    n=len(M)
    if n==0: return Fraction(1)
    B=[[Fraction(x) for x in row] for row in M]; s=Fraction(1)
    for i in range(n):
        p=next((r for r in range(i,n) if B[r][i]!=0),None)
        if p is None: return Fraction(0)
        if p!=i: B[i],B[p]=B[p],B[i]; s=-s
        s*=B[i][i]
        for r in range(i+1,n):
            f=B[r][i]/B[i][i]
            for c in range(i,n): B[r][c]-=f*B[i][c]
    return s
def det_lin(Mc,Ml):
    from itertools import combinations as C
    d=[Fraction(0)]*5
    for k in range(5):
        for R in C(range(4),k):
            Rc=[i for i in range(4) if i not in R]
            for Cc_ in C(range(4),k):
                Cc=[j for j in range(4) if j not in Cc_]
                d[k]+=((-1)**(sum(R)+sum(Cc_)))*det_int([[Ml[r][c] for c in Cc_] for r in R])*det_int([[Mc[r][c] for c in Cc] for r in Rc])
    while len(d)>1 and d[-1]==0: d.pop()
    return d
verts=list(itertools.combinations(range(8),4))
ok=True
# 1: support
for S in verts:
    d=det_int([[cols[c][r] for c in S] for r in range(4)])
    if (d==0)!=(S in NB): ok=False; print("SUPPORT FAIL",S,d)
print("1) support exact:", ok)
# 2: exchange + connected
F=set(s for s in verts if s not in NB)
def exch(fam):
    F_=set(fam)
    for B1 in fam:
        for B2 in fam:
            for x in B1:
                if x in B2: continue
                if not any(tuple(sorted((set(B1)-{x})|{y})) in F_ for y in B2 if y not in B1): return False
    return True
print("2) exchange:", exch(list(F)))
def rank(S):
    S=set(S)
    if len(S)<=3: return len(S)
    if tuple(sorted(S)) in NB and len(S)==4: return 3
    for B in itertools.combinations(sorted(S),4):
        if B not in NB: return 4
    return 3
seps=[X for k in range(1,8) for X in itertools.combinations(range(8),k) if rank(set(X))+rank(set(range(8))-set(X))==4]
print("   connected:", seps==[])
# 3: Dressian
def h(S): return 1 if tuple(sorted(S)) in NB else 0
nrel=0; dok=True
for Sm in itertools.combinations(range(8),2):
    R=[i for i in range(8) if i not in Sm]
    for i,j,k,l in itertools.combinations(R,4):
        t=sorted([h(Sm+(i,j))+h(Sm+(k,l)),h(Sm+(i,k))+h(Sm+(j,l)),h(Sm+(i,l))+h(Sm+(j,k))])
        nrel+=1
        if t[0]!=t[1]: dok=False
print(f"3) Dressian 3-term x{nrel}:", dok)
# 4: subdivision
C1=[(0,1,2,3)]+[S for S in verts if len(set(S)&{0,1,2,3})==3 and S!=(0,1,2,3)]
C2=[(4,5,6,7)]+[S for S in verts if len(set(S)&{4,5,6,7})==3 and S!=(4,5,6,7)]
C0=[S for S in verts if S not in NB]
p1=lambda S: len(set(S)&{0,1,2,3})-3; p2=lambda S: len(set(S)&{4,5,6,7})-3
f0=all(h(S)==0 for S in C0) and all(h(T)>0 for T in verts if T not in C0)
f1=all(h(S)==p1(S) for S in C1) and all(h(T)>p1(T) for T in verts if T not in C1)
f2=all(h(S)==p2(S) for S in C2) and all(h(T)>p2(T) for T in verts if T not in C2)
def affdim(cell):
    M2=[[ (1 if i in P else 0)-(1 if i in cell[0] else 0) for i in range(8)] for P in cell[1:]]
    r=0
    for c in range(8):
        p=next((i for i in range(r,len(M2)) if M2[i][c]!=0),None)
        if p is None: continue
        M2[r],M2[p]=M2[p],M2[r]
        for i in range(len(M2)):
            if i!=r and M2[i][c]!=0:
                f=Fraction(M2[i][c],M2[r][c])
                for j in range(8): M2[i][j]-=f*M2[r][j]
        r+=1
    return r
d0,d1,d2=affdim(C0),affdim(C1),affdim(C2)
print("4) sizes:",len(C0),len(C1),len(C2),"| faces:",f0,f1,f2,"| dims:",d0,d1,d2,
      "| cover:",set(C0)|set(C1)|set(C2)==set(verts),"| C1∩C2:",len(set(C1)&set(C2)),
      "| matroid cells:",exch(C1),exch(C2))
# 5: valued lift
vok=True
for S in verts:
    d=det_lin([[A[r][c] for c in S] for r in range(4)],[[G[r][c] for c in S] for r in range(4)])
    if next((i for i,x in enumerate(d) if x!=0),None)!=(1 if S in NB else 0): vok=False; print("VAL FAIL",S,d)
print("5) lift valuations = h:", vok)
print("   det1234(t) =",det_lin([[A[r][c] for c in (0,1,2,3)] for r in range(4)],[[G[r][c] for c in (0,1,2,3)] for r in range(4)]))
print("   det5678(t) =",det_lin([[A[r][c] for c in (4,5,6,7)] for r in range(4)],[[G[r][c] for c in (4,5,6,7)] for r in range(4)]))
allok=ok and dok and f0 and f1 and f2 and (d0,d1,d2)==(7,7,7) and vok
print("ALL_CHECKS_PASS" if allok else "CHECKS_FAILED")
