#!/usr/bin/env python3
from itertools import permutations, combinations
from fractions import Fraction
from collections import defaultdict, deque

N=11
L=(1,2,3,5)
LINK_ORDER=(9,10,6,5,3,2,4,7,8,1)
MINORS={
  1:{'rows':[0,1,2,3,4,5,6,7,8,9],
     'cols':[0,1,2,6,9,12,17,21,24,27], 'det':1},
  2:{'rows':[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,28,29,30,31,32,33,34,35,36,37,39,40,41,42,43,45,47],
     'cols':[0,1,2,4,5,7,8,10,11,13,15,17,18,20,22,23,25,26,28,29,31,33,35,37,39,41,43,45,47,49,54,55,56,58,60,63,65,69,72,75,77,80,83,95], 'det':-1},
  3:{'rows':[0,1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19,20,21,22,24,25,26,27,29,30,31,32,34,35,36,37,38,40,41,42,44,46,50,51,52,53,54,55,56,57,58,59,60,61,62,64,65,67,68,69,73,79,81,82,86,88,98],
     'cols':list(range(65)), 'det':1},
}

def key(face): return tuple(sorted(face))

def complex_from_facets(facets):
    faces=[{} for _ in range(max(map(len,facets)))]
    for f in facets:
        f=tuple(sorted(f))
        for r in range(1,len(f)+1):
            for c in combinations(f,r): faces[r-1].setdefault(c,None)
    return [list(x.keys()) for x in faces]

def tonnetz(n,L):
    facets={}
    k=len(L)
    for x in range(n):
        for sig in permutations(range(k)):
            cur=x; verts=[x]
            for i in sig[:-1]:
                cur=(cur+L[i])%n
                verts.append(cur)
            facets.setdefault(tuple(sorted(verts)),None)
    flist=list(facets.keys())
    return flist, complex_from_facets(flist)

def boundary(faces,d):
    rows=faces[d-1]; cols=faces[d]
    ridx={f:i for i,f in enumerate(rows)}
    M=[[0]*len(cols) for _ in rows]
    for j,f in enumerate(cols):
        for q in range(len(f)):
            g=f[:q]+f[q+1:]
            M[ridx[g]][j]=1 if q%2==0 else -1
    return M

def matmul(A,B):
    if not A or not B: return []
    BT=list(zip(*B))
    return [[sum(x*y for x,y in zip(r,c)) for c in BT] for r in A]

def rank_q(M):
    A=[[Fraction(x) for x in row] for row in M]
    m=len(A); n=len(A[0]) if m else 0
    r=0
    for c in range(n):
        p=next((i for i in range(r,m) if A[i][c]),None)
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        piv=A[r][c]
        for j in range(c,n): A[r][j]/=piv
        for i in range(r+1,m):
            if A[i][c]:
                z=A[i][c]
                for j in range(c,n): A[i][j]-=z*A[r][j]
        r+=1
        if r==m: break
    return r

def rank_mod(M,p):
    A=[[x%p for x in row] for row in M]
    m=len(A); n=len(A[0]) if m else 0; r=0
    for c in range(n):
        q=next((i for i in range(r,m) if A[i][c]),None)
        if q is None: continue
        A[r],A[q]=A[q],A[r]
        inv=pow(A[r][c],-1,p)
        A[r]=[(x*inv)%p for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                z=A[i][c]
                A[i]=[(a-z*b)%p for a,b in zip(A[i],A[r])]
        r+=1
        if r==m: break
    return r

def det_bareiss(M):
    A=[row[:] for row in M]
    n=len(A)
    if n==0:return 1
    sign=1; den=1
    for k in range(n-1):
        p=next((i for i in range(k,n) if A[i][k]),None)
        if p is None:return 0
        if p!=k:
            A[k],A[p]=A[p],A[k]; sign=-sign
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                A[i][j]=(A[i][j]*pivot-A[i][k]*A[k][j])//den
        den=pivot
        for i in range(k+1,n):A[i][k]=0
    return sign*A[-1][-1]

def staged_matching(faces,order):
    cells={f:{'dim':d,'matched':False} for d,fs in enumerate(faces) for f in fs}
    pairs=[]
    for v in order:
        candidates=sorted((f for f,o in cells.items() if not o['matched'] and v not in f), key=lambda f:(-len(f),f))
        for f in candidates:
            if cells[f]['matched']:continue
            up=tuple(sorted(f+(v,)))
            if up in cells and not cells[up]['matched']:
                cells[f]['matched']=cells[up]['matched']=True
                pairs.append((f,up))
    crit=[f for f,o in cells.items() if not o['matched']]
    # Verify Forman acyclicity by orienting unmatched covers downward, matched covers upward.
    matchset={(a,b) for a,b in pairs}
    nodes=list(cells); idx={f:i for i,f in enumerate(nodes)}
    adj=[[] for _ in nodes]; indeg=[0]*len(nodes)
    for d in range(1,len(faces)):
        for high in faces[d]:
            for q in range(len(high)):
                low=high[:q]+high[q+1:]
                if (low,high) in matchset: u,v=idx[low],idx[high]
                else: u,v=idx[high],idx[low]
                adj[u].append(v); indeg[v]+=1
    dq=deque(i for i,x in enumerate(indeg) if x==0); seen=0
    while dq:
        u=dq.popleft();seen+=1
        for v in adj[u]:
            indeg[v]-=1
            if indeg[v]==0:dq.append(v)
    assert seen==len(nodes), 'matching cycle detected'
    counts=[0]*len(faces)
    for f in crit:counts[len(f)-1]+=1
    return pairs,sorted(crit),counts

facets,faces=tonnetz(N,L)
assert [len(x) for x in faces]==[11,55,110,66]
assert len(facets)==66
B={d:boundary(faces,d) for d in (1,2,3)}
for d in (2,3):
    Z=matmul(B[d-1],B[d])
    assert all(x==0 for row in Z for x in row)
ranks={d:rank_q(B[d]) for d in (1,2,3)}
assert ranks=={1:10,2:44,3:65}
for d,c in MINORS.items():
    sub=[[B[d][i][j] for j in c['cols']] for i in c['rows']]
    got=det_bareiss(sub)
    assert got==c['det'],(d,got)
for p in (2,3,5,7,11,13):
    assert {d:rank_mod(B[d],p) for d in (1,2,3)}==ranks
betti=[len(faces[0])-ranks[1], len(faces[1])-ranks[1]-ranks[2], len(faces[2])-ranks[2]-ranks[3], len(faces[3])-ranks[3]]
assert betti==[1,1,1,1]
# A unit maximal-rank minor in each B_d makes coker(B_d) torsion-free;
# H_{d-1}=ker(B_{d-1})/im(B_d) embeds in coker(B_d), hence all homology is free.

link_facets=sorted(tuple(x for x in f if x!=0) for f in facets if 0 in f)
link_faces=complex_from_facets(link_facets)
assert [len(x) for x in link_faces]==[10,30,24]
LB={d:boundary(link_faces,d) for d in (1,2)}
link_ranks={d:rank_q(LB[d]) for d in (1,2)}
assert link_ranks=={1:9,2:21}
link_betti=[10-9,30-9-21,24-21]
assert link_betti==[1,0,3]
pairs,crit,counts=staged_matching(link_faces,LINK_ORDER)
assert counts==[1,0,3]
assert crit==[(1,3,8),(1,4,6),(2,7,8),(9,)]
assert len(pairs)==30
# Cyclic translation v -> v+a preserves Tonnetz facets and is vertex-transitive.
for a in range(N):
    shifted={tuple(sorted((x+a)%N for x in f)) for f in facets}
    assert shifted==set(facets)

# Natural-size check: among four distinct positive integers, minimum sum is 10,
# uniquely {1,2,3,4}; at sum 11 the unique partition is {1,2,3,5}.
parts=[]
for a in range(1,N):
  for b in range(a+1,N):
    for c in range(b+1,N):
      for d in range(c+1,N):
        if a+b+c+d==N: parts.append((a,b,c,d))
assert parts==[(1,2,3,5)]
assert 1+2==3 # explicit failure of subset-sum genericity

print('VERIFY_OK')
print('facets',len(facets),'f_vector',tuple(map(len,faces)))
print('boundary_ranks_Q',ranks,'betti_Z',tuple(betti),'unit_minor_dets',{d:c['det'] for d,c in MINORS.items()})
print('vertex_link_f_vector',tuple(map(len,link_faces)),'vertex_link_betti_Z',tuple(link_betti))
print('vertex_link_morse_critical',counts,'pairs',len(pairs),'acyclic',True)
print('all_vertex_links_isomorphic_by_cyclic_translation',True)
