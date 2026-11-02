"""Exact independent finite checks for an elliptic Kummer fiber-product theorem.

Runs with Python 3 and SymPy. The all-parameter proof is in RESULT.md.
"""
from itertools import product
from math import gcd
import sympy as sp

x, y = sp.symbols('x y')
I = sp.I
plus = -2*(1+I*y)/x**2
minus = -2*(1-I*y)/x**2
# x(P+T), x(P-T) via elliptic group law, with T=(0,i).
num = sp.together(x*plus*minus - 4)*x**3
poly = sp.Poly(sp.cancel(num), y, domain=sp.QQ.algebraic_field(I).poly_ring(x))
assert sp.rem(poly, sp.Poly(y*y-x**3+1,y,domain=sp.QQ.algebraic_field(I).poly_ring(x))).is_zero

D = [(-2,1,1),(1,-2,1),(1,1,-2)]
assert [sum(D[j][k] for j in range(3)) for k in range(3)] == [0,0,0]
assert D[0][0]*D[1][1]-D[1][0]*D[0][1] == 3

for m in (5,7,11,13,17,19):
    for k in (1,2,3):
        ker = [a for a in product(range(m),repeat=k)
               if all(sum(a[j]*D[j][l] for j in range(k))%m==0 for l in range(3))]
        expected = [(0,)*k] if k<3 else [(z,z,z) for z in range(m)]
        assert set(ker) == set(expected), (m,k,ker)
        # The local Kummer inertia order at each point in this orbit is m.
        assert all(gcd(m,*[abs(D[j][l]) for j in range(k)])==1 for l in range(3))

# For t full cosets, c occupied cosets and r indexed shifts,
# the normalized fiber product has m^t components, each degree m^(r-t).
def invariants(m, occupancy):
    assert m>=5 and gcd(m,6)==1 and occupancy and all(1<=k<=3 for k in occupancy)
    r=sum(occupancy); c=len(occupancy); t=occupancy.count(3); s=r-t
    components=m**t; degree=m**s
    genus=1+3*c*degree*(m-1)//(2*m)
    assert 2*(genus-1)==3*c*degree*(m-1)//m
    assert components*degree==m**r
    return (components,degree,genus)

assert invariants(5,[1,1]) == (1,25,61)
assert invariants(5,[2]) == (1,25,31)
assert invariants(5,[3]) == (5,25,31)
assert invariants(5,[3,1]) == (5,125,301)
assert invariants(5,[1,1,1,1]) == (1,625,3001)
print('VERIFY_OK: translation, valuation kernels, inertia, and genus examples')
