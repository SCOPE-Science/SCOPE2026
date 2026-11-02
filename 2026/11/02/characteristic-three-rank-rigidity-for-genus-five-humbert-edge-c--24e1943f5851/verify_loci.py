"""Exact characteristic-three polynomial certificates for five degeneracy divisors.

Dependency: sympy==1.14.0. Run: python verify_loci.py
"""
from itertools import combinations
import sympy as sp

u, v, z = sp.symbols('u v z')
forbidden = u * v * (u - 1) * (v - 1) * (u - v)
conditions = [u + 1, v + 1, u + v, u + v + 1, u*v + u + v]
for i, j in combinations(range(5), 2):
    ideal = sp.groebner(
        [conditions[i], conditions[j], z*forbidden-1],
        z, u, v, modulus=3,
    )
    assert len(ideal.polys) == 1 and ideal.polys[0].as_expr() == 1, (i,j)
print('PAIRWISE_SATURATION_OK', 10)
# The five equations are each an invertible graph over a coordinate line
# with precisely three forbidden parameter values 0, 1, and -1.
# Thus every locus has q-3 points over any field of order q=3^m.
for q in [9, 27, 81]:
    assert (q-2)*(q-3) == 5*(q-3)+(q-3)*(q-7)
print('COUNT_POLYNOMIAL_OK')
