---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Set t=br, u=y/x and A=b−1−bd. On the given parameter surface the ratio equation factors as u′=u(1−tu)(x+A/(1+u)). Thus u=1/t is invariant; in fact the coefficient of x forces this slope for any invariant positive ray. The restricted equation is x′=x(κ−x); κ>0 gives forward convergence at every x>0 on the ray. The linearization in (x,u) is triangular, with entries −κ and −κ−tA/(1+t)=b[d+r−2br(1−d)]/(1+t). When the latter is positive, local stable manifold uniqueness and backward uniqueness of a trajectory that eventually enters that local manifold exclude all off-ray initial points in the quadrant. I independently solved the two nullclines using w=x/(x+y), checked the printed inequalities at the rational witness, and obtained eigenvalues −9/1100 and 18/275 at E1 and trace −963171/7896100 and determinant 1260441/98701250 at the stated E2. Thus the local-attraction sign is verified directly from the vector field. Bounded exact arithmetic: independent_checks.py 1. No conclusion about an entire attraction-basin boundary or cases with κ≤0 or zero transverse eigenvalue.

## originality

PASS

The supported distinction is the exact parameter surface and straight stable manifold with its scalar dynamics for this specific autonomous field, not the existence of a stable manifold or bistability in ratio-dependent models. No tested available result covers that distinction; full-text priority in the older same-family papers remains unresolved.

## value

PASS

The coexistence saddle's stable set is a natural geometric object organizing trajectories in the two-equilibrium regime. The ray formula gives its exact location and time parametrization and a realizable benchmark within that regime, not merely the equilibrium coordinates or a plot. The codimension-one restriction is the precise condition that enables straightness and is not an arbitrary numerical choice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
