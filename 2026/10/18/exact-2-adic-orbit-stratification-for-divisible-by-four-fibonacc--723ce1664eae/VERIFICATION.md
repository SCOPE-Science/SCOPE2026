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

Run `python3 verify.py` using the standalone artifact provided with this statement. The expected terminal line begins with `VERIFY_OK`.

The verifier performs 144 full state-orbit enumerations: for each of 18 nonzero coefficients divisible by four (including negative coefficients) and \(1\le k\le8\), it counts all cycles by their exact lengths and compares with the mathematical classification. It also computes exact integer companion-matrix powers, divides each entry of \(M^{2^j}-I\) by its prescribed power of two, and checks the normalized determinant is odd for \(1\le j\le8\). The script makes no network calls, downloads, or external-package imports.

These finite checks are corroborative and do not establish the theorem for arbitrary modulus exponents or coefficients. The proof of all-exponents validity is the integral matrix identity, two-adic induction, Smith invariant factors and exact orbit counting in `RESULT.md`. Scholarly novelty remains subject to the stated accessible-literature limits. No independent audit has been carried out.
