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

The analytical proof uses explicit Fourier eigenvalues, a cyclotomic trace-and-norm lemma excluding all other interbranch collisions, and exact squared-multiplicity accounting. The supporting executable checks the formula for 598 lengths by two-branch enumeration and for 48 lengths by independent direct adjacency diagonalization. Run `python prism_checker.py` after installing `numpy>=1.20`.

Numerical diagonalization groups eigenvalues within a tolerance and therefore is not an infinite-size proof. The source comparison is limited to the identifiable literature listed in RESULT.md. Neither the multiplicity checker nor the historical search constitutes independent mathematical certification.
