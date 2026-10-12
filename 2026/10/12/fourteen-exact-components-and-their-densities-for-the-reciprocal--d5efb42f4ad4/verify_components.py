from fractions import Fraction as F
from itertools import product
from functools import reduce
from operator import mul
P=[2,3,5,7];K=[2,1,1,1];N=100

def f(p,a):return sum((F(1,p**(3*j)) for j in range(a+1)),F(0))
def finf(p):return F(p**3,p**3-1)
F0=reduce(mul,((1-F(1,p**3)) for p in P),F(1))
Z0=sum((F(1,k**3) for k in range(1,N+1)),F(0))
L=F0*(Z0+F(1,2*(N+1)**2));U=F0*(Z0+F(1,2*N**2))
print('T bounds',float(L),float(U),'width',float(U-L))
assert L>1
for p,k in zip(P,K):
 print(p,k,'ratio at k:',float(f(p,k+1)/f(p,k)), 'ratio at k-1',float(f(p,k)/f(p,k-1)))
 assert f(p,k+1)<=L*f(p,k)
 assert f(p,k)>U*f(p,k-1)
for p,qs in {11:[13,17,19],13:[17,19,23,29],17:[19,23,29],19:[23,29,31],23:[29,31,37]}.items():
 s=sum((F(1,q**3) for q in qs),F(0))
 print('tail',p,qs,float(s-F(1,p**3)))
 assert s>F(1,p**3-1)
assert sum((F(5,6)**(3*i) for i in range(1,4)),F(0)) > F(29**3,29**3-1)
opts=[]
for p,k in zip(P,K):
 opts.append([(str(a),f(p,a),f(p,a),F(p-1,p**(a+1))) for a in range(k)] + [(str(k)+'+',f(p,k),finf(p),F(1,p**k))])
rows=[]
for t in product(*opts):
 lo=reduce(mul,(x[1] for x in t),F(1));hi=reduce(mul,(x[2] for x in t),F(1));weight=reduce(mul,(x[3] for x in t),F(1))
 rows.append({'state':','.join(x[0] for x in t),'lo':lo,'hi':hi,'weight':weight})
rows.sort(key=lambda x:x['lo'])
groups=[]
for r in rows:
 if not groups or r['lo']>groups[-1]['hi']*U:
  groups.append({'lo':r['lo'],'hi':r['hi'],'left':r['state'],'right':r['state'],'mass':r['weight'],'states':[r['state']]})
 else:
  g=groups[-1]
  assert r['lo']<=g['hi']*L,('ambiguous overlap',r['state'],g['hi'],r['lo'])
  g['states'].append(r['state']);g['mass']+=r['weight']
  if r['hi']>g['hi']:g['hi']=r['hi'];g['right']=r['state']
print('groups',len(groups),'rows',len(rows),'mass',sum((g['mass'] for g in groups),F(0)))
for i,g in enumerate(groups):
 print(f'{i+1:2}', 'L='+str(g['lo']),'Hcoeff='+str(g['hi']),'mass='+str(g['mass']), 'left='+g['left'],'right='+g['right'], 'states='+','.join(g['states']))
assert all(groups[i+1]['lo']-groups[i]['hi']*U > F(1,1000) for i in range(len(groups)-1))
print('min_gap',min((float(groups[i+1]['lo']-groups[i]['hi']*U) for i in range(len(groups)-1))))
EXPECTED = [
 ('1','1','8/35'),
 ('344/343','343/342','4/105'),
 ('126/125','125/124','2/35'),
 ('6192/6125','42875/42408','1/105'),
 ('28/27','1029/988','2/15'),
 ('392/375','128625/122512','1/30'),
 ('9/8','9/8','4/35'),
 ('387/343','343/304','2/105'),
 ('567/500','1125/992','1/35'),
 ('6966/6125','42875/37696','1/210'),
 ('73/64','196/171','2/15'),
 ('4599/4000','6125/5301','1/30'),
 ('7/6','9261/7904','1/15'),
 ('147/125','18375/15314','1/10'),
]
assert len(groups) == len(EXPECTED)
for g,(a,b,w) in zip(groups,EXPECTED):
 assert g['lo']==F(a) and g['hi']==F(b) and g['mass']==F(w)
assert sum((g['mass'] for g in groups),F(0))==1
assert groups[-1]['hi']==1/F0
print('CERTIFICATE_OK ordinary_sigma_minus_three components=14 candidates=24 tail_threshold=11 rational_density_total=1')
