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

Reproduce with `python verification_long_window.py` in a directory containing this file and the embedded script. The code uses integer coefficients of independent Bernoulli generating polynomials divided by powers of resolution \(k\), and `Fraction` for all probability tests.

The script independently constructs exact weighted finite-word counts for \(3\le w\le5\), \(2\le k\le5\), all \(1\le m<w\), rational tolerances and lengths \(w\), \(w+1\), \(w+2\). It checks all finite bounds and zero-plateau identities for 291 cases. It separately checks the closed first-threshold count at \(3\le k\le6\), \(3\le w\le6\), all \(1\le m<w\), and lengths \(w\), \(w+1\), \(w+3\) for 168 cases. The embedded output records `VERIFY_OK` and `ONSET_VERIFY_OK`. These tests do not exhaust all parameter values or establish the asymptotic theorem; that follows from the mathematical proof.
