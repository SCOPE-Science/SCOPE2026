import json,itertools
from functools import lru_cache
from pathlib import Path

def create(n,depth):
 V=list(itertools.combinations(range(n),2)); masks=[]
 for x in V:
  masks.append(sum(1<<i for i,y in enumerate(V) if len(set(x)&set(y))==1))
 @lru_cache(None)
 def possible(s,k):
  if k==0:return bool(s)
  if s.bit_count()<2**k:return False
  for m in masks:
   y=s&m;z=s^y
   if y.bit_count()<2**(k-1) or z.bit_count()<2**(k-1):continue
   if possible(y,k-1) and possible(z,k-1):return True
  return False
 def tree(s,k):
  if k==0:return {'center':V[(s&-s).bit_length()-1]}
  for i,m in enumerate(masks):
   y=s&m;z=s^y
   if y.bit_count()<2**(k-1) or z.bit_count()<2**(k-1):continue
   if possible(y,k-1) and possible(z,k-1):
    return {'query':V[i],'zero':tree(z,k-1),'one':tree(y,k-1)}
  raise ValueError('not possible')
 s=(1<<len(V))-1
 assert possible(s,depth)
 return {'n':n,'depth':depth,'tree':tree(s,depth)}

if __name__=='__main__':
 obj={'J(5,2)':create(5,3),'J(7,2)':create(7,4)}
 Path(__file__).with_name('lower_certificates.json').write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n')
 print('CERTIFICATES',len(obj))
