"""Independent finite checks of rooted cup-stacking on matching-deleted bicliques.

Run: python3 verify_cup.py
Only finite checks are performed; the universal theorem requires the written proof.
"""
from collections import deque
from functools import lru_cache


def graph(m, n, t):
    verts = range(m+n)
    neighbors = [set() for _ in verts]
    for a in range(m):
        for b in range(n):
            if a == b and a < t:
                continue
            neighbors[a].add(m+b)
            neighbors[m+b].add(a)
    d = []
    for s in verts:
        ds = [m+n+1]*(m+n)
        ds[s] = 0
        q = deque([s])
        while q:
            x = q.popleft()
            for y in neighbors[x]:
                if ds[y] == m+n+1:
                    ds[y] = ds[x]+1
                    q.append(y)
        d.append(ds)
    return neighbors, d


def prediction(m,n,t,r):
    if r < m:
        return m <= n + (2 if r < t else 1)
    return n <= m + (2 if r-m < t else 1)


def matching(left, right, adjacency):
    """Backtracking augmenting-path matching saturating the requested left vertices."""
    mates={}
    def augment(x, used):
        for y in right:
            if y not in adjacency[x] or y in used:
                continue
            used.add(y)
            if y not in mates or augment(mates[y], used):
                mates[y]=x
                return True
        return False
    for x in left:
        assert augment(x, set()), ('matching failure', x, left, right)
    return {x:y for y,x in mates.items()}


def witness(m,n,t,r):
    if not prediction(m,n,t,r):
        return None
    adj,d = graph(m,n,t)
    state=[1]*(m+n)
    moves=[]
    def push(x,y):
        assert x!=r and state[x]>0 and state[y]>0
        assert state[x]==d[x][y], (m,n,t,r,x,y,state[x],d[x][y])
        state[y]+=state[x]
        state[x]=0
        moves.append((x,y))
    if r<m:
        side = [a for a in range(m) if a!=r]
        opp = list(range(m,m+n))
        exceptional=m+r if r<t else None
    else:
        side = [b for b in range(m,m+n) if b!=r]
        opp = list(range(m))
        exceptional=r-m if r-m<t else None
    if exceptional is not None:
        # Unique nonneighbor of the target collects a 3-packet from two
        # other same-side vertices; their distance to it is one.
        x,y=side[:2]
        push(x,exceptional)
        push(y,exceptional)
        push(exceptional,r)
        side=side[2:]
        opp.remove(exceptional)
    mate=matching(side, opp, adj)
    for x in side:
        y=mate[x]
        push(y,x)
        push(x,r)
    for y in opp:
        if state[y]:
            push(y,r)
    assert state[r]==m+n and all(not state[x] for x in range(m+n) if x!=r)
    assert len(moves)==m+n-1
    return moves


def exact_reachable(m,n,t,r):
    _,d=graph(m,n,t)
    total=m+n
    @lru_cache(None)
    def reachable(st):
        if st[r]==total:
            return True
        for x,c in enumerate(st):
            if x==r or c==0:
                continue
            for y,z in enumerate(st):
                if x!=y and z and d[x][y]==c:
                    nxt=list(st)
                    nxt[y]+=nxt[x]
                    nxt[x]=0
                    if reachable(tuple(nxt)):
                        return True
        return False
    outcome=reachable((1,)*total)
    return outcome, reachable.cache_info().currsize


def main():
    brute_cases=0
    states=0
    for m in range(3,7):
        for n in range(3,7):
            if m+n>9:
                continue
            for t in range(min(m,n)+1):
                for r in range(m+n):
                    expected=prediction(m,n,t,r)
                    actual,n_states=exact_reachable(m,n,t,r)
                    assert actual==expected,(m,n,t,r,actual,expected)
                    brute_cases+=1
                    states+=n_states
    print('exhaustive_cases',brute_cases)
    print('memoized_states_across_cases',states)
    witness_cases=0
    for m in range(3,13):
        for n in range(3,13):
            for t in range(min(m,n)+1):
                for r in range(m+n):
                    if prediction(m,n,t,r):
                        assert witness(m,n,t,r) is not None
                        witness_cases+=1
    print('constructive_witnesses',witness_cases)
    assert prediction(5,3,1,0) and not prediction(5,3,1,1)
    print('sharp_nonhamiltonian_example K_5,3 - M_1: matched large-side target yes, unmatched large-side target no')
    print('PASS')

if __name__=='__main__':
    main()
