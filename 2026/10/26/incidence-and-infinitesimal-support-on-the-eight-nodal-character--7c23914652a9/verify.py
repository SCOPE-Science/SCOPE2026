#!/usr/bin/env python3
"""Exact exhaustive arithmetic for a specified quartic over F_3; standard library only."""
from collections import Counter, defaultdict, deque
from itertools import combinations, product

# F_9 = F_3[t]/(t*t+1); integer code a+3*b represents a+b*t.
def add(a,b):
    return ((a%3+b%3)%3)+3*((a//3+b//3)%3)
def mul(a,b):
    aa,ab=a%3,a//3
    ba,bb=b%3,b//3
    return (aa*ba+2*ab*bb)%3+3*((aa*bb+ab*ba)%3)
ADD=tuple(tuple(add(i,j) for j in range(9)) for i in range(9))
MUL=tuple(tuple(mul(i,j) for j in range(9)) for i in range(9))
INV={a:next(b for b in range(1,9) if MUL[a][b]==1) for a in range(1,9)}
ZERO=(0,0,0,0)
# Expansion of Psi(x0,x1,x2,x3)-Psi(-x1,x0,-x3,x2), mod 3.
# Entries are (coefficient, exponents of x0,x1,x2,x3).
TERMS=((1,(3,0,0,1)),(1,(2,1,1,0)),(1,(2,1,0,1)),
       (2,(1,2,1,0)),(1,(1,2,0,1)),(1,(1,0,2,1)),
       (1,(1,0,1,2)),(1,(1,0,0,3)),(1,(0,3,1,0)),
       (1,(0,1,3,0)),(2,(0,1,2,1)),(1,(0,1,1,2)))

def peval(terms,v):
    pw=[[1]*5 for _ in range(4)]
    for i in range(4):
        for d in range(1,5):pw[i][d]=MUL[pw[i][d-1]][v[i]]
    s=0
    for c,e in terms:
        z=c
        for i,k in enumerate(e): z=MUL[z][pw[i][k]]
        s=ADD[s][z]
    return s

def grad_terms(i):
    out=[]
    for c,e in TERMS:
        if e[i] % 3:
            ee=list(e); ee[i]-=1
            out.append((c*(e[i]%3)%3,tuple(ee)))
    return tuple(out)
GRAD=tuple(grad_terms(i) for i in range(4))

def smul(a,v):return tuple(MUL[a][x] for x in v)
def plus(u,v):return tuple(ADD[a][b] for a,b in zip(u,v))
def norm(v):
    nz=next(x for x in v if x)
    return smul(INV[nz],v)
def proj_points():
    for i in range(4):
        for rem in product(range(9),repeat=3-i):
            yield (0,)*i+(1,)+rem
POINTS=tuple(proj_points())
assert len(POINTS)==820 and len(set(POINTS))==820
NODES={p for p in POINTS if peval(TERMS,p)==0 and all(peval(G,p)==0 for G in GRAD)}
assert len(NODES)==8

# Independent direct form evaluation over F9; avoids relying on expanded TERMS.
def sub(a,b):return ADD[a][add(0, ((-b%3)+3*((-(b//3))%3)))]
def psi(w,x,y,z):
    w2=MUL[w][w]; x2=MUL[x][x]; y2=MUL[y][y]; z2=MUL[z][z]
    temp=0
    for q in (w2,MUL[w][x],x2,y2,MUL[y][z],z2):temp=ADD[temp][q]
    return MUL[MUL[w][z]][temp]
def direct(v):
    w,x,y,z=v
    nx=add(0, (-x%3)+3*((-(x//3))%3))
    nz=add(0, (-z%3)+3*((-(z//3))%3))
    return sub(psi(w,x,y,z),psi(nx,w,nz,y))
assert all(direct(v)==peval(TERMS,v) for v in POINTS)

# Every 2-dimensional subspace of F9^4 has a unique reduced row echelon basis.
RREF_TOTAL=0
LINES=[]
for i in range(4):
    for j in range(i+1,4):
        f0=[k for k in range(i+1,4) if k!=j]
        f1=list(range(j+1,4))
        for vals in product(range(9),repeat=len(f0)+len(f1)):
            RREF_TOTAL+=1
            u=[0]*4; v=[0]*4; u[i]=1;v[j]=1
            for c,a in zip(f0,vals):u[c]=a
            for c,a in zip(f1,vals[len(f0):]):v[c]=a
            u=tuple(u); v=tuple(v)
            if peval(TERMS,u) or peval(TERMS,v):continue
            if all(peval(TERMS,plus(u,smul(t,v)))==0 for t in range(1,9)):
                LINES.append((u,v))
assert RREF_TOTAL==7462 and len(LINES)==48 and len(set(LINES))==48

def line_points(uv):
    u,v=uv
    return frozenset({norm(v)} | {norm(plus(u,smul(t,v))) for t in range(9)})
LPS=tuple(line_points(L) for L in LINES)
assert all(len(S)==10 and all(peval(TERMS,p)==0 for p in S) for S in LPS)
assert len(set(LPS))==48
PTO=defaultdict(set)
for i,ps in enumerate(LPS):
    for p in ps:PTO[p].add(i)
assert {len(PTO[p]) for p in NODES}=={6}
line_nodes=Counter(len(ps&NODES) for ps in LPS)
assert line_nodes==Counter({0:8,1:32,2:8})
intersection={}
for p,inds in PTO.items():
    for i,j in combinations(sorted(inds),2):
        assert (i,j) not in intersection
        intersection[(i,j)]=p
assert len(intersection)==384
assert sum(p in NODES for p in intersection.values())==120
assert sum(p not in NODES for p in intersection.values())==264
DEG=Counter(sum(i in ij for ij in intersection) for i in range(48))
assert DEG==Counter({14:8,16:32,18:8})
SMOOTH=Counter(sum(i in ij and p not in NODES for ij,p in intersection.items()) for i in range(48))
assert SMOOTH==Counter({8:8,11:32,14:8})
assert Counter(len(PTO[p]) for p in PTO if p not in NODES and len(PTO[p])>=2)==Counter({2:168,3:32})
# Connectedness of intersection graph.
adj=[set() for _ in range(48)]
for i,j in intersection:adj[i].add(j);adj[j].add(i)
seen={0};todo=deque([0])
while todo:
    i=todo.popleft()
    for j in adj[i]-seen:seen.add(j);todo.append(j)
assert len(seen)==48

# Coefficients in F3 give exactly the fixed Frobenius lines (RREF is canonical).
F3_LINES=sum(all(x<3 for row in L for x in row) for L in LINES)
assert F3_LINES==6
assert len(LINES)==6+2*21
assert all(norm(tuple(a%3+3*((-(a//3))%3) for a in p)) in NODES for p in NODES)
assert all(any(c>2 for c in node) for node in NODES)
F3_PTS=sum(all(a<3 for a in p) and peval(TERMS,p)==0 for p in POINTS)
F9_PTS=sum(peval(TERMS,p)==0 for p in POINTS)
assert (F3_PTS,F9_PTS)==(16,208)

def g_poly(terms,u,v,degree):
 poly=[0]*(degree+1)
 for coeff,exps in terms:
  cur=[coeff]
  for i,e in enumerate(exps):
   fact=[0]*(e+1)
   for k in range(e+1):
    z=__import__("math").comb(e,k)%3
    for j in range(e-k):z=MUL[z][u[i]]
    for j in range(k):z=MUL[z][v[i]]
    fact[k]=z
   nxt=[0]*(len(cur)+len(fact)-1)
   for a,p in enumerate(cur):
    for b,q in enumerate(fact):nxt[a+b]=ADD[nxt[a+b]][MUL[p][q]]
   cur=nxt
  for k,c in enumerate(cur):poly[k]=ADD[poly[k]][c]
 return poly

def rank(A):
 mat=[list(row) for row in A]
 r=0
 for c in range(len(mat[0])):
  p=next((k for k in range(r,len(mat)) if mat[k][c]),None)
  if p is None:continue
  mat[r],mat[p]=mat[p],mat[r]
  z=INV[mat[r][c]]
  mat[r]=[MUL[z][x] for x in mat[r]]
  for k in range(len(mat)):
   if k!=r and mat[k][c]:
    fac=mat[k][c]
    mat[k]=[ADD[x][add(0,(-MUL[fac][y]%3)+3*((-(MUL[fac][y]//3))%3))] for x,y in zip(mat[k],mat[r])]
  r+=1
 return r

def tangent_dim(u,v):
 piv=[next(j for j,x in enumerate(row) if x) for row in (u,v)]
 i,j=piv
 f0=[c for c in range(i+1,4) if c!=j];f1=list(range(j+1,4))
 cols=[]
 for c in f0:
  dg=g_poly(GRAD[c],u,v,3)
  cols.append(dg+[0])
 for c in f1:
  dg=g_poly(GRAD[c],u,v,3)
  cols.append([0]+dg)
 A=[[col[k] for col in cols] for k in range(5)]
 return len(cols)-rank(A)
# Zero-dimensional tangent spaces to the line Fano scheme.
TANGENT=[tangent_dim(*L) for L in LINES]
assert Counter(TANGENT)==Counter({0:41,1:7})
assert Counter((len(LPS[i]&NODES),len(adj[i]),TANGENT[i]) for i in range(48)) == Counter({(0,14,0):8,(1,16,0):32,(2,18,1):7,(2,18,0):1})
SPECIAL=((0,1,0,0),(0,0,0,1))
assert [(LINES[i],TANGENT[i]) for i in range(48) if len(LPS[i]&NODES)==2 and TANGENT[i]==0] == [(SPECIAL,0)]

# Independent point-pair line census through rational surface points.
SURF={p for p in POINTS if peval(TERMS,p)==0}
pair_lines=set()
for a,b in combinations(sorted(SURF),2):
    ps=frozenset({norm(b)}|{norm(plus(a,smul(t,b))) for t in range(9)})
    if ps <= SURF:pair_lines.add(ps)
assert pair_lines==set(LPS)
print('VERIFY_OK: 7462 ambient lines; 48 surface lines; 8 nodes;')
print('Frobenius line cycles 1^6 2^21; node cycles 2^4;')
print('384 intersection pairs, 120 at nodes; graph degrees 14^8 16^32 18^8;')
print('F3/F9 surface-point counts 16/208; 7 tangent-obstructed lines are exactly all but')
print('one of the 8 two-node lines; independent point-pair census agrees.')
