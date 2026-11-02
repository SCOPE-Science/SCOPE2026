"""DFS-based verification of an explicit infinite-family Hamiltonian-cycle classification.

No perfect-matching enumeration is used. For moderate n, a depth-first
search finds all spanning cycles and checks that the explicit templates
are exactly the full solution set. Legal two-edge switches are verified
by symmetric differences of edge sets.
"""
from collections import Counter


def edges(n,twist):
    es=set()
    def add(a,b):es.add(tuple(sorted((a,b))))
    for i in range(n):add(i,n+i)
    for k in (0,1):
        for i in range(n-1):add(k*n+i,k*n+i+1)
        if not twist:add(k*n+n-1,k*n)
    if twist:
        add(n-1,n);add(2*n-1,0)
    return frozenset(es)


def make_templates(n,twist):
    E=edges(n,twist)
    horz={e for e in E if abs(e[0]-e[1])!=n}
    # The seam of a twisted ribbon also consists of horizontal edges.
    rungs={tuple(sorted((i,n+i))) for i in range(n)}
    horz=E-rungs
    templates=set()
    for i in range(n):
        j=(i+1)%n
        if j!=0:
            crossing={tuple(sorted((i,j))),tuple(sorted((n+i,n+j)))}
        elif not twist:
            crossing={tuple(sorted((n-1,0))),tuple(sorted((2*n-1,n)))}
        else:
            crossing={tuple(sorted((n-1,n))),tuple(sorted((2*n-1,0)))}
        # Removing one pair of horizontal edges and adding its two rungs.
        templates.add(frozenset((horz-crossing)|{tuple(sorted((i,n+i))),tuple(sorted((j,n+j)))}))
    if twist:
        templates.add(frozenset(horz))
    if twist and n%2:
        rim=list(range(2*n))
        for parity in (0,1):
            chosen={tuple(sorted((rim[k],rim[(k+1)%(2*n)])))
                    for k in range(2*n) if k%2==parity}
            templates.add(frozenset(rungs|chosen))
    elif not twist and n%2==0:
        for parity in (0,1):
            chosen=set()
            for i in range(n):
                if i%2==parity:chosen.add(tuple(sorted((i,(i+1)%n))))
                if i%2!=parity:chosen.add(tuple(sorted((n+i,n+(i+1)%n))))
            templates.add(frozenset(rungs|chosen))
    return templates


def dfs_hamiltonian(n,twist):
    E=edges(n,twist);neigh=[set() for _ in range(2*n)]
    for u,v in E:neigh[u].add(v);neigh[v].add(u)
    cycles=set()
    def rec(last, visited, path):
        if len(path)==2*n:
            if 0 in neigh[last]:
                pair=path[1:]+[0]
                cycles.add(frozenset(tuple(sorted((a,b))) for a,b in zip(path,pair)))
            return
        for w in sorted(neigh[last]):
            if not visited>>w&1:
                rec(w,visited|(1<<w),path+[w])
    rec(0,1,[0])
    return cycles


def check(n,twist):
    explicit=make_templates(n,twist)
    direct=dfs_hamiltonian(n,twist)
    assert explicit==direct,(n,twist,len(explicit),len(direct),explicit-direct,direct-explicit)
    ed={c:set() for c in explicit}
    for c in explicit:
        for d in explicit:
            if c!=d and len(c^d)==4:ed[c].add(d)
    degree=Counter(map(len,ed.values()))
    if twist:
        expect=Counter({1:n,n:1})
        if n%2:expect[0]=2
    else:expect=Counter({0:len(explicit)})
    assert degree==expect,(n,twist,degree,expect)
    return len(explicit), dict(degree)


if __name__=='__main__':
    for n in range(4,14):
        for twist in (0,1):
            print(n,twist,check(n,twist))
    print('DFS_AND_EXPLICIT_TEMPLATES_PASS')
