---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Let Z_i be the clean-window indicators. Then W_b=n-sum_i Z_i, E Z_i=r^b, and for offset d the joint clean event is exactly avoidance on the union of two cyclic length-b windows. Direct set counting gives union size u_0=b and u_d=2b-max(0,b-d)-max(0,b-(n-d)); therefore E[Z_i Z_{i+d}]=r^{u_d} and the stated covariance sum follows by cyclic translation invariance. The n>=2b reduction leaves paired overlap offsets d=1,...,b-1 with union size b+d and zero covariance for disjoint offsets. Boundary cases p=0, p=1, b=1 and b=n are consistent. An independent exact rational replay over all binary support patterns for small n reproduced both moments; it was used only as a check on the analytic proof.

## originality

PASS

Best-of-knowledge originality passes. The foundational full text defines the exact cyclic b-read metric and develops deterministic MDS bounds; Vega's open full text gives b-weight enumerators for structured semiprimitive cyclic codes. Neither supplies the iid Bernoulli support law or the all-parameter first and second moments. The closest sphere-bound paper was only abstract-accessible, so it is retained as a named residual risk rather than treated as noncoverage.

## value

PASS

The random b-symbol corruption count is the channel's direct stochastic distortion under the standard iid substitution model. Overlapping reads create dependence even when coordinates are independent, so the exact variance and its stable linear-in-n regime quantify a natural channel fluctuation scale rather than an arbitrary finite statistic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
