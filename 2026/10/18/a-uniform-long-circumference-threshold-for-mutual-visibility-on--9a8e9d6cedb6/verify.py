"""Reproducible finite checks for the three-window cylinder construction.
This is a test of instances, not an infinite proof; the latter is mathematical.
Run: python3 verify.py
"""
from collections import deque
from itertools import combinations


def chosen(s,t):
    h=t//3
    return {(a,k*h+a) for a in range(s) for k in range(3)}


def distance(u,v,t):
    x=abs(u[1]-v[1]);return abs(u[0]-v[0])+min(x,t-x)


def neighbors(p,s,t):
    a,c=p
    if a>0:yield(a-1,c)
    if a+1<s:yield(a+1,c)
    yield(a,(c-1)%t);yield(a,(c+1)%t)


def check_by_deletion_bfs(s,t):
    sel=chosen(s,t)
    assert len(sel)==3*s
    for u,v in combinations(sorted(sel),2):
        forbidden=sel-{u,v}
        q=deque([(u,0)]); visited={u}; answer=None
        while q:
            w,d=q.popleft()
            if w==v:
                answer=d;break
            for z in neighbors(w,s,t):
                if z not in forbidden and z not in visited:
                    visited.add(z);q.append((z,d+1))
        if answer != distance(u,v,t):
            raise AssertionError((s,t,u,v,answer,distance(u,v,t)))
    return len(sel)*(len(sel)-1)//2


def explicit_path(u,v,s,t):
    """Three-stage path from proof: horizontal, vertical in a gap, horizontal."""
    h=t//3; r=t-3*h
    a,c=u;b,d=v
    k=c//h # for block 2 correct even t not multiple 3
    l=d//h
    if k==l:
        # vertical first at c; then horizontal direct to d
        step=1 if b>a else -1
        path=[u]
        for z in range(a+step,b+step,step):path.append((z,c))
        stepc=1 if d>c else -1
        for col in range(c+stepc,d+stepc,stepc):path.append((b,col))
        return path
    # orient pair from block k to next block l in cyclic order
    if (l-k)%3!=1:
        return list(reversed(explicit_path(v,u,s,t)))
    # next free column after block k in forward orientation
    gapcol=(k*h+s)%t
    # block 2 next gap begins at 2h+s, wraps to block 0
    assert gapcol not in {col for _,col in chosen(s,t)}
    path=[u]
    col=c
    while col != gapcol:
        col=(col+1)%t;path.append((a,col))
        assert len(path)<=t+1
    step=1 if b>a else -1
    for row in range(a+step,b+step,step):path.append((row,col))
    while col != d:
        col=(col+1)%t;path.append((b,col))
        assert len(path)<=t+s+2
    return path


def check_explicit(s,t):
    M=chosen(s,t)
    for u,v in combinations(sorted(M),2):
        path=explicit_path(u,v,s,t)
        if not (path[0]==u and path[-1]==v and len(path)==len(set(path)) and
           len(path)-1==distance(u,v,t) and
           all((x in M) == (x==u or x==v) for x in path) and
           all(v in set(neighbors(u,s,t)) for u,v in zip(path,path[1:]))):
            raise AssertionError((s,t,u,v,path,distance(u,v,t)))

if __name__=='__main__':
    tests=[(s,t) for s in range(3,11) for t in range(6*s,6*s+10)]
    tests += [(s,6*s+r) for s in (12,16,20) for r in (0,1,2)]
    paircount=0
    for s,t in tests:
        check_explicit(s,t)
        paircount+=check_by_deletion_bfs(s,t)
    print(f'PASS: {len(tests)} pairs (s,t), {paircount} endpoint pairs, explicit routes and independent shortest-path BFS.')
