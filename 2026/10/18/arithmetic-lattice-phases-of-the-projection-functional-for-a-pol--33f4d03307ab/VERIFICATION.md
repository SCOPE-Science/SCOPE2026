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

# Verification record
The analytic proof in `RESULT.md` establishes all integer-indexed assertions; the finite checker is supplemental and does not certify infinite results. Run `python3 verify_frame.py` with Python 3.9 or newer, using only the standard library.

The checker recomputes the tight-frame second-moment tensor, selected fourth-moment identities, each row of the positive absolute Gram leading eigenvector, the exact trigonometric summation, and finite-index diagnostics for the second-order Bernoulli phase. The checks passed at the indices encoded in the script. Mathematical limits that are **not** experimentally proven are the complete all-index spectral radius identity and the uniform \(O(n^{-3})\) remainder; the independent analytic arguments proving them are supplied in `RESULT.md`.

No independent audit has been performed.
