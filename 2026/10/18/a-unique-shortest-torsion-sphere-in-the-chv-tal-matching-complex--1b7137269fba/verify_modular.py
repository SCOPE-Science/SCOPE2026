from itertools import combinations
E=[(0,1),(0,4),(0,6),(0,9),(1,2),(1,5),(1,7),(2,3),(2,6),(2,8),(3,4),(3,7),(3,9),(4,5),(4,8),(5,10),(5,11),(6,10),(6,11),(7,8),(7,11),(8,10),(9,10),(9,11)]
conf=[0]*24
for i,a in enumerate(E):
 for j,b in enumerate(E):
  if set(a)&set(b):conf[i]|=1<<j
F=[[] for _ in range(6)]
def rec(f,j,b):
 if f:F[len(f)-1].append(tuple(f))
 for k in range(j,24):
  if not(b>>k&1):rec(f+[k],k+1,b|conf[k])
rec([],0,0)
def rank_mod(k,p):
 index={f:i for i,f in enumerate(F[k-1])};basis={}
 for top in F[k]:
  c={index[top[:j]+top[j+1:]]:(-1 if j%2 else 1)%p for j in range(len(top))}
  while c:
   i=max(c);v=c[i]
   if i not in basis:
    inv=pow(v,-1,p)
    basis[i]={j:v2*inv%p for j,v2 in c.items()};break
   b=basis[i]
   for j,v2 in b.items():
    c[j]=(c.get(j,0)-v*v2)%p
    if not c[j]:del c[j]
 return len(basis)
print('F_VECTOR',list(map(len,F)))
for p in (2,3,5,7):
 print('MOD',p,[(k,rank_mod(k,p)) for k in (3,4,5)])
