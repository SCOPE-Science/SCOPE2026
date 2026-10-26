"""Exact-arithmetic checks for the subdivision-graph RK4 theorem.
This is finite corroboration and symbolic identity testing, not an infinite proof.
Run: python verify.py (requires sympy >=1.12)."""
from fractions import Fraction as F
from itertools import combinations
from sympy import symbols, factor, expand, Rational

d,h,x=symbols('d h x')
Finc=1-(d+2)*h/2+(d*d+3*d+5)*h*h/6-(d+2)*(d*d+2*d+6)*h**3/24
assert factor(Finc.subs(h,2/(d+2))-Rational(1,3))==0
A=2*(d*d+3*d+5)/(3*(d+2)**2)
B=(d*d+2*d+6)/(3*(d+2)**2)
assert factor(A-B-Rational(1,3))==0
assert factor(Finc.subs(h,2*x/(d+2))-(1-x+x*x*(A-B*x)))==0
assert expand(64*(d+1)**2-48*(3*d*d+6*d+4+symbols('t'))+80*d*d+160*d+128+48*symbols('t'))==0
assert expand(16*(d+4)**2-48*(d*d+5*d+14+symbols('s'))+32*d*d+112*d+416+48*symbols('s'))==0
Z=symbols('Z')
R4=1-Z+Z**2/2-Z**3/6+Z**4/24
assert factor(R4-((1-Z/2)**2+Z**2*((Z-2)**2+2)/24))==0
assert factor((1-R4).subs(Z,x)+x*(x**3-4*x*x+12*x-24)/24)==0


def matmul(X,Y):
 n=len(X);m=len(Y);p=len(Y[0]);Z=[[0]*p for _ in range(n)]
 for i in range(n):
  for k in range(m):
   a=X[i][k]
   if a:
    for j in range(p):Z[i][j]+=a*Y[k][j]
 return Z


def base_graph(kind,param):
 if kind=='clique':
  n=param;return n,list(combinations(range(n),2))
 if kind=='cycle':
  n=param;return n,sorted({tuple(sorted((i,(i+1)%n))) for i in range(n)})
 if kind=='biclique':
  n=2*param;return n,[(i,j) for i in range(param) for j in range(param,n)]
 if kind=='cube':
  d0=param;n=2**d0;return n,[(i,i^(1<<k)) for i in range(n) for k in range(d0) if not(i & (1<<k))]
 if kind=='petersen':
  E=[(i,(i+1)%5) for i in range(5)]+[(i,i+5) for i in range(5)]+[(i+5,(i+2)%5+5) for i in range(5)]
  return 10,E
 if kind=='prism':
  E=[(i,(i+1)%param) for i in range(param)]+[(i+param,(i+1)%param+param) for i in range(param)]+[(i,i+param) for i in range(param)]
  return 2*param,E
 if kind=='octahedral':
  E=[(i,j) for i,j in combinations(range(6),2) if i//2!=j//2];return 6,E
 if kind=='heawood':
  # Fano plane: 7 points, 7 lines, each line 3 points.
  lines=[{(k+t)%7 for t in (0,1,3)} for k in range(7)]
  return 14,[(i,j+7) for j,l in enumerate(lines) for i in l]
 raise ValueError(kind)


def check(kind,param):
 n,ed=base_graph(kind,param)
 ed=[tuple(sorted(e)) for e in ed]
 assert len(set(ed))==len(ed) and all(u!=v for u,v in ed)
 g=[set() for _ in range(n)]
 for u,v in ed:g[u].add(v);g[v].add(u)
 deg=len(g[0]);assert deg>=2 and all(len(nei)==deg for nei in g)
 # Connectedness
 seen={0};todo=[0]
 for u in todo:
  for v in g[u]:
   if v not in seen:seen.add(v);todo.append(v)
 assert len(seen)==n
 m=len(ed);N=n+m
 adj=[set() for _ in range(N)]
 for j,(u,v) in enumerate(ed):
  adj[u].add(n+j);adj[v].add(n+j)
  adj[n+j].add(u);adj[n+j].add(v)
 L=[[0]*N for _ in range(N)]
 for i in range(N):
  L[i][i]=len(adj[i]);
  for j in adj[i]:L[i][j]=-1
 P=[[[1 if i==j else 0 for j in range(N)] for i in range(N)]]
 for _ in range(4):P.append(matmul(P[-1],L))
 fac=[1,1,2,6,24]
 count=0
 for i in range(N):
  for j in range(N):
   if i==j:continue
   actual=[F((-1)**k*P[k][i][j],fac[k]) for k in range(5)]
   if i<n and j<n:
    if j in g[i]:
     tt=len(g[i]&g[j]);wanted=[F(0),F(0),F(1,2),F(-deg-1,3),F(3*deg*deg+6*deg+4+tt,24)]
    else:wanted=[F(0),F(0),F(0),F(0),F(len(g[i]&g[j]),24)]
   elif i>=n and j>=n:
    a,b=ed[i-n],ed[j-n];shared=set(a)&set(b)
    if shared:
     uu=next(iter(set(a)-shared));vv=next(iter(set(b)-shared));ss=int(vv in g[uu]);wanted=[F(0),F(0),F(1,2),F(-(deg+4),6),F(deg*deg+5*deg+14+ss,24)]
    else:
     crossing=sum(int(v in g[u]) for u in a for v in b)
     wanted=[F(0),F(0),F(0),F(0),F(crossing,24)]
   else:
    u=i if i<n else j
    a,b=ed[(j if j>=n else i)-n]
    if u in (a,b):
     wanted=[F(0),F(1),F(-(deg+2),2),F(deg*deg+3*deg+5,6),F(-(deg+2)*(deg*deg+2*deg+6),24)]
    else:
     cc=int(a in g[u])+int(b in g[u]);wanted=[F(0),F(0),F(0),F(cc,6),F(-cc*(deg+2),12)]
   assert actual==wanted,(kind,param,i,j,actual,wanted)
   count+=1
 def Tval(i,j,t):return sum(F((-1)**k*P[k][i][j],fac[k])*t**k for k in range(5))
 H=F(2,deg+2)
 for step in [F(0),H/3,F(1,deg),H]:
  assert all(Tval(i,j,step)>=0 for i in range(N) for j in range(N)),(kind,param,step)
  assert all(sum(Tval(i,j,step) for j in range(N))==1 for i in range(N))
 for t in [H+F(1,10*(deg+2)),2*H,10*H]:
  assert any(Tval(i,j,t)<0 for i in range(N) for j in range(N)),(kind,param,t)
 # Verify explicit upper-eigenvalue eigenvector with old values d and new values -2.
 eigvec=[deg]*n+[-2]*m
 assert all(sum(L[i][j]*eigvec[j] for j in range(N))==(deg+2)*eigvec[i] for i in range(N))
 return N,count

cases=[('clique',k) for k in range(3,8)]+[('cycle',k) for k in range(3,11)]+[('biclique',k) for k in (2,3,4)]+[('cube',k) for k in (2,3,4)]+[('petersen',0),('prism',3),('prism',5),('octahedral',0),('heawood',0)]
total=0;entries=0
for kind,param in cases:
 N,z=check(kind,param);total+=1;entries+=z
print('VERIFY_OK',total,'different regular base graphs;',entries,'exact off-diagonal RK4 coefficient comparisons; rational steps and spectral eigenvector verified; all symbolic certificates verified')
