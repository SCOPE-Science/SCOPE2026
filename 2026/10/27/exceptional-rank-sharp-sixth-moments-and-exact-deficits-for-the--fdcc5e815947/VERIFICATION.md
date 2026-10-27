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

# Reproducibility and scientific limits

Run `python3 check.py` with Python 3.9 or later and no additional packages. The expected terminal text is given verbatim in `check_output.txt`. The replay obtained 27,695 passing assertions. The script computes relevant total-order-six Haar moments via integer Schur--Weyl multiplicities, and independently uses the special-unitary Weyl-denominator torus constant term for selected exceptional ranks. It checks the exact polynomial, sharp constants, equality witnesses and nonnegative global deficits over 25 by 25 Gaussian-integer coefficient pairs for each rank from 3 through 13.

These finite tests are not an exhaustive search over all complex coefficients or all integers N. The unlimited theorem follows from the highest-weight equivalence and character orthogonality lemma, the complete sixth-degree moment classification, and the exact nonnegative deficit identities proved in `RESULT.md`. The independent torus computations check arithmetic by a different mathematical route but are not an independent external scientific audit.
