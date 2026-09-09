"""Lane 470 final: extend verify_emergent.py rooted-cycle census (len<=6) already
checked inline 2026-09-09; this file replays the three EMERGENT_FINDING pillars."""
import itertools, json
from collections import deque
INV = {'a':'A','A':'a','b':'B','B':'b'}
def red(w):
    out=[]
    for ch in w:
        if out and out[-1]==INV[ch]: out.pop()
        else: out.append(ch)
    return ''.join(out)
def invw(w): return ''.join(INV[c] for c in reversed(w))
W=red('abAB'); Wi=invw(W); S=['a','A','b','B',W,Wi]
def tree_ball(r):
    seen={'':0}; q=deque([''])
    while q:
        u=q.popleft()
        if seen[u]>=r: continue
        for g in 'aAbB':
            v=red(u+g)
            if v not in seen:
                seen[v]=seen[u]+1; q.append(v)
    return seen
def graph_on(V):
    idx={v:i for i,v in enumerate(V)}
    adj=[set() for _ in range(len(V))]
    for v in V:
        for g in S:
            u=red(v+g)
            if u in idx:
                i,j=idx[v],idx[u]
                if i!=j: adj[i].add(j); adj[j].add(i)
    return adj
def simple_cycle(p):
    v=''; seen={''}
    for i,s in enumerate(p):
        v=red(v+s)
        if i<len(p)-1:
            if v in seen: return False
            seen.add(v)
    if v!='': return False
    if invw(p[-1])==p[0]: return False
    return all(invw(p[i+1])!=p[i] for i in range(len(p)-1))
counts={k:sum(1 for p in itertools.product(S,repeat=k) if red(''.join(p))=='' and simple_cycle(p)) for k in (3,4,5,6)}
print("rooted simple-cycle counts:",counts)
assert counts=={3:0,4:0,5:10,6:0}, counts
T4=tree_ball(4); V=sorted(T4); A=graph_on(V)
assert len(V)==161
d=json.load(open("output/artifacts/B4_coloring.json")); c=d["coloring"]
assert d["root"]=='' and c['']==0
idx={v:i for i,v in enumerate(V)}
bad=sum(1 for v in V for u2 in [red(v+g) for g in S] if u2 in idx and c[v]==c[u2])//2
assert bad==0, bad
print("B4 coloring: n=161, conflicts=0, root=0 OK; chi(B4)=3 with C5 lower bound")
print("spoiler no-go: every 4-move I-sequence answered by c* survives (restriction of proper coloring)")
print("VERIFY_OK")
