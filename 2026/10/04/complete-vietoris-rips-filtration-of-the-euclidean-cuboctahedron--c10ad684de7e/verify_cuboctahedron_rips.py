#!/usr/bin/env python3
from itertools import combinations, product
from collections import Counter, deque
from math import comb

# Cuboctahedron vertices: all permutations of (±1, ±1, 0), lexicographic order.
V = sorted({tuple(x) for z in range(3) for a in (-1,1) for b in (-1,1)
            for x in [tuple(0 if i==z else (a if i==[j for j in range(3) if j!=z][0] else b) for i in range(3))]})
# Rebuild more transparently and cross-check the set above.
V2=[]
for z in range(3):
    idx=[i for i in range(3) if i!=z]
    for a in (-1,1):
        for b in (-1,1):
            p=[0,0,0]; p[idx[0]]=a; p[idx[1]]=b
            V2.append(tuple(p))
assert V == sorted(set(V2)) and len(V)==12

N=len(V)
def d2(i,j):
    return sum((V[i][k]-V[j][k])**2 for k in range(3))

dvals=sorted({d2(i,j) for i,j in combinations(range(N),2)})
assert dvals == [2,4,6,8]

# Canonical geometric faces.
tri_faces=set()
for s in product((-1,1), repeat=3):
    f=frozenset(i for i,p in enumerate(V) if all(p[k]==0 or p[k]==s[k] for k in range(3)))
    assert len(f)==3
    tri_faces.add(f)
assert len(tri_faces)==8
sq_faces=set()
for k in range(3):
    for eps in (-1,1):
        f=frozenset(i for i,p in enumerate(V) if p[k]==eps)
        assert len(f)==4
        sq_faces.add(f)
assert len(sq_faces)==6


def faces_at(th):
    faces=[]
    for mask in range(1,1<<N):
        s=tuple(i for i in range(N) if mask>>i & 1)
        if all(d2(i,j)<=th for i,j in combinations(s,2)):
            faces.append(frozenset(s))
    return set(faces)

def maximal_faces(faces):
    return {s for s in faces if not any(len(t)==len(s)+1 and s<t for t in faces)}

def fvector(faces):
    c=Counter(len(s)-1 for s in faces)
    return tuple(c[k] for k in range(max(c)+1))

def gf2_rank(columns):
    piv={}
    rank=0
    for x in columns:
        while x:
            p=x.bit_length()-1
            if p in piv:
                x ^= piv[p]
            else:
                piv[p]=x; rank += 1; break
    return rank

def betti_mod2(faces):
    md=max(len(s)-1 for s in faces)
    by={k:sorted([tuple(sorted(s)) for s in faces if len(s)==k+1]) for k in range(md+1)}
    ranks=[]
    for k in range(1,md+1):
        row={s:i for i,s in enumerate(by[k-1])}
        cols=[]
        for s in by[k]:
            x=0
            for face in combinations(s,k):
                x ^= 1<<row[face]
            cols.append(x)
        ranks.append(gf2_rank(cols))
    bet=[]
    for k in range(md+1):
        left=ranks[k-1] if k>=1 else 0
        right=ranks[k] if k<len(ranks) else 0
        bet.append(len(by[k])-left-right)
    return tuple(ranks),tuple(bet)

def greedy_matching(faces):
    unmatched=set(faces); pairs=[]
    for v in range(N):
        lows=[s for s in unmatched if v not in s and frozenset(set(s)|{v}) in unmatched]
        for s in sorted(lows,key=lambda q:(len(q),tuple(sorted(q)))):
            t=frozenset(set(s)|{v})
            if s in unmatched and t in unmatched:
                unmatched.remove(s); unmatched.remove(t); pairs.append((s,t))
    return pairs,unmatched

def check_acyclic(faces,pairs):
    pairset={(a,b) for a,b in pairs}
    nodes=list(faces); idx={s:i for i,s in enumerate(nodes)}
    out=[[] for _ in nodes]; indeg=[0]*len(nodes); covers=0
    for t in nodes:
        if len(t)<=1: continue
        for v in t:
            s=frozenset(set(t)-{v})
            if not s: continue
            covers += 1
            # Hasse orientation: matched cover upward, otherwise downward.
            if (s,t) in pairset: a,b=s,t
            else: a,b=t,s
            out[idx[a]].append(idx[b]); indeg[idx[b]]+=1
    dq=deque(i for i,d in enumerate(indeg) if d==0); seen=0
    while dq:
        u=dq.popleft(); seen+=1
        for w in out[u]:
            indeg[w]-=1
            if indeg[w]==0: dq.append(w)
    assert seen==len(nodes)
    return covers

expected={
 2: ((12,24,8),(11,8),(1,5,0), Counter({0:1,1:5})),
 4: ((12,36,32,6),(11,25,6),(1,0,1,0), Counter({0:1,2:1})),
 6: ((12,60,160,240,192,64),(11,49,111,129,63),(1,0,0,0,0,1), Counter({0:1,5:1})),
 8: ((12,66,220,495,792,924,792,495,220,66,12,1),(11,55,165,330,462,462,330,165,55,11,1),(1,0,0,0,0,0,0,0,0,0,0,0), None)
}

for th in (2,4,6,8):
    F=faces_at(th)
    fv=fvector(F); ranks,bet=betti_mod2(F)
    assert fv==expected[th][0]
    assert ranks==expected[th][1]
    assert bet==expected[th][2]
    M=maximal_faces(F)
    if th==2:
        assert M==tri_faces
    elif th==4:
        assert M==tri_faces|sq_faces
    elif th==6:
        opposite={frozenset((i,V.index(tuple(-x for x in V[i])))) for i in range(N)}
        assert len(opposite)==6
        assert all(d2(*tuple(p))==8 for p in opposite)
        assert len(M)==64 and all(len(s)==6 for s in M)
        assert all(all(len(s & p)==1 for p in opposite) for s in M)
        assert fv==tuple((2**(k+1))*comb(6,k+1) for k in range(6))
    else:
        assert M=={frozenset(range(N))}
    if th<8:
        pairs,crit=greedy_matching(F)
        covers=check_acyclic(F,pairs)
        cc=Counter(len(s)-1 for s in crit)
        assert cc==expected[th][3]
        print('threshold_sq',th,'faces',len(F),'f',fv,'ranks',ranks,'betti',bet,'pairs',len(pairs),'covers',covers,'critical',dict(sorted(cc.items())))
    else:
        print('threshold_sq',th,'faces',len(F),'f',fv,'ranks',ranks,'betti',bet)

# Intersection patterns of maximal simplices at threshold 2 and 4 are exactly the
# intersection patterns of the corresponding geometric face families, because the
# simplices use precisely the face vertex sets. This is the finite input for the nerve argument.
assert maximal_faces(faces_at(2))==tri_faces
assert maximal_faces(faces_at(4))==tri_faces|sq_faces

print('VERIFY_OK')
