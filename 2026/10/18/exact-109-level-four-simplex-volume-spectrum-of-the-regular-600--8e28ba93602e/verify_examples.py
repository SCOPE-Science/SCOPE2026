"""Independent symbolic checks of extremal 4-simplex witnesses.

Requires SymPy. Reads the companion spectrum.csv for count consistency.
"""
from csv import DictReader
from math import comb
from sympy import Matrix, Rational, sqrt, simplify

phi = (1 + sqrt(5))/2
base = [
    (-2, 0, 0, 0),
    (phi-1, 0, phi, 1),
    (phi-1, 0, -phi, 1),
    (phi-1, 1, 0, -phi),
]
ends = [(0,-2,0,0), (0,-phi,phi-1,-1)]

def determinant(vertices):
    v = Matrix(vertices)
    return simplify(Matrix([[v[i,j]-v[0,j] for j in range(4)]
                            for i in range(1,5)]).det())

expected = -12-24*phi
for v in ends:
    assert simplify(determinant(base+[v])-expected)==0
mid = tuple((a+b)/2 for a,b in zip(*ends))
assert simplify(determinant(base+[mid])-expected)==0
with open('spectrum.csv', newline='', encoding='utf-8') as handle:
    rows = list(DictReader(handle))
assert len(rows)==109
assert sum(int(r['total_count']) for r in rows)==comb(120,5)
assert sum(int(r['count_through_vertex']) for r in rows)==comb(119,4)
assert rows[0] == {'det_a':'0','det_b':'0','count_through_vertex':'687241',
                   'total_count':'16493784'}
assert rows[-1] == {'det_a':'12','det_b':'24','count_through_vertex':'100',
                    'total_count':'2400'}
print('SYMBOLIC_CHECK_OK two endpoint simplices and their midpoint attain the sharp determinant')
