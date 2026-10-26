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
# Reproduction and limits

Run `python3 verification/check.py` using a standard CPython installation. No third-party packages or source downloads are needed. The checker computes the four-stage composition with `fractions.Fraction`, verifies the second-order characteristic identities, brackets the unique threshold at high decimal precision, and samples 600 stable negative steps for spectral and sign-transition checks. A replay of the packaged file returned `VERIFY_OK 2229`, with \(z_*=-3.762080033887951242488783736580249799942429593\ldots\). The infinite sign classification, strict monotonicity, and logarithmic delay are proved in `RESULT.md`; finite numerical tests do not certify them independently.
