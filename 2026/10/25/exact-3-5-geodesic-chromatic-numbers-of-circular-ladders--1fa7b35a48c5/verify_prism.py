"""Independent finite checks for bounded-geodesic colorings of prism graphs.
Uses only Python's standard library.  Exhaustiveness of lower-bound searches
is justified by canonical first-occurrence color labels and full backtracking.
"""
import json
from collections import deque
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parent
WORDS = json.loads((ROOT / 'prism_witnesses.json').read_text('utf-8'))
PERIOD = [(0, 1), (1, 0), (2, 3), (3, 2)]


def adjacency(n, circular=True):
    """Vertex id: row*n + column; rows 0 and 1."""
    adj = [set() for _ in range(2*n)]
    for row in (0, 1):
        for i in range(n):
            v = row*n+i
            adj[v].add((1-row)*n+i)
            for j in (i-1, i+1):
                if circular:
                    adj[v].add(row*n+(j % n))
                elif 0 <= j < n:
                    adj[v].add(row*n+j)
    return [tuple(sorted(x)) for x in adj]


def forbidden_triples(n, circular=True):
    """Build all triples on a geodesic of length <=5 from BFS distances.
    Does not use a transfer-state simplification or the witness construction.
    """
    adj = adjacency(n, circular)
    N = 2*n
    hyperedges = set()
    for root in range(N):
        dist = [-1]*N
        dist[root] = 0
        queue = deque([root])
        while queue:
            v = queue.popleft()
            for w in adj[v]:
                if dist[w] < 0:
                    dist[w] = dist[v] + 1
                    queue.append(w)
        def dfs(path):
            if len(path) >= 3 and len(path)-1 == dist[path[-1]]:
                hyperedges.update(combinations(sorted(path), 3))
            if len(path) >= 6:
                return
            for w in adj[path[-1]]:
                if w not in path:
                    dfs(path+[w])
        dfs([root])
    return sorted(hyperedges)


def coloring_from_word(word):
    return [pair[0] for pair in word]+[pair[1] for pair in word]


def verify_word(word):
    colors = coloring_from_word(word)
    triples = forbidden_triples(len(word))
    for x,y,z in triples:
        if colors[x] == colors[y] == colors[z]:
            raise AssertionError((len(word), x,y,z,colors[x]))
    return len(triples)


def exhaustive_noncolorability(n, palette, circular=True):
    """Complete canonical-labeling search, including color-label symmetry.
    Branches on a fixed vertex order and may introduce only the next unseen
    color: any coloring is equivalent to one of these canonical colorings.
    """
    triples = forbidden_triples(n, circular)
    inc = [[] for _ in range(2*n)]
    for a,b,c in triples:
        inc[a].append((b,c)); inc[b].append((a,c)); inc[c].append((a,b))
    # Interleaved order by consecutive columns, fixed a priori.
    order = [r*n+i for i in range(n) for r in (0,1)]
    a = [-1]*(2*n)
    a[order[0]] = 0
    count = 0
    def dfs(i, used):
        nonlocal count
        count += 1
        if i == len(order):
            return True
        v = order[i]
        forbidden = {a[x] for x,y in inc[v] if a[x]>=0 and a[x]==a[y]}
        for c in range(min(used+1,palette)):
            if c in forbidden:
                continue
            a[v] = c
            if dfs(i+1, max(used,c+1)):
                return True
        a[v] = -1
        return False
    feasible = dfs(1, 1)
    if feasible:
        raise AssertionError(f'unexpected coloring: n={n}, palette={palette}, colors={a}')
    return count


def verify_six_windows(word):
    """Independently check every cyclic six-column window on the linear strip."""
    n = len(word)
    strip_triples = forbidden_triples(6, circular=False)
    for start in range(n):
        sub = [word[(start+i) % n] for i in range(6)]
        colors = coloring_from_word(sub)
        for x,y,z in strip_triples:
            if colors[x] == colors[y] == colors[z]:
                raise AssertionError((n,start,x,y,z))

def pumped(word, times=1):
    # The first nine columns of each pumpable seed coincide with PERIOD.
    # Inserting four more consecutive periodic columns closes a five-column
    # finite-state loop. Iterate without altering the rest of the word.
    for _ in range(times):
        word = word[:4] + PERIOD + word[4:]
    return word


def main():
    small = {3:1,4:1,5:2,6:2,7:3,8:3,9:4}
    for n, palette in small.items():
        nodes = exhaustive_noncolorability(n, palette)
        print(f'EXHAUSTIVE prism={n} colors={palette} search_nodes={nodes} impossible=YES')
    nodes = exhaustive_noncolorability(5, 3, circular=False)
    print(f'EXHAUSTIVE linear_ladder=5 colors=3 search_nodes={nodes} impossible=YES')
    print(f'UPPER seed_sizes={sorted(map(int, WORDS))}')
    for nstr, record in sorted(WORDS.items(), key=lambda x: int(x[0])):
        n = int(nstr)
        word = record['word']
        assert len(word)==n
        assert all(0 <= c < record['colors'] for p in word for c in p)
        if record['periodic_prefix']:
            assert n in {12,14,15,21}
            assert all(tuple(word[i]) == PERIOD[i%4] for i in range(10))
        verify_word(word)
        if n >= 10:
            verify_six_windows(word)
        if record['periodic_prefix']:
            for j in (1,2,4,8):
                verify_word(pumped(word,j))
                verify_six_windows(pumped(word,j))
            print(f'PUMP base={n} plus_steps=1,2,4,8 verified=YES')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
