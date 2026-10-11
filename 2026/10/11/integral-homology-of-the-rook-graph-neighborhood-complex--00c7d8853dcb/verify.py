#!/usr/bin/env python3
from itertools import combinations
from collections import Counter, deque

N=16
def rc(v): return divmod(v,4)
adj={v:set() for v in range(N)}
for u,v in combinations(range(N),2):
    ru,cu=rc(u); rv,cv=rc(v)
    if ru==rv or cu==cv:
        adj[u].add(v); adj[v].add(u)
assert all(len(adj[v])==6 for v in range(N))
for u,v in combinations(range(N),2):
    assert len(adj[u]&adj[v])==2

faces=set()
for v in range(N):
    nb=sorted(adj[v])
    for r in range(1,7):
        for s in combinations(nb,r):
            faces.add(sum(1<<x for x in s))
fv=Counter(m.bit_count()-1 for m in faces)
assert len(faces)==808
assert tuple(fv[d] for d in range(6))==(16,120,320,240,96,16)

order=[9,1,6,13,11,3,5,8,7,14,0,12,10,15,2,4]
remaining=set(faces); pairs=[]
for v in order:
    b=1<<v
    for lo in sorted(m for m in remaining if not(m&b) and (m|b) in remaining):
        hi=lo|b
        if lo in remaining and hi in remaining:
            pairs.append((lo,hi,v))
            remaining.remove(lo); remaining.remove(hi)
crit=sorted(remaining)
cc=Counter(m.bit_count()-1 for m in crit)
assert len(pairs)==375 and len(crit)==58
assert dict(cc)=={0:1,1:1,2:56}

# Complete Forman acyclicity check on every nonempty face-poset cover.
pairset={(a,b) for a,b,_ in pairs}
indeg={m:0 for m in faces}; out={m:[] for m in faces}; covers=0
for hi in faces:
    t=hi
    while t:
        b=t&-t; t-=b
        lo=hi^b
        if lo==0 or lo not in faces: continue
        a,c=(hi,lo) if (lo,hi) in pairset else (lo,hi)
        out[a].append(c); indeg[c]+=1; covers+=1
q=deque([m for m,d in indeg.items() if d==0]); seen=0
while q:
    x=q.popleft(); seen+=1
    for y in out[x]:
        indeg[y]-=1
        if indeg[y]==0:q.append(y)
assert covers==2736 and seen==808

# H_1 over Z. The 1-skeleton is K_16. Relative to the star spanning tree at 0,
# the integral cycle lattice has basis z_ij=e_0i+e_ij-e_0j, 1<=i<j<=15.
basis=[(i,j) for i in range(1,16) for j in range(i+1,16)]
idx={e:k for k,e in enumerate(basis)}
triangles=sorted(tuple(i for i in range(N) if (m>>i)&1)
                 for m in faces if m.bit_count()==3)
assert len(triangles)==320
cols=[]
for a,b,c in triangles:
    x=[0]*105
    if a==0:
        x[idx[(b,c)]]=1
    else:
        x[idx[(b,c)]]+=1
        x[idx[(a,c)]]-=1
        x[idx[(a,b)]]+=1
    cols.append(x)

def rank_mod_p(p):
    A=[[cols[j][i]%p for j in range(len(cols))] for i in range(105)]
    r=0
    for c in range(len(cols)):
        pivot=next((i for i in range(r,105) if A[i][c]),None)
        if pivot is None: continue
        A[r],A[pivot]=A[pivot],A[r]
        inv=pow(A[r][c],-1,p)
        A[r]=[(z*inv)%p for z in A[r]]
        for i in range(r+1,105):
            if A[i][c]:
                f=A[i][c]
                A[i]=[(A[i][j]-f*A[r][j])%p for j in range(len(cols))]
        r+=1
        if r==105: break
    return r
assert rank_mod_p(2)==104
assert rank_mod_p(3)==105
assert rank_mod_p(5)==105

unit_cols=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,61,63,65,67,69,71,73,74,75,76,77,78,79,81,82,85,86,88,90,92,94,96,97,102,103,105,107,109,110,118,121,123,129,132,136,137,139,141,151,152,154,160,162,172]
full_cols=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,61,63,65,67,69,71,73,74,75,76,77,78,79,81,82,85,86,88,90,92,94,96,97,102,103,105,107,109,110,118,121,123,126,129,132,136,137,139,141,151,152,154,160,162,172]

def bareiss(A):
    A=[row[:] for row in A]
    n=len(A)
    if n==0:return 1
    sign=1; prev=1
    for k in range(n-1):
        if A[k][k]==0:
            p=next((i for i in range(k+1,n) if A[i][k]!=0),None)
            if p is None:return 0
            A[k],A[p]=A[p],A[k]; sign=-sign
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                A[i][j]=(A[i][j]*pivot-A[i][k]*A[k][j])//prev
        prev=pivot
        for i in range(k+1,n): A[i][k]=0
        for j in range(k+1,n): A[k][j]=0
    return sign*A[-1][-1]

# A unit 104-minor forces the first 104 Smith factors to 1.
rows104=[i for i in range(105) if i!=2]
A104=[[cols[j][i] for j in unit_cols] for i in rows104]
assert bareiss(A104)==1

# This full-rank 105-minor has determinant -2. Since rank mod 2 is only 104,
# every 105-minor is even. Thus the gcd of all 105-minors is exactly 2.
A105=[[cols[j][i] for j in full_cols] for i in range(105)]
assert bareiss(A105)==-2

# Therefore coker(B)=Z/2. This is H_1 because the chosen z_ij form the full
# integral cycle lattice of K_16 and triangle boundaries generate im(d_2).
# The Morse model has cells only in dimensions 0,1,2, so H_i=0 for i>=3.
# Euler characteristic is 56 and rank H_1=0, hence H_2 is free of rank 55.
chi=sum(((-1)**d)*fv[d] for d in range(6))
assert chi==56

print("graph=H(2,4)=K4_square_K4")
print("faces=808")
print("f_vector=(16,120,320,240,96,16)")
print("hasse_covers=2736")
print("morse_pairs=375")
print("critical_cells=(1,1,56)")
print("triangle_relation_ranks_mod_2_3_5=(104,105,105)")
print("smith_certificate=unit_104_minor:1,full_105_minor:-2,all_full_minors_even")
print("integral_homology=H0:Z,H1:Z/2,H2:Z^55,H>=3:0")
print("VERIFY_OK")
