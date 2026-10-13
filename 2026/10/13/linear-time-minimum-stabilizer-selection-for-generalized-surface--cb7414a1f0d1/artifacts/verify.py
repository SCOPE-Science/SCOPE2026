#!/usr/bin/env python3
import random

def gf2_rank(rows, ncols):
    a=[]
    for row in rows:
        x=0
        for j,b in enumerate(row):
            if b&1: x |= 1<<j
        a.append(x)
    rank=0
    for col in range(ncols):
        pivot=next((i for i in range(rank,len(a)) if (a[i]>>col)&1),None)
        if pivot is None: continue
        a[rank],a[pivot]=a[pivot],a[rank]
        for i in range(len(a)):
            if i!=rank and ((a[i]>>col)&1): a[i]^=a[rank]
        rank+=1
    return rank

def comps(n, edges):
    adj=[[] for _ in range(n)]
    active=set()
    for u,v in edges:
        adj[u].append(v); adj[v].append(u); active|={u,v}
    seen=set(); out=[]
    for s in active:
        if s in seen: continue
        stack=[s]; seen.add(s); c=[]
        while stack:
            u=stack.pop(); c.append(u)
            for v in adj[u]:
                if v not in seen: seen.add(v); stack.append(v)
        out.append(c)
    return out

def primal_check(rng):
    n=rng.randint(2,12)
    all_edges=[(u,v) for u in range(n) for v in range(u+1,n)]
    rng.shuffle(all_edges); edges=all_edges[:rng.randint(1,min(len(all_edges),18))]
    W={v for v in range(n) if rng.random()<0.72}
    active={x for e in edges for x in e}
    wr=sorted(W&active); idx={v:i for i,v in enumerate(wr)}
    rows=[[0]*len(edges) for _ in wr]
    for j,(u,v) in enumerate(edges):
        if u in idx: rows[idx[u]][j]=1
        if v in idx: rows[idx[v]][j]=1
    closed=sum(1 for c in comps(n,edges) if all(v in W for v in c))
    formula=len(wr)-closed
    assert gf2_rank(rows,len(edges))==formula
    omit=set()
    for c in comps(n,edges):
        if all(v in W for v in c): omit.add(c[0])
    sel=[row for v,row in zip(wr,rows) if v not in omit]
    assert gf2_rank(sel,len(edges))==formula==len(sel)

def dual_check(rng):
    nf=rng.randint(1,10)
    pairs=[]
    for _ in range(rng.randint(1,18)):
        if nf>=2 and rng.random()<0.75:
            u,v=rng.sample(range(nf),2); pairs.append((u,v,False))
        else:
            u=rng.randrange(nf); pairs.append((u,None,True))
    active={u for u,v,b in pairs}
    active|={v for u,v,b in pairs if v is not None}
    fr=sorted(active); idx={f:i for i,f in enumerate(fr)}
    rows=[[0]*len(pairs) for _ in fr]
    internal=[]; marked=set()
    for j,(u,v,boundary) in enumerate(pairs):
        rows[idx[u]][j]=1
        if v is not None:
            rows[idx[v]][j]=1; internal.append((u,v))
        else: marked.add(u)
    # Components of the internal adjacency, including isolated active faces.
    adj={f:[] for f in active}
    for u,v in internal: adj[u].append(v); adj[v].append(u)
    seen=set(); cs=[]
    for s in active:
        if s in seen: continue
        st=[s];seen.add(s);c=[]
        while st:
            u=st.pop();c.append(u)
            for v in adj[u]:
                if v not in seen:seen.add(v);st.append(v)
        cs.append(c)
    unmarked=sum(1 for c in cs if not any(v in marked for v in c))
    formula=len(fr)-unmarked
    assert gf2_rank(rows,len(pairs))==formula
    omit=set()
    for c in cs:
        if not any(v in marked for v in c): omit.add(c[0])
    sel=[row for f,row in zip(fr,rows) if f not in omit]
    assert gf2_rank(sel,len(pairs))==formula==len(sel)

def main():
    rng=random.Random(240517)
    for _ in range(4000): primal_check(rng)
    for _ in range(4000): dual_check(rng)
    print('VERIFY_OK')
if __name__=='__main__': main()
