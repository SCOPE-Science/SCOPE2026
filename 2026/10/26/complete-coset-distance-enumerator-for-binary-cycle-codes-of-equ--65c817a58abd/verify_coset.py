from itertools import product
from collections import Counter
from math import comb

def mul(p,q):
 r=Counter()
 for a,c in p.items():
  for b,d in q.items():r[a+b]+=c*d
 return r

def powp(p,k):
 r={0:1}
 for _ in range(k):r=mul(r,p)
 return r

def add(p,q,s=1):
 r=Counter(p)
 for e,c in q.items():r[e]+=s*c
 return {e:c for e,c in r.items() if c}

def pol(m,L):
 h=(L-1)//2
 F=lambda j:{a:comb(L,a) for a in range(j+1)}
 top=F(h)
 G={a:2*comb(L,a) for a in range(h+1)}
 if L%2==0:G[L//2]=comb(L,L//2)
 # avoiding fraction: compose using integer division
 gpow=powp(G,m)
 assert all(v%(1<<(m-1))==0 for v in gpow.values())
 res={k:v//(1<<(m-1)) for k,v in gpow.items()}
 res=add(res,powp(top,m),-1)
 for j in range(h+1):
  w=add(powp(F(j),m),powp(F(j-1),m) if j else {},-1)
  res=add(res,{k+L-2*j:v for k,v in w.items()})
 return res

def brute(m,L):
 N=m*L
 C=[]
 for bits in product(range(2),repeat=m-1):
  b=list(bits)+[sum(bits)%2]
  cw=0
  for j,x in enumerate(b):
   if x:cw |= ((1<<L)-1)<<(j*L)
  C.append(cw)
 out=Counter()
 for x in range(1<<N):
  d=min((x^c).bit_count() for c in C)
  out[d]+=1
 assert all(v%len(C)==0 for v in out.values())
 return {k:v//len(C) for k,v in out.items()}

for m,L in [(4,2),(4,3),(4,4),(6,2)]:
 p=pol(m,L)
 b=brute(m,L)
 assert p==b,(m,L,p,b)
 print('VERIFIED m,L=',m,L,'cosets',sum(p.values()),'covering-radius',max(p),'deep-count',p[max(p)],'spectrum',sorted(p.items()))
for m in [4,6,8,10]:
 for L in range(2,13):
  p=pol(m,L)
  assert sum(p.values())==1<<(m*L-m+1)
  wantR=(m*L//2 if L%2==0 else m*((L-1)//2)+1)
  deep=(comb(L,L//2)**m//(1<<(m-1)) if L%2==0 else comb(L,(L-1)//2)**m)
  assert max(p)==wantR,(m,L,max(p),wantR)
  assert p[max(p)]==deep,(m,L,p[max(p)],deep)
  assert all(v>=0 for v in p.values())
print('VERIFY_OK')
