from itertools import combinations

def all_posets(n):
  edges=list(combinations(range(n),2))
  for code in range(3**len(edges)):
   val=code; le=[1<<i for i in range(n)]
   for i,j in edges:
    tr=val%3; val//=3
    if tr==1: le[i]|=1<<j
    if tr==2: le[j]|=1<<i
   if any((le[i]>>j&1) and (le[j]&~le[i]) for i in range(n) for j in range(n)):continue
   yield le

def upsets(le):
 n=len(le); return [s for s in range(1<<n) if all(not(s>>i&1) or (le[i]&s)==le[i] for i in range(n))]
def connected(le):
 n=len(le); vis=0;cc=[]
 for i in range(n):
  if vis>>i&1:continue
  active=1<<i;old=0
  while active!=old:
   old=active
   for j in range(n):
    if active>>j&1:
     for k in range(n):
      if (le[j]>>k&1) or (le[k]>>j&1):active |=1<<k
  cc.append(active);vis|=active
 return cc

def check(le):
 n=len(le);full=(1<<n)-1; us=upsets(le)
 def neg(s):return sum(1<<i for i in range(n) if not(le[i]&s))
 top=sum(1<<i for i in range(n) if le[i]==1<<i)
 cs=connected(le); m=top.bit_count();c=len(cs)
 # Every component's upsets containing maxima are equivalent to upsets on nonmaximal induced P
 W=1
 for comp in cs:
  mx=comp&top; rem=comp&~top
  rp=sum(1 for s in range(1<<n) if s&~rem==0 and all(not(s>>i&1) or (le[i]&rem&s)==(le[i]&rem) for i in range(n)))
  W*=rp+1
 w=sum(1 for s in us if (neg(s)|neg(neg(s)))==full)
 d=sum(1 for s in us if neg(neg(s))==s)
 b=sum(1 for s in us if neg(neg(s))==s and (neg(s)|neg(neg(s)))==full)
 if (w,d,b)!=(W,1<<m,1<<c):return ('counts',le,us,(w,d,b),(W,1<<m,1<<c))
 # classify neither absent
 multim=[comp for comp in cs if (comp&top).bit_count()>=2]
 expected= not multim or (len(multim)==1 and all(comp==multim[0] or comp.bit_count()==1 for comp in cs) and all((le[i]&top)==(multim[0]&top) for i in range(n) if (multim[0]>>i&1) and not (top>>i&1)))
 actual= all((neg(s)|neg(neg(s)))==full or neg(neg(s))==s for s in us)
 if actual!=expected:return ('classification',le,us,actual,expected)
 return None
cnt=0
for n in range(1,6):
 for le in all_posets(n):
  bad=check(le)
  if bad:raise AssertionError(bad)
  cnt+=1
 print('checked n',n, 'cumulative',cnt)
print('VERIFY_OK all labelled posets <=5',cnt)
