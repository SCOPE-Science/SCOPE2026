import sympy as sp

g = sp.symbols('g0:6')
d = sp.symbols('d0:6')
g0,g1,g2,g3,g4,g5 = g
d0,d1,d2,d3,d4,d5 = d

qg = sp.Matrix([
    g4**2 - 4*g3*g5,
    g2*g4 - 2*g1*g5,
    g2**2 - 4*g0*g5,
])
qd = sp.Matrix([
    d2**2 - 4*d0*d5,
    d1*d2 - 2*d0*d4,
    d1**2 - 4*d0*d3,
])
F = sp.Matrix([
    qg[0]*qd[1] - qg[1]*qd[0],
    qg[0]*qd[2] - qg[2]*qd[0],
    qg[1]*qd[2] - qg[2]*qd[1],
])
vars = list(g)+list(d)
J = F.jacobian(vars)

# The reducible-conic epipolar plane P_gamma: g2=g4=g5=0.
Pgamma = {g2:0, g4:0, g5:0}
assert all(sp.expand(f.subs(Pgamma)) == 0 for f in F)
JP = J.subs(Pgamma)
# Only the g5-column may survive, hence rank <= 1 everywhere on P_gamma x P^5.
nonzero_cols = [j for j in range(JP.cols) if any(sp.expand(JP[i,j]) != 0 for i in range(JP.rows))]
assert nonzero_cols == [5], nonzero_cols

# Symmetric epipolar plane P_delta: d0=d1=d2=0.
Pdelta = {d0:0, d1:0, d2:0}
assert all(sp.expand(f.subs(Pdelta)) == 0 for f in F)
JD = J.subs(Pdelta)
nonzero_cols_delta = [j for j in range(JD.cols) if any(sp.expand(JD[i,j]) != 0 for i in range(JD.rows))]
assert nonzero_cols_delta == [6], nonzero_cols_delta

# Explicit singular point on P_gamma x P^5 with Jacobian rank 1.
sing = {g0:1,g1:0,g2:0,g3:1,g4:0,g5:0,
        d0:1,d1:0,d2:0,d3:0,d4:0,d5:1}
assert all(sp.expand(f.subs(sing)) == 0 for f in F)
assert J.subs(sing).rank() == 1

# A general double-line point of the zero-row locus is smooth on the codimension-2 variety.
# gamma=(u^2,2uv,2uw,v^2,2vw,w^2) with (u,v,w)=(1,1,1).
smooth = {g0:1,g1:2,g2:2,g3:1,g4:2,g5:1,
          d0:1,d1:0,d2:0,d3:0,d4:0,d5:1}
assert all(sp.expand(f.subs(smooth)) == 0 for f in F)
assert J.subs(smooth).rank() == 2

# At the double-line point, the differential of q_gamma is surjective (affine rank 3).
Jqg = qg.jacobian(g)
assert Jqg.subs({g0:1,g1:2,g2:2,g3:1,g4:2,g5:1}).rank() == 3

print('VERIFY_OK')
print('singular_rank=1')
print('double_line_rank=2')
print('Pgamma_nonzero_jacobian_columns=', nonzero_cols)
print('Pdelta_nonzero_jacobian_columns=', nonzero_cols_delta)
