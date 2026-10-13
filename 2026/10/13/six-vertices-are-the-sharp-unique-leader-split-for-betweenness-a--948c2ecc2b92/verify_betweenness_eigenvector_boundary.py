from fractions import Fraction
import math, json, time

def trim(p):
    while len(p)>1 and p[-1]==0: p.pop()
    return p

def peval(p,x):
    y=Fraction(0)
    for c in reversed(p): y=y*x+c
    return y

def pder(p): return trim([Fraction((i+1)*p[i+1]) for i in range(len(p)-1)] or [Fraction(0)])
def pdivmod(a,b):
    a=[Fraction(x) for x in a]; b=trim([Fraction(x) for x in b])
    if len(b)==1 and b[0]==0: raise ZeroDivisionError
    q=[Fraction(0)]*max(1,(len(a)-len(b)+1))
    while len(a)>=len(b) and not (len(a)==1 and a[0]==0):
        k=len(a)-len(b); c=a[-1]/b[-1]; q[k]=c
        for i in range(len(b)): a[i+k]-=c*b[i]
        trim(a)
    return trim(q),trim(a)
def pneg(p): return [-x for x in p]
def pgcd(a,b):
    a=trim([Fraction(x) for x in a]); b=trim([Fraction(x) for x in b])
    while not(len(b)==1 and b[0]==0):
        _,r=pdivmod(a,b); a,b=b,r
    if len(a)==1 and a[0]==0:return [Fraction(0)]
    lc=a[-1]; return trim([x/lc for x in a])
def sturm(p):
    p=trim([Fraction(x) for x in p]); seq=[p,pder(p)]
    while not(len(seq[-1])==1 and seq[-1][0]==0):
        _,r=pdivmod(seq[-2],seq[-1])
        if len(r)==1 and r[0]==0: break
        seq.append(pneg(r))
    return seq
def variations(seq,x):
    s=[]
    for p in seq:
        v=peval(p,x)
        if v>0:s.append(1)
        elif v<0:s.append(-1)
    return sum(s[i]!=s[i-1] for i in range(1,len(s)))
def roots_between(seq,a,b): return variations(seq,a)-variations(seq,b)

def matmul(A,B):
 n=len(A);return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
def charpoly(A): # ascending coeffs
 n=len(A)
 if n==0:return [1]
 I=[[int(i==j) for j in range(n)] for i in range(n)]
 P=[row[:] for row in A]
 tr=[None]+[sum(P[i][i] for i in range(n))]
 for k in range(2,n+1):
  P=matmul(P,A);tr.append(sum(P[i][i] for i in range(n)))
 c=[Fraction(1)]
 for k in range(1,n+1):
  s=sum(c[k-i]*tr[i] for i in range(1,k+1))
  c.append(-s/Fraction(k))
 # descending: 1,c1,...cn ; convert ascending cn,...,1
 assert all(x.denominator==1 for x in c)
 return [int(x) for x in reversed(c)]

def delete_vertex(A,v): return [[A[i][j] for j in range(len(A)) if j!=v] for i in range(len(A)) if i!=v]

def isolate_perron(p,n):
 seq=sturm(p); U=Fraction(n); a=Fraction(0); b=U
 # if 0 maybe root okay; find interval by bisection based roots above mid
 for _ in range(80):
  m=(a+b)/2
  pm=peval(p,m)
  if pm==0:
   # if no roots above, exact perron
   if roots_between(seq,m,b)==0:return ('exact',m,seq)
   a=m;continue
  cnt=roots_between(seq,m,b)
  if cnt>=1:a=m
  else:b=m
  if roots_between(seq,a,b)==1 and b-a < Fraction(1,1<<20):
   return ('interval',(a,b),seq)
 raise RuntimeError('isolate')

def cmp_at_perron(p, rootinfo, d):
 # sign d(lambda)
 if all(x==0 for x in d):return 0
 typ,val,_=rootinfo
 if typ=='exact':
  z=peval(d,val); return (z>0)-(z<0)
 a,b=val
 g=pgcd(p,d)
 if len(g)>1:
  gs=sturm(g)
  if roots_between(gs,a,b)>0:return 0
 ds=sturm(d)
 for _ in range(100):
  if roots_between(ds,a,b)==0:
   z=peval(d,(a+b)/2);return (z>0)-(z<0)
  m=(a+b)/2
  ps=sturm(p)
  if roots_between(ps,m,b)>=1:a=m
  else:b=m
 raise RuntimeError('cmp')

def ec_rel(A):
 n=len(A);p=charpoly(A);ri=isolate_perron(p,n)
 qs=[charpoly(delete_vertex(A,i)) for i in range(n)]
 # compare q_i pairwise to find maximizers
 win=[]
 for i in range(n):
  ok=True
  for j in range(n):
   if i==j:continue
   L=max(len(qs[i]),len(qs[j]));d=[0]*L
   for k in range(L):d[k]=(qs[i][k] if k<len(qs[i]) else 0)-(qs[j][k] if k<len(qs[j]) else 0)
   if cmp_at_perron(p,ri,d)<0:ok=False;break
  if ok:win.append(i)
 return win,p,ri

def Afrom(n,mask):
 A=[[0]*n for _ in range(n)];k=0
 for i in range(n):
  for j in range(i+1,n):
   if mask>>k&1:A[i][j]=A[j][i]=1
   k+=1
 return A


from pathlib import Path
from itertools import permutations
from collections import Counter
from fractions import Fraction
import json, math
ATLAS=Path(__file__).with_name('graph_atlas_connected_2to6.json')
EXPECTED_COUNTS={2:1,3:2,4:6,5:21,6:112}
EXPECTED_CLASSES={2:0,3:0,4:0,5:0,6:7}
EXPECTED={
 28679:(0,3,4,180),4909:(1,0,1,720),21225:(4,1,1,720),4857:(0,1,1,720),
 29481:(1,5,2,360),31458:(2,3,2,360),13117:(3,0,1,720)
}
def epairs(n): return [(i,j) for i in range(n) for j in range(i+1,n)]
def pmask(n,mask,p):
 ps=epairs(n); idx={e:i for i,e in enumerate(ps)}; out=0
 for k,(i,j) in enumerate(ps):
  if mask>>k&1:
   a,b=sorted((p[i],p[j])); out|=1<<idx[(a,b)]
 return out
def aut_order(n,mask): return sum(pmask(n,mask,p)==mask for p in permutations(range(n)))
def edge_list(n,mask): return [e for k,e in enumerate(epairs(n)) if mask>>k&1]

def betweenness_brandes(A):
 n=len(A); b=[Fraction(0) for _ in range(n)]
 for s in range(n):
  dist=[-1]*n; sigma=[0]*n; pred=[[] for _ in range(n)]
  dist[s]=0; sigma[s]=1; Q=[s]; S=[]
  for v in Q:
   S.append(v)
   for w,a in enumerate(A[v]):
    if not a: continue
    if dist[w]<0: dist[w]=dist[v]+1; Q.append(w)
    if dist[w]==dist[v]+1: sigma[w]+=sigma[v]; pred[w].append(v)
  delta=[Fraction(0) for _ in range(n)]
  for w in reversed(S):
   for v in pred[w]: delta[v]+=Fraction(sigma[v],sigma[w])*(1+delta[w])
   if w!=s: b[w]+=delta[w]
 return [x/2 for x in b]

def bfs_counts(A,s):
 n=len(A); d=[-1]*n; sig=[0]*n; d[s]=0; sig[s]=1; Q=[s]
 for v in Q:
  for w,a in enumerate(A[v]):
   if not a: continue
   if d[w]<0: d[w]=d[v]+1; Q.append(w)
   if d[w]==d[v]+1: sig[w]+=sig[v]
 return d,sig

def betweenness_pairwise(A):
 n=len(A); ds=[]; sig=[]
 for s in range(n):
  d,q=bfs_counts(A,s); ds.append(d); sig.append(q)
 b=[Fraction(0) for _ in range(n)]
 for s in range(n):
  for t in range(s+1,n):
   for v in range(n):
    if v==s or v==t: continue
    if ds[s][v]+ds[v][t]==ds[s][t]:
     b[v]+=Fraction(sig[s][v]*sig[v][t],sig[s][t])
 return b

rows=json.loads(ATLAS.read_text(encoding='utf-8'))
counts=Counter(r['n'] for r in rows); assert dict(sorted(counts.items()))==EXPECTED_COUNTS
cc=Counter(); bad=[]
for r in rows:
 n,mask=r['n'],r['mask']
 if n>6: continue
 A=Afrom(n,mask)
 b1=betweenness_brandes(A); b2=betweenness_pairwise(A); assert b1==b2
 mb=max(b1); bw=[i for i,x in enumerate(b1) if x==mb]
 ew,_,_=ec_rel(A)
 if len(bw)==1 and len(ew)==1 and bw[0]!=ew[0]:
  cc[n]+=1; bad.append((n,mask,bw[0],ew[0],b1))
assert {n:cc[n] for n in range(2,7)}==EXPECTED_CLASSES
assert {m for n,m,b,e,z in bad if n==6}==set(EXPECTED)
for n,mask,bh,eh,b in bad:
 eb,ee,ea,eo=EXPECTED[mask]; assert (bh,eh)==(eb,ee)
 a=aut_order(n,mask); assert a==ea and math.factorial(n)//a==eo
assert sum(v[3] for v in EXPECTED.values())==3780
total_labeled_6=sum(math.factorial(6)//aut_order(6,r['mask']) for r in rows if r['n']==6)
assert total_labeled_6==26704
print('VERIFY_OK')
print('connected_unlabeled',dict(sorted(counts.items())))
print('conflict_classes',{n:cc[n] for n in range(2,7)})
print('labeled_connected_6',total_labeled_6)
print('labeled_first_conflicts',3780)
for n,mask,bh,eh,b in sorted(bad,key=lambda z:z[1]):
 print('class',mask,'edges',edge_list(n,mask),'betweenness_leader',bh,'betweenness',b[bh],
       'eigenvector_leader',eh,'aut',EXPECTED[mask][2],'orbit',EXPECTED[mask][3])
