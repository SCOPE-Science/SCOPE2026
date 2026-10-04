import sympy as sp
from itertools import combinations

# Coordinates of the u=(1,2,3) scroll in P^8 and family parameters.
a0,a1,b0,b1,b2,c0,c1,c2,c3,t,s,u = sp.symbols(
    'a0 a1 b0 b1 b2 c0 c1 c2 c3 t s u'
)
X = [a0,a1,b0,b1,b2,c0,c1,c2,c3]
H = [[a0,b0,b1,c0,c1,c2],
     [a1,b1,b2,c1,c2,c3]]

def minors2(M):
    return [sp.expand(M[0][i]*M[1][j]-M[0][j]*M[1][i])
            for i,j in combinations(range(len(M[0])),2)]

IS = minors2(H)

def ideal_equal(g1,g2,vars_):
    G1 = sp.groebner(g1,*vars_,order='grlex')
    G2 = sp.groebner(g2,*vars_,order='grlex')
    return (all(G1.reduce(f)[1] == 0 for f in g2) and
            all(G2.reduce(f)[1] == 0 for f in g1))

def saturate_by_t(gens):
    G = sp.groebner(gens+[1-s*t],s,t,*X,order='lex')
    return [p.as_expr() for p in G.polys if not p.as_expr().has(s)]

def intersection(g1,g2):
    G = sp.groebner([u*f for f in g1]+[(1-u)*f for f in g2],u,*X,order='lex')
    return [p.as_expr() for p in G.polys if not p.as_expr().has(u)]

# Classification of the three coefficient strata follows directly from the dense
# parameterization (a,at | b,bt,bt^2 | c,ct,ct^2,ct^3).
# We verify the standard scroll minors after eliminating the dependent block.
H23 = [[b0,b1,c0,c1,c2],[b1,b2,c1,c2,c3]]
H13 = [[a0,c0,c1,c2],[a1,c1,c2,c3]]
H12 = [[a0,b0,b1],[a1,b1,b2]]
I23,I13,I12 = map(minors2,(H23,H13,H12))
assert len(I23)==10 and len(I13)==6 and len(I12)==3

# Representative symbolic substitutions for the three line strata.
# alpha != 0: a = -2 b - 3 c, hence S(2,3).
sub23 = {a0:-2*b0-3*c0, a1:-2*b1-3*c1}
# The restricted ambient-scroll ideal is exactly the S(2,3) ideal after substitution.
restricted23 = [sp.expand(f.subs(sub23)) for f in IS]
assert ideal_equal(restricted23,I23,[b0,b1,b2,c0,c1,c2,c3])

# alpha=0, beta != 0: b = -2 c, hence S(1,3).
sub13 = {b0:-2*c0,b1:-2*c1,b2:-2*c2}
restricted13 = [sp.expand(f.subs(sub13)) for f in IS]
assert ideal_equal(restricted13,I13,[a0,a1,c0,c1,c2,c3])

# alpha=beta=0: c=0, hence S(1,2).
sub12 = {c0:0,c1:0,c2:0,c3:0}
restricted12 = [sp.expand(f.subs(sub12)) for f in IS]
assert ideal_equal(restricted12,I12,[a0,a1,b0,b1,b2])

# Adjacent degeneration 1: L_t = V(t a + b).
F1 = IS + [t*a0+b0,t*a1+b1]
Sat1 = saturate_by_t(F1)
assert ideal_equal(F1,Sat1,[t]+X)  # t-saturated closure = flat closure at t=0.
J1 = IS + [b0,b1]
K13 = [b0,b1,b2] + I13                     # actual special distortion S(1,3)
B = [a0,b0,b1,c0,c1,c2]                    # base-locus plane P^2
assert ideal_equal(J1,intersection(K13,B),X)
# Intersection S(1,3) cap B is the line with free coordinates a1,c3.
assert ideal_equal(K13+B,[a0,b0,b1,b2,c0,c1,c2],X)

# Adjacent degeneration 2: M_t = V(t b + c).
F2 = IS + [t*b0+c0,t*b1+c1,t*b2+c2]
Sat2 = saturate_by_t(F2)
assert ideal_equal(F2,Sat2,[t]+X)
J2 = IS + [c0,c1,c2]
K12 = [c0,c1,c2,c3] + I12                   # actual special distortion S(1,2)
assert ideal_equal(J2,intersection(K12,B),X)
# Intersection S(1,2) cap B is the line with free coordinates a1,b2.
assert ideal_equal(K12+B,[a0,b0,b1,c0,c1,c2,c3],X)

print('VERIFY_OK')
print('scroll_types=S(2,3),S(1,3),S(1,2)')
print('degrees=5,4,3')
print('flat_limit_1=S(1,3)_union_base_plane')
print('flat_limit_2=S(1,2)_union_base_plane')
