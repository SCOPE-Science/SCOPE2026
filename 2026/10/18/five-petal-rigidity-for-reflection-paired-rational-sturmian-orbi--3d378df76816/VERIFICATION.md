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

# Verification
The analytic argument determines the predecessor bits for all coprime positive \(k,n\) off the half-slope boundary. The complete boundary and hypotheses are given in RESULT.md. The included `verify.py` was executed from a new independent extraction path, without source-level dependencies. It computes exact fractions and proves consistency of the six-block finite instances for 170 slope pairs with denominators \(3\le n\le23\), checking orbit cardinality, unique predecessor labeling and five discontinuities. These tests are finite diagnostics, not certificates for all integers. The infinite proof is given in RESULT.md.

Self-review was performed; independent audit and independent validation were not performed.
