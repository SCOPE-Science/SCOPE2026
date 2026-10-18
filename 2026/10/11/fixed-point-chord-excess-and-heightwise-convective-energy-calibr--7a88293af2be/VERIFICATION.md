---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

Variation of constants for zdot+z=y² on any bounded complete orbit gives z(t)=∫_0^∞e^(−s)y(t−s)²ds, strictly positive except the identically zero orbit (uniqueness). For compact invariant μ of xdot=−a x+b y−y z, ydot=x, zdot=y²−z, primitive tests give E[x|y]=0, E[y²|z]=z, E[y(b−z)|x]=a x. With m=Ez, stationarity of xy yields 0=E[x²]−aE[xy]+bE[y²]−E[y²z]=E[x²]+bm−E[z²]; so Var(z)=m(b−m)+E[x²]. Conditional E[zdot|z]=0 gives Var(y²)=Var(z)+E[zdot²] and Cov(z,y²)=Var(z). Vanishing x² or zdot² on invariant compact support implies only equilibria (using bounded completeness and tangency). For b>0, all z≥0 on recurrent support, E[z(z−b)]=E[x²]>0 away from equilibria forces μ(z>b)>0. Correlation strict away from equilibrium mixtures. Exact rational checker inspected; finite algebra is not used as proof of conditional stationarity.

## originality

PASS

Compared exact Rucklidge vector field, not just topic labels. The 2013 Dias–Mello paper develops local Hopf and first/second Lyapunov coefficients, not invariant probability moments; the open 2021 Dong et al. treats periodic-orbit symbolic coding, return maps and z=b section. Neither contains the stationary conditional regression E[y²|z]=z, the exact chord-excess Var(z)=m(b−m)+E[x²], or its strict excursion implication. The indexed prior Rucklidge damping recurrence is credited separately, not claimed here. The memory formula is the standard stable-filter solution and is not independently novel in isolation; the unified exact invariant-statistical geometry is assessed.

## value

PASS

For the convection model, y² is convective intensity and z thermal memory. The exact stationary y²|z calibration yields a sharp nonnegative fixed-point chord lower envelope, with measurable kinetic x² and vertical speed defects, plus a topologically nontrivial recurrence barrier: every non-equilibrium stationary state must spend positive invariant mass above the nonzero-equilibrium height b. At the standard (2,6.7) parameters this is exactly the physically used Poincaré section; sharpness and equality characterization make it independently useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
