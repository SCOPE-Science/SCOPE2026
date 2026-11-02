"""Reproduce super-domination and reconfiguration enumerations on crown graphs.
Requires Python 3.9+; no external dependencies.
"""
from collections import Counter, deque
from itertools import combinations
from math import comb


def crown_neighborhoods(n):
    # A_i has index i, B_j has index n+j; A_i ~ B_j iff i != j.
    return [tuple(n+j for j in range(n) if i != j) for i in range(n)] + [
        tuple(i for i in range(n) if i != j) for j in range(n)]


def superdom(n, chosen, nbr):
    left = set(range(2*n)) - set(chosen)
    witnesses = set()
    for w in chosen:
        outside = [x for x in nbr[w] if x in left]
        if len(outside) == 1:
            witnesses.add(outside[0])
    return witnesses == left


def predicted_omissions(n):
    c2 = comb(n, 2)
    return {0:1, 1:2*n, 2:n*n+2*c2,
            3:2*n*comb(n-1,2), 4:c2*comb(n-2,2)}


def minimum_states(n):
    pairs = list(combinations(range(n), 2))
    return [(a, b) for a in pairs for b in pairs if set(a).isdisjoint(b)]


def configuration_graph(n):
    states = minimum_states(n)
    ix = {s:i for i,s in enumerate(states)}
    adj = []
    for a, b in states:
        free = set(range(n)) - set(a) - set(b)
        neighbors = []
        for old in (a,b):
            for x in old:
                for y in free:
                    new = tuple(sorted((set(old)-{x})|{y}))
                    target = (new,b) if old==a else (a,new)
                    neighbors.append(ix[target])
        adj.append(tuple(neighbors))
    return states, adj


def bfs(graph, start):
    dist = {start:0}
    q = deque([start])
    while q:
        v = q.popleft()
        for w in graph[v]:
            if w not in dist:
                dist[w] = dist[v]+1
                q.append(w)
    return dist


def conjectured_distance(a,b,c,d):
    base = 4 - len(set(a)&set(c)) - len(set(b)&set(d))
    return base + int(set(a)|set(b) == set(c)|set(d) and (a,b)!=(c,d))


def run():
    for n in range(4,9):
        nbr = crown_neighborhoods(n)
        tally = Counter()
        minima = set()
        for mask in range(1 << (2*n)):
            selected = [v for v in range(2*n) if mask >> v & 1]
            if superdom(n,selected,nbr):
                omit = 2*n-len(selected)
                tally[omit] += 1
                if omit == 4:
                    minima.add(tuple(i for i in range(2*n) if not(mask >> i & 1)))
        assert dict(tally)==predicted_omissions(n),(n,tally,predicted_omissions(n))
        states = minimum_states(n)
        predicted = {tuple(sorted(set(a)|{n+j for j in b})) for a,b in states}
        assert minima==predicted,(n,len(minima),len(predicted))
        print('SUPERDOM',n, 'sets',sum(tally.values()), 'coefficients', dict(sorted(tally.items())))
    for n in range(4,11):
        states,adj = configuration_graph(n)
        vcount=comb(n,2)*comb(n-2,2)
        assert len(states)==vcount
        for neighbors in adj:
            assert len(neighbors)==4*(n-4)
        if n==4:
            assert all(not a for a in adj)
            print('RECONFIG',n, 'isolated',vcount)
            continue
        # The natural simultaneous permutation of the n indices acts transitively.
        src=states[0]
        distances=bfs(adj,0)
        assert len(distances)==len(states)
        freq=Counter()
        for i,(c,d) in enumerate(states):
            pred=conjectured_distance(src[0],src[1],c,d)
            assert distances[i]==pred, (n,src,(c,d),distances[i],pred)
            freq[pred]+=1
        assert max(distances.values())==5
        assert freq[5]==1
        print('RECONFIG',n,'vertices',len(states),'degree',len(adj[0]),
              'distance_shells', [freq[j] for j in range(6)])
    print('VERIFY_OK')

if __name__=='__main__':
    run()
