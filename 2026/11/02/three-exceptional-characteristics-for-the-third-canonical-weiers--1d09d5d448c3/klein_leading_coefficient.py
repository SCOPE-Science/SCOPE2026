#!/usr/bin/env python3
"""Integral leading-term normalization of the 3-canonical Klein Wronskian.
Only exact arithmetic. Pair with the argument in RESULT.md.
"""
import math
import sympy as s

t=s.Symbol('t')
# On C in the chart z=1, use t=y at P=(0,0); x=-t^3+t^10+O(t^17).
xx=-t**3+t**10
basis=[(0,0),(1,0),(0,1),(2,0),(1,1),(0,2),(3,0),(2,1),(1,2),(0,3)]
orders=[0,1,2,3,4,5,6,7,9,10]
polys=[s.Poly(s.expand(xx**i*t**j),t) for i,j in basis]
minor=s.Matrix([[q.coeff_monomial(t**order) for q in polys] for order in orders]).det()
assert minor == -1
vander=math.prod(orders[j]-orders[i] for i in range(10) for j in range(i+1,10))
# At P, the Hamiltonian derivation delta=f_y d/dx-f_x d/dy is -d/dt,
# and sum(0..9)=45 is odd. Hence W_delta leading term is +vander*t^2.
coefficient=-minor*vander
assert coefficient == 82572006251298816000000
# Phi6^2*Phi21*(3*Phi14^3+21962*Phi6^7) begins with 3*t^2.
assert coefficient % 3==0
c=coefficient//3
assert c == 27524002083766272000000
assert s.factorint(c)=={2:30,3:14,5:6,7:3}
assert s.factorint(21962)=={2:1,79:1,139:1}
assert s.factorint(21962+3*1728)=={2:1,7:2,277:1}
assert all(2*24+84+168==300 for _ in [0])
assert 2*24+84+3*56==300
assert 2*24+3*84==300
print('leading_minor',minor,'Hamiltonian_leading_coefficient',coefficient,'unit',c)
print('collision_prime_sets',{79,139},{277})
print('VERIFY_LEADING_AND_COLLISIONS_OK')
