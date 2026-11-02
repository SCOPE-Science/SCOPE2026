"""Standalone exact finite certificate for total perfect Roman domination on ladders.

Run: python3 verify.py  (Python standard library only).
No inputs, network, or external packages are required.
"""
from itertools import product
from math import comb

COL = tuple(product((0, 1, 2), repeat=2))
K = len(COL)
STATES = K*K
ABSENT = (0, 0)
INF = 10**12


def valid(a, b, c):
    """Feasibility at column b, given its two adjoining columns."""
    for row in range(2):
        neighbors = (a[row], b[1-row], c[row])
        if b[row] == 0:
            if sum(label == 2 for label in neighbors) != 1:
                return False
        elif not any(label > 0 for label in neighbors):
            return False
    return True


def state(a, b):
    return a*K+b


def new_layer(cost, count):
    best = [INF]*STATES
    ways = [0]*STATES
    for a in range(K):
        for b in range(K):
            old = state(a, b)
            if cost[old] == INF:
                continue
            for c in range(K):
                if not valid(COL[a], COL[b], COL[c]):
                    continue
                nxt = state(b, c)
                cand = cost[old]+sum(COL[c])
                if cand < best[nxt]:
                    best[nxt] = cand
                    ways[nxt] = count[old]
                elif cand == best[nxt]:
                    ways[nxt] += count[old]
    return best, ways


def terminal(cost, count):
    candidates = [state(a,b) for a in range(K) for b in range(K)
                  if valid(COL[a], COL[b], ABSENT) and cost[state(a,b)] < INF]
    val = min(cost[s] for s in candidates)
    return val, sum(count[s] for s in candidates if cost[s] == val)


def build(N=17):
    initial_cost = [INF]*STATES
    initial_count = [0]*STATES
    for a in range(K):
        for b in range(K):
            if valid(ABSENT, COL[a], COL[b]):
                s = state(a,b)
                initial_cost[s] = sum(COL[a])+sum(COL[b])
                initial_count[s] = 1
    out = {2:(initial_cost,initial_count)}
    for n in range(3,N+1):
        out[n] = new_layer(*out[n-1])
    return out


def target(n):
    q, r = divmod(n, 3)
    optimum = 2*n-2*q
    if r == 0:
        number = 1
    elif r == 1:
        number = q+1
    else:
        number = 13+9*q*(q+3)//2
    return optimum, number


def independent_graph_census(n):
    """Directly check labels of all individual vertices, without column transitions."""
    adjacency = [[] for _ in range(2*n)]
    for col in range(n):
        for row in range(2):
            v = 2*col+row
            adjacency[v].append(2*col+1-row)
            if col: adjacency[v].append(2*(col-1)+row)
            if col+1<n: adjacency[v].append(2*(col+1)+row)
    minimum, ways = INF, 0
    for labels in product((0,1,2),repeat=2*n):
        weight = sum(labels)
        if weight > minimum:
            continue
        accepted = True
        for v,x in enumerate(labels):
            neigh = [labels[u] for u in adjacency[v]]
            if x == 0:
                if sum(y==2 for y in neigh) != 1:
                    accepted=False
                    break
            elif not any(y>0 for y in neigh):
                accepted=False
                break
        if accepted:
            if weight < minimum:
                minimum, ways = weight, 0
            ways += 1
    return minimum, ways


def canonical_witness(n):
    q,r = divmod(n,3)
    symbols = [0,2,0]*q + ([1] if r==1 else [0,2] if r==2 else [])
    assert len(symbols) == n
    for j,b in enumerate(symbols):
        a = symbols[j-1] if j else 0
        c = symbols[j+1] if j<n-1 else 0
        assert valid((a,a),(b,b),(c,c))
    return 2*sum(symbols)


def main():
    D = build()
    # A finite exact identity of all 81 min-cost states, not only terminal states.
    for r in (3,4,5):
        c1, _ = D[r]
        c2, _ = D[r+3]
        for i in range(STATES):
            assert (c1[i]==INF and c2[i]==INF) or (c1[i]<INF and c2[i]==c1[i]+4), (r,i)
    # The fourth forward difference of every state count is zero at each phase.
    # Because the min-cost states repeat up to a constant, the optimal-transition
    # matrices repeat every three steps. Thus their fourth differences remain zero.
    for r in (3,4,5):
        for s in range(STATES):
            delta4 = sum((-1)**(4-j)*comb(4,j)*D[r+3*j][1][s] for j in range(5))
            assert delta4==0, (r,s,delta4)
    # Four terminal values uniquely fix each polynomial of degree at most three.
    for r in (3,4,5):
        for j in range(4):
            n=r+3*j
            assert terminal(*D[n])==target(n), (n,terminal(*D[n]),target(n))
    assert terminal(*D[2]) == target(2)
    for n in range(2,18):
        assert terminal(*D[n])==target(n)
    for n in range(2,7):
        assert independent_graph_census(n)==target(n), (n,independent_graph_census(n),target(n))
    for n in range(2,101):
        assert canonical_witness(n)==target(n)[0]
    print('VERIFY_OK: 81-state three-period min-plus certificate; fourth state-count differences;')
    print('           four terminal samples per phase; 5 direct all-label graph censuses;')
    print('           99 explicit constructions (lengths 2 through 100).')
    for n in range(2,15):
        print(n,*target(n))

if __name__ == '__main__':
    main()
