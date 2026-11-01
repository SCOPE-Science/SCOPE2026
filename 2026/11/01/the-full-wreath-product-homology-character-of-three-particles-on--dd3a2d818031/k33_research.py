#!/usr/bin/env python3
"""Exact weight-three reduced graph-chain computation for K3,3."""
import itertools,collections,math,json,time
from functools import lru_cache
V=range(6)
E=tuple((a,b) for a in range(3) for b in range(3,6))
INC={v:tuple(i for i,e in enumerate(E) if v in e) for v in V}
K=9

def expm(k,n):
 if k==1:yield (n,);return
 for j in range(n+1):
  for t in expm(k-1,n-j):yield (j,)+t

def bases(n=3):
 out=[]
 for q in range(n+1):
  b=[]
  for vv in itertools.combinations(V,q):
   for cc in itertools.product((1,2),repeat=q):
    for ee in expm(K,n-q):b.append((vv,cc,ee))
  out.append(tuple(b))
 return out
B=bases()
IND=[{b:i for i,b in enumerate(bb)} for bb in B]

def boundary_col(q,c):
 vv,cc,ee=c
 for j,v in enumerate(vv):
  for sign,e in [(1,INC[v][cc[j]]),(-1,INC[v][0])]:
   ne=list(ee);ne[e]+=1
   target=(vv[:j]+vv[j+1:],cc[:j]+cc[j+1:],tuple(ne))
   yield IND[q-1][target],sign*(-1)**j

def rank_mod(cols,p):
 piv={}
 for column in cols:
  vec=collections.defaultdict(int)
  for i,a in column:vec[i]=(vec[i]+a)%p
  while vec:
   row=min(vec)
   val=vec[row]%p
   if not val:del vec[row];continue
   if row not in piv:
    iv=pow(val,-1,p)
    piv[row]={i:(x*iv)%p for i,x in vec.items() if x%p}
    break
   base=piv[row]
   for i,x in base.items():vec[i]=(vec.get(i,0)-val*x)%p
   vec={i:x for i,x in vec.items() if x}
 return len(piv)

def inv_sign(s):
 return -1 if sum(s[i]>s[j] for i in range(len(s)) for j in range(i+1,len(s)))%2 else 1

def group():
 for l in itertools.permutations(range(3)):
  for r in itertools.permutations(range(3)):
   for t in (0,1):
    if t==0:g=l+tuple(3+x for x in r)
    else:g=tuple(3+x for x in l)+r
    yield (l,r,t),g

def symtrace(g,q):
 tr=0
 perm=[E.index(tuple(sorted((g[a],g[b])))) for a,b in E]
 for vv,cc,ee in B[q]:
  if vv and tuple(sorted(g[x] for x in vv))!=vv:continue
  if any(ee[i]!=ee[perm[i]] for i in range(K)):continue
  gg=tuple(g[x] for x in vv)
  sign=inv_sign(gg)
  coeff=1
  for v,c in zip(vv,cc):
   dest=g[v];d=cc[vv.index(dest)]
   ec=perm[INC[v][c]];e0=perm[INC[v][0]]
   coeff*=int(ec==INC[dest][d])-int(e0==INC[dest][d])
   if coeff==0:break
  tr+=sign*coeff
 return tr

def graphcycletrace(g):
 # C1 (edge orientation L to R), minus C0, plus H0
 vv=sum(g[v]==v for v in V)
 ee=sum(tuple(sorted((g[a],g[b])))==(a,b) and (1 if g[a]<3 else -1) for a,b in E)
 return ee-vv+1

def main():
 st=time.time()
 print('chain dimensions',tuple(map(len,B)),flush=True)
 rs={}
 for q in (1,2,3):
  for p in (101,103):
   cols=(boundary_col(q,c) for c in B[q])
   r=rank_mod(cols,p)
   print('rank',q,'mod',p,r,'time',round(time.time()-st,2),flush=True)
   if p==101:rs[q]=r

 for q in (2,3):
  for c in B[q]:
   acc=collections.Counter()
   for i,a in boundary_col(q,c):
    for j,b in boundary_col(q-1,B[q-1][i]):acc[j]+=a*b
   assert all(x==0 for x in acc.values())
 print('boundary-square-zero all degree 2 and 3 columns')
 assert rs=={1:164,2:372,3:160}
 print('betti (finite field)',(len(B[0])-rs[1],len(B[1])-rs[1]-rs[2],len(B[2])-rs[2]-rs[3],len(B[3])-rs[3]))
 result=[]
 for params,g in group():
  ts=tuple(symtrace(g,q) for q in range(4))
  chi=sum((-1)**q*ts[q] for q in range(4))
  h1=graphcycletrace(g)
  h2=chi-1+h1
  l,r,t=params
  def stdtrace(p):return sum(i==p[i] for i in range(3))-1
  def sg(p):return inv_sign(p)
  if t==0:
   expect_h1=stdtrace(l)*stdtrace(r)
   expect_h2=expect_h1+sg(l)*stdtrace(r)+stdtrace(l)*sg(r)
  else:
   comp=tuple(r[l[i]] for i in range(3))
   expect_h1=expect_h2=-stdtrace(comp)
  assert (h1,h2)==(expect_h1,expect_h2),(params,(h1,h2),(expect_h1,expect_h2))
  result.append({'parameters':params,'permutation':g,'chain_traces':ts,'H1_trace':h1,'H2_trace':h2})
 classes=collections.defaultdict(lambda:collections.Counter())
 for d in result:
  l,r,t=d['parameters']
  def cyc(p):
   seen=set(); out=[]
   for i in range(3):
    if i in seen:continue
    k=i;ct=0
    while k not in seen:seen.add(k);ct+=1;k=p[k]
    out.append(ct)
   return tuple(sorted(out))
  if not t:key=(0,cyc(l),cyc(r))
  else:
   comp=tuple(r[l[i]] for i in range(3))
   key=(1,cyc(comp))
  classes[key][(d['H1_trace'],d['H2_trace'])]+=1
 print('class character:',flush=True)
 for k,v in sorted(classes.items()):print(k,dict(v),flush=True)
 assert all(len(d)==1 for d in classes.values())
 assert result[0]['H1_trace']==4 and result[0]['H2_trace']==8
 print('dims',len(result),'H1fixed',sum(d['H1_trace'] for d in result)//72,'H2fixed',sum(d['H2_trace'] for d in result)//72,'time',round(time.time()-st,2))
 print('All 72 element characters match the two stated W representations; VERIFY_OK')
if __name__=='__main__':main()
