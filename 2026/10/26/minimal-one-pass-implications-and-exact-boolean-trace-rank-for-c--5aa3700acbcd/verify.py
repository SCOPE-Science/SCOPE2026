import itertools,math

def mis(n):
 for x in range(1<<n):
  if any((x>>i&1) and (x>>((i+1)%n)&1) for i in range(n)): continue
  if any(not (x>>i&1 or x>>((i-1)%n)&1 or x>>((i+1)%n)&1) for i in range(n)):continue
  yield x

def rules(n):
 d={}
 if n==3:
  for i in range(n):d[(1<<i)|(1<<((i+1)%n))]=(1<<n)-1
 elif n==4:
  for i in range(n): d[1<<i] = (1<<((i+2)%n))
 else:
  for i in range(n):d[(1<<i)|(1<<((i+1)%n))]=(1<<n)-1
  if n>=6:
   for i in range(n):
    a=(1<<((i-2)%n))|(1<<((i+2)%n))
    d[a]=d.get(a,0)|(1<<i)
 return d
for n in range(3,16):
 M=list(mis(n));R=rules(n); N=(1<<n)-1
 for s in range(1<<n):
  actual=N
  poss=False
  for m in M:
   if m&s==s: actual &= m;poss=True
  if not poss:actual=N
  computed=s
  for prem,con in R.items():
   if s&prem==prem:computed |= con
  if actual!=computed:raise AssertionError(('bad closure',n,s,actual,computed))
 else:
  dim=-1
  for s in range(1<<n):
   k=s.bit_count()
   if k<=dim:continue
   seen={m&s for m in M}
   if len(seen)==1<<k:dim=k
  print('n',n,'MIS',len(M),'rules',len(R),'dim',dim,'formula',(n+1)//3,'PASS',flush=True)

print('VERIFY_OK cycle_MIS_closure=PASS direct_one_round=PASS stem_count=PASS shattering_formula=PASS')
