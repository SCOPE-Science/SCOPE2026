#!/usr/bin/env python3
"""Generate all unlabelled trees through 14 vertices using deterministic leaf addition and AHU centers; stdlib only."""
from verify import canonical_tree
COUNTS=[1,1,1,2,3,6,11,23,47,106,235,551,1301,3159]
level={canonical_tree(1,()):()}
with open('tree_catalog.txt','w',encoding='utf-8') as f:
 for n in range(1,15):
  assert len(level)==COUNTS[n-1],(n,len(level))
  for edges in level.values():
   f.write(' '.join(map(str,[n]+[v for edge in edges for v in edge]))+'\n')
  if n==14:break
  nxt={}
  for edges in level.values():
   for v in range(n):
    new=edges+((v,n),)
    key=canonical_tree(n+1,new)
    if key not in nxt:nxt[key]=new
  level=nxt
print('CATALOG_OK: 14 graph orders, total',sum(COUNTS),'unlabelled trees')
