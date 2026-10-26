"""Independent finite-field factorization and Wronskian checks."""
import itertools,collections
from sympy import Poly,symbols
x=symbols('x');vlist=list(itertools.product(range(3),repeat=5));nz=vlist[1:]
parts={};roots={}
for v in nz:
 p=Poly(sum(v[i]*x**(4-i) for i in range(5)),x,modulus=3)
 k=next(i for i,z in enumerate(v) if z)
 fac=p.factor_list()[1]
 pa=([k] if k else []);S={('infinity',)} if k else set()
 for g,e in fac:
  pa.extend([int(e)]*g.degree());S.add(tuple(int(t)%3 for t in g.all_coeffs()))
 parts[v]=tuple(sorted(pa,reverse=True));roots[v]=S
allowed={(1,1,1,1),(2,1,1),(2,2),(4,)}
total=0;good=collections.Counter();count_four=0
for a in nz:
 for b in nz:
  if next(z for z in a+b if z)!=1 or roots[a]&roots[b]:continue
  total+=1
  fs=[b,a,tuple((u-z)%3 for u,z in zip(a,b)),tuple((u-2*z)%3 for u,z in zip(a,b))]
  ps=[parts[f] for f in fs]
  branch=sum(p!=(1,1,1,1) for p in ps)
  if branch<3 or any(p not in allowed for p in ps):continue
  r=sum(4-len(p) for p in ps)
  if r>6:continue
  if branch==4:
   count_four+=1;continue
  if r==6:
   good[tuple(sorted(ps))]+=1
  elif r==3 and tuple(sorted(ps))==((1,1,1,1),(2,1,1),(2,1,1),(2,1,1)):
   A=Poly(sum(a[i]*x**(4-i) for i in range(5)),x,modulus=3)
   B=Poly(sum(b[i]*x**(4-i) for i in range(5)),x,modulus=3)
   W=A.diff()*B-A*B.diff()
   fact=W.factor_list()[1]
   allpart=sorted([(g.degree(),int(e)) for g,e in fact]+ ([(1,6-W.degree())] if W.degree()<6 else []))
   if allpart==[(1,1),(1,1),(1,1),(3,1)]:good['cubic residual']+=1
assert total==17496
assert count_four==0
assert good[((1,1,1,1),(2,1,1),(2,2),(4,))]==576
assert good[((1,1,1,1),(2,2),(2,2),(2,2))]==96
assert good['cubic residual']==192
print('SYMBOlic EXACT:',total,'maps; b=3:',sum(good.values()),'; b=4:',count_four,dict(good))
