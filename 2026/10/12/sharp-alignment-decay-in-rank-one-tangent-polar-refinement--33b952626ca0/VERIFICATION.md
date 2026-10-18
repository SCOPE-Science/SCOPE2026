---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

On real 2x2 rank-one tangent plane T_W at W=e1e1^T, P_T deletes bottom-right entry. For a,b>0, g=[[a,b],[b,0]] is invertible symmetric indefinite and polar(g) is its sign matrix [[a,2b],[2b,-a]]/sqrt(a²+4b²). Iteration yields X_t=[[a,2^t b],[2^t b,0]]/sqrt(a²+4^t b²), all t≥1; the exact nuclear norm of g is sqrt(a²+4b²). Differentiation of the alignment in k=2^t proves strict decrease after t=1; factoring d/dy of squared alignment gives (k-2)^2(2ky-1)(2ky+1)/((1+k²y)^2(1+4y)^2), so the global minimum over y=b²/a²>0 at y=1/(2k) is 8k/(k+2)^2, with sharp alignment 2sqrt(2k)/(k+2). Independently factored derivative with symbolic algebra and evaluated fresh exact rational and polar examples; t=3 is 4/5 and t=5 is 8/17. The t=1 boundary is exactly 1. No spectral-norm feasibility or optimizer convergence failure is asserted.

## originality

PASS

No inspected prior result proved the exact submitted mathematical conclusion; comparisons evaluate statements and implications rather than titles, with bounded source-access and bibliographic uncertainties retained.

## value

PASS

A directly motivated extremal limitation of the actual raw alternating tangent-polar update: more inner steps can strictly degrade descent correlation, and the sharp worst-case bound decays to zero with horizon, explaining the pre-existing safeguard. The theorem quantifies a nontrivial canonical low-rank geometry and exact practical iteration horizons without claiming a full algorithm divergence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
