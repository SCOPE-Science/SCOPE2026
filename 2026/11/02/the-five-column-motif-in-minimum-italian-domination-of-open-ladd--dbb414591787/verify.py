"""Standalone exact finite-state certificate for minimum Italian domination on open ladders.

Execute: python3 italian_ladder_verify.py. No third-party packages needed.
"""
from collections import defaultdict, deque
from itertools import product

D = list(product(range(3), repeat=2))
W = [sum(x) for x in D]
H = [
    [0, 0, 1, 0, 1, 1, 1, 1, 2],
    [-1, 0, 1, 0, 1, 2, 1, 2, 3],
    [0, 1, 2, 1, 2, 3, 2, 3, 4],
    [-1, 0, 1, 0, 1, 2, 1, 2, 3],
    [0, 1, 2, 1, 2, 3, 2, 3, 4],
    [0, 1, 2, 1, 2, 3, 2, 3, 4],
    [0, 1, 2, 1, 2, 3, 2, 3, 4],
    [0, 1, 2, 1, 2, 3, 2, 3, 4],
    [1, 2, 3, 2, 3, 4, 3, 4, 5],
]

def ok(a, b, c):
    A, B, C = D[a], D[b], D[c]
    return all(B[r] > 0 or A[r] + B[1-r] + C[r] >= 2 for r in range(2))

def reach(initial, adjacency):
    seen, queue = set(initial), list(initial)
    while queue:
        for nxt in adjacency.get(queue.pop(), []):
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return seen

def verify_certificate():
    triples = 0
    for a, b in product(range(9), repeat=2):
        if ok(0, a, b):
            assert W[a] + W[b] - 2 >= H[a][b], ('left boundary', a, b)
        if ok(a, b, 0):
            assert H[a][b] >= 0, ('right boundary', a, b)
        for c in range(9):
            triples += 1
            if ok(a, b, c):
                assert H[a][b] + W[c] - 1 >= H[b][c], ('middle', a, b, c)
    assert triples == 729

    initial = {9*a+b for a in range(9) for b in range(9)
               if ok(0, a, b) and W[a] + W[b] - 2 == H[a][b]}
    terminal = {9*a+b for a in range(9) for b in range(9)
                if ok(a, b, 0) and H[a][b] == 0}
    adj, back = defaultdict(list), defaultdict(list)
    for a, b, c in product(range(9), repeat=3):
        if ok(a, b, c) and H[a][b] + W[c] - 1 == H[b][c]:
            u, v = 9*a+b, 9*b+c
            adj[u].append(v)
            back[v].append(u)
    alive = reach(initial, adj) & reach(terminal, back)
    expected = {
        1:(12,), 3:(28,), 5:(45,), 7:(63,), 9:(7,), 10:(12,),
        12:(27,28,30), 27:(5,), 28:(9,10,12), 30:(28,),
        45:(3,), 63:(1,),
    }
    assert alive == set(expected)
    assert initial & alive == {12,28}
    assert terminal & alive == {12,28}
    assert {i:tuple(sorted(set(adj[i]) & alive)) for i in alive} == expected
    return expected

def direct_minimum_dp(n):
    """Independent full Italian-domination dynamic programming, no potential used."""
    if n == 1:
        raise ValueError('Ladder starts at two columns')
    dp = {(a,b):(W[a]+W[b],1) for a,b in product(range(9),repeat=2) if ok(0,a,b)}
    for _ in range(3,n+1):
        new = {}
        for (a,b),(cost,count) in dp.items():
            for c in range(9):
                if not ok(a,b,c):
                    continue
                key, total = (b,c), cost+W[c]
                if key not in new or total<new[key][0]:
                    new[key]=(total,count)
                elif total==new[key][0]:
                    new[key]=(total,new[key][1]+count)
        dp=new
    feasible = [x for (a,b),x in dp.items() if ok(a,b,0)]
    minweight=min(v for v,_ in feasible)
    return minweight,sum(count for val,count in feasible if val==minweight)

def brute(n):
    """Original graph-rule check over all 3^(2n) labelings for n=2,...,6."""
    best = 2*n+1
    count = 0
    for lab in product(range(3),repeat=2*n):
        weight = sum(lab)
        if weight>best:
            continue
        valid = True
        for c in range(n):
            for r in range(2):
                v = 2*c+r
                if lab[v]:
                    continue
                neigh = lab[2*c+1-r]
                if c:
                    neigh += lab[v-2]
                if c+1<n:
                    neigh += lab[v+2]
                if neigh<2:
                    valid=False
                    break
            if not valid:
                break
        if valid:
            if weight<best:
                best,count=weight,1
            else:
                count+=1
    return best,count

def main():
    arcs=verify_certificate()
    # Composition bijection from alternating connector states and excursions
    comp=[0]*79
    comp[0]=1
    for j in range(1,len(comp)):
        comp[j]=sum(comp[j-d] for d in (1,2,5) if d<=j)
    ways={12:1,28:1}
    for n in range(2,64):
        count=sum(ways.get(x,0) for x in (12,28))
        assert count==2*comp[n-2], ('tight walk',n,count,2*comp[n-2])
        if n<=60:
            assert direct_minimum_dp(n)==(n,count), ('full DP', n)
        if n<=6:
            assert brute(n)==(n,count), ('independent brute', n)
        nxt=defaultdict(int)
        for u,v in ways.items():
            for w in arcs[u]:
                nxt[w]+=v
        ways=nxt
    print('VERIFY_OK: 729 local certificate triples; 12 tight states and 16 tight arcs; n=2..60 full DP; n=2..6 direct graph enumeration; n=2..63 composition identity')
    print('minimum counts n=2..11:',[(n,2*comp[n-2]) for n in range(2,12)])

if __name__ == '__main__':
    main()
