#!/usr/bin/env python3
from collections import defaultdict, deque
from itertools import product

def invmod(a,q): return pow(a,q-2,q)
def norm(v,q):
    for a in v:
        if a%q:
            z=invmod(a%q,q)
            return tuple((x*z)%q for x in v)
    raise ValueError

def pg2(q):
    pts=sorted({norm(v,q) for v in product(range(q), repeat=3) if any(v)})
    lns=pts[:]
    V=[('p',p) for p in pts]+[('l',l) for l in lns]
    idx={v:i for i,v in enumerate(V)}
    adj=[set() for _ in V]
    for p in pts:
        for l in lns:
            if sum(a*b for a,b in zip(p,l))%q==0:
                i=idx[('p',p)]; j=idx[('l',l)]
                adj[i].add(j); adj[j].add(i)
    n=len(V)
    dist=[[99]*n for _ in range(n)]
    for s in range(n):
        dist[s][s]=0; dq=deque([s])
        while dq:
            u=dq.popleft()
            for v in adj[u]:
                if dist[s][v]==99:
                    dist[s][v]=dist[s][u]+1; dq.append(v)
    return V,dist

def tuples_len(dist,k,L):
    n=len(dist); out=[]
    def rec(seq,rem):
        if len(seq)==k+1:
            if rem==0: out.append(tuple(seq))
            return
        u=seq[-1]; left=k-(len(seq)-1)
        for v in range(n):
            if v==u: continue
            d=dist[u][v]
            if 1<=d<=rem-(left-1): rec(seq+[v],rem-d)
    for s in range(n): rec([s],L)
    return out

def rank(cols):
    piv={}
    for x in cols:
        while x:
            p=x.bit_length()-1
            if p in piv: x ^= piv[p]
            else: piv[p]=x; break
    return len(piv)

def local_dim(q):
    V,d=pg2(q)
    bases={k:tuples_len(d,k,4) for k in (2,3,4)}
    by={k:defaultdict(list) for k in (2,3,4)}
    for k in (2,3,4):
        for t in bases[k]: by[k][(t[0],t[-1])].append(t)
    vals=[]
    for ep,l3 in by[3].items():
        a,b=ep
        if d[a][b]!=2: continue
        rows2={t:i for i,t in enumerate(by[2][ep])}
        cols3=[]
        for t in l3:
            bits=0
            for i in (1,2):
                if d[t[i-1]][t[i+1]]==d[t[i-1]][t[i]]+d[t[i]][t[i+1]]:
                    bits ^= 1<<rows2[t[:i]+t[i+1:]]
            cols3.append(bits)
        r3=rank(cols3)
        rows3={t:i for i,t in enumerate(l3)}
        cols4=[]
        for t in by[4][ep]:
            bits=0
            for i in (1,2,3):
                if d[t[i-1]][t[i+1]]==2:
                    bits ^= 1<<rows3[t[:i]+t[i+1:]]
            cols4.append(bits)
        r4=rank(cols4)
        vals.append((len(by[2][ep]),len(l3),len(by[4][ep]),r3,r4,len(l3)-r3-r4))
    assert vals
    assert set(vals)=={(q*q+3*q-1,3*q*(q+2),q*q+3*q+1,q*q+3*q-1,q*q+3*q+1,q*q)}
    return len(vals), vals[0][-1]

for q in (2,3,5):
    blocks,h=local_dim(q)
    N=q*q+q+1
    assert blocks==2*N*(N-1)
    assert h==q*q
    print(f"q={q}: distance-2 endpoint blocks={blocks}, local MH_3,4 mod 2 dimension={h}")
print("VERIFY_OK")
