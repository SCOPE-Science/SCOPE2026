---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For compact invariant μ of xdot=−σx+ζz+αyz, ydot=ρ−y−xz, zdot=−z+xy (all four parameters positive), test generators on arbitrary C¹ antiderivatives of one-coordinate continuous functions. This proves all three conditional regressions. Independently checked exact polynomial cancellation L(y²+z²)=2ρy−2y²−2z² with SymPy and inspected pinned verify.py, yielding E[(y−ρ/2)²+z²]=ρ²/4 and Var(y)+E[z²]=m(ρ−m). m=0 contradicts invariant support since ydot=ρ on {y=z=0}; m=ρ forces δ_(0,ρ,0). For R=xy−z=zdot, E[R|z]=0 implies orthogonality, Var(xy)=Var(z)+E[R²], Cov(z,xy)=Var(z). Zero defect implies z constant on invariant trajectories, and by Poincaré recurrence every μ-typical such orbit reduces to equilibrium: when z≠0, x solves scalar autonomous xdot=−σx+ζz+α z²/x; when z=0, ydot=ρ−y on x=0. Therefore non-equilibrium-supported μ has positive Var(z) and E[R²], and Corr(z,xy)=1/sqrt(1+E[R²]/Var(z))∈(0,1).

## originality

PASS

Current and historic same-system papers inspected by accessible statements concern absorbing sets, homoclinics, self-excited/hidden attractors, Lyapunov dimension, and global dynamics; these do not yield the all-invariant-measure fiberwise conditional expectations or exact height–speed variance decomposition. Exact generator calculations are classical in method, but the combined source-specific invariant-measure calibration and equality classification were not located as a statement or an implication of checked sources.

## value

PASS

A natural calibrated invariant-statistics law in a classical physical convection model, with a rigid parameter-only second-moment circle and measurable speed/coherence defect for any stationary regime; distinguishes equilibria from all genuine recurrent nonequilibrium measures. It is not claimed as an attractor-existence theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
