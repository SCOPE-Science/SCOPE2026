#!/usr/bin/env python3
"""Exact arithmetic finite certificate for a symmetric-group word-language invariant.
Uses only the Python standard library. Run: python3 verify_s4.py
"""
from itertools import permutations
from collections import defaultdict

I=(0,1,2,3)
a=(1,2,3,0) # (0 1 2 3)
b=(1,0,2,3) # (0 1)
G=set(permutations(range(4)))
def mul(p,q):return tuple(p[q[i]] for i in range(4))
assert len(G)==24 and {a,b}<=G
# Check the generators generate S4 as a group, with positive words.
H={I}
while True:
    X=H|{mul(g,c) for g in H for c in (a,b)}
    if X==H:break
    H=X
assert len(H)==24

# Exact dynamic program over all word permutations with each Parikh vector.
N=24
D={}
W={}
for total in range(N+1):
    for i in range(total+1):
        j=total-i
        if (i,j)==(0,0):
            D[i,j]={I}; W[i,j]={I:''};continue
        row={}
        if i:
            for g,word in W[i-1,j].items():
                h=mul(g,a)
                if h not in row:row[h]=word+'a'
        if j:
            for g,word in W[i,j-1].items():
                h=mul(g,b)
                if h not in row:row[h]=word+'b'
        W[i,j]=row;D[i,j]=set(row)
        assert D[i,j]<=G
A={(i,j) for i,j in D if I in D[i,j]}
B=((0,2),(4,0),(3,3),(6,4),(9,3))
def generator_monoid(N):
    M={(0,0)}
    for total in range(1,N+1):
        for i in range(total+1):
            j=total-i
            if any(i>=u and j>=v and (i-u,j-v) in M for u,v in B):M.add((i,j))
    return M
assert A==generator_monoid(N),sorted(A^generator_monoid(N))
for u,v in B:
    word=W[u,v][I]
    assert word.count('a')==u and word.count('b')==v
    g=I
    for letter in word:g=mul(g,a if letter=='a' else b)
    assert g==I
    print('GENERATOR',u,v,word)
# Irredundancy: no generator can be produced by the other four.
for u,v in B:
    C=[t for t in B if t!=(u,v)]
    S={(0,0)}
    for t in range(1,u+v+1):
        for x in range(t+1):
            y=t-x
            if any(x>=s and y>=r and (x-s,y-r) in S for s,r in C):S.add((x,y))
    assert (u,v) not in S

def membership(i,j):
    if j%2==0:
        return i%4==0 or (j>=4 and i>=6 and i%4==2)
    return j>=3 and ((i>=3 and i%4==3) or (i>=9 and i%4==1))
for i in range(101):
    for j in range(101):
        if i+j<=N:assert membership(i,j)==((i,j) in A)
# Independent exhaustive testing on a much larger finite Parikh grid,
# not used to establish the infinite result.
M=generator_monoid(100)
for i in range(101):
    for j in range(101-i):assert membership(i,j)==((i,j) in M)

def cap_i(i):return i if i<=12 else 9+(i-9)%4
def cap_j(j):return j if j<=4 else 3+(j-3)%2
Q=[(i,j) for i in range(13) for j in range(5)]
index={p:s for s,p in enumerate(Q)}
T=[(index[(cap_i(i+1),j)],index[(i,cap_j(j+1))]) for i,j in Q]
final=[membership(*p) for p in Q]
assert len(Q)==65
# Reachability within the proposed DFA.
seen={index[0,0]}
while True:
    more=seen|{t for s in seen for t in T[s]}
    if more==seen:break
    seen=more
assert len(seen)==65
# Moore refinement, obtaining all the distinct Myhill-Nerode quotients.
P=[int(t) for t in final]
while True:
    sig=[(final[s],P[T[s][0]],P[T[s][1]]) for s in range(len(Q))]
    look={s:k for k,s in enumerate(sorted(set(sig)))}
    P2=[look[s] for s in sig]
    if all((P[s]==P[t])==(P2[s]==P2[t]) for s in range(len(Q)) for t in range(len(Q))):
        P=P2
        break
    P=P2
assert len(set(P))==44,len(set(P))
# Each partition cell is a right congruence, and all cells are inequivalent:
for s in range(65):
    for t in range(65):
        if P[s]==P[t]:
            assert final[s]==final[t] and P[T[s][0]]==P[T[t][0]] and P[T[s][1]]==P[T[t][1]]
# Independent witness distinguishability by suffixes of length <=64.
def distinguish():
    E={(s,t) for s in range(65) for t in range(65) if final[s]!=final[t]}
    for k in range(1,66):
        F=E|{(s,t) for s in range(65) for t in range(65)
             if (T[s][0],T[t][0]) in E or (T[s][1],T[t][1]) in E}
        if F==E:return k,E
        E=F
    raise AssertionError('distinguishability horizon exceeded')
horizon,diffs=distinguish()
for s in range(65):
    for t in range(65):
        assert ((s,t) in diffs)==(P[s]!=P[t])
# Compact class census: no class ambiguities allowed.
classes=defaultdict(list)
for p,c in zip(Q,P):classes[c].append(p)
assert sorted(map(len,classes.values()))==[1]*33+[2]*9+[7]*2
print('CERTIFICATE_OK |G|=24 finite_words<=24 generator_atoms=5 DFA_raw=65 DFA_min=44 horizon=',horizon)
