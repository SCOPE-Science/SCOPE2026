from itertools import product
from collections import Counter

def rot(x,k):return ((x<<1)&((1<<k)-1))|(x>>(k-1))
def constrained_necklaces(k):
 seen=set();out=[]
 for x in range(1<<k):
  if x in seen:continue
  p=[];j=x
  while j not in p:
   p.append(j);seen.add(j);j=rot(j,k)
  if all('11' not in format(y,f'0{k}b') for y in p):out.append(tuple(p))
 return out

def graph(k):
 n=1<<k
 vs=tuple(x for x in range(n) if '11' not in format(x,f'0{k}b'))
 neigh={v: tuple(w for b in (0,1) if (w:=((v<<1)&(n-1))|b) in vs) for v in vs}
 return vs,neigh

def residual_path(k,delset,vs,neigh):
 rem=set(vs)-delset
 indeg={v:0 for v in rem}
 for v in rem:
  for w in neigh[v]:
   if w in rem:indeg[w]+=1
 pending=[v for v in rem if indeg[v]==0]
 d={v:1 for v in pending}; order=0;maxp=0
 while pending:
  v=pending.pop();order+=1;maxp=max(maxp,d[v])
  for w in neigh[v]:
   if w not in rem:continue
   d[w]=max(d.get(w,0),d[v]+1);indeg[w]-=1
   if indeg[w]==0:pending.append(w)
 if order!=len(rem):return None
 return maxp

def solve(k):
 ps=constrained_necklaces(k)
 vs,neigh=graph(k)
 cnt=0;hist=Counter(); rows=[]
 for tuplechoice in product(*ps):
  S=set(tuplechoice)
  lp=residual_path(k,S,vs,neigh)
  if lp is not None:
   cnt+=1;hist[lp]+=1;rows.append((tuple(sorted(tuplechoice)),lp))
 print(f"n={k} allowed={len(vs)} cycles={len(ps)} cand={__import__('math').prod(map(len,ps))} accepted={cnt} hist="+','.join(f'{d}:{v}' for d,v in sorted(hist.items())))
 return rows
if __name__=='__main__':
 import pathlib
 path=pathlib.Path(__file__).with_name('optimizers.tsv')
 lines=path.read_text(encoding='utf-8').splitlines()[1:]
 for k in range(2,9):
  found=sorted((tuple(v),d) for v,d in solve(k))
  listed=sorted((tuple(map(int,s.split(','))),int(d)) for kk,d,s in (line.split('\t') for line in lines) if int(kk)==k)
  assert found==listed,(k,'catalog mismatch')
 print('VERIFY_OK')
