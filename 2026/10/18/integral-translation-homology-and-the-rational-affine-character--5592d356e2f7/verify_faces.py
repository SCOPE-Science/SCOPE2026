#!/usr/bin/env python3
"""Exact face, integral boundary, and equivariant Lefschetz checks for the Paley-17 flag complex."""
from itertools import combinations
from collections import Counter

P = 17
R = {x*x % P for x in range(1,P)}
assert R == {1,2,4,8,9,13,15,16}
adj = lambda u,v: (v-u)%P in R
V = [(i,) for i in range(P)]
E = [(i,j) for i,j in combinations(range(P),2) if adj(i,j)]
T = [(i,j,k) for i,j,k in combinations(range(P),3) if adj(i,j) and adj(i,k) and adj(j,k)]
assert (len(V),len(E),len(T))==(17,68,68)
assert not any(all(adj(x,y) for x,y in combinations(f,2)) for f in combinations(range(P),4))
index = {e:i for i,e in enumerate(E)}
B = [[0]*len(T) for _ in E]
for j,(i,k,l) in enumerate(T):
    B[index[(k,l)]][j]=1
    B[index[(i,l)]][j]=-1
    B[index[(i,k)]][j]=1

# Fixed explicitly enumerated unimodular 52x52 minor, in lexicographic indexing.
C = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,44,45,46,47,49,52,56,59,61]
I = [0,1,2,3,4,5,6,8,9,10,11,12,13,15,16,17,18,19,21,22,23,24,25,27,28,29,30,32,33,34,35,37,38,39,40,42,43,44,45,47,48,49,51,52,54,55,57,58,60,61,63,65]
assert len(C)==len(I)==52
M = [[B[i][j] for j in C] for i in I]

def bareiss(A):
    A=[list(x) for x in A]
    n=len(A)
    sign=1
    last=1
    for k in range(n-1):
        if A[k][k]==0:
            next_row=next((i for i in range(k+1,n) if A[i][k]),None)
            if next_row is None:return 0
            A[k],A[next_row]=A[next_row],A[k]
            sign=-sign
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator=A[i][j]*pivot-A[i][k]*A[k][j]
                assert numerator%last==0
                A[i][j]=numerator//last
            A[i][k]=0
        last=pivot
    return sign*A[-1][-1]

assert bareiss(M)==-1
# Because the 1-skeleton is connected, rank(∂1)=16, and ∂1∂2=0,
# the rank of ∂2 is at most 68-16=52; unimodular minor proves rank exactly 52,
# and primitive image, so H1=0 integrally, H2=Z^16.
seen={0}; pending=[0]
while pending:
    i=pending.pop()
    for j in range(P):
        if j not in seen and adj(i,j):seen.add(j);pending.append(j)
assert len(seen)==P

def sign(seq):
    return -1 if sum(a>b for i,a in enumerate(seq) for b in seq[i+1:])%2 else 1

def trace(faces,a,b):
    t=0
    for F in faces:
        image=tuple((a*v+b)%P for v in F)
        if tuple(sorted(image))==F:t+=sign(image)
    return t

classes=Counter()
for a in R:
    for b in range(P):
        assert all(adj((a*u+b)%P,(a*v+b)%P) for u,v in E)
        tr0,tr1,tr2=(trace(F,a,b) for F in (V,E,T))
        chi=tr2-tr1+tr0-1
        target=sum(1 for x in range(P) if (a*x+b)%P==x)-1
        assert chi==target,(a,b,tr0,tr1,tr2,chi,target)
        classes[(a==1,b==0,a==16,chi)]+=1
assert sum(classes.values())==136
assert sorted(set(k[-1] for k in classes))==[-1,0,16]
assert sum(n for k,n in classes.items() if k[-1]==16)==1
assert sum(n for k,n in classes.items() if k[-1]==-1)==16
assert sum(n for k,n in classes.items() if k[-1]==0)==119
print('faces',len(V),len(E),len(T))
print('unimodular_minor',len(I),len(C),-1)
print('reduced_integral_homology: H2=Z^16, others=0')
print('affine elements',136,'H2 character distribution',{'16':1,'-1':16,'0':119})
print('rational representation: augmentation module of Q[F17]')
