---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Direct reconstruction from rho_1=diag(p,1-p), rho_2=I/2, Pi_1=diag(q,1-q) yields s=1-p-q+2pq and log likelihood log(s)+(log p+log(1-p))/2 plus constants. At p=q=1/2, s=1/2, s_p=s_q=0, s_pq=2, so log(s) has mixed curvature 4, q curvature 0; calibration p curvature -4. Determinant -16 is strictly negative, proving indefinite curvature in an interior feasible convex slice. The fixed calibration probabilities are positive; POVM positivity and completeness hold. Independently recomputed exact Hessian; direct Git RESULT.md and artifacts/verify.py inspected. The negative conclusion applies to joint curvature, not all possible convergence arguments.

## originality

PASS

A specific two-dimensional physically feasible counterexample targets the assertion in Jezek's original simultaneous-optimization protocol; fixed-measurement state tomography and measurement-only SDP optimize one factor and cannot rescue joint concavity. Basic bilinearity is known; the source-specific false implication and exact calibration-inclusive counterexample appear new in the inspected literature, subject to priority risk.

## value

PASS

A published inference scheme invokes convexity for a global optimum guarantee; exhibiting a valid, easily reproducible counterexample changes how the method may be certified. Although the Hessian is small, it addresses a substantive structural justification, not arbitrary normalization or a trivial one-off calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
