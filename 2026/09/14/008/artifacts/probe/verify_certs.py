import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from m4_data import COVERS, EDGES, n
from fractions import Fraction

# Independent exact re-verification of certs.txt (pure stdlib, no solver):
# each line: x (11 half-integers), z (16 rationals); check z>=0, loads(z)<=x,
# sum z >= 29/38, and x is an edge-cover.
TARGET = Fraction(29, 38)
n = 0
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'certs.txt')) as f:
    for line in f:
        assert line.startswith('x=')
        body, zpart = line.strip().split(' z=')
        xs = body[2:].split(',')
        zs, val = zpart.split(' val=')
        x = [Fraction(v) for v in xs]
        z = [Fraction(v) for v in zs.split(',')]
        assert len(x) == 11 and len(z) == 16
        assert all(v >= 0 for v in z)
        assert all(x[u] + x[v] >= 1 for (u, v) in EDGES), 'x not edge-cover'
        for v in range(11):
            assert sum(z[i] for i, C in enumerate(COVERS) if v in C) <= x[v], 'load violated'
        assert sum(z) >= TARGET, 'value below target'
        assert Fraction(val) == sum(z)
        n += 1
print('independently verified certs:', n)
