#!/usr/bin/env python3
"""Independent direct simplicial chain and C7-coinvariant check for a cyclic tournament."""
from itertools import combinations
from collections import defaultdict, Counter
from fractions import Fraction

def rank_Q(columns):
    pivots={}
    for col in columns:
        v={i:Fraction(x) for i,x in col.items() if x}
        while v:
            i=min(v)
            if i not in pivots:
                factor=v[i]
                pivots[i]={j:x/factor for j,x in v.items()}
                break
            factor=v[i]
            for j,x in pivots[i].items():
                val=v.get(j,Fraction(0))-factor*x
                if val:v[j]=val
                else:v.pop(j,None)
    return len(pivots)

def rank_mod(columns,p):
    pivots={}
    for c in columns:
        v={i:x%p for i,x in c.items() if x%p}
        while v:
            i=min(v)
            if i not in pivots:
                t=pow(v[i],-1,p)
                pivots[i]={j:(x*t)%p for j,x in v.items()}
                break
            q=v[i]
            for j,x in pivots[i].items():
                val=(v.get(j,0)-q*x)%p
                if val:v[j]=val
                else:v.pop(j,None)
    return len(pivots)

def boundaries(s):
    j=0
    while s:
        b=s&-s
        yield b, (-1 if j%2 else 1)
        s-=b;j+=1

n=7; arcs=[(a,b) for a in range(n) for b in range(n) if (b-a)%n in (1,2,3)]
assert len(arcs)==21
C=defaultdict(list)
for size in range(1,7):
    for indices in combinations(range(21),size):
        indeg=[0]*n;outdeg=[0]*n; nxt=[-1]*n
        ok=True
        for i in indices:
            a,b=arcs[i];indeg[b]+=1;outdeg[a]+=1;nxt[a]=b
            if indeg[b]>1 or outdeg[a]>1:ok=False;break
        if not ok:continue
        for a in range(n):
            cur=a; seen=set()
            while cur!=-1 and cur not in seen:
                seen.add(cur);cur=nxt[cur]
            if cur!=-1:ok=False;break
        if ok:C[size-1].append(sum(1<<i for i in indices))
print('independent face vector', [len(C[k]) for k in range(6)])
assert [len(C[k]) for k in range(6)]==[21,168,630,1113,819,175]
for p in (2,3,5,101):
    ranks={}
    for k in range(1,6):
        rid={s:i for i,s in enumerate(C[k-1])}
        cols=[]
        for s in C[k]:
            d={}
            for b,sgn in boundaries(s):d[rid[s^b]]=sgn
            cols.append(d)
        ranks[k]=rank_mod(cols,p)
    bettis=[len(C[k])-ranks.get(k,0)-ranks.get(k+1,0) for k in range(6)]
    print('prime',p,'ranks',ranks,'bettis',bettis)
    assert bettis==[1,0,0,13,43,17]
# rotation orbit quotient: signed coinvariant matrix
arcid={e:i for i,e in enumerate(arcs)}
rot=[arcid[( (a+1)%n, (b+1)%n)] for a,b in arcs]
def rotate(s,steps):
    lis=[i for i in range(21) if (s>>i)&1]
    for _ in range(steps):lis=[rot[i] for i in lis]
    sign=(-1)**sum(lis[i]>lis[j] for i in range(len(lis)) for j in range(i+1,len(lis)))
    return sum(1<<i for i in lis),sign
reprs={};bydim=defaultdict(list)
for k in range(6):
 for s in C[k]:
    if s in reprs:continue
    orbit=[rotate(s,j)[0] for j in range(7)]
    assert len(set(orbit))==7
    rep=min(orbit);bydim[k].append(rep)
    for t in orbit:
        sg=[u for j in range(7) for v,u in [rotate(t,j)] if v==rep]
        assert len(sg)==1
        reprs[t]=(rep,sg[0])
for k in bydim:bydim[k].sort()
assert [len(bydim[k]) for k in range(6)]==[3,24,90,159,117,25]
for p in (101,1000003,"Q"):
 ranks={}
 for k in range(1,6):
    idx={s:i for i,s in enumerate(bydim[k-1])}
    cols=[]
    for s in bydim[k]:
        v=Counter()
        for b,sgn in boundaries(s):
            rep,ori=reprs[s^b];v[idx[rep]]+=sgn*ori
        cols.append({i:x for i,x in v.items() if x})
    ranks[k]=rank_Q(cols) if p=="Q" else rank_mod(cols,p)
 bettis=[len(bydim[k])-ranks.get(k,0)-ranks.get(k+1,0) for k in range(1,6)]
 print('rotation invariants field',p,'ranks',ranks,'betti degree1-5',bettis)
 assert bettis==[0,0,1,7,5]
print('PASS independent direct and rotation quotient')
