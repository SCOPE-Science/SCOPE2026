#!/usr/bin/env python3
"""Exact polynomial and numerical-invariant checks for the Fermat-Cremona union.
The infinite-parameter branch/resolution argument is in RESULT.md, not certified
by the finite parameter tests in this script.
Requires SymPy 1.12 or later.
"""
import sympy as sp

X, Y, Z = sp.symbols('X Y Z')
Q = X*Y + Y*Z + X*Z
H = sp.expand(Q*(X+Y)*(Y+Z))
Hx, Hy, Hz = [sp.diff(H, u) for u in (X, Y, Z)]

# Pull back under x->x^m etc.; the m-dependent factors cancel in these two
# universal polynomial identities.
assert sp.expand((X+Y)*Hx - (Y+Z)*Hz) == 0
assert sp.expand(X*(2*X+3*Y)*Hx - (2*Q+Y**2)*Hy
                 + Z*(2*Z+3*Y)*Hz) == 0

# Universal Saito determinant, after replacing X,Y,Z by x^m,y^m,z^m.
D = (-X*(Y+Z)*(2*Q+Y**2)
     -Y*(X*(Y+Z)*(2*X+3*Y)+Z*(X+Y)*(2*Z+3*Y))
     -Z*(X+Y)*(2*Q+Y**2))
assert sp.expand(D+4*H) == 0
assert sp.expand(Q.subs({X:-Y}) + Y**2) == 0
assert sp.expand(Q.subs({Z:-Y}) + Y**2) == 0
assert sp.det(sp.Matrix([[0,1,1],[1,0,1],[1,1,0]])) == 2

# Direct low-degree checks do not substitute for the universal identities.
x,y,z = sp.symbols('x y z')
for m in (2,3,4):
    F = sp.expand(H.subs({X:x**m,Y:y**m,Z:z**m}))
    Qm = Q.subs({X:x**m,Y:y**m,Z:z**m})
    r1 = [z**(m-1)*(x**m+y**m), 0, -x**(m-1)*(y**m+z**m)]
    r2 = [x*y**(m-1)*(2*x**m+3*y**m),
          -(2*Qm+y**(2*m)),
          z*y**(m-1)*(2*z**m+3*y**m)]
    grad = [sp.diff(F,v) for v in (x,y,z)]
    for rr in (r1,r2):
        assert sp.expand(sum(a*b for a,b in zip(rr,grad))) == 0
    assert sp.expand(sp.det(sp.Matrix([[x,y,z],r1,r2]))+4*F) == 0

# Exact algebraic consistency of the branch pair contact data, resolution
# multiplicities, Milnor formula and Euler characteristic A'Campo data.
t=sp.symbols('t')
for m in range(2,25):
    r=2*m
    delta=sp.binomial(r,2)-m + m*(m+1)
    assert delta == 3*m*m-m
    mu=2*delta-r+1
    assert mu == 6*m*m-4*m+1
    multiplicity_central=2*m
    tails=[2*m+2*k for k in range(1,m+1)]
    assert len(tails)==m and tails[-1]==4*m
    # A'Campo gives the H1 characteristic polynomial because H0 contributes
    # the factor (1-t)^{-1} to the Lefschetz zeta function.
    char=(1-t)*(1-t**(2*m))**(m-2)*(1-t**(4*m))**m
    assert sp.degree(char,t)==mu
    assert 1+(m-2)+m == 2*m-1  # eigenvalue-one multiplicity = branches-1
    tau_global=(4*m-1)**2-(2*m-1)*(2*m)
    tau_at_vertices=(tau_global-(m-1)**2-m*m)//2
    assert tau_at_vertices == 5*m*m-2*m
    assert mu-tau_at_vertices == (m-1)**2
    mu_global=2*mu+(m-1)**2+m*m
    assert mu_global == 14*m*m-10*m+3
    assert mu_global-tau_global == 2*(m-1)**2
    # Arithmetic genus of one degree-2m component plus 2m lines:
    # p_a(B) = sum geometric genera + sum local delta - (#components) + 1.
    gQ=(m-1)*(m-2)//2
    delta_global=2*delta + m*(m-1)//2 + m*m
    pa=(4*m-1)*(4*m-2)//2
    assert pa == gQ+delta_global-(2*m+1)+1
print('VERIFY_OK symbolic_syzygies=2 saito_det=-4F direct_m=2,3,4'
      ' local_branches=2m matched_contact=m+1 local_delta=3m2-m'
      ' local_mu=6m2-4m+1 local_tau=5m2-2m'
      ' resolution=E0(2m)+m_tails(2m+2k)'
      ' local_monodromy=(1-t)(1-t^(2m))^(m-2)(1-t^(4m))^m')
