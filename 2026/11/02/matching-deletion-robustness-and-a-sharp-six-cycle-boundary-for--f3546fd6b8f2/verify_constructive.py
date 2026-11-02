"""Constructive independent checker for the six-cube/square-ear model.
Does not enumerate all ternary assignments and uses a separate adjacency method.
Run: python verify_constructive.py
"""
from itertools import product
from collections import deque

def structures(m,n,t):
    assert 3 <= m <= n and t <= m and (m,n,t)!=(3,3,3)
    S=set();cubes=[]
    for side in (0,1):
        for mono in range(3):
            other=tuple(a for a in range(3) if a!=mono)
            block=set()
            for q in product(other,repeat=n if side==0 else m):
                x=(mono,)*m+q if side==0 else q+(mono,)*n
                block.add(x);S.add(x)
            cubes.append(block)
    ears=set()
    for k in range(t):
        for b in range(3):
            for c in range(3):
                if b==c:continue
                a=3-b-c
                L=[b]*m;R=[c]*n;L[k]=a;R[k]=a
                x=tuple(L+R)
                ears.add(x)
    assert S.isdisjoint(ears)
    allstates=S|ears
    # The six monochromatic corners are intersections of the six cubes.
    corners={x for x in S if sum(x in block for block in cubes)==2}
    assert len(corners)==6
    assert all(sum(x in block for block in cubes)==1 for x in S-corners)
    assert len(ears)==6*t
    # Build the adjacency independently by testing all one-site alternatives.
    neighbors={x:set() for x in allstates}
    for x in allstates:
        for v in range(m+n):
            for a in range(3):
                if a!=x[v]:
                    y=x[:v]+(a,)+x[v+1:]
                    if y in allstates:neighbors[x].add(y)
    assert all(x in neighbors[y] for x,ys in neighbors.items() for y in ys)
    assert all(sum(y in S for y in neighbors[x])==2 and len(neighbors[x])==2 for x in ears)
    # Every new state is joined to one vertex one step into either of two cubes
    # meeting at the unique corner given by its majority-side color values.
    for x in ears:
        b=max(set(x[:m]), key=x[:m].count)
        c=max(set(x[m:]), key=x[m:].count)
        corner=(b,)*m+(c,)*n
        u,v=neighbors[x]
        assert corner in neighbors[u] and corner in neighbors[v]
        assert len(neighbors[u]&neighbors[v])>=2
    # Each hypercube is induced and has dimension its variable part size.
    for B in cubes:
        L=len(B).bit_length()-1
        assert len(B)==2**L
        for x in B:
            assert len(neighbors[x]&B)==L
    ed=sum(map(len,neighbors.values()))//2
    expect=3*(m*2**(m-1)+n*2**(n-1))+12*t
    assert ed==expect
    # The six cubes intersect in one corner per cycle edge.
    inter=[[len(cubes[i]&cubes[j]) for j in range(6)] for i in range(6)]
    assert sorted(sum(inter[i][j]>0 for j in range(6) if j!=i) for i in range(6))==[2]*6
    assert all(inter[i][j] in (0,1) for i in range(6) for j in range(6) if i!=j)
    # Compute distances in this constructive graph independently of direct exhaustive program.
    N=len(allstates);D=(3*(m+n))//2
    for root in allstates:
        dist={root:0};q=deque([root])
        while q:
            x=q.popleft()
            for y in neighbors[x]:
                if y not in dist:dist[y]=dist[x]+1;q.append(y)
        assert len(dist)==N and max(dist.values())==D,(m,n,t,root)
    print(f'CONSTRUCTIVE_PASS m={m} n={n} t={t} V={N} E={ed} diam={D}')

if __name__=='__main__':
    for m,n in [(3,3),(3,4),(3,5),(4,4),(4,7),(5,6),(6,6),(5,8)]:
        for t in sorted(set([0,1,2,m])):
            if (m,n,t)==(3,3,3):continue
            structures(m,n,t)
    print('CONSTRUCTIVE_ALL_PASS')
