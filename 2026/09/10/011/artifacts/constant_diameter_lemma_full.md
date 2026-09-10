# Constant-diameter lemma — full auditable proof (target premise test)

## Statement
Let X = S^2(1), Y_a = S^1_a (metric circle, length a), a in (0,2pi].
Let J_a = X *_s Y_a be the metric spherical join with distance defined by
  cos d(p1,p2) = cos t1 cos t2 cos d_X(x1,x2) + sin t1 sin t2 cos d_Y(y1,y2),
t_i in [0,pi/2] (AKP Foundations § join; Rong–Wang §2; BGP join construction).
Then diam(J_a) = pi for every a. In particular there is no a_c in (0,2pi)
with diam(J_a) = pi/2, and f(a) := diam(J_a) is constant (hence continuous
but not strictly monotone).

## Proof
H1: diam(X) = pi; diam(Y_a) = a/2 <= pi (half-circumference; a<=2pi).
  So all comparison distances lie in [0,pi] where cos is strictly decreasing;
  the arccos formula defines a genuine metric (cited join theorem), and J_a is
  compact Alexandrov, curv>=1, dim 4.

Lower bound diam >= pi:
  Take p1=(x1,·,0), p2=(x2,·,0) with d_X(x1,x2)=pi (antipodes exist in S^2).
  t1=t2=0: cos d = 1·1·cos(pi)+0 = -1, so d(p1,p2)=pi. Hence diam(J_a)>=pi.
  This uses only the t=0 slice, where the formula reduces exactly to d_X
  (factor isometry; verified with err 0.0 in check_factor_isometry.py).

Upper bound diam <= pi:
  For any pair: cos t_i, sin t_i >= 0 on [0,pi/2]; cos d_X, cos d_Y >= -1.
  Hence cos d(p1,p2) >= -cos t1 cos t2 - sin t1 sin t2 = -cos(t1-t2) >= -1.
  So d(p1,p2) = acos(·) <= pi. Hence diam(J_a) <= pi.
  (Grid sweep in check_join_diameter.py confirms max <= pi + 1e-9.)

Combine: diam(J_a) = pi identically. The equation diam = pi/2 has no solution
in (0,2pi]; continuity holds trivially, strict monotonicity fails everywhere
(f constant). The target's "existence and uniqueness by continuity and strict
monotonicity" step is therefore false for the stated object. ∎

## Why no re-interpretation rescues a_c within the admitted statement
- "Circle of length a": diam(Y_a)=a/2 standard; any other normalization (radius
  a, curvature-scaled) is not in the admitted problem statement.
- Join theorem hypothesis diam<=pi holds for all a in (0,2pi]; no rescaling needed.
- Radius r(a) does vary (pi/2 for a<=pi, >pi/2 after; eccentricity lemma), but
  the target pins a_c by DIAMETER, which is the constant functional. Substituting
  radius would change the theorem (different constant origin: Grove–Petersen
  rad>pi/2 vs Grove–Shiohama diam>pi/2) and is not attempted as it would be a
  different claim.
- Volume vol(J_a)=4pi·a/3 varies, but the target pins by diameter, not volume.

## Audit-plan mapping
- Item (1) join setup: confirmed (closed 4-space curv>=1, S^2 edge for a<2pi).
- Item (2) a_c well-defined: REFUTED by this lemma.
- Items (3)–(5) therefore test a conditional with unsatisfiable hypothesis;
  their audits (rigidity_route_audit.md, phi_estimate_derivation.md,
  gh_stability_note.md) show additionally that neither branch route would
  produce a diameter threshold even conditionally.

## Replay
python3 output/artifacts/check_join_diameter.py      # antipodal pi, grid max<=pi
python3 output/artifacts/check_factor_isometry.py    # exact factor isometry
python3 output/artifacts/check_link_volume.py        # vol(Sigma_p)=pi·a
python3 output/artifacts/check_volume_collapse.py    # vol(J_a)=4pi·a/3
python3 output/artifacts/check_radius_and_topology.py# ecc table, radius kink
