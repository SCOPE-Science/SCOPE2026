#!/usr/bin/env python3
"""Exact integer check of the nonzero edge-direction stretches for a planar map.

The mathematical argument is independent of this finite audit; all parameter values
share the same four derivative matrices.
"""

A = {
    'Q1': (( 1,-1),(1,-1)),
    'Q2': ((-1,-1),(1,-1)),
    'Q3': ((-1,-1),(1, 1)),
    'Q4': (( 1,-1),(1, 1)),
}
V = {'horizontal': (1,0), 'vertical': (0,1),
     'northeast': (1,1), 'southeast': (1,-1)}

for quadrant, matrix in A.items():
    for direction, vector in V.items():
        out = tuple(row[0]*vector[0]+row[1]*vector[1] for row in matrix)
        in_squared = sum(x*x for x in vector)
        out_squared = sum(x*x for x in out)
        if out_squared:
            assert out_squared in (2*in_squared,4*in_squared), (
                quadrant,direction,out,out_squared,in_squared)
        else:
            assert (quadrant,direction) in {('Q1','northeast'),('Q3','southeast')}
    print(quadrant, 'all four direction images verified exactly')

# Once a fixed iterate r >= 4 has no zero-slope intermediate branch,
# its Euclidean length multiplier is >= (sqrt(2))**r.
for r in range(4,11):
    assert 9 < 2**r  # equivalently 3*2**(-r/2)<1
print('A four-step Lasota--Yorke variation contraction threshold holds.')
