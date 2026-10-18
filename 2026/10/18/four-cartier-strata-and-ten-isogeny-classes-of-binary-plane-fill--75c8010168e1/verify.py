#!/usr/bin/env python3
import itertools, collections, sympy as S, time
X,Y,Z=S.symbols('X Y Z'); vars=(X,Y,Z)
Mons=sorted([(a,b,5-a-b) for a in range(6) for b in range(6-a)],reverse=True)
index={m:i for i,m in enumerate(Mons)}
pts=[i for i in range(1,8)]
# Polynomial on rational point mod 2 (homogeneous)
E=[[int(all((i>>j)&1 for j,e in enumerate(m) if e)) for m in Mons] for i in pts]
# RREF rows for evaluation
rows=[sum(v<<i for i,v in enumerate(row)) for row in E]
pivot=[];basis=[]
for row in rows:
 for p,rr in zip(pivot,basis):
  if (row>>p)&1: row^=rr
 if row:
  p=(row&-row).bit_length()-1
  for j,rr in enumerate(basis):
   if (rr>>p)&1: basis[j]^=row
  pivot.append(p);basis.append(row)
free=[j for j in range(21) if j not in pivot]
K=[]
for f in free:
 v=1<<f
 for p,rr in zip(pivot,basis):
  if (rr>>f)&1:v^=1<<p
 assert all(bin(v & rr).count('1')%2==0 for rr in rows)
 K.append(v)
assert len(K)==14

def mul(p,q):
 out={}
 for a,c in p.items():
  for b,d in q.items():
   m=tuple(x+y for x,y in zip(a,b))
   out[m]=out.get(m,0)^(c&d)
 return {m:b for m,b in out.items() if b}

def transmap(B):
 L=[{tuple(int(k==j) for k in range(3)):B[i][j] for j in range(3) if B[i][j]} for i in range(3)]
 out=[]
 for m in Mons:
  prod={(0,0,0):1}
  for j,e in enumerate(m):
   for _ in range(e): prod=mul(prod,L[j])
  out.append(sum(1<<index[mm] for mm in prod))
 return out

def trans(v, T):
 res=0
 while v:
  b=v&-v;i=b.bit_length()-1;res^=T[i];v^=b
 return res
Ts=[transmap([[0,1,0],[1,0,0],[0,0,1]]),transmap([[1,0,0],[0,0,1],[0,1,0]]),transmap([[1,1,0],[0,1,0],[0,0,1]])]
# Validate kernel invariant
assert all(all(bin(trans(v,T)&rr).count('1')%2==0 for rr in rows) for T in Ts for v in K)
allforms=[]
for s in range(1,1<<14):
 v=0
 for i,b in enumerate(K):
  if (s>>i)&1: v^=b
 allforms.append(v)
assert len(set(allforms))==16383
unseen=set(allforms);orbits=[]
while unseen:
 v=min(unseen);orb={v};work=[v]
 for a in work:
  for T in Ts:
   b=trans(a,T)
   if b not in orb:orb.add(b);work.append(b)
 assert orb<=unseen
 unseen-=orb
 orbits.append((v,len(orb)))
print('all orbits',len(orbits),'orbit histogram',collections.Counter(s for _,s in orbits),flush=True)

def poly(v):
 return S.Add(*[X**a*Y**b*Z**c for i,(a,b,c) in enumerate(Mons) if (v>>i)&1])

def smooth(v):
 F=poly(v);grad=[S.diff(F,x) for x in vars]
 for i,x in enumerate(vars):
  others=[w for w in vars if w!=x]
  gs=S.groebner([p.subs(x,1) for p in grad],*others,order='grevlex',modulus=2)
  if not gs.is_zero_dimensional and (len(gs.polys)!=1 or gs.polys[0].as_expr()!=1): return False
  if len(gs.polys)!=1 or gs.polys[0].as_expr()!=1:return False
 return True

start=time.time();so=[]
for j,(v,size) in enumerate(orbits):
 if smooth(v):
  so.append((v,size));print('smooth orbit',len(so),size,'mask',v,'elapsed',round(time.time()-start,2),flush=True)
print('smooth total',sum(s for _,s in so),'orbits',len(so),flush=True)
assert len(so)==10 and sum(s for _,s in so)==1512

def mat(v):
 basis2=[(a,b,2-a-b) for a in range(3) for b in range(3-a)]
 six=len(basis2)
 H=[[0]*six for _ in range(six)]
 for i,a in enumerate(basis2):
  for j,b in enumerate(basis2):
   m=tuple(2*a[k]-b[k]+1 for k in range(3))
   if all(x>=0 for x in m):H[i][j]=(v>>index[m])&1
 return H

def rank(A):
 n=len(A);rows=[sum(t<<i for i,t in enumerate(row)) for row in A];r=0
 for j in range(n):
  ind=next((i for i in range(r,n) if (rows[i]>>j)&1),None)
  if ind is not None:
   rows[r],rows[ind]=rows[ind],rows[r]
   for k in range(n):
    if k!=r and ((rows[k]>>j)&1):rows[k]^=rows[r]
   r+=1
 return r

def mm(A,B):return [[sum(a&b for a,b in zip(row,col))&1 for col in zip(*B)] for row in A]
for v,s in so:
 H=mat(v);A=H;rr=[]
 for n in range(1,8):
  rr.append(rank(A));A=mm(A,H)
 print('arithmetic',v,s,'ranks',rr,'F=',str(poly(v)),flush=True)
mods={1:0b11,2:0b111,3:0b1011,4:0b10011,5:0b100101,6:0b1000011}
def fm(a,b,n):
 if n==1:return a&b
 out=0;poly=mods[n]
 while b:
  if b&1:out^=a
  a<<=1
  if (a>>n)&1:a^=poly
  b>>=1
 return out

def powf(a,e,n):
 out=1
 while e:
  if e&1:out=fm(out,a,n)
  a=fm(a,a,n);e>>=1
 return out

def pointcnt(v,n):
 q=2**n
 powcache=[[powf(x,e,n) for e in range(6)] for x in range(q)]
 num=0
 for yy in range(q):
  for zz in range(q):
   val=0
   for i,(a,b,c) in enumerate(Mons):
    if (v>>i)&1:
     val^=fm(powcache[yy][b],powcache[zz][c],n)
   num+=val==0
 for zz in range(q):
  val=0
  for i,(a,b,c) in enumerate(Mons):
   if a==0 and ((v>>i)&1):val^=fm(powcache[1][b],powcache[zz][c],n)
  num+=val==0
 num+=((v>>index[(0,0,5)])&1)==0
 return num

def lp(v):
 N=[pointcnt(v,n) for n in range(1,7)]
 s=[0]+[(1<<i)+1-N[i-1] for i in range(1,7)]
 c=[1]
 for k in range(1,7):
  tot=sum(c[k-i]*s[i] for i in range(1,k+1))
  assert tot%k==0
  c.append(-tot//k)
 c.extend([0]*6)
 for i in range(6):c[12-i]=(1<<(6-i))*c[i]
 return N,c
certificates=[]
for v,size in so:
 N,C=lp(v)
 print('zeta',v,size,'N',N,'C',C,flush=True)
 H=mat(v);qrank=next(r for r in reversed([rank(__import__('functools').reduce(mm,[H]*n)) for n in range(1,8)]))
 assert max(i for i,c in enumerate(C) if c%2)==qrank
 certificates.append((v,size,qrank,6-rank(H),tuple(C)))
assert len({c[-1] for c in certificates})==10
assert collections.Counter((f,a) for v,s,f,a,c in certificates)=={(2,3):1,(2,1):2,(5,1):2,(6,0):5}
assert {(f,a):sum(s for v,s,ff,aa,c in certificates if (ff,aa)==(f,a)) for _,_,f,a,_ in certificates}=={(2,3):168,(2,1):252,(5,1):336,(6,0):756}
print('CERTIFIED: 1512 smooth equations, ten distinct zeta polynomials, and complete Cartier stratification')
