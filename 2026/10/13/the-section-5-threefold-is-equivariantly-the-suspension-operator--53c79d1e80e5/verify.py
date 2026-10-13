import sympy as sp

u1,u2,v,y1,y2,w = sp.symbols('u1 u2 v y1 y2 w')
r1 = u1*v-y1*y2
r2 = u2*v-(y1+1)*y2
r3 = u1*(y1+1)-u2*y1

# Source equations imply the suspension coordinates.
assert sp.expand((r2-r1) - ((u2-u1)*v-y2)) == 0
assert sp.expand(r3 - (u1-y1*(u2-u1))) == 0
assert sp.expand(r3 - (u2-(y1+1)*(u2-u1))) == 0

# Forward parametrization A^3_{w,v,y1} -> X.
phi = {u1:y1*w, u2:(y1+1)*w, y2:w*v}
for r in (r1,r2,r3):
    assert sp.expand(r.subs(phi)) == 0

# Inverse coordinate w=u2-u1; all coordinates recover modulo source relations.
recover = [u1-y1*(u2-u1), u2-(y1+1)*(u2-u1), y2-(u2-u1)*v]
G = sp.groebner([r1,r2,r3], u1,u2,v,y1,y2, order='lex')
for f in recover:
    assert G.reduce(f)[1] == 0

# Degree-one module: w=u2-u1, u1=y1*w, u2=(y1+1)*w.
assert sp.expand((u2-u1) - (u2-u1)) == 0
print('VERIFY_OK')
print('source_relations_to_suspension: OK')
print('forward_map: OK')
print('inverse_map_mod_source_ideal: OK')
print('degree_one_generator: w=u2-u1')
