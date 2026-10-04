import sympy as sp
from itertools import combinations

q = [
    sp.Matrix([1,0,0,0]),
    sp.Matrix([0,1,0,0]),
    sp.Matrix([0,0,1,0]),
    sp.Matrix([0,0,0,1]),
    sp.Matrix([1,1,1,1]),
    sp.Matrix([1,2,3,5]),
]

# The chosen world points satisfy the source paper's genericity hypothesis.
for I in combinations(range(6),4):
    assert sp.Matrix.hstack(*(q[i] for i in I)).det() != 0

Q4x6 = sp.Matrix.hstack(*q)
rels = Q4x6.nullspace()
assert len(rels) == 2

# Build the square 6-focal matrix from Definition 5 of arXiv:2309.04028.
p = []
M = sp.zeros(18,18)
for i, qi in enumerate(q):
    pv = sp.symbols(f'p{i+1}_0 p{i+1}_1 p{i+1}_2')
    p.append(pv)
    for r in range(3):
        for c in range(4):
            M[3*i+r,4*r+c] = qi[c]
        M[3*i+r,12+i] = pv[r]

F = sp.expand(M.det(method='domain-ge'))
assert F != 0
for i in range(6):
    assert sp.Poly(F, *p[i]).total_degree() == 1

# A symbolic collinear sextuple in the affine chart p_i=[1:y_i:a+b*y_i].
ys = sp.symbols('y1:7')
a, b = sp.symbols('a b')
col_sub = {}
for i in range(6):
    col_sub[p[i][0]] = 1
    col_sub[p[i][1]] = ys[i]
    col_sub[p[i][2]] = a + b*ys[i]
Mc = M.subs(col_sub)
ell = sp.Matrix([-a,-b,1])
for alpha in rels:
    w = sp.zeros(18,1)
    for i in range(6):
        for r in range(3):
            w[3*i+r] = alpha[i]*ell[r]
    assert all(sp.expand(x) == 0 for x in (w.T*Mc))

# Exact Morse-Bott witness on the collinearity locus.
zs = sp.symbols('z1:7')
aff_sub = {}
for i in range(6):
    aff_sub[p[i][0]] = 1
    aff_sub[p[i][1]] = ys[i]
    aff_sub[p[i][2]] = zs[i]
Fa = sp.expand(F.subs(aff_sub))
vars = list(ys) + list(zs)
pt = {ys[i]: i+1 for i in range(6)}
pt.update({zs[i]: 0 for i in range(6)})
point_sub = {}
for i in range(6):
    point_sub[p[i][0]] = 1
    point_sub[p[i][1]] = i+1
    point_sub[p[i][2]] = 0
Mw = M.subs(point_sub)
assert Mw.rank() == 16
assert sp.expand(Fa.subs(pt)) == 0
G = sp.Matrix([sp.diff(Fa,v) for v in vars])
assert all(sp.expand(x.subs(pt)) == 0 for x in G)
H = sp.Matrix([[sp.diff(Fa,u,v).subs(pt) for v in vars] for u in vars])
assert H.rank() == 4

# Tangent space to the collinearity locus: six independent y_i motions and two line motions.
T = sp.zeros(12,8)
for i in range(6):
    T[i,i] = 1
for i in range(6):
    T[6+i,6] = 1
    T[6+i,7] = i+1
assert T.rank() == 8
assert H*T == sp.zeros(12,8)
assert 12 - H.rank() == 8

# A nonzero exact normal Hessian minor.
normal_minor = H[6:,6:].extract((0,1,2,3),(0,1,2,3)).det()
assert normal_minor == 484

print('VERIFY_OK')
print('six_focal_terms=', len(sp.Poly(F,*sum([list(x) for x in p],[])).terms()))
print('witness_matrix_rank=', Mw.rank())
print('hessian_rank=', H.rank())
print('normal_minor_det=', normal_minor)
