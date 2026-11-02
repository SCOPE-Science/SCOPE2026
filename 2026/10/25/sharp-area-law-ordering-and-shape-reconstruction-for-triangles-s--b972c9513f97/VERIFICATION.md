---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For independent edge choices of weights p_i the three occupancy cases are exhaustive and disjoint, and their probabilities sum exactly to one. Conditional on two edge samples, the determinant has |U-V| times independent uniform opposite-edge height; conditional on three distinct sides it is R=UVW+(1-U)(1-V)(1-W). The displayed conditional coupling replaces U by 1-U, giving R in law as min((1-U)V,U(1-V))+|U-V|W and strictly greater tail at every t in (0,1). Differentiating 3(e2-3e3)A+6e3B along a two-coordinate equalization gives -3(p_i-p_j)^2[A(1-p_k)+2p_k(B-A)]<0, so majorization and both sharp envelopes follow, with triangle constraint 0<p_i<1/2 and unattained lower degeneracy. Beta integrals yield m1=e2/2,m2=e2/6,m3=3e2/40-e3/60; cubic x^3-x^2+e2 x-e3 has the unordered normalized side lengths as roots. Independently recomputed the first four component moments and exact mixture, inversion, and atom identities for multiple rational side vectors; no finite experiment substitutes for the analytic all-triangles conclusion.

## originality

PASS

Maesumi gives the full one-sample-per-side universal area law R, including its density/CDF and moments; that component is explicitly prior. It does not imply that three independently placed points sampled by *total arclength* obey a mixture with shape-dependent edge occupancy, strict Schur ordering across all thresholds, or 2-moment reconstruction. Published random-circle extreme polygon and uncertain finite-hull results have different domains. Published Resultary semantic matches on triangle sampling/area and geometric inverse statistics were checked for stronger implication; none located that settles this all-boundary theorem. This is best-of-knowledge originality, not a certification of absolute priority.

## value

PASS

The entire-perimeter arclength measure is intrinsic to triangle geometry and differs materially from a forced-one-point-per-side law. The exact distribution yields the globally sharp stochastic shape extremum and an inverse similarity theorem from only two specific area statistics, while showing why the first two moments fail. Researchers can use either the conditional law, the all-threshold comparison, or the explicit shape inversion as natural exact facts, rather than an arbitrary finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
