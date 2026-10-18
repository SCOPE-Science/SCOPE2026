"""Independent brute-force confirmation of Catalan generation and exact colour signatures."""
from itertools import permutations
from collections import defaultdict
from math import comb

def avoids(p):
 n=len(p)
 return not any(p[i]<p[j]<p[k] for i in range(n) for j in range(i+1,n) for k in range(j+1,n))

def insert_family(n):
 fam=[()]
 for v in range(n):
  nxt=[]
  for p in fam:
   for i in range(v+1):
    z=p[:i]+(v,)+p[i:]
    if avoids(z):nxt.append(z)
  fam=nxt
 return fam

def source_rows(p):
 n=len(p)
 return [[int(i<j and p[i]<p[j]) for j in range(n)] for i in range(n)]

def wl_classes(perms,n):
 graph=[source_rows(p) for p in perms]; c=[[0]*n for _ in perms]
 for rnd in range(n):
  uniq={}; new=[]
  for P,C in zip(graph,c):
   nxt=[]
   for i in range(n):
    below=tuple(sorted(C[j] for j in range(n) if P[j][i]))
    above=tuple(sorted(C[j] for j in range(n) if P[i][j]))
    key=(C[i],below,above)
    if key not in uniq: uniq[key]=len(uniq)
    nxt.append(uniq[key])
   new.append(nxt)
  c=new
 return len({tuple(sorted(z)) for z in c})

def main():
 expected=[1,2,4,9,21,55,151,447]
 for n in range(1,9):
  raw=[p for p in permutations(range(n)) if avoids(p)]
  ins=insert_family(n)
  assert set(ins)==set(raw) and len(ins)==comb(2*n,n)//(n+1)
  types=wl_classes(raw,n)
  assert types==expected[n-1],(n,types)
  print(n,len(raw),types)
 print('PASS: independent brute permutations agree through n=8')
if __name__=='__main__':main()
