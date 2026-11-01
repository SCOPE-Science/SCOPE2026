#!/usr/bin/env python3
"""Finite independent checks of fixed faces in directed rooted-forest complexes.
Only finite checks; the arbitrary-size theorem follows from the separate proof.
"""
from itertools import product

def forest(n, arcs):
    # Check indegree and directed-cycle condition separately (no theorem encoded).
    parents={v:[] for v in range(n)}
    for a,b in arcs:
        parents[b].append(a)
        if len(parents[b])>1:return False
    for v in range(n):
        path=set();u=v
        while parents[u]:
            if u in path:return False
            path.add(u);u=parents[u][0]
    return True

def group_generators(blocks, f, symmetric=False):
    n=sum(blocks)+f
    offset=0;gens=[];groups=[]
    for b in blocks:
        B=list(range(offset,offset+b));groups.append(B)
        rot=list(range(n))
        for i,a in enumerate(B):rot[a]=B[(i+1)%b]
        gens.append(rot)
        if symmetric and b>2:
            g=list(range(n));g[B[0]],g[B[1]]=g[B[1]],g[B[0]]
            gens.append(g)
        offset+=b
    return n,gens,groups,list(range(offset,n))

def arc_orbits(n,gens):
    pending={(i,j) for i in range(n) for j in range(n) if i!=j}; out=[]
    while pending:
        v=min(pending);O={v};todo=[v]
        while todo:
            a,b=todo.pop()
            for g in gens:
                w=(g[a],g[b])
                if w not in O:O.add(w);todo.append(w)
        pending-=O;out.append(frozenset(O))
    return out

def run():
    checked=0;orbits=0;faces=0
    configurations=[([2],0),([2],1),([2],2),([2],3),([2],4),
      ([3],0),([3],1),([3],2),([3],3),([4],1),([4],2),
      ([2,2],0),([2,2],1),([2,2],2),([2,2],3),
      ([2,3],0),([2,3],1),([2,3],2),([3,3],2),
      ([2,2,2],0),([2,2,2],1),([2,2,2],2),([2,3,4],2)]
    for blocks,f in configurations:
      for symmetric in (False, True):
        n,gens,groups,fixed=group_generators(blocks,f,symmetric)
        oo=arc_orbits(n,gens)
        usable=[O for O in oo if forest(n,O)]
        wanted={frozenset(((a,b),)) for a in fixed for b in fixed if a!=b}
        wanted|={frozenset((a,b) for b in B) for B in groups for a in fixed}
        assert set(usable)==wanted,('orbit mismatch',blocks,f,symmetric)
        orbits+=len(oo)
        if len(usable)>17:continue
        for bits in range(1<<len(usable)):
          chosen=[usable[i] for i in range(len(usable)) if bits>>i&1]
          actual=forest(n,[edge for O in chosen for edge in O])
          fixed_arcs=[next(iter(O)) for O in chosen if len(O)==1]
          selected=[sum(1 for O in chosen if len(O)>1 and {b for a,b in O}==set(B)) for B in groups]
          predicted=forest(n,fixed_arcs) and all(k<=1 for k in selected)
          assert actual==predicted,('face mismatch',blocks,f,symmetric,bits)
          faces+=1
        checked+=1
    print(f'PASS: {orbits} edge orbits classified; {faces} orbit-subsets checked exhaustively over {checked} finite cases (cyclic and symmetric block actions).')

if __name__=='__main__':run()
