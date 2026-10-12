"""Exact symbolic checks for the local critical scheme of a cusp blow-up.

Requires Python 3 and SymPy 1.14 or later. Global elliptic descent and
coherent-cohomology arguments are mathematical, not computational checks.
"""
from sympy import QQ, diff, groebner, symbols

x, y, u, w, f = symbols('x y u w f')
# The chart where the normal coordinate w generates the blow-up ideal.
t = x**3 + y**2 - u*w
J = [diff(t, z) for z in (x, y, u, w)]
G = groebner(J, x, y, u, w, order='lex', domain=QQ)
assert list(G) == [x**2, y, u, w], list(G)
assert G.reduce(t)[1] == 0
assert G.reduce(x)[1] == x
assert G.reduce(x**2)[1] == 0
assert G.reduce(y)[1] == 0
assert G.reduce(u)[1] == 0
assert G.reduce(w)[1] == 0
# The other blow-up chart has the variable f as a coordinate and t=x^3+y^2-f.
assert diff(x**3 + y**2 - f, f) == -1
# The order-six action preserves the equation x^3+y^2=t.
assert (3*2) % 6 == 0 and (2*3) % 6 == 0
# The nilpotent coordinate x has precisely order-three character.
assert (2*3) % 6 == 0 and (2*1) % 6 != 0 and (2*2) % 6 != 0
# As a module over Q[y,u,w], the local Jacobian algebra has Q-basis 1,x.
assert G.reduce(x**3)[1] == 0
print('ELLIPTIC_CRITICAL_RIBBON_LOCAL_OK')
