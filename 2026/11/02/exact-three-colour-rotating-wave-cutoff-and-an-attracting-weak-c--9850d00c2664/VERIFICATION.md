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

# Reproducibility and verification

Run `python verification.py` using Python 3.10+ and SymPy. The checker executes symbolic polynomial identities, an exact discriminant and a fixed-point resultant, exact moving-frame characteristic polynomial coefficients, three signed root enclosures, and five strict Schur inequalities for the actual claimed wave. Its interval comparisons rely exclusively on rational inequalities enclosing \(\sqrt{543}\). The proof of parameter-wide branch counts is algebraic; finite parameter sampling would not suffice.

A successful local run printed PASS and the exact characteristic coefficients. No external independent scientific audit has been performed. No claim of global convergence, complete stable-parameter classification, or higher-site extension is certified.
