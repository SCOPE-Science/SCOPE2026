"""Independent finite-extension point checks for a genus-four canonical-curve certificate.
This does not replace the exact Groebner smoothness test in the main certificate.
"""
import json,itertools,collections,sys
D=json.load(open(sys.argv[1] if len(sys.argv)>1 else '../data/qminus_genus4_results.json'))
mons=[tuple(int(t[1:]) for t in z.split('*')) for z in D['basis']]
# primitive irreducible polynomials, degrees 1..4
polys={1:0b11,2:0b111,3:0b1011,4:0b10011}

def field(d):
 q=1<<d;mod=polys[d];mx=q-1
 def mul(a,b):
  r=0
  while b:
   if b&1:r^=a
   b>>=1;a<<=1
   if a&q:a^=mod
  return r
 return q,mul

def derivative_term(m,i):
 if m.count(i)%2==0:return None
 a=list(m);a.remove(i);return a

def poly_eval(terms,p,mul):
 total=0
 for mon in terms:
  value=1
  for i in mon:value=mul(value,p[i])
  total ^=value
 return total

def singular_points(mask,d):
 q,mul=field(d)
 forms=[mons[i] for i in range(16) if mask>>i&1]
 partials=[[derivative_term(a,i) for a in forms if derivative_term(a,i) is not None] for i in range(4)]
 points=[]
 for k in range(4):
  for vv in itertools.product(range(q), repeat=3-k):
   p=(0,)*k+(1,)+vv
   Q=mul(p[0],p[1])^mul(p[2],p[2])^mul(p[2],p[3])^mul(p[3],p[3])
   if Q:continue
   if poly_eval(forms,p,mul):continue
   grad=[poly_eval(c,p,mul) for c in partials]
   dq=[p[1],p[0],p[3],p[2]]
   if any(mul(dq[i],grad[j])^mul(dq[j],grad[i]) for i in range(4) for j in range(i+1,4)):continue
   points.append(p)
 return points

N=0
for v in D['smooth_orbits']:
 mask=v['mask']
 for d in (1,2,3,4):
  bad=singular_points(mask,d)
  assert not bad,(mask,d,bad)
  N+=1
print('PASS: independent extension-field gradient checks:',N,'(representative, extension-degree) cases, degrees 1 through 4')
# Group-weighted distribution and joint theta profile are checked independently from the certificate rows.
weighted=collections.Counter();theta_tan=collections.Counter()
tangent={p['plane'] for p in D['plane_details'] if p['type']=='tangent'}
for row in D['smooth_orbits']:
 k=row['theta_planes'].bit_count()
 assert k==row['theta_count']
 weighted[k]+=row['size']
 n=sum(bool(row['theta_planes']>>(h-1)&1) for h in tangent)
 theta_tan[(k-n,n)]+=row['size']
assert sorted(weighted.items())==list(map(tuple,D['smooth_equation_distribution']))
assert sum(weighted.values())==27060
assert len(D['smooth_orbits'])==254
print('PASS: weighted theta distribution',sorted(weighted.items()))
print('PASS: joint smooth-conic/tangent-conic theta profile',sorted(theta_tan.items()))
