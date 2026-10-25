#!/usr/bin/env python3
"""Exact standalone verification for the cyclic-order-six partial-transversal complex.
Python standard library only. Produces finite, replayable acyclicity and integer certificates.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
N=6
ORDER=[22,26,7,34,3,15,19,24,1,5,33,14,13,32,8,10,29,23,4,20,2,18,28,35,27,30,25,16,0,11,17,31,12,9,21,6]
assert sorted(ORDER)==list(range(36))
faces_by_size=[[] for _ in range(7)]
def enum(row, face, used_cols, used_symbols):
    if row==N:
        if face: faces_by_size[len(face)].append(sum(1 << x for x in face))
        return
    enum(row+1, face, used_cols, used_symbols)
    for col in range(N):
        sym=(row+col)%N
        if not (used_cols>>col)&1 and not (used_symbols>>sym)&1:
            enum(row+1, face+[N*row+col], used_cols | (1<<col), used_symbols | (1<<sym))
enum(0,[],0,0)
assert [len(faces_by_size[k]) for k in range(1,7)] == [36,360,1200,1224,288,0]
faces=set(x for block in faces_by_size for x in block)
assert len(faces)==3108
# Every simplex is encoded by its 36-bit set of cells; values increasing by row.
remaining=set(faces)
pairs=[]
for v in ORDER:
    bit=1<<v
    for low in sorted(remaining):
        high=low|bit
        if not (low&bit) and high in remaining:
            remaining.remove(low);remaining.remove(high);pairs.append((low,high))
assert len(pairs)==1500
critical=Counter(c.bit_count()-1 for c in remaining)
assert critical=={0:1,2:23,3:84}, critical
up=dict(pairs);down={h:l for l,h in pairs}
# Orient all codimension-one inclusions upward when matched, downward otherwise.
out=defaultdict(list);deg=Counter();incidences=0
for high in faces:
    for v in range(36):
        if not (high>>v)&1: continue
        low=high&~(1<<v)
        if not low:continue
        incidences+=1
        a,b=(low,high) if up.get(low)==high else (high,low)
        out[a].append(b);deg[b]+=1
ready=deque(v for v in faces if deg[v]==0)
topo=0
while ready:
    x=ready.popleft();topo+=1
    for y in out[x]:
        deg[y]-=1
        if deg[y]==0:ready.append(y)
assert topo==len(faces)

def boundary(mask):
    t=[v for v in range(36) if mask>>v&1]
    return [(mask&~(1<<v),(-1)**i) for i,v in enumerate(t)]
critical_two=sorted(x for x in remaining if x.bit_count()==3)
critical_three=sorted(x for x in remaining if x.bit_count()==4)
critical_index={x:i for i,x in enumerate(critical_two)}
@lru_cache(None)
def project_two(t):
    if t in critical_index:return {critical_index[t]:1}
    if t in down:return {}
    assert t in up, (t, 'unhandled 2-simplex')
    high=up[t]; incidence=dict(boundary(high))[t]
    result=Counter()
    for f,s in boundary(high):
        if f==t:continue
        for i,z in project_two(f).items():result[i]-=incidence*s*z
    return {i:z for i,z in result.items() if z}
A=[[0]*len(critical_three) for _ in critical_two]
for j,t in enumerate(critical_three):
    for f,s in boundary(t):
        for i,z in project_two(f).items():A[i][j]+=s*z
assert sum(a!=0 for row in A for a in row)==327
assert max(abs(a) for row in A for a in row)==3
# Unimodular elementary row/column operations: Euclidean diagonalization.
# Multiplying rows/columns by +/-1 and adding integer multiples are invertible over Z.
B=[row[:] for row in A]; m=len(B);n=len(B[0]);diag=[]
k=0
while k<min(m,n):
    nonzero=[(abs(B[i][j]),i,j) for i in range(k,m) for j in range(k,n) if B[i][j]]
    if not nonzero: break
    _,i,j=min(nonzero)
    B[k],B[i]=B[i],B[k]
    for row in B:row[k],row[j]=row[j],row[k]
    passes=0
    while True:
        passes+=1
        assert passes < 20000, 'diagonalization failed to converge'
        changed=False
        for i in range(k+1,m):
            if B[i][k]:
                q=B[i][k]//B[k][k]
                for j in range(k,n):B[i][j]-=q*B[k][j]
                if B[i][k]:
                    B[i],B[k]=B[k],B[i]
                changed=True
                break
        if changed:continue
        for j in range(k+1,n):
            if B[k][j]:
                q=B[k][j]//B[k][k]
                for i in range(k,m):B[i][j]-=q*B[i][k]
                if B[k][j]:
                    for row in B:row[k],row[j]=row[j],row[k]
                changed=True
                break
        if changed:continue
        # Ensure Smith divisibility of the remaining block: if pivot does not
        # divide an entry, add its row to the pivot row and restart reductions.
        bad=next(((i,j) for i in range(k+1,m) for j in range(k+1,n) if B[i][j]%B[k][k]!=0),None)
        if bad is None:break
        i,j=bad
        for t in range(k,n):B[k][t]+=B[i][t]
    diag.append(abs(B[k][k])); k+=1
assert diag==[1]*9,diag
assert all(B[i][j]==(B[i][i] if i==j and i<len(diag) else 0) for i in range(m) for j in range(n))
print('VERIFY_OK faces', [len(faces_by_size[k]) for k in range(1,7)],
      'pairs',len(pairs),'incidences',incidences,'DAG',topo,
      'critical',dict(sorted(critical.items())),
      'morse_nonzero',327,'smith_units',len(diag),
      'betti2',23-len(diag),'betti3',84-len(diag))
