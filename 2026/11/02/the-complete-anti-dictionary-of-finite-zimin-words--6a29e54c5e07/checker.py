from collections import defaultdict

def zim(n):
 s=''
 for k in range(1,n+1):s+=chr(96+k)+s
 return s

def oracle_maw(s):
 # Independent adjacency/suffix-prefix construction, no formula assumptions.
 n=len(s); fs=[{''}]+[set(s[i:i+l] for i in range(n-l+1)) for l in range(1,n+1)]
 out=set()
 for m in range(2,n+2):
  L=defaultdict(set);R=defaultdict(set)
  for q in fs[m-1]:L[q[1:]].add(q[0]); R[q[:-1]].add(q[-1])
  for z in fs[m-2]:
   for a in L[z]:
    for b in R[z]:
     c=a+z+b
     if m==n+1 or c not in fs[m]:out.add(c)
 return out

def construction(n):
 Z=['']
 for j in range(1,n+1):Z.append(Z[-1]+chr(96+j)+Z[-1])
 out=set()
 for m in range(n):
  low=m+1
  out.add(chr(96+low)+Z[m]+chr(96+low))
  for i in range(m+2,n+1):
   for j in range(m+2,n+1):out.add(chr(96+i)+Z[m]+chr(96+j))
 return out

for n in range(1,10):
 s=zim(n);calc=construction(n);oracle=oracle_maw(s)
 assert calc==oracle,(n,len(calc),len(oracle),list(calc-oracle)[:3],list(oracle-calc)[:3])
 cnt={2**m+1:1+(n-m-1)**2 for m in range(n)}
 assert {l:sum(len(x)==l for x in oracle) for l in sorted(map(len,oracle))} ==cnt
 assert len(calc)==n+n*(n-1)*(2*n-1)//6
 for t in range(len(s)):
  pref=s[:t]
  possible={s[i+t] for i in range(len(s)-t) if s.startswith(pref,i)}
  if t==0:expected=set(s)
  else:
   m=(t+1).bit_length()-1
   expected={chr(96+j) for j in range(m+1,n+1)} if t==2**m-1 else {s[t]}
  assert possible==expected,(n,t,possible,expected)
 print('n',n,'length',len(s),'MAWs',len(oracle),'all-good')
print('SUCCESS')
