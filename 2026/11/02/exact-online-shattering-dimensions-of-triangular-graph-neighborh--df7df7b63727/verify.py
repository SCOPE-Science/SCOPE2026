import itertools,json
from functools import lru_cache
from pathlib import Path

def adj(e,f):return len(set(e)&set(f))==1

def dim(n):
 V=list(itertools.combinations(range(n),2)); tests=[sum(1<<j for j,v in enumerate(V) if adj(v,w)) for w in V]; total=(1<<len(V))-1
 @lru_cache(None)
 def ld(s):
  if s.bit_count()<2:return 0
  best=0
  for m in tests:
   a=s&m;b=s^a
   if not a or not b:continue
   if min(a.bit_count(),b.bit_count())<1<<best:continue
   best=max(best,1+min(ld(a),ld(b)))
   if best==s.bit_count().bit_length()-1:break
  return best
 return ld(total)

def check(t,n,depth=0):
 if 'center' in t:
  assert 'query' not in t and depth==0
  return [tuple(t['center'])]
 assert depth>0
 v=tuple(t['query']);out=[]
 for bit,key in [(0,'zero'),(1,'one')]:
  centers=check(t[key],n,depth-1)
  assert all(int(adj(c,v))==bit for c in centers)
  out+=centers
 assert len(set(out))==2**depth
 return out

if __name__=='__main__':
 data=json.loads(Path(__file__).with_name('lower_certificates.json').read_text())
 for name,o in data.items():
  leaves=check(o['tree'],o['n'],o['depth']);print(name,'certificate',len(leaves),'PASS')
 expect={2:0,3:1,4:1,5:3,6:3,7:4,8:4,9:4}
 for n,target in expect.items():
  value=dim(n);assert value==target,(n,value,target)
  print('EXACT',n,value,'PASS')
 print('TRIANGULAR_NEIGHBORHOODS_ALL_CHECKS_PASS')
