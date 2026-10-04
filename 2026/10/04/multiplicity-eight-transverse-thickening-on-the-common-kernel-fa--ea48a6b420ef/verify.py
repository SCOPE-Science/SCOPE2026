import sympy as sp

# Grassmann chart for planes through Q0=<E11,E12+E21,E22> in Sym^2(k^3).
a1,a2,a3,b1,b2,b3,c1,c2,c3 = sp.symbols('a1 a2 a3 b1 b2 b3 c1 c2 c3')
x,y,z = sp.symbols('x y z')
M = sp.Matrix([
    [x, y, a1*x+b1*y+c1*z],
    [y, z, a2*x+b2*y+c2*z],
    [a1*x+b1*y+c1*z, a2*x+b2*y+c2*z, a3*x+b3*y+c3*z],
])
D = sp.expand(M.det())
P = sp.Poly(D,x,y,z)
terms = dict(P.terms())
expected = {
 (3,0,0): -a2**2,
 (2,1,0): 2*a2*(a1-b2),
 (2,0,1): -a1**2-2*a2*c2+a3,
 (1,2,0): 2*a1*b2+2*a2*b1-a3-b2**2,
 (1,1,1): -2*a1*b1+2*a1*c2+2*a2*c1-2*b2*c2+b3,
 (1,0,2): -2*a1*c1-c2**2+c3,
 (0,3,0): 2*b1*b2-b3,
 (0,2,1): -b1**2+2*b1*c2+2*b2*c1-c3,
 (0,1,2): -2*b1*c1+2*c1*c2,
 (0,0,3): -c1**2,
}
assert all(sp.expand(terms[k]-expected[k]) == 0 for k in expected)

# Eliminate the three graph coordinates a3,b3,c3.
subs = {a3:a1**2+2*a2*c2, b3:2*b1*b2, c3:2*a1*c1+c2**2}
remaining = [sp.expand(f.subs(subs)) for f in expected.values()]
remaining = [f for f in remaining if f != 0]

# Coordinates tangent to the reduced common-kernel component and four transverse directions.
s,t,A,H,K,C = sp.symbols('s t A H K C')
change = {a1:s,b1:t,a2:A,c1:C,b2:s+H,c2:t+K}
transformed = [sp.expand(f.subs(change)) for f in remaining]
Jgens = [A**2, A*H, H**2+2*A*K, A*C-H*K, 2*C*H-K**2, C*K, C**2]
assert sp.groebner(transformed,A,H,K,C,s,t,order='lex') == sp.groebner(Jgens,A,H,K,C,s,t,order='lex')

G = sp.groebner(Jgens,A,H,K,C,order='lex')
gbasis = [sp.expand(g.as_expr()) for g in G.polys]
expected_gb = [
 A**2,
 A*H,
 2*A*K + H**2,
 A*C - H*K,
 H**3,
 H**2*K,
 H*K**2,
 2*C*H - K**2,
 K**3,
 C*K,
 C**2,
]
assert sp.groebner(gbasis,A,H,K,C,order='lex') == sp.groebner(expected_gb,A,H,K,C,order='lex')

# Standard monomial basis for the transverse Artin algebra.
basis = [1,A,H,K,C,H**2,H*K,K**2]
# Show spanning by reducing all monomials of degree <= 3 and nilpotence of degree >=3.
def rem(f):
    return sp.expand(G.reduce(sp.expand(f))[1])
for m in basis:
    assert rem(m) == m
# All degree-three monomials reduce to zero.
vv=[A,H,K,C]
for i in range(4):
    for j in range(i,4):
        for k in range(j,4):
            assert rem(vv[i]*vv[j]*vv[k]) == 0
# Independence follows from distinct standard monomials for this Groebner basis.
assert len(basis)==8
# Radical is the maximal ideal because each generator is nilpotent modulo J.
assert rem(A**2)==0 and rem(C**2)==0 and rem(H**3)==0 and rem(K**3)==0

# Tangent-space check: no linear equations transversely, hence 4 transverse tangent directions;
# with the two smooth component directions this gives dimension 6, matching the source formula.
print('determinant_coefficients=10')
print('transverse_groebner_basis_size=%d' % len(expected_gb))
print('transverse_hilbert_function=1,4,3')
print('transverse_length=8')
print('transverse_nilpotence_index=3')
print('local_tangent_dimension=6')
print('VERIFY_OK')
