from itertools import product
from collections import Counter
from math import comb

def graph(parts):
 N=sum(parts); p=[]
 for j,v in enumerate(parts):p.extend([j]*v)
 nn=2*N; adj=[set() for _ in range(nn)]
 for i in range(N):
  for j in range(i+1,N):
   if p[i]!=p[j]:adj[i].add(j);adj[j].add(i)
  adj[i].add(i+N);adj[i+N].add(i)
 return [sum(1<<v for v in a) for a in adj], p

def power(adj,mask):
 n=len(adj);obs=mask
 for i in range(n):
  if mask>>i&1:obs|=adj[i]
 while True:
  old=obs
  for i in range(n):
   if obs>>i&1:
    w=adj[i]&~obs
    if w and w&(w-1)==0:obs|=w
  if obs==old:break
 return obs==(1<<n)-1

def classification(parts,mask):
 N=sum(parts); pos=0;sstrong=[];passives=[];leaf_active=[]
 for i,a in enumerate(parts):
  strong=0;pas=0;active_leaves=0
  for j in range(pos,pos+a):
   c=(mask>>j)&1; l=(mask>>(N+j))&1
   strong+=c;pas+=(not(c or l));active_leaves+=l
  sstrong.append(strong);passives.append(pas);leaf_active.append(active_leaves);pos+=a
 nstrong=sum(x>0 for x in sstrong)
 if nstrong>=2:return True
 if nstrong==1:
  i=next(i for i,x in enumerate(sstrong) if x>0)
  return passives[i]==0 or (passives[i]==1 and sum(leaf_active[j] for j in range(len(parts)) if j!=i)>0)
 return sum(passives)==0 or sum(passives)==1 or (sum(passives)==2 and sum(p>0 for p in passives)==2)

def predicted(parts):
 N=sum(parts)
 def addpoly(a,b):
  m=max(len(a),len(b));return [ (a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(m)]
 def subpoly(a,b):return addpoly(a,[-v for v in b])
 def mul(a,b):
  out=[0]*(len(a)+len(b)-1)
  for i,x in enumerate(a):
   for j,y in enumerate(b):out[i+j]+=x*y
  return out
 def powpoly(a,k):
  o=[1]
  for _ in range(k):o=mul(o,a)
  return o
 def p1(n):return [comb(n,i) for i in range(n+1)]
 def strong(n):return subpoly(p1(2*n),p1(n))
 def shiftmono(n):return [0]*n+[1]
 def active(n):return powpoly([0,2,1],n)
 P=subpoly(p1(2*N),p1(N))
 for n in parts:P=subpoly(P,mul(strong(n),p1(N-n)))
 p_no=[0]*(2*N+1)
 p_no[N]+=1;p_no[N-1]+=N;p_no[N-2]+=sum(parts[i]*parts[j] for i in range(len(parts)) for j in range(i+1,len(parts)))
 P=addpoly(P,p_no)
 for n in parts:
  x0=subpoly(active(n),shiftmono(n))
  x1=[c*n for c in subpoly(active(n-1),shiftmono(n-1))]
  v=addpoly(mul(x0,p1(N-n)),mul(x1,subpoly(p1(N-n),[1])))
  P=addpoly(P,v)
 return P

if __name__=='__main__':
 total=0
 for parts in [(2,2),(2,3),(3,3),(2,2,2),(2,2,3),(2,3,3),(2,2,2,2)]:
  adj,p=graph(parts); got=Counter(); mismatches=[]
  for mask in range(1<<len(adj)):
   actual=power(adj,mask); assumed=classification(parts,mask)
   if actual!=assumed:mismatches.append((mask,actual,assumed))
   if actual:got[mask.bit_count()]+=1
  expect=predicted(parts)
  print(parts,'tested',1<<len(adj),'mismatch',len(mismatches),'coefs',got,'matches_poly',all(got[k]==v for k,v in enumerate(expect)), 'first bad',mismatches[:2]);total+=1<<len(adj)
 print('Total',total)
