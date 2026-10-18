"""Brute-force all orientations and count acyclic members by indegree parity.
Independent of the proposed path-coherence counting formula."""
from itertools import product
from collections import Counter, defaultdict

def graph(lengths):
    edges=[]; n=2
    for L in lengths:
        path=[0]
        for _ in range(L-1): path.append(n); n+=1
        path.append(1)
        edges += list(zip(path,path[1:]))
    return n,edges

def acyclic(n,edges,mask):
    d=[0]*n; adj=[[] for _ in range(n)]
    for k,(u,v) in enumerate(edges):
        if mask>>k & 1:u,v=v,u
        adj[u].append(v); d[v]+=1
    stack=[i for i in range(n) if d[i]==0]; seen=0
    while stack:
        u=stack.pop();seen+=1
        for v in adj[u]:
            d[v]-=1
            if d[v]==0:stack.append(v)
    return seen==n

def actual(lengths):
    n,edges=graph(lengths)
    classes=defaultdict(int)
    for mask in range(1<<len(edges)):
        sig=0
        for k,(u,v) in enumerate(edges): sig^=1<<(u if mask>>k&1 else v)
        classes.setdefault(sig,0)
        classes[sig]+=acyclic(n,edges,mask)
    return Counter(classes.values())

def predicted(lengths):
    m=len(lengths); w=[(1<<(L-1))-1 for L in lengths]
    hist=Counter()
    for s in product((0,1),repeat=m):
        r=sum(s)
        if r==m: continue
        mult=2
        for j in range(m):
            if not s[j]:mult*=w[j]
        ca=(1<<(m-1)) if r<=1 else (1<<(m-r))
        hist[ca]+=mult
    if m&1:hist[1]+=2
    else:hist[0]+=1;hist[2]+=1
    return hist

def main():
    cases=[]
    for m in (3,4,5):
        for lengths in product((2,3,4),repeat=m):
            if sum(lengths)>13: continue
            if sorted(lengths)!=list(lengths):continue
            cases.append(lengths)
    cases.extend([(2,)*6,(2,)*7,(2,)*8])
    total=0
    for ls in cases:
        got=actual(ls);want=predicted(ls)
        assert got==want,(ls,got,want)
        n,e=graph(ls);total+=(1<<len(e))
        assert sum(got.values())==(1<<(len(e)-len(ls)+1))
    print(f'PASS {len(cases)} graphs, {total} exhaustively enumerated orientations')
    for x in ((2,2,2),(2,2,2,2),(2,2,2,2,2),(2,3,4),(2,2,3,3)):
        print(x,sorted(actual(x).items()))
if __name__=='__main__':main()
