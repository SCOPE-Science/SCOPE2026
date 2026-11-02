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

Finite check: run `python checker.py` with the Python standard library. The checker performs rational-sign comparisons in dimensions \(2\) through \(16\), cross-alphabet spectral checks, and direct small-matrix Fourier eigenvector calculations, reporting `FINITE CHECKS PASS 2074`. It verifies finite identities only; the proof for all dimensions and alphabets uses the inequalities in RESULT.md.

The first root is defined by an exact polynomial, not by a rounded numerical constant. The asymptotic error is a proved order term; it is not an exhaustive interval certificate. The theorem does not classify possible further transitions away from the first-loss bracket.
