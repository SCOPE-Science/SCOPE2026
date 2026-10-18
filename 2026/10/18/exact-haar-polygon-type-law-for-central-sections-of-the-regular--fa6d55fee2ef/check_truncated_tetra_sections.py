import itertools,collections,math
A=[(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]
V=[tuple(2*a+b for a,b in zip(A[i],A[j])) for i in range(4) for j in range(4) if i!=j]
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def mul(k,a):return tuple(k*x for x in a)
def sig(t):return 1 if t>0 else (-1 if t<0 else 0)
assert len(V)==12 and all(dot(v,v)==11 for v in V)
pairs=list(itertools.combinations(range(12),2))
assert all(dot(V[k],cross(V[i],V[j]))!=0 for i,j,k in itertools.combinations(range(12),3))
E=[(i,j) for i,j in pairs if dot(add(V[i],mul(-1,V[j])),add(V[i],mul(-1,V[j])))==8]
assert len(E)==18
signatures={}
for i,j in pairs:
 x=cross(V[i],V[j]); c=dot(V[i],V[j]);assert abs(c) in (1,5,7,9)
 for orient in (-1,1):
  xx=mul(orient,x)
  for si,sj in itertools.product((-1,1),repeat=2):
   d=add(mul(si,add(mul(11,V[i]),mul(-c,V[j]))),mul(sj,add(mul(11,V[j]),mul(-c,V[i]))))
   u=add(mul(10000,xx),d)
   S=tuple(sig(dot(v,u)) for v in V)
   assert all(S) and S[i]==si and S[j]==sj
   assert all(S[k]==sig(dot(V[k],xx)) for k in range(12) if k not in (i,j))
   signatures[S]=u
assert len(signatures)==134
assert len({S for S in signatures})==134
C=collections.Counter();types=collections.Counter();coefN=collections.defaultdict(lambda:[0]*5); patterns=collections.defaultdict(collections.Counter);observed_chambers=collections.Counter()
for S,u in signatures.items():
 corners=[]
 for i,j in pairs:
  w=cross(V[i],V[j])
  for orient in (-1,1):
   ww=mul(orient,w)
   if all(S[k]*dot(V[k],ww)>=0 for k in range(12)):
    corners.append((i,j,orient))
 m=len(corners)
 n=sum(dot(V[i],u)*dot(V[j],u)<0 for i,j in E)
 assert 3<=m<=12
 C[(n,m)]+=1
 coeff=[2-m,0,0,0,0]
 for i,j,orient in corners:
  c=S[i]*S[j]*dot(V[i],V[j]);ind={1:1,5:2,7:3,9:4}[abs(c)]
  if c>0:coeff[0]+=1;coeff[ind]-=1
  else:coeff[ind]+=1
 for k in range(5):coefN[n][k]+=coeff[k]
 types[tuple(coeff)]+=1
 patterns[n][tuple(coeff)]+=1
 observed_chambers[(n,m,tuple(coeff))]+=1
expected_chambers={
 (4,4,(-1,2,1,-1,0)):24,
 (4,8,(2,0,0,-4,-4)):6,
 (5,3,(0,-1,0,1,1)):48,
 (5,5,(2,-2,-2,-1,0)):24,
 (6,4,(-1,2,0,1,-1)):24,
 (6,3,(-1,0,3,0,0)):8,
}
assert dict(observed_chambers)==expected_chambers
assert {n:coefN[n] for n in coefN}=={4:[-12,48,24,-48,-24],5:[48,-96,-48,24,48],6:[-32,48,24,24,-24]}
assert [sum(coefN[n][k] for n in (4,5,6)) for k in range(5)]==[4,0,0,0,0]
assert [sum(n*coefN[n][k] for n in (4,5,6)) for k in range(5)]==[0,0,0,72,0]
assert sum(m for (n,sides,coeff),m in observed_chambers.items())==134
print('exact_134_cell_census')
for x in sorted(expected_chambers):print(x, expected_chambers[x])
for n in sorted(coefN):
 v=coefN[n];A=float(v[0])*math.pi+sum(float(v[i])*math.acos(k/11) for i,k in enumerate((1,5,7,9),start=1));print('N',n,'coefficients',v,'area',A,'prob',A/(4*math.pi),'types',patterns[n])
print('EXACT_CHAMBERS_OK 134_cells 18_edges 3_support_values')
