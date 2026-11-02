"""Reproduce the shortest circular three-palindrome-cover theorem.

Python standard library only. This tests the formula and a constructive
Euler-tour witness, and independently obtains exact minima for q <= 4.
"""
from collections import deque
from itertools import product


def optimum(q):
    if q < 2:
        raise ValueError('q >= 2 is required')
    base = (3*q*q+q)//2
    return base + (q//2 if q % 2 == 0 else 0)


def construct(q):
    # Undirected looped complete graph; for even q add a perfect matching.
    edges = [(i,i) for i in range(q)]
    edges += [(i,j) for i in range(q) for j in range(i+1,q)]
    if q % 2 == 0:
        edges += [(2*i,2*i+1) for i in range(q//2)]
    incident = [[] for _ in range(q)]
    for eid,(u,v) in enumerate(edges):
        incident[u].append(eid)
        if u != v:
            incident[v].append(eid)
    assert all((len(incident[u])+(1 if (u,u) in edges else 0)) % 2 == 0
               for u in range(q))
    seen = [False]*len(edges)
    stack = [(0, None)]
    traversal = []
    while stack:
        u,_ = stack[-1]
        while incident[u] and seen[incident[u][-1]]:
            incident[u].pop()
        if incident[u]:
            eid=incident[u].pop()
            if seen[eid]:
                continue
            seen[eid]=True
            a,b=edges[eid]
            stack.append((b if u==a else a,eid))
        else:
            vertex,eid=stack.pop()
            if stack:
                traversal.append((stack[-1][0],vertex,eid))
    assert len(traversal)==len(edges) and all(seen)
    traversal.reverse()
    word = [0]
    seen_pairs = set()
    for u,v,_ in traversal:
        assert word[-1] == u
        if u == v:
            word.extend([u,u])
        else:
            pair = (min(u,v),max(u,v))
            if pair in seen_pairs:
                word.append(v)
            else:
                seen_pairs.add(pair)
                word.extend([v,u,v])
    assert word[-1] == word[0]
    cyclic = tuple(word[:-1])
    assert len(cyclic)==optimum(q)
    observed={(cyclic[i],cyclic[(i+1)%len(cyclic)])
              for i in range(len(cyclic)) if cyclic[i]==cyclic[(i+2)%len(cyclic)]}
    assert observed == set(product(range(q),repeat=2))
    undirected_counts = {}
    for i, u in enumerate(cyclic):
        v = cyclic[(i+1)%len(cyclic)]
        e = (min(u,v),max(u,v))
        undirected_counts[e] = undirected_counts.get(e,0)+1
    for u in range(q):
        assert undirected_counts[(u,u)] == 2
    extras = [(u,v) for u in range(q) for v in range(u+1,q)
              if undirected_counts[(u,v)] == 4]
    for u in range(q):
        for v in range(u+1,q):
            assert undirected_counts[(u,v)] in (3,4)
    if q%2:
        assert extras == []
    else:
        assert extras == [(2*i,2*i+1) for i in range(q//2)]
    return cyclic


def brute_minimum(q):
    # Every required cover has cyclic factor 000; rotate it to initial 00.
    # State tracks the last two letters and all completed palindrome windows.
    target=(1<<(q*q))-1
    start=(0,0,0)
    queue=deque([(start,2)])
    visited={start}
    states=0
    while queue:
        (x,y,mask),length=queue.popleft()
        states+=1
        if length >= 3:
            final_mask=mask
            if x == 0:  # triple (x,y,0)
                final_mask |= 1<<y
            if y == 0:  # triple (y,0,0)
                final_mask |= 1<<0
            if final_mask == target:
                return length,states
        for z in range(q):
            nm=mask | ((1<<(x*q+y)) if x==z else 0)
            node=(y,z,nm)
            if node not in visited:
                visited.add(node)
                queue.append((node,length+1))
    raise AssertionError('unreachable')


def run():
    covered=0
    for q in range(2,31):
        word=construct(q)
        covered+=q*q
        assert len(word)==optimum(q)
    for q in (2,3,4):
        exact,states=brute_minimum(q)
        assert exact==optimum(q),(q,exact,optimum(q))
        print('EXACT_CYCLIC_OPTIMUM q=%d length=%d BFS_STATES=%d'%
              (q,exact,states))
    print('VERIFY_OK alphabet_sizes=2..30 required_triplets=%d complete_constructive_covers=True brute_force_q=2..4'%covered)


if __name__=='__main__':
    run()
