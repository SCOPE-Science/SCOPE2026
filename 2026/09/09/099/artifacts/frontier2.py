"""Lane 470: extend exact 3-color frontier (S-ball r4 n=833; tree-ball B6 n=1457), save colorings."""
from collections import deque
import sys, json
sys.setrecursionlimit(100000)
INV = {'a':'A','A':'a','b':'B','B':'b'}
def red(w):
    out=[]
    for ch in w:
        if out and out[-1]==INV[ch]: out.pop()
        else: out.append(ch)
    return ''.join(out)
def invw(w): return ''.join(INV[c] for c in reversed(w))
W = red('abAB'); Wi = invw(W)
SGENS = ['a','A','b','B',W,Wi]
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
def s_ball(r):
    seen={'':0}; q=deque([''])
    while q:
        u=q.popleft()
        if seen[u]>=r: continue
        for g in SGENS:
            v=red(u+g)
            if v not in seen:
                seen[v]=seen[u]+1; q.append(v)
    return seen
def graph_on(V):
    idx={v:i for i,v in enumerate(V)}
    adj=[set() for _ in range(len(V))]
    for v in V:
        for g in SGENS:
            u=red(v+g)
            if u in idx:
                i,j=idx[v],idx[u]
                if i!=j: adj[i].add(j); adj[j].add(i)
    return adj
def dsatur(adj,k,timeout=8000000):
    n=len(adj); col=[-1]*n; cnt=[0]
    def select():
        best=-1;bk=-1;bd=-1
        for i in range(n):
            if col[i]!=-1: continue
            used={col[j] for j in adj[i] if col[j]!=-1}
            u=len(used); d=len(adj[i])
            if u>bk or (u==bk and d>bd): best=i;bk=u;bd=d
        return best
    def dfs(done):
        cnt[0]+=1
        if cnt[0]>timeout: raise TimeoutError
        if done==n: return True
        v=select()
        used={col[j] for j in adj[v] if col[j]!=-1}
        for c in range(k):
            if c not in used:
                col[v]=c
                if dfs(done+1): return True
                col[v]=-1
        return False
    try:
        return dfs(0),col,cnt[0]
    except TimeoutError:
        return None,col,cnt[0]

which=sys.argv[1] if len(sys.argv)>1 else "s4"
if which=="s4":
    Sb=s_ball(4); V=sorted(Sb); A=graph_on(V)
    print(f"S-ball r4: n={len(V)}, m={sum(map(len,A))//2}", flush=True)
    ok,col,nn=dsatur(A,3)
    print("3-colorable:",ok,"nodes:",nn, flush=True)
    if ok:
        bad=sum(1 for i in range(len(V)) for j in A[i] if j>i and col[i]==col[j])
        print("conflicts:",bad)
        json.dump({"coloring":{V[i]:col[i] for i in range(len(V))}},
                  open("output/artifacts/Sball4_coloring.json","w"))
        print("saved Sball4_coloring.json")
elif which=="b6":
    T=tree_ball(6); V=sorted(T); A=graph_on(V)
    print(f"tree-ball B6: n={len(V)}, m={sum(map(len,A))//2}", flush=True)
    ok,col,nn=dsatur(A,3)
    print("3-colorable:",ok,"nodes:",nn, flush=True)
    if ok:
        bad=sum(1 for i in range(len(V)) for j in A[i] if j>i and col[i]==col[j])
        print("conflicts:",bad)
        json.dump({"root":V[V.index('')],"coloring":{V[i]:col[i] for i in range(len(V))}},
                  open("output/artifacts/B6_coloring.json","w"))
        print("saved B6_coloring.json")
