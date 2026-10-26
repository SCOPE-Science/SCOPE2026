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

# Reproducibility and limits

Running `python3 verify.py` performs direct finite enumeration of weak cycle maps and separately calculates the rank formula from tridiagonal matrix walks; it checks all coefficients for \(3\le n\le9\) and boundary cases for larger \(n\). Every map in the brute-force enumeration is explicitly checked for idempotency and cyclic weak adjacency preservation. This is a finite cross-check, not an infinite proof or an independent mathematical audit.

The unrestricted polynomial follows from the arc-to-walk bijection. The cube-root concentration and total-count asymptotics follow from the eigenvalue expansion, spectral gap estimate and a global Laplace principle. All fields, hypotheses and quantifiers are specified in RESULT.md. No independent review or certification is asserted.
