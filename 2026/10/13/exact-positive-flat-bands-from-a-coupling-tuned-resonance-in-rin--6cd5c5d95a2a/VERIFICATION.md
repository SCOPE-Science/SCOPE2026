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

The analytic verification uses the *un-divided* Bloch secular equation in [1, Eqs. (2.9)–(2.10), Section 4]. Its two trigonometric Bloch coefficients force \(k\) to be a strictly positive integer, and the remaining constant term then becomes an explicit perfect square times \(\sin(ml_1)\sin^2(ml_3)\). The half-angle identity supplies the coupling branch. The positive-measure direct-integral criterion identifies these exactly with the positive point spectrum.

Run `python3 verify.py` with Python 3. The script uses only the standard library and performs exact polynomial-algebra verification plus separate representative numerical checks of a direct six-by-six Bloch boundary matrix. Expected output begins with `VERIFY_OK: exact polynomial factorization` and ends with `VERIFY_OK: direct Bloch matrix finite sanity checks`.

The numerical determinant checks only test selected phases and are not completeness certificates. Completeness is given by the analytic Bloch-coefficient argument. The 2024 journal-version full text was not available for comparison, and independent audit has not been performed.
