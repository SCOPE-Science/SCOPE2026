"""Exact finite verifier for a tetrahedral graph-metric Rips homology character.
Public mathematical data and reproducible computation only; no external dependencies.
"""
from itertools import combinations, permutations
from collections import Counter, deque
from fractions import Fraction

NAMES = [(a,b) for a in range(4) for b in range(4) if a!=b]
IDX = {v:i for i,v in enumerate(NAMES)}
ADJ = [set() for _ in NAMES]
for i,(a,b) in enumerate(NAMES):
    for j,(c,d) in enumerate(NAMES):
        if i!=j and (a==c or (a==d and b==c)):
            ADJ[i].add(j)
assert all(len(n)==3 for n in ADJ)
D=[]
for i in range(12):
    dist = {i:0}; q=deque([i])
    while q:
        u=q.popleft()
        for v in ADJ[u]:
            if v not in dist:
                dist[v]=dist[u]+1; q.append(v)
    assert len(dist)==12
    D.append([dist[j] for j in range(12)])
assert Counter(D[i][j] for i in range(12) for j in range(i+1,12))=={1:18,2:24,3:24}

def full_faces(r):
    return [C for k in range(1,13) for C in combinations(range(12), k)
            if all(D[u][v]<=r for u,v in combinations(C,2))]

def boundary_rank(lower, upper):
    idx={s:i for i,s in enumerate(lower)}
    pivots={}
    for sigma in upper:
        vector = 0
        for j in range(len(sigma)):
            vector ^= 1 << idx[sigma[:j]+sigma[j+1:]]
        while vector:
            pivot=vector.bit_length()-1
            if pivot not in pivots:
                pivots[pivot]=vector; break
            vector ^= pivots[pivot]
    return len(pivots)

def perm_sign(xs):
    return -1 if sum(xs[i]>xs[j] for i in range(len(xs)) for j in range(i+1,len(xs)))%2 else 1

def cycle_type(p):
    left=set(range(4)); lengths=[]
    while left:
        u=min(left); v=u; cnt=0
        while v in left:
            left.remove(v); cnt+=1;v=p[v]
        lengths.append(cnt)
    return tuple(sorted(lengths, reverse=True))

def lefschetz(faces, p):
    act=[IDX[(p[a],p[b])] for a,b in NAMES]
    total=0
    for s in faces:
        image=[act[i] for i in s]
        if sorted(image)==list(s):
            total += (-1)**(len(s)-1)*perm_sign(image)
    return total

F1=full_faces(1); F2=full_faces(2)
assert Counter(map(len,F1))=={1:12,2:18,3:4}
assert Counter(map(len,F2))=={1:12,2:42,3:48,4:12}
faces1={k:[s for s in F1 if len(s)==k] for k in range(1,4)}
faces2={k:[s for s in F2 if len(s)==k] for k in range(1,5)}
r11=boundary_rank(faces1[1],faces1[2]);r12=boundary_rank(faces1[2],faces1[3]);
r21=boundary_rank(faces2[1],faces2[2]);r22=boundary_rank(faces2[2],faces2[3]);r23=boundary_rank(faces2[3],faces2[4]);
assert (r11,r12)==(11,4),(r11,r12)
assert (r21,r22,r23)==(11,31,12),(r21,r22,r23)
# r1: connected, H1 rank 18-11-4=3; no H2.
# r2: connected, H1 rank 42-11-31=0; H2 rank 48-31-12=5; no H3.
# Mod-two ranks already attain maximal possible rational ranks due d^2=0.
classes = [(1,1,1,1),(2,1,1),(2,2),(3,1),(4,)]
chars1={};chars2={}; counts=Counter()
for p in permutations(range(4)):
    t=cycle_type(p);counts[t]+=1
    u=lefschetz(F1,p);v=lefschetz(F2,p)
    if t in chars1:
        assert chars1[t]==u and chars2[t]==v
    else:
        chars1[t]=u;chars2[t]=v
assert [counts[t] for t in classes]==[1,6,3,8,6]
assert [chars1[t] for t in classes]==[-2,2,2,1,0]
assert [chars2[t] for t in classes]==[6,2,2,3,0]
chi_H1=[1-chars1[t] for t in classes]
chi_H2=[chars2[t]-1 for t in classes]
assert chi_H1==[3,-1,-1,0,1]
assert chi_H2==[5,1,1,2,-1]
characters={
    'trivial': [1,1,1,1,1],
    'sign': [1,-1,1,1,-1],
    'standard': [3,1,-1,0,-1],
    'sign_standard':[3,-1,-1,0,1],
    'two_dimensional':[2,0,2,-1,0],
}
weight=[1,6,3,8,6]
def multiplicities(chi):
    x={key:Fraction(sum(a*b*m for a,b,m in zip(chi,c,weight)),24)
       for key,c in characters.items()}
    assert all(v.denominator==1 and v>=0 for v in x.values())
    return {k:int(v) for k,v in x.items() if v}
assert multiplicities(chi_H1)=={'sign_standard':1}
assert multiplicities(chi_H2)=={'trivial':1,'sign':1,'standard':1}
assert (sum(weight[i]*chi_H1[i] for i in range(5))//24)==0
assert (sum(weight[i]*chi_H2[i] for i in range(5))//24)==1
assert (chi_H2[0]+3*chi_H2[2]+8*chi_H2[3])//12==2
print('TETRAHEDRAL_EQUIVARIANT_CHARACTER_OK')
print('rank_GF2_r1',r11,r12, 'rank_GF2_r2',r21,r22,r23)
print('Lefschetz_r1', [chars1[t] for t in classes])
print('Lefschetz_r2', [chars2[t] for t in classes])
print('H1_char',chi_H1,'H2_char',chi_H2)
print('H1',multiplicities(chi_H1),'H2',multiplicities(chi_H2))
