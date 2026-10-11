#!/usr/bin/env python3
from itertools import combinations
from collections import Counter, defaultdict, deque
from fractions import Fraction

N=7
EDGES=[(i,j) for i in range(N) for j in range(i+1,N)]
EI={e:k for k,e in enumerate(EDGES)}
DOM=[]
for d in (1,2,3):
    for D0 in combinations(range(N),d):
        D=set(D0); groups=[]
        for v in range(N):
            if v not in D:
                g=0
                for u in D:
                    a,b=sorted((u,v)); g |= 1<<EI[(a,b)]
                groups.append(g)
        DOM.append(tuple(groups))

def gamma_ge4(mask):
    for groups in DOM:
        if all(mask & g for g in groups):
            return False
    return True

# Exhaust all labeled simple graphs on seven vertices.
faces_by_size=defaultdict(list)
for m in range(1<<21):
    if gamma_ge4(m):
        faces_by_size[m.bit_count()].append(m)
expected={0:1,1:21,2:210,3:1330,4:4515,5:7077,6:3605,7:630}
assert {k:len(v) for k,v in faces_by_size.items()}==expected
assert max(faces_by_size)==7
all_faces=set().union(*(set(v) for k,v in faces_by_size.items() if k>0))

# Successive toggle matching on the nonempty face poset.
unmatched=set(all_faces); pairs=[]
for e in range(21):
    bit=1<<e
    lowers=[m for m in unmatched if not (m&bit) and (m|bit) in unmatched]
    for l in lowers:
        u=l|bit
        if l in unmatched and u in unmatched:
            pairs.append((l,u)); unmatched.remove(l); unmatched.remove(u)
assert len(pairs)==8210
crit=Counter(m.bit_count()-1 for m in unmatched)
assert crit==Counter({4:847,5:120,0:1})

# Verify acyclicity of the entire modified Hasse diagram.
pairset=set(pairs); indeg={f:0 for f in all_faces}; out=defaultdict(list); covers=0
for u in all_faces:
    for e in range(21):
        if (u>>e)&1:
            l=u&~(1<<e)
            if l and l in all_faces:
                covers += 1
                a,b=(l,u) if (l,u) in pairset else (u,l)
                out[a].append(b); indeg[b]+=1
q=deque([x for x,d in indeg.items() if d==0]); seen=0
while q:
    x=q.popleft(); seen+=1
    for y in out[x]:
        indeg[y]-=1
        if indeg[y]==0:q.append(y)
assert covers==83895 and seen==len(all_faces)

low_to_up={l:u for l,u in pairs}
crit4=sorted(m for m in unmatched if m.bit_count()==5)
crit5=sorted(m for m in unmatched if m.bit_count()==6)
idx4={m:i for i,m in enumerate(crit4)}

def inc(u,l):
    d=u^l; e=(d&-d).bit_length()-1
    return -1 if (u & ((1<<e)-1)).bit_count()%2 else 1

memo={}; visiting=set()
def morse_col(u):
    if u in memo:return memo[u]
    assert u not in visiting
    visiting.add(u); v={}
    for e in range(21):
        if not ((u>>e)&1):continue
        l=u&~(1<<e); a=inc(u,l)
        if l in idx4:
            i=idx4[l]; v[i]=v.get(i,0)+a
        elif l in low_to_up and low_to_up[l]!=u:
            u2=low_to_up[l]
            if u2.bit_count()==6:
                b=inc(u2,l); c=-a*b
                for i,x in morse_col(u2).items():
                    z=v.get(i,0)+c*x
                    if z:v[i]=z
                    elif i in v:del v[i]
    visiting.remove(u); memo[u]=v; return v
cols=[morse_col(u) for u in crit5]

# Exact rational rank of the Morse boundary.
basis={}
for c in cols:
    v={i:Fraction(x) for i,x in c.items() if x}
    while v:
        p=min(v)
        if p not in basis:
            a=v[p]; basis[p]={i:x/a for i,x in v.items()}; break
        a=v[p]; b=basis[p]
        for i,x in b.items():
            z=v.get(i,Fraction(0))-a*x
            if z:v[i]=z
            elif i in v:del v[i]
assert len(basis)==36

# A unimodular full-rank minor proves all nonzero Smith factors are units.
PC=[16,17,28,29,31,32,35,40,41,42,51,56,59,60,70,71,73,74,75,76,80,81,88,89,90,91,94,95,102,103,104,105,106,107,108,109]
PR=[2,6,8,11,15,17,26,31,32,44,45,46,53,54,55,67,68,69,74,75,76,77,78,79,88,103,140,148,166,212,227,251,295,296,297,304]
A=[[cols[j].get(i,0) for j in PC] for i in PR]
def bareiss_det(a):
    a=[r[:] for r in a]; n=len(a); sign=1; prev=1
    for k in range(n-1):
        if a[k][k]==0:
            s=next(i for i in range(k+1,n) if a[i][k])
            a[k],a[s]=a[s],a[k]; sign=-sign
        p=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                a[i][j]=(a[i][j]*p-a[i][k]*a[k][j])//prev
        prev=p
        for i in range(k+1,n):a[i][k]=0
    return sign*a[-1][-1]
assert bareiss_det(A)==-1

# Independent mod-2 simplicial boundary ranks.
def rank2(bitcols):
    b={}
    for x in bitcols:
        while x:
            p=x.bit_length()-1
            if p in b:x^=b[p]
            else:b[p]=x;break
    return len(b)
ranks={}
for qsize in range(2,8):
    rows=faces_by_size[qsize-1]; ri={m:i for i,m in enumerate(rows)}; bcols=[]
    for u in faces_by_size[qsize]:
        x=0
        for e in range(21):
            if (u>>e)&1:x ^= 1<<ri[u&~(1<<e)]
        bcols.append(x)
    ranks[qsize-1]=rank2(bcols)
assert ranks=={1:20,2:190,3:1140,4:3375,5:2891,6:630}
assert 7077-3375-2891==811
assert 3605-2891-630==84
assert 21-210+1330-4515+7077-3605+630==728
print('VERIFY_OK')
print('faces_nonempty=17388 covers=83895 matching_pairs=8210 critical=(1,847,120)')
print('morse_boundary_rank=36 unimodular_minor=-1 betti4=811 betti5=84 euler=728')
