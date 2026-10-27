from collections import deque,Counter,defaultdict
from math import gcd
from functools import reduce
from sympy import Matrix,ZZ
from sympy.matrices.normalforms import smith_normal_form
from itertools import combinations
from sympy.matrices.normalforms import hermite_normal_form

# v=(h,e1,...,e6) with Ei coefficient +1; intersection h*h - sum ei*ej.
H=(1,0,0,0,0,0,0)
E=[tuple(int(j==i+1) for j in range(7)) for i in range(6)]
L=[]
L+=E
for i,j in combinations(range(6),2):L.append(tuple(H[k]-E[i][k]-E[j][k] for k in range(7)))
for i in range(6):L.append(tuple(2*H[k]-sum(E[j][k] for j in range(6) if j!=i) for k in range(7)))
assert len(L)==27 and len(set(L))==27
ind={v:i for i,v in enumerate(L)}
def dot(v,w):return v[0]*w[0]-sum(v[i]*w[i] for i in range(1,7))
def sub(u,v):return tuple(a-b for a,b in zip(u,v))
roots=[sub(E[i],E[i+1]) for i in range(5)]+[tuple(H[k]-E[0][k]-E[1][k]-E[2][k] for k in range(7))]
assert all(dot(r,r)==-2 for r in roots)
def ref(v,r):
 d=dot(v,r)
 return tuple(v[k]+d*r[k] for k in range(7))
gens=[]
for r in roots:
 p=tuple(ind[ref(v,r)] for v in L)
 assert len(set(p))==27
 gens.append(p)
iden=tuple(range(27))
def mul(a,b):return tuple(a[b[i]] for i in range(27))
def inv(a):
 out=[0]*27
 for i,j in enumerate(a):out[j]=i
 return tuple(out)
# BFS all group by right multiplication; words optional
allp={iden:0}; g_list=[iden];queue=deque([iden]);
while queue:
 p=queue.popleft()
 for q in gens:
  r=mul(p,q)
  if r not in allp:
   allp[r]=len(g_list);g_list.append(r);queue.append(r)

assert len(allp)==51840
# conjugacy classes orbit by conjugation of 6 generators
seen=set(); classes=[]
for p in g_list:
 if p in seen:continue
 cl={p}; dq=deque([p])
 while dq:
  x=dq.popleft()
  for g in gens:
   y=mul(mul(g,x),g) # g involution
   if y not in cl:
    cl.add(y);dq.append(y)
 classes.append((p,len(cl)))
 seen.update(cl)

assert len(classes)==25

def permcycles(p):
 vis=set(); c=[]
 for i in range(len(p)):
  if i not in vis:
   cyc=[];j=i
   while j not in vis:
    vis.add(j);cyc.append(j);j=p[j]
   c.append(cyc)
 return c

def permord(p):
 from math import lcm
 return reduce(lcm,(len(c) for c in permcycles(p)),1)

def mappic(p):
 ecol=[L[p[i]] for i in range(6)]
 # H'= (3H - Sigma Ei + Sigma images(E_i))/3
 hcol=[]
 for j in range(7):
  v=3*H[j]-sum(E[i][j] for i in range(6))+sum(ecol[i][j] for i in range(6))
  assert v%3==0, (p,v)
  hcol.append(v//3)
 W=Matrix.hstack(Matrix(hcol),*[Matrix(e) for e in ecol]);
 assert W.det() in (1,-1)
 return W

def trindex(p):
 cycles=permcycles(p)
 trs=[tuple(sum(L[i][j] for i in c) for j in range(7)) for c in cycles]
 A=Matrix.hstack(*[Matrix(v) for v in trs]); r=A.rank()
 S=smith_normal_form(A,domain=ZZ)
 d=[abs(int(S[i,i])) for i in range(min(S.rows,S.cols)) if S[i,i]!=0]
 assert len(d)==r
 return r,reduce(lambda x,y:x*y,d,1),tuple(d),cycles

out=[]
for idx,(p,size) in enumerate(classes):
 rank,index,snf,cycles=trindex(p)
 W=mappic(p)
 assert (W-Matrix.eye(7)).nullspace().__len__()==rank
 assert W.T * Matrix.diag(1,-1,-1,-1,-1,-1,-1)*W==Matrix.diag(1,-1,-1,-1,-1,-1,-1)
 cyc=Counter(map(len,cycles))
 out.append({'idx':idx,'order':permord(p),'class_size':size,'pic_rank':rank,'trace_index':index,'snf':snf,'line_cycles':str(sorted(cyc.items())),'p':list(p)})


# Independent integer saturation computation: Hermite basis and gcd of maximal minors.
from math import gcd
for row in out:
    p=tuple(row['p'])
    cycles=permcycles(p)
    A=Matrix.hstack(*(Matrix([sum(L[i][j] for i in c) for j in range(7)]) for c in cycles))
    B=hermite_normal_form(A)
    r=row['pic_rank']
    assert B.shape==(7,r)
    gcd_minor=0
    for indices in combinations(range(7),r):
        gcd_minor=gcd(gcd_minor,abs(int(B[list(indices),:].det())))
    assert gcd_minor==row['trace_index'], (row['idx'],gcd_minor,row['trace_index'])
assert sorted([int(row['class_size']) for row in out]) and sum(row['class_size'] for row in out)==51840
assert Counter(row['trace_index'] for row in out)=={1:22,3:3}
exceptional=sorted((row['order'],row['pic_rank'],row['class_size'],
                sorted(Counter(map(len,permcycles(tuple(row['p'])))).items()), row['snf'])
                 for row in out if row['trace_index']==3)
assert exceptional==[(3,3,480,[(3,9)],(1,1,3)),
                     (6,2,4320,[(3,1),(6,4)],(1,3)),
                     (9,1,5760,[(9,3)],(3,))]
# A conjugacy-class representative of order 9 gives three orbit sums equal to 3H.
Hanti=Matrix([3,-1,-1,-1,-1,-1,-1])
for row in out:
    if row['order']==9 and row['trace_index']==3:
        p=tuple(row['p'])
        assert mappic(p)*Hanti==Hanti
        for c in permcycles(p):
            assert abs(int(Matrix([sum(L[i][j] for i in c) for j in range(7)])[0]))==9
            assert Matrix([sum(L[i][j] for i in c) for j in range(7)])==3*Hanti
print('VERIFY_OK: 51840 Weyl elements; 25 conjugacy classes; index 3 for exactly orders/ranks (3,3), (6,2), (9,1); independent Hermite-minor check')
