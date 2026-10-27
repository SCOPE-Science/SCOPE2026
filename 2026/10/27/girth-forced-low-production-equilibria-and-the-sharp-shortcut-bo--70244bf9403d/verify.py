"""Exact finite verification of the girth/low-producer equilibrium theorem.

Run: python3 verify.py. Standard library only.
These checks supplement, rather than replace, the proof for arbitrary graphs.
"""
from collections import Counter, deque
from itertools import combinations


def graph(n, edges):
    a = [set() for _ in range(n)]
    for x,y in edges:
        assert x!=y and 0<=x<n and 0<=y<n
        a[x].add(y); a[y].add(x)
    return a


def cycle_graph(g):
    return graph(g, [(i,(i+1)%g) for i in range(g)])


def theta_graph(g):
    paths = []
    nxt=2
    for length in (g-2,g-2,2):
        path=[0]
        for _ in range(length-1):
            path.append(nxt); nxt+=1
        path.append(1)
        paths.append(path)
    return graph(nxt, [(u,v) for p in paths for u,v in zip(p,p[1:])])


def petersen():
    return graph(10, [(i,(i+1)%5) for i in range(5)] +
                     [(i,i+5) for i in range(5)] +
                     [(i+5,5+(i+2)%5) for i in range(5)])


def heawood():
    lines=[(0,1,2),(0,3,4),(0,5,6),(1,3,5),
           (1,4,6),(2,3,6),(2,4,5)]
    return graph(14,[(p,j+7) for j,line in enumerate(lines) for p in line])


def girth(a):
    g=float('inf')
    for root in range(len(a)):
        depth={root:0}; parent={root:None}; q=deque([root])
        while q:
            u=q.popleft()
            for v in a[u]:
                if v not in depth:
                    depth[v]=depth[u]+1; parent[v]=u; q.append(v)
                elif parent[u]!=v:
                    g=min(g,depth[u]+depth[v]+1)
    return g


def cycle_counts(a):
    n=len(a); found=Counter()
    # Each unoriented cycle is seen twice, once per traversal orientation;
    # the unique smallest vertex on it is forced to be the start.
    for root in range(n):
        def dfs(v, seen):
            for w in a[v]:
                if w==root and len(seen)>=3:
                    found[len(seen)]+=1
                elif w>root and w not in seen:
                    dfs(w,seen|{w})
        dfs(root,{root})
    assert all(k%2==0 for k in found.values())
    return Counter({k:v//2 for k,v in found.items()})


def equilibrium_counts(a):
    n=len(a); out=Counter()
    for k in range(n+1):
        for tup in combinations(range(n),k):
            S=set(tup)
            if all((v in S)==(len(S.intersection(a[v]))==2) for v in range(n)):
                out[k]+=1
    return out


def test(a, name):
    g=girth(a)
    assert g>=5
    c=cycle_counts(a); e=equilibrium_counts(a)
    assert e[0]==1
    assert all(e[k]==c[k] for k in range(1,2*g-4)), (name,c,e)
    assert min(k for k in e if k)>0 and min(k for k in e if k>0)==g
    assert e[g]==c[g]
    print(f'{name}: n={len(a)}, girth={g}, min_support={g}, multiplicity={e[g]}, PASS')
    return e,c


def main():
    num=0
    for g in range(5,14):
        test(cycle_graph(g),f'C{g}'); num+=1
    for a,name in [(petersen(),'Petersen'),(heawood(),'Heawood')]:
        test(a,name);num+=1
    for g in range(5,10):
        e,c=test(theta_graph(g),f'theta(g={g})');num+=1
        k=2*g-4
        assert c[k]==1 and e[k]==0
        print(f'  sharp boundary: cycles[{k}]=1, equilibria[{k}]=0')
    print(f'PASS: {num} distinct graphs and sharpness for g=5 through 9')

if __name__=='__main__':main()
