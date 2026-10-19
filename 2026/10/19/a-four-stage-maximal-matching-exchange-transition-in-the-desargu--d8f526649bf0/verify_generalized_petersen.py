"""Exhaustive edge-subset certificate for maximal-matching exchange graphs.

Requires Python 3.9 or later; uses only the standard library.
"""
from collections import Counter, deque
import json


def edges_gp(n, k):
    # Generalized Petersen G(n,k): vertices 0..n-1 outer, n..2n-1 inner.
    edges = {tuple(sorted((i, (i+1) % n))) for i in range(n)}
    edges |= {(i, n+i) for i in range(n)}
    edges |= {tuple(sorted((n+i, n+(i+k) % n))) for i in range(n)}
    return sorted(edges)


def enumerate_maximal_matchings(edges, nvertices):
    endpoints = [(1 << u) | (1 << v) for u,v in edges]
    all_items = []
    def visit(i, occupied, chosen):
        if i == len(edges):
            if all(occupied & edge_mask for edge_mask in endpoints):
                all_items.append(tuple(chosen))
            return
        visit(i+1, occupied, chosen)
        if not (occupied & endpoints[i]):
            chosen.append(i)
            visit(i+1, occupied | endpoints[i], chosen)
            chosen.pop()
    visit(0, 0, [])
    return all_items


def get_invariants(edges, nvertices):
    bysize = {}
    for matching in enumerate_maximal_matchings(edges, nvertices):
        bysize.setdefault(len(matching), []).append(matching)
    out = {}
    for k, matchings in sorted(bysize.items()):
        states = sorted(matchings)
        lookup = {state: j for j,state in enumerate(states)}
        neighbors = [set() for _ in states]
        for i, state in enumerate(states):
            present = set(state)
            for removed in state:
                retained = present - {removed}
                for added in range(len(edges)):
                    if added in present:
                        continue
                    trial = tuple(sorted(retained | {added}))
                    j = lookup.get(trial)
                    if j is not None:
                        neighbors[i].add(j)
        components = []
        visited = set()
        for start in range(len(states)):
            if start in visited:
                continue
            queue = deque([start]); visited.add(start); component = []
            while queue:
                i = queue.popleft(); component.append(i)
                for j in neighbors[i]:
                    if j not in visited:
                        visited.add(j); queue.append(j)
            components.append(component)
        eccentricities = []
        for component in components:
            if len(component) == 1:
                eccentricities.append(0)
                continue
            allowed = set(component)
            diameter = 0
            for source in component:
                levels = {source:0}; queue = deque([source])
                while queue:
                    i = queue.popleft()
                    for j in neighbors[i]:
                        if j in allowed and j not in levels:
                            levels[j] = levels[i] + 1
                            queue.append(j)
                assert len(levels) == len(component)
                diameter = max(diameter, max(levels.values()))
            eccentricities.append(diameter)
        out[str(k)] = {
            'matchings':len(states),
            'exchange_edges':sum(map(len,neighbors))//2,
            'components':len(components),
            'component_sizes':dict(sorted(Counter(map(len,components)).items())),
            'degree_distribution':dict(sorted(Counter(map(len,neighbors)).items())),
            'diameters':dict(sorted(Counter(eccentricities).items())),
        }
        assert sum(len(c) for c in components) == len(states)
        assert sum(out[str(k)]['component_sizes'].values()) <= len(states)
    return out


def main():
    result = {
        'Petersen_G(5,2)': get_invariants(edges_gp(5,2),10),
        'Desargues_G(10,3)': get_invariants(edges_gp(10,3),20),
    }
    print(json.dumps(result,sort_keys=True,separators=(',',':')))
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
