#!/usr/bin/env python3
"""Independent signed simplicial Lefschetz checks for cyclic-coordinate actions."""
import networkx as nx

def sign_of_perm(lst):
  v=0
  for i,a in enumerate(lst):
    for b in lst[i+1:]:
      if a>b:v+=1
  return -1 if v%2 else 1

def check(k,f):
  n=k+f
  V=list(range(1<<n))
  G=nx.Graph()
  G.add_nodes_from(V)
  for i in V:
    for j in range(i+1,len(V)):
      if (i^j).bit_count()<=2:G.add_edge(i,j)
  def rot(z):
    mov=z&((1<<k)-1)
    return (z & ~((1<<k)-1)) | ((mov<<1)&((1<<k)-1)) | (mov>>(k-1))
  total=0; num=0; faces=0
  for c in nx.enumerate_all_cliques(G):
    faces+=1
    if set(map(rot,c)) != set(c): continue
    num+=1
    order={v:i for i,v in enumerate(sorted(c))}
    perm=[order[rot(v)] for v in sorted(c)]
    total += (-1)**(len(c)-1) * sign_of_perm(perm)
  expected=0 if k==3 and f==0 else 2
  assert total==expected,(k,f,total,expected)
  return faces,num,total
if __name__=='__main__':
  for k,f in [(3,0),(4,0),(4,1),(4,2),(5,0),(5,1)]:
    print('PASS',k,f,*check(k,f),flush=True)
