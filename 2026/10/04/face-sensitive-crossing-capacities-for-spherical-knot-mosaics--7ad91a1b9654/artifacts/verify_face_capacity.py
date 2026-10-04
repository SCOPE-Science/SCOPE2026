#!/usr/bin/env python3
"""Exact finite replay for face-support crossing-position capacities."""
import itertools

FACES = ('+x','-x','+y','-y','+z','-z')
OPP = {'+x':'-x','-x':'+x','+y':'-y','-y':'+y','+z':'-z','-z':'+z'}
# Cyclic neighbors around each face. Opposite entries in this 4-cycle correspond
# to opposite sides of the square face; adjacent entries correspond to adjacent sides.
CYCLE = {
    '+x': ('+y','+z','-y','-z'), '-x': ('+y','-z','-y','+z'),
    '+y': ('+x','-z','-x','+z'), '-y': ('+x','+z','-x','-z'),
    '+z': ('+x','+y','-x','-y'), '-z': ('+x','-y','-x','+y'),
}

def face_capacity(face, support, n):
    forbidden=[i for i,g in enumerate(CYCLE[face]) if g not in support]
    # A crossing tile must avoid every boundary side abutting an empty face.
    rows=n; cols=n
    # sides 0,2 and 1,3 are opposite pairs in the chosen cyclic order.
    if 0 in forbidden: rows -= 1
    if 2 in forbidden: rows -= 1
    if 1 in forbidden: cols -= 1
    if 3 in forbidden: cols -= 1
    return max(rows,0)*max(cols,0)

def capacity(support,n):
    return sum(face_capacity(f,support,n) for f in support)

def formulas(n):
    return {
        1:(n-2)**2,
        2:2*(n-1)*(n-2),
        3:3*(n-1)**2,
        4:2*(n-1)*(2*n-1),
        5:5*n*n-4*n,
    }

for n in range(2,101):
    want=formulas(n)
    for f in range(1,6):
        vals=[capacity(set(S),n) for S in itertools.combinations(FACES,f)]
        got=max(vals)
        assert got == want[f], (n,f,got,want[f])
    # Monotonicity through the known all-six-face knot bound.
    seq=[want[f] for f in range(1,6)] + [6*n*n-3*n+1]
    assert all(a <= b for a,b in zip(seq,seq[1:])), (n,seq)

print('VERIFY_OK n=2..100; all 62 nonempty proper face supports enumerated per n; formulas B1..B5 exact as positional capacities')
print('n=2:', [formulas(2)[f] for f in range(1,6)] + [19])
print('n=3:', [formulas(3)[f] for f in range(1,6)] + [46])
