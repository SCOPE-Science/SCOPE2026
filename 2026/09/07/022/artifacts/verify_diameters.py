"""Exact matrix mutation closures and all-pairs graph diameters, stdlib only."""
import csv
from collections import deque
from pathlib import Path
import sys

def mutate(b, k):
    return tuple(-b[5*i+j] if i == k or j == k else
                 b[5*i+j] + (abs(b[5*i+k])*b[5*k+j] +
                 b[5*i+k]*abs(b[5*k+j]))//2
                 for i in range(5) for j in range(5))

def check(path):
    rows = list(csv.DictReader(Path(path).read_text().splitlines()))
    assert len(rows) == 7
    for row in sorted(rows, key=lambda x: int(x['N_labeled'])):
        root = tuple(map(int, row['lexmin_matrix_flat25'].split(';')))
        nodes, ids = [root], {root: 0}
        adj = []
        for b in nodes:
            neighbors = []
            for k in range(5):
                c = mutate(b, k)
                assert max(map(abs, c)) <= 2
                assert mutate(c, k) == b
                if c not in ids:
                    ids[c] = len(nodes)
                    nodes.append(c)
                neighbors.append(ids[c])
            adj.append(neighbors)
        assert len(nodes) == int(row['N_labeled'])
        diameter = 0
        for source in range(len(nodes)):
            distances = [-1]*len(nodes)
            distances[source] = 0
            q = deque([source])
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if distances[v] == -1:
                        distances[v] = distances[u] + 1
                        q.append(v)
            assert min(distances) == 0
            diameter = max(diameter, max(distances))
        assert diameter == int(row['diameter'])
        print('class', row['class_id'], 'order', len(nodes), 'diameter', diameter, flush=True)
    print('DIAMETERS_OK')

if __name__ == '__main__':
    check(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).with_name('representatives.csv'))
