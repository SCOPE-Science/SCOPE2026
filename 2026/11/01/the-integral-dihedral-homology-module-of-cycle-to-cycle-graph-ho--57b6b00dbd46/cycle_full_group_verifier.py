#!/usr/bin/env python3
"""Exhaustive integral cubical Lefschetz character checks for small cycle Hom complexes."""
from cycle_action_verifier import build,operation,cell_operation,oriented_cell_sign


def verify(m,n):
    maps,ids,adj,faces,comps,compid,tags=build(m,n)
    fs=[(cell,sum(len(x)==2 for x in cell)) for cell in faces]
    tested=0
    for s in (1,-1):
      for k in range(m):
       for t in (1,-1):
        for l in range(n):
         fixed0=0
         for comp in comps:
           f=maps[comp[0]]
           j=ids[operation(f,s,k,t,l,m,n)]
           fixed0+=(compid[j]==compid[comp[0]])
         lef=0
         for cell,dim in fs:
           if cell_operation(cell,s,k,t,l,m,n)==cell:
             lef+=(-1)**dim*oriented_cell_sign(cell,s,k,t,l,m,n)
         predicted=t*sum(
           abs(w)*n<m and (s*t*w, None if n%2 else (p+k+l)%2)==(w,p)
           for w,p in set(tags))
         assert fixed0-lef==predicted, (m,n,s,k,t,l,fixed0,lef,predicted)
         tested+=1
    print('m=%d n=%d cells=%d operations=%d ALL_TRACES_PASS'%(m,n,len(faces),tested),flush=True)

if __name__=='__main__':
 for m,n in [(6,5),(7,5),(8,6)]: verify(m,n)
 print('ALL_CHECKS_PASS',flush=True)
