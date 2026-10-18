"""Finite verification of the nucleus composition stabilization theorem."""
import itertools

def posets(n):
 pairs=list(itertools.combinations(range(n),2))
 for choices in itertools.product((0,1,2), repeat=len(pairs)):
  leq=[[i==j for j in range(n)] for i in range(n)]
  for (i,j),d in zip(pairs,choices):
   if d==1:leq[i][j]=True
   if d==2:leq[j][i]=True
  if any(leq[i][j] and leq[j][k] and not leq[i][k] for i in range(n) for j in range(n) for k in range(n)):
   continue
  yield leq

def height(leq):
 n=len(leq)
 return max((sum(1 for x in range(n) if leq[x][y]) for y in range(n)),default=0) if False else max((len(c) for r in range(1,n+1) for c in itertools.permutations(range(n),r) if all(leq[c[i]][c[i+1]] for i in range(r-1))), default=0)

def upsets(leq):
 n=len(leq)
 return [U for U in range(1<<n) if all(not (U>>x&1 and leq[x][y]) or U>>y&1 for x in range(n) for y in range(n))]

def nucleus(S,U,leq):
 n=len(leq);out=0
 for x in range(n):
  if all(not(S>>y&1 and leq[x][y]) or U>>y&1 for y in range(n)):out|=1<<x
 return out

def core_bridged(S,T,leq):
 n=len(leq);C=S&T
 return all(not((S>>s)&1 and (T>>t)&1 and leq[s][t]) or any(C>>c&1 and leq[s][c] and leq[c][t] for c in range(n)) for s in range(n) for t in range(n))

def core_path(S,T,r,leq):
 n=len(leq);C=S&T
 # All 2r alternating paths s,t,s,t,... must pass over at least one c in C between endpoints
 def rec(last,d,first):
  if d==2*r:
   return any(C>>c&1 and leq[first][c] and leq[c][last] for c in range(n))
  V=S if d%2==0 else T
  return all(rec(y,d+1,first if d else y) for y in range(n) if V>>y&1 and (d==0 or leq[last][y]))
 return rec(0,0,0)

checks=0;posets_count=0;pathchecks=0
for n in range(1,5):
 for leq in posets(n):
  posets_count+=1;ups=upsets(leq);h=height(leq)
  nuclei={(S,U):nucleus(S,U,leq) for S in range(1<<n) for U in ups}
  for S in range(1<<n):
   for T in range(1<<n):
    C=S&T
    F={U:nuclei[S,nuclei[T,U]] for U in ups}
    expected={U:nuclei[C,U] for U in ups}
    assert (F==expected)==core_bridged(S,T,leq)
    comp={U:U for U in ups}
    for r in range(1,h//2+2):
     comp={U:F[comp[U]] for U in ups}
     assert (comp==expected)==core_path(S,T,r,leq)
     pathchecks+=1
    assert comp==expected
    checks+=1
 print('n',n,'posets',sum(1 for _ in posets(n)),'pairs checked cumulative',checks)
print('VERIFY_OK',posets_count,'labelled-posets',checks,'nucleus-pairs',pathchecks,'power/path identities')
