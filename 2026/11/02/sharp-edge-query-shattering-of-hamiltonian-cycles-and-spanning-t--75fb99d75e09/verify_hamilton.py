#!/usr/bin/env python3
"""Exact Hamiltonian-cycle concept class static and adaptive certificates."""
import itertools,json
from functools import lru_cache
from pathlib import Path
TARGET={3:(1,[1],0),4:(3,[1,6],1),5:(12,[1,10,45,60],3),
        6:(60,[1,15,105,375,360],5),7:(360,[1,21,210,1155,3465,2520],6)}

def cycles(n):
 E=list(itertools.combinations(range(n),2)); idx={e:i for i,e in enumerate(E)}
 vals=[]
 for p in itertools.permutations(range(1,n)):
  if p[0]>p[-1]:continue
  order=(0,)+p
  vals.append(sum(1<<idx[tuple(sorted((a,b)))] for a,b in zip(order,order[1:]+order[:1])))
 assert len(set(vals))==len(vals)
 return E,sorted(vals)

def census(H,qcount):
 front=[()];counts=[1]
 while front:
  new=[]
  for s in front:
   for j in range(s[-1]+1 if s else 0,qcount):
    t=s+(j,);patterns=set()
    for h in H:
     patterns.add(sum(((h>>e)&1)<<k for k,e in enumerate(t)))
     if len(patterns)==2**len(t):break
    if len(patterns)==2**len(t):new.append(t)
  if not new:break
  counts.append(len(new));front=new
 return counts

def game(H,qcount):
 B=[sum(1<<i for i,h in enumerate(H) if h>>q&1) for q in range(qcount)]
 root=(1<<len(H))-1
 @lru_cache(None)
 def can(S,k):
  if k==0:return True
  if S.bit_count()<2**k:return False
  for j,Q in enumerate(B):
   one=S&Q;zero=S&~Q
   if min(one.bit_count(),zero.bit_count())>=2**(k-1) and can(one,k-1) and can(zero,k-1):return True
  return False
 def build(S,k):
  if not k:return {'witness':(S&-S).bit_length()-1}
  for j,Q in enumerate(B):
   one=S&Q;zero=S&~Q
   if min(one.bit_count(),zero.bit_count())>=2**(k-1) and can(one,k-1) and can(zero,k-1):
    return {'query':j,'zero':build(zero,k-1),'one':build(one,k-1)}
  raise AssertionError('missing tree')
 return can,build,root,B

def main():
 out={'schema_version':1,'description':'Hamiltonian cycles complete game witnesses','trees':{}}
 for n,(nh,counts,dim) in TARGET.items():
  E,H=cycles(n);assert len(H)==nh
  assert census(H,len(E))==counts
  can,build,root,B=game(H,len(E))
  assert can(root,dim) and not can(root,dim+1)
  tree=build(root,dim)
  out['trees'][str(n)]={'depth':dim,'edge_order':[list(e) for e in E],
                       'cycles':[format(x,'x') for x in H], 'tree':tree}
  print(f'HAMILTON_N{n}_PASS hypotheses={nh} shattering_counts={counts} VC={len(counts)-1} LD={dim}')
  if n==7:
   c2,_,_,BB=game(H,len(E));assert not c2(BB[0],6)
   print(f'HAMILTON_N7_POSITIVE_UPPER_PASS count={BB[0].bit_count()} states={c2.cache_info().currsize}')
 Path(__file__).with_name('hamilton_certificate.json').write_text(json.dumps(out,separators=(',',':'),sort_keys=True)+'\n')
 print('ALL_HAMILTON_CHECKS_PASS')
if __name__=='__main__':main()
