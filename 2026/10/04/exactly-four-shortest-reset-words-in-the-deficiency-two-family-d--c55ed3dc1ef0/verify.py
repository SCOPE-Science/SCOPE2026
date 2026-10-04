#!/usr/bin/env python3
from collections import deque, defaultdict

def transitions(n):
    a=[0]*(n+1); b=[0]*(n+1); c=[0]*(n+1)
    for q in range(1,n+1):
        a[q]=1 if q<=3 else q
        b[q]=1 if q<=2 else (2 if q==3 else q)
        if q==1: c[q]=4
        elif q==2: c[q]=1
        elif q==3: c[q]=4
        elif q<n: c[q]=q+1
        else: c[q]=3
    return {'a':a,'b':b,'c':c}

def image_mask(mask, t):
    out=0; q=1
    while mask:
        if mask & 1: out |= 1 << (t[q]-1)
        mask >>= 1; q += 1
    return out

def bfs(n):
    T=transitions(n)
    start=(1<<n)-1
    dist={start:0}; ways={start:1}
    q=deque([start]); target_depth=None
    while q:
        s=q.popleft(); d=dist[s]
        if target_depth is not None and d>=target_depth: continue
        for ch in 'abc':
            u=image_mask(s,T[ch])
            nd=d+1
            if u not in dist:
                dist[u]=nd; ways[u]=ways[s]; q.append(u)
                if u & (u-1)==0: target_depth=nd if target_depth is None else min(target_depth,nd)
            elif dist[u]==nd:
                ways[u]+=ways[s]
    L=min(dist[s] for s in dist if s and s&(s-1)==0)
    targets={s.bit_length(): ways[s] for s in dist if s and s&(s-1)==0 and dist[s]==L}
    return L,sum(targets.values()),targets,len(dist)

def act_word(n,w):
    T=transitions(n); states=set(range(1,n+1))
    for ch in w: states={T[ch][q] for q in states}
    return states

def formula_words(n):
    mid=('b'+'c'*(n-1))*(n-4)
    return [x+'c'+mid+'bc'+y for x in 'ac' for y in 'ac']

rows=[]
for n in range(5,17):
    L,count,targets,seen=bfs(n)
    expected=(n-2)**2+1
    assert L==expected, (n,L,expected)
    assert count==4, (n,count)
    assert targets=={1:2,4:2}, (n,targets)
    rows.append({'n':n,'length':L,'count':count,'targets':targets,'reachable_subsets':seen})
for n in range(5,101):
    ws=formula_words(n)
    assert len(set(ws))==4
    for w in ws:
        assert len(w)==(n-2)**2+1
        target=act_word(n,w)
        assert len(target)==1
        expected={1} if w.endswith('a') else {4}
        assert target==expected,(n,w[-1],target)
print('VERIFY_OK bfs_n=5..16 formula_n=5..100')
print(rows)
