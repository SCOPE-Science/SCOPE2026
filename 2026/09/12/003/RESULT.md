# The interface Robin gap is false: exact hemisphere buckling witness at v=1/6

## Context

Work in the round 3-sphere S^3(1). Consider the symmetric spherical double
bubble with per-bubble volume fraction v, the two bubbles congruent by the
reflection x4 -> -x4. Freeze the outer caps to first order and consider the
separating interface disk D_v with Jacobi operator J = -Delta_D - (|A_D|^2+2)
and linearized triple-junction Robin condition partial_nu u + q u = 0 with
canonically computed q. The admitted target claims mu_1(D_v) >= 1/8 uniformly
for v in [0.05, 0.30]. This record disproves that eigenvalue clause within the
stated frozen-exterior reduction.

## Definitions

- Interface: D(rho) = geodesic disk of radius rho in the great S^2 {x4=0},
  D(rho) = {x3 >= cos rho}, junction circle C(rho) = {x3 = cos rho, x4=0}.
- Outer cap spheres: centers m_pm = (0,0,a,+-b), spherical radius R_s, with
  a^2+b^2 = 1. Circle-on-sphere plus 120-degree stationarity give
  cos^2 R_s = 3 cos^2 rho / (4 - cos^2 rho), b = sin R_s / 2,
  a = sqrt(1-b^2), a cos rho = cos R_s.
- Trial: u = x3 - c0 on D with c0 = cos rho; smooth, H^1, zero trace on the
  boundary circle. Robin boundary term int_{partial D} q u^2 vanishes exactly
  for every finite q.
- Exact disk moments: A = 2pi(1-c0), M1 = pi(1-c0^2), M2 = 2pi(1-c0^3)/3,
  G = A - M2, Dm = M2 - 2 c0 M1 + c0^2 A, Q = (G - 2 Dm)/Dm.
- Bubble 1: Omega_1 = {p . m_+ <= cos R_s} cap {x4 >= 0}; volume fraction
  f = V(Omega_1)/(2 pi^2).

## Result

At rho = pi/2 (c0 = 0), D is the hemisphere {x3 >= 0} in the great S^2,
u = x3 has zero trace on the junction circle, and Q[u] = 0 exactly
(G = 4pi/3, Dm = 2pi/3). Hence mu_1(D_{1/6}) <= 0 < 1/8 with margin 1/8.
At the same point f = 1/6 exactly, inside [0.05, 0.30]. Therefore the uniform
gap mu_1 >= 1/8 is false. Two further in-window violations: Q = 0.108 at
rho = 88 deg (f = 0.1764) and Q = 0.053 at rho = 89 deg (f = 0.1715).

## Proof / evidence

Totally geodesic interface: |A_D| = 0, so J = -Delta - 2 exactly. On the
hemisphere u = x3 satisfies -Delta x3 = 2 x3 (l=1 spherical harmonic), so
J u = 0 in the interior; zero Dirichlet trace kills the Robin term for any
finite q, giving mu_1 <= Q = 0 by the variational principle.

Volume: fiber-circle proof. Fix (x1,x2) with R = sqrt(1-x1^2-x2^2) > 0 a.e.;
fiber circle (x3,x4) = R(cos s, sin s) carries dV_{S^3} = ds dx1 dx2 (Gram
determinant exactly 1, verified symbolically). Conditions sin s >= 0 and
cos(s - pi/6) <= 0 give s in [2pi/3, pi], width pi/3 out of 2pi: fraction 1/6
of every fiber. Hence V = pi^2/3, f = 1/6 exactly.

Junction: residual |a cos rho - cos R_s| < 1e-9 on 0 < rho <= pi/2 and the
three consistently-oriented unit normals at the junction point are pairwise
at 120 degrees (all dots -1/2); for rho > pi/2 the residual is O(0.3), so the
symmetric branch ends at the hemisphere. At the witness rho = R_s = pi/2:
a = sqrt(3)/2, b = 1/2.

Replay: python3 output/artifacts/verify_target.py (stdlib only) exits 0 and
prints DISPROOF_WITNESS_CONFIRMED / VERIFY_OK.

## Limitations

The disproof operates within the target frozen-exterior reduction and refutes
the eigenvalue clause mu_1 >= 1/8; the lift to a full volume-constrained
cluster instability (outer-cap compensators with junction remainder ledger)
is documented as the next step and is not claimed here.

## Reproducibility

Run python3 output/artifacts/verify_target.py from the record root. It checks
junction residuals, 120-degree dots, wedge = 1/2, f(pi/2) = 1/6, Q = 0, and
window membership. Exact identities above are hand-checkable; quadrature in
the script is corroboration only.

## References

- Emanuel Milman, Multi-Bubble Isoperimetric Problems, arXiv:2510.07078
  (spectral program announcement, no explicit interface eigenvalue).
- Batista-Cavalcante-Melo, First Eigenvalue of Jacobi Operator and Rigidity
  Results, arXiv:2405.18233 (closed/free-boundary Jacobi bounds, distinct
  operator and boundary conditions).
- Pinsky-type spherical-cap Laplacian bounds and Freitas-Mao-Salavessa
  geodesic-disk symmetrization (Laplacian only, no Jacobi potential or
  junction Robin coefficient).
- Hutchings et al., Proof of the Double Bubble Conjecture (R^3 area
  minimization, distinct problem).
