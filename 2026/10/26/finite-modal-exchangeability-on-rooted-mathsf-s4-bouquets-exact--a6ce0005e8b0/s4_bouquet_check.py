from itertools import product
from math import comb

def test(k,t,s):
 q=1<<k
 n=1+t*s
 R=[[0]+list(range(1,n))]+[[1+i*s+j for j in range(s)] for i in range(t) for _ in range(s)]
 spectra=[set() for _ in range(5)]
 orbit=set()
 support=set()
 for v in product(range(q),repeat=n):
  signatures=tuple(v)
  spectra[0].add(signatures[0])
  for d in range(1,5):
   signatures=tuple((signatures[i],frozenset(signatures[j] for j in R[i])) for i in range(n))
   spectra[d].add(signatures[0])
  vecs=tuple(sorted(tuple(v[1+i*s:1+(i+1)*s].count(color) for color in range(q)) for i in range(t)))
  orbit.add((v[0],vecs))
  sups=frozenset(frozenset(v[1+i*s:1+(i+1)*s]) for i in range(t))
  support.add((v[0],sups))
 N=sum(comb(q,j) for j in range(1,min(s,q)+1))
 h=comb(s+q-1,q-1)
 expected=q*sum(comb(N,j) for j in range(1,min(t,N)+1))
 eo=q*comb(t+h-1,h-1)
 got=[len(z) for z in spectra]
 assert got[2]==expected==len(support),(k,t,s,got,expected,len(support))
 assert len(orbit)==eo,(k,t,s,len(orbit),eo)
 assert got[2]==got[3]==got[4]
 return k,t,s,got,expected,eo

if __name__=='__main__':
 for k,t,s in [(1,1,1),(1,1,2),(1,1,3),(1,2,1),(1,2,2),(1,3,2),(1,3,1),(1,2,3),(2,1,2),(2,2,1),(2,2,2),(1,3,3),(2,1,3),(0,3,2)]:
  print(test(k,t,s))
 print('BOUQUET_MODAL_CREDAL_FINITE_OK')
