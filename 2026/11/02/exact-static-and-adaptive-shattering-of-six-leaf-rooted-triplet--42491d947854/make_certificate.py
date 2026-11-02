"""Generate an explicit complete nine-level triplet decision tree."""
import functools,json
from verify_rooted_triples import trees_by_splitting,triplets,responses
n=6;rows=trees_by_splitting(n);q=responses(rows,triplets(n));full=(1<<len(rows))-1
@functools.lru_cache(None)
def feasible(s,d):
 if s.bit_count()<(1<<d):return False
 if d==0:return True
 for m in q:
  a=s&m;b=s^a
  if a and b and feasible(a,d-1) and feasible(b,d-1):return True
 return False

def build(s,d):
 if d==0:return {'leaf':(s&-s).bit_length()-1}
 for j,m in enumerate(q):
  a=s&m;b=s^a
  if a and b and feasible(a,d-1) and feasible(b,d-1):
   return {'query':j,'zero':build(b,d-1),'one':build(a,d-1)}
 raise RuntimeError
assert feasible(full,9)
cert={'n':6,'depth':9,'tree':build(full,9)}
with open('depth9_certificate.json','w',encoding='utf-8') as f:json.dump(cert,f,separators=(',',':'))
print('certificate encoded')
