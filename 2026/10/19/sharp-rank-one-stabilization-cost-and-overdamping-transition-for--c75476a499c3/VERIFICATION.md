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

# Verification details

The attached `VERIFY.py` uses only the Python 3 standard library. Running `python3 VERIFY.py` after extracting all files to one directory produces `CHECKS_PASSED 39823`.

The exact rational checker verifies the rank-one coordinate invariants, the characteristic determinant formula, the explicit boundary matrices across zero/weak/equal/strong rotation cases, the spectral trace/determinant conditions, strict-margin approximations, symmetric damping thresholds, and overdamping examples. A separate 3,000-case floating-point probe was used as a preliminary sign stress test, but is not a rigorous certificate and is not required for verification.

The proof in RESULT.md establishes every continuous-domain assertion by algebraic identities, monotonicity and the two-dimensional Routh–Hurwitz criterion. Finite arithmetic sampling does not independently certify a theorem on an infinite parameter domain. The primary literature comparison was not an independent priority audit. The full text of the 2017 SIAM paper was inaccessible after lawful open-source attempts and an institutional-access attempt could not proceed, so equivalent earlier formulas cannot be categorically excluded. No external independent review has occurred.
