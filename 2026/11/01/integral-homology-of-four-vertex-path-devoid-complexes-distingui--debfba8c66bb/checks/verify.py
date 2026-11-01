#!/usr/bin/env python3
"""Finite integer-chain verification for four-vertex-path-devoid graph complexes."""
from collections import Counter,defaultdict,deque
from functools import lru_cache
from itertools import combinations

N=16
V=list(range(N))
ALL=(1<<N)-1

def vertices(mask):
 while mask:
  bit=mask & -mask
  yield bit.bit_length()-1
  mask^=bit

def graph(which):
 adj=[0]*N
 for u in V:
  a,b=divmod(u,4)
  if which=='sh':
   offsets=((1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1))
   neighbors=[((a+x)%4)*4+(b+y)%4 for x,y in offsets]
  else:
   neighbors=[i for i in V if i!=u and (i//4==a or i%4==b)]
  for v in neighbors: adj[u]|=1<<v
 assert all(m.bit_count()==6 for m in adj)
 assert all(bool(adj[u]&(1<<v))==bool(adj[v]&(1<<u)) for u in V for v in V)
 assert sum((adj[u]&(1<<v)!=0) for u in V for v in range(u+1,N))==48
 triangles=sum(1 for a,b,c in combinations(V,3) if adj[a]>>b&1 and adj[a]>>c&1 and adj[b]>>c&1)
 assert triangles==32
 for u,v in combinations(V,2):
  assert (adj[u]&adj[v]).bit_count()==2
 return adj

def matching(face):
 unpaired=face[:]
 partner=[0]*(1<<N)
 for v in V:
  bit=1<<v
  for s in range(1,len(unpaired)):
   if not s&bit and unpaired[s] and unpaired[s|bit]:
    unpaired[s]=unpaired[s|bit]=0
    partner[s]=s|bit;partner[s|bit]=s
 critical=[s for s in range(1,len(unpaired)) if unpaired[s]]
 assert all((partner[s] and face[partner[s]]) or (not partner[s] and unpaired[s]) for s in range(1,len(face)) if face[s])
 return partner,critical

def topo_check(face,partner):
 # Arcs point from high face to lower face, except matched incidences, reversed.
 indeg=[0]*len(face)
 alive=[s for s in range(1,len(face)) if face[s]]
 incidences=0
 for hi in alive:
  for v in vertices(hi):
   lo=hi^(1<<v)
   if not lo:continue
   incidences+=1
   if partner[lo]==hi: indeg[hi]+=1
   else:indeg[lo]+=1
 todo=deque(s for s in alive if indeg[s]==0)
 popped=0
 while todo:
  s=todo.popleft();popped+=1
  if partner[s] and partner[s]>s:
   hi=partner[s];indeg[hi]-=1
   if not indeg[hi]:todo.append(hi)
  if s.bit_count()>1:
   for v in vertices(s):
    lo=s^(1<<v)
    if partner[lo]==s:continue
    indeg[lo]-=1
    if not indeg[lo]:todo.append(lo)
 assert popped==len(alive),(popped,len(alive))
 return incidences

def simplicial_boundary(s):
 return [(s^(1<<v),(-1)**i) for i,v in enumerate(vertices(s))]

def morse_boundary(top,partner,critical):
 # Boundary of a critical 12-cell reduced along the gradient to critical 11-cells.
 cc=set(critical)
 @lru_cache(None)
 def reduce_low(s):
  if s in cc:return {s:1}
  hi=partner[s]
  if hi and hi.bit_count()==s.bit_count()-1:
   return {} # cell matched downward, eliminated in the next dimension
  assert hi and hi.bit_count()==s.bit_count()+1,(s,hi)
  eps=dict(simplicial_boundary(hi))[s]
  out=defaultdict(int)
  for t,coef in simplicial_boundary(hi):
   if t==s:continue
   for key,v in reduce_low(t).items():out[key]-=coef*eps*v
  return {k:v for k,v in out.items() if v}
 out=defaultdict(int)
 for s,coef in simplicial_boundary(top):
  for key,v in reduce_low(s).items():out[key]+=coef*v
 return {k:v for k,v in out.items() if v},reduce_low.cache_info()

def p4_devoid_faces(which):
    A=graph(which)
    forbidden=set()
    for a in V:
        for b in V:
            if not A[a]>>b&1:continue
            for c in V:
                if c in (a,b) or not A[b]>>c&1:continue
                for d in V:
                    if d in (a,b,c) or not A[c]>>d&1:continue
                    forbidden.add((1<<a)|(1<<b)|(1<<c)|(1<<d))
    # Independently test every four-subset against all twenty-four vertex orderings.
    for T in combinations(V,4):
        subset=sum(1<<v for v in T)
        path=any(A[a]>>b&1 and A[b]>>c&1 and A[c]>>d&1
                 for a in T for b in T for c in T for d in T
                 if len({a,b,c,d})==4)
        assert path==(subset in forbidden)
    face=bytearray([1])*(1<<N)
    for minimal_nonface in forbidden:
        remaining=ALL^minimal_nonface
        q=remaining
        while True:
            face[q|minimal_nonface]=0
            if not q:break
            q=(q-1)&remaining
    face[0]=0  # the empty face is not part of the nonempty Hasse diagram
    for mask in range(1,len(face)):
        if face[mask]:
            assert all(face[mask^(1<<v)] for v in vertices(mask) if mask!=(1<<v))
    return face,forbidden

def boundary_matrix(partner,critical,dim):
    lower=sorted(s for s in critical if s.bit_count()==dim)
    upper=sorted(s for s in critical if s.bit_count()==dim+1)
    matrix=[[0]*len(upper) for _ in lower]
    for j,s in enumerate(upper):
        a,_=morse_boundary(s,partner,critical)
        assert set(a)<=set(lower)
        for i,t in enumerate(lower):matrix[i][j]=a.get(t,0)
    return matrix

def exact_unit_smith(matrix):
    # Only integer unimodular operations. Return unit diagonal count,
    # and require a zero residual matrix; this proves no nonunit Smith factors.
    if not matrix:return 0
    M=[row[:] for row in matrix]
    r=len(M);c=len(M[0]);k=0
    while k<min(r,c):
        choice=next(((i,j) for i in range(k,r) for j in range(k,c)
                     if abs(M[i][j])==1),None)
        if choice is None:break
        i,j=choice;M[i],M[k]=M[k],M[i]
        for row in M:row[j],row[k]=row[k],row[j]
        if M[k][k]<0:M[k]=[-a for a in M[k]]
        for i in range(k+1,r):
            a=M[i][k]
            if a:M[i]=[M[i][j]-a*M[k][j] for j in range(c)]
        for j in range(k+1,c):
            a=M[k][j]
            if a:
                for i in range(r):M[i][j]-=a*M[i][k]
        assert M[k][k]==1
        assert all(M[i][k]==0 for i in range(k+1,r))
        assert all(M[k][j]==0 for j in range(k+1,c))
        k+=1
    assert all(M[i][j]==0 for i in range(k,r) for j in range(k,c)), 'nonunit torsion risk'
    return k

def mod2_rank(column_bitvectors):
    pivots={}
    for col in column_bitvectors:
        while col:
            b=col.bit_length()-1
            if b in pivots:col^=pivots[b]
            else:pivots[b]=col;break
    return len(pivots)

def independent_mod2_homology(face):
    by={d:[s for s in range(1,len(face)) if face[s] and s.bit_count()==d+1]
        for d in range(7)}
    ranks={0:0}
    for d in range(1,7):
        rowmap={s:i for i,s in enumerate(by[d-1])}
        columns=[]
        for top in by[d]:
            z=0
            for t,_ in simplicial_boundary(top):z^=1<<rowmap[t]
            columns.append(z)
        ranks[d]=mod2_rank(columns)
    betti={d:len(by[d])-ranks[d]-ranks.get(d+1,0) for d in range(7)}
    betti[0]-=1
    return {i:v for i,v in betti.items() if v}

def product_zero(A,B):
    if not A or not B:return True
    assert len(A[0])==len(B)
    return all(sum(A[i][k]*B[k][j] for k in range(len(B)))==0
               for i in range(len(A)) for j in range(len(B[0])))

def run(which):
    face,bad=p4_devoid_faces(which)
    hist=Counter(s.bit_count()-1 for s in range(1,len(face)) if face[s])
    partner,critical=matching(face)
    crit=Counter(s.bit_count()-1 for s in critical)
    incidences=topo_check(face,partner)
    matrices={d:boundary_matrix(partner,critical,d) for d in range(2,6)}
    ranks={d:exact_unit_smith(matrices[d]) for d in matrices}
    assert all(product_zero(matrices[d],matrices[d+1]) for d in range(2,5))
    homology={d:crit[d]-ranks.get(d,0)-ranks.get(d+1,0) for d in range(2,6)}
    homology={d:k for d,k in homology.items() if k}
    mod2=independent_mod2_homology(face)
    assert homology==mod2,(homology,mod2)
    if which=='sh':
        assert (len(bad),sum(face)+1,incidences)==(636,3193,13536)
        assert crit=={0:1,3:38,4:51,5:6}
        assert ranks=={2:0,3:0,4:6,5:0}
        assert homology=={3:32,4:45,5:6}
    else:
        assert (len(bad),sum(face)+1,incidences)==(620,3305,14064)
        assert crit=={0:1,2:1,3:17,4:89,5:18}
        assert ranks=={2:0,3:1,4:16,5:0}
        assert homology=={4:73,5:18}
    print(which,'forbidden',len(bad),'faces',sum(face)+1,
          'f_vector',dict(sorted(hist.items())),'incidences',incidences,
          'critical',dict(sorted(crit.items())),'unit_smith_ranks',ranks,
          'integral_reduced_betti',homology,'mod2_check',mod2)
    return homology

if __name__=='__main__':
    run('sh');run('rook')
    print('VERIFY_OK')
