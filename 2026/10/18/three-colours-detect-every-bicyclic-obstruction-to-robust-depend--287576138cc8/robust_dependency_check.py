"""Finite independent checks of the stated edge-label robustness equivalence."""
from itertools import product

def sat(nl,nr,edges,colors,q=3):
    for a in product(range(q), repeat=nl):
        for b in product(range(q), repeat=nr):
            if all(c==a[x] or c==b[y] for (x,y),c in zip(edges,colors)):
                return True
    return False

def pseudo(nl,nr,edges):
    adj=[[] for _ in range(nl+nr)]
    for x,y in edges:
        adj[x].append(nl+y);adj[nl+y].append(x)
    seen=set()
    for x in range(nl+nr):
        if x in seen: continue
        st=[x]; seen.add(x); v=0; deg=0
        while st:
            u=st.pop();v+=1;deg+=len(adj[u])
            for w in adj[u]:
                if w not in seen:seen.add(w);st.append(w)
        if deg//2>v:return False
    return True

def exhaustive(nl,nr):
    full=list(product(range(nl),range(nr)))
    count=0;unsat=0
    for bits in product((0,1),repeat=len(full)):
        edges=[e for e,t in zip(full,bits) if t]
        p=pseudo(nl,nr,edges)
        all_satisfiable=True
        for vals in product(range(3),repeat=len(edges)):
            if not sat(nl,nr,edges,vals,3):
                all_satisfiable=False;unsat+=1
                break
        assert p==all_satisfiable,(nl,nr,edges,p)
        count+=1
    return count,unsat
for sizes in ((1,1),(1,3),(2,2),(2,3)):
    a,b=exhaustive(*sizes)
    print('EXHAUSTIVE',sizes,a,b)
# Two C4 cycles sharing x0; forcing colors 0 at the central vertex
# in one cycle and 1 in the other.
E=[(0,0),(1,0),(1,1),(0,1),(0,2),(2,2),(2,3),(0,3)]
C=[0,1,2,0,1,0,2,1]
assert not sat(3,4,E,C,3)
print('FIGURE_EIGHT_WITNESS_OK',len(E))
print('ROBUST_DEPENDENCY_CHECK_OK')
