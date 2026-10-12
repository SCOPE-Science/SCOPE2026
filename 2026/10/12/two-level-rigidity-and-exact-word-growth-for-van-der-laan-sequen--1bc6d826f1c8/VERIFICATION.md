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

# Verification of two-level Van der Laan rigidity and growth

Run `python3 verify.py` with Python 3.8 or later. No third-party packages, internet connection or externally stored intermediate files are required.

The verifier constructs the complete adjacency matrix directly from the allowed binary four-blocks, checks every binary word at lengths \(0\) through \(13\) against direct max/min evaluation, computes the characteristic polynomial using exact integer Newton identities, and checks the claimed rational generating function at 120 successive coefficients. It also independently enumerates zero-and-positive-word possibilities through length \(11\), checks all pertinent local two-symbol cases, verifies strong connectivity of the seven active states and the explicit return cycles of lengths three and four, and brackets the stated positive root numerically. The recorded output is in `verify_output.txt`.

The unrestricted existence/classification result is proved by the full local-multiplicity argument; the rational generating function comes from the displayed exact finite matrix resolvent. Finite word enumeration does not establish an unrestricted infinite sequence claim. The spectral statement uses the standard Perron–Frobenius theorem on the explicitly primitive essential state graph. No independent audit has been performed.
