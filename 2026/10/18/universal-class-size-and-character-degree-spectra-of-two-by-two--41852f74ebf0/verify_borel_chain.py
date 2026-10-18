from collections import Counter

def ring(p,m,model):
 N=p**m
 def add(a,b):
  if model=='residue':return (a+b)%N
  v=0;P=1
  for i in range(m): v+=(((a//P)%p+(b//P)%p)%p)*P;P*=p
  return v
 def mul(a,b):
  if model=='residue':return (a*b)%N
  aa=[(a//p**i)%p for i in range(m)]; bb=[(b//p**i)%p for i in range(m)]
  return sum((sum(aa[j]*bb[i-j] for j in range(i+1))%p)*p**i for i in range(m))
 def sub(a,b):
  if model=='residue': return (a-b)%N
  return sum((((a//p**i)%p-(b//p**i)%p)%p)*p**i for i in range(m))
 def val(x):
  if not x:return m
  if model=='residue':
   t=0
   while x%p==0:t+=1;x//=p
   return t
  t=0
  while (x//p**t)%p==0:t+=1
  return t
 return range(N),add,mul,sub,val

def test(p,m,model):
 R,add,mul,sub,val=ring(p,m,model);units=[a for a in R if val(a)==0]; U=len(units)
 G=[(a,b,d) for a in units for b in R for d in units]
 sizes=Counter(); theoretical=Counter()
 for a,b,d in G:
  Δ=sub(a,d); alpha=val(Δ); beta=val(b)
  cls=(p**(m-alpha)) if beta>=alpha else (p-1)*p**(m-1-beta)
  theoretical[cls]+=1
  cent=sum(1 for x,y,z in G if add(mul(a,y),mul(b,z))==add(mul(x,b),mul(y,d)))
  assert len(G)%cent==0, (p,m,model,a,b,d,cent)
  s=len(G)//cent
  assert s==cls, (p,m,model,(a,b,d),s,cls)
  sizes[s]+=1
 # explicit orbit count from dual action
 degree=Counter()
 visited=set()
 for c in R:
  if c in visited: continue
  orbit={mul(u,c) for u in units};visited|=orbit
  degree[len(orbit)]+=U*(U//len(orbit))
 # check expected character degree
 expected_degree=Counter()
 expected_degree[1]+=U*U
 for t in range(m):expected_degree[(p-1)*p**(m-t-1)]+=U*p**t
 assert degree==expected_degree,('degree',degree,expected_degree)
 assert sum(v*s*s for s,v in degree.items())==len(G)
 v0=(p-2)*p**(m-1)
 expected_classes=Counter()
 for alpha in range(m+1):
  va=(v0 if alpha==0 else ((p-1)*p**(m-alpha-1) if alpha<m else 1))
  expected_classes[p**(m-alpha)]+=U*va
 for beta in range(m):
  expected_classes[(p-1)*p**(m-1-beta)]+=U*p**(m-beta-1)
 class_counts=Counter({s:(v//s) for s,v in sizes.items()})
 assert all(v%s==0 for s,v in sizes.items())
 assert class_counts==expected_classes, ('classes',class_counts,expected_classes)
 print('PASS',p,m,model,'group',len(G),'classes',sum(class_counts.values()),'class spectrum',sorted(class_counts.items()),'character degrees',sorted(degree.items()))

if __name__=='__main__':
 for p,m,model in [(2,1,'residue'),(3,1,'residue'),(2,2,'residue'),(2,2,'polynomial'),(2,3,'residue'),(2,3,'polynomial'),(2,4,'residue'),(3,2,'residue'),(3,2,'polynomial'),(5,1,'residue')]:test(p,m,model)
 print('VERIFY_OK_BOREL_CHAIN_DUAL_SPECTRA')
