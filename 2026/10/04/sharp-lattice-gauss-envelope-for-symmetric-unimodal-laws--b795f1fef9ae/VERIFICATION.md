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

The centered-discrete-uniform mixture representation is exact. Variance and the threshold tail are linear in its weights, so the problem is the upper concave hull of (V_k,T_k). Direct algebra shows the origin slope is maximized at the displayed kappa_a, while all subsequent adjacent slopes are strictly decreasing and begin below the contact slope. This proves the complete hull and equality mixtures. The scaling limit follows from kappa_a/a->3/2 and V_k~k^2/3.

## originality

PASS

Best-of-knowledge originality passes. Huber's full arXiv text proves a discrete unimodal two-sided bound but explicitly states it is not tight; the classical and modern sharp Gauss results are continuous. No checked source gives the exact arithmetic upper hull, breakpoint index, or centered-discrete-uniform equality mixtures.

## value

PASS

This is a sharp lattice analogue of a foundational Gauss concentration inequality, with a genuinely arithmetic breakpoint and exact equality laws. Huber explicitly leaves the discrete bound non-tight, so resolving the exact symmetric subclass is a motivated quantitative gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
