"""Independent integer-polynomial irreducibility check (requires SymPy)."""
from sympy import Poly, symbols, factor_list
T = symbols('T')
F2 = 1 - T*T + 4*T**4
F4 = 1 - 2*T*T + T**4 - 8*T**6 + 16*T**8
for degree, f in ((4,F2),(8,F4)):
    p=Poly(f,T,domain='ZZ')
    assert p.degree()==degree
    assert p.is_irreducible
    unit, factors=factor_list(p)
    assert unit==1 and len(factors)==1 and factors[0][0]==p and factors[0][1]==1
print('SIMPLE_FACTOR_VERIFY_OK')
