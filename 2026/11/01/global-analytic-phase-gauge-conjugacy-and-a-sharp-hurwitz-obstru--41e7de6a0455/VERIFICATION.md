---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

Directly from w_dot=[mu Q(R,z)+i(1+eS(R,z))]w and z_dot=-S with Q=(R-5)(20/21-R)-400z²/21, S=z+R/10, the entire-space real-analytic rotation W=e^(iez)w differentiates to W_dot=(mu Q+i)W, so H_e conjugates e to 0 at every point including the axis. Its inverse is H_-e and Jacobian determinant 1. The radial ODE R_dot=2mu RQ bounds R by max(R0,5) forward; variation of constants bounds z, proving forward completeness. The Cartesian Jacobian at (1,0,-1/10) has characteristic polynomial lambda³+(1-166mu/21)lambda²+(1+e/5-50mu/7)lambda+1, confirmed independently by symbolic differentiation and exact symbolic conjugacy. Cubic Routh–Hurwitz a1>0,a2>0,a1a2>1 yields exactly 0<mu<21/166, e>250mu/7+830mu/(21-166mu); e=0 is never locally Hurwitz there. Angle derivative theta_dot+e z_dot=1 gives global asymptotic phase theta+e(z+2/5) on the actual basin of R=4,z=-2/5. Existence of an open globally Hurwitz parameter region is cited to Castañeda–Rebollo-Perdomo, not independently reproved, and the pointwise bound is not claimed globally sufficient.

## originality

PASS

Comparison across equivalence, broader coverage, exact results and claimed implication finds no decisive existing result that covers the final scoped theorem in accessible inspected material; precise covered ingredients and full-text access risks are explicitly recorded. This is a best-knowledge scientific judgment, not an attestation of independence or a guarantee of historical priority.

## value

PASS

The exact analytic volume-preserving time-preserving gauge shows that an angular parameter controlling global Jacobian-Hurwitzness is dynamically redundant in a natural 2026 counterexample to naive global-Hurwitz dynamics; a single rational-point Hurwitz cutoff and explicit entire-basin isochrons quantify this contradiction between coordinate-dependent Jacobians and invariant orbit dynamics. Although short algebra once the model is known, the connection and sharp constraint are directly motivated by its defining problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
