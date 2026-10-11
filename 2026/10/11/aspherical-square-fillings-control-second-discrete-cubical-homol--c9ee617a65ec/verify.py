#!/usr/bin/env python3
"""Finite consistency checks for discrete cubical H2 and square fillings."""
from itertools import combinations, product


def graph(m,n):
    vs=list(product(range(m),range(n)))
    def adj(a,b):
        return (a[0]==b[0] and (a[1]-b[1])%n in (1,n-1)) or (a[1]==b[1] and (a[0]-b[0])%m in (1,m-1))
    neigh={v:[w for w in vs if adj(v,w)] for v in vs}
    return vs,adj,neigh

def square_cycle_sets(m,n,vs,adj):
    squares=set()
    for four in combinations(vs,4):
        e=sum(adj(a,b) for a,b in combinations(four,2))
        if e==4 and all(sum(adj(v,w) for w in four)!=3 for v in four):
            if all(sum(adj(v,w) for w in four)==2 for v in four):squares.add(frozenset(four))
    expected={frozenset(((x,y),((x+1)%m,y),(x,(y+1)%n),((x+1)%m,(y+1)%n))) for x in range(m) for y in range(n)}
    assert squares==expected,(m,n,len(squares),len(expected))
    return expected

def test_cubes(m,n,adj,neigh):
    bot={(0,0):(0,0),(1,0):(1,0),(0,1):(0,1),(1,1):(1,1)}
    q=frozenset(bot.values());total=0;bad=0
    for tup in product(*( [bot[(x,y)]]+neigh[bot[(x,y)]] for y in (0,1) for x in (0,1))):
        top={(x,y):tup[2*y+x] for x,y in product((0,1),repeat=2)}
        if any(not (top[p]==top[r] or adj(top[p],top[r])) for p,r in [((0,0),(1,0)),((0,0),(0,1)),((1,0),(1,1)),((0,1),(1,1))]):continue
        full={(x,y,z): bot[(x,y)] if z==0 else top[(x,y)] for x,y,z in product((0,1),repeat=3)}
        occurrences=sum(1 for axis in range(3) for v in (0,1) if frozenset(full[p] for p in full if p[axis]==v)==q)
        total+=1
        if occurrences<2:bad+=1
    return total,bad

def boundary_check(m,n):
    # Every elementary face has oriented boundary in the graph; connected
    # toroidal dual graph means all 2-cycle coefficients are equal.
    verts=[(x,y) for x in range(m) for y in range(n)]
    sq={(x,y):[(x,y),((x+1)%m,y),((x+1)%m,(y+1)%n),(x,(y+1)%n)] for x,y in verts}
    boundary={}
    for s,cyc in sq.items():
        for a,b in zip(cyc,cyc[1:]+cyc[:1]):
            e=tuple(sorted((a,b)));sg=1 if (a,b)==e else -1
            boundary.setdefault(e,[]).append((s,sg))
    assert len(boundary)==2*m*n
    assert all(len(v)==2 and v[0][1]==-v[1][1] for v in boundary.values())
    # Face incidence graph connected -> kernel of boundary is exactly Z.
    adj={s:set() for s in sq}
    for pairs in boundary.values():
        s,t=pairs[0][0],pairs[1][0]
        adj[s].add(t);adj[t].add(s)
    seen={(0,0)}; todo=[(0,0)]
    while todo:
        cur=todo.pop()
        for nxt in adj[cur]-seen:seen.add(nxt);todo.append(nxt)
    assert len(seen)==m*n

if __name__=='__main__':
    tested=0;cubes=0;counter=0
    for m,n in ((5,5),(5,6),(5,7),(6,6),(6,7)):
        v,a,ne=graph(m,n)
        square_cycle_sets(m,n,v,a)
        total,bad=test_cubes(m,n,a,ne)
        assert bad==0,(m,n,bad)
        boundary_check(m,n)
        cubes+=total;tested+=1
    for m,n in ((4,5),(4,6)):
        v,a,ne=graph(m,n)
        total,bad=test_cubes(m,n,a,ne)
        assert bad>0
        counter+=bad
    print('VERIFY_OK:',tested,'toroidal square complexes,',cubes,'singular 3-cubes with fixed face,',counter,'short-cycle counterexamples')
