"""Independent finite-extension point test for singular cubic candidates.
This is a cross-check, not the proof of geometric smoothness: the latter
uses complete Groebner tests in verify_census.py.
"""
import json,collections
MOD={1:0b11,2:0b111,3:0b1011,4:0b10011}
MON=[(2,1,0),(2,0,1),(1,2,0),(1,1,1),(1,0,2),(0,2,1),(0,1,2)]

def mul(a,b,m):
 p=MOD[m];v=0
 for _ in range(m):
  if b&1:v^=a
  b>>=1;a<<=1
  if a&(1<<m):a^=p
 return v

def powf(a,n,m):
 out=1
 for _ in range(n):out=mul(out,a,m)
 return out

def terms(mask):
 bits=[(mask>>k)&1 for k in range(6)]
 bits.append(sum(bits)%2)
 return [e for e,b in zip(MON,bits) if b]

def eval_poly(exps,point,m,derivative=-1):
 result=0
 for e in exps:
  f=list(e)
  if derivative!=-1:
   if not e[derivative]&1:continue
   f[derivative]-=1
  term=1
  for x,p in zip(point,f):term=mul(term,powf(x,p,m),m)
  result^=term
 return result

def points(m):
 q=1<<m
 for a in range(q):
  for b in range(q):yield (a,b,1)
 for a in range(q):yield (a,1,0)
 yield (1,0,0)

bits=collections.Counter();first_field={};smooth=[]
for mask in range(1,64):
 e=terms(mask)
 for m in MOD:
  if any(all(eval_poly(e,p,m,derivative=d)==0 for d in (-1,0,1,2)) for p in points(m)):
   first_field[mask]=m;break
 else:smooth.append(mask)
assert smooth==[7,22,38,49,51,53],smooth
print(json.dumps({'checked_field_degrees':list(MOD),'singular_curve_count':len(first_field),
 'first_detected_singular_degree_counts':dict(sorted(collections.Counter(first_field.values()).items())),
 'no_singular_points_detected_through_degree_four':smooth,
 'agreement_with_complete_ideal_tests':True},indent=2,sort_keys=True))
