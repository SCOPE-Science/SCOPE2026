from prism_chain import complexes
from prism_core import graph,act,char
from itertools import combinations

def pivots(cols,p):
 bases={}
 for col in cols:
  a={k:v%p for k,v in col.items() if v%p}
  while a:
   k=max(a)
   if k not in bases:
    inv=pow(a[k],-1,p);bases[k]={j:v*inv%p for j,v in a.items()};break
   c=a[k]
   for j,v in bases[k].items():
    t=(a.get(j,0)-c*v)%p
    if t:a[j]=t
    else:a.pop(j,None)
 return bases

def test(n):
 V,E=graph(n); c0,c1,c2,b1,b2=complexes(n)
 cells=[(i,v) for i,e in enumerate(E) for v in V if v not in e]
 lookup={cell:j for j,cell in enumerate(cells)}
 eix={e:i for i,e in enumerate(E)}
 p=1009; bases=pivots(b2,p);free=set(range(c1))-set(bases)
 assert len(free)==n+2+c0-1
 for a in range(n):
  for s in range(2):
   for t in range(2):
    g=act(n,a,s,t);coker=0
    for j in free:
     ei,v=cells[j];edge=E[ei];mapped=(min(g[edge[0]],g[edge[1]]),max(g[edge[0]],g[edge[1]]))
     k=lookup[(eix[mapped],g[v])];sign=1 if g[edge[0]]<g[edge[1]] else -1
     vec={k:sign%p}
     for ix in sorted(bases,reverse=True):
      if ix not in vec:continue
      mult=vec[ix]
      for z,d in bases[ix].items():
       val=(vec.get(z,0)-mult*d)%p
       if val:vec[z]=val
       else:vec.pop(z,None)
     coker+=vec.get(j,0)
    coker%=p
    tr=(coker-(char(n,a,s,t)[0]-1))%p
    expected=char(n,a,s,t)[-2]%p
    assert tr==expected,(n,a,s,t,tr,expected)
 print('n',n,'H1 character verified all',4*n,'actions modulo',p)
if __name__=='__main__':
 for n in range(5,11):test(n)
 print('PRISM_H1_ALL_ACTIONS_OK')
