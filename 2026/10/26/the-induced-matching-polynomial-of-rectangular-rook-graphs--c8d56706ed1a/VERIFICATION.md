---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The symbolic proof establishes the feasible profile conditions, the exact profile coefficient, and the all-parameter maximum-size formula. The included `verify_induced_matching_polynomial.py` was executed from the package directory and checks coefficients against exhaustive independent-set enumeration for every board with \(1\le m,n\le4\). The finite check is supplemental and does not replace the proof.

Limits: no asymptotic coefficient estimates or weighted extension are claimed. The literature comparison is best-knowledge; independent audit and external validation remain unperformed.

The trusted importer initializes absent external channels as unperformed; research never assesses/authors them or resets old evidence.
