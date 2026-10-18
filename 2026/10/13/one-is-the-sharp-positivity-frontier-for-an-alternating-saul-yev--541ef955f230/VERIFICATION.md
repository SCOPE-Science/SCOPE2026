---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

With beta=r/(1+r), gamma=(1-r)/(1+r), the left and right recurrence matrices have nonnegative coefficients if 0<=r<=1; forward and reverse induction then prove P_n=RL>=0 for every n. For n>=2, apply the two sweeps to e1: after left sweep v_j=beta^(j-1)gamma. The final component after right sweep is w_n=beta v_(n-1)+gamma v_n=beta^(n-1)gamma(1+gamma)=2r^(n-1)(1-r)/(1+r)^(n+1), strictly negative for r>1. At n=1 the product is gamma^2≥0 for all r>=0. For n=2,r=2 the entry is -4/27, a sharp minimal witness. Independently implemented both sweeps with rational fractions and checked the exact corner for n=2..9 at r=1/2,1,6/5,2,9/2; these bounded checks corroborate, not establish, the full all-n proof. Precisely full-step historical alternation, uniform 1D grid, Dirichlet zeros and constant D.

## originality

PASS

Chin gives the classical directional Saulyev coefficients, unconditional Fourier stability and recommended alternation, and notes gamma may turn negative. The inspected full treatment does not claim the completed-two-sweep entrywise positivity iff r<=1, exceptional n=1, or universal explicit negative corner. Campbell and Yin 2007 analyze directional alternating stability but accessible abstract is insufficient for a whole-document noncoverage judgment. Distinguishes monotonicity from stability; residual older discrete maximum-principle priority risk noted.

## value

PASS

A positivity threshold determines whether physically nonnegative diffusion states remain componentwise nonnegative after a complete explicit alternating update despite unconditional von Neumann stability. Exact necessity for all n>=2, a minimal-size witness, and a one-node exception identify a real numerical-PDE scheme boundary rather than a trivial sign of a single sweep.

The dated certificate retains the supplied scientific assessment, sources and limitations.
