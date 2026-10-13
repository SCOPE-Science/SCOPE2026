from itertools import product

def spread_once(state,S,m,n):
 st=list(state); new=list(state)
 for v in range(m+n):
  if st[v]!=0: continue
  total=0
  if v<m:
   for j in range(n):
    if st[m+j]: total += S[v][j]*st[m+j]
  else:
   j=v-m
   for i in range(m):
    if st[i]: total += S[i][j]*st[i]
  if total>0:new[v]=1
  elif total<0:new[v]=-1
 return tuple(new)

def exact(S,m,n):
 best=0; memo={}
 def rec(state, first=False):
  # after an ignition; next round starts with one spread, then if unburned choose one ignition
  key=state
  if key in memo:return memo[key]
  ns=spread_once(state,S,m,n)
  if all(ns):
   val=max(ns.count(1),ns.count(-1));memo[key]=val;return val
  val=0
  for v,x in enumerate(ns):
   if x==0:
    for c in (-1,1):
     z=list(ns);z[v]=c
     val=max(val,rec(tuple(z)))
  memo[key]=val;return val
 for v in range(m+n):
  st=[0]*(m+n);st[v]=1
  best=max(best,rec(tuple(st)))
 return best

def formula(S,m,n):
 vals=[]
 for i in range(m):
  p=sum(x==1 for x in S[i]);q=n-p; pos=neg=zero=0
  for k in range(m):
   if k==i:continue
   d=sum(S[i][j]*S[k][j] for j in range(n))
   pos+=d>0; neg+=d<0; zero+=d==0
  vals.append(zero+max(1+p+pos+(1 if neg else 0), q+neg+(1 if pos else 0)))
 for j in range(n):
  p=sum(S[i][j]==1 for i in range(m));q=m-p;pos=neg=zero=0
  for l in range(n):
   if l==j:continue
   d=sum(S[i][j]*S[i][l] for i in range(m))
   pos+=d>0;neg+=d<0;zero+=d==0
  vals.append(zero+max(1+p+pos+(1 if neg else 0), q+neg+(1 if pos else 0)))
 return max(vals)

def mat(b,m,n):return [list(b[i*n:(i+1)*n]) for i in range(m)]
count=0
for m,n in [(2,2),(2,3),(3,2),(2,4),(4,2),(3,3)]:
 c=0
 for b in product((-1,1),repeat=m*n):
  S=mat(b,m,n);a=exact(S,m,n);f=formula(S,m,n)
  if a!=f: print('FAIL',m,n,S,a,f);raise SystemExit
  c+=1;count+=1
 print(m,n,c)
print('ALL CHECKS PASSED',count)
