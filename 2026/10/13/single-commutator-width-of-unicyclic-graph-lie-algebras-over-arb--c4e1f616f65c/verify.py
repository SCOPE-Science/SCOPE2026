"""Finite-field exhaustive checks for graph-Lie commutator-width criterion."""
from itertools import product

CASES = [
    ('triangle', 2, 3, [(0,1),(1,2),(2,0)], True),
    ('triangle', 3, 3, [(0,1),(1,2),(2,0)], True),
    ('triangle with leaf', 2, 4, [(0,1),(1,2),(2,0),(0,3)], False),
    ('triangle with leaf', 3, 4, [(0,1),(1,2),(2,0),(0,3)], False),
    ('square with one leaf', 2, 5, [(0,1),(1,2),(2,3),(3,0),(0,4)], True),
    ('square with one leaf', 3, 5, [(0,1),(1,2),(2,3),(3,0),(0,4)], True),
    ('square with opposite leaves', 2, 6, [(0,1),(1,2),(2,3),(3,0),(0,4),(2,5)], True),
    ('square with adjacent leaves', 2, 6, [(0,1),(1,2),(2,3),(3,0),(0,4),(1,5)], False),
]

def bracket_image(q, n, edges):
    labels = list(product(range(q), repeat=2))
    out = set()
    for idx in product(range(q*q), repeat=n):
        pair = [labels[t] for t in idx]
        out.add(tuple((pair[i][0]*pair[j][1]-pair[i][1]*pair[j][0]) % q for i,j in edges))
    return out

def main():
    for label,q,n,edges,expected in CASES:
        image = bracket_image(q,n,edges)
        ambient = set(product(range(q),repeat=len(edges)))
        assert (image==ambient)==expected,(label,q,'width-classification')
        # Sum of two commutators must cover every central value.
        if not expected:
            sums = {tuple((x+y)%q for x,y in zip(u,v)) for u in image for v in image}
            assert sums==ambient,(label,q,'width-two')
        print(f'{label}: q={q}, image={len(image)}/{len(ambient)}, width={1 if expected else 2}')
    print('VERIFY_OK')

if __name__=='__main__':
    main()
