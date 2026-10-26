#!/usr/bin/env python3
"""Exact standalone checks for cyclic-prism neighborhood-odd colorings."""
from collections import Counter, defaultdict
from math import factorial

def admissible(triple):
    return len(set(triple)) in (1,3)

def transitions(q):
    columns=[(a,b) for a in range(q) for b in range(q) if a!=b]
    states=[(x,y) for x in columns for y in columns
            if x[0]!=y[0] and x[1]!=y[1]]
    neighbors={s:[] for s in states}
    for x,y in states:
        for z in columns:
            if z[0]==y[0] or z[1]==y[1]:continue
            if admissible((x[0],z[0],y[1])) and admissible((x[1],z[1],y[0])):
                neighbors[(x,y)].append((y,z))
    return states,neighbors

def direct_check(cols):
    n=len(cols)
    if any(cols[i][0]==cols[i][1] for i in range(n)):return False
    for i in range(n):
        a,b=cols[i]; p=cols[(i-1)%n]; t=cols[(i+1)%n]
        if a==t[0] or b==t[1]:return False
        if not admissible((p[0],b,t[0])):return False
        if not admissible((p[1],a,t[1])):return False
    return True

def exact_trace(q,n):
    states,neighbors=transitions(q)
    total=0
    for root in states:
        dp={root:1}
        for _ in range(n):
            ndp=defaultdict(int)
            for s,count in dp.items():
                for t in neighbors[s]:ndp[t]+=count
            dp=ndp
        total+=dp.get(root,0)
    return total

def certificate_four():
    states,adj=transitions(4)
    assert len(states)==84 and sum(len(x) for x in adj.values())==84
    assert all(len(adj[s])==1 for s in states)
    hist=Counter(); unseen=set(states)
    while unseen:
        start=next(iter(unseen)); cur=start; orbit=[]
        while cur not in orbit:
            orbit.append(cur);cur=adj[cur][0]
        assert cur==start
        for state in orbit:
            assert state in unseen
            unseen.remove(state)
        hist[len(orbit)]+=1
    assert hist=={2:6,4:6,6:8},hist
    reps={
       'two': [((0,1),(1,0)),((1,0),(0,1))],
       'three_A': [((0,1),(2,0)),((2,0),(0,3)),((0,3),(1,0)),((1,0),(0,2)),((0,2),(3,0)),((3,0),(0,1))],
       'three_B': [((0,1),(1,2)),((1,2),(3,1)),((3,1),(1,0)),((1,0),(2,1)),((2,1),(1,3)),((1,3),(0,1))],
       'four': [((0,1),(2,3)),((2,3),(1,0)),((1,0),(3,2)),((3,2),(0,1))]
    }
    for name,seq in reps.items():
        for i,s in enumerate(seq): assert adj[s]==[seq[(i+1)%len(seq)]],(name,i,s)
    print('4-color transition permutation: 84 states, cycle profile 6x2 + 6x4 + 8x6: OK')

def certificate_five():
    loops={
        4:[(0,1),(2,3),(1,0),(4,2)],
        5:[(0,1),(2,3),(4,0),(1,2),(3,4)],
        7:[(0,1),(2,3),(4,0),(3,1),(2,4),(1,0),(3,2)],
    }
    _,adj=transitions(5)
    for length,cols in loops.items():
        assert direct_check(cols) and len(cols)==length
        states=[(cols[i],cols[(i+1)%length]) for i in range(length)]
        assert states[0]==((0,1),(2,3))
        for i,s in enumerate(states):
            assert states[(i+1)%length] in adj[s]
    # Join the 4-walk to each odd base walk at the common two-column state.
    root=((0,1),(2,3))
    def append_loop(seq,part):
        # Given cyclic column lists sharing a first two-column state, splice
        # at the state by adding all columns from second loop at that state.
        return seq+part
    # Verify arbitrary long odd examples by constructing the closed walk on states.
    for n in range(5,100,2):
        base=loops[5] if n%4==1 else loops[7]
        pieces=[base]+[loops[4]]*((n-len(base))//4)
        # State sequence from each loop, rotate start at the fixed shared state.
        walks=[]
        for p in pieces:
            states=[(p[i],p[(i+1)%len(p)]) for i in range(len(p))]
            assert states[0]==root
            walks+=states
        assert len(walks)==n
        for i in range(n):assert walks[(i+1)%n] in adj[walks[i]]
        cols=[s[0] for s in walks]
        assert direct_check(cols)
    print('5-color closed walks of lengths 4,5,7 and odd constructions through 99: OK')

def brute_count(q,n):
    # Independent vertex-level restricted-growth exhaustive search, not using transfer states.
    N=2*n
    graph=[set() for _ in range(N)]
    for i in range(n):
        for r in (0,1):
            v=r*n+i
            graph[v].add(r*n+(i-1)%n)
            graph[v].add(r*n+(i+1)%n)
            graph[v].add((1-r)*n+i)
    colors=[-1]*N
    total=0
    def dfs(pos,used):
        nonlocal total
        if pos==N:
            assert all(admissible(tuple(colors[w] for w in graph[v])) for v in range(N))
            total+=factorial(q)//factorial(q-used)
            return
        for c in range(min(q-1,used)+1):
            if any(colors[w]==c for w in graph[pos]):continue
            colors[pos]=c
            ok=True
            for v in (pos,)+tuple(graph[pos]):
                vals=[colors[w] for w in graph[v] if colors[w]!=-1]
                if len(vals)==3 and not admissible(vals):ok=False;break
                if len(vals)==2 and vals[0]==vals[1]:
                    # A neighbor must remain available to make three equal.
                    missing=[w for w in graph[v] if colors[w]<0]
                    if len(missing)!=1:ok=False;break
                    w=missing[0]
                    if any(colors[t]==vals[0] for t in graph[w]):ok=False;break
            if ok:dfs(pos+1,max(used,c+1))
            colors[pos]=-1
    dfs(0,0)
    return total

def main():
    certificate_four();certificate_five()
    expected4={4:36,6:60,8:36,10:12,12:84}
    for n,v in expected4.items():assert exact_trace(4,n)==v
    known5={3:0,5:240,7:1680,9:18000,11:171600}
    for n,v in known5.items():assert exact_trace(5,n)==v
    for q,n in [(4,3),(4,4),(5,3),(5,5),(5,7)]:
        d=brute_count(q,n);t=exact_trace(q,n)
        assert d==t,(q,n,d,t)
        print('Independent vertex DFS vs transfer:',q,n,t,'OK')
    print('All checks PASS')
if __name__=='__main__':main()
