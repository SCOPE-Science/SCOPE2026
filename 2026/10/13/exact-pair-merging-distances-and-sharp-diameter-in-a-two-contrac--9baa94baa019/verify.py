"""Reproduce exact pair-merging distances for a cycle with two contraction sites.

Uses an independent reverse breadth-first search as a finite test;
finite enumeration is not the proof of the all-order formula.
"""
from collections import deque


def residue(z,n):
    return z%n


def u(n,j):
    if j==1:return 2
    return n*((j+1)//2 + (int(n%2==0 and j==n-2)))


def v(n,j):
    if j==1:return n-2
    return n*((j+2)//2 + (int(n%2==0 and j==n-1)))-2


def oriented(n,x,d):
    if d==0:return 0
    R0=(-x)%n; R2=(2-x)%n
    if d==1:return 1+min(R0,R2)
    if d==2:return n-1+R2
    if d==n-2:return 1+R0+u(n,d-1)
    return 1+min(R0+u(n,d-1),R2+v(n,d-1))


def target(n,x,y):
    d=(y-x)%n
    return min(oriented(n,x,d),oriented(n,y,n-d))


def reverse_bfs(n):
    pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
    parents={p:[] for p in pairs}
    seeds=set()
    def aa(z):return (z+1)%n
    def bb(z):return 1 if z==0 else 3 if z==2 else z
    for p in pairs:
        for transition in (aa,bb):
            i,j=map(transition,p)
            if i==j:seeds.add(p)
            else:parents[tuple(sorted((i,j)))].append(p)
    distances={p:1 for p in seeds}
    todo=deque(seeds)
    while todo:
        current=todo.popleft()
        for predecessor in parents[current]:
            if predecessor not in distances:
                distances[predecessor]=distances[current]+1
                todo.append(predecessor)
    assert len(distances)==len(pairs)
    return distances


def predicted_diameter(n):
    k=n//2
    if n%2==0:return k*k+k-2
    return k*(k+1)+(k+1)//2


def predicted_band(n,d):
    k=n//2
    if d<k:
        if d==1:return n-2
        if d%2==0:return n*(d//2+1)-2
        return n*((d+1)//2)
    if n%2==0:
        return k*k+k-2 if k%2==0 else k*k
    return k*(k+1)+k//2 if k%2==0 else (k+1)*n//2


def run():
    pairs_total=0
    for n in range(5,121):
        dist=reverse_bfs(n)
        assert max(dist.values())==predicted_diameter(n),n
        pairs_total+=len(dist)
        for (i,j),shortest in dist.items():
            claimed=target(n,i,j)
            assert shortest==claimed,(n,i,j,shortest,claimed)
        for d in range(1,n//2+1):
            values=[target(n,x,(x+d)%n) for x in range(n)]
            critical=[1,3,1-d,3-d]
            assert max(values)==max(values[x%n] for x in critical),(n,d)
            assert max(values)==predicted_band(n,d),(n,d,max(values),predicted_band(n,d))
        for x in range(n):
            for d in range(1,n-1):
                assert oriented(n,x,d)<=oriented(n,x,d+1),(n,x,d)
        for j in range(1,n):
            assert u(n,j)==oriented(n,1,j),(n,j,'u')
            assert v(n,j)==oriented(n,3,j),(n,j,'v')
    print('VERIFY_OK n=5..120 pair_distances='+str(pairs_total)+' all_oriented_masks=checked monotonicity=checked four_phase_maxima=checked diameter=checked')

if __name__=='__main__':
    run()
