"""Independent vertex-decision enumerator for maximal-matchings on two cubic graphs.

This implementation neither enumerates edge subsets nor uses generalized Petersen edges.
Only the Python standard library is required.
"""
from collections import Counter, deque
from itertools import combinations
import json


def graphs():
    pairs = list(combinations(range(5),2))
    p_edges = {(i,j) for i in range(10) for j in range(i+1,10)
               if not (set(pairs[i]) & set(pairs[j]))}
    # The Kronecker bipartite double of the Kneser Petersen representation.
    d_edges = {tuple(sorted((2*u,2*v+1))) for u,v in p_edges}
    d_edges |= {tuple(sorted((2*u+1,2*v))) for u,v in p_edges}
    return {'Petersen_G(5,2)': (10, sorted(p_edges)),
            'Desargues_G(10,3)': (20, sorted(d_edges))}


def matchings_by_vertices(n, edges):
    neighbor = [0] * n
    edge_lookup = {}
    for i,(a,b) in enumerate(edges):
        neighbor[a] |= 1 << b
        neighbor[b] |= 1 << a
        edge_lookup[(a,b)] = i
    groups = {}
    # At each step the smallest unresolved vertex is left unmatched or
    # paired with one unresolved neighbor, obtaining each matching once.
    def recurse(remaining, unmatched, matching):
        if remaining == 0:
            # Maximal iff no edge joins two unmatched vertices.
            if all(not ((unmatched >> a) & (unmatched >> b) & 1)
                   for a,b in edges):
                groups.setdefault(len(matching),[]).append(tuple(sorted(matching)))
            return
        low = remaining & -remaining
        v = low.bit_length()-1
        remaining ^= low
        recurse(remaining, unmatched | low, matching)
        can_pair = remaining & neighbor[v]
        while can_pair:
            bit = can_pair & -can_pair
            w = bit.bit_length()-1
            pair = (min(v,w),max(v,w))
            matching.append(edge_lookup[pair])
            recurse(remaining ^ bit, unmatched, matching)
            matching.pop()
            can_pair ^= bit
    recurse((1 << n)-1,0,[])
    return groups


def classify(n,edges):
    groups = matchings_by_vertices(n,edges)
    results = {}
    for k,matchings in sorted(groups.items()):
        matchings = sorted(matchings)
        assert len(matchings)==len(set(matchings))
        adjacency=[set() for _ in matchings]
        edge_positions={}
        for i,matching in enumerate(matchings):
            for edge in matching:
                partial=tuple(e for e in matching if e!=edge)
                edge_positions.setdefault(partial,[]).append(i)
        for group in edge_positions.values():
            for a,b in combinations(group,2):
                adjacency[a].add(b)
                adjacency[b].add(a)
        visited=set();component_sizes=[];diameters=[]
        for source in range(len(matchings)):
            if source in visited:continue
            comp={source}; stack=[source]
            for v in stack:
                for w in adjacency[v]:
                    if w not in comp:comp.add(w);stack.append(w)
            visited.update(comp)
            component_sizes.append(len(comp))
            diam=0
            for start in comp:
                ds={start:0}; q=deque([start])
                while q:
                    v=q.popleft()
                    for w in adjacency[v]:
                        if w not in ds:
                            ds[w]=ds[v]+1;q.append(w)
                assert len(ds)==len(comp)
                diam=max(diam,max(ds.values()))
            diameters.append(diam)
        results[str(k)]={
            'matchings':len(matchings),
            'exchange_edges':sum(len(x) for x in adjacency)//2,
            'components':len(component_sizes),
            'component_sizes':dict(sorted(Counter(component_sizes).items())),
            'degree_distribution':dict(sorted(Counter(len(x) for x in adjacency).items())),
            'diameters':dict(sorted(Counter(diameters).items())),
        }
    return results


def main():
    result={name:classify(n,edges) for name,(n,edges) in graphs().items()}
    print(json.dumps(result,sort_keys=True,separators=(',',':')))
    print('VERIFY_OK')


if __name__=='__main__':
    main()
