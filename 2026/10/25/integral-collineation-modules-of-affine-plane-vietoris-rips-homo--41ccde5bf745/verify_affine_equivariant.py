#!/usr/bin/env python3
"""Independent finite checks for integral symmetry formulas of affine incidence Rips complexes.
No external dependencies. Finite checks supplement the universal proof.
"""
from itertools import combinations, product
from collections import Counter, defaultdict
from math import gcd

Q=3
points=list(product(range(Q),repeat=2))
pid={p:i for i,p in enumerate(points)}
normals=((1,0),(0,1),(1,1),(1,2))
lines=[]; classes=[]
for a,b in normals:
    row=[]
    for c in range(Q):
        S=frozenset(pid[(x,y)] for x,y in points if (a*x+b*y)%Q==c)
        assert len(S)==Q
        row.append(len(lines));lines.append(S)
    classes.append(tuple(row))
line_id={S:i for i,S in enumerate(lines)}
assert len(lines)==12 and len(set(lines))==12
assert all(sum(int(p in L) for L in lines)==4 for p in range(9))
assert all(sum(int(x in L and y in L) for L in lines)==1 for x,y in combinations(range(9),2))

subsets=lambda S: (tuple(c) for k in range(len(S)+1) for c in combinations(S,k))
# The scale-two Vietoris-Rips faces assembled independently from the distance conditions.
U=set(tuple(c) for c in subsets(tuple(range(9))) if c)
for i,L in enumerate(lines):
    v=9+i
    for c in subsets(sorted(L)):U.add(tuple(sorted((v,)+c)))
B=set()
for choices in product((-1,0,1,2),repeat=4):
    if all(c==-1 for c in choices):continue
    B.add(tuple(sorted(9+classes[d][c] for d,c in enumerate(choices) if c>=0)))
V=set(B)
for p in range(9):
    for c in subsets(tuple(9+j for j,L in enumerate(lines) if p in L)):
        V.add(tuple(sorted((p,)+c)))
W=U&V
assert len(W)==21+36
assert all((len(s)==1 or len(s)==2 and s[0]<9<=s[1] and s[0] in lines[s[1]-9]) for s in W)
K=U|V
# Independent reconstruction from shortest-path distances and clique enumeration.
from collections import deque
adj={i:set() for i in range(21)}
for j,L in enumerate(lines):
    for p in L:
        adj[p].add(9+j);adj[9+j].add(p)
dists=[]
for src in range(21):
    dst={src:0};queue=deque([src])
    while queue:
        v=queue.popleft()
        for w in adj[v]:
            if w not in dst:dst[w]=dst[v]+1;queue.append(w)
    assert len(dst)==21
    dists.append(dst)
assert all(dists[p][v]<=3 for p in range(9) for v in range(21))
assert max(dists[0].values())==3
N={i:{j for j in range(21) if j!=i and dists[i][j]<=2} for i in range(21)}
independent_cliques=set()
def enum(prefix,candidates):
    for a,v in enumerate(candidates):
        s=prefix+(v,)
        independent_cliques.add(s)
        enum(s,[w for w in candidates[a+1:] if w in N[v]])
enum(tuple(),list(range(21)))
assert independent_cliques==K,('distance_two_clique_mismatch',len(independent_cliques),len(K))
fv=[sum(len(s)==k for s in K) for k in range(1,10)]
assert fv==[21,126,282,255,135,84,36,9,1],fv
assert [sum(len(s)==k for s in B) for k in range(1,5)]==[12,54,108,81]

def rank_mod2_columns(faces_below,faces):
    ix={s:i for i,s in enumerate(faces_below)}
    piv={}
    for face in faces:
        n=0
        for j in range(len(face)):
            n ^= 1 << ix[face[:j]+face[j+1:]]
        while n:
            k=n.bit_length()-1
            if k in piv:n^=piv[k]
            else:piv[k]=n;break
    return len(piv)

bydim={j:sorted(s for s in K if len(s)==j+1) for j in range(9)}
rank={j:rank_mod2_columns(bydim[j-1],bydim[j]) for j in range(1,9)}
betti={j:len(bydim[j])-rank.get(j,0)-rank.get(j+1,0) for j in range(9)}
assert [betti[j] for j in range(9)]==[1,0,16,16,0,0,0,0,0],betti

def sign_of_reorder(t):
    return -1 if sum(t[i]>t[j] for i in range(len(t)) for j in range(i+1,len(t)))%2 else 1

def lef_reduced(faces,perm):
    total=-1 # reduced C_{-1} correction
    for s in faces:
        t=tuple(perm[v] for v in s)
        if tuple(sorted(t))==s:
            total+=((-1)**(len(s)-1))*sign_of_reorder(t)
    return total

def det(A):return (A[0]*A[3]-A[1]*A[2])%Q

count=0
trans_trace=Counter();group_class_trace=Counter()
for A in product(range(Q),repeat=4):
    if det(A)==0:continue
    for shift in points:
        pmap=tuple(pid[((A[0]*x+A[1]*y+shift[0])%Q,(A[2]*x+A[3]*y+shift[1])%Q)] for x,y in points)
        lmap=tuple(line_id[frozenset(pmap[p] for p in L)] for L in lines)
        perm=pmap+tuple(9+k for k in lmap)
        newclass=tuple(next(j for j,D in enumerate(classes) if lmap[C[0]] in D) for C in classes)
        assert sorted(newclass)==list(range(4))
        for i,C in enumerate(classes):assert {lmap[t] for t in C}==set(classes[newclass[i]])
        fixed_flag=sum(pmap[p]==p and lmap[l]==l for l,L in enumerate(lines) for p in L)
        fixed_point=sum(pmap[p]==p for p in range(9))
        fixed_line=sum(lmap[j]==j for j in range(12))
        chi2=fixed_flag-fixed_point-fixed_line+1
        chi3=sign_of_reorder(newclass)
        visited=set()
        for start in range(4):
            if start in visited:continue
            orbit=[];j=start
            while j not in visited:
                visited.add(j);orbit.append(j);j=newclass[j]
            length=len(orbit)
            nfix=0
            for l in classes[start]:
                t=l
                for _ in range(length):t=lmap[t]
                nfix+=(t==l)
            chi3*=nfix-1
        assert lef_reduced(K,perm)==chi2-chi3,(A,shift,chi2,chi3)
        bperm=tuple(lmap[j] for j in range(12))
        assert lef_reduced(B,perm)==-chi3,(A,shift,chi3)
        group_class_trace[(chi2,chi3)]+=1
        if A==(1,0,0,1):trans_trace[(shift,chi2,chi3)]+=1
        count+=1
assert count==432,count
assert sum(k[0]==(0,0) and k[1]==16 and k[2]==16 for k in trans_trace)==1
assert all(chi2==-2 and chi3==-2 for (shift,chi2,chi3),mult in trans_trace.items() if shift!=(0,0))
assert (16+8*(-2))//9==0
print('AFFINE_INTEGRAL_MODULE_VERIFIED', 'q=3', 'elements='+str(count), 'faces='+str(len(K)), 'homology='+str([betti[j] for j in range(4)]),'character_classes='+str(len(group_class_trace)))
print('AFFINE_TRANSLATION_QUOTIENT_VERIFIED', 'q=3', 'dimension_H2=0', 'dimension_H3=0')
for q in [3,4,5,7,8,9]:
    numerator=(q-1)**(q+1)+(q*q-1)*(q-1)*((-1)**q)
    assert numerator% (q*q)==0
    print('TRANSLATION_FORMULA',q, numerator//(q*q))
