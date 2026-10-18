from collections import Counter,defaultdict
from itertools import product,permutations
# finite field GF(8) with t^3+t+1
mul=[[0]*8 for _ in range(8)]
for x in range(8):
 for y in range(8):
  a=0
  for i in range(3):
   for j in range(3):
    if x>>i&1 and y>>j&1: a^=1<<(i+j)
  for k in range(4,2,-1):
   if a>>k&1:a^=(0b1011<<(k-3))
  mul[x][y]=a
inv={a:next(b for b in range(1,8) if mul[a][b]==1) for a in range(1,8)}
def mult(a,b):return mul[a][b]
def matv(M,v):return tuple(mult(M[i][j],v[j])^mult(M[i][(j+1)%3],v[(j+1)%3])^mult(M[i][(j+2)%3],v[(j+2)%3]) for i,j in [(0,0),(1,0),(2,0)])
def invmat(A):
 a=[[A[i][j] for j in range(3)]+[int(i==j) for j in range(3)] for i in range(3)]
 for j in range(3):
  p=next((i for i in range(j,3) if a[i][j]),None)
  if p is None:return None
  a[j],a[p]=a[p],a[j]; x=inv[a[j][j]]
  a[j]=[mult(x,t) for t in a[j]]
  for k in range(3):
   if k!=j and a[k][j]:
    t=a[k][j];a[k]=[a[k][h]^mult(t,a[j][h]) for h in range(6)]
 return [r[3:] for r in a]
def normal(v):
 j=next(i for i in range(3) if v[i]); c=inv[v[j]]
 return tuple(mult(c,x) for x in v)
pts=[tuple((i>>j)&1 for j in range(3)) for i in range(1,8)]
idx={p:i for i,p in enumerate(pts)}
G=[]
for c in product(range(8),repeat=3):
 M=[[((c[j]>>i)&1) for j in range(3)] for i in range(3)]
 if invmat(M) is None:continue
 p=tuple(idx[matv(M,q)] for q in pts)
 G.append(p)
G=set(G)
assert len(G)==168

def compose(p,q):return tuple(p[q[i]] for i in range(7))
def cyc(p):
 seen=set();ans=[]
 for i in range(7):
  if i not in seen:
   j=i;c=0
   while j not in seen:seen.add(j);j=p[j];c+=1
   ans.append(c)
 return tuple(sorted(ans))
# choose non-collinear degree3 basis orbit
alpha=2
v=(1,alpha,mult(alpha,alpha))
sq=lambda x:mult(x,x)
orb=[v,tuple(sq(t) for t in v),tuple(sq(sq(t)) for t in v)]
H=[[orb[j][i] for j in range(3)] for i in range(3)]
Hi=invmat(H)
print('orbit',orb,'H',H,'invertible',Hi is not None)
def apply(v):
 x,y,z=matv(Hi,v)
 w=(mult(y,z),mult(x,z),mult(x,y))
 return normal(matv(H,w))
U=tuple(idx[apply(q)] for q in pts)
print('U',U,'cyc',cyc(U),'fixed',sum(i==U[i] for i in range(7)))
assert compose(U,U)==tuple(range(7))
P=set(compose(a,compose(U,b)) for a in G for b in G)
print('double coset',len(P),'types',sorted(Counter(map(cyc,P)).items()))
print('transpositions',sum(cyc(p)==(1,1,1,1,1,2) for p in P))
# compute generated group closure
H0=set(G)
# coset closure by U: after two quadratics, see if identity etc, bound 5040
queue=list(G); visited=set(G)
for p in queue:
 for q in (compose(U,p),)+(tuple(compose(g,p) for g in G)):
  if q not in visited:visited.add(q);queue.append(q)
print('generated',len(visited))
# distinct quadratic maps (should 1344), same images = 1344 via double coset
# classification by cycle type and parity
# identity / nonidentity comparison of permutations in G and P
print('P intersection G',len(P&G))
# Exhaustive permutation-level statements.
def sign(p):return (-1)**sum(1 for i in range(7) for j in range(i+1,7) if p[i]>p[j])
assert len(P)==1344
assert all(sign(p)==-1 for p in P)
assert not any(cyc(p)==(1,1,1,1,1,2) for p in P)
print('quadratic_certificate PASS; 1344 odd images; zero transpositions')
lines={frozenset(i for i in range(7) if sum(pts[i][k]*l[k] for k in range(3))%2==0) for l in pts}
assert len(lines)==7
def kept(p):return sum(frozenset(p[i] for i in l) in lines for l in lines)
assert kept(U)==0 and {kept(p) for p in P}=={0}
transpositions=[tuple(j if k==i else i if k==j else k for k in range(7)) for i in range(7) for j in range(i+1,7)]
assert {kept(p) for p in transpositions}=={3}
assert {kept(p) for p in G}=={7}
print('line_incidence_certificate PASS: projective 7; quadratic 0; transpositions 3')
