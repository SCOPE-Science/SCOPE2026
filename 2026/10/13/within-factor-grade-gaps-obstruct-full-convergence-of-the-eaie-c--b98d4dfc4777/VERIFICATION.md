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

Definition 4.2 adds the same increment to every positive grade of a factor, so their offsets from the top grade are exact invariants. If s_m is the separate top-grade effect and c=(H(d)-sum s_m)/n, then e_m=s_m-x_top,m. Efficiency fixes the sum of top grades, and the top-grade error relative to s_m+c is multiplied by 1-n alpha. This proves the claimed full limit and its iff compatibility criterion for 0<alpha<2/n. Subtracting the PCOMR equations at k and at d_m fixes the offset at H(d_-m,k)-H(d), not the EAIE offset. In the (2,1) witness the only nonzero grid value is H(1,1)=1. The payoff (1,0,0) satisfies all PCOMR equations and top efficiency. All separate effects and the balance term vanish; both top excesses vanish, so the correction and stopping discrepancy are identically zero at this non-EAIE point. Two factors and one lower positive grade are minimal within the stated scope. This is an exact hand reconstruction against the source definitions, not execution of the bundled verify.py or a formal certificate.

## originality

PASS

The checked prior results do not supply the invariant-based refutation of Liao's Theorem 4.5, the admissible PCOMR witness, or the exact offset criterion. Liao's valid top-grade theorem is used, not claimed as new. The previously identified EAIE covariance defect addresses a different axiom and does not refute this iteration.

## value

PASS

The obstruction refutes a published full-coordinate convergence theorem on its own hypotheses, explains why its stopping rule can accept a non-target point, and supplies the exact initialization compatibility that preserves the valid top-grade result. This is more informative than an isolated numerical counterexample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
