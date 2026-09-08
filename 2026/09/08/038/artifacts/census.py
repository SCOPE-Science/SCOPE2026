#!/usr/bin/env python3
"""Braid-orbit census for Nielsen class (PSL(2,7),(2A,3A,7A,7A)).
Model: G = PSL(2,7) = SL(2,7)/{+-I}, matrices over F7 as (a,b,c,d).
Steps: group table, classes, Nielsen enumeration (all 12 position patterns),
full-braid BFS, conjugation-quotient BFS, Schur (SL) lift invariant check,
explicit braid-word path witness. Stdlib only. Prints results JSON.
"""
import json, itertools, collections, sys

P = 7
def mat(a,b,c,d): return (a%P,b%P,c%P,d%P)
def mul(m,n): return mat(m[0]*n[0]+m[1]*n[2], m[0]*n[1]+m[1]*n[3], m[2]*n[0]+m[3]*n[2], m[2]*n[1]+m[3]*n[3])
def det(m): return (m[0]*m[3]-m[1]*m[2])%P
def inv(m): return mat(m[3],-m[1],-m[2],m[0])  # det=1
def neg(m): return ((-m[0])%P,(-m[1])%P,(-m[2])%P,(-m[3])%P)
ONE = mat(1,0,0,1)

# SL(2,7): 336 elements
SL = [mat(a,b,c,d) for a in range(P) for b in range(P) for c in range(P) for d in range(P) if (a*d-b*c)%P==1]
assert len(SL)==336, len(SL)
# PSL: identify m ~ -m, canonical = lex-min
def can(m):
    n = neg(m); return m if m<=n else n
EL = sorted(set(can(m) for m in SL))
assert len(EL)==168
idx = {g:i for i,g in enumerate(EL)}
MUL = [[0]*168 for _ in range(168)]
INV = [0]*168
for i,g in enumerate(EL):
    for j,h in enumerate(EL):
        MUL[i][j]=idx[can(mul(g,h))]
    INV[i]=idx[can(inv(g))]
def prod(*xs):
    r=idx[ONE]
    for x in xs: r=MUL[r][x]
    return r
def order(i):
    r=i; k=1
    while r!=idx[ONE]: r=MUL[r][i]; k+=1
    return k
ORD=[order(i) for i in range(168)]
# conjugacy classes in PSL
def conj(h,x): return MUL[MUL[h][x]][INV[h]]
seen=[False]*168; CLASSES=[]
for x in range(168):
    if not seen[x]:
        c=sorted(set(conj(h,x) for h in range(168)))
        for y in c: seen[y]=True
        CLASSES.append(c)
CLASSES.sort(key=len)
info=[(len(c),ORD[c[0]]) for c in CLASSES]
print("classes (size,order):",info,file=sys.stderr)
C2=[c for c in CLASSES if len(c)==21 and ORD[c[0]]==2][0]
C3=[c for c in CLASSES if len(c)==56 and ORD[c[0]]==3][0]
C7s=[c for c in CLASSES if len(c)==24 and ORD[c[0]]==7]
assert len(C2)==21 and len(C3)==56 and len(C7s)==2, info
u=idx[can(mat(1,1,0,1))]
C7A=[c for c in C7s if u in c][0]
C7B=[c for c in C7s if u not in c][0]
S2A,S3A,S7A,S7B=set(C2),set(C3),set(C7A),set(C7B)
print("7A contains [[1,1],[0,1]]:",u in S7A," sizes:",len(C2),len(C3),len(C7A),len(C7B),file=sys.stderr)

# outer automorphism: conjugation by diag(1,3) (det 3 nonsquare) on SL, descends to PSL
D=mat(1,0,0,3); Di=mat(1,0,0,5)
def aut(g): return idx[can(mul(mul(D,EL[g]),Di))]
AUT=[aut(g) for g in range(168)]
print("outer swaps 7A/7B:", {AUT[g] for g in C7A}==S7B, " fixes 2A:",{AUT[g] for g in C2}==S2A," fixes 3A:",{AUT[g] for g in C3}==S3A,file=sys.stderr)

# generation test via subgroup BFS
def generates(t):
    s={idx[ONE]}; s.update(t); st=list(s)
    while st:
        x=st.pop()
        for y in list(t):
            for z in (MUL[x][y],MUL[y][x]):
                if z not in s: s.add(z); st.append(z)
                if len(s)==168: return True
    return len(s)==168

# enumerate Nielsen tuples for each distinct position pattern of multiset {2A,3A,7A,7A}
pats=sorted(set(itertools.permutations(["2","3","7","7"])))
POOLS={"2":C2,"3":C3,"7":C7A}
N=[]; per_pat={}
for pat in pats:
    A,B,C,Dp=POOLS[pat[0]],POOLS[pat[1]],POOLS[pat[2]],POOLS[pat[3]]
    need=S7A if pat[3]=="7" else (S2A if pat[3]=="2" else S3A)
    got=[]
    for a in A:
        for b in B:
            ab=MUL[a][b]
            for c in C:
                g4=MUL[INV[MUL[ab][c]]][idx[ONE]]  # (abc)^{-1}
                if g4 in need:
                    t=(a,b,c,g4)
                    if generates(t): got.append(t)
    per_pat["".join(pat)]=len(got); N.extend(got)
print("patterns:",per_pat,file=sys.stderr)
print("|N| =",len(N),file=sys.stderr)
NSET=set(N)
assert len(NSET)==len(N)
assert all(prod(*t)==idx[ONE] for t in N)

# braid moves sigma1..sigma3 and inverses on 4-tuples
def sig(t,i,inv_):
    t=list(t)
    if not inv_: a=t[i]; b=t[i+1]; t[i]=MUL[MUL[a][b]][INV[a]]; t[i+1]=a
    else: a=t[i]; b=t[i+1]; t[i+1]=MUL[MUL[INV[b]][a]][b]; t[i]=b
    return tuple(t)
MOVES=[(i,s) for i in range(3) for s in (False,True)]
def moves(t):
    for i,s in MOVES:
        r=sig(t,i,s)
        assert r in NSET, ("braid leaves N!",t,i,s)
        yield (i,s),r

# full braid orbits on N (ordered tuples)
comp=[-1]*len(N); pos={t:k for k,t in enumerate(N)}; norb=0; sizes=[]
from collections import deque
for k in range(len(N)):
    if comp[k]<0:
        comp[k]=norb; dq=deque([N[k]]); n=0
        while dq:
            t=dq.popleft(); n+=1
            for _,r in moves(t):
                j=pos[r]
                if comp[j]<0: comp[j]=norb; dq.append(r)
        sizes.append(n); norb+=1
print("full-braid orbits on ordered tuples:",norb,sizes,file=sys.stderr)

# reduced (conjugation-quotient) BFS: canonical rep
def canon(t): return min(tuple(conj(h,x) for x in t) for h in range(168))
CREPS=sorted(set(canon(t) for t in N))
print("|N/G| =",len(CREPS),file=sys.stderr)
cpos={c:k for k,c in enumerate(CREPS)}
# braid descends: orbit BFS on canonical reps
rcomp=[-1]*len(CREPS); rnorb=0; rsizes=[]
for k in range(len(CREPS)):
    if rcomp[k]<0:
        rcomp[k]=rnorb; dq=deque([CREPS[k]]); n=0
        while dq:
            t=dq.popleft(); n+=1
            for _,r in moves(t):
                j=cpos[canon(r)]
                if rcomp[j]<0: rcomp[j]=rnorb; dq.append(r)
        rsizes.append(n); rnorb+=1
print("reduced braid orbits (components):",rnorb,rsizes,file=sys.stderr)
# closure/coverage certificate: every canonical rep assigned, sizes sum
assert sum(rsizes)==len(CREPS) and all(c>=0 for c in rcomp)

# orbit members (canonical reps) per component
members=collections.defaultdict(list)
for k,c in enumerate(CREPS): members[rcomp[k]].append(c)
rep={k:min(v) for k,v in members.items()}  # lex-min rep per component

# Schur lift invariant: lift each entry to SL(2,7); product of lifts in {+-I} -> sign.
# Well-definedness: for classes 2A,3A,7A use the canonical-section lift? Test: changing
# one lift flips sign, so fix section s(g)=lex-min of the two SL preimages; record sign.
# Then VERIFY braid-invariance computationally on all of N.
def lift(g):
    m=EL[g]; n=neg(m); return m if m<=n else n
def linv(t):
    r=lift(t[0])
    for x in t[1:]: r=mul(r,lift(x))
    return 1 if r==ONE else (-1 if r==neg(ONE) else 0)
VALS=[linv(t) for t in N]
assert all(v in (1,-1) for v in VALS)
ok=True
for t in N:
    v=linv(t)
    for _,r in moves(t):
        if linv(r)!=v: ok=False
print("lift invariant braid-stable on all N:",ok," value distribution:",{1:VALS.count(1),-1:VALS.count(-1)},file=sys.stderr)
# values per reduced component
compvals={}
for k in members:
    vs={linv(t) for t in members[k]}
    compvals[k]=sorted(vs)
print("lift values per component:",compvals,file=sys.stderr)

# explicit braid-word path witness inside component 0 (or largest)
def find_path(src,dst):
    prev={src:None}; dq=deque([src])
    while dq:
        t=dq.popleft()
        if t==dst: break
        for mv,r in moves(t):
            if r not in prev: prev[r]=(t,mv); dq.append(r)
    assert dst in prev
    word=[]; t=dst
    while prev[t] is not None: p,mv=prev[t]; word.append(mv); t=p
    word.reverse(); return word
def apply_word(t,word):
    for i,s in word: t=sig(t,i,s)
    return t
K0=max(members,key=lambda k: len(members[k]))
A=rep[K0]; B=[t for t in members[K0] if t!=A][0]
word=find_path(A,B)
assert apply_word(A,word)==B
print("witness: component",K0,"size",len(members[K0]),"word length",len(word),file=sys.stderr)

def name(t):
    return [EL[x] for x in t]
out={
 "group":"PSL(2,7)","classes":{"2A":21,"3A":56,"7A":24,"7B":24},
 "Nielsen_total_ordered":len(N),"per_pattern":per_pat,
 "full_braid_orbits":norb,"full_orbit_sizes":sorted(sizes),
 "reduced_components":rnorb,"reduced_sizes":sorted(rsizes),
 "lift_braid_stable":ok,"lift_dist":{ "plus1":VALS.count(1),"minus1":VALS.count(-1)},
 "lift_values_per_component":{str(k):v for k,v in compvals.items()},
 "witness":{"component":K0,"from":A,"to":B,"word":word,"length":len(word)},
 "reps":{str(k):list(v) for k,v in rep.items()},
}
json.dump(out,open("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-178/output/artifacts/results.json","w"))
print("WROTE results.json")
