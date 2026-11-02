from itertools import product
from verify import ops,generated

def test(q,k):
 add,mul,neg=ops(q);el=list(product(range(q),repeat=3))
 cone=[x for x in el if add(mul(x[0],x[0]),mul(x[1],x[2]))==0]
 assert len(cone)==q*q,(q,len(cone))
 sq={mul(a,a) for a in range(1,q)}
 types={}
 for x in el:
  if q%2==0:typ='center' if x[1]==x[2]==0 else 'other'
  elif x==(0,0,0):typ='zero'
  else:
   d=add(mul(x[0],x[0]),mul(x[1],x[2]));typ='nil' if d==0 else ('split' if d in sq else 'nonsplit')
  base=q**k
  if typ in ('zero','center'):exp=(base-1)*(base-q)
  elif typ in ('nil','other'):exp=base*(base-1)
  elif typ=='split':exp=(base-1)**2
  else:exp=base**2-1
  count=sum(generated((x,)+ys,q,add,mul,neg) for ys in product(cone,repeat=k))
  assert count==exp,(q,k,x,typ,count,exp)
  types.setdefault(typ,[]).append(count)
 print(q,k,{t:(len(v),v[0]) for t,v in types.items()})
for q,k in [(2,1),(3,1),(4,1),(5,1),(7,1),(2,2),(3,2)]:test(q,k)
print('NIL_VERIFY_OK')
