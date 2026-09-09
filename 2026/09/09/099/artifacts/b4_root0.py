"""Lane 470 gate test: is tree-ball B4(e) 3-colorable with root fixed 0?
If YES => depth-4 spoiler cannot force a win (II mirrors the fixed coloring)
=> preset fallback claim is FALSE. Exact DSATUR."""
from collections import deque
import sys
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
def graph_on(V):
    idx={v:i for i,v in enumerate(V)}; n=len(V)
    adj=[set() for _ in range(n)]
    for v in V:
        for g in SGENS:
            u=red(v+g)
            if u in idx:
                i,j=idx[v],idx[u]
                if i!=j:
                    adj[i].add(j); adj[j].add(i)
    return adj
T4=tree_ball(4); V=sorted(T4); A=graph_on(V)
n=len(V); m=sum(map(len,A))//2
print(f"B4 tree-ball: n={n}, internal S-edges={m}", flush=True)
def dsatur(adj,k,fixed=None,timeout=5000000):
    n=len(adj); col=[-1]*n; cnt=[0]
    if fixed:
        for v,c in fixed.items(): col[v]=c
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
        r=dfs(sum(1 for c in col if c!=-1)); return r,col,cnt[0]
    except TimeoutError:
        return None,col,cnt[0]
root=V.index('')
ok,col,nn=dsatur(A,3,fixed={root:0})
print("3-colorable with root=0:",ok,"nodes:",nn, flush=True)
if ok:
    # verify + class sizes
    bad=sum(1 for i in range(n) for j in A[i] if j>i and col[i]==col[j])
    print("conflicts:",bad)
    from collections import Counter
    print("class sizes:",sorted(Counter(col).items()))
    # save coloring
    import json
    json.dump({"root":V[root],"coloring":{V[i]:col[i] for i in range(n)}},
              open("output/artifacts/B4_coloring.json","w"))
    print("saved output/artifacts/B4_coloring.json")
